# Ansible 12 Release Notes

This changelog describes changes since Ansible 11\.0\.0\.

- <a href="#v12-0-0rc1">v12\.0\.0rc1</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v12-0-0a9">v12\.0\.0a9</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v12-0-0a8">v12\.0\.0a8</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#changed-collections-2">Changed Collections</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>
- <a href="#v12-0-0a7">v12\.0\.0a7</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#changed-collections-3">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#known-issues-1">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-3">Unchanged Collections</a>
- <a href="#v12-0-0a6">v12\.0\.0a6</a>
    - <a href="#release-summary-4">Release Summary</a>
    - <a href="#added-collections-1">Added Collections</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#changed-collections-4">Changed Collections</a>
    - <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#new-modules-3">New Modules</a>
    - <a href="#unchanged-collections-4">Unchanged Collections</a>
- <a href="#v12-0-0a5">v12\.0\.0a5</a>
    - <a href="#release-summary-5">Release Summary</a>
    - <a href="#ansible-core-13">Ansible\-core</a>
    - <a href="#changed-collections-5">Changed Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-2">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated-1">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#known-issues-2">Known Issues</a>
    - <a href="#new-plugins-1">New Plugins</a>
    - <a href="#new-modules-4">New Modules</a>
    - <a href="#unchanged-collections-5">Unchanged Collections</a>
- <a href="#v12-0-0a4">v12\.0\.0a4</a>
    - <a href="#release-summary-6">Release Summary</a>
    - <a href="#ansible-core-17">Ansible\-core</a>
    - <a href="#changed-collections-6">Changed Collections</a>
    - <a href="#major-changes-3">Major Changes</a>
    - <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#new-modules-5">New Modules</a>
    - <a href="#unchanged-collections-6">Unchanged Collections</a>
- <a href="#v12-0-0a3">v12\.0\.0a3</a>
    - <a href="#release-summary-7">Release Summary</a>
    - <a href="#ansible-core-20">Ansible\-core</a>
    - <a href="#changed-collections-7">Changed Collections</a>
    - <a href="#major-changes-4">Major Changes</a>
    - <a href="#minor-changes-7">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-3">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated-2">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes-7">Bugfixes</a>
    - <a href="#known-issues-3">Known Issues</a>
    - <a href="#new-modules-6">New Modules</a>
    - <a href="#unchanged-collections-7">Unchanged Collections</a>
- <a href="#v12-0-0a2">v12\.0\.0a2</a>
    - <a href="#release-summary-8">Release Summary</a>
    - <a href="#ansible-core-24">Ansible\-core</a>
    - <a href="#changed-collections-8">Changed Collections</a>
    - <a href="#major-changes-5">Major Changes</a>
    - <a href="#minor-changes-8">Minor Changes</a>
    - <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#bugfixes-8">Bugfixes</a>
    - <a href="#known-issues-4">Known Issues</a>
    - <a href="#new-plugins-2">New Plugins</a>
    - <a href="#new-modules-7">New Modules</a>
    - <a href="#unchanged-collections-8">Unchanged Collections</a>
- <a href="#v12-0-0a1">v12\.0\.0a1</a>
    - <a href="#release-summary-9">Release Summary</a>
    - <a href="#removed-collections-1">Removed Collections</a>
    - <a href="#added-collections-2">Added Collections</a>
    - <a href="#ansible-core-27">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-6">Major Changes</a>
    - <a href="#minor-changes-9">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-4">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-7">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated-3">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#bugfixes-9">Bugfixes</a>
    - <a href="#known-issues-5">Known Issues</a>
    - <a href="#new-plugins-3">New Plugins</a>
    - <a href="#new-modules-8">New Modules</a>
    - <a href="#unchanged-collections-9">Unchanged Collections</a>

<a id="v12-0-0rc1"></a>
## v12\.0\.0rc1

- <a href="#release-summary">Release Summary</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#community-ciscosmb">community\.ciscosmb</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#community-hashi-vault">community\.hashi\_vault</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-hashi-vault-1">community\.hashi\_vault</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2025\-07\-21

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections"></a>
### Added Collections

* google\.cloud \(version 1\.0\.2\)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 12\.0\.0rc1 contains ansible\-core version 2\.19\.0\.
This is a newer version than version 2\.19\.0rc2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection            | Ansible 12.0.0a9 | Ansible 12.0.0rc1 | Notes                                                                                                                                                                                                        |
| --------------------- | ---------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cisco.meraki          | 2.21.3           | 2.21.4            |                                                                                                                                                                                                              |
| community.ciscosmb    | 1.0.10           | 1.0.11            |                                                                                                                                                                                                              |
| community.crypto      | 3.0.0            | 3.0.1             |                                                                                                                                                                                                              |
| community.dns         | 3.2.5            | 3.2.6             |                                                                                                                                                                                                              |
| community.hashi_vault | 6.2.0            | 6.2.1             |                                                                                                                                                                                                              |
| cyberark.conjur       | 1.3.3            | 1.3.6             | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| google.cloud          |                  | 1.0.2             | The collection was added to Ansible                                                                                                                                                                          |

<a id="minor-changes"></a>
### Minor Changes

<a id="community-ciscosmb"></a>
#### community\.ciscosmb

* Update modules to conform core 2\.19 and templating changes
* solves

<a id="deprecated-features"></a>
### Deprecated Features

<a id="community-hashi-vault"></a>
#### community\.hashi\_vault

* ansible\-core \- support for several <code>ansible\-core</code> versions will be dropped in <code>v7\.0\.0</code>\. The collection will focus on current supported versions of <code>ansible\-core</code> going forward and more agressively drop end\-of\-life or soon\-to\-be EOL versions \([https\://docs\.ansible\.com/ansible/devel/reference\_appendices/release\_and\_maintenance\.html](https\://docs\.ansible\.com/ansible/devel/reference\_appendices/release\_and\_maintenance\.html)\)\.
* python \- support for several <code>python</code> versions will be dropped in <code>v7\.0\.0</code>\. The collection will focus on <code>python</code> versions that are supported by the active versions of <code>ansible\-core</code> on the controller side at a minimum\, and some subset of target versions \([https\://docs\.ansible\.com/ansible/devel/reference\_appendices/release\_and\_maintenance\.html](https\://docs\.ansible\.com/ansible/devel/reference\_appendices/release\_and\_maintenance\.html)\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="cisco-meraki"></a>
#### cisco\.meraki

* cisco\.meraki\.networks\_appliance\_traffic\_shaping\_uplink\_bandwidth \- fix idempotency error\.

<a id="community-crypto"></a>
#### community\.crypto

* openssl\_csr and openssl\_csr\_pipe \- the idempotency check for <code>key\_usage</code> resulted in a crash if <code>Key Agreement</code>/<code>keyAgreement</code> was not set \([https\://github\.com/ansible\-collections/community\.crypto/issues/934](https\://github\.com/ansible\-collections/community\.crypto/issues/934)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/935](https\://github\.com/ansible\-collections/community\.crypto/pull/935)\)\.

<a id="community-dns"></a>
#### community\.dns

* Update Public Suffix List\.
* hetzner\_dns\_records inventory plugin \- avoid using deprecated option when templating options \([https\://github\.com/ansible\-collections/community\.dns/pull/266](https\://github\.com/ansible\-collections/community\.dns/pull/266)\)\.
* hosttech\_dns\_records inventory plugin \- avoid using deprecated option when templating options \([https\://github\.com/ansible\-collections/community\.dns/pull/266](https\://github\.com/ansible\-collections/community\.dns/pull/266)\)\.

<a id="community-hashi-vault-1"></a>
#### community\.hashi\_vault

* connection\_options \- the <code>validate\_certs</code> option had no effect if the <code>retries</code> option was set\. Fix now also sets the parameter correctly in the retry request session \([https\://github\.com/ansible\-collections/community\.hashi\_vault/issues/461](https\://github\.com/ansible\-collections/community\.hashi\_vault/issues/461)\)\.

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.0\)
* ansible\.netcommon \(still version 8\.0\.1\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.1\.0\)
* arista\.eos \(still version 11\.0\.1\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.6\.0\)
* check\_point\.mgmt \(still version 6\.4\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.dnac \(still version 6\.36\.0\)
* cisco\.intersight \(still version 2\.1\.0\)
* cisco\.ios \(still version 10\.1\.1\)
* cisco\.iosxr \(still version 11\.1\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.2\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 5\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.1\)
* community\.aws \(still version 10\.0\.0\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.docker \(still version 4\.6\.1\)
* community\.general \(still version 11\.0\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hrobot \(still version 2\.5\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.4\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 3\.14\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.1\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.5\.0\)
* community\.routeros \(still version 3\.8\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.1\.0\)
* community\.vmware \(still version 5\.7\.1\)
* community\.windows \(still version 3\.0\.0\)
* community\.zabbix \(still version 4\.0\.0\)
* containers\.podman \(still version 1\.17\.0\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.openmanage \(still version 9\.12\.2\)
* dellemc\.powerflex \(still version 2\.6\.1\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.37\.1\)
* fortinet\.fortimanager \(still version 2\.10\.0\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.2\)
* hetzner\.hcloud \(still version 5\.1\.0\)
* hitachivantara\.vspone\_block \(still version 3\.5\.1\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.4\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.0\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.ad \(still version 1\.9\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.0\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flasharray \(still version 1\.35\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.3\.0\)
* theforeman\.foreman \(still version 5\.4\.0\)
* vmware\.vmware \(still version 2\.2\.0\)
* vmware\.vmware\_rest \(still version 4\.8\.1\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a9"></a>
## v12\.0\.0a9

- <a href="#release-summary-1">Release Summary</a>
- <a href="#ansible-core-1">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-proxmox">community\.proxmox</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#vmware-vmware-rest-2">vmware\.vmware\_rest</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#cisco-dnac-1">cisco\.dnac</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-hrobot-1">community\.hrobot</a>
    - <a href="#community-proxmox-1">community\.proxmox</a>
    - <a href="#f5networks-f5-modules">f5networks\.f5\_modules</a>
    - <a href="#vmware-vmware-rest-3">vmware\.vmware\_rest</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#community-hrobot-2">community\.hrobot</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#community-proxmox-2">community\.proxmox</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2025\-07\-09

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-1"></a>
### Ansible\-core

Ansible 12\.0\.0a9 contains ansible\-core version 2\.19\.0rc2\.
This is a newer version than version 2\.19\.0rc1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection            | Ansible 12.0.0a8 | Ansible 12.0.0a9 | Notes |
| --------------------- | ---------------- | ---------------- | ----- |
| ansible.netcommon     | 8.0.0            | 8.0.1            |       |
| arista.eos            | 11.0.0           | 11.0.1           |       |
| cisco.dnac            | 6.35.0           | 6.36.0           |       |
| cisco.ios             | 10.1.0           | 10.1.1           |       |
| cisco.nxos            | 10.1.0           | 10.2.0           |       |
| community.crypto      | 3.0.0-rc1        | 3.0.0            |       |
| community.hrobot      | 2.4.0            | 2.5.0            |       |
| community.proxmox     | 1.0.1            | 1.1.0            |       |
| dellemc.openmanage    | 9.12.1           | 9.12.2           |       |
| f5networks.f5_modules | 1.36.0           | 1.37.1           |       |
| vmware.vmware_rest    | 4.7.0            | 4.8.1            |       |

<a id="major-changes"></a>
### Major Changes

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* idrac\_bios \- This module is enhanced to support iDRAC10\.
* idrac\_diagnostics \- This module is enhanced to support iDRAC10\.
* idrac\_firmware \- This module is enhanced to support iDRAC10\.
* idrac\_job\_queue \- This role is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_logs \- This module is enhanced to support iDRAC10\.
* idrac\_network\_attributes \- This module is enhanced to support iDRAC10\.
* idrac\_secure\_boot \- This module is enhanced to support iDRAC10\.
* idrac\_server\_powerstate \- This role is enhanced to support iDRAC10\.
* idrac\_session \- This module is enhanced to support iDRAC10\.
* idrac\_system\_erase \- This module is enhanced to support iDRAC10\.
* redfish\_event\_subscription \- This module is enhanced to support iDRAC10\.
* redfish\_power\_state \- This module is enhanced to support iDRAC10\.

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* modules \- disable turbo mode for module execution by default\. Make it optional to enable it using an environment variable \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/499](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/499)\)

<a id="minor-changes-1"></a>
### Minor Changes

<a id="cisco-dnac"></a>
#### cisco\.dnac

* Added create in configuration\_template module
* Changes in lan\_automation\_create module
* Update dnacentersdk requirement from 2\.7\.0 to 2\.10\.1

<a id="cisco-nxos"></a>
#### cisco\.nxos

* nxos\_interfaces \- Added service\-policy\, logging\, mac\-address and snmp configuration options for interface\.
* nxos\_l2\_interfaces \- Enhances capability of the module to deal with addition attributes under l2 interfaces\. Adds support for CDP\, Link flap and beacon\.

<a id="community-hrobot"></a>
#### community\.hrobot

* Introduced a new action group \(module defaults group\) <code>community\.hrobot\.api</code> that includes all modules that support the new Hetzner API\. This is currently limited to a subset of the storage box modules\; these currently support both the <code>community\.hrobot\.robot</code> and the new <code>community\.hrobot\.api</code> action group\, and will eventually drop the <code>community\.hrobot\.robot</code> action group once the Robot API for storage boxes is removed by Hetzner \([https\://github\.com/ansible\-collections/community\.hrobot/pull/166](https\://github\.com/ansible\-collections/community\.hrobot/pull/166)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/167](https\://github\.com/ansible\-collections/community\.hrobot/pull/167)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/169](https\://github\.com/ansible\-collections/community\.hrobot/pull/169)\)\.
* storagebox \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/166](https\://github\.com/ansible\-collections/community\.hrobot/pull/166)\)\.
* storagebox\_info \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/166](https\://github\.com/ansible\-collections/community\.hrobot/pull/166)\)\.
* storagebox\_set\_password \- support the new Hetzner API\. Note that the new API does not support setting a random password\; you must always provide a password when using the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\)\.
* storagebox\_snapshot \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\)\.
* storagebox\_snapshot\_info \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\)\.
* storagebox\_snapshot\_plan \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/167](https\://github\.com/ansible\-collections/community\.hrobot/pull/167)\)\.
* storagebox\_snapshot\_plan\_info \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/167](https\://github\.com/ansible\-collections/community\.hrobot/pull/167)\)\.
* storagebox\_subaccount \- no longer mark <code>password\_mode</code> as <code>no\_log</code> \([https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\)\.
* storagebox\_subaccount \- support the new Hetzner API\. Note that the new API does not support setting a random password\; you must always provide a password when using the new API to create a storagebox \([https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\)\.
* storagebox\_subaccount\_info \- support the new Hetzner API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/168](https\://github\.com/ansible\-collections/community\.hrobot/pull/168)\)\.

<a id="community-proxmox"></a>
#### community\.proxmox

* proxmox \- allow force deletion of LXC containers \([https\://github\.com/ansible\-collections/community\.proxmox/pull/105](https\://github\.com/ansible\-collections/community\.proxmox/pull/105)\)\.
* proxmox \- validate the cluster name length \([https\://github\.com/ansible\-collections/community\.proxmox/pull/119](https\://github\.com/ansible\-collections/community\.proxmox/pull/119)\)\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* change cloud\.common dependency to 4\.1 to support anisble 2\.19

<a id="deprecated-features-1"></a>
### Deprecated Features

<a id="ansible-core-2"></a>
#### Ansible\-core

* Jinja test plugins \- Returning a non\-boolean result from a Jinja test plugin is deprecated\.
* YAML parsing \- Usage of the YAML 1\.1 <code>\!\!omap</code> and <code>\!\!pairs</code> tags is deprecated\. Use standard mappings instead\.
* YAML parsing \- Usage of the undocumented <code>\!vault\-encrypted</code> YAML tag is deprecated\. Use <code>\!vault</code> instead\.
* config \- The <code>DEFAULT\_ALLOW\_UNSAFE\_LOOKUPS</code> configuration option is deprecated and no longer has any effect\. Ansible templating no longer encounters situations where use of lookup plugins is considered \"unsafe\"\.
* config \- The <code>DEFAULT\_UNDEFINED\_VAR\_BEHAVIOR</code> configuration option is deprecated and no longer has any effect\. Attempting to use an undefined variable where undefined values are unexpected is now always an error\. This behavior was enabled by default in previous versions\, and disabling it yielded inconsistent results\.
* config \- The <code>STRING\_TYPE\_FILTERS</code> configuration option is deprecated and no longer has any effect\. Since the template engine now always preserves native types\, there is no longer a risk of unintended conversion from strings to native types\.
* config \- Using the <code>DEFAULT\_JINJA2\_EXTENSIONS</code> configuration option to enable Jinja2 extensions is deprecated\. Previously\, custom Jinja extensions were disabled by default\, as they can destabilize the Ansible templating environment\. Templates should only make use of filter\, test and lookup plugins\.
* config \- Using the <code>DEFAULT\_MANAGED\_STR</code> configuration option to customize the value of the <code>ansible\_managed</code> variable is deprecated\. The <code>ansible\_managed</code> variable can now be set the same as any other variable\.
* playbook \- The <code>timedout\.frame</code> task result value \(injected when a task timeout occurs\) is deprecated\. Include <code>error</code> in the <code>DISPLAY\_TRACEBACK</code> config value to capture a full Python traceback for timed out actions\.
* public API \- The <code>ansible\.errors\.AnsibleFilterTypeError</code> exception type has been deprecated\. Use <code>AnsibleTypeError</code> instead\.
* public API \- The <code>ansible\.errors\.\_AnsibleActionDone</code> exception type has been deprecated\. Action plugins should return a task result dictionary in success cases instead of raising\.
* public API \- The <code>ansible\.module\_utils\.common\.json\.json\_dump</code> function is deprecated\. Call Python stdlib <code>json\.dumps</code> instead\, with <code>cls</code> set to an Ansible profile encoder type from <code>ansible\.module\_utils\.common\.json\.get\_encoder</code>\.

<a id="community-crypto-1"></a>
#### community\.crypto

* acme\_certificate \- the option <code>modify\_account</code>\'s default value <code>true</code> has been deprecated\. It will change to <code>false</code> in community\.crypto 4\.0\.0\. We recommend to set the option to an explicit value to avoid deprecation warnings\, and to prefer setting it to <code>false</code> already now\. Better use the <code>community\.crypto\.acme\_account</code> module instead \([https\://github\.com/ansible\-collections/community\.crypto/issues/924](https\://github\.com/ansible\-collections/community\.crypto/issues/924)\)\.

<a id="vmware-vmware-rest-2"></a>
#### vmware\.vmware\_rest

* lookup plugins \- Deprecate all lookup plugins in favor of vmware\.vmware\.moid\_from\_path \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/608](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/608)\)

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* \(\#633\) Fixed typo in ansible\.netcommon\.telnet parameter crlf \(was clrf by mistake\)
* netconf \- Adds check for netconf session\_close RPC happens only if connection is alive\.

<a id="arista-eos"></a>
#### arista\.eos

* Fix route map community handling to include missing community\_attributes level in the dictionary
* Fixed idempotency regarding logging port in differing versions of EOS
* Fixed idempotency when using <em class="title-reference">replaced</em> state on host with multiple ACLs present\.
* Fixed parsing of relative route\-map metric adjustments in when extracting settings from device output\.
* Support colon\-delimited format in BGP community strings
* Update route\_maps to correctly handle ipv6 next\-hop address

<a id="cisco-dnac-1"></a>
#### cisco\.dnac

* Fixed get in sites\_telemetry\_settings module

<a id="cisco-ios"></a>
#### cisco\.ios

* cisco\.ios\.ios\_acls \- Added default acls to not get updated/removed in any state\.
* cisco\.ios\.ios\_hsrp\_interfaces \- Fix module operation around the preempt attributes\, also addressed issues around command ordering\.
* cisco\.ios\.ios\_l3\_interfaces \- Fixed Helper Address command support for l3 interface\.
* cisco\.ios\.ios\_ospfv2 \- Fix ospf admin distance parameter and fix other distance specific attributes to be optional\.
* cisco\.ios\.ios\_vlans \- Fixed errors during VLAN overrides where primary VLANs have private VLAN associations referencing non\-existent or higher VLAN IDs\, ensuring smoother private VLAN handling and preventing module failures\.
* ios\_bgp\_address\_family \- Refined state handling for <em class="title-reference">replaced</em> and <em class="title-reference">overridden</em> modes and enhanced address\-family parsing to accurately differentiate between types such as unicast\, multicast\, and others\.
* ios\_static\_routes \- Add missing interface names in parser
* ios\_vrf\_address\_family \- Added support for parsing the <em class="title-reference">stitching</em> attribute under route targets when gathering facts\. Enhanced handling of <em class="title-reference">import\_config</em> and <em class="title-reference">export</em> and renamed them to <em class="title-reference">imports</em> and <em class="title-reference">exports</em> to consistently represent them as lists of dictionaries during fact collection\.

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* nxos\_acls \- Fix issue where Not sufficient TCAM bank error not being captured by error regex\.

<a id="community-hrobot-1"></a>
#### community\.hrobot

* robot inventory plugin \- avoid using deprecated option when templating options \([https\://github\.com/ansible\-collections/community\.hrobot/pull/165](https\://github\.com/ansible\-collections/community\.hrobot/pull/165)\)\.

<a id="community-proxmox-1"></a>
#### community\.proxmox

* proxmox inventory plugin \- avoid using deprecated option when templating options \([https\://github\.com/ansible\-collections/community\.proxmox/pull/108](https\://github\.com/ansible\-collections/community\.proxmox/pull/108)\)\.

<a id="f5networks-f5-modules"></a>
#### f5networks\.f5\_modules

* bigip\_virtual\_server fix module crash issue

<a id="vmware-vmware-rest-3"></a>
#### vmware\.vmware\_rest

* Allow cloud\.common 5\.0\.0 and later again \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/614](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/614)\)\.

<a id="known-issues"></a>
### Known Issues

<a id="community-hrobot-2"></a>
#### community\.hrobot

* storagebox\* modules \- the Hetzner Robot API for storage boxes is [deprecated and will be sunset on July 30\, 2025](https\://docs\.hetzner\.cloud/changelog\#2025\-06\-25\-new\-api\-for\-storage\-boxes)\. The modules are currently not compatible with the new API\. We will try to adjust them until then\, but usage and return values might change slightly due to differences in the APIs\.
  For the new API\, an API token needs to be registered and provided as <code>hetzner\_token</code> \([https\://github\.com/ansible\-collections/community\.hrobot/pull/166](https\://github\.com/ansible\-collections/community\.hrobot/pull/166)\)\.

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_attributes \- The module accepts both the string as well as integer value for the field \"SNMP\.1\.AgentCommunity\" for iDRAC10\.
* idrac\_diagnostics \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* ome\_smart\_fabric\_uplink \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules"></a>
### New Modules

<a id="community-proxmox-2"></a>
#### community\.proxmox

* community\.proxmox\.proxmox\_access\_acl \- Management of ACLs for objects in Proxmox VE Cluster\.
* community\.proxmox\.proxmox\_cluster\_ha\_groups \- Management of HA groups in Proxmox VE Cluster\.
* community\.proxmox\.proxmox\_cluster\_ha\_resources \- Management of HA groups in Proxmox VE Cluster\.

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.1\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.6\.0\)
* check\_point\.mgmt \(still version 6\.4\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.intersight \(still version 2\.1\.0\)
* cisco\.iosxr \(still version 11\.1\.0\)
* cisco\.meraki \(still version 2\.21\.3\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 5\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.1\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.2\.5\)
* community\.docker \(still version 4\.6\.1\)
* community\.general \(still version 11\.0\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.4\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 3\.14\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.5\.0\)
* community\.routeros \(still version 3\.8\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.1\.0\)
* community\.vmware \(still version 5\.7\.1\)
* community\.windows \(still version 3\.0\.0\)
* community\.zabbix \(still version 4\.0\.0\)
* containers\.podman \(still version 1\.17\.0\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.powerflex \(still version 2\.6\.1\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.10\.0\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.2\)
* hetzner\.hcloud \(still version 5\.1\.0\)
* hitachivantara\.vspone\_block \(still version 3\.5\.1\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.4\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.0\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.ad \(still version 1\.9\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.0\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flasharray \(still version 1\.35\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.3\.0\)
* theforeman\.foreman \(still version 5\.4\.0\)
* vmware\.vmware \(still version 2\.2\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a8"></a>
## v12\.0\.0a8

- <a href="#release-summary-2">Release Summary</a>
- <a href="#ansible-core-3">Ansible\-core</a>
- <a href="#changed-collections-2">Changed Collections</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#containers-podman-1">containers\.podman</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2025\-07\-01

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-3"></a>
### Ansible\-core

Ansible 12\.0\.0a8 contains ansible\-core version 2\.19\.0rc1\.
This is a newer version than version 2\.19\.0b7 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-2"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 12.0.0a7 | Ansible 12.0.0a8 | Notes                                                                                                                        |
| --------------------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| azure.azcollection          | 3.5.0            | 3.6.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| containers.podman           | 1.16.4           | 1.17.0           |                                                                                                                              |
| dellemc.powerflex           | 2.6.0            | 2.6.1            |                                                                                                                              |
| hitachivantara.vspone_block | 3.5.0            | 3.5.1            |                                                                                                                              |

<a id="minor-changes-2"></a>
### Minor Changes

<a id="ansible-core-4"></a>
#### Ansible\-core

* templating \- Relaxed the Jinja sandbox to allow specific bitwise operations which have no filter equivalent\. The allowed methods are <code>\_\_and\_\_</code>\, <code>\_\_lshift\_\_</code>\, <code>\_\_or\_\_</code>\, <code>\_\_rshift\_\_</code>\, <code>\_\_xor\_\_</code>\.
* templating \- Switched from the Jinja immutable sandbox to the standard sandbox\. This restores the ability to use mutation methods such as <code>list\.append</code> and <code>dict\.update</code>\.

<a id="containers-podman"></a>
#### containers\.podman

* Add another test for volumes
* Added checks for volume opts

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added none check for mdm cluster id in mdm\_cluster module\.
* Updated minimum SDK version to 2\.6\.1\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-5"></a>
#### Ansible\-core

* Update automatic role argument spec validation to not use deprecated syntax \([https\://github\.com/ansible/ansible/issues/85399](https\://github\.com/ansible/ansible/issues/85399)\)\.
* ssh connection plugin \- Allow only one password prompt attempt when utilizing <code>SSH\_ASKPASS</code> \([https\://github\.com/ansible/ansible/issues/85359](https\://github\.com/ansible/ansible/issues/85359)\)

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* snapshot\_policy \- Renamed snapshotAccessMode and secureSnapshots to snapshot\_access\_mode and secure\_snapshots respectively\.

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Resolved an issue where adding a path to an external path group for FC and retrieving external path group facts would fail\.

<a id="new-modules-1"></a>
### New Modules

<a id="containers-podman-1"></a>
#### containers\.podman

* containers\.podman\.podman\_system\_info \- Get podman system information from host machine

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.0\)
* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.1\.0\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 6\.4\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.dnac \(still version 6\.35\.0\)
* cisco\.intersight \(still version 2\.1\.0\)
* cisco\.ios \(still version 10\.1\.0\)
* cisco\.iosxr \(still version 11\.1\.0\)
* cisco\.meraki \(still version 2\.21\.3\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.1\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 5\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.1\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.crypto \(still version 3\.0\.0\-rc1\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.2\.5\)
* community\.docker \(still version 4\.6\.1\)
* community\.general \(still version 11\.0\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.4\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.4\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 3\.14\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.5\.0\)
* community\.routeros \(still version 3\.8\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.1\.0\)
* community\.vmware \(still version 5\.7\.1\)
* community\.windows \(still version 3\.0\.0\)
* community\.zabbix \(still version 4\.0\.0\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.openmanage \(still version 9\.12\.1\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.36\.0\)
* fortinet\.fortimanager \(still version 2\.10\.0\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.2\)
* hetzner\.hcloud \(still version 5\.1\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.4\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.0\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.ad \(still version 1\.9\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.0\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flasharray \(still version 1\.35\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.3\.0\)
* theforeman\.foreman \(still version 5\.4\.0\)
* vmware\.vmware \(still version 2\.2\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a7"></a>
## v12\.0\.0a7

- <a href="#release-summary-3">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#ansible-core-6">Ansible\-core</a>
- <a href="#changed-collections-3">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
    - <a href="#vyos-vyos">vyos\.vyos</a>
- <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#cisco-dnac-2">cisco\.dnac</a>
    - <a href="#cloud-common">cloud\.common</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-okd">community\.okd</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#netapp-storagegrid">netapp\.storagegrid</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
    - <a href="#vyos-vyos-1">vyos\.vyos</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#cloud-common-1">cloud\.common</a>
    - <a href="#community-okd-1">community\.okd</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#vyos-vyos-2">vyos\.vyos</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#vyos-vyos-3">vyos\.vyos</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#community-general-2">community\.general</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#community-general-3">community\.general</a>
- <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#netapp-storagegrid-1">netapp\.storagegrid</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
    - <a href="#vyos-vyos-4">vyos\.vyos</a>
- <a href="#known-issues-1">Known Issues</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#vyos-vyos-5">vyos\.vyos</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#callback">Callback</a>
    - <a href="#connection">Connection</a>
    - <a href="#filter">Filter</a>
    - <a href="#inventory">Inventory</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#netapp-storagegrid-2">netapp\.storagegrid</a>
- <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="release-summary-3"></a>
### Release Summary

Release Date\: 2025\-06\-25

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* cisco\.ise \(previously included version\: 2\.10\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="ansible-core-6"></a>
### Ansible\-core

Ansible 12\.0\.0a7 contains ansible\-core version 2\.19\.0b7\.
This is a newer version than version 2\.19\.0b6 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-3"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 12.0.0a6 | Ansible 12.0.0a7 | Notes                                                                                                                        |
| ---------------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ansible.utils          | 5.1.2            | 6.0.0            |                                                                                                                              |
| azure.azcollection     | 3.4.0            | 3.5.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.dnac             | 6.31.3           | 6.35.0           |                                                                                                                              |
| cloud.common           | 4.2.0            | 5.0.0            |                                                                                                                              |
| community.crypto       | 3.0.0-a2         | 3.0.0-rc1        |                                                                                                                              |
| community.dns          | 3.2.4            | 3.2.5            |                                                                                                                              |
| community.general      | 10.7.0           | 11.0.0           |                                                                                                                              |
| community.okd          | 4.0.2            | 5.0.0            |                                                                                                                              |
| community.routeros     | 3.7.0            | 3.8.0            |                                                                                                                              |
| community.sops         | 2.0.5            | 2.1.0            |                                                                                                                              |
| community.vmware       | 5.7.0            | 5.7.1            |                                                                                                                              |
| fortinet.fortimanager  | 2.9.1            | 2.10.0           |                                                                                                                              |
| grafana.grafana        | 6.0.1            | 6.0.2            |                                                                                                                              |
| kubernetes.core        | 5.3.0            | 6.0.0            |                                                                                                                              |
| netapp.storagegrid     | 21.14.0          | 21.15.0          |                                                                                                                              |
| purestorage.flasharray | 1.34.1           | 1.35.1           |                                                                                                                              |
| vmware.vmware          | 2.1.0            | 2.2.0            |                                                                                                                              |
| vyos.vyos              | 5.0.0            | 6.0.0            |                                                                                                                              |

<a id="major-changes-1"></a>
### Major Changes

<a id="ansible-utils"></a>
#### ansible\.utils

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Add delete protection by \@KucicM in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/381](https\://github\.com/grafana/grafana\-ansible\-collection/pull/381)
* Fix Mimir URL verify task by \@parcimonic in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/358](https\://github\.com/grafana/grafana\-ansible\-collection/pull/358)
* Fix some regression introduced by v6 by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/376](https\://github\.com/grafana/grafana\-ansible\-collection/pull/376)
* Update when statement to test for dashboard files found by \@hal58th in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/363](https\://github\.com/grafana/grafana\-ansible\-collection/pull/363)
* Use become false in find task by \@santilococo in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/368](https\://github\.com/grafana/grafana\-ansible\-collection/pull/368)
* alloy\_readiness\_check\_use\_https by \@piotr\-g in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/359](https\://github\.com/grafana/grafana\-ansible\-collection/pull/359)

<a id="vyos-vyos"></a>
#### vyos\.vyos

* bgp modules \- Added support for 1\.4\+ \"system\-as\"\. 1\.3 embedded as\_number is still supported
* vyos bgp modules \- Many configuration attributes moved from <em class="title-reference">bgp\_global</em> to <em class="title-reference">bgp\_address\_family</em> module \(see documentation\)\.
* vyos\_bgp\_address\_family \- Aligned with version 1\.3\+ configuration \- aggregate\_address\, maximum\_paths\, network\, and redistribute moved from <em class="title-reference">bgp\_global</em> module\. These are now Address\-family specific\. Many neighbor attributes also moved from <em class="title-reference">vyos\_bgp\_global</em> to <em class="title-reference">vyos\_bgp\_address\_family</em> module\.
* vyos\_bgp\_global \- Aligned with version 1\.3\+ configuration \- aggregate\_address\, maximum\_paths\, network\, and redistribute Removed to <em class="title-reference">bgp\_address\_family</em> module\.
* vyos\_user \- add support for encrypted password specification
* vyos\_user \- add support for public\-key authentication

<a id="minor-changes-3"></a>
### Minor Changes

<a id="ansible-core-7"></a>
#### Ansible\-core

* Added type annotations to the <code>Role\.\_\_init\_\_\(\)</code> method to enable type checking\. \([https\://github\.com/ansible/ansible/pull/85346](https\://github\.com/ansible/ansible/pull/85346)\)
* ansible\-test \- Added experimental support for remote debugging\.
* ansible\-test \- Added support for setting static environment variables in integration tests using <code>env/set/</code> entries in the <code>aliases</code> file\. For example\, <code>env/set/MY\_KEY/MY\_VALUE</code> or <code>env/set/MY\_PATH//an/abs/path</code>\.
* ansible\-test \- The <code>shell</code> command has been augmented to propagate remote debug configurations and other test\-related settings when running on the controller\. Use the <code>\-\-raw</code> argument to bypass the additional environment configuration\.
* apt \- consider lock timeout while invoking apt\-get command \([https\://github\.com/ansible/ansible/issues/78658](https\://github\.com/ansible/ansible/issues/78658)\)\.
* assemble action added check\_mode support
* display \- The <code>formatted</code> arg to <code>warning</code> has no effect\. Warning wrapping is left to the consumer \(e\.g\. terminal\, browser\)\.
* display \- The <code>wrap\_text</code> and <code>stderr</code> arguments to <code>error</code> have no effect\. Errors are always sent to stderr and wrapping is left to the consumer \(e\.g\. terminal\, browser\)\.
* module\_utils\.basic\.backup\_local enforces check\_mode now
* variables \- Removed restriction on usage of most Python keywords as Ansible variable names\.
* variables \- Warnings about reserved variable names now show context where the variable was defined\.

<a id="cisco-dnac-2"></a>
#### cisco\.dnac

* API Modules 2\_2\_2\_3\, 2\_2\_3\_3\, 2\_3\_3\_0 were removed
* Added \'application\_policy\_workflow\_manager\' for managing queuing profiles\, applications\, sets and policies
* Added \'assurance\_device\_health\_score\_settings\_workflow\_manager\' for managing assurance Health score settings
* Added \'assurance\_icap\_settings\_workflow\_manager\' for configuring and managing ICAP \(Intelligent Capture\) settings
* Added \'assurance\_issue\_workflow\_manager\' for managing assurance global profile settings and issue resolution
* Added \'network\_profile\_switching\_workflow\_manager\' for managing switch profiles
* Added \'network\_profile\_wireless\_workflow\_manager\' for managing network wireless profile
* Added \'path\_trace\_workflow\_manager\' for managing PathTrace settings
* Added \'tags\_workflow\_manager\' for create\, update\, delete Tags and Tag Memberships
* Added \'wireless\_design\_workflow\_manager\' for managing wireless design elements
* Added attribute \'device\_type\' in \'assurance\_issue\_workflow\_manager\' module
* Added attribute \'devices\_maintenance\_schedule\' in \'inventory\_workflow\_manager\' module
* Added attribute \'minimum\_rssi\' in \'wireless\_design\_workflow\_manager\' module
* Added attribute \'resource\_parameters\' and \'copy\_config\' in \'template\_workflow\_manager\' module
* Added attribute \'sda\_fabric\_gateway\_limit\' in \'sda\_fabric\_virtual\_networks\_workflow\_manager\' module
* Added attribute \'ssid\_name\' in \'network\_profile\_wireless\_workflow\_manager\' module
* Added attribute \'sub\_package\_images\' in \'swim\_workflow\_manager\' module
* Added attributes \'ipv4\_total\_addresses\'\, \'ipv4\_unassignable\_addresses\'\, \'ipv4\_assigned\_addresses\'\, \'ipv4\_default\_assigned\_addresses\'\, \'ipv6\_total\_addresses\'\, \'ipv6\_unassignable\_addresses\'\, \'ipv6\_assigned\_addresses\'\, \'ipv6\_default\_assigned\_addresses\' in \'network\_settings\_workflow\_manager\' module
* Added compatibility with Cisco version 3\.1\.3\.0 \-all corresponding modules were added\-\.
* All alias modules were removed  \-\*v1\-\.
* Changes in \'application\_policy\_workflow\_manager\' module
* Changes in \'assurance\_icap\_settings\_workflow\_manager\' module
* Changes in \'assurance\_issue\_workflow\_manager\' module
* Changes in \'device\_configs\_backup\_workflow\_manager\' module
* Changes in \'device\_credential\_backup\_workflow\_manager\' module
* Changes in \'discovery\_workflow\_manager\' module
* Changes in \'events\_and\_notifications\_workflow\_manager\' module
* Changes in \'inventory\_workflow\_manager\' module
* Changes in \'ise\_radius\_integration\_workflow\_manager\' module
* Changes in \'lan\_automation\_workflow\_manager\' module
* Changes in \'network\_compliance\_workflow\_manager\' module
* Changes in \'network\_profile\_switching\_workflow\_manager\' module
* Changes in \'network\_profile\_wireless\_workflow\_manager\' module
* Changes in \'network\_settings\_workflow\_manager\' module
* Changes in \'pnp\_workflow\_manager\' module
* Changes in \'provision\_workflow\_manager\' module
* Changes in \'sda\_extranet\_policies\_workflow\_manager\' module
* Changes in \'sda\_fabric\_devices\_workflow\_manager\' module
* Changes in \'sda\_fabric\_sites\_zones\_workflow\_manager\' module
* Changes in \'sda\_fabric\_transits\_workflow\_manager\' module
* Changes in \'sda\_fabric\_virtual\_networks\_workflow\_manager\' module
* Changes in \'sda\_host\_onboarding\_workflow\_manager\' module
* Changes in \'swim\_workflow\_manager\' module
* Changes in \'tags\_workflow\_manager\' module
* Changes in \'template\_workflow\_manager\' module
* Changes in \'user\_and\_roles\_workflow\_manager\' module
* Changes in \'wireless\_design\_workflow\_manager\' module
* Changes in application\_policy\_workflow\_manager workflow manager module
* Changes in assurance\_device\_health\_score\_settings\_workflow\_manager module
* Changes in assurance\_issue\_workflow\_manager workflow manager module
* Changes in path\_trace\_workflow\_manager module
* Correction of issue 266 in the reserve\_ip\_subpool modules
* New enhancment in template\_workflow\_manager workflow manager module
* Removed attribute \'application\_sets\' and \'application\' in \'application\_policy\_workflow\_manager\' module
* Removed attribute \'control\_path\'  in \'path\_trace\_workflow\_manager\' module
* Removed attribute \'minimum\_rss\' in \'wireless\_design\_workflow\_manager\' module
* Removed attributes \'application\_set\_name\' in \'application\_policy\_workflow\_manager\' module
* Removed attributes \'ssid\'\, \'onboarding\_templates\' in \'network\_profile\_wireless\_workflow\_manager\' module
* changing ansible\.utils 6\.x\.y
* modify problems in requests to the API

<a id="cloud-common"></a>
#### cloud\.common

* Bump version of ansible\-lint to minimum 24\.7\.0 \([https\://github\.com/ansible\-collections/cloud\.common/pull/159](https\://github\.com/ansible\-collections/cloud\.common/pull/159)\)\.

<a id="community-crypto-2"></a>
#### community\.crypto

* Remove various no longer needed abstraction layers for multiple backends \([https\://github\.com/ansible\-collections/community\.crypto/pull/912](https\://github\.com/ansible\-collections/community\.crypto/pull/912)\)\.
* Various code refactorings \([https\://github\.com/ansible\-collections/community\.crypto/pull/905](https\://github\.com/ansible\-collections/community\.crypto/pull/905)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/909](https\://github\.com/ansible\-collections/community\.crypto/pull/909)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/911](https\://github\.com/ansible\-collections/community\.crypto/pull/911)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/913](https\://github\.com/ansible\-collections/community\.crypto/pull/913)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/914](https\://github\.com/ansible\-collections/community\.crypto/pull/914)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/917](https\://github\.com/ansible\-collections/community\.crypto/pull/917)\)\.

<a id="community-general"></a>
#### community\.general

* CmdRunner module utils \- the convenience method <code>cmd\_runner\_fmt\.as\_fixed\(\)</code> now accepts multiple arguments as a list \([https\://github\.com/ansible\-collections/community\.general/pull/9893](https\://github\.com/ansible\-collections/community\.general/pull/9893)\)\.
* MH module utils \- delegate <code>debug</code> to the underlying <code>AnsibleModule</code> instance or issues a warning if an attribute already exists with that name \([https\://github\.com/ansible\-collections/community\.general/pull/9577](https\://github\.com/ansible\-collections/community\.general/pull/9577)\)\.
* alternatives \- add <code>family</code> parameter that allows to utilize the <code>\-\-family</code> option available in RedHat version of update\-alternatives \([https\://github\.com/ansible\-collections/community\.general/issues/5060](https\://github\.com/ansible\-collections/community\.general/issues/5060)\, [https\://github\.com/ansible\-collections/community\.general/pull/9096](https\://github\.com/ansible\-collections/community\.general/pull/9096)\)\.
* apache2\_mod\_proxy \- better handling regexp extraction \([https\://github\.com/ansible\-collections/community\.general/pull/9609](https\://github\.com/ansible\-collections/community\.general/pull/9609)\)\.
* apache2\_mod\_proxy \- change type of <code>state</code> to a list of strings\. No change for the users \([https\://github\.com/ansible\-collections/community\.general/pull/9600](https\://github\.com/ansible\-collections/community\.general/pull/9600)\)\.
* apache2\_mod\_proxy \- code simplification\, no change in functionality \([https\://github\.com/ansible\-collections/community\.general/pull/9457](https\://github\.com/ansible\-collections/community\.general/pull/9457)\)\.
* apache2\_mod\_proxy \- improve readability when using results from <code>fecth\_url\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9608](https\://github\.com/ansible\-collections/community\.general/pull/9608)\)\.
* apache2\_mod\_proxy \- refactor repeated code into method \([https\://github\.com/ansible\-collections/community\.general/pull/9599](https\://github\.com/ansible\-collections/community\.general/pull/9599)\)\.
* apache2\_mod\_proxy \- remove unused parameter and code from <code>Balancer</code> constructor \([https\://github\.com/ansible\-collections/community\.general/pull/9614](https\://github\.com/ansible\-collections/community\.general/pull/9614)\)\.
* apache2\_mod\_proxy \- simplified and improved string manipulation \([https\://github\.com/ansible\-collections/community\.general/pull/9614](https\://github\.com/ansible\-collections/community\.general/pull/9614)\)\.
* apache2\_mod\_proxy \- use <code>deps</code> to handle dependencies \([https\://github\.com/ansible\-collections/community\.general/pull/9612](https\://github\.com/ansible\-collections/community\.general/pull/9612)\)\.
* apache2\_module \- added workaround for new PHP module name\, from <code>php7\_module</code> to <code>php\_module</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9951](https\://github\.com/ansible\-collections/community\.general/pull/9951)\)\.
* bitwarden lookup plugin \- add new option <code>collection\_name</code> to filter results by collection name\, and new option <code>result\_count</code> to validate number of results \([https\://github\.com/ansible\-collections/community\.general/pull/9728](https\://github\.com/ansible\-collections/community\.general/pull/9728)\)\.
* bitwarden lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* cargo \- add <code>features</code> parameter to allow activating specific features when installing Rust packages \([https\://github\.com/ansible\-collections/community\.general/pull/10198](https\://github\.com/ansible\-collections/community\.general/pull/10198)\)\.
* cartesian lookup plugin \- removed compatibility code for ansible\-core \< 2\.14 \([https\://github\.com/ansible\-collections/community\.general/pull/10160](https\://github\.com/ansible\-collections/community\.general/pull/10160)\)\.
* cgroup\_memory\_recap callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* cgroup\_memory\_recap callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* chef\_databag lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* chroot connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* chroot connection plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* chroot connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* cloud\_init\_data\_facts \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* cloudflare\_dns \- add support for <code>comment</code> and <code>tags</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9132](https\://github\.com/ansible\-collections/community\.general/pull/9132)\)\.
* cobbler inventory plugin \- add <code>connection\_timeout</code> option to specify the connection timeout to the cobbler server \([https\://github\.com/ansible\-collections/community\.general/pull/11063](https\://github\.com/ansible\-collections/community\.general/pull/11063)\)\.
* cobbler inventory plugin \- add <code>facts\_level</code> option to allow requesting fully rendered variables for Cobbler systems \([https\://github\.com/ansible\-collections/community\.general/issues/9419](https\://github\.com/ansible\-collections/community\.general/issues/9419)\, [https\://github\.com/ansible\-collections/community\.general/pull/9975](https\://github\.com/ansible\-collections/community\.general/pull/9975)\)\.
* cobbler inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* cobbler inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* cobbler inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* collection\_version lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* consul\_kv lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* consul\_token \- fix idempotency when <code>policies</code> or <code>roles</code> are supplied by name \([https\://github\.com/ansible\-collections/community\.general/issues/9841](https\://github\.com/ansible\-collections/community\.general/issues/9841)\, [https\://github\.com/ansible\-collections/community\.general/pull/9845](https\://github\.com/ansible\-collections/community\.general/pull/9845)\)\.
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
* dependent lookup plugin \- removed compatibility code for ansible\-core \< 2\.14 \([https\://github\.com/ansible\-collections/community\.general/pull/10160](https\://github\.com/ansible\-collections/community\.general/pull/10160)\)\.
* dependent lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* deps module utils \- add <code>deps\.clear\(\)</code> to clear out previously declared dependencies \([https\://github\.com/ansible\-collections/community\.general/pull/9179](https\://github\.com/ansible\-collections/community\.general/pull/9179)\)\.
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
* elastic callback plugin \- instead of trying to extract the ansible\-core version from task data\, use ansible\-core\'s actual version \([https\://github\.com/ansible\-collections/community\.general/pull/10193](https\://github\.com/ansible\-collections/community\.general/pull/10193)\)\.
* elastic callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* etcd lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* etcd3 lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* etcd3 lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* filetree lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* flattened lookup plugin \- removed compatibility code for ansible\-core \< 2\.14 \([https\://github\.com/ansible\-collections/community\.general/pull/10160](https\://github\.com/ansible\-collections/community\.general/pull/10160)\)\.
* from\_csv filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* from\_csv filter plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* from\_ini filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* from\_ini filter plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* funcd connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* funcd connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* git\_config \- remove redundant <code>required\=False</code> from <code>argument\_spec</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10177](https\://github\.com/ansible\-collections/community\.general/pull/10177)\)\.
* github\_app\_access\_token lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* github\_key \- add <code>api\_url</code> parameter to support GitHub Enterprise Server installations \([https\://github\.com/ansible\-collections/community\.general/pull/10191](https\://github\.com/ansible\-collections/community\.general/pull/10191)\)\.
* gitlab\_instance\_variable \- add support for <code>raw</code> variables suboption \([https\://github\.com/ansible\-collections/community\.general/pull/9425](https\://github\.com/ansible\-collections/community\.general/pull/9425)\)\.
* gitlab\_project \- add option <code>build\_timeout</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9960](https\://github\.com/ansible\-collections/community\.general/pull/9960)\)\.
* gitlab\_project\_members \- extend choices parameter <code>access\_level</code> by missing upstream valid value <code>owner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9953](https\://github\.com/ansible\-collections/community\.general/pull/9953)\)\.
* gitlab\_runners inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* gitlab\_runners inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* gitlab\_runners inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* groupby\_as\_dict filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* hashids filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* hiera lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* homebrew \- greatly speed up module when multiple packages are passed in the <code>name</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9181](https\://github\.com/ansible\-collections/community\.general/pull/9181)\)\.
* homebrew \- remove duplicated package name validation \([https\://github\.com/ansible\-collections/community\.general/pull/9076](https\://github\.com/ansible\-collections/community\.general/pull/9076)\)\.
* hpilo\_boot \- add option to get an idempotent behavior while powering on server\, resulting in success instead of failure when using <code>state\: boot\_once</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9646](https\://github\.com/ansible\-collections/community\.general/pull/9646)\)\.
* icinga2 inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* icinga2 inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* idrac\_redfish\_command\, idrac\_redfish\_config\, idrac\_redfish\_info \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* ilo\_redfish\_command\, ilo\_redfish\_config\, ilo\_redfish\_info \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* incus connection plugin \- adds <code>remote\_user</code> and <code>incus\_become\_method</code> parameters for allowing a non\-root user to connect to an Incus instance \([https\://github\.com/ansible\-collections/community\.general/pull/9743](https\://github\.com/ansible\-collections/community\.general/pull/9743)\)\.
* incus connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* incus connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* ini\_file \- modify an inactive option also when there are spaces in front of the comment symbol \([https\://github\.com/ansible\-collections/community\.general/pull/10102](https\://github\.com/ansible\-collections/community\.general/pull/10102)\, [https\://github\.com/ansible\-collections/community\.general/issues/8539](https\://github\.com/ansible\-collections/community\.general/issues/8539)\)\.
* iocage connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* iocage connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* iocage inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* iocage inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* iocage inventory plugin \- the new parameter <code>hooks\_results</code> of the plugin is a list of files inside a jail that provide configuration parameters for the inventory\. The inventory plugin reads the files from the jails and put the contents into the items of created variable <code>iocage\_hooks</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9650](https\://github\.com/ansible\-collections/community\.general/issues/9650)\, [https\://github\.com/ansible\-collections/community\.general/pull/9651](https\://github\.com/ansible\-collections/community\.general/pull/9651)\)\.
* iocage inventory plugin \- the new parameter <code>inventory\_hostname\_tag</code> of the plugin provides the name of the tag in the C\(iocage properties notes\) that contains the jails alias\. The new parameter <code>inventory\_hostname\_required</code>\, if enabled\, makes the tag mandatory \([https\://github\.com/ansible\-collections/community\.general/issues/10206](https\://github\.com/ansible\-collections/community\.general/issues/10206)\, [https\://github\.com/ansible\-collections/community\.general/pull/10207](https\://github\.com/ansible\-collections/community\.general/pull/10207)\)\.
* iocage inventory plugin \- the new parameter <code>sudo</code> of the plugin lets the command <code>iocage list \-l</code> to run as root on the iocage host\. This is needed to get the IPv4 of a running DHCP jail \([https\://github\.com/ansible\-collections/community\.general/issues/9572](https\://github\.com/ansible\-collections/community\.general/issues/9572)\, [https\://github\.com/ansible\-collections/community\.general/pull/9573](https\://github\.com/ansible\-collections/community\.general/pull/9573)\)\.
* iptables\_state action plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* iptables\_state action plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9318](https\://github\.com/ansible\-collections/community\.general/pull/9318)\)\.
* iso\_extract \- adds <code>password</code> parameter that is passed to 7z \([https\://github\.com/ansible\-collections/community\.general/pull/9159](https\://github\.com/ansible\-collections/community\.general/pull/9159)\)\.
* jabber callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* jabber callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* jail connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* jail connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* jc filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* jira \- adds <code>client\_cert</code> and <code>client\_key</code> parameters for supporting client certificate authentification when connecting to Jira \([https\://github\.com/ansible\-collections/community\.general/pull/9753](https\://github\.com/ansible\-collections/community\.general/pull/9753)\)\.
* jira \- transition operation now has <code>status\_id</code> to directly reference wanted transition \([https\://github\.com/ansible\-collections/community\.general/pull/9602](https\://github\.com/ansible\-collections/community\.general/pull/9602)\)\.
* json\_query filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* keep\_keys filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* keycloak \- add an action group for Keycloak modules to allow <code>module\_defaults</code> to be set for Keycloak tasks \([https\://github\.com/ansible\-collections/community\.general/pull/9284](https\://github\.com/ansible\-collections/community\.general/pull/9284)\)\.
* keycloak module\_utils \- user groups can now be referenced by their name\, like <code>staff</code>\, or their path\, like <code>/staff/engineering</code>\. The path syntax allows users to reference subgroups\, which is not possible otherwise \([https\://github\.com/ansible\-collections/community\.general/pull/9898](https\://github\.com/ansible\-collections/community\.general/pull/9898)\)\.
* keycloak\_\* modules \- <code>refresh\_token</code> parameter added\. When multiple authentication parameters are provided \(<code>token</code>\, <code>refresh\_token</code>\, and <code>auth\_username</code>/<code>auth\_password</code>\)\, modules will now automatically retry requests upon authentication errors \(401\)\, using in order the token\, refresh token\, and username/password \([https\://github\.com/ansible\-collections/community\.general/pull/9494](https\://github\.com/ansible\-collections/community\.general/pull/9494)\)\.
* keycloak\_realm \- remove ID requirement when creating a realm to allow Keycloak generating its own realm ID \([https\://github\.com/ansible\-collections/community\.general/pull/9768](https\://github\.com/ansible\-collections/community\.general/pull/9768)\)\.
* keycloak\_user module \- user groups can now be referenced by their name\, like <code>staff</code>\, or their path\, like <code>/staff/engineering</code>\. The path syntax allows users to reference subgroups\, which is not possible otherwise \([https\://github\.com/ansible\-collections/community\.general/pull/9898](https\://github\.com/ansible\-collections/community\.general/pull/9898)\)\.
* keyring lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* known\_hosts \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* ksu become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* ksu become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* lastpass lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* launchd \- add <code>plist</code> option for services such as sshd\, where the plist filename doesn\'t match the service name \([https\://github\.com/ansible\-collections/community\.general/pull/9102](https\://github\.com/ansible\-collections/community\.general/pull/9102)\)\.
* linode inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* linode inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* lists filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* lists\_mergeby filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* lldp \- adds <code>multivalues</code> parameter to control behavior when lldpctl outputs an attribute multiple times \([https\://github\.com/ansible\-collections/community\.general/pull/9657](https\://github\.com/ansible\-collections/community\.general/pull/9657)\)\.
* lmdb\_kv lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* lmdb\_kv lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* locale\_gen \- invert the logic to determine <code>ubuntu\_mode</code>\, making it look first for <code>/etc/locale\.gen</code> \(set <code>ubuntu\_mode</code> to <code>False</code>\) and only then looking for <code>/var/lib/locales/supported\.d/</code> \(set <code>ubuntu\_mode</code> to <code>True</code>\) \([https\://github\.com/ansible\-collections/community\.general/pull/9238](https\://github\.com/ansible\-collections/community\.general/pull/9238)\, [https\://github\.com/ansible\-collections/community\.general/issues/9131](https\://github\.com/ansible\-collections/community\.general/issues/9131)\, [https\://github\.com/ansible\-collections/community\.general/issues/8487](https\://github\.com/ansible\-collections/community\.general/issues/8487)\)\.
* locale\_gen \- new return value <code>mechanism</code> to better express the semantics of the <code>ubuntu\_mode</code>\, with the possible values being either <code>glibc</code> \(<code>ubuntu\_mode\=False</code>\) or <code>ubuntu\_legacy</code> \(<code>ubuntu\_mode\=True</code>\) \([https\://github\.com/ansible\-collections/community\.general/pull/9238](https\://github\.com/ansible\-collections/community\.general/pull/9238)\)\.
* log\_plays callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* log\_plays callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* loganalytics callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* loganalytics callback plugin \- instead of trying to extract the ansible\-core version from task data\, use ansible\-core\'s actual version \([https\://github\.com/ansible\-collections/community\.general/pull/10193](https\://github\.com/ansible\-collections/community\.general/pull/10193)\)\.
* loganalytics callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* logdna callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* logdna callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* logentries callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* logentries callback plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* logentries callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* logstash callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* lvg \- add <code>remove\_extra\_pvs</code> parameter to control if ansible should remove physical volumes which are not in the <code>pvs</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/9698](https\://github\.com/ansible\-collections/community\.general/pull/9698)\)\.
* lxc connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* lxc connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* lxd connection plugin \- adds <code>remote\_user</code> and <code>lxd\_become\_method</code> parameters for allowing a non\-root user to connect to an LXD instance \([https\://github\.com/ansible\-collections/community\.general/pull/9659](https\://github\.com/ansible\-collections/community\.general/pull/9659)\)\.
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
* maven\_artifact \- removed compatibility code for ansible\-core \< 2\.12 \([https\://github\.com/ansible\-collections/community\.general/pull/10192](https\://github\.com/ansible\-collections/community\.general/pull/10192)\)\.
* memcached cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* memcached cache plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9320](https\://github\.com/ansible\-collections/community\.general/pull/9320)\)\.
* merge\_variables lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* nmap inventory plugin \- adds <code>dns\_servers</code> option for specifying DNS servers for name resolution\. Accepts hostnames or IP addresses in the same format as the <code>exclude</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9849](https\://github\.com/ansible\-collections/community\.general/pull/9849)\)\.
* nmap inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* nmap inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* nmap inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* nmcli \- add <code>sriov</code> parameter that enables support for SR\-IOV settings \([https\://github\.com/ansible\-collections/community\.general/pull/9168](https\://github\.com/ansible\-collections/community\.general/pull/9168)\)\.
* nmcli \- add a option <code>fail\_over\_mac</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9570](https\://github\.com/ansible\-collections/community\.general/issues/9570)\, [https\://github\.com/ansible\-collections/community\.general/pull/9571](https\://github\.com/ansible\-collections/community\.general/pull/9571)\)\.
* nmcli \- add support for Infiniband MAC setting when <code>type</code> is <code>infiniband</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9962](https\://github\.com/ansible\-collections/community\.general/pull/9962)\)\.
* nmcli \- adds VRF support with new <code>type</code> value <code>vrf</code> and new <code>slave\_type</code> value <code>vrf</code> as well as new <code>table</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/9658](https\://github\.com/ansible\-collections/community\.general/pull/9658)\, [https\://github\.com/ansible\-collections/community\.general/issues/8014](https\://github\.com/ansible\-collections/community\.general/issues/8014)\)\.
* nmcli \- adds <code>autoconnect\_priority</code> and <code>autoconnect\_retries</code> options to support autoconnect logic \([https\://github\.com/ansible\-collections/community\.general/pull/10134](https\://github\.com/ansible\-collections/community\.general/pull/10134)\)\.
* nrdp callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* nrdp callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* null callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* one\_template \- adds <code>filter</code> option for retrieving templates which are not owned by the user \([https\://github\.com/ansible\-collections/community\.general/pull/9547](https\://github\.com/ansible\-collections/community\.general/pull/9547)\, [https\://github\.com/ansible\-collections/community\.general/issues/9278](https\://github\.com/ansible\-collections/community\.general/issues/9278)\)\.
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
* onepassword lookup plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* onepassword lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* onepassword\_doc lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* onepassword\_ssh\_key \- refactor to move code to lookup class \([https\://github\.com/ansible\-collections/community\.general/pull/9633](https\://github\.com/ansible\-collections/community\.general/pull/9633)\)\.
* online inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* online inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* opennebula inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* opennebula inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* opennebula inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* opentelemetry callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* opentelemetry callback plugin \- instead of trying to extract the ansible\-core version from task data\, use ansible\-core\'s actual version \([https\://github\.com/ansible\-collections/community\.general/pull/10193](https\://github\.com/ansible\-collections/community\.general/pull/10193)\)\.
* opentelemetry callback plugin \- remove code handling Python versions prior to 3\.7 \([https\://github\.com/ansible\-collections/community\.general/pull/9482](https\://github\.com/ansible\-collections/community\.general/pull/9482)\)\.
* opentelemetry callback plugin \- remove code handling Python versions prior to 3\.7 \([https\://github\.com/ansible\-collections/community\.general/pull/9503](https\://github\.com/ansible\-collections/community\.general/pull/9503)\)\.
* opentelemetry callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* pacemaker\_cluster \- remove unused code \([https\://github\.com/ansible\-collections/community\.general/pull/9471](https\://github\.com/ansible\-collections/community\.general/pull/9471)\)\.
* pacemaker\_cluster \- using safer mechanism to run external command \([https\://github\.com/ansible\-collections/community\.general/pull/9471](https\://github\.com/ansible\-collections/community\.general/pull/9471)\)\.
* pacemaker\_resource \- add maintenance mode support for handling resource creation and deletion \([https\://github\.com/ansible\-collections/community\.general/issues/10180](https\://github\.com/ansible\-collections/community\.general/issues/10180)\, [https\://github\.com/ansible\-collections/community\.general/pull/10194](https\://github\.com/ansible\-collections/community\.general/pull/10194)\)\.
* pacman\_key \- support verifying that keys are trusted and not expired \([https\://github\.com/ansible\-collections/community\.general/issues/9949](https\://github\.com/ansible\-collections/community\.general/issues/9949)\, [https\://github\.com/ansible\-collections/community\.general/pull/9950](https\://github\.com/ansible\-collections/community\.general/pull/9950)\)\.
* parted \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* passwordstore lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* pbrun become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pbrun become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* pfexec become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pfexec become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* pickle cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pipx \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9180](https\://github\.com/ansible\-collections/community\.general/pull/9180)\)\.
* pipx \- parameter <code>name</code> now accepts Python package specifiers \([https\://github\.com/ansible\-collections/community\.general/issues/7815](https\://github\.com/ansible\-collections/community\.general/issues/7815)\, [https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pipx module\_utils \- filtering application list by name now happens in the modules \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pipx\_info \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9180](https\://github\.com/ansible\-collections/community\.general/pull/9180)\)\.
* pipx\_info \- filtering application list by name now happens in the module  \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pmrun become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* pmrun become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* pulp\_repo \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* puppet \- improve parameter formatting\, no impact to user \([https\://github\.com/ansible\-collections/community\.general/pull/10014](https\://github\.com/ansible\-collections/community\.general/pull/10014)\)\.
* qubes connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* qubes connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* random\_mac filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* random\_pet lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* redfish module utils \- add <code>REDFISH\_COMMON\_ARGUMENT\_SPEC</code>\, a corresponding <code>redfish</code> docs fragment\, and support for its <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* redfish module utils \- removed compatibility code for ansible\-core \< 2\.14 \([https\://github\.com/ansible\-collections/community\.general/pull/10160](https\://github\.com/ansible\-collections/community\.general/pull/10160)\)\.
* redfish\_command \- add <code>PowerFullPowerCycle</code> to power command options \([https\://github\.com/ansible\-collections/community\.general/pull/9729](https\://github\.com/ansible\-collections/community\.general/pull/9729)\)\.
* redfish\_command \- add <code>update\_custom\_oem\_header</code>\, <code>update\_custom\_oem\_params</code>\, and <code>update\_custom\_oem\_mime\_type</code> options \([https\://github\.com/ansible\-collections/community\.general/pull/9123](https\://github\.com/ansible\-collections/community\.general/pull/9123)\)\.
* redfish\_command\, redfish\_config\, redfish\_info \- add <code>validate\_certs</code> and <code>ca\_path</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* redfish\_config \- add command <code>SetPowerRestorePolicy</code> to set the desired power state of the system when power is restored \([https\://github\.com/ansible\-collections/community\.general/pull/9837](https\://github\.com/ansible\-collections/community\.general/pull/9837)\)\.
* redfish\_info \- add command <code>GetAccountServiceConfig</code> to get full information about AccountService configuration \([https\://github\.com/ansible\-collections/community\.general/pull/9403](https\://github\.com/ansible\-collections/community\.general/pull/9403)\)\.
* redfish\_info \- add command <code>GetPowerRestorePolicy</code> to get the desired power state of the system when power is restored \([https\://github\.com/ansible\-collections/community\.general/pull/9824](https\://github\.com/ansible\-collections/community\.general/pull/9824)\)\.
* redfish\_utils module utils \- remove redundant code \([https\://github\.com/ansible\-collections/community\.general/pull/9190](https\://github\.com/ansible\-collections/community\.general/pull/9190)\)\.
* redhat\_subscription \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* redis cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* redis cache plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* redis cache plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9320](https\://github\.com/ansible\-collections/community\.general/pull/9320)\)\.
* redis lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* remove\_keys filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* replace\_keys filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* revbitspss lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* reveal\_ansible\_type filter plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9585](https\://github\.com/ansible\-collections/community\.general/pull/9585)\)\.
* rocketchat \- fix duplicate JSON conversion for Rocket\.Chat \< 7\.4\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9965](https\://github\.com/ansible\-collections/community\.general/pull/9965)\)\.
* rocketchat \- option <code>is\_pre740</code> has been added to control the format of the payload\. For Rocket\.Chat 7\.4\.0 or newer\, it must be set to <code>false</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9882](https\://github\.com/ansible\-collections/community\.general/pull/9882)\)\.
* rpm\_ostree\_pkg \- added the options <code>apply\_live</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9167](https\://github\.com/ansible\-collections/community\.general/pull/9167)\)\.
* rpm\_ostree\_pkg \- added the return value <code>needs\_reboot</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9167](https\://github\.com/ansible\-collections/community\.general/pull/9167)\)\.
* run0 become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* saltstack connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* saltstack connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* say callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* say callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* scaleway inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* scaleway inventory plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* scaleway inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* scaleway\_lb \- minor simplification in the code \([https\://github\.com/ansible\-collections/community\.general/pull/9189](https\://github\.com/ansible\-collections/community\.general/pull/9189)\)\.
* selective callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* selective callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* sesu become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* sesu become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* shelvefile lookup plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9324](https\://github\.com/ansible\-collections/community\.general/pull/9324)\)\.
* shutdown action plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* shutdown action plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* shutdown action plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9318](https\://github\.com/ansible\-collections/community\.general/pull/9318)\)\.
* slack callback plugin \- add <code>http\_agent</code> option to enable the user to set a custom user agent for slack callback plugin \([https\://github\.com/ansible\-collections/community\.general/issues/9813](https\://github\.com/ansible\-collections/community\.general/issues/9813)\, [https\://github\.com/ansible\-collections/community\.general/pull/9836](https\://github\.com/ansible\-collections/community\.general/pull/9836)\)\.
* slack callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* slack callback plugin \- clean up string conversions \([https\://github\.com/ansible\-collections/community\.general/pull/9379](https\://github\.com/ansible\-collections/community\.general/pull/9379)\)\.
* slack callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* snap \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9598](https\://github\.com/ansible\-collections/community\.general/pull/9598)\)\.
* snap\_alias \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9598](https\://github\.com/ansible\-collections/community\.general/pull/9598)\)\.
* solaris\_zone \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* sorcery \- open file using <code>open\(\)</code> as a context manager \([https\://github\.com/ansible\-collections/community\.general/pull/9579](https\://github\.com/ansible\-collections/community\.general/pull/9579)\)\.
* splunk callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* splunk callback plugin \- instead of trying to extract the ansible\-core version from task data\, use ansible\-core\'s actual version \([https\://github\.com/ansible\-collections/community\.general/pull/10193](https\://github\.com/ansible\-collections/community\.general/pull/10193)\)\.
* splunk callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* ssh\_config \- add <code>dynamicforward</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9192](https\://github\.com/ansible\-collections/community\.general/pull/9192)\)\.
* ssh\_config \- add <code>other\_options</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/8053](https\://github\.com/ansible\-collections/community\.general/issues/8053)\, [https\://github\.com/ansible\-collections/community\.general/pull/9684](https\://github\.com/ansible\-collections/community\.general/pull/9684)\)\.
* stackpath\_compute inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* stackpath\_compute inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* sudosu become plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* sudosu become plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9319](https\://github\.com/ansible\-collections/community\.general/pull/9319)\)\.
* sumologic callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* sumologic callback plugin \- instead of trying to extract the ansible\-core version from task data\, use ansible\-core\'s actual version \([https\://github\.com/ansible\-collections/community\.general/pull/10193](https\://github\.com/ansible\-collections/community\.general/pull/10193)\)\.
* syslog\_json callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* systemd\_info \- add wildcard expression support in <code>unitname</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9821](https\://github\.com/ansible\-collections/community\.general/pull/9821)\)\.
* systemd\_info \- extend support to timer units \([https\://github\.com/ansible\-collections/community\.general/pull/9891](https\://github\.com/ansible\-collections/community\.general/pull/9891)\)\.
* terraform \- adds the <code>no\_color</code> parameter\, which suppresses or allows color codes in stdout from Terraform commands \([https\://github\.com/ansible\-collections/community\.general/pull/10154](https\://github\.com/ansible\-collections/community\.general/pull/10154)\)\.
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
* vmadm \- add new options <code>flexible\_disk\_size</code> and <code>owner\_uuid</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9892](https\://github\.com/ansible\-collections/community\.general/pull/9892)\)\.
* wdc\_redfish\_command\, wdc\_redfish\_info \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* xbps \- add <code>root</code> and <code>repository</code> options to enable bootstrapping new void installations \([https\://github\.com/ansible\-collections/community\.general/pull/9174](https\://github\.com/ansible\-collections/community\.general/pull/9174)\)\.
* xcc\_redfish\_command \- add <code>validate\_certs</code>\, <code>ca\_path</code>\, and <code>ciphers</code> options to configure TLS/SSL \([https\://github\.com/ansible\-collections/community\.general/issues/3686](https\://github\.com/ansible\-collections/community\.general/issues/3686)\, [https\://github\.com/ansible\-collections/community\.general/pull/9964](https\://github\.com/ansible\-collections/community\.general/pull/9964)\)\.
* xen\_orchestra inventory plugin \- add <code>use\_vm\_uuid</code> and <code>use\_host\_uuid</code> boolean options to allow switching over to using VM/Xen name labels instead of UUIDs as item names \([https\://github\.com/ansible\-collections/community\.general/pull/9787](https\://github\.com/ansible\-collections/community\.general/pull/9787)\)\.
* xen\_orchestra inventory plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* xen\_orchestra inventory plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9323](https\://github\.com/ansible\-collections/community\.general/pull/9323)\)\.
* xfconf \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9226](https\://github\.com/ansible\-collections/community\.general/pull/9226)\)\.
* xfconf\_info \- add return value <code>version</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9226](https\://github\.com/ansible\-collections/community\.general/pull/9226)\)\.
* xml \- support adding value of children when creating with subnodes \([https\://github\.com/ansible\-collections/community\.general/pull/8437](https\://github\.com/ansible\-collections/community\.general/pull/8437)\)\.
* yaml cache plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* yaml callback plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9583](https\://github\.com/ansible\-collections/community\.general/pull/9583)\)\.
* yaml callback plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9321](https\://github\.com/ansible\-collections/community\.general/pull/9321)\)\.
* zone connection plugin \- adjust standard preamble for Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9584](https\://github\.com/ansible\-collections/community\.general/pull/9584)\)\.
* zone connection plugin \- use f\-strings instead of interpolations or <code>format</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9322](https\://github\.com/ansible\-collections/community\.general/pull/9322)\)\.
* zypper \- add <code>quiet</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9270](https\://github\.com/ansible\-collections/community\.general/pull/9270)\)\.
* zypper \- add <code>simple\_errors</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/9270](https\://github\.com/ansible\-collections/community\.general/pull/9270)\)\.
* zypper \- adds <code>skip\_post\_errors</code> that allows to skip RPM post\-install errors \(Zypper return code 107\) \([https\://github\.com/ansible\-collections/community\.general/issues/9972](https\://github\.com/ansible\-collections/community\.general/issues/9972)\)\.

<a id="community-okd"></a>
#### community\.okd

* Bump version of ansible\-lint to 25\.1\.2 \([https\://github\.com/openshift/community\.okd/pull/255](https\://github\.com/openshift/community\.okd/pull/255)\)\.
* Bump version of ansible\-lint to minimum 24\.7\.0 \([https\://github\.com/openshift/community\.okd/pull/240](https\://github\.com/openshift/community\.okd/pull/240)\)\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_info\, api\_modify \- add <code>interface ethernet switch port\-isolation</code> which is supported since RouterOS 6\.43 \([https\://github\.com/ansible\-collections/community\.routeros/pull/375](https\://github\.com/ansible\-collections/community\.routeros/pull/375)\)\.
* api\_info\, api\_modify \- add <code>routing bfd configuration</code>\. Officially stabilized BFD support for BGP and OSPF is available since RouterOS 7\.11
  \([https\://github\.com/ansible\-collections/community\.routeros/pull/375](https\://github\.com/ansible\-collections/community\.routeros/pull/375)\)\.
* api\_modify\, api\_info \- support API path <code>ip ipsec mode\-config</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/376](https\://github\.com/ansible\-collections/community\.routeros/pull/376)\)\.

<a id="community-sops"></a>
#### community\.sops

* Now supports specifying SSH private keys for age with the new <code>age\_ssh\_private\_keyfile</code> option \([https\://github\.com/ansible\-collections/community\.sops/pull/241](https\://github\.com/ansible\-collections/community\.sops/pull/241)\)\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Supported new modules in FortiManager 7\.4\.6\, 7\.4\.7\, 7\.6\.3\.

<a id="netapp-storagegrid"></a>
#### netapp\.storagegrid

* na\_sg\_grid\_ha\_group \- added check mode support in the module\.
* na\_sg\_org\_container \- Enhanced the Consistency setting\.
* na\_sg\_org\_container \- new option <em class="title-reference">capacity\_limit</em> added for bucket\, requires storageGRID 11\.9 or later\.

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* purefa\_endpoint \- Converted to REST v2
* purefa\_fleet \- Allows FlashBlades to be added to Fusion fleets if FlashArray is Purity//FA 6\.8\.5 or higher
* purefa\_host \- Hosts can be created in realms and renamed within the same realm
* purefa\_host \- Move function added to allow movement of host to/from realms
* purefa\_inventory \- Added support for capacity down licensing
* purefa\_policy \- Added support change a specific quota rule by name
* purefa\_subnet \- Converted to use REST 2
* purefa\_volume \- Added support for creating volumes in Realms

<a id="vmware-vmware"></a>
#### vmware\.vmware

* Fixed ansible\-lint errors in examples\.
* cluster\_ha \- Add module required\_by rules for admission control arguments that are mentioned in the docs \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/201](https\://github\.com/ansible\-collections/vmware\.vmware/issues/201)\)
* cluster\_ha \- admission\_control\_failover\_level can now always be managed by the user\'s inputs\, and the default value for dedicated\_host policy type is the number of dedicated failover hosts \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/201](https\://github\.com/ansible\-collections/vmware\.vmware/issues/201)\)

<a id="vyos-vyos-1"></a>
#### vyos\.vyos

* README\.md \- Add Communication section with Forum information\.
* vyos\_bgp\_address\_family \- Redistribute\, network stanza \- added support for modifiers \(metric\, backdoor etc as per T6829\)
* vyos\_bgp\_global \- Added support for <em class="title-reference">solo</em> neighbor attribute
* vyos\_config \- block get\_config call if match is set to \"none\"
* vyos\_facts \- added <em class="title-reference">network\_os\_major\_version</em> to facts
* vyos\_firewall\_global \- Added support for input\, output\, and forward chains \(1\.4\+\)
* vyos\_firewall\_global \- Added support for log\-level in state\-policy \(1\.4\+\)
* vyos\_firewall\_global \- with 1\.4\+\, use the the global keyword to define global firewall rules
* vyos\_firewall\_interfaces \- added support for VIF interfaces
* vyos\_firewall\_interfaces \- enable support for 1\.4 firewall
* vyos\_firewall\_interfaces \- expanded firewall interface types to match existing types
* vyos\_firewall\_rules \- Add support for diff mode for rulesets
* vyos\_firewall\_rules \- Added support for 1\.4\+ firewall rules
* vyos\_firewall\_rules \- Fixed comparing of firewall rules
* vyos\_firewall\_rules \- added support for 1\.5\+ firewall <em class="title-reference">match\-ipsec\-in</em>\, <em class="title-reference">match\-ipsec\-out</em>\, <em class="title-reference">match\-none\-in</em>\, <em class="title-reference">match\-none\-out</em>
* vyos\_firewall\_rules \- added support for packet\-length\-exclude for 1\.4\+ and the states
* vyos\_l3\_interfaces \- make l3\_interfaces pick up loopback interfaces
* vyos\_lldp\_global \-  address is now addresses\, with appropriate coercion for existing address keys
* vyos\_ntp\_global \- Added ntp options for 1\.5\+ \(interleave\, ptp\)
* vyos\_ntp\_global \- Added support for VyOS 1\.4\+ \(chronyd vs ntpd\)
* vyos\_ntp\_global \- Added syntax for allow\_client in 1\.4\+
* vyos\_ospf\_interaces \- support for 1\.4 ospf interfaces
* vyos\_ospf\_interfaces \- add support for VyOS 1\.3\- virtual interfaces
* vyos\_ospf\_interfaces \- add support for VyOS 1\.4\+\, which moved interface configuration from the interfaces to ospf/ospfv3 interfaces configuration
* vyos\_route\_maps \- add support for as\-path\-prepend policy option

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="cloud-common-1"></a>
#### cloud\.common

* Remove support for ansible versions greater than <code>2\.19</code> \([https\://github\.com/ansible\-collections/cloud\.common/pull/183](https\://github\.com/ansible\-collections/cloud\.common/pull/183)\)\.

<a id="community-okd-1"></a>
#### community\.okd

* Remove openshift inventory plugin deprecated in 3\.0\.0 \([https\://github\.com/openshift/community\.okd/pull/252](https\://github\.com/openshift/community\.okd/pull/252)\)\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* Remove deprecated <code>k8s</code> invetory plugin \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/867](https\://github\.com/ansible\-collections/kubernetes\.core/pull/867)\)\.
* Remove support for <code>ansible\-core\<2\.16</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/867](https\://github\.com/ansible\-collections/kubernetes\.core/pull/867)\)\.

<a id="vyos-vyos-2"></a>
#### vyos\.vyos

* Removed <em class="title-reference">vyos\_logging</em>\. Use <em class="title-reference">vyos\_logging\_global</em> instead\.
* lldp\_global \- if \"address\" is available\, merge will cause it to be added\, in contrast to the previous behavior where it was replaced\. When used in replace mode\, it will remove any existing addresses and replace them with the new one\.
* vyos\_bgp\_address\_family \- Support for 1\.3\+ VyOS only
* vyos\_bgp\_global \- Support for 1\.3\+ VyOS only
* vyos\_firewall\_rules \- removed p2p options as they have been removed prior to 1\.3 of VyOS
* vyos\_firewall\_rules \- tcp\.flags is now a list with an inversion flag to support 1\.4\+ firewall rules\, but still supports 1\.3\-
* vyos\_lldp\_global \- civic\_address is no longer a valid key \(removed prior to 1\.3\)
* vyos\_logging\_global \- For 1\.4\, <em class="title-reference">protocol</em> is an attribute of the syslog host\, not the facility
* vyos\_snmp\_server \- no longer works with versions prior to 1\.3
* vyos\_snmp\_server \- parameter <em class="title-reference">engine\_id</em> is no longer a <em class="title-reference">user</em> or <em class="title-reference">trap\_target</em> parameter and is now a <em class="title-reference">snmp\_v3</em> parameter
* vyos\_snmp\_server \- parameters <em class="title-reference">encrypted\-key</em> and <em class="title-reference">plaintext\-key</em> are now <em class="title-reference">encrypted\-password</em> and <em class="title-reference">plaintext\-password</em>
* vyos\_user \- explicit support for version 1\.3\+ only
* vyos\_user \- removed level \(and its alias\, role\) they were removed in 1\.3

<a id="deprecated-features-2"></a>
### Deprecated Features

<a id="ansible-core-8"></a>
#### Ansible\-core

* inventory plugins \- Setting invalid Ansible variable names in inventory plugins is deprecated\.
* playbook syntax \- Specifying the task <code>args</code> keyword without a value is deprecated\.
* playbook syntax \- Using <code>key\=value</code> args and the task <code>args</code> keyword on the same task is deprecated\.
* playbook syntax \- Using a mapping with the <code>action</code> keyword is deprecated\. \([https\://github\.com/ansible/ansible/issues/84101](https\://github\.com/ansible/ansible/issues/84101)\)

<a id="community-general-1"></a>
#### community\.general

* MH module utils \- attribute <code>debug</code> definition in subclasses of MH is now deprecated\, as that name will become a delegation to <code>AnsibleModule</code> in community\.general 12\.0\.0\, and any such attribute will be overridden by that delegation in that version \([https\://github\.com/ansible\-collections/community\.general/pull/9577](https\://github\.com/ansible\-collections/community\.general/pull/9577)\)\.
* atomic\_container \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9487](https\://github\.com/ansible\-collections/community\.general/pull/9487)\)\.
* atomic\_host \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9487](https\://github\.com/ansible\-collections/community\.general/pull/9487)\)\.
* atomic\_image \- module is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9487](https\://github\.com/ansible\-collections/community\.general/pull/9487)\)\.
* facter \- module is deprecated and will be removed in community\.general 12\.0\.0\, use <code>community\.general\.facter\_facts</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9451](https\://github\.com/ansible\-collections/community\.general/pull/9451)\)\.
* locale\_gen \- <code>ubuntu\_mode\=True</code>\, or <code>mechanism\=ubuntu\_legacy</code> is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9238](https\://github\.com/ansible\-collections/community\.general/pull/9238)\)\.
* manifold lookup plugin \- plugin is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10028](https\://github\.com/ansible\-collections/community\.general/pull/10028)\)\.
* opkg \- deprecate value <code>\"\"</code> for parameter <code>force</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9172](https\://github\.com/ansible\-collections/community\.general/pull/9172)\)\.
* pipx module\_utils \- function <code>make\_process\_list\(\)</code> is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* profitbricks \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_datacenter \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_nic \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_volume \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* profitbricks\_volume\_attachments \- module is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9733](https\://github\.com/ansible\-collections/community\.general/pull/9733)\)\.
* pure module utils \- the module utils is deprecated and will be removed from community\.general 12\.0\.0\. The modules using this were removed in community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9432](https\://github\.com/ansible\-collections/community\.general/pull/9432)\)\.
* purestorage doc fragments \- the doc fragment is deprecated and will be removed from community\.general 12\.0\.0\. The modules using this were removed in community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9432](https\://github\.com/ansible\-collections/community\.general/pull/9432)\)\.
* redfish\_utils module utils \- deprecate method <code>RedfishUtils\.\_init\_session\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9190](https\://github\.com/ansible\-collections/community\.general/pull/9190)\)\.
* sensu\_check \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_client \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_handler \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_silence \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* sensu\_subscription \- module is deprecated and will be removed in community\.general 13\.0\.0\, use collection <code>sensu\.sensu\_go</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/9483](https\://github\.com/ansible\-collections/community\.general/pull/9483)\)\.
* slack \- the default value <code>auto</code> of the <code>prepend\_hash</code> option is deprecated and will change to <code>never</code> in community\.general 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9443](https\://github\.com/ansible\-collections/community\.general/pull/9443)\)\.
* stackpath\_compute inventory plugin \- plugin is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10026](https\://github\.com/ansible\-collections/community\.general/pull/10026)\)\.
* yaml callback plugin \- deprecate plugin in favor of <code>result\_format\=yaml</code> in plugin <code>ansible\.bulitin\.default</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9456](https\://github\.com/ansible\-collections/community\.general/pull/9456)\)\.
* yaml callback plugin \- the YAML callback plugin was deprecated for removal in community\.general 13\.0\.0\. Since it needs to use ansible\-core internals since ansible\-core 2\.19 that are changing a lot\, we will remove this plugin already from community\.general 12\.0\.0 to ease the maintenance burden \([https\://github\.com/ansible\-collections/community\.general/pull/10213](https\://github\.com/ansible\-collections/community\.general/pull/10213)\)\.

<a id="vyos-vyos-3"></a>
#### vyos\.vyos

* vyos\_bgp\_global \- no\_ipv4\_unicast \- deprecated for use with VyOS 1\.4\+\, use <em class="title-reference">ipv4\_unicast</em> instead
* vyos\_firewall\_interfaces \- deprecated for use with VyOS 1\.4\+\, firewalls are no longer connected directly to interfaces\. See the Firewall Configuration documentation for how to establish a connection betwen the firewall rulesets and the flow\, interface\, or zone\.
* vyos\_lldp\_global \- <em class="title-reference">address</em> is deprecated\, use <em class="title-reference">addresses</em> instead\. To be removed in 7\.0\.0\.
* vyos\_logging\_global \- <em class="title-reference">protocol</em> is deprecated for 1\.4 and later\, use <em class="title-reference">facility</em> instead\. To be removed in next major version where supprot for 1\.3 is removed

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The <code>cisco\.ise</code> collection was considered unmaintained and has been removed from Ansible 12 \([https\://forum\.ansible\.com/t/43367](https\://forum\.ansible\.com/t/43367)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install cisco\.ise</code>\.

<a id="community-general-2"></a>
#### community\.general

* Dropped support for ansible\-core 2\.15\. The collection now requires ansible\-core 2\.16 or newer\. This means that on the controller\, Python 3\.10\+ is required\. On the target side\, Python 2\.7 and Python 3\.6\+ are supported \([https\://github\.com/ansible\-collections/community\.general/pull/10160](https\://github\.com/ansible\-collections/community\.general/pull/10160)\, [https\://github\.com/ansible\-collections/community\.general/pull/10192](https\://github\.com/ansible\-collections/community\.general/pull/10192)\)\.
* The Proxmox content \(modules and plugins\) has been moved to the [new collection community\.proxmox](https\://github\.com/ansible\-collections/community\.proxmox)\. Since community\.general 11\.0\.0\, these modules and plugins have been replaced by deprecated redirections to community\.proxmox\. You need to explicitly install community\.proxmox\, for example with <code>ansible\-galaxy collection install community\.proxmox</code>\, or by installing a new enough version of the Ansible community package\. We suggest to update your roles and playbooks to use the new FQCNs as soon as possible to avoid getting deprecation messages \([https\://github\.com/ansible\-collections/community\.general/pull/10110](https\://github\.com/ansible\-collections/community\.general/pull/10110)\)\.
* apt\_rpm \- the <code>present</code> and <code>installed</code> states are no longer equivalent to <code>latest</code>\, but to <code>present\_not\_latest</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* clc\_\* modules and doc fragment \- the modules were removed since CenturyLink Cloud services went EOL in September 2023 \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* django\_manage \- the <code>ack\_venv\_creation\_deprecation</code> option has been removed\. It had no effect anymore anyway \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* git\_config \- it is no longer allowed to use <code>state\=present</code> with no value to read the config value\. Use the <code>community\.general\.git\_config\_info</code> module instead \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* git\_config \- the <code>list\_all</code> option has been removed\. Use the <code>community\.general\.git\_config\_info</code> module instead \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* hipchat \- the module was removed since the hipchat service has been discontinued and the self\-hosted variant has been End of Life since 2020 \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* manifold lookup plugin \- the plugin was removed since the company was acquired in 2021 and service was ceased afterwards \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* mh\.mixins\.deps module utils \- this module utils has been removed\. Use the <code>deps</code> module utils instead \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* mh\.mixins\.vars module utils \- this module utils has been removed\. Use <code>VarDict</code> from the <code>vardict</code> module utils instead \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* mh\.module\_helper module utils \- <code>AnsibleModule</code> and <code>VarsMixin</code> are no longer provided \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* mh\.module\_helper module utils \- <code>VarDict</code> is now imported from the <code>vardict</code> module utils and no longer from the removed <code>mh\.mixins\.vars</code> module utils \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* mh\.module\_helper module utils \- the attributes <code>use\_old\_vardict</code> and <code>mute\_vardict\_deprecation</code> from <code>ModuleHelper</code> have been removed\. We suggest to remove them from your modules if you no longer support community\.general \< 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* module\_helper module utils \- <code>StateMixin</code>\, <code>DependencyCtxMgr</code>\, <code>VarMeta</code>\, <code>VarDict</code>\, and <code>VarsMixin</code> are no longer provided \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* pipx \- module no longer supports <code>pipx</code> older than 1\.7\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10137](https\://github\.com/ansible\-collections/community\.general/pull/10137)\)\.
* pipx\_info \- module no longer supports <code>pipx</code> older than 1\.7\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10137](https\://github\.com/ansible\-collections/community\.general/pull/10137)\)\.
* profitbrick\* modules \- the modules were removed since the supporting library is unsupported since 2021 \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* redfish\_utils module utils \- the <code>\_init\_session</code> method has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.
* stackpath\_compute inventory plugin \- the plugin was removed since the company and the service were sunset in June 2024 \([https\://github\.com/ansible\-collections/community\.general/pull/10126](https\://github\.com/ansible\-collections/community\.general/pull/10126)\)\.

<a id="security-fixes"></a>
### Security Fixes

<a id="community-general-3"></a>
#### community\.general

* keycloak\_authentication \- API calls did not properly set the <code>priority</code> during update resulting in incorrectly sorted authentication flows\. This apparently only affects Keycloak 25 or newer \([https\://github\.com/ansible\-collections/community\.general/pull/9263](https\://github\.com/ansible\-collections/community\.general/pull/9263)\)\.
* keycloak\_client \- Sanitize <code>saml\.encryption\.private\.key</code> so it does not show in the logs \([https\://github\.com/ansible\-collections/community\.general/pull/9621](https\://github\.com/ansible\-collections/community\.general/pull/9621)\)\.

<a id="bugfixes-3"></a>
### Bugfixes

<a id="ansible-core-9"></a>
#### Ansible\-core

* ansible\-test \- Fix Python relative import resolution from <code>\_\_init\_\_\.py</code> files when using change detection\.
* callback plugins \- A more descriptive error is now raised if the stdout callback plugin cannot be loaded\.
* callback plugins \- Callback plugins that do not extend <code>ansible\.plugins\.callback\.CallbackBase</code> will fail to load with a warning\. If the plugin is used as the stdout callback plugin\, this will also be a fatal error\.
* callback plugins \- Removed unused methods \- runner\_on\_no\_hosts\, playbook\_on\_setup\, playbook\_on\_import\_for\_host\, playbook\_on\_not\_import\_for\_host\, v2\_playbook\_on\_cleanup\_task\_start\, v2\_playbook\_on\_import\_for\_host\, v2\_playbook\_on\_not\_import\_for\_host\.
* callback plugins \- The stdout callback plugin is no longer called twice if it is also in the list of additional callback plugins\.
* password lookup \- fix acquiring the lock when human\-readable FileExistsError error message is not English\.
* plugin loader \- A warning is now emitted for any plugin which fails to load due to a missing base class\.
* variables \- Added Jinja scalar singletons \(<code>true</code>\, <code>false</code>\, <code>none</code>\) to invalid Ansible variable name detection\. Previously\, variables with these names could be assigned without error\, but could not be resolved\.

<a id="community-crypto-3"></a>
#### community\.crypto

* acme\_account \- make work with CAs that do not accept any account request without External Account Binding data \([https\://github\.com/ansible\-collections/community\.crypto/issues/918](https\://github\.com/ansible\-collections/community\.crypto/issues/918)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/919](https\://github\.com/ansible\-collections/community\.crypto/pull/919)\)\.
* openssl\_csr\, openssl\_csr\_pipe \- avoid accessing internal members of cryptography\'s <code>KeyUsage</code> extension object \([https\://github\.com/ansible\-collections/community\.crypto/pull/910](https\://github\.com/ansible\-collections/community\.crypto/pull/910)\)\.

<a id="community-dns-1"></a>
#### community\.dns

* Update Public Suffix List\.
* lookup and lookup\_as\_dict lookup plugins \- removed type <code>ALL</code>\, which never worked \([https\://github\.com/ansible\-collections/community\.dns/issues/264](https\://github\.com/ansible\-collections/community\.dns/issues/264)\, [https\://github\.com/ansible\-collections/community\.dns/pull/265](https\://github\.com/ansible\-collections/community\.dns/pull/265)\)\.

<a id="community-general-4"></a>
#### community\.general

* apache2\_mod\_proxy \- make compatible with Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/9762](https\://github\.com/ansible\-collections/community\.general/pull/9762)\)\.
* apache2\_mod\_proxy \- passing the cluster\'s page as referer for the member\'s pages\. This makes the module actually work again for halfway modern Apache versions\. According to some comments founds on the net the referer was required since at least 2019 for some versions of Apache 2 \([https\://github\.com/ansible\-collections/community\.general/pull/9762](https\://github\.com/ansible\-collections/community\.general/pull/9762)\)\.
* cloudflare\_dns \- fix crash when deleting a DNS record or when updating a record with <code>solo\=true</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9652](https\://github\.com/ansible\-collections/community\.general/issues/9652)\, [https\://github\.com/ansible\-collections/community\.general/pull/9649](https\://github\.com/ansible\-collections/community\.general/pull/9649)\)\.
* cloudlare\_dns \- handle exhausted response stream in case of HTTP errors to show nice error message to the user \([https\://github\.com/ansible\-collections/community\.general/issues/9782](https\://github\.com/ansible\-collections/community\.general/issues/9782)\, [https\://github\.com/ansible\-collections/community\.general/pull/9818](https\://github\.com/ansible\-collections/community\.general/pull/9818)\)\.
* cobbler\_system \- fix bug with Cobbler \>\= 3\.4\.0 caused by giving more than 2 positional arguments to <code>CobblerXMLRPCInterface\.get\_system\_handle\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8506](https\://github\.com/ansible\-collections/community\.general/issues/8506)\, [https\://github\.com/ansible\-collections/community\.general/pull/10145](https\://github\.com/ansible\-collections/community\.general/pull/10145)\)\.
* cobbler\_system \- update minimum version number to avoid wrong comparisons that happen in some cases using LooseVersion class which results in TypeError \([https\://github\.com/ansible\-collections/community\.general/issues/8506](https\://github\.com/ansible\-collections/community\.general/issues/8506)\, [https\://github\.com/ansible\-collections/community\.general/pull/10145](https\://github\.com/ansible\-collections/community\.general/pull/10145)\, [https\://github\.com/ansible\-collections/community\.general/pull/10178](https\://github\.com/ansible\-collections/community\.general/pull/10178)\)\.
* dependent look plugin \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* dig lookup plugin \- correctly handle <code>NoNameserver</code> exception \([https\://github\.com/ansible\-collections/community\.general/pull/9363](https\://github\.com/ansible\-collections/community\.general/pull/9363)\, [https\://github\.com/ansible\-collections/community\.general/issues/9362](https\://github\.com/ansible\-collections/community\.general/issues/9362)\)\.
* diy callback plugin \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* dnf\_config\_manager \- fix hanging when prompting to import GPG keys \([https\://github\.com/ansible\-collections/community\.general/pull/9124](https\://github\.com/ansible\-collections/community\.general/pull/9124)\, [https\://github\.com/ansible\-collections/community\.general/issues/8830](https\://github\.com/ansible\-collections/community\.general/issues/8830)\)\.
* dnf\_config\_manager \- forces locale to <code>C</code> before module starts\. If the locale was set to non\-English\, the output of the <code>dnf config\-manager</code> could not be parsed \([https\://github\.com/ansible\-collections/community\.general/pull/9157](https\://github\.com/ansible\-collections/community\.general/pull/9157)\, [https\://github\.com/ansible\-collections/community\.general/issues/9046](https\://github\.com/ansible\-collections/community\.general/issues/9046)\)\.
* dnf\_versionlock \- add support for dnf5 \([https\://github\.com/ansible\-collections/community\.general/issues/9556](https\://github\.com/ansible\-collections/community\.general/issues/9556)\)\.
* elasticsearch\_plugin \- fix <code>ERROR\: D is not a recognized option</code> issue when configuring proxy settings \([https\://github\.com/ansible\-collections/community\.general/pull/9774](https\://github\.com/ansible\-collections/community\.general/pull/9774)\, [https\://github\.com/ansible\-collections/community\.general/issues/9773](https\://github\.com/ansible\-collections/community\.general/issues/9773)\)\.
* flatpak \- force the locale language to <code>C</code> when running the flatpak command \([https\://github\.com/ansible\-collections/community\.general/pull/9187](https\://github\.com/ansible\-collections/community\.general/pull/9187)\, [https\://github\.com/ansible\-collections/community\.general/issues/8883](https\://github\.com/ansible\-collections/community\.general/issues/8883)\)\.
* gio\_mime \- fix command line when determining version of <code>gio</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9171](https\://github\.com/ansible\-collections/community\.general/pull/9171)\, [https\://github\.com/ansible\-collections/community\.general/issues/9158](https\://github\.com/ansible\-collections/community\.general/issues/9158)\)\.
* github\_deploy\_key \- check that key really exists on 422 to avoid masking other errors \([https\://github\.com/ansible\-collections/community\.general/issues/6718](https\://github\.com/ansible\-collections/community\.general/issues/6718)\, [https\://github\.com/ansible\-collections/community\.general/pull/10011](https\://github\.com/ansible\-collections/community\.general/pull/10011)\)\.
* github\_key \- in check mode\, a faulty call to <code>\`datetime\.strftime\(\.\.\.\)\`</code> was being made which generated an exception \([https\://github\.com/ansible\-collections/community\.general/issues/9185](https\://github\.com/ansible\-collections/community\.general/issues/9185)\)\.
* gitlab\_group\_access\_token\, gitlab\_project\_access\_token \- fix handling of group and project access tokens for changes in GitLab 17\.10 \([https\://github\.com/ansible\-collections/community\.general/pull/10196](https\://github\.com/ansible\-collections/community\.general/pull/10196)\)\.
* hashids and unicode\_normalize filter plugins \- avoid deprecated <code>AnsibleFilterTypeError</code> on ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/9992](https\://github\.com/ansible\-collections/community\.general/pull/9992)\)\.
* homebrew \- emit a useful error message if <code>brew info</code> reports a package tap is <code>null</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10013](https\://github\.com/ansible\-collections/community\.general/pull/10013)\, [https\://github\.com/ansible\-collections/community\.general/issues/10012](https\://github\.com/ansible\-collections/community\.general/issues/10012)\)\.
* homebrew \- fix crash when package names include tap \([https\://github\.com/ansible\-collections/community\.general/issues/9777](https\://github\.com/ansible\-collections/community\.general/issues/9777)\, [https\://github\.com/ansible\-collections/community\.general/pull/9803](https\://github\.com/ansible\-collections/community\.general/pull/9803)\)\.
* homebrew \- fix incorrect handling of aliased homebrew modules when the alias is requested \([https\://github\.com/ansible\-collections/community\.general/pull/9255](https\://github\.com/ansible\-collections/community\.general/pull/9255)\, [https\://github\.com/ansible\-collections/community\.general/issues/9240](https\://github\.com/ansible\-collections/community\.general/issues/9240)\)\.
* homebrew \- fix incorrect handling of homebrew modules when a tap is requested \([https\://github\.com/ansible\-collections/community\.general/pull/9546](https\://github\.com/ansible\-collections/community\.general/pull/9546)\, [https\://github\.com/ansible\-collections/community\.general/issues/9533](https\://github\.com/ansible\-collections/community\.general/issues/9533)\)\.
* homebrew \- make package name parsing more resilient \([https\://github\.com/ansible\-collections/community\.general/pull/9665](https\://github\.com/ansible\-collections/community\.general/pull/9665)\, [https\://github\.com/ansible\-collections/community\.general/issues/9641](https\://github\.com/ansible\-collections/community\.general/issues/9641)\)\.
* homebrew\_cask \- allow <code>\+</code> symbol in Homebrew cask name validation regex \([https\://github\.com/ansible\-collections/community\.general/pull/9128](https\://github\.com/ansible\-collections/community\.general/pull/9128)\)\.
* homebrew\_cask \- handle unusual brew version strings \([https\://github\.com/ansible\-collections/community\.general/issues/8432](https\://github\.com/ansible\-collections/community\.general/issues/8432)\, [https\://github\.com/ansible\-collections/community\.general/pull/9881](https\://github\.com/ansible\-collections/community\.general/pull/9881)\)\.
* htpasswd \- report changes when file permissions are adjusted \([https\://github\.com/ansible\-collections/community\.general/issues/9485](https\://github\.com/ansible\-collections/community\.general/issues/9485)\, [https\://github\.com/ansible\-collections/community\.general/pull/9490](https\://github\.com/ansible\-collections/community\.general/pull/9490)\)\.
* iocage inventory plugin \- the plugin parses the IP4 tab of the jails list and put the elements into the new variable <code>iocage\_ip4\_dict</code>\. In multiple interface format the variable <code>iocage\_ip4</code> keeps the comma\-separated list of IP4 \([https\://github\.com/ansible\-collections/community\.general/issues/9538](https\://github\.com/ansible\-collections/community\.general/issues/9538)\)\.
* ipa\_host \- module revoked existing host certificates even if <code>user\_certificate</code> was not given \([https\://github\.com/ansible\-collections/community\.general/pull/9694](https\://github\.com/ansible\-collections/community\.general/pull/9694)\)\.
* java\_cert \- the module no longer fails if the optional parameters <code>pkcs12\_alias</code> and <code>cert\_alias</code> are not provided \([https\://github\.com/ansible\-collections/community\.general/pull/9970](https\://github\.com/ansible\-collections/community\.general/pull/9970)\)\.
* kdeconfig \- allow option values beginning with a dash \([https\://github\.com/ansible\-collections/community\.general/issues/10127](https\://github\.com/ansible\-collections/community\.general/issues/10127)\, [https\://github\.com/ansible\-collections/community\.general/pull/10128](https\://github\.com/ansible\-collections/community\.general/pull/10128)\)\.
* keycloak \- update more than 10 sub\-groups \([https\://github\.com/ansible\-collections/community\.general/issues/9690](https\://github\.com/ansible\-collections/community\.general/issues/9690)\, [https\://github\.com/ansible\-collections/community\.general/pull/9692](https\://github\.com/ansible\-collections/community\.general/pull/9692)\)\.
* keycloak module utils \- replaces missing return in get\_role\_composites method which caused it to return None instead of composite roles \([https\://github\.com/ansible\-collections/community\.general/issues/9678](https\://github\.com/ansible\-collections/community\.general/issues/9678)\, [https\://github\.com/ansible\-collections/community\.general/pull/9691](https\://github\.com/ansible\-collections/community\.general/pull/9691)\)\.
* keycloak\_authentication \- fix authentification config duplication for Keycloak \< 26\.2\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/9987](https\://github\.com/ansible\-collections/community\.general/pull/9987)\)\.
* keycloak\_client \- fix and improve existing tests\. The module showed a diff without actual changes\, solved by improving the <code>normalise\_cr\(\)</code> function \([https\://github\.com/ansible\-collections/community\.general/pull/9644](https\://github\.com/ansible\-collections/community\.general/pull/9644)\)\.
* keycloak\_client \- fix diff by removing code that turns the attributes dict which contains additional settings into a list \([https\://github\.com/ansible\-collections/community\.general/pull/9077](https\://github\.com/ansible\-collections/community\.general/pull/9077)\)\.
* keycloak\_client \- fix the idempotency regression by normalizing the Keycloak response for <code>after\_client</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9905](https\://github\.com/ansible\-collections/community\.general/issues/9905)\, [https\://github\.com/ansible\-collections/community\.general/pull/9976](https\://github\.com/ansible\-collections/community\.general/pull/9976)\)\.
* keycloak\_client \- in check mode\, detect whether the lists in before client \(for example redirect URI list\) contain items that the lists in the desired client do not contain \([https\://github\.com/ansible\-collections/community\.general/pull/9739](https\://github\.com/ansible\-collections/community\.general/pull/9739)\)\.
* keycloak\_clientscope \- fix diff and <code>end\_state</code> by removing the code that turns the attributes dict\, which contains additional config items\, into a list \([https\://github\.com/ansible\-collections/community\.general/pull/9082](https\://github\.com/ansible\-collections/community\.general/pull/9082)\)\.
* keycloak\_clientscope\_type \- sort the default and optional clientscope lists to improve the diff \([https\://github\.com/ansible\-collections/community\.general/pull/9202](https\://github\.com/ansible\-collections/community\.general/pull/9202)\)\.
* keycloak\_user\_rolemapping \- fix <code>\-\-diff</code> mode \([https\://github\.com/ansible\-collections/community\.general/issues/10067](https\://github\.com/ansible\-collections/community\.general/issues/10067)\, [https\://github\.com/ansible\-collections/community\.general/pull/10075](https\://github\.com/ansible\-collections/community\.general/pull/10075)\)\.
* lldp \- fix crash caused by certain lldpctl output where an attribute is defined as branch and leaf \([https\://github\.com/ansible\-collections/community\.general/pull/9657](https\://github\.com/ansible\-collections/community\.general/pull/9657)\)\.
* nmcli \- enable changing only the order of DNS servers or search suffixes \([https\://github\.com/ansible\-collections/community\.general/issues/8724](https\://github\.com/ansible\-collections/community\.general/issues/8724)\, [https\://github\.com/ansible\-collections/community\.general/pull/9880](https\://github\.com/ansible\-collections/community\.general/pull/9880)\)\.
* onepassword\_doc lookup plugin \- ensure that 1Password Connect support also works for this plugin \([https\://github\.com/ansible\-collections/community\.general/pull/9625](https\://github\.com/ansible\-collections/community\.general/pull/9625)\)\.
* passwordstore lookup plugin \- fix subkey creation even when <code>create\=false</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9105](https\://github\.com/ansible\-collections/community\.general/issues/9105)\, [https\://github\.com/ansible\-collections/community\.general/pull/9106](https\://github\.com/ansible\-collections/community\.general/pull/9106)\)\.
* pickle cache plugin \- avoid extra JSON serialization with ansible\-core \>\= 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/10136](https\://github\.com/ansible\-collections/community\.general/pull/10136)\)\.
* pipx \- honor option <code>global</code> when <code>state\=latest</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9623](https\://github\.com/ansible\-collections/community\.general/pull/9623)\)\.
* qubes connection plugin \- fix the printing of debug information \([https\://github\.com/ansible\-collections/community\.general/pull/9334](https\://github\.com/ansible\-collections/community\.general/pull/9334)\)\.
* redfish\_utils module utils \- Fix <code>VerifyBiosAttributes</code> command on multi system resource nodes \([https\://github\.com/ansible\-collections/community\.general/pull/9234](https\://github\.com/ansible\-collections/community\.general/pull/9234)\)\.
* redfish\_utils module utils \- remove undocumented default applytime \([https\://github\.com/ansible\-collections/community\.general/pull/9114](https\://github\.com/ansible\-collections/community\.general/pull/9114)\)\.
* redhat\_subscription \- do not try to unsubscribe \(i\.e\. remove subscriptions\)
  when unregistering a system\: newer versions of subscription\-manager\, as
  available in EL 10 and Fedora 41\+\, do not support entitlements anymore\, and
  thus unsubscribing will fail
  \([https\://github\.com/ansible\-collections/community\.general/pull/9578](https\://github\.com/ansible\-collections/community\.general/pull/9578)\)\.
* redhat\_subscription \- use the \"enable\_content\" option \(when available\) when
  registering using D\-Bus\, to ensure that subscription\-manager enables the
  content on registration\; this is particular important on EL 10\+ and Fedora
  41\+
  \([https\://github\.com/ansible\-collections/community\.general/pull/9778](https\://github\.com/ansible\-collections/community\.general/pull/9778)\)\.
* reveal\_ansible\_type filter plugin and ansible\_type test plugin \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* rundeck\_acl\_policy \- ensure that project ACLs are sent to the correct endpoint \([https\://github\.com/ansible\-collections/community\.general/pull/10097](https\://github\.com/ansible\-collections/community\.general/pull/10097)\)\.
* slack \- fail if Slack API response is not OK with error message \([https\://github\.com/ansible\-collections/community\.general/pull/9198](https\://github\.com/ansible\-collections/community\.general/pull/9198)\)\.
* sudoers \- display stdout and stderr raised while failed validation \([https\://github\.com/ansible\-collections/community\.general/issues/9674](https\://github\.com/ansible\-collections/community\.general/issues/9674)\, [https\://github\.com/ansible\-collections/community\.general/pull/9871](https\://github\.com/ansible\-collections/community\.general/pull/9871)\)\.
* sysrc \- no longer always reporting <code>changed\=true</code> when <code>state\=absent</code>\. This fixes the method <code>exists\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10004](https\://github\.com/ansible\-collections/community\.general/issues/10004)\, [https\://github\.com/ansible\-collections/community\.general/pull/10005](https\://github\.com/ansible\-collections/community\.general/pull/10005)\)\.
* sysrc \- split the output of <code>sysrc \-e \-a</code> on the first <code>\=</code> only \([https\://github\.com/ansible\-collections/community\.general/issues/10120](https\://github\.com/ansible\-collections/community\.general/issues/10120)\, [https\://github\.com/ansible\-collections/community\.general/pull/10121](https\://github\.com/ansible\-collections/community\.general/pull/10121)\)\.
* xml \- ensure file descriptor is closed \([https\://github\.com/ansible\-collections/community\.general/pull/9695](https\://github\.com/ansible\-collections/community\.general/pull/9695)\)\.
* yaml callback plugin \- adjust to latest changes in ansible\-core devel \([https\://github\.com/ansible\-collections/community\.general/pull/10212](https\://github\.com/ansible\-collections/community\.general/pull/10212)\)\.
* yaml callback plugin \- use ansible\-core internals to avoid breakage with Data Tagging \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.
* yaml callback plugin \- when using ansible\-core 2\.19\.0b2 or newer\, uses a new utility provided by ansible\-core\. This allows us to remove all hacks and vendored code that was part of the plugin for ansible\-core versions with Data Tagging so far \([https\://github\.com/ansible\-collections/community\.general/pull/10242](https\://github\.com/ansible\-collections/community\.general/pull/10242)\)\.
* zfs \- fix handling of multi\-line values of user\-defined ZFS properties \([https\://github\.com/ansible\-collections/community\.general/pull/6264](https\://github\.com/ansible\-collections/community\.general/pull/6264)\)\.
* zfs\_facts \- parameter <code>type</code> now accepts multple values as documented \([https\://github\.com/ansible\-collections/community\.general/issues/5909](https\://github\.com/ansible\-collections/community\.general/issues/5909)\, [https\://github\.com/ansible\-collections/community\.general/pull/9697](https\://github\.com/ansible\-collections/community\.general/pull/9697)\)\.
* zypper\_repository \- make compatible with Python 3\.12\+ \([https\://github\.com/ansible\-collections/community\.general/issues/10222](https\://github\.com/ansible\-collections/community\.general/issues/10222)\, [https\://github\.com/ansible\-collections/community\.general/pull/10223](https\://github\.com/ansible\-collections/community\.general/pull/10223)\)\.
* zypper\_repository \- use <code>metalink</code> attribute to identify repositories without <code>\<url/\></code> element \([https\://github\.com/ansible\-collections/community\.general/issues/10224](https\://github\.com/ansible\-collections/community\.general/issues/10224)\, [https\://github\.com/ansible\-collections/community\.general/pull/10225](https\://github\.com/ansible\-collections/community\.general/pull/10225)\)\.

<a id="community-vmware"></a>
#### community\.vmware

* Fix issues with pyvmomi 9\.0\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/issues/2414](https\://github\.com/ansible\-collections/community\.vmware/issues/2414)\)\.
* vmware\_vmotion \- Fix issue with same resource pool name on different clusters \([https\://github\.com/ansible\-collections/community\.vmware/issues/1719](https\://github\.com/ansible\-collections/community\.vmware/issues/1719)\)\.

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Added \"gather\_facts\" to all example playbooks\.
* Fixed a BUG that occurred when username/password and access token were used at the same time\.

<a id="netapp-storagegrid-1"></a>
#### netapp\.storagegrid

* na\_sg\_org\_user \- fix where existing users with no groups attached were not getting any groups added\.

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_ds \- Fixed issue with updaing a LDAP configuration fails with a list error\.
* purefa\_proxy \- Fixed issue with incorrect string comparison
* purefa\_volume \- Fixed issue for error on volume delete w/o eradicate

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* content\_template \- Fix error when creating template from VM and not specifying certain non\-critical placement options
* content\_template \- Replace non\-existent method used when handling api errors
* pyvmomi \- Replace deprecated JSON encoder with new one from pyvmomi package \([https\://github\.com/vmware/pyvmomi/blob/e6cc09f32593d263b9ea0b611596a2c505786c6b/CHANGELOG\.md\?plain\=1\#L72](https\://github\.com/vmware/pyvmomi/blob/e6cc09f32593d263b9ea0b611596a2c505786c6b/CHANGELOG\.md\?plain\=1\#L72)\)

<a id="vyos-vyos-4"></a>
#### vyos\.vyos

* vyos\_config \- Fix change detection for recent Vyos versions
* vyos\_firewall\_global \- Fix removing last member of a firewall group\.
* vyos\_firewall\_global \- Fixed ipv6 route\-redirects and tests
* vyos\_firewall\_global \- Fixed parsing of global\-options \(1\.4\+\)
* vyos\_firewall\_global \- Fixed state\-policy deletion \(partial and full\)
* vyos\_firewall\_global \- fixed behavior for stanzas processing by facts in 1\.4\+ \(e\.g\. present/absent stanza vs enable/disable\)
* vyos\_firewall\_global \- fixed the facts parsers to include state\-policies\, redirect
* vyos\_firewall\_rules \- Allow deleting of firewall description\.
* vyos\_firewall\_rules \- Fix limit parameter processing
* vyos\_firewall\_rules \- fixed behavior for log\, disable attributes
* vyos\_firewall\_rules \- fixed behavior for override and replaced states
* vyos\_interfaces \- fixed bug where \'replace\' would delete an active disable and not reinstate it
* vyos\_interfaces \- fixed over\-zealous handling of disable\, which could catch other interface items that are disabled\.
* vyos\_l3\_interfaces \- fix delete in interfaces to remove vif completely if in affected interface
* vyos\_l3\_interfaces \- fix override in interfaces to remove vif completely if not present in new config
* vyos\_l3\_interfaces \- fix replace in interfaces to remove vif completely if not present in new config
* vyos\_logging\_global \- Fixed v1\.3 and before when <em class="title-reference">protocol</em> and <em class="title-reference">level</em> were set for the same host
* vyos\_ospf\_interfaces \- fixed get\_config to cater for unordered command lists in 1\.4\+
* vyos\_ospfv2 \- passive\-interface processing for 1\.3\- and 1\.4\+
* vyos\_ospfv3 \- added support for adding interfaces to areas
* vyos\_static routes \- fixed the facts\, argspecs\, config to include interface\-routes
* vyos\_user \- fix handling of <em class="title-reference">full\-name</em> in parser and module

<a id="known-issues-1"></a>
### Known Issues

<a id="community-general-5"></a>
#### community\.general

* reveal\_ansible\_type filter plugin and ansible\_type test plugin \- note that ansible\-core\'s Data Tagging feature implements new aliases\, such as <code>\_AnsibleTaggedStr</code> for <code>str</code>\, <code>\_AnsibleTaggedInt</code> for <code>int</code>\, and <code>\_AnsibleTaggedFloat</code> for <code>float</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.

<a id="vyos-vyos-5"></a>
#### vyos\.vyos

* existing code for 1\.3 facility protocol and facility level are not compatible\, only one will be set and level is the priority\.

<a id="new-plugins"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.print\_task \- Prints playbook task snippet to job output\.

<a id="connection"></a>
#### Connection

* community\.general\.wsl \- Run tasks in WSL distribution using wsl\.exe CLI via SSH\.

<a id="filter"></a>
#### Filter

* community\.general\.accumulate \- Produce a list of accumulated sums of the input list contents\.
* community\.general\.json\_diff \- Create a JSON patch by comparing two JSON files\.
* community\.general\.json\_patch \- Apply a JSON\-Patch \(RFC 6902\) operation to an object\.
* community\.general\.json\_patch\_recipe \- Apply JSON\-Patch \(RFC 6902\) operations to an object\.
* community\.general\.to\_prettytable \- Format a list of dictionaries as an ASCII table\.

<a id="inventory"></a>
#### Inventory

* community\.general\.iocage \- iocage inventory source\.

<a id="lookup"></a>
#### Lookup

* community\.general\.onepassword\_ssh\_key \- Fetch SSH keys stored in 1Password\.

<a id="new-modules-2"></a>
### New Modules

<a id="community-general-6"></a>
#### community\.general

* community\.general\.android\_sdk \- Manages Android SDK packages\.
* community\.general\.decompress \- Decompresses compressed files\.
* community\.general\.ldap\_inc \- Use the Modify\-Increment LDAP V3 feature to increment an attribute value\.
* community\.general\.lvm\_pv \- Manage LVM Physical Volumes\.
* community\.general\.pacemaker\_resource \- Manage pacemaker resources\.
* community\.general\.systemd\_creds\_decrypt \- C\(systemd\)\'s C\(systemd\-creds decrypt\) plugin\.
* community\.general\.systemd\_creds\_encrypt \- C\(systemd\)\'s C\(systemd\-creds encrypt\) plugin\.
* community\.general\.systemd\_info \- Gather C\(systemd\) unit info\.
* community\.general\.xdg\_mime \- Set default handler for MIME types\, for applications using XDG tools\.
* community\.general\.zpool \- Manage ZFS zpools\.

<a id="fortinet-fortimanager-2"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_dlp\_exactdatamatch \- Configure exact\-data\-match template used by DLP scan\.
* fortinet\.fortimanager\.fmgr\_dlp\_exactdatamatch\_columns \- DLP exact\-data\-match column types\.
* fortinet\.fortimanager\.fmgr\_dlp\_label \- Configure labels used by DLP blocking\.
* fortinet\.fortimanager\.fmgr\_dlp\_label\_entries \- DLP label entries\.
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extendervap \- FortiExtender wifi vap configuration\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension \- Configure Internet Services Extension\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension\_disableentry \- Disable entries in the Internet Service database\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension\_disableentry\_ip6range \- IPv6 ranges in the disable entry\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension\_disableentry\_iprange \- IPv4 ranges in the disable entry\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension\_disableentry\_portrange \- Port ranges in the disable entry\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension\_entry \- Entries added to the Internet Service extension database\.
* fortinet\.fortimanager\.fmgr\_firewall\_internetserviceextension\_entry\_portrange \- Port ranges in the custom entry\.
* fortinet\.fortimanager\.fmgr\_fmupdate\_fgdsetting \- Cli fmupdate fgd setting
* fortinet\.fortimanager\.fmgr\_fmupdate\_fgdsetting\_serveroverride \- Cli fmupdate fgd setting server override
* fortinet\.fortimanager\.fmgr\_gtp\_rattimeoutprofile \- RAT timeout profile
* fortinet\.fortimanager\.fmgr\_icap\_servergroup \- Configure an ICAP server group consisting of multiple forward servers\.
* fortinet\.fortimanager\.fmgr\_icap\_servergroup\_serverlist \- Add ICAP servers to a list to form a server group\.
* fortinet\.fortimanager\.fmgr\_system\_log\_deviceselector \- Accept/reject devices matching specified filter types\.
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_agentprofile \- Configure FortiTelemetry agent profiles\.
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_application\_predefine \- Configure FortiTelemetry predefined applications\.
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_profile \- Configure FortiTelemetry profiles\.
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_profile\_application \- Configure applications\.
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_profile\_application\_sla \- Service level agreement
* fortinet\.fortimanager\.fmgr\_user\_scim \- Configure SCIM client entries\.
* fortinet\.fortimanager\.fmgr\_wireless\_vap\_ip6prefixlist \- Wireless controller vap ip6 prefix list

<a id="netapp-storagegrid-2"></a>
#### netapp\.storagegrid

* netapp\.storagegrid\.na\_sg\_grid\_alert\_receiver \- NetApp StorageGRID manage alert receiver\.
* netapp\.storagegrid\.na\_sg\_grid\_audit\_destination \- Configure audit log destinations on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_autosupport \- Configure autosupport on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_domain\_name \- Configure endpoint domain name on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_hotfix \- Apply hotfixes on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_proxy\_settings \- NetApp StorageGRID manage proxy settings for the grid\.
* netapp\.storagegrid\.na\_sg\_grid\_snmp \- Configure SNMP agent on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_tenant \- NetApp StorageGRID manage tenant accounts\.
* netapp\.storagegrid\.na\_sg\_grid\_vlan\_interface \- Configure VLAN interface on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_org\_bucket \- Manage buckets on StorageGRID\.

<a id="unchanged-collections-3"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.0\)
* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.windows \(still version 3\.1\.0\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 6\.4\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.intersight \(still version 2\.1\.0\)
* cisco\.ios \(still version 10\.1\.0\)
* cisco\.iosxr \(still version 11\.1\.0\)
* cisco\.meraki \(still version 2\.21\.3\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.1\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.1\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.docker \(still version 4\.6\.1\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.4\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.4\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 3\.14\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.5\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 3\.0\.0\)
* community\.zabbix \(still version 4\.0\.0\)
* containers\.podman \(still version 1\.16\.4\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.openmanage \(still version 9\.12\.1\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.36\.0\)
* fortinet\.fortios \(still version 2\.4\.0\)
* hetzner\.hcloud \(still version 5\.1\.0\)
* hitachivantara\.vspone\_block \(still version 3\.5\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.4\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubevirt\.core \(still version 2\.2\.3\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.ad \(still version 1\.9\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.0\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.3\.0\)
* theforeman\.foreman \(still version 5\.4\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a6"></a>
## v12\.0\.0a6

- <a href="#release-summary-4">Release Summary</a>
- <a href="#added-collections-1">Added Collections</a>
- <a href="#ansible-core-10">Ansible\-core</a>
- <a href="#changed-collections-4">Changed Collections</a>
- <a href="#minor-changes-4">Minor Changes</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
- <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
- <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#community-vmware-2">community\.vmware</a>
- <a href="#bugfixes-4">Bugfixes</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-hrobot-3">community\.hrobot</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-2">hitachivantara\.vspone\_block</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-3">vmware\.vmware</a>
- <a href="#new-modules-3">New Modules</a>
    - <a href="#community-hrobot-4">community\.hrobot</a>
    - <a href="#hitachivantara-vspone-block-3">hitachivantara\.vspone\_block</a>
    - <a href="#telekom-mms-icinga-director-2">telekom\_mms\.icinga\_director</a>
- <a href="#unchanged-collections-4">Unchanged Collections</a>

<a id="release-summary-4"></a>
### Release Summary

Release Date\: 2025\-06\-12

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections-1"></a>
### Added Collections

* community\.proxmox \(version 1\.0\.1\)

<a id="ansible-core-10"></a>
### Ansible\-core

Ansible 12\.0\.0a6 contains ansible\-core version 2\.19\.0b6\.
This is a newer version than version 2\.19\.0b5 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-4"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 12.0.0a5 | Ansible 12.0.0a6 | Notes                                                                                                                        |
| --------------------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| cisco.meraki                | 2.21.2           | 2.21.3           |                                                                                                                              |
| community.docker            | 4.6.0            | 4.6.1            |                                                                                                                              |
| community.hrobot            | 2.3.0            | 2.4.0            |                                                                                                                              |
| community.proxmox           |                  | 1.0.1            | The collection was added to Ansible                                                                                          |
| community.vmware            | 5.6.0            | 5.7.0            |                                                                                                                              |
| community.zabbix            | 3.3.0            | 4.0.0            |                                                                                                                              |
| containers.podman           | 1.16.3           | 1.16.4           |                                                                                                                              |
| hetzner.hcloud              | 5.0.1            | 5.1.0            |                                                                                                                              |
| hitachivantara.vspone_block | 3.4.2            | 3.5.0            |                                                                                                                              |
| kubevirt.core               | 2.2.2            | 2.2.3            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| telekom_mms.icinga_director | 2.2.2            | 2.3.0            |                                                                                                                              |
| theforeman.foreman          | 5.3.0            | 5.4.0            |                                                                                                                              |
| vmware.vmware               | 2.0.1            | 2.1.0            |                                                                                                                              |

<a id="minor-changes-4"></a>
### Minor Changes

<a id="ansible-core-11"></a>
#### Ansible\-core

* ansiballz \- Added an experimental AnsiballZ extension for remote debugging\.
* ansiballz \- Added support for AnsiballZ extensions\.
* ansiballz \- Moved AnsiballZ code coverage support into an extension\.
* ansiballz \- Refactored AnsiballZ and module respawn\.
* template action and lookup plugin \- The value of the <code>ansible\_managed</code> variable \(if set\) will not be masked by the <code>template</code> action and lookup\. Previously\, the value calculated by the <code>DEFAULT\_MANAGED\_STR</code> configuration option always masked the variable value during plugin execution\, preventing runtime customization\.

<a id="community-vmware-1"></a>
#### community\.vmware

* vcenter\_extension \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_guest\_cross\_vc\_clone \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_guest\_instant\_clone \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_vm\_inventory \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_vsan\_cluster \- Stop using <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.

<a id="community-zabbix"></a>
#### community\.zabbix

* Add <em class="title-reference">zabbix\_http\_headers</em> variable to allow specifying custom HTTP headers for Zabbix API calls\. This can be useful for authentication or other custom header requirements\.
* Agent Role \- Removed Temporary Fix supporting RHEL9
* You can now deploy these roles with inject\_facts\_as\_vars set to false
* roles \- sane selinux defaults
* roles/proxy \- optionally creation of proxy\_group and adding proxy to group \(Zabbix 7\.0\+\)
* roles/zabbix\_agent \- Tweaking the windows service
* zabbix\_action module \- properly configure discovery check condition in discovery action depending on information provided in discovery check <em class="title-reference">value</em>\.
* zabbix\_configuration module \- Add this module to import configuration data\.
* zabbix\_group \- add propagate parameter
* zabbix\_item \- added support for item types zabbix\_agent\, snmp\_trap\, snmp\_agent\, ipmi\_agent and jmx\_agent
* zabbix\_mediatype \- add Message template for services
* zabbix\_proxy role \- fix Zabbix proxy with encryptuion registration
* zabbix\_server role \- facilitate overriding database schemas loaded
* zabbix\_server role \- facilitate overriding packages installed
* zabbix\_service \- add better idempotency that checks every parameter for change and updates only the changed ones
* zabbix\_templategroup \- add propagate parameter
* zabbix\_token module \- Fix status value for zabbix Auth token\.
* zabbix\_token module \- update the logic for update of Zabbix Token

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* ssh\_key \- Log a warning when the provided public key does not match one in the API\.
* ssh\_key \- When the public key does not match the one in the API\, allow recreating the SSH Key in the API using the <code>force\=true</code> argument\.

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

* Added additional parameters primary\_volume\_device\_group\_name and secondary\_volume\_device\_group\_name to retrieve ShadowImage group details more quickly\.
* Added new module <em class="title-reference">hv\_external\_paritygroup\_facts</em> to retrieve information about External Parity Group\.
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

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* Add API timeout option for all modules \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/282](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/282)\)
* Add support for IcingaDB in inventory plugin \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/274](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/274)\)
* Icinga dependency modules implementation \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/272](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/272)\)

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* repository \- add <code>rhel\-10</code> to os version filter choices
* repository \- add support for the <code>retain\_package\_versions\_count</code> parameter

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* moid\_from\_path \- Add lookup plugins to get an objects MOID \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/191](https\://github\.com/ansible\-collections/vmware\.vmware/issues/191)\)

<a id="breaking-changes--porting-guide-1"></a>
### Breaking Changes / Porting Guide

<a id="community-zabbix-1"></a>
#### community\.zabbix

* All Roles \- Remove support for Ubuntu 20\.04
* zabbix 6\.4 in roles is no longer supported

<a id="deprecated-features-3"></a>
### Deprecated Features

<a id="community-vmware-2"></a>
#### community\.vmware

* module\_utils\.vmware \- Deprecate <code>connect\_to\_api</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2372](https\://github\.com/ansible\-collections/community\.vmware/pull/2372)\)\.
* vmware\_guest\_powerstate \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2398](https\://github\.com/ansible\-collections/community\.vmware/pull/2398)\)\.

<a id="bugfixes-4"></a>
### Bugfixes

<a id="ansible-core-12"></a>
#### Ansible\-core

* Fix templating <code>tags</code> on plays and roles\. \([https\://github\.com/ansible/ansible/issues/69903](https\://github\.com/ansible/ansible/issues/69903)\)
* ansible\-doc will no longer ignore docs for modules without an extension \([https\://github\.com/ansible/ansible/issues/85279](https\://github\.com/ansible/ansible/issues/85279)\)\.
* display \- Fix hang caused by early post\-fork writers to stdout/stderr \(e\.g\.\, pydevd\) encountering an unreleased fork lock\.
* get\_url \- add a check to recognize incomplete data transfers\.
* include\_tasks \- fix templating options when used as a handler \([https\://github\.com/ansible/ansible/pull/85015](https\://github\.com/ansible/ansible/pull/85015)\)\.
* templating \- Fixed cases where template expression blocks halted prematurely when a Jinja macro invocation returned an undefined value\.
* templating \- Jinja macros returned from a template expression can now be called from another template expression\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* cisco\.meraki\.devices\_cellular\_sims \- fix idempotency error\.

<a id="community-docker"></a>
#### community\.docker

* docker\_compose\_v2 \- handle a \(potentially unintentional\) breaking change in Docker Compose 2\.37\.0\. Note that <code>ContainerName</code> is no longer part of the return value \([https\://github\.com/ansible\-collections/community\.docker/issues/1082](https\://github\.com/ansible\-collections/community\.docker/issues/1082)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1083](https\://github\.com/ansible\-collections/community\.docker/pull/1083)\)\.
* docker\_container \- fix idempotency if <code>command\=\[\]</code> and <code>command\_handling\=correct</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1080](https\://github\.com/ansible\-collections/community\.docker/issues/1080)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1085](https\://github\.com/ansible\-collections/community\.docker/pull/1085)\)\.

<a id="community-hrobot-3"></a>
#### community\.hrobot

* storagebox \- make sure that changes of boolean parameters are sent correctly to the Robot service \([https\://github\.com/ansible\-collections/community\.hrobot/issues/160](https\://github\.com/ansible\-collections/community\.hrobot/issues/160)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/161](https\://github\.com/ansible\-collections/community\.hrobot/pull/161)\)\.

<a id="community-vmware-3"></a>
#### community\.vmware

* vm\_device\_helper \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_guest\_controller \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_guest\_disk \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_host\_inventory \- New option <code>enable\_backward\_compatability</code> that can be set to <code>false</code> to work with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_target\_canonical\_info \- Fix an issue with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.
* vmware\_vm\_inventory \- New option <code>enable\_backward\_compatability</code> that can be set to <code>false</code> to work with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2391](https\://github\.com/ansible\-collections/community\.vmware/pull/2391)\)\.

<a id="community-zabbix-2"></a>
#### community\.zabbix

* host module \- Fixed idempotentcy related to changes in tag order\.
* maintenace module \- Fixed idempotentcy related to changes in tag order\.
* roles/zabbix\_agent \- Reading existing PSK files failed on Windows
* roles/zabbix\_agent \- UserParameterDir get wrong value if var zabbix\_agent\_userparamaterdir is set
* roles/zabbix\_repo \- debian architectures should map better for i386 and armhf
* roles/zabbix\_repo \- debian/ubuntu arm64 repo url fixed for zabbix 7\.2
* zabbix\_agent Role \- Add \_zabbix\_agent\_pluginsocket variable to override /tmp/agent\.plugin\.sock
* zabbix\_service \- fix propagation\_value and propagation\_rule parameters
* zabbix\_template\_info module \- Dump YAML formatted template data without date in Zabbix 7\.0 or higher\.
* zabbix\_web role \- fix /etc/zabbix/web/zabbix\.conf\.php file mode\.

<a id="containers-podman-2"></a>
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

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* All returned resource IDs are now integers instead of strings\.
* server \- The <code>placement\_group</code> argument now correctly handles placement group IDs during updates\.

<a id="hitachivantara-vspone-block-2"></a>
#### hitachivantara\.vspone\_block

* Fixed output details of <em class="title-reference">host\_group\_number</em> and <em class="title-reference">host\_group\_id</em> in <em class="title-reference">hv\_hg</em> and \'hv\_hg\_facts\' modules to be consistent\.

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* Bug\: dependency apply module raises error when using a variable for parent host or service \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/276](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/276)\)
* Extend checks in diff as a workaround for type confusion with the Director API \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/278](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/278)\)
* add \'groups\' parameter to task \'icinga\_user\.yml\' \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/284](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/284)\)

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* content\_upload \- lower chunk size to 1MB to avoid generating too big requests \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1862](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1862)\)
* host \- ensure LCE and CV are always sent together when updating one of them

<a id="vmware-vmware-3"></a>
#### vmware\.vmware

* Make integration tests compatible with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/194](https\://github\.com/ansible\-collections/vmware\.vmware/issues/194)\)
* cluster\_drs \- Fix error when non\-string advanced settings are applied \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/190](https\://github\.com/ansible\-collections/vmware\.vmware/issues/190)\)
* cluster\_ha \- Fix error when non\-string advanced settings are applied \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/190](https\://github\.com/ansible\-collections/vmware\.vmware/issues/190)\)
* tests/integration/vmware\_folder\_template\_from\_vm \- Fix tests for 2\.19

<a id="new-modules-3"></a>
### New Modules

<a id="community-hrobot-4"></a>
#### community\.hrobot

* community\.hrobot\.storagebox\_snapshot\_info \- Query the snapshots for a storage box\.
* community\.hrobot\.storagebox\_subaccount \- Create\, update\, or delete a subaccount for a storage box\.
* community\.hrobot\.storagebox\_subaccount\_info \- Query the subaccounts for a storage box\.

<a id="hitachivantara-vspone-block-3"></a>
#### hitachivantara\.vspone\_block

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_external\_paritygroup\_facts \- Retrieves information about External Parity Group from Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_external\_path\_group \- Manages External Path Groups in the Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_external\_path\_group\_facts \- Retrieves information about External Path Group from Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_mp\_facts \- Retrieves MP blades information from Hitachi VSP storage systems\.

<a id="telekom-mms-icinga-director-2"></a>
#### telekom\_mms\.icinga\_director

* telekom\_mms\.icinga\_director\.icinga\_dependency\_apply \- Manage dependency apply rules in Icinga2

<a id="unchanged-collections-4"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.0\)
* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 3\.1\.0\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.4\.0\)
* check\_point\.mgmt \(still version 6\.4\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.intersight \(still version 2\.1\.0\)
* cisco\.ios \(still version 10\.1\.0\)
* cisco\.iosxr \(still version 11\.1\.0\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.1\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 4\.2\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.1\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.crypto \(still version 3\.0\.0\-a2\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.2\.4\)
* community\.general \(still version 10\.7\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.4\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 3\.14\.0\)
* community\.okd \(still version 4\.0\.2\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.5\.0\)
* community\.routeros \(still version 3\.7\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.0\.5\)
* community\.windows \(still version 3\.0\.0\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.openmanage \(still version 9\.12\.1\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.36\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.1\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.4\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.3\.0\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.ad \(still version 1\.9\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.0\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flasharray \(still version 1\.34\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a5"></a>
## v12\.0\.0a5

- <a href="#release-summary-5">Release Summary</a>
- <a href="#ansible-core-13">Ansible\-core</a>
- <a href="#changed-collections-5">Changed Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
- <a href="#minor-changes-5">Minor Changes</a>
    - <a href="#ansible-core-14">Ansible\-core</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#cloud-common-2">cloud\.common</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-crypto-4">community\.crypto</a>
    - <a href="#community-general-7">community\.general</a>
    - <a href="#community-libvirt">community\.libvirt</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-rabbitmq">community\.rabbitmq</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-4">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#ovirt-ovirt">ovirt\.ovirt</a>
- <a href="#breaking-changes--porting-guide-2">Breaking Changes / Porting Guide</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#community-crypto-5">community\.crypto</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
- <a href="#deprecated-features-4">Deprecated Features</a>
    - <a href="#ansible-core-15">Ansible\-core</a>
    - <a href="#cisco-nxos-3">cisco\.nxos</a>
    - <a href="#community-aws-2">community\.aws</a>
    - <a href="#community-crypto-6">community\.crypto</a>
    - <a href="#community-general-8">community\.general</a>
    - <a href="#community-postgresql">community\.postgresql</a>
- <a href="#removed-features-previously-deprecated-1">Removed Features \(previously deprecated\)</a>
    - <a href="#community-crypto-7">community\.crypto</a>
- <a href="#bugfixes-5">Bugfixes</a>
    - <a href="#ansible-core-16">Ansible\-core</a>
    - <a href="#amazon-aws-3">amazon\.aws</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-meraki-2">cisco\.meraki</a>
    - <a href="#cloudscale-ch-cloud-1">cloudscale\_ch\.cloud</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-general-9">community\.general</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#community-rabbitmq-1">community\.rabbitmq</a>
    - <a href="#f5networks-f5-modules-1">f5networks\.f5\_modules</a>
    - <a href="#hitachivantara-vspone-block-5">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#ovirt-ovirt-1">ovirt\.ovirt</a>
    - <a href="#vmware-vmware-4">vmware\.vmware</a>
- <a href="#known-issues-2">Known Issues</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
- <a href="#new-plugins-1">New Plugins</a>
    - <a href="#callback-1">Callback</a>
    - <a href="#filter-1">Filter</a>
- <a href="#new-modules-4">New Modules</a>
    - <a href="#cloudscale-ch-cloud-2">cloudscale\_ch\.cloud</a>
    - <a href="#community-general-10">community\.general</a>
    - <a href="#community-libvirt-1">community\.libvirt</a>
- <a href="#unchanged-collections-5">Unchanged Collections</a>

<a id="release-summary-5"></a>
### Release Summary

Release Date\: 2025\-06\-04

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-13"></a>
### Ansible\-core

Ansible 12\.0\.0a5 contains ansible\-core version 2\.19\.0b5\.
This is a newer version than version 2\.19\.0b4 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-5"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 12.0.0a4 | Ansible 12.0.0a5 | Notes                                                                                                                        |
| --------------------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws                  | 9.5.0            | 10.1.0           |                                                                                                                              |
| ansible.windows             | 3.0.0            | 3.1.0            |                                                                                                                              |
| azure.azcollection          | 3.3.1            | 3.4.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| check_point.mgmt            | 6.4.0            | 6.4.1            |                                                                                                                              |
| cisco.intersight            | 2.0.20           | 2.1.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.ios                   | 10.0.0           | 10.1.0           |                                                                                                                              |
| cisco.iosxr                 | 11.0.0           | 11.1.0           |                                                                                                                              |
| cisco.meraki                | 2.21.1           | 2.21.2           |                                                                                                                              |
| cisco.nxos                  | 10.0.0           | 10.1.0           |                                                                                                                              |
| cloud.common                | 4.0.0            | 4.2.0            |                                                                                                                              |
| cloudscale_ch.cloud         | 2.4.1            | 2.5.1            |                                                                                                                              |
| community.aws               | 9.3.0            | 10.0.0           |                                                                                                                              |
| community.crypto            | 2.26.1           | 3.0.0-a2         |                                                                                                                              |
| community.dns               | 3.2.3            | 3.2.4            |                                                                                                                              |
| community.general           | 10.6.0           | 10.7.0           |                                                                                                                              |
| community.libvirt           | 1.3.1            | 1.4.0            |                                                                                                                              |
| community.mongodb           | 1.7.9            | 1.7.10           | There are no changes recorded in the changelog.                                                                              |
| community.mysql             | 3.13.0           | 3.14.0           |                                                                                                                              |
| community.okd               | 4.0.1            | 4.0.2            |                                                                                                                              |
| community.postgresql        | 4.0.0            | 4.1.0            |                                                                                                                              |
| community.rabbitmq          | 1.4.0            | 1.5.0            |                                                                                                                              |
| community.routeros          | 3.6.0            | 3.7.0            |                                                                                                                              |
| dellemc.openmanage          | 9.12.0           | 9.12.1           |                                                                                                                              |
| f5networks.f5_modules       | 1.35.0           | 1.36.0           |                                                                                                                              |
| hetzner.hcloud              | 4.3.0            | 5.0.1            |                                                                                                                              |
| hitachivantara.vspone_block | 3.4.0            | 3.4.2            |                                                                                                                              |
| ibm.storage_virtualize      | 2.7.3            | 2.7.4            |                                                                                                                              |
| kubernetes.core             | 5.2.0            | 5.3.0            |                                                                                                                              |
| kubevirt.core               | 2.2.0            | 2.2.2            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| microsoft.ad                | 1.9.0            | 1.9.1            |                                                                                                                              |
| ovirt.ovirt                 | 3.2.0            | 3.2.1            |                                                                                                                              |
| vmware.vmware               | 2.0.0            | 2.0.1            |                                                                                                                              |

<a id="major-changes-2"></a>
### Major Changes

<a id="amazon-aws"></a>
#### amazon\.aws

* amazon\.aws collection \- The amazon\.aws collection has dropped support for <code>botocore\<1\.34\.0</code> and <code>boto3\<1\.34\.0</code>\. Most modules will continue to work with older versions of the AWS SDK\, however compatibility with older versions of the SDK is not guaranteed and will not be tested\. When using older versions of the SDK a warning will be emitted by Ansible \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2426](https\://github\.com/ansible\-collections/amazon\.aws/pull/2426)\)\.
* amazon\.aws collection \- due to the AWS SDKs announcing the end of support for Python less than 3\.8 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\)\, support for Python less than 3\.8 by this collection was deprecated in release 6\.0\.0 and removed in release 10\.0\.0\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2426](https\://github\.com/ansible\-collections/amazon\.aws/pull/2426)\)\.
* connection/aws\_ssm \- The module has been migrated from the <code>community\.aws</code> collection\. Playbooks using the Fully Qualified Collection Name for this module should be updated to use <code>amazon\.aws\.aws\_ssm</code>\.

<a id="community-aws"></a>
#### community\.aws

* community\.aws collection \- The community\.aws collection has dropped support for <code>botocore\<1\.34\.0</code> and <code>boto3\<1\.34\.0</code>\. Most modules will continue to work with older versions of the AWS SDK\, however compatibility with older versions of the SDK is not guaranteed and will not be tested\. When using older versions of the SDK a warning will be emitted by Ansible \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2426](https\://github\.com/ansible\-collections/amazon\.aws/pull/2426)\)\.

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* idrac\_attributes \- This module is enhanced to support iDRAC10\.
* idrac\_attributes \- This role is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_jobs \- This module is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_status\_info \- This module is enhanced to support iDRAC10\.
* idrac\_syslog \- This module is deprecated\.
* idrac\_user\_info \- This module is enhanced to support iDRAC10\.
* idrac\_virtual\_media \- This module is enhanced to support iDRAC10\.

<a id="minor-changes-5"></a>
### Minor Changes

<a id="ansible-core-14"></a>
#### Ansible\-core

* Improved SUSE distribution detection in distribution\.py by parsing VARIANT\_ID from /etc/os\-release for identifying SLES\_SAP and SL\-Micro\. Falls back to /etc/products\.d/baseproduct symlink for older systems\.
* Remove unnecessary shebang from the <code>hostname</code> module\.
* Use <code>importlib\.metadata\.version\(\)</code> to detect Jinja version as jinja2\.\_\_version\_\_ is deprecated and will be removed in Jinja 3\.3\.
* ansible\-doc \- Return dynamic stub when reporting on Jinja filters and tests not explicitly documented in Ansible
* ansible\-doc \- Skip listing the internal <code>ansible\.\_protomatter</code> plugins unless explicitly requested
* ansible\-test \- Add RHEL 10\.0 as a remote platform for testing\.
* apt\_repository \- remove Python 2 support
* csvfile lookup \- remove Python 2 compat
* display \- Add <code>help\_text</code> and <code>obj</code> to <code>Display\.error\_as\_warning</code>\.
* display \- Replace Windows newlines \(<code>\\r\\n</code>\) in display output with Unix newlines \(<code>\\n</code>\)\. This ensures proper display of strings sourced from Windows hosts in environments which treat <code>\\r</code> as <code>\\n</code>\, such as Azure Pipelines\.
* facts \- add \"Linode\" for Linux VM in virtual facts
* module\_utils \- Add <code>AnsibleModule\.error\_as\_warning</code>\.
* module\_utils \- Add <code>ansible\.module\_utils\.common\.warnings\.error\_as\_warning</code>\.
* module\_utils \- Add optional <code>help\_text</code> argument to <code>AnsibleModule\.warn</code>\.
* ssh agent \- Added <code>SSH\_AGENT\_EXECUTABLE</code> config to allow override of ssh\-agent\.
* ssh connection plugin \- Added <code>verbosity</code> config to decouple SSH debug output verbosity from Ansible verbosity\. Previously\, the Ansible verbosity value was always applied to the SSH client command\-line\, leading to excessively verbose output\. Set the <code>ANSIBLE\_SSH\_VERBOSITY</code> envvar or <code>ansible\_ssh\_verbosity</code> Ansible variable to a positive integer to increase SSH client verbosity\.
* task timeout \- Specifying a timeout greater than 100\,000\,000 now results in an error\.
* templating \- Added <code>\_ANSIBLE\_TEMPLAR\_SANDBOX\_MODE\=allow\_unsafe\_attributes</code> environment variable to disable Jinja template attribute sandbox\. \([https\://github\.com/ansible/ansible/issues/85202](https\://github\.com/ansible/ansible/issues/85202)\)
* windows \- Added support for <code>\#AnsibleRequires \-Wrapper</code> to request a PowerShell module be run through the execution wrapper scripts without any module utils specified\.
* windows \- Added support for running signed modules and scripts with a Windows host protected by Windows App Control/WDAC\. This is a tech preview and the interface may be subject to change\.
* windows \- Script modules will preserve UTF\-8 encoding when executing the script\.

<a id="amazon-aws-1"></a>
#### amazon\.aws

* inventory/aws\_ec2 \- Adding support for Route53 as hostname \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2580](https\://github\.com/ansible\-collections/amazon\.aws/pull/2580)\)\.
* module\_utils\.s3 \- added \"501\" to the list of error codes thrown by S3 replacements \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2447](https\://github\.com/ansible\-collections/amazon\.aws/issues/2447)\)\.
* module\_utils/s3 \- add initial ErrorHandler for S3 modules \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2060](https\://github\.com/ansible\-collections/amazon\.aws/pull/2060)\)\.
* s3\_bucket \- migrated to use updated error handlers for better handling of non\-AWS errors \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2478](https\://github\.com/ansible\-collections/amazon\.aws/pull/2478)\)\.

<a id="ansible-windows"></a>
#### ansible\.windows

* setup \- add \"CloudStack KVM Hypervisor\" for Windows VM in virtual facts \([https\://github\.com/ansible\-collections/ansible\.windows/pull/785](https\://github\.com/ansible\-collections/ansible\.windows/pull/785)\)\.
* setup \- added <code>ansible\_product\_uuid</code> to align with Python facts \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/789](https\://github\.com/ansible\-collections/ansible\.windows/issues/789)
* win\_dns\_client \- add support for suffixsearchlist \([https\://github\.com/ansible\-collections/ansible\.windows/issues/656](https\://github\.com/ansible\-collections/ansible\.windows/issues/656)\)\.
* win\_powershell \- Add support for running scripts on a Windows host with an active Windows Application Control policy in place\. Scripts that are unsigned will be run in Constrained Language Mode while scripts that are signed and trusted by the remote host\'s WDAC policy will be run in Full Language Mode\.
* win\_powershell \- Added the <code>path</code> and <code>remote\_src</code> options which can be used to specify a local or remote PowerShell script to run\.
* win\_shell \- Add support for running scripts on a Windows host with an active Windows Application Control policy in place\. Scripts will always run in Contrained Language Mode as they are executed in memory\, use the <code>ansible\.windows\.win\_powershell</code> module to run signed scripts in Full Language Mode on a WDAC enabled host\.

<a id="cisco-ios-1"></a>
#### cisco\.ios

* ios\_hsrp\_interfaces \- Added support for cisco\.ios\.hsrp\_interfaces module \(standby commands\)\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* Adds support for missing set route map attributes med and extcommunity
* Enhanced CDP neighbor parsing to support updated output formats in IOS\-XR 7\.7\.21 and 7\.4\.1
* Modified <em class="title-reference">parse\_cdp\_ip</em> to recognize \"IPv4 address\" in place of \"IP address\"
* Updated <em class="title-reference">parse\_cdp\_intf\_port</em> to handle newline\-separated \"Interface\" and \"Port ID\" fields

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* hsrp\_interfaces \- Fixes and enhances capability of the module to deal with entire hsrp configuration under interfaces\.

<a id="cloud-common-2"></a>
#### cloud\.common

* Bump version of ansible\-lint to minimum 25\.1\.2
* module\_utils/turbo/module \- Add support for 2\.19 by returning a json compatible arg obj instead of a dict if possible \([https\://github\.com/ansible\-collections/cloud\.common/pull/167](https\://github\.com/ansible\-collections/cloud\.common/pull/167)\)\.
* module\_utils/turbo/server \- Add support for 2\.19 by making FakeStdin implement the IOBase ABC \([https\://github\.com/ansible\-collections/cloud\.common/pull/167](https\://github\.com/ansible\-collections/cloud\.common/pull/167)\)\.
* plugins/module\_utils/turbo/server \- Update how the async loop is created to support python 3\.12\+ \([https\://github\.com/ansible\-collections/cloud\.common/pull/169](https\://github\.com/ansible\-collections/cloud\.common/pull/169)\)\.

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Add ansible\-core 2\.19\+ compatibility
* volume \- Add revert parameter\.

<a id="community-crypto-4"></a>
#### community\.crypto

* No longer provide cryptography\'s <code>backend</code> parameter\. This will break with cryptography \< 3\.1 \([https\://github\.com/ansible\-collections/community\.crypto/pull/878](https\://github\.com/ansible\-collections/community\.crypto/pull/878)\)\.
* On cryptography 36\.0\.0\+\, always use <code>public\_bytes\(\)</code> for X\.509 extension objects instead of using cryptography internals to obtain DER value of extension \([https\://github\.com/ansible\-collections/community\.crypto/pull/878](https\://github\.com/ansible\-collections/community\.crypto/pull/878)\)\.
* Python code modernization\: add type hints and type checking \([https\://github\.com/ansible\-collections/community\.crypto/pull/885](https\://github\.com/ansible\-collections/community\.crypto/pull/885)\)\.
* Python code modernization\: avoid unnecessary string conversion \([https\://github\.com/ansible\-collections/community\.crypto/pull/880](https\://github\.com/ansible\-collections/community\.crypto/pull/880)\)\.
* Python code modernization\: avoid using <code>six</code> \([https\://github\.com/ansible\-collections/community\.crypto/pull/884](https\://github\.com/ansible\-collections/community\.crypto/pull/884)\)\.
* Python code modernization\: remove Python 3 specific code \([https\://github\.com/ansible\-collections/community\.crypto/pull/877](https\://github\.com/ansible\-collections/community\.crypto/pull/877)\)\.
* Python code modernization\: update <code>\_\_future\_\_</code> imports\, remove Python 2 specific boilerplates \([https\://github\.com/ansible\-collections/community\.crypto/pull/876](https\://github\.com/ansible\-collections/community\.crypto/pull/876)\)\.
* Python code modernization\: use <code>unittest\.mock</code> instead of <code>ansible\_collections\.community\.internal\_test\_tools\.tests\.unit\.compat\.mock</code> \([https\://github\.com/ansible\-collections/community\.crypto/pull/881](https\://github\.com/ansible\-collections/community\.crypto/pull/881)\)\.
* Python code modernization\: use f\-strings instead of <code>\%</code> and <code>str\.format\(\)</code> \([https\://github\.com/ansible\-collections/community\.crypto/pull/875](https\://github\.com/ansible\-collections/community\.crypto/pull/875)\)\.
* Remove <code>backend</code> parameter from internal code whenever possible \([https\://github\.com/ansible\-collections/community\.crypto/pull/883](https\://github\.com/ansible\-collections/community\.crypto/pull/883)\)\.
* Remove various compatibility code for cryptography \< 3\.3 \([https\://github\.com/ansible\-collections/community\.crypto/pull/878](https\://github\.com/ansible\-collections/community\.crypto/pull/878)\)\.
* Remove vendored copy of <code>distutils\.version</code> in favor of vendored copy included with ansible\-core 2\.12\+ \([https\://github\.com/ansible\-collections/community\.crypto/pull/371](https\://github\.com/ansible\-collections/community\.crypto/pull/371)\)\.
* acme\_\* modules \- improve parsing of <code>Retry\-After</code> reply headers in regular ACME requests \([https\://github\.com/ansible\-collections/community\.crypto/pull/890](https\://github\.com/ansible\-collections/community\.crypto/pull/890)\)\.
* action\_module plugin utils \- remove compatibility with older ansible\-core/ansible\-base/Ansible versions \([https\://github\.com/ansible\-collections/community\.crypto/pull/872](https\://github\.com/ansible\-collections/community\.crypto/pull/872)\)\.
* x509\_certificate\, x509\_certificate\_pipe \- the <code>ownca\_version</code> and <code>selfsigned\_version</code> parameters explicitly only allow the value <code>3</code>\. The module already failed for other values in the past\, now this is validated as part of the module argument spec \([https\://github\.com/ansible\-collections/community\.crypto/pull/890](https\://github\.com/ansible\-collections/community\.crypto/pull/890)\)\.

<a id="community-general-7"></a>
#### community\.general

* cobbler inventory plugin \- add <code>connection\_timeout</code> option to specify the connection timeout to the cobbler server \([https\://github\.com/ansible\-collections/community\.general/pull/11063](https\://github\.com/ansible\-collections/community\.general/pull/11063)\)\.
* cobbler inventory plugin \- add <code>facts\_level</code> option to allow requesting fully rendered variables for Cobbler systems \([https\://github\.com/ansible\-collections/community\.general/issues/9419](https\://github\.com/ansible\-collections/community\.general/issues/9419)\, [https\://github\.com/ansible\-collections/community\.general/pull/9975](https\://github\.com/ansible\-collections/community\.general/pull/9975)\)\.
* ini\_file \- modify an inactive option also when there are spaces in front of the comment symbol \([https\://github\.com/ansible\-collections/community\.general/pull/10102](https\://github\.com/ansible\-collections/community\.general/pull/10102)\, [https\://github\.com/ansible\-collections/community\.general/issues/8539](https\://github\.com/ansible\-collections/community\.general/issues/8539)\)\.
* pipx \- parameter <code>name</code> now accepts Python package specifiers \([https\://github\.com/ansible\-collections/community\.general/issues/7815](https\://github\.com/ansible\-collections/community\.general/issues/7815)\, [https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pipx module\_utils \- filtering application list by name now happens in the modules \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.
* pipx\_info \- filtering application list by name now happens in the module  \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.

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

<a id="community-routeros-1"></a>
#### community\.routeros

* api\_find\_and\_modify \- allow to control whether <code>dynamic</code> and/or <code>builtin</code> entries are ignored with the new <code>ignore\_dynamic</code> and <code>ignore\_builtin</code> options \([https\://github\.com/ansible\-collections/community\.routeros/issues/372](https\://github\.com/ansible\-collections/community\.routeros/issues/372)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/373](https\://github\.com/ansible\-collections/community\.routeros/pull/373)\)\.
* api\_info\, api\_modify \- add <code>port\-cost\-mode</code> to <code>interface bridge</code> which is supported since RouterOS 7\.13 \([https\://github\.com/ansible\-collections/community\.routeros/pull/371](https\://github\.com/ansible\-collections/community\.routeros/pull/371)\)\.

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* server \- Allow renaming a server\.
* volume\_attachment \- Add new <em class="title-reference">volume\_attachment</em> module to manage Volumes attachment\.

<a id="hitachivantara-vspone-block-4"></a>
#### hitachivantara\.vspone\_block

* Added back \'mu\_number\' parameter to the <em class="title-reference">hv\_gad</em> module\.
* Resolved various documentation inconsistencies\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_host\.py \- Added support for adding and removing preferred location\, and IO Groups
* ibm\_svc\_hostcluster\.py \- Added support for adding site
* ibm\_svc\_manage\_volume \- Added support for warning parameter

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* Bump version of ansible\-lint to 25\.1\.2 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/919](https\://github\.com/ansible\-collections/kubernetes\.core/pull/919)\)\.
* action/k8s\_info \- update templating mechanism with changes from <code>ansible\-core 2\.19</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/888](https\://github\.com/ansible\-collections/kubernetes\.core/pull/888)\)\.
* helm \- add reset\_then\_reuse\_values support to helm module \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/803](https\://github\.com/ansible\-collections/kubernetes\.core/issues/803)\)\.
* helm \- add support for <code>insecure\_skip\_tls\_verify</code> option to helm and helm\_repository\([https\://github\.com/ansible\-collections/kubernetes\.core/issues/694](https\://github\.com/ansible\-collections/kubernetes\.core/issues/694)\)\.

<a id="ovirt-ovirt"></a>
#### ovirt\.ovirt

* Enable and start postfix service so that ovirt\-ha\-agent logs are not filled with mail notification errors \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/741](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/741)\)
* Maintenance tasks regarding linting\, testing and CI \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/762](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/762)\)

<a id="breaking-changes--porting-guide-2"></a>
### Breaking Changes / Porting Guide

<a id="amazon-aws-2"></a>
#### amazon\.aws

* amazon\.aws collection \- Support for ansible\-core \< 2\.17 has been dropped \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2601](https\://github\.com/ansible\-collections/amazon\.aws/pull/2601)\)\.
* amazon\.aws collection \- Support for the <code>EC2\_ACCESS\_KEY</code> environment variable was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>access\_key</code> parameter or <code>AWS\_ACCESS\_KEY\_ID</code> environment variable instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- Support for the <code>EC2\_REGION</code> environment variable was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>region</code> parameter or <code>AWS\_REGION</code> environment variable instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- Support for the <code>EC2\_SECRET\_KEY</code> environment variable was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>secret\_key</code> parameter or <code>AWS\_SECRET\_ACCESS\_KEY</code> environment variable instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- Support for the <code>EC2\_SECURITY\_TOKEN</code> and <code>AWS\_SECURITY\_TOKEN</code> environment variables were deprecated in release <code>6\.0\.0</code> and have now been removed\.  Please use the <code>session\_token</code> parameter or <code>AWS\_SESSION\_TOKEN</code> environment variable instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- Support for the <code>EC2\_URL</code> and <code>S3\_URL</code> environment variables were deprecated in release <code>6\.0\.0</code> and have now been removed\.  Please use the <code>endpoint\_url</code> parameter or <code>AWS\_URL</code> environment variable instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- The <code>access\_token</code>\, <code>aws\_security\_token</code> and <code>security\_token</code> aliases for the <code>session\_token</code> parameter were deprecated in release <code>6\.0\.0</code> and have now been removed\.  Please use the <code>session\_token</code> name instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- The <code>boto\_profile</code> alias for the <code>profile</code> parameter was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>profile</code> name instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- The <code>ec2\_access\_key</code> alias for the <code>access\_key</code> parameter was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>access\_key</code> name instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- The <code>ec2\_region</code> alias for the <code>region</code> parameter was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>region</code> name instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- The <code>ec2\_secret\_key</code> alias for the <code>secret\_key</code> parameter was deprecated in release <code>6\.0\.0</code> and has now been removed\.  Please use the <code>secret\_key</code> name instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* amazon\.aws collection \- The <code>endpoint</code>\, <code>ec2\_url</code> and <code>s3\_url</code> aliases for the <code>endpoint\_url</code> parameter were deprecated in release <code>6\.0\.0</code> and have now been removed\.  Please use the <code>region</code> name instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* docs\_fragments \- The previously deprecated <code>amazon\.aws\.aws\_credentials</code> docs fragment has been removed please use <code>amazon\.aws\.common\.plugins</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* docs\_fragments \- The previously deprecated <code>amazon\.aws\.aws\_region</code> docs fragment has been removed please use <code>amazon\.aws\.region\.plugins</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* docs\_fragments \- The previously deprecated <code>amazon\.aws\.aws</code> docs fragment has been removed please use <code>amazon\.aws\.common\.modules</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* docs\_fragments \- The previously deprecated <code>amazon\.aws\.ec2</code> docs fragment has been removed please use <code>amazon\.aws\.region\.modules</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2527](https\://github\.com/ansible\-collections/amazon\.aws/pull/2527)\)\.
* ec2\_vpc\_peering\_info \- the <em class="title-reference">result</em> key has been removed from the return value\. <em class="title-reference">vpc\_peering\_connections</em> should be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2618](https\://github\.com/ansible\-collections/amazon\.aws/pull/2618)\)\.
* module\_utils\.botocore \- drop deprecated <code>boto3</code> parameter for <code>get\_aws\_region\(\)</code> and <code>get\_aws\_connection\_info\(\)</code>\, this parameter has had no effect since release 4\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2443](https\://github\.com/ansible\-collections/amazon\.aws/pull/2443)\)\.
* module\_utils\.ec2 \- drop deprecated <code>boto3</code> parameter for <code>get\_ec2\_security\_group\_ids\_from\_names\(\)</code> and <code>get\_aws\_connection\_info\(\)</code>\, this parameter has had no effect since release 4\.0\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2603](https\://github\.com/ansible\-collections/amazon\.aws/pull/2603)\)\.
* rds\_param\_group \- the redirect has been removed and playbooks should be updated to use rds\_instance\_param\_group \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2618](https\://github\.com/ansible\-collections/amazon\.aws/pull/2618)\)\.

<a id="community-aws-1"></a>
#### community\.aws

* Support for <code>ansible\-core\<2\.17</code> has been dropped \([https\://github\.com/ansible\-collections/community\.aws/pull/2303](https\://github\.com/ansible\-collections/community\.aws/pull/2303)\)\.
* The community\.aws collection has dropped support for <code>botocore\<1\.31\.0</code> and <code>boto3\<1\.28\.0</code>\. Most modules will continue to work with older versions of the AWS SDK\.  However\, compatibility with older versions of the SDK is not guaranteed and will not be tested\. When using older versions of the SDK a warning will be emitted by Ansible \([https\://github\.com/ansible\-collections/community\.aws/pull/2195](https\://github\.com/ansible\-collections/community\.aws/pull/2195)\)\.
* connection/aws\_ssm \- The connection plugin has been migrated from the <code>community\.aws</code> collection\. Playbooks or Inventory using the Fully Qualified Collection Name for this connection plugin should be updated to use <code>amazon\.aws\.aws\_ssm</code>\.

<a id="community-crypto-5"></a>
#### community\.crypto

* All doc\_fragments are now private to the collection and must not be used from other collections or unrelated plugins/modules\. Breaking changes in these can happen at any time\, even in bugfix releases \([https\://github\.com/ansible\-collections/community\.crypto/pull/898](https\://github\.com/ansible\-collections/community\.crypto/pull/898)\)\.
* All module\_utils and plugin\_utils are now private to the collection and must not be used from other collections or unrelated plugins/modules\. Breaking changes in these can happen at any time\, even in bugfix releases \([https\://github\.com/ansible\-collections/community\.crypto/pull/887](https\://github\.com/ansible\-collections/community\.crypto/pull/887)\)\.
* Ignore value of <code>select\_crypto\_backend</code> for all modules except acme\_\* and \.\.\.\, and always assume the value <code>auto</code>\. This ensures that the <code>cryptography</code> version is always checked \([https\://github\.com/ansible\-collections/community\.crypto/pull/883](https\://github\.com/ansible\-collections/community\.crypto/pull/883)\)\.
* The validation for relative timestamps is now more strict\. A string starting with <code>\+</code> or <code>\-</code> must be valid\, otherwise validation will fail\. In the past such strings were often silently ignored\, and in many cases the code which triggered the validation was not able to handle no result \([https\://github\.com/ansible\-collections/community\.crypto/pull/885](https\://github\.com/ansible\-collections/community\.crypto/pull/885)\)\.
* acme\.certificates module utils \- the <code>retrieve\_acme\_v1\_certificate\(\)</code> helper function has been removed \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* get\_certificate \- the default for <code>asn1\_base64</code> changed from <code>false</code> to <code>true</code> \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* x509\_crl \- the <code>mode</code> parameter no longer denotes the update mode\, but the CRL file mode\. Use <code>crl\_mode</code> instead for the update mode \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* Drop support for ansible\-core 2\.15\.
* Drop support for ansible\-core 2\.16\.
* Drop support for python 3\.8\.
* inventory \- The default value for the <em class="title-reference">hostvars\_prefix</em> option is now set to <em class="title-reference">hcloud\_</em>\. Make sure to update all references to host variables provided by the inventory\. You may revert this change by setting the <em class="title-reference">hostvars\_prefix</em> option to <em class="title-reference">\"\"</em>\.
* server \- The deprecated <code>force\_upgrade</code> argument is removed from the server module\. Please use the <code>force</code> argument instead\.
* volume \- Volumes are no longer detached when the server argument is not provided\. Please use the <code>volume\_attachment</code> module to manage volume attachments\.

<a id="deprecated-features-4"></a>
### Deprecated Features

<a id="ansible-core-15"></a>
#### Ansible\-core

* The <code>ShellModule\.checksum</code> method is now deprecated and will be removed in ansible\-core 2\.23\. Use <code>ActionBase\.\_execute\_remote\_stat\(\)</code> instead\.
* The <code>ansible\.module\_utils\.common\.collections\.count\(\)</code> function is deprecated and will be removed in ansible\-core 2\.23\. Use <code>collections\.Counter\(\)</code> from the Python standard library instead\.
* <code>ansible\.compat\.importlib\_resources</code> is deprecated and will be removed in ansible\-core 2\.23\. Use <code>importlib\.resources</code> from the Python standard library instead\.

<a id="cisco-nxos-3"></a>
#### cisco\.nxos

* nxos\_hsrp \- deprecate nxos\.nxos\.nxos\_hsrp in favor of nxos\.nxos\.nxos\_hsrp\_interfaces\.
* nxos\_vrf\_interface \- deprecate nxos\.nxos\.nxos\_vrf\_interface in favor of nxos\.nxos\.nxos\_vrf\_interfaces\.

<a id="community-aws-2"></a>
#### community\.aws

* community\.aws collection \- due to the AWS SDKs announcing the end of support for Python less than 3\.8 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\) support for Python less than 3\.8 by this collection has been deprecated and will removed in release 10\.0\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2195](https\://github\.com/ansible\-collections/community\.aws/pull/2195)\)\.

<a id="community-crypto-6"></a>
#### community\.crypto

* acme\_certificate \- deprecate the <code>agreement</code> option which has no more effect\. It will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/891](https\://github\.com/ansible\-collections/community\.crypto/pull/891)\)\.
* openssl\_pkcs12 \- deprecate the <code>maciter\_size</code> option which has no more effect\. It will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/891](https\://github\.com/ansible\-collections/community\.crypto/pull/891)\)\.

<a id="community-general-8"></a>
#### community\.general

* The proxmox content \(modules and plugins\) is being moved to the [new collection community\.proxmox](https\://github\.com/ansible\-collections/community\.proxmox)\. In community\.general 11\.0\.0\, these modules and plugins will be replaced by deprecated redirections to community\.proxmox\. You need to explicitly install community\.proxmox\, for example with <code>ansible\-galaxy collection install community\.proxmox</code>\. We suggest to update your roles and playbooks to use the new FQCNs as soon as possible to avoid getting deprecation messages \([https\://github\.com/ansible\-collections/community\.general/pull/10109](https\://github\.com/ansible\-collections/community\.general/pull/10109)\)\.
* pipx module\_utils \- function <code>make\_process\_list\(\)</code> is deprecated and will be removed in community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10031](https\://github\.com/ansible\-collections/community\.general/pull/10031)\)\.

<a id="community-postgresql"></a>
#### community\.postgresql

* postgresql modules \- the <code>port</code> alias is deprecated and will be removed in <code>community\.postgresql 5\.0\.0</code>\, use the <code>login\_port</code> argument instead\.

<a id="removed-features-previously-deprecated-1"></a>
### Removed Features \(previously deprecated\)

<a id="community-crypto-7"></a>
#### community\.crypto

* All Entrust content is being removed since the Entrust service in currently being sunsetted after the sale of Entrust\'s Public Certificates Business to Sectigo\; see [the announcement with key dates](https\://www\.entrust\.com/tls\-certificate\-information\-center) and [the migration brief for customers](https\://www\.sectigo\.com/uploads/resources/EOL\_Migration\-Brief\-End\-Customer\.pdf) for details\. Since this process will be completed in 2025\, we decided to remove all Entrust content from community\.general 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/issues/895](https\://github\.com/ansible\-collections/community\.crypto/issues/895)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/901](https\://github\.com/ansible\-collections/community\.crypto/pull/901)\)\.
* The collection no longer supports cryptography \< 3\.3 \([https\://github\.com/ansible\-collections/community\.crypto/pull/878](https\://github\.com/ansible\-collections/community\.crypto/pull/878)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/882](https\://github\.com/ansible\-collections/community\.crypto/pull/882)\)\.
* acme\.acme module utils \- the <code>get\_default\_argspec\(\)</code> function has been removed\. Use <code>create\_default\_argspec\(\)</code> instead \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* acme\.backends module utils \- the methods <code>get\_ordered\_csr\_identifiers\(\)</code> and <code>get\_cert\_information\(\)</code> of <code>CryptoBackend</code> now must be implemented \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* acme\.documentation docs fragment \- the <code>documentation</code> docs fragment has been removed\. Use both the <code>basic</code> and <code>account</code> docs fragments in <code>acme</code> instead \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* acme\_\* modules \- support for ACME v1 has been removed \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* community\.crypto no longer supports Ansible 2\.9\, ansible\-base 2\.10\, and ansible\-core versions 2\.11\, 2\.12\, 2\.13\, 2\.14\, 2\.15\, and 2\.16\. While content from this collection might still work with some older versions of ansible\-core\, it will not work with any Python version before 3\.7 \([https\://github\.com/ansible\-collections/community\.crypto/pull/870](https\://github\.com/ansible\-collections/community\.crypto/pull/870)\)\.
* crypto\.basic module utils \- remove <code>CRYPTOGRAPHY\_HAS\_\*</code> flags\. All tested features are supported since cryptography 3\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/878](https\://github\.com/ansible\-collections/community\.crypto/pull/878)\)\.
* crypto\.cryptography\_support module utils \- remove <code>cryptography\_serial\_number\_of\_cert\(\)</code> helper function \([https\://github\.com/ansible\-collections/community\.crypto/pull/878](https\://github\.com/ansible\-collections/community\.crypto/pull/878)\)\.
* crypto\.module\_backends\.common module utils \- this module utils has been removed\. Use the <code>argspec</code> module utils instead \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* crypto\.support module utils \- remove <code>pyopenssl</code> backend \([https\://github\.com/ansible\-collections/community\.crypto/pull/874](https\://github\.com/ansible\-collections/community\.crypto/pull/874)\)\.
* ecs\_certificate \- the module has been removed\. Please use community\.crypto 2\.x\.y if you need this module \([https\://github\.com/ansible\-collections/community\.crypto/pull/900](https\://github\.com/ansible\-collections/community\.crypto/pull/900)\)\.
* ecs\_domain \- the module has been removed\. Please use community\.crypto 2\.x\.y if you need this module \([https\://github\.com/ansible\-collections/community\.crypto/pull/900](https\://github\.com/ansible\-collections/community\.crypto/pull/900)\)\.
* execution environment dependencies \- remove PyOpenSSL dependency \([https\://github\.com/ansible\-collections/community\.crypto/pull/874](https\://github\.com/ansible\-collections/community\.crypto/pull/874)\)\.
* openssl\_csr\_pipe \- the module now ignores check mode and will always behave as if check mode is not active \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* openssl\_pkcs12 \- support for the <code>pyopenssl</code> backend has been removed \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* openssl\_privatekey\_pipe \- the module now ignores check mode and will always behave as if check mode is not active \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.
* time module utils \- remove <code>pyopenssl</code> backend \([https\://github\.com/ansible\-collections/community\.crypto/pull/874](https\://github\.com/ansible\-collections/community\.crypto/pull/874)\)\.
* x509\_certificate \- the <code>entrust</code> provider has been removed\. Please use community\.crypto 2\.x\.y if you need this provider \([https\://github\.com/ansible\-collections/community\.crypto/pull/900](https\://github\.com/ansible\-collections/community\.crypto/pull/900)\)\.
* x509\_certificate\_pipe \- the <code>entrust</code> provider has been removed\. Please use community\.crypto 2\.x\.y if you need this provider \([https\://github\.com/ansible\-collections/community\.crypto/pull/900](https\://github\.com/ansible\-collections/community\.crypto/pull/900)\)\.
* x509\_certificate\_pipe \- the module now ignores check mode and will always behave as if check mode is not active \([https\://github\.com/ansible\-collections/community\.crypto/pull/873](https\://github\.com/ansible\-collections/community\.crypto/pull/873)\)\.

<a id="bugfixes-5"></a>
### Bugfixes

<a id="ansible-core-16"></a>
#### Ansible\-core

* Core Jinja test plugins \- Builtin test plugins now always return <code>bool</code> to avoid spurious deprecation warnings for some malformed inputs\.
* ansible\-test \- Disabled the <code>bad\-super\-call</code> pylint rule due to false positives\.
* ansible\-test \- Fix incorrect handling of options with optional args \(e\.g\. <code>\-\-color</code>\)\, when followed by other options which are omitted during arg filtering \(e\.g\. <code>\-\-docker</code>\)\. Previously it was possible for non\-option arguments to be incorrectly omitted in these cases\. \([https\://github\.com/ansible/ansible/issues/85173](https\://github\.com/ansible/ansible/issues/85173)\)
* ansible\-test \- Improve type inference for pylint deprecated checks to accommodate some type annotations\.
* async\_status module \- The <code>started</code> and <code>finished</code> return values are now <code>True</code> or <code>False</code> instead of <code>1</code> or <code>0</code>\.
* constructed inventory \- Use the <code>default\_value</code> or <code>trailing\_separator</code> in a <code>keyed\_groups</code> entry if the expression result of <code>key</code> is <code>None</code> and not just an empty string\.
* dnf5 \- handle all libdnf5 specific exceptions \([https\://github\.com/ansible/ansible/issues/84634](https\://github\.com/ansible/ansible/issues/84634)\)
* error handling \- Error details and tracebacks from connection and built\-in action exceptions are preserved\. Previously\, much of the detail was lost or mixed into the error message\.
* from\_yaml\_all filter \- <em class="title-reference">None</em> and empty string inputs now always return an empty list\. Previously\, <em class="title-reference">None</em> was returned in Jinja native mode and empty list in classic mode\.
* local connection plugin \- The command\-line used to create subprocesses is now always <code>str</code> to avoid issues with debuggers and profilers\.
* ssh agent \- Fixed several potential startup hangs for badly\-behaved or overloaded ssh agents\.
* task timeout \- Specifying a negative task timeout now results in an error\.

<a id="amazon-aws-3"></a>
#### amazon\.aws

* s3\_bucket \- bucket ACLs now consistently returned \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2478](https\://github\.com/ansible\-collections/amazon\.aws/pull/2478)\)\.
* s3\_bucket \- fixed idempotency when setting bucket ACLs \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2478](https\://github\.com/ansible\-collections/amazon\.aws/pull/2478)\)\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* win\_package \- fail to remove package when no product id is provided with path as an URL \([https\://github\.com/ansible\-collections/ansible\.windows/issues/667](https\://github\.com/ansible\-collections/ansible\.windows/issues/667)\)\.

<a id="check-point-mgmt"></a>
#### check\_point\.mgmt

* Added required management version to the documentation for all collection modules\.
* module\_utils/checkpoint \- Prevent redundant logout call when there is no authentication header \'X\-chkp\-sid\'\.

<a id="cisco-ios-2"></a>
#### cisco\.ios

* cisco\.ios\.ios\_interfaces \- Improved handling of the <em class="title-reference">enabled</em> state to prevent incorrect <em class="title-reference">shutdown</em> or <em class="title-reference">no shutdown</em> commands during configuration changes\.
* ios\_acls \- Fix issue where commands were not being parsed correctly and incorrect commands were being generated\.
* ios\_bgp\_address\_family \- fix configuration of neighbor\'s as\-override split\-horizon\.

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Fixes route map fact gathering to correctly gather facts with a elif condition\.
* cisco\.iosxr\.iosxr\_interfaces \- Improved handling of the <em class="title-reference">enabled</em> state to prevent incorrect <em class="title-reference">shutdown</em> or <em class="title-reference">no shutdown</em> commands during configuration changes\.
* iosxr\_route\_maps \- Fix issue where wrong commands were being generated for several attributes\.

<a id="cisco-meraki-2"></a>
#### cisco\.meraki

* cisco\.meraki\.networks\_appliance\_firewall\_l7\_firewall\_rules \- fix idempotency error\.

<a id="cloudscale-ch-cloud-1"></a>
#### cloudscale\_ch\.cloud

* floating\_ip \- Fix sanity tests\.

<a id="community-dns-2"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-9"></a>
#### community\.general

* cobbler\_system \- fix bug with Cobbler \>\= 3\.4\.0 caused by giving more than 2 positional arguments to <code>CobblerXMLRPCInterface\.get\_system\_handle\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8506](https\://github\.com/ansible\-collections/community\.general/issues/8506)\, [https\://github\.com/ansible\-collections/community\.general/pull/10145](https\://github\.com/ansible\-collections/community\.general/pull/10145)\)\.
* kdeconfig \- allow option values beginning with a dash \([https\://github\.com/ansible\-collections/community\.general/issues/10127](https\://github\.com/ansible\-collections/community\.general/issues/10127)\, [https\://github\.com/ansible\-collections/community\.general/pull/10128](https\://github\.com/ansible\-collections/community\.general/pull/10128)\)\.
* keycloak\_user\_rolemapping \- fix <code>\-\-diff</code> mode \([https\://github\.com/ansible\-collections/community\.general/issues/10067](https\://github\.com/ansible\-collections/community\.general/issues/10067)\, [https\://github\.com/ansible\-collections/community\.general/pull/10075](https\://github\.com/ansible\-collections/community\.general/pull/10075)\)\.
* pickle cache plugin \- avoid extra JSON serialization with ansible\-core \>\= 2\.19 \([https\://github\.com/ansible\-collections/community\.general/pull/10136](https\://github\.com/ansible\-collections/community\.general/pull/10136)\)\.
* proxmox \- fix crash in module when the used on an existing LXC container with <code>state\=present</code> and <code>force\=true</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/91](https\://github\.com/ansible\-collections/community\.proxmox/pull/91)\, [https\://github\.com/ansible\-collections/community\.general/pull/10155](https\://github\.com/ansible\-collections/community\.general/pull/10155)\)\.
* rundeck\_acl\_policy \- ensure that project ACLs are sent to the correct endpoint \([https\://github\.com/ansible\-collections/community\.general/pull/10097](https\://github\.com/ansible\-collections/community\.general/pull/10097)\)\.
* sysrc \- split the output of <code>sysrc \-e \-a</code> on the first <code>\=</code> only \([https\://github\.com/ansible\-collections/community\.general/issues/10120](https\://github\.com/ansible\-collections/community\.general/issues/10120)\, [https\://github\.com/ansible\-collections/community\.general/pull/10121](https\://github\.com/ansible\-collections/community\.general/pull/10121)\)\.

<a id="community-mysql-1"></a>
#### community\.mysql

* mysql\_info \- fix a crash \(ERROR 1141\, There is no such grant defined for user \'PUBLIC\' on host \'\%\'\) when using the <code>users\_info</code> filter with a PUBLIC role present in MariaDB 10\.11\+\. Do note that the fix doesn\'t change the fact that the module won\'t return the privileges from the PUBLIC role in the users privileges list\. It can\'t do that because you have to login as the particular user and use <em class="title-reference">SHOW GRANTS FOR CURRENT\_USER</em>\. We considered using an aggregation with the <em class="title-reference">SHOW GRANTS FOR PUBLIC</em> command\. However\, this approach would make copying users from one server to another transform the privileges inherited from the role as if they were direct privileges on the user\.
* mysql\_replication \- fixed an issue where setting <code>primary\_ssl\_verify\_server\_cert</code> to false had no effect \([https\://github\.com/ansible\-collections/community\.mysql/issues/689](https\://github\.com/ansible\-collections/community\.mysql/issues/689)\)\.

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_alter\_system \- fix failure when max\_val contains a huge number written in scientific notation \([https\://github\.com/ansible\-collections/community\.postgresql/issues/853](https\://github\.com/ansible\-collections/community\.postgresql/issues/853)\)\.
* postgresql\_schema \- change reported in check\_mode was negated\. Now it reports a change when removing an existing schema \([https\://github\.com/ansible\-collections/community\.postgresql/pull/858](https\://github\.com/ansible\-collections/community\.postgresql/pull/858)\)

<a id="community-rabbitmq-1"></a>
#### community\.rabbitmq

* rabbitmq\_binding \- fix idempotency when arguments and/or routing\_key are given \([https\://github\.com/ansible\-collections/community\.rabbitmq/pull/191](https\://github\.com/ansible\-collections/community\.rabbitmq/pull/191)\)

<a id="f5networks-f5-modules-1"></a>
#### f5networks\.f5\_modules

* bigip\_virtual\_server fix module crash issue

<a id="hitachivantara-vspone-block-5"></a>
#### hitachivantara\.vspone\_block

* Fixed the mapping lun to multiple HostGroup/Iscsi Target issues for remote replication\.
* Resolved various documentation inconsistencies\.

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_ssh \- Added fix for nginx timeout
* ibm\_svc\_utils \- Added fix for nginx timeout

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* module\_utils/k8s/service \- fix issue when trying to delete resource using <em class="title-reference">delete\_options</em> and <em class="title-reference">check\_mode\=true</em> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/892](https\://github\.com/ansible\-collections/kubernetes\.core/issues/892)\)\.

<a id="microsoft-ad"></a>
#### microsoft\.ad

* microsoft\.ad\.ldap \- Ensure the encrypted LAPS value is marked as unsafe to stop unexpected templating of the raw JSON result value \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/194](https\://github\.com/ansible\-collections/microsoft\.ad/issues/194)

<a id="ovirt-ovirt-1"></a>
#### ovirt\.ovirt

* ovirt\_disk \- fix documentation for lun\_id parameter \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/740](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/740)\)
* ovirt\_proxied\_check \- fix documentation string \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/761](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/761)\)
* roles \- Fix ansible\-test errors change include to include\_tasks \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/733](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/733)\)\.

<a id="vmware-vmware-4"></a>
#### vmware\.vmware

* cluster\_ha \- fix typo that causes PDL response mode \'restart\' to throw an error
* deploy\_\* \- Fix issue where datastore was expected even though it is optional
* deploy\_content\_library\_ovf \- fix error when deploying from a datastore cluster by simplifying the ds selection process
* inventory plugins \- fix issue where cache did not work \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/175](https\://github\.com/ansible\-collections/vmware\.vmware/issues/175)\)

<a id="known-issues-2"></a>
### Known Issues

<a id="dellemc-openmanage-3"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins-1"></a>
### New Plugins

<a id="callback-1"></a>
#### Callback

* community\.general\.print\_task \- Prints playbook task snippet to job output\.

<a id="filter-1"></a>
#### Filter

* community\.general\.to\_prettytable \- Format a list of dictionaries as an ASCII table\.

<a id="new-modules-4"></a>
### New Modules

<a id="cloudscale-ch-cloud-2"></a>
#### cloudscale\_ch\.cloud

* cloudscale\_ch\.cloud\.volume\_snapshot \- Manage volume snapshots on the cloudscale\.ch IaaS service

<a id="community-general-10"></a>
#### community\.general

* community\.general\.xdg\_mime \- Set default handler for MIME types\, for applications using XDG tools\.

<a id="community-libvirt-1"></a>
#### community\.libvirt

* community\.libvirt\.virt\_volume \- Manage libvirt volumes inside a storage pool

<a id="unchanged-collections-5"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 5\.1\.2\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.docker \(still version 4\.6\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.3\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.0\.5\)
* community\.vmware \(still version 5\.6\.0\)
* community\.windows \(still version 3\.0\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.1\)
* ibm\.qradar \(still version 4\.0\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.0\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* purestorage\.flasharray \(still version 1\.34\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 5\.3\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a4"></a>
## v12\.0\.0a4

- <a href="#release-summary-6">Release Summary</a>
- <a href="#ansible-core-17">Ansible\-core</a>
- <a href="#changed-collections-6">Changed Collections</a>
- <a href="#major-changes-3">Major Changes</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
- <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#ansible-core-18">Ansible\-core</a>
    - <a href="#amazon-aws-4">amazon\.aws</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
- <a href="#bugfixes-6">Bugfixes</a>
    - <a href="#ansible-core-19">Ansible\-core</a>
    - <a href="#amazon-aws-5">amazon\.aws</a>
    - <a href="#cisco-meraki-3">cisco\.meraki</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
- <a href="#new-modules-5">New Modules</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
- <a href="#unchanged-collections-6">Unchanged Collections</a>

<a id="release-summary-6"></a>
### Release Summary

Release Date\: 2025\-05\-12

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-17"></a>
### Ansible\-core

Ansible 12\.0\.0a4 contains ansible\-core version 2\.19\.0b4\.
This is a newer version than version 2\.19\.0b3 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-6"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection   | Ansible 12.0.0a3 | Ansible 12.0.0a4 | Notes                                                                                                                        |
| ------------ | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws   | 9.4.0            | 9.5.0            |                                                                                                                              |
| cisco.meraki | 2.21.0           | 2.21.1           |                                                                                                                              |
| cyberark.pas | 1.0.32           | 1.0.35           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| netapp.ontap | 22.14.0          | 23.0.0           |                                                                                                                              |

<a id="major-changes-3"></a>
### Major Changes

<a id="netapp-ontap"></a>
#### netapp\.ontap

* library <em class="title-reference">netapp\-lib</em> is now an optional requirement\.
* na\_ontap\_lun \- added compatibility for ASA r2 systems\.
* na\_ontap\_lun\_copy \- added check to prevent use on unsupported ASA r2 systems\.
* na\_ontap\_lun\_map \- added compatibility for ASA r2 systems\.
* na\_ontap\_lun\_map\_reporting\_nodes \- added compatibility for ASA r2 systems\.
* na\_ontap\_nvme\_namespace \- added compatibility for ASA r2 systems\.
* na\_ontap\_nvme\_subsystem \- added compatibility for ASA r2 systems\.

<a id="minor-changes-6"></a>
### Minor Changes

<a id="ansible-core-18"></a>
#### Ansible\-core

* facts \- add \"CloudStack KVM Hypervisor\" for Linux VM in virtual facts \([https\://github\.com/ansible/ansible/issues/85089](https\://github\.com/ansible/ansible/issues/85089)\)\.
* modules \- use <code>AnsibleModule\.warn</code> instead of passing <code>warnings</code> to <code>exit\_json</code> or <code>fail\_json</code> which is deprecated\.

<a id="amazon-aws-4"></a>
#### amazon\.aws

* Bump version of ansible\-lint to 25\.1\.2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2590](https\://github\.com/ansible\-collections/amazon\.aws/pull/2590)\)\.
* iam\_user\_info \- Add tags to ListUsers or GetGroup results \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* iam\_user\_info \- Return empty user list when invalid group name is provided instead of python error \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* module\_utils/modules\.py \- call to <code>deprecate\(\)</code> without specifying <code>collection\_name</code>\, <code>version</code> or <code>date</code> arguments raises a sanity errors \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2607](https\://github\.com/ansible\-collections/amazon\.aws/pull/2607)\)\.

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* all modules \- defaults to certificate based authentication if <em class="title-reference">username\,password</em> and <em class="title-reference">cert\_filepath/key\_filepath</em> are set\.
* na\_ontap\_ndmp \- Added get method to generate and retrieve ndmp user passowrd in REST\.
* na\_ontap\_volume \- updated documentation for <em class="title-reference">snapshot\_auto\_delete</em>\.
* updated ZAPI deprecation warnings in README \& module utilities\.

<a id="bugfixes-6"></a>
### Bugfixes

<a id="ansible-core-19"></a>
#### Ansible\-core

* ansible\-test \- Updated the <code>pylint</code> sanity test to skip some deprecation validation checks when all arguments are dynamic\.
* config \- Preserve or apply Origin tag to values returned by config\.
* config \- Prevented fatal errors when <code>MODULE\_IGNORE\_EXTS</code> configuration was set\.
* config \- Templating failures on config defaults now issue a warning\. Previously\, failures silently returned an unrendered and untrusted template to the caller\.
* config \- <code>ensure\_type</code> correctly propagates trust and other tags on returned values\.
* config \- <code>ensure\_type</code> now converts mappings to <code>dict</code> when requested\, instead of returning the mapping\.
* config \- <code>ensure\_type</code> now converts sequences to <code>list</code> when requested\, instead of returning the sequence\.
* config \- <code>ensure\_type</code> now correctly errors when <code>pathlist</code> or <code>pathspec</code> types encounter non\-string list items\.
* config \- <code>ensure\_type</code> now reports an error when <code>bytes</code> are provided for any known <code>value\_type</code>\. Previously\, the behavior was undefined\, but often resulted in an unhandled exception or incorrect return type\.
* config \- <code>ensure\_type</code> with expected type <code>int</code> now properly converts <code>True</code> and <code>False</code> values to <code>int</code>\. Previously\, these values were silently returned unmodified\.
* convert\_bool\.boolean API conversion function \- Unhashable values passed to <code>boolean</code> behave like other non\-boolean convertible values\, returning False or raising <code>TypeError</code> depending on the value of <code>strict</code>\. Previously\, unhashable values always raised <code>ValueError</code> due to an invalid set membership check\.
* dnf5 \- when <code>bugfix</code> and/or <code>security</code> is specified\, skip packages that do not have any such updates\, even for new versions of libdnf5 where this functionality changed and it is considered failure
* plugin loader \- Apply template trust to strings loaded from plugin configuration definitions and doc fragments\.
* template action \- Template files where the entire file\'s output renders as <code>None</code> are no longer emitted as the string \"None\"\, but instead render to an empty file as in previous releases\.

<a id="amazon-aws-5"></a>
#### amazon\.aws

* iam\_user\_info \- Actually call GetUser when only user name is supplied instead of listing and filtering from all users \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* iam\_user\_info \- Actually filter users by path prefix when one is provided \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2567](https\://github\.com/ansible\-collections/amazon\.aws/pull/2567)\)\.
* route53\_info \- removes jijna delimiters from example using when \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2594](https\://github\.com/ansible\-collections/amazon\.aws/issues/2594)\)\.

<a id="cisco-meraki-3"></a>
#### cisco\.meraki

* cisco\.meraki\.devices\_switch\_ports \- fix get\_object\_by\_name method\.

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* na\_ontap\_ems\_config \- fix issue with support check mode when proxy\_password is not set in REST\.
* na\_ontap\_quotas \- changed examples in documentation for <em class="title-reference">type</em>\.
* na\_ontap\_snapmirror \- fix delete snapmirror timeout issue by retrying in REST\.
* na\_ontap\_software\_update \- Updated documentation for <em class="title-reference">https</em>\.
* na\_ontap\_user\_role \- fix issue with modifying privileges in REST\.

<a id="new-modules-5"></a>
### New Modules

<a id="netapp-ontap-3"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_mav\_approval\_group \- NetApp ONTAP multi\-admin verification \(MAV\) approval group
* netapp\.ontap\.na\_ontap\_mav\_config \- NetApp ONTAP multi\-admin verification \(MAV\) global setting
* netapp\.ontap\.na\_ontap\_mav\_rule \- NetApp ONTAP multi\-admin verification \(MAV\) rule
* netapp\.ontap\.na\_ontap\_storage\_unit \- NetApp ONTAP ASA r2 storage unit
* netapp\.ontap\.na\_ontap\_storage\_unit\_snapshot \- NetApp ONTAP ASA r2 storage unit snapshot
* netapp\.ontap\.na\_ontap\_support\_config\_backup \- NetApp ONTAP support configuration backup

<a id="unchanged-collections-6"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 3\.0\.0\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.3\.1\)
* check\_point\.mgmt \(still version 6\.4\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ios \(still version 10\.0\.0\)
* cisco\.iosxr \(still version 11\.0\.0\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.aws \(still version 9\.3\.0\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.crypto \(still version 2\.26\.1\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.2\.3\)
* community\.docker \(still version 4\.6\.0\)
* community\.general \(still version 10\.6\.0\)
* community\.grafana \(still version 2\.2\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.hrobot \(still version 2\.3\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.3\.1\)
* community\.mongodb \(still version 1\.7\.9\)
* community\.mysql \(still version 3\.13\.0\)
* community\.okd \(still version 4\.0\.1\)
* community\.postgresql \(still version 4\.0\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.routeros \(still version 3\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.0\.5\)
* community\.vmware \(still version 5\.6\.0\)
* community\.windows \(still version 3\.0\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.conjur \(still version 1\.3\.3\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.openmanage \(still version 9\.12\.0\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.35\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* grafana\.grafana \(still version 6\.0\.1\)
* hetzner\.hcloud \(still version 4\.3\.0\)
* hitachivantara\.vspone\_block \(still version 3\.4\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.3\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.2\.0\)
* kubevirt\.core \(still version 2\.2\.0\)
* lowlydba\.sqlserver \(still version 2\.6\.1\)
* microsoft\.ad \(still version 1\.9\.0\)
* microsoft\.iis \(still version 1\.0\.2\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.storagegrid \(still version 21\.14\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* purestorage\.flasharray \(still version 1\.34\.1\)
* purestorage\.flashblade \(still version 1\.20\.0\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 5\.3\.0\)
* vmware\.vmware \(still version 2\.0\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a3"></a>
## v12\.0\.0a3

- <a href="#release-summary-7">Release Summary</a>
- <a href="#ansible-core-20">Ansible\-core</a>
- <a href="#changed-collections-7">Changed Collections</a>
- <a href="#major-changes-4">Major Changes</a>
    - <a href="#community-postgresql-2">community\.postgresql</a>
    - <a href="#dellemc-openmanage-4">dellemc\.openmanage</a>
    - <a href="#vmware-vmware-5">vmware\.vmware</a>
- <a href="#minor-changes-7">Minor Changes</a>
    - <a href="#ansible-core-21">Ansible\-core</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#community-aws-3">community\.aws</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-grafana">community\.grafana</a>
    - <a href="#community-postgresql-3">community\.postgresql</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#grafana-grafana-1">grafana\.grafana</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-6">vmware\.vmware</a>
- <a href="#breaking-changes--porting-guide-3">Breaking Changes / Porting Guide</a>
    - <a href="#vmware-vmware-7">vmware\.vmware</a>
- <a href="#deprecated-features-5">Deprecated Features</a>
    - <a href="#ansible-core-22">Ansible\-core</a>
    - <a href="#community-postgresql-4">community\.postgresql</a>
    - <a href="#community-windows-1">community\.windows</a>
- <a href="#removed-features-previously-deprecated-2">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-windows-3">ansible\.windows</a>
    - <a href="#community-postgresql-5">community\.postgresql</a>
    - <a href="#community-windows-2">community\.windows</a>
    - <a href="#vmware-vmware-8">vmware\.vmware</a>
- <a href="#bugfixes-7">Bugfixes</a>
    - <a href="#ansible-core-23">Ansible\-core</a>
    - <a href="#ansible-windows-4">ansible\.windows</a>
    - <a href="#community-crypto-8">community\.crypto</a>
    - <a href="#community-grafana-1">community\.grafana</a>
    - <a href="#community-windows-3">community\.windows</a>
    - <a href="#dellemc-openmanage-5">dellemc\.openmanage</a>
    - <a href="#microsoft-ad-2">microsoft\.ad</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-9">vmware\.vmware</a>
- <a href="#known-issues-3">Known Issues</a>
    - <a href="#dellemc-openmanage-6">dellemc\.openmanage</a>
- <a href="#new-modules-6">New Modules</a>
    - <a href="#community-hrobot-5">community\.hrobot</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
- <a href="#unchanged-collections-7">Unchanged Collections</a>

<a id="release-summary-7"></a>
### Release Summary

Release Date\: 2025\-05\-06

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-20"></a>
### Ansible\-core

Ansible 12\.0\.0a3 contains ansible\-core version 2\.19\.0b3\.
This is a newer version than version 2\.19\.0b2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-7"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 12.0.0a2 | Ansible 12.0.0a3 | Notes                                                                                                                        |
| ---------------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ansible.windows        | 2.8.0            | 3.0.0            |                                                                                                                              |
| community.aws          | 9.2.0            | 9.3.0            |                                                                                                                              |
| community.crypto       | 2.26.0           | 2.26.1           |                                                                                                                              |
| community.docker       | 4.5.2            | 4.6.0            |                                                                                                                              |
| community.grafana      | 2.1.0            | 2.2.0            |                                                                                                                              |
| community.hrobot       | 2.2.0            | 2.3.0            |                                                                                                                              |
| community.postgresql   | 3.14.0           | 4.0.0            |                                                                                                                              |
| community.windows      | 2.4.0            | 3.0.0            |                                                                                                                              |
| cyberark.pas           | 1.0.30           | 1.0.32           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| dellemc.openmanage     | 9.11.0           | 9.12.0           |                                                                                                                              |
| grafana.grafana        | 6.0.0            | 6.0.1            |                                                                                                                              |
| kubevirt.core          | 2.1.0            | 2.2.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| lowlydba.sqlserver     | 2.6.0            | 2.6.1            |                                                                                                                              |
| microsoft.ad           | 1.8.1            | 1.9.0            |                                                                                                                              |
| purestorage.flashblade | 1.19.2           | 1.20.0           |                                                                                                                              |
| vmware.vmware          | 1.11.0           | 2.0.0            |                                                                                                                              |

<a id="major-changes-4"></a>
### Major Changes

<a id="community-postgresql-2"></a>
#### community\.postgresql

* the collection does not test against Python 2 and starts accepting content written in Python 3 since collection version 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.postgresql/issues/829](https\://github\.com/ansible\-collections/community\.postgresql/issues/829)\)\.

<a id="dellemc-openmanage-4"></a>
#### dellemc\.openmanage

* idrac\_gather\_facts \- This role is enhanced to support iDRAC10\.
* idrac\_lifecycle\_controller\_job\_status\_info \- This module is enhanced to support iDRAC10\.
* idrac\_system\_info \- This module is enhanced to support iDRAC10\.

<a id="vmware-vmware-5"></a>
#### vmware\.vmware

* cluster modules \- Add identifying information about the cluster managed to the output of cluster modules
* folder\_paths \- Throw an error when a relative folder path is provided and the datacenter name is not provided
* module\_utils/argument\_spec \- make argument specs public so other collections can use them [https\://github\.com/ansible\-collections/vmware\.vmware/issues/144](https\://github\.com/ansible\-collections/vmware\.vmware/issues/144)
* module\_utils/clients \- make client utils public so other collections can use them [https\://github\.com/ansible\-collections/vmware\.vmware/issues/144](https\://github\.com/ansible\-collections/vmware\.vmware/issues/144)
* update query file to include cluster module queries

<a id="minor-changes-7"></a>
### Minor Changes

<a id="ansible-core-21"></a>
#### Ansible\-core

* ansible\-config will now show internal\, but not test configuration entries\. This allows for debugging but still denoting the configurations as internal use only \(\_ prefix\)\.
* ansible\-test \- Improved <code>pylint</code> checks for Ansible\-specific deprecation functions\.
* ansible\-test \- Use the <code>\-t</code> option to set the stop timeout when stopping a container\. This avoids use of the <code>\-\-time</code> option which was deprecated in Docker v28\.0\.
* collection metadata \- The collection loader now parses scalar values from <code>meta/runtime\.yml</code> as strings\. This avoids issues caused by unquoted values such as versions or dates being parsed as types other than strings\.
* deprecation warnings \- Deprecation warning APIs automatically capture the identity of the deprecating plugin\. The <code>collection\_name</code> argument is only required to correctly attribute deprecations that occur in module\_utils or other non\-plugin code\.
* deprecation warnings \- Improved deprecation messages to more clearly indicate the affected content\, including plugin name when available\.
* deprecations \- Collection name strings not of the form <code>ns\.coll</code> passed to deprecation API functions will result in an error\.
* deprecations \- Removed support for specifying deprecation dates as a <code>datetime\.date</code>\, which was included in an earlier 2\.19 pre\-release\.
* deprecations \- Some argument names to <code>deprecate\_value</code> for consistency with existing APIs\. An earlier 2\.19 pre\-release included a <code>removal\_</code> prefix on the <code>date</code> and <code>version</code> arguments\.
* modules \- The <code>AnsibleModule\.deprecate</code> function no longer sends deprecation messages to the target host\'s logging system\.

<a id="ansible-windows-2"></a>
#### ansible\.windows

* Set minimum supported Ansible version to 2\.16 to align with the versions still supported by Ansible\.
* win\_template \- Added <code>comment\_start\_string</code> and <code>comment\_end\_string</code> as options to align with the builtin <code>template</code> module\.

<a id="community-aws-3"></a>
#### community\.aws

* Bump version of ansible\-lint to 25\.1\.2 \([https\://github\.com/ansible\-collections/community\.aws/pull/2295](https\://github\.com/ansible\-collections/community\.aws/pull/2295)\)\.
* aws\_ssm \- Move the <code>aws\_ssm</code> connection plugin\'s plugin\_utils into a dedicated folder \([https\://github\.com/ansible\-collections/community\.aws/pull/2279](https\://github\.com/ansible\-collections/community\.aws/pull/2279)\)\.
* aws\_ssm \- Refactor S3 operations methods for improved clarity \([https\://github\.com/ansible\-collections/community\.aws/pull/2275](https\://github\.com/ansible\-collections/community\.aws/pull/2275)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new TerminalManager class and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2270](https\://github\.com/ansible\-collections/community\.aws/pull/2270)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new <code>FileTransferManager</code> class and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2273](https\://github\.com/ansible\-collections/community\.aws/pull/2273)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new <code>SSMSessionManager</code> and <code>ProcessManager</code> classes and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2272](https\://github\.com/ansible\-collections/community\.aws/pull/2272)\)\.

<a id="community-docker-1"></a>
#### community\.docker

* docker\_container\_copy\_into \- add <code>mode\_parse</code> parameter which determines how <code>mode</code> is parsed \([https\://github\.com/ansible\-collections/community\.docker/pull/1074](https\://github\.com/ansible\-collections/community\.docker/pull/1074)\)\.

<a id="community-grafana"></a>
#### community\.grafana

* Add argument <em class="title-reference">tls\_servername</em> for <em class="title-reference">grafana\_datasource</em>
* Support <em class="title-reference">alertmanager</em> as type for <em class="title-reference">grafana\_datasource</em>
* grafana\_dashboard \- allow creating dashboards in subfolders

<a id="community-postgresql-3"></a>
#### community\.postgresql

* postgresql\_user \- return a PostgreSQL error message when a user cannot be removed\.

<a id="community-windows"></a>
#### community\.windows

* Set minimum supported Ansible version to 2\.16 to align with the versions still supported by Ansible\.

<a id="grafana-grafana-1"></a>
#### grafana\.grafana

* Remove Node modules from Ansible Collection build

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

<a id="vmware-vmware-6"></a>
#### vmware\.vmware

* Warn the user when more than one host has the same name in the inventory plugins\. Throw an error if strict is true
* content\_template \- Added more options to search for the source VM like uuid and moid\. Also made argument validation more accurate
* guest\_info \- Allow user to specify folder path to help select the VM to query
* rename private module\_utils to drop the redundant vmware prefix
* vcsa\_backup\_schedule \- Add module to manage the vCenter backup schedule
* vcsa\_backup\_schedule\_info \- Add module to gather info about the vCenter backup schedules
* vm\_advanced\_settings \- Add module to manage the advanced settings on a VM
* vm\_powerstate \- Add better error message when scheduling a power state task in the past
* vm\_snapshot \- migrate vmware\_guest\_snapshot module from community to here
* vms inventory \- Fixed issue where a user could accidentally not collect a required parameter\, config\.guestId

<a id="breaking-changes--porting-guide-3"></a>
### Breaking Changes / Porting Guide

<a id="vmware-vmware-7"></a>
#### vmware\.vmware

* drop support for ansible 2\.15 since it is EOL [https\://github\.com/ansible\-collections/vmware\.vmware/issues/103](https\://github\.com/ansible\-collections/vmware\.vmware/issues/103)
* updated minimum pyVmomi version to 8\.0\.3\.0\.1 [https\://github\.com/ansible\-collections/vmware\.vmware/issues/56](https\://github\.com/ansible\-collections/vmware\.vmware/issues/56)

<a id="deprecated-features-5"></a>
### Deprecated Features

<a id="ansible-core-22"></a>
#### Ansible\-core

* Passing a <code>warnings\` or \`\`deprecations</code> key to <code>exit\_json</code> or <code>fail\_json</code> is deprecated\. Use <code>AnsibleModule\.warn</code> or <code>AnsibleModule\.deprecate</code> instead\.
* plugins \- Accessing plugins with <code>\_</code>\-prefixed filenames without the <code>\_</code> prefix is deprecated\.

<a id="community-postgresql-4"></a>
#### community\.postgresql

* postgresql modules \= the <code>login</code>\, <code>unix\_socket</code> and <code>host</code> aliases are deprecated and will be removed in <code>community\.postgresql 5\.0\.0</code>\, use the <code>login\_user</code>\, <code>login\_unix\_socket</code> and <code>login\_host</code> arguments instead\.
* postgresql\_set \- the module has been deprecated and will be removed in <code>community\.postgresql 5\.0\.0</code>\. Please use the <code>community\.postgresql\.postgresql\_alter\_system</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/823](https\://github\.com/ansible\-collections/community\.postgresql/issues/823)\)\.

<a id="community-windows-1"></a>
#### community\.windows

* win\_audit\_policy\_system \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_audit\_policy\_system</code>\. Use <code>ansible\.windows\.win\_audit\_policy\_system</code> instead as the redirection will be removed in 4\.0\.0
* win\_audit\_rule \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_audit\_rule</code>\. Use <code>ansible\.windows\.win\_audit\_rule</code> instead as the redirection will be removed in 4\.0\.0
* win\_auto\_logon \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_auto\_logon</code>\. Use <code>ansible\.windows\.win\_auto\_logon</code> instead as the redirection will be removed in 4\.0\.0
* win\_certificate\_info \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_certificate\_info</code>\. Use <code>ansible\.windows\.win\_certificate\_info</code> instead as the redirection will be removed in 4\.0\.0
* win\_computer\_description \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_computer\_description</code>\. Use <code>ansible\.windows\.win\_computer\_description</code> instead as the redirection will be removed in 4\.0\.0
* win\_credential \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_credential</code>\. Use <code>ansible\.windows\.win\_credential</code> instead as the redirection will be removed in 4\.0\.0
* win\_dhcp\_lease \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_dhcp\_lease</code>\. Use <code>ansible\.windows\.win\_dhcp\_lease</code> instead as the redirection will be removed in 4\.0\.0
* win\_dns\_record \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_dns\_record</code>\. Use <code>ansible\.windows\.win\_dns\_record</code> instead as the redirection will be removed in 4\.0\.0
* win\_dns\_zone \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_dns\_zone</code>\. Use <code>ansible\.windows\.win\_dns\_zone</code> instead as the redirection will be removed in 4\.0\.0
* win\_eventlog \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_eventlog</code>\. Use <code>ansible\.windows\.win\_eventlog</code> instead as the redirection will be removed in 4\.0\.0
* win\_feature\_info \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_feature\_info</code>\. Use <code>ansible\.windows\.win\_feature\_info</code> instead as the redirection will be removed in 4\.0\.0
* win\_file\_compression \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_file\_compression</code>\. Use <code>ansible\.windows\.win\_file\_compression</code> instead as the redirection will be removed in 4\.0\.0
* win\_firewall \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_firewall</code>\. Use <code>ansible\.windows\.win\_firewall</code> instead as the redirection will be removed in 4\.0\.0
* win\_hosts \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_hosts</code>\. Use <code>ansible\.windows\.win\_hosts</code> instead as the redirection will be removed in 4\.0\.0
* win\_hotfix \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_hotfix</code>\. Use <code>ansible\.windows\.win\_hotfix</code> instead as the redirection will be removed in 4\.0\.0
* win\_http\_proxy \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_http\_proxy</code>\. Use <code>ansible\.windows\.win\_http\_proxy</code> instead as the redirection will be removed in 4\.0\.0
* win\_iis\_virtualdirectory \- Deprecated module\, use <code>microsoft\.iis\.virtual\_directory</code> instead as the module will be removed in 4\.0\.0
* win\_iis\_webapplication \- Deprecated module\, use <code>microsoft\.iis\.web\_application</code> instead instead as the module will be removed in 4\.0\.0
* win\_iis\_webapppool \- Deprecated module\, use <code>microsoft\.iis\.web\_app\_pool</code> instead instead as the module will be removed in 4\.0\.0
* win\_iis\_webbinding \- Deprecated module\, use <code>microsoft\.iis\.website</code> instead instead as the module will be removed in 4\.0\.0
* win\_iis\_website \- Deprecated module\, use <code>microsoft\.iis\.website</code> instead instead as the module will be removed in 4\.0\.0
* win\_inet\_proxy \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_inet\_proxy</code>\. Use <code>ansible\.windows\.win\_inet\_proxy</code> instead as the redirection will be removed in 4\.0\.0
* win\_listen\_ports\_facts \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_listen\_ports\_facts</code>\. Use <code>ansible\.windows\.win\_listen\_ports\_facts</code> instead as the redirection will be removed in 4\.0\.0
* win\_mapped\_drive \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_mapped\_drive</code>\. Use <code>ansible\.windows\.win\_mapped\_drive</code> instead as the redirection will be removed in 4\.0\.0
* win\_product\_facts \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_product\_facts</code>\. Use <code>ansible\.windows\.win\_product\_facts</code> instead as the redirection will be removed in 4\.0\.0
* win\_region \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_region</code>\. Use <code>ansible\.windows\.win\_region</code> instead as the redirection will be removed in 4\.0\.0
* win\_route \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_route</code>\. Use <code>ansible\.windows\.win\_route</code> instead as the redirection will be removed in 4\.0\.0
* win\_timezone \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_timezone</code>\. Use <code>ansible\.windows\.win\_timezone</code> instead as the redirection will be removed in 4\.0\.0
* win\_user\_profile \- Deprecated module and will be redirected to <code>ansible\.windows\.win\_user\_profile</code>\. Use <code>ansible\.windows\.win\_user\_profile</code> instead as the redirection will be removed in 4\.0\.0

<a id="removed-features-previously-deprecated-2"></a>
### Removed Features \(previously deprecated\)

<a id="ansible-windows-3"></a>
#### ansible\.windows

* win\_domain \- Removed deprecated module\, use <code>microsoft\.ad\.domain</code> instead
* win\_domain\_controller \- Removed deprecated module\, use <code>microsoft\.ad\.domain\_controller</code> instead
* win\_domain\_membership \- Removed deprecated module\, use <code>microsoft\.ad\.membership</code> instead
* win\_feature \- Removed deprecated return value <code>restart\_needed</code> in <code>feature\_result</code>\, use <code>reboot\_required</code> instead
* win\_updates \- Removed deprecated return value <code>filtered\_reason</code>\, use <code>filtered\_reasons</code> instead

<a id="community-postgresql-5"></a>
#### community\.postgresql

* postgresql\_info \- the db alias has been removed in <code>community\.postgresql 4\.0\.0</code>\. Please use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/801](https\://github\.com/ansible\-collections/community\.postgresql/issues/801)\)\.
* postgresql\_lang \- the module has been removed in <code>community\.postgresql 4\.0\.0</code>\. Please use the <code>community\.postgresql\.postgresql\_ext</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/561](https\://github\.com/ansible\-collections/community\.postgresql/issues/561)\)\.
* postgresql\_privs \- the <code>password</code> argument has been removed in <code>community\.postgresql 4\.0\.0</code>\. Use the <code>login\_password</code> argument instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/408](https\://github\.com/ansible\-collections/community\.postgresql/issues/408)\)\.
* postgresql\_user \- the <code>priv</code> argument has been removed in <code>community\.postgresql 4\.0\.0</code>\. Please use the <code>community\.postgresql\.postgresql\_privs</code> module to grant/revoke privileges instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/493](https\://github\.com/ansible\-collections/community\.postgresql/issues/493)\)\.

<a id="community-windows-2"></a>
#### community\.windows

* win\_domain\_computer \- Removed deprecated module\, use <code>microsoft\.ad\.computer</code> instead
* win\_domain\_group \- Removed deprecated module\, use <code>microsoft\.ad\.group</code> instead
* win\_domain\_group\_membership \- Removed deprecated module\, use <code>microsoft\.ad\.membership</code> instead
* win\_domain\_object\_info \- Removed deprecated module\, use <code>microsoft\.ad\.object\_info</code> instead
* win\_domain\_ou \- Removed deprecated module\, use <code>microsoft\.ad\.ou</code> instead
* win\_domain\_user \- Removed deprecated module\, use <code>microsoft\.ad\.user</code> instead
* win\_lineinfile \- Removed deprecated return value <code>backup</code>\, use <code>backup\_file</code> instead
* win\_xml \- Removed deprecated\, and undocumented\, return value <code>backup</code>\, use <code>backup\_file</code> instead

<a id="vmware-vmware-8"></a>
#### vmware\.vmware

* vm\_list\_group\_by\_clusters \- Tombstone module in favor of vmware\.vmware\.vm\_list\_group\_by\_clusters\_info

<a id="bugfixes-7"></a>
### Bugfixes

<a id="ansible-core-23"></a>
#### Ansible\-core

* Ansible will now ensure predictable permissions on remote artifacts\, until now it only ensured executable and relied on system masks for the rest\.
* dnf5 \- avoid generating excessive transaction entries in the dnf5 history \([https\://github\.com/ansible/ansible/issues/85046](https\://github\.com/ansible/ansible/issues/85046)\)

<a id="ansible-windows-4"></a>
#### ansible\.windows

* win\_find \- allow users case sensitive match the filename \([https\://github\.com/ansible\-collections/ansible\.windows/issues/473](https\://github\.com/ansible\-collections/ansible\.windows/issues/473)\)\.
* win\_powershell \- Handle failure on output conversion when the output object uses a custom adapter set that fails to enumerate the method members\. This is seen when using the output from <code>Get\-WmiObject</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/767](https\://github\.com/ansible\-collections/ansible\.windows/issues/767)
* win\_regedit \- Handle decimal values with no decimal values which may be the result of a Jinja2 template
* win\_template \- Added support for Ansible 2\.19 and the introduction of the data tagging feature\.

<a id="community-crypto-8"></a>
#### community\.crypto

* luks\_device \- mark parameter <code>passphrase\_encoding</code> as <code>no\_log\=False</code> to avoid confusing warning \([https\://github\.com/ansible\-collections/community\.crypto/pull/867](https\://github\.com/ansible\-collections/community\.crypto/pull/867)\)\.
* luks\_device \- removing a specific keyslot with <code>remove\_keyslot</code> caused the module to hang while cryptsetup was waiting for a passphrase from stdin\, while the module did not supply one\. Since a keyslot is not necessary\, do not provide one \([https\://github\.com/ansible\-collections/community\.crypto/issues/864](https\://github\.com/ansible\-collections/community\.crypto/issues/864)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/868](https\://github\.com/ansible\-collections/community\.crypto/pull/868)\)\.

<a id="community-grafana-1"></a>
#### community\.grafana

* Remove field <em class="title-reference">apiVersion</em> from return of current <em class="title-reference">grafana\_datasource</em> for working diff
* grafana\_dashboard \- add uid to payload
* test\: replace more deprecated <em class="title-reference">TestCase\.assertEquals</em> to support Python 3\.12

<a id="community-windows-3"></a>
#### community\.windows

* win\_format \- fix crash when using path parameter without force option \([https\://github\.com/ansible\-collections/community\.windows/pull/615](https\://github\.com/ansible\-collections/community\.windows/pull/615)\)\.
* win\_toast \- fix title and message in the notification\.

<a id="dellemc-openmanage-5"></a>
#### dellemc\.openmanage

* idrac\_system\_info \- \(Issue 812\) \- idrac\_system\_info fails on iDRAC10\.

<a id="microsoft-ad-2"></a>
#### microsoft\.ad

* ldap inventory \- Fix up support for Ansible 2\.19\.

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Resolved issue with removing bucket quota
* purefb\_info \- Fixed issue after SMD Directory Services no longer avaible from REST 2\.16
* purefb\_policy \- Fixed creation of snapshot policies with assigned filesystems and/or replica links
* purefb\_s3acc \- Fixed issue with public access config settings not being correctly for an account

<a id="vmware-vmware-9"></a>
#### vmware\.vmware

* cluster\_ha \- Fix exception when cluster ha module checks for differences with VM monitoring configs
* fix method to lookup datastore clusters by name or moid [https\://github\.com/ansible\-collections/vmware\.vmware/issues/152](https\://github\.com/ansible\-collections/vmware\.vmware/issues/152)
* vm\_snapshot \- Make sure snapshot output is always included if state is present

<a id="known-issues-3"></a>
### Known Issues

<a id="dellemc-openmanage-6"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-modules-6"></a>
### New Modules

<a id="community-hrobot-5"></a>
#### community\.hrobot

* community\.hrobot\.storagebox\_snapshot \- Create\, update\, or delete a snapshot of a storage box\.

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_bucket\_access \- Manage FlashBlade bucket access policies
* purestorage\.flashblade\.purefb\_fleet \- Manage Fusion Fleet
* purestorage\.flashblade\.purefb\_server \- Manage FlashBlade servers

<a id="unchanged-collections-7"></a>
### Unchanged Collections

* amazon\.aws \(still version 9\.4\.0\)
* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 5\.1\.2\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.3\.1\)
* check\_point\.mgmt \(still version 6\.4\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.11\.0\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ios \(still version 10\.0\.0\)
* cisco\.iosxr \(still version 11\.0\.0\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.meraki \(still version 2\.21\.0\)
* cisco\.mso \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.ciscosmb \(still version 1\.0\.10\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.2\.3\)
* community\.general \(still version 10\.6\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.1\)
* community\.libvirt \(still version 1\.3\.1\)
* community\.mongodb \(still version 1\.7\.9\)
* community\.mysql \(still version 3\.13\.0\)
* community\.okd \(still version 4\.0\.1\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.routeros \(still version 3\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.sops \(still version 2\.0\.5\)
* community\.vmware \(still version 5\.6\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.conjur \(still version 1\.3\.3\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.35\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* hetzner\.hcloud \(still version 4\.3\.0\)
* hitachivantara\.vspone\_block \(still version 3\.4\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.3\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.2\.0\)
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
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 5\.3\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a2"></a>
## v12\.0\.0a2

- <a href="#release-summary-8">Release Summary</a>
- <a href="#ansible-core-24">Ansible\-core</a>
- <a href="#changed-collections-8">Changed Collections</a>
- <a href="#major-changes-5">Major Changes</a>
    - <a href="#grafana-grafana-2">grafana\.grafana</a>
- <a href="#minor-changes-8">Minor Changes</a>
    - <a href="#ansible-core-25">Ansible\-core</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-meraki-4">cisco\.meraki</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#community-general-11">community\.general</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#community-vmware-4">community\.vmware</a>
    - <a href="#hitachivantara-vspone-block-6">hitachivantara\.vspone\_block</a>
- <a href="#deprecated-features-6">Deprecated Features</a>
    - <a href="#community-general-12">community\.general</a>
    - <a href="#community-vmware-5">community\.vmware</a>
- <a href="#bugfixes-8">Bugfixes</a>
    - <a href="#ansible-core-26">Ansible\-core</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-meraki-5">cisco\.meraki</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#community-dns-3">community\.dns</a>
    - <a href="#community-general-13">community\.general</a>
    - <a href="#community-vmware-6">community\.vmware</a>
- <a href="#known-issues-4">Known Issues</a>
    - <a href="#community-general-14">community\.general</a>
- <a href="#new-plugins-2">New Plugins</a>
    - <a href="#connection-1">Connection</a>
- <a href="#new-modules-7">New Modules</a>
    - <a href="#hitachivantara-vspone-block-7">hitachivantara\.vspone\_block</a>
- <a href="#unchanged-collections-8">Unchanged Collections</a>

<a id="release-summary-8"></a>
### Release Summary

Release Date\: 2025\-04\-24

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-24"></a>
### Ansible\-core

Ansible 12\.0\.0a2 contains ansible\-core version 2\.19\.0b2\.
This is a newer version than version 2\.19\.0b1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-8"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 12.0.0a1 | Ansible 12.0.0a2 | Notes |
| ---------------------------------------- | ---------------- | ---------------- | ----- |
| cisco.aci                                | 2.10.1           | 2.11.0           |       |
| cisco.meraki                             | 2.20.8           | 2.21.0           |       |
| cisco.mso                                | 2.9.0            | 2.10.0           |       |
| community.dns                            | 3.2.2            | 3.2.3            |       |
| community.general                        | 10.5.0           | 10.6.0           |       |
| community.library_inventory_filtering_v1 | 1.1.0            | 1.1.1            |       |
| community.routeros                       | 3.5.0            | 3.6.0            |       |
| community.sops                           | 2.0.4            | 2.0.5            |       |
| community.vmware                         | 5.5.0            | 5.6.0            |       |
| grafana.grafana                          | 5.7.0            | 6.0.0            |       |
| hitachivantara.vspone_block              | 3.3.0            | 3.4.0            |       |

<a id="major-changes-5"></a>
### Major Changes

<a id="grafana-grafana-2"></a>
#### grafana\.grafana

* Add tempo role by \@CSTDev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/323](https\://github\.com/grafana/grafana\-ansible\-collection/pull/323)
* Do not log grafana\.ini contents when setting facts by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/325](https\://github\.com/grafana/grafana\-ansible\-collection/pull/325)
* Fix loki\_operational\_config section not getting rendered in config\.yml by \@olegkaspersky in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/330](https\://github\.com/grafana/grafana\-ansible\-collection/pull/330)
* Fix sectionless items edge case by \@santilococo in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/303](https\://github\.com/grafana/grafana\-ansible\-collection/pull/303)
* Fix tags Inherit default vars by \@MJurayev in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/341](https\://github\.com/grafana/grafana\-ansible\-collection/pull/341)
* Fix the markdown code fences for install command by \@benmatselby in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/306](https\://github\.com/grafana/grafana\-ansible\-collection/pull/306)
* Grafana fix facts in main\.yml by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/315](https\://github\.com/grafana/grafana\-ansible\-collection/pull/315)
* Make dashboard imports more flexible by \@torfbolt in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/308](https\://github\.com/grafana/grafana\-ansible\-collection/pull/308)
* force temporary directory even in check mode for  dashboards\.yml by \@cmehat in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/339](https\://github\.com/grafana/grafana\-ansible\-collection/pull/339)
* integrate sles legacy init\-script support by \@floerica in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/184](https\://github\.com/grafana/grafana\-ansible\-collection/pull/184)
* management of the config\.river with the conversion of the config\.yaml by \@lbrule in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/149](https\://github\.com/grafana/grafana\-ansible\-collection/pull/149)

<a id="minor-changes-8"></a>
### Minor Changes

<a id="ansible-core-25"></a>
#### Ansible\-core

* comment filter \- Improve the error message shown when an invalid <code>style</code> argument is provided\.

<a id="cisco-aci"></a>
#### cisco\.aci

* Add aci\_endpoint\_tag\_ip and aci\_endpoint\_tag\_mac modules to manage Endpoint IP and MAC Tags\.
* Add aci\_ip\_sla\_monitoring\_policy module\.
* Add management\_epg and management\_epg\_type attributes in aci\_dns\_profile module\.
* Add stratum attribute to aci\_ntp\_policy module\.
* Add support for Ansible 2\.18 and dropped support for Ansible 2\.15 as required by Ansible Galaxy\.

<a id="cisco-meraki-4"></a>
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

<a id="community-general-11"></a>
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

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_info\, api\_modify \- add <code>mdns\-repeat\-ifaces</code> to <code>ip dns</code> for RouterOS 7\.16 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/358](https\://github\.com/ansible\-collections/community\.routeros/pull/358)\)\.
* api\_info\, api\_modify \- field name change in <code>routing bgp connection</code> path implemented by RouterOS 7\.19 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/360](https\://github\.com/ansible\-collections/community\.routeros/pull/360)\)\.
* api\_info\, api\_modify \- rename <code>is\-responder</code> property in <code>interface wireguard peers</code> to <code>responder</code> for RouterOS 7\.17 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/364](https\://github\.com/ansible\-collections/community\.routeros/pull/364)\)\.

<a id="community-vmware-4"></a>
#### community\.vmware

* module\_utils\.vmware \- Move <code>vmware\_argument\_spec</code> to a dedicated file \([https\://github\.com/ansible\-collections/community\.vmware/pull/2370](https\://github\.com/ansible\-collections/community\.vmware/pull/2370)\)\.
* module\_utils\.vmware\_rest\_client \- Move <code>vmware\_client\_argument\_spec</code> to a dedicated file \([https\://github\.com/ansible\-collections/community\.vmware/pull/2370](https\://github\.com/ansible\-collections/community\.vmware/pull/2370)\)\.
* vmware\_dvs\_portgroup \- New option <code>network\_policy\.mac\_learning</code> to replace <code>mac\_learning</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2360](https\://github\.com/ansible\-collections/community\.vmware/pull/2360)\)\.
* vmware\_object\_role\_permission \- Document setting permissions on vCenter level \([https\://github\.com/ansible\-collections/community\.vmware/pull/2374](https\://github\.com/ansible\-collections/community\.vmware/pull/2374)\)\.

<a id="hitachivantara-vspone-block-6"></a>
#### hitachivantara\.vspone\_block

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

<a id="deprecated-features-6"></a>
### Deprecated Features

<a id="community-general-12"></a>
#### community\.general

* manifold lookup plugin \- plugin is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10028](https\://github\.com/ansible\-collections/community\.general/pull/10028)\)\.
* stackpath\_compute inventory plugin \- plugin is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10026](https\://github\.com/ansible\-collections/community\.general/pull/10026)\)\.

<a id="community-vmware-5"></a>
#### community\.vmware

* vmware\_dvs\_portgroup \- <code>mac\_learning</code> is deprecated in favour of <code>network\_policy\.mac\_learning</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2360](https\://github\.com/ansible\-collections/community\.vmware/pull/2360)\)\.

<a id="bugfixes-8"></a>
### Bugfixes

<a id="ansible-core-26"></a>
#### Ansible\-core

* Remove use of <em class="title-reference">required</em> parameter in <em class="title-reference">get\_bin\_path</em> which has been deprecated\.
* ansible\-doc \- fix indentation for first line of descriptions of suboptions and sub\-return values \([https\://github\.com/ansible/ansible/pull/84690](https\://github\.com/ansible/ansible/pull/84690)\)\.
* ansible\-doc \- fix line wrapping for first line of description of options and return values \([https\://github\.com/ansible/ansible/pull/84690](https\://github\.com/ansible/ansible/pull/84690)\)\.

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Fix aci\_rest module to only add annotation when the value is a dictionary
* Fix payload to define the correct vPC member side in aci\_l3out\_logical\_interface\_vpc\_member \(\#663\)
* Fix subclass issue in aci\_domain\_to\_vlan\_pool to fix deletion of binding \(\#695\)
* Modify interface\_configs requirement using required\_if dependency for aci\_bulk\_static\_binding\_to\_epg

<a id="cisco-meraki-5"></a>
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

<a id="community-dns-3"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-13"></a>
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

<a id="community-vmware-6"></a>
#### community\.vmware

* vmware\_dvs\_portgroup \- Fix idempotency issue with <code>mac\_learning</code> \([https\://github\.com/ansible\-collections/community\.vmware/issues/1873](https\://github\.com/ansible\-collections/community\.vmware/issues/1873)\)\.

<a id="known-issues-4"></a>
### Known Issues

<a id="community-general-14"></a>
#### community\.general

* reveal\_ansible\_type filter plugin and ansible\_type test plugin \- note that ansible\-core\'s Data Tagging feature implements new aliases\, such as <code>\_AnsibleTaggedStr</code> for <code>str</code>\, <code>\_AnsibleTaggedInt</code> for <code>int</code>\, and <code>\_AnsibleTaggedFloat</code> for <code>float</code> \([https\://github\.com/ansible\-collections/community\.general/pull/9833](https\://github\.com/ansible\-collections/community\.general/pull/9833)\)\.

<a id="new-plugins-2"></a>
### New Plugins

<a id="connection-1"></a>
#### Connection

* community\.general\.wsl \- Run tasks in WSL distribution using wsl\.exe CLI via SSH\.

<a id="new-modules-7"></a>
### New Modules

<a id="hitachivantara-vspone-block-7"></a>
#### hitachivantara\.vspone\_block

<a id="vsp-1"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_ddp\_pool \- Manages DDP Pools on Hitachi VSP storage systems\.
* hitachivantara\.vspone\_block\.hv\_ddp\_pool\_facts \- Get facts of DDP Pools on Hitachi VSP storage systems\.

<a id="unchanged-collections-8"></a>
### Unchanged Collections

* amazon\.aws \(still version 9\.4\.0\)
* ansible\.netcommon \(still version 8\.0\.0\)
* ansible\.posix \(still version 2\.0\.0\)
* ansible\.utils \(still version 5\.1\.2\)
* ansible\.windows \(still version 2\.8\.0\)
* arista\.eos \(still version 11\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.3\.1\)
* check\_point\.mgmt \(still version 6\.4\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.dnac \(still version 6\.31\.3\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.ios \(still version 10\.0\.0\)
* cisco\.iosxr \(still version 11\.0\.0\)
* cisco\.ise \(still version 2\.10\.0\)
* cisco\.nxos \(still version 10\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloud\.common \(still version 4\.0\.0\)
* cloudscale\_ch\.cloud \(still version 2\.4\.1\)
* community\.aws \(still version 9\.2\.0\)
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
* community\.okd \(still version 4\.0\.1\)
* community\.postgresql \(still version 3\.14\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.4\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* community\.windows \(still version 2\.4\.0\)
* community\.zabbix \(still version 3\.3\.0\)
* containers\.podman \(still version 1\.16\.3\)
* cyberark\.conjur \(still version 1\.3\.3\)
* cyberark\.pas \(still version 1\.0\.30\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.openmanage \(still version 9\.11\.0\)
* dellemc\.powerflex \(still version 2\.6\.0\)
* dellemc\.unity \(still version 2\.0\.0\)
* f5networks\.f5\_modules \(still version 1\.35\.0\)
* fortinet\.fortimanager \(still version 2\.9\.1\)
* fortinet\.fortios \(still version 2\.4\.0\)
* hetzner\.hcloud \(still version 4\.3\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ibm\.storage\_virtualize \(still version 2\.7\.3\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 10\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 5\.2\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* lowlydba\.sqlserver \(still version 2\.6\.0\)
* microsoft\.ad \(still version 1\.8\.1\)
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
* purestorage\.flashblade \(still version 1\.19\.2\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.2\.2\)
* theforeman\.foreman \(still version 5\.3\.0\)
* vmware\.vmware \(still version 1\.11\.0\)
* vmware\.vmware\_rest \(still version 4\.7\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v12-0-0a1"></a>
## v12\.0\.0a1

- <a href="#release-summary-9">Release Summary</a>
- <a href="#removed-collections-1">Removed Collections</a>
- <a href="#added-collections-2">Added Collections</a>
- <a href="#ansible-core-27">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-6">Major Changes</a>
    - <a href="#ansible-core-28">Ansible\-core</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#arista-eos-1">arista\.eos</a>
    - <a href="#cisco-ios-3">cisco\.ios</a>
    - <a href="#cisco-iosxr-2">cisco\.iosxr</a>
    - <a href="#cisco-nxos-4">cisco\.nxos</a>
    - <a href="#community-vmware-7">community\.vmware</a>
    - <a href="#community-zabbix-3">community\.zabbix</a>
    - <a href="#dellemc-openmanage-7">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#grafana-grafana-3">grafana\.grafana</a>
    - <a href="#junipernetworks-junos">junipernetworks\.junos</a>
- <a href="#minor-changes-9">Minor Changes</a>
    - <a href="#ansible-core-29">Ansible\-core</a>
    - <a href="#amazon-aws-6">amazon\.aws</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#ansible-posix">ansible\.posix</a>
    - <a href="#ansible-windows-5">ansible\.windows</a>
    - <a href="#arista-eos-2">arista\.eos</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#cisco-dnac-3">cisco\.dnac</a>
    - <a href="#cisco-ios-4">cisco\.ios</a>
    - <a href="#cisco-iosxr-3">cisco\.iosxr</a>
    - <a href="#cisco-ise">cisco\.ise</a>
    - <a href="#cisco-meraki-6">cisco\.meraki</a>
    - <a href="#cisco-nxos-5">cisco\.nxos</a>
    - <a href="#community-aws-4">community\.aws</a>
    - <a href="#community-ciscosmb-1">community\.ciscosmb</a>
    - <a href="#community-crypto-9">community\.crypto</a>
    - <a href="#community-dns-4">community\.dns</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-15">community\.general</a>
    - <a href="#community-hrobot-6">community\.hrobot</a>
    - <a href="#community-library-inventory-filtering-v1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-okd-2">community\.okd</a>
    - <a href="#community-postgresql-6">community\.postgresql</a>
    - <a href="#community-rabbitmq-2">community\.rabbitmq</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#community-vmware-8">community\.vmware</a>
    - <a href="#community-windows-4">community\.windows</a>
    - <a href="#community-zabbix-4">community\.zabbix</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-8">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex-2">dellemc\.powerflex</a>
    - <a href="#f5networks-f5-modules-2">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-3">fortinet\.fortimanager</a>
    - <a href="#hetzner-hcloud-4">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-1">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-3">microsoft\.ad</a>
    - <a href="#netapp-ontap-4">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-3">netapp\.storagegrid</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
    - <a href="#vmware-vmware-10">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-4">vmware\.vmware\_rest</a>
- <a href="#breaking-changes--porting-guide-4">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-30">Ansible\-core</a>
    - <a href="#ansible-posix-1">ansible\.posix</a>
    - <a href="#community-postgresql-7">community\.postgresql</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#theforeman-foreman-3">theforeman\.foreman</a>
- <a href="#deprecated-features-7">Deprecated Features</a>
    - <a href="#ansible-core-31">Ansible\-core</a>
    - <a href="#amazon-aws-7">amazon\.aws</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#cisco-ios-5">cisco\.ios</a>
    - <a href="#community-crypto-10">community\.crypto</a>
    - <a href="#community-hrobot-7">community\.hrobot</a>
    - <a href="#community-postgresql-8">community\.postgresql</a>
    - <a href="#community-vmware-9">community\.vmware</a>
    - <a href="#vmware-vmware-rest-5">vmware\.vmware\_rest</a>
- <a href="#removed-features-previously-deprecated-3">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-32">Ansible\-core</a>
    - <a href="#ansible-posix-2">ansible\.posix</a>
    - <a href="#cisco-nxos-6">cisco\.nxos</a>
    - <a href="#junipernetworks-junos-1">junipernetworks\.junos</a>
- <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#ansible-core-33">Ansible\-core</a>
    - <a href="#cloudscale-ch-cloud-3">cloudscale\_ch\.cloud</a>
- <a href="#bugfixes-9">Bugfixes</a>
    - <a href="#ansible-core-34">Ansible\-core</a>
    - <a href="#amazon-aws-8">amazon\.aws</a>
    - <a href="#ansible-netcommon-4">ansible\.netcommon</a>
    - <a href="#ansible-posix-3">ansible\.posix</a>
    - <a href="#ansible-windows-6">ansible\.windows</a>
    - <a href="#arista-eos-3">arista\.eos</a>
    - <a href="#cisco-ios-6">cisco\.ios</a>
    - <a href="#cisco-iosxr-4">cisco\.iosxr</a>
    - <a href="#cisco-ise-1">cisco\.ise</a>
    - <a href="#cisco-meraki-7">cisco\.meraki</a>
    - <a href="#cisco-nxos-7">cisco\.nxos</a>
    - <a href="#community-aws-5">community\.aws</a>
    - <a href="#community-crypto-11">community\.crypto</a>
    - <a href="#community-dns-5">community\.dns</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-general-16">community\.general</a>
    - <a href="#community-library-inventory-filtering-v1-1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-libvirt-2">community\.libvirt</a>
    - <a href="#community-mysql-3">community\.mysql</a>
    - <a href="#community-postgresql-9">community\.postgresql</a>
    - <a href="#community-rabbitmq-3">community\.rabbitmq</a>
    - <a href="#community-routeros-4">community\.routeros</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-vmware-10">community\.vmware</a>
    - <a href="#community-zabbix-5">community\.zabbix</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-9">dellemc\.openmanage</a>
    - <a href="#f5networks-f5-modules-3">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager-4">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#hetzner-hcloud-5">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-3">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#kubernetes-core-4">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-2">lowlydba\.sqlserver</a>
    - <a href="#netapp-ontap-5">netapp\.ontap</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-3">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
    - <a href="#telekom-mms-icinga-director-3">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-4">theforeman\.foreman</a>
    - <a href="#vmware-vmware-11">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-6">vmware\.vmware\_rest</a>
- <a href="#known-issues-5">Known Issues</a>
    - <a href="#dellemc-openmanage-10">dellemc\.openmanage</a>
    - <a href="#purestorage-flasharray-4">purestorage\.flasharray</a>
- <a href="#new-plugins-3">New Plugins</a>
    - <a href="#filter-2">Filter</a>
    - <a href="#lookup-1">Lookup</a>
- <a href="#new-modules-8">New Modules</a>
    - <a href="#amazon-aws-9">amazon\.aws</a>
    - <a href="#ansible-windows-7">ansible\.windows</a>
    - <a href="#check-point-mgmt-2">check\_point\.mgmt</a>
    - <a href="#cisco-ios-7">cisco\.ios</a>
    - <a href="#cisco-iosxr-5">cisco\.iosxr</a>
    - <a href="#cisco-nxos-8">cisco\.nxos</a>
    - <a href="#community-crypto-12">community\.crypto</a>
    - <a href="#community-docker-4">community\.docker</a>
    - <a href="#community-general-17">community\.general</a>
    - <a href="#community-hrobot-8">community\.hrobot</a>
    - <a href="#community-postgresql-10">community\.postgresql</a>
    - <a href="#community-vmware-11">community\.vmware</a>
    - <a href="#community-zabbix-6">community\.zabbix</a>
    - <a href="#dellemc-enterprise-sonic-3">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-powerflex-3">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager-5">fortinet\.fortimanager</a>
    - <a href="#ibm-storage-virtualize-4">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#kubernetes-core-5">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-3">lowlydba\.sqlserver</a>
    - <a href="#netapp-ontap-6">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-4">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-5">purestorage\.flasharray</a>
- <a href="#unchanged-collections-9">Unchanged Collections</a>

<a id="release-summary-9"></a>
### Release Summary

Release Date\: 2025\-04\-16

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections-1"></a>
### Removed Collections

* cisco\.asa \(previously included version\: 6\.0\.0\)
* community\.network \(previously included version\: 5\.1\.0\)
* google\.cloud \(previously included version\: 1\.4\.1\)
* ibm\.spectrum\_virtualize \(previously included version\: 2\.0\.0\)
* sensu\.sensu\_go \(previously included version\: 1\.14\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections-2"></a>
### Added Collections

* hitachivantara\.vspone\_block \(version 3\.3\.0\)
* microsoft\.iis \(version 1\.0\.2\)

<a id="ansible-core-27"></a>
### Ansible\-core

Ansible 12\.0\.0a1 contains ansible\-core version 2\.19\.0b1\.
This is a newer version than version 2\.18\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 11.0.0 | Ansible 12.0.0a1 | Notes                                                                                                                                                                                                        |
| ---------------------------------------- | -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                               | 9.0.0          | 9.4.0            |                                                                                                                                                                                                              |
| ansible.netcommon                        | 7.1.0          | 8.0.0            |                                                                                                                                                                                                              |
| ansible.posix                            | 1.6.2          | 2.0.0            |                                                                                                                                                                                                              |
| ansible.windows                          | 2.5.0          | 2.8.0            |                                                                                                                                                                                                              |
| arista.eos                               | 10.0.1         | 11.0.0           |                                                                                                                                                                                                              |
| azure.azcollection                       | 3.0.0          | 3.3.1            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt                         | 6.2.1          | 6.4.0            |                                                                                                                                                                                                              |
| cisco.dnac                               | 6.22.0         | 6.31.3           |                                                                                                                                                                                                              |
| cisco.ios                                | 9.0.3          | 10.0.0           |                                                                                                                                                                                                              |
| cisco.iosxr                              | 10.2.2         | 11.0.0           |                                                                                                                                                                                                              |
| cisco.ise                                | 2.9.5          | 2.10.0           |                                                                                                                                                                                                              |
| cisco.meraki                             | 2.18.3         | 2.20.8           |                                                                                                                                                                                                              |
| cisco.nxos                               | 9.2.1          | 10.0.0           |                                                                                                                                                                                                              |
| cisco.ucs                                | 1.14.0         | 1.16.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cloudscale_ch.cloud                      | 2.4.0          | 2.4.1            |                                                                                                                                                                                                              |
| community.aws                            | 9.0.0          | 9.2.0            |                                                                                                                                                                                                              |
| community.ciscosmb                       | 1.0.9          | 1.0.10           |                                                                                                                                                                                                              |
| community.crypto                         | 2.22.3         | 2.26.0           |                                                                                                                                                                                                              |
| community.dns                            | 3.0.7          | 3.2.2            |                                                                                                                                                                                                              |
| community.docker                         | 4.0.1          | 4.5.2            |                                                                                                                                                                                                              |
| community.general                        | 10.0.1         | 10.5.0           |                                                                                                                                                                                                              |
| community.hrobot                         | 2.0.2          | 2.2.0            |                                                                                                                                                                                                              |
| community.library_inventory_filtering_v1 | 1.0.2          | 1.1.0            |                                                                                                                                                                                                              |
| community.libvirt                        | 1.3.0          | 1.3.1            |                                                                                                                                                                                                              |
| community.mongodb                        | 1.7.8          | 1.7.9            | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.mysql                          | 3.10.3         | 3.13.0           |                                                                                                                                                                                                              |
| community.okd                            | 4.0.0          | 4.0.1            |                                                                                                                                                                                                              |
| community.postgresql                     | 3.7.0          | 3.14.0           |                                                                                                                                                                                                              |
| community.rabbitmq                       | 1.3.0          | 1.4.0            |                                                                                                                                                                                                              |
| community.routeros                       | 3.0.0          | 3.5.0            |                                                                                                                                                                                                              |
| community.sops                           | 2.0.0          | 2.0.4            |                                                                                                                                                                                                              |
| community.vmware                         | 5.1.0          | 5.5.0            |                                                                                                                                                                                                              |
| community.windows                        | 2.3.0          | 2.4.0            |                                                                                                                                                                                                              |
| community.zabbix                         | 3.1.2          | 3.3.0            |                                                                                                                                                                                                              |
| containers.podman                        | 1.16.2         | 1.16.3           |                                                                                                                                                                                                              |
| cyberark.conjur                          | 1.3.1          | 1.3.3            | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| cyberark.pas                             | 1.0.27         | 1.0.30           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| dellemc.enterprise_sonic                 | 2.5.1          | 3.0.0            |                                                                                                                                                                                                              |
| dellemc.openmanage                       | 9.8.0          | 9.11.0           |                                                                                                                                                                                                              |
| dellemc.powerflex                        | 2.5.0          | 2.6.0            |                                                                                                                                                                                                              |
| f5networks.f5_modules                    | 1.32.1         | 1.35.0           |                                                                                                                                                                                                              |
| fortinet.fortimanager                    | 2.7.0          | 2.9.1            |                                                                                                                                                                                                              |
| fortinet.fortios                         | 2.3.8          | 2.4.0            |                                                                                                                                                                                                              |
| grafana.grafana                          | 5.6.0          | 5.7.0            |                                                                                                                                                                                                              |
| hetzner.hcloud                           | 4.2.1          | 4.3.0            |                                                                                                                                                                                                              |
| hitachivantara.vspone_block              |                | 3.3.0            | The collection was added to Ansible                                                                                                                                                                          |
| ibm.storage_virtualize                   | 2.5.0          | 2.7.3            |                                                                                                                                                                                                              |
| infoblox.nios_modules                    | 1.7.0          | 1.8.0            |                                                                                                                                                                                                              |
| junipernetworks.junos                    | 9.1.0          | 10.0.0           |                                                                                                                                                                                                              |
| kubernetes.core                          | 5.0.0          | 5.2.0            |                                                                                                                                                                                                              |
| lowlydba.sqlserver                       | 2.3.4          | 2.6.0            |                                                                                                                                                                                                              |
| microsoft.ad                             | 1.7.1          | 1.8.1            |                                                                                                                                                                                                              |
| microsoft.iis                            |                | 1.0.2            | The collection was added to Ansible                                                                                                                                                                          |
| netapp.ontap                             | 22.12.0        | 22.14.0          |                                                                                                                                                                                                              |
| netapp.storagegrid                       | 21.13.0        | 21.14.0          |                                                                                                                                                                                                              |
| netbox.netbox                            | 3.20.0         | 3.21.0           |                                                                                                                                                                                                              |
| openstack.cloud                          | 2.2.0          | 2.4.1            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| purestorage.flasharray                   | 1.31.1         | 1.34.1           |                                                                                                                                                                                                              |
| purestorage.flashblade                   | 1.19.1         | 1.19.2           |                                                                                                                                                                                                              |
| telekom_mms.icinga_director              | 2.2.0          | 2.2.2            |                                                                                                                                                                                                              |
| theforeman.foreman                       | 4.2.0          | 5.3.0            |                                                                                                                                                                                                              |
| vmware.vmware                            | 1.6.0          | 1.11.0           |                                                                                                                                                                                                              |
| vmware.vmware_rest                       | 4.2.0          | 4.7.0            |                                                                                                                                                                                                              |

<a id="major-changes-6"></a>
### Major Changes

<a id="ansible-core-28"></a>
#### Ansible\-core

* Jinja plugins \- Jinja builtin filter and test plugins are now accessible via their fully\-qualified names <code>ansible\.builtin\.\{name\}</code>\.
* Task Execution / Forks \- Forks no longer inherit stdio from the parent <code>ansible\-playbook</code> process\. <code>stdout</code>\, <code>stderr</code>\, and <code>stdin</code> within a worker are detached from the terminal\, and non\-functional\. All needs to access stdio from a fork for controller side plugins requires use of <code>Display</code>\.
* ansible\-test \- Packages beneath <code>module\_utils</code> can now contain <code>\_\_init\_\_\.py</code> files\.
* variables \- The type system underlying Ansible\'s variable storage has been significantly overhauled and formalized\. Attempts to store unsupported Python object types in variables now more consistently yields early warnings or errors\.
* variables \- To support new Ansible features\, many variable objects are now represented by subclasses of their respective native Python types\. In most cases\, they behave indistinguishably from their original types\, but some Python libraries do not handle builtin object subclasses properly\. Custom plugins that interact with such libraries may require changes to convert and pass the native types\.

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="arista-eos-1"></a>
#### arista\.eos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-ios-3"></a>
#### cisco\.ios

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-iosxr-2"></a>
#### cisco\.iosxr

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-nxos-4"></a>
#### cisco\.nxos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="community-vmware-7"></a>
#### community\.vmware

* vmware\_dvswitch\_pvlans \- The VLAN ID type has been updated to be handled as an integer \([https\://github\.com/ansible\-collections/community\.vmware/pull/2267](https\://github\.com/ansible\-collections/community\.vmware/pull/2267)\)\.

<a id="community-zabbix-3"></a>
#### community\.zabbix

* All Roles \- Updated to support version 7\.2

<a id="dellemc-openmanage-7"></a>
#### dellemc\.openmanage

* omevv\_baseline\_profile \- This module allows to manage baseline profile\.
* omevv\_baseline\_profile\_info \- This module allows to retrieve baseline profile information\.
* omevv\_compliance\_info \- This module allows to retrieve firmware compliance reports\.
* omevv\_firmware \- This module allows to update firmware of the single host and single cluster\.

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Support check\_mode on all the configuration modules\.
* Supported new versions 7\.6\.1 and 7\.6\.2\.
* Updated the examples with correct values that have minimum or maximum values\.

<a id="grafana-grafana-3"></a>
#### grafana\.grafana

* Ability to set custom directory path for \*\.alloy config files by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/294](https\://github\.com/grafana/grafana\-ansible\-collection/pull/294)
* Fix \'dict object\' has no attribute \'path\' when running with \-\-check by \@JMLX42 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/283](https\://github\.com/grafana/grafana\-ansible\-collection/pull/283)
* Update grafana template by \@santilococo in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/300](https\://github\.com/grafana/grafana\-ansible\-collection/pull/300)
* add loki bloom support by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/298](https\://github\.com/grafana/grafana\-ansible\-collection/pull/298)
* grafana\.ini yaml syntax by \@intermittentnrg in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/232](https\://github\.com/grafana/grafana\-ansible\-collection/pull/232)

<a id="junipernetworks-junos"></a>
#### junipernetworks\.junos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.16\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="minor-changes-9"></a>
### Minor Changes

<a id="ansible-core-29"></a>
#### Ansible\-core

* Added a \-vvvvv log message indicating when a host fails to produce output within the timeout period\.
* AnsibleModule\.uri \- Add option <code>multipart\_encoding</code> for <code>form\-multipart</code> files in body to change default base64 encoding for files
* INVENTORY\_IGNORE\_EXTS config\, removed <code>ini</code> from the default list\, inventory scripts using a corresponding \.ini configuration are rare now and inventory\.ini files are more common\. Those that need to ignore the ini files for inventory scripts can still add it to configuration\.
* Jinja plugins \- Plugins can declare support for undefined values\.
* Jinja2 version 3\.1\.0 or later is now required on the controller\.
* Move <code>follow\_redirects</code> parameter to module\_utils so external modules can reuse it\.
* PlayIterator \- do not return tasks from already executed roles so specific strategy plugins do not have to do the filtering of such tasks themselves
* SSH Escalation\-related \-vvv log messages now include the associated host information\.
* Windows \- Add support for Windows Server 2025 to Ansible and as an <code>ansible\-test</code> remote target \- [https\://github\.com/ansible/ansible/issues/84229](https\://github\.com/ansible/ansible/issues/84229)
* Windows \- refactor the async implementation to better handle errors during bootstrapping and avoid WMI when possible\.
* <code>ansible\-galaxy collection install</code> — the collection dependency resolver now prints out conflicts it hits during dependency resolution when it\'s taking too long and it ends up backtracking a lot\. It also displays suggestions on how to help it compute the result more quickly\.
* ansible\, ansible\-console\, ansible\-pull \- add \-\-flush\-cache option \([https\://github\.com/ansible/ansible/issues/83749](https\://github\.com/ansible/ansible/issues/83749)\)\.
* ansible\-galaxy \- Add support for Keycloak service accounts
* ansible\-galaxy \- support <code>resolvelib \>\= 0\.5\.3\, \< 2\.0\.0</code> \([https\://github\.com/ansible/ansible/issues/84217](https\://github\.com/ansible/ansible/issues/84217)\)\.
* ansible\-test \- Added a macOS 15\.3 remote VM\, replacing 14\.3\.
* ansible\-test \- Automatically retry HTTP GET/PUT/DELETE requests on exceptions\.
* ansible\-test \- Default to Python 3\.13 in the <code>base</code> and <code>default</code> containers\.
* ansible\-test \- Disable the <code>deprecated\-</code> prefixed <code>pylint</code> rules as their results vary by Python version\.
* ansible\-test \- Disable the <code>pep8</code> sanity test rules <code>E701</code> and <code>E704</code> to improve compatibility with <code>black</code>\.
* ansible\-test \- Improve container runtime probe error handling\. When unexpected probe output is encountered\, an error with more useful debugging information is provided\.
* ansible\-test \- Replace container Alpine 3\.20 with 3\.21\.
* ansible\-test \- Replace container Fedora 40 with 41\.
* ansible\-test \- Replace remote Alpine 3\.20 with 3\.21\.
* ansible\-test \- Replace remote Fedora 40 with 41\.
* ansible\-test \- Replace remote FreeBSD 13\.3 with 13\.5\.
* ansible\-test \- Replace remote FreeBSD 14\.1 with 14\.2\.
* ansible\-test \- Replace remote RHEL 9\.4 with 9\.5\.
* ansible\-test \- Show a more user\-friendly error message when a <code>runme\.sh</code> script is not executable\.
* ansible\-test \- The <code>yamllint</code> sanity test now enforces string values for the <code>\!vault</code> tag\.
* ansible\-test \- Update <code>nios\-test\-container</code> to version 7\.0\.0\.
* ansible\-test \- Update <code>pylint</code> sanity test to use version 3\.3\.1\.
* ansible\-test \- Update distro containers to remove unnecessary packages \(apache2\, subversion\, ruby\)\.
* ansible\-test \- Update sanity test requirements to latest available versions\.
* ansible\-test \- Update the HTTP test container\.
* ansible\-test \- Update the PyPI test container\.
* ansible\-test \- Update the <code>base</code> and <code>default</code> containers\.
* ansible\-test \- Update the utility container\.
* ansible\-test \- Use Python\'s <code>urllib</code> instead of <code>curl</code> for HTTP requests\.
* ansible\-test \- When detection of the current container network fails\, a warning is now issued and execution continues\. This simplifies usage in cases where the current container cannot be inspected\, such as when running in GitHub Codespaces\.
* ansible\-test acme test container \- bump [version to 2\.3\.0](https\://github\.com/ansible/acme\-test\-container/releases/tag/2\.3\.0) to include newer versions of Pebble\, dependencies\, and runtimes\. This adds support for ACME profiles\, <code>dns\-account\-01</code> support\, and some smaller improvements \([https\://github\.com/ansible/ansible/pull/84547](https\://github\.com/ansible/ansible/pull/84547)\)\.
* apt\_key module \- add notes to docs and errors to point at the CLI tool deprecation by Debian and alternatives
* apt\_repository module \- add notes to errors to point at the CLI tool deprecation by Debian and alternatives
* become plugins get new property \'pipelining\' to show support or lack there of for the feature\.
* callback plugins \- add has\_option\(\) to CallbackBase to match other functions overloaded from AnsiblePlugin
* callback plugins \- fix get\_options\(\) for CallbackBase
* copy \- fix sanity test failures \([https\://github\.com/ansible/ansible/pull/83643](https\://github\.com/ansible/ansible/pull/83643)\)\.
* copy \- parameter <code>local\_follow</code> was incorrectly documented as having default value <code>True</code> \([https\://github\.com/ansible/ansible/pull/83643](https\://github\.com/ansible/ansible/pull/83643)\)\.
* cron \- Provide additional error information while writing cron file \([https\://github\.com/ansible/ansible/issues/83223](https\://github\.com/ansible/ansible/issues/83223)\)\.
* csvfile \- let the config system do the typecasting \([https\://github\.com/ansible/ansible/pull/82263](https\://github\.com/ansible/ansible/pull/82263)\)\.
* display \- Deduplication of warning and error messages considers the full content of the message \(including source and traceback contexts\, if enabled\)\. This may result in fewer messages being omitted\.
* distribution \- Added openSUSE MicroOS to Suse OS family \(\#84685\)\.
* dnf5\, apt \- add <code>auto\_install\_module\_deps</code> option \([https\://github\.com/ansible/ansible/issues/84206](https\://github\.com/ansible/ansible/issues/84206)\)
* docs \- add collection name in message from which the module is being deprecated \([https\://github\.com/ansible/ansible/issues/84116](https\://github\.com/ansible/ansible/issues/84116)\)\.
* env lookup \- The error message generated for a missing environment variable when <code>default</code> is an undefined value \(e\.g\. <code>undef\(\'something\'\)</code>\) will contain the hint from that undefined value\, except when the undefined value is the default of <code>undef\(\)</code> with no arguments\. Previously\, any existing undefined hint would be ignored\.
* file \- enable file module to disable diff\_mode \([https\://github\.com/ansible/ansible/issues/80817](https\://github\.com/ansible/ansible/issues/80817)\)\.
* file \- make code more readable and simple\.
* filter \- add support for URL\-safe encoding and decoding in b64encode and b64decode \([https\://github\.com/ansible/ansible/issues/84147](https\://github\.com/ansible/ansible/issues/84147)\)\.
* find \- add a checksum\_algorithm parameter to specify which type of checksum the module will return
* from\_json filter \- The filter accepts a <code>profile</code> argument\, which defaults to <code>tagless</code>\.
* handlers \- Templated handler names with syntax errors\, or that resolve to <code>omit</code> are now skipped like handlers with undefined variables in their name\.
* improved error message for yaml parsing errors in plugin documentation
* local connection plugin \- A new <code>become\_strip\_preamble</code> config option \(default True\) was added\; disable to preserve diagnostic <code>become</code> output in task results\.
* local connection plugin \- A new <code>become\_success\_timeout</code> operation\-wide timeout config \(default 10s\) was added for <code>become</code>\.
* local connection plugin \- When a <code>become</code> plugin\'s <code>prompt</code> value is a non\-string after the <code>check\_password\_prompt</code> callback has completed\, no prompt stripping will occur on stderr\.
* lookup\_template \- add an option to trim blocks while templating \([https\://github\.com/ansible/ansible/issues/75962](https\://github\.com/ansible/ansible/issues/75962)\)\.
* module \- set ipv4 and ipv6 rules simultaneously in iptables module \([https\://github\.com/ansible/ansible/issues/84404](https\://github\.com/ansible/ansible/issues/84404)\)\.
* module\_utils \- Add <code>NoReturn</code> type annotations to functions which never return\.
* modules \- PowerShell modules can now receive <code>datetime\.date</code>\, <code>datetime\.time</code> and <code>datetime\.datetime</code> values as ISO 8601 strings\.
* modules \- PowerShell modules can now receive strings sourced from inline vault\-encrypted strings\.
* modules \- Unhandled exceptions during Python module execution are now returned as structured data from the target\. This allows the new traceback handling to be applied to exceptions raised on targets\.
* pipelining logic has mostly moved to connection plugins so they can decide/override settings\.
* plugin error handling \- When raising exceptions in an exception handler\, be sure to use <code>raise \.\.\. from</code> as appropriate\. This supersedes the use of the <code>AnsibleError</code> arg <code>orig\_exc</code> to represent the cause\. Specifying <code>orig\_exc</code> as the cause is still permitted\. Failure to use <code>raise \.\.\. from</code> when <code>orig\_exc</code> is set will result in a warning\. Additionally\, if the two cause exceptions do not match\, a warning will be issued\.
* removed hardcoding of su plugin as it now works with pipelining\.
* runtime\-metadata sanity test \- improve validation of <code>action\_groups</code> \([https\://github\.com/ansible/ansible/pull/83965](https\://github\.com/ansible/ansible/pull/83965)\)\.
* service\_facts module got freebsd support added\.
* ssh connection plugin \- Support <code>SSH\_ASKPASS</code> mechanism to provide passwords\, making it the default\, but still offering an explicit choice to use <code>sshpass</code> \([https\://github\.com/ansible/ansible/pull/83936](https\://github\.com/ansible/ansible/pull/83936)\)
* ssh connection plugin now overrides pipelining when a tty is requested\.
* ssh\-agent \- <code>ansible</code>\, <code>ansible\-playbook</code> and <code>ansible\-console</code> are capable of spawning or reusing an ssh\-agent\, allowing plugins to interact with the ssh\-agent\. Additionally a pure python ssh\-agent client has been added\, enabling easy interaction with the agent\. The ssh connection plugin contains new functionality via <code>ansible\_ssh\_private\_key</code> and <code>ansible\_ssh\_private\_key\_passphrase</code>\, for loading an SSH private key into the agent from a variable\.
* templating \- Access to an undefined variable from inside a lookup\, filter\, or test \(which raises MarkerError\) no longer ends processing of the current template\. The triggering undefined value is returned as the result of the offending plugin invocation\, and the template continues to execute\.
* templating \- Embedding <code>range\(\)</code> values in containers such as lists will result in an error on use\. Previously the value would be converted to a string representing the range parameters\, such as <code>range\(0\, 3\)</code>\.
* templating \- Handling of omitted values is now a first\-class feature of the template engine\, and is usable in all Ansible Jinja template contexts\. Any template that resolves to <code>omit</code> is automatically removed from its parent container during templating\.
* templating \- Template evaluation is lazier than in previous versions\. Template expressions which resolve only portions of a data structure no longer result in the entire structure being templated\.
* templating \- Templating errors now provide more information about both the location and context of the error\, especially for deeply\-nested and/or indirected templating scenarios\.
* templating \- Unified <code>omit</code> behavior now requires that plugins calling <code>Templar\.template\(\)</code> handle cases where the entire template result is omitted\, by catching the <code>AnsibleValueOmittedError</code> that is raised\. Previously\, this condition caused a randomly\-generated string marker to appear in the template result\.
* templating \- Variables of type <code>set</code> and <code>tuple</code> are now converted to <code>list</code> when exiting the final pass of templating\.
* to\_json / to\_nice\_json filters \- The filters accept a <code>profile</code> argument\, which defaults to <code>tagless</code>\.
* troubleshooting \- Tracebacks can be collected and displayed for most errors\, warnings\, and deprecation warnings \(including those generated by modules\)\. Tracebacks are no longer enabled with <code>\-vvv</code>\; the behavior is directly configurable via the <code>DISPLAY\_TRACEBACK</code> config option\. Module tracebacks passed to <code>fail\_json</code> via the <code>exception</code> kwarg will not be included in the task result unless error tracebacks are configured\.
* undef jinja function \- The <code>undef</code> jinja function now raises an error if a non\-string hint is given\. Attempting to use an undefined hint also results in an error\, ensuring incorrect use of the function can be distinguished from the function\'s normal behavior\.
* validate\-modules sanity test \- make sure that <code>module</code> and <code>plugin</code> <code>seealso</code> entries use FQCNs \([https\://github\.com/ansible/ansible/pull/84325](https\://github\.com/ansible/ansible/pull/84325)\)\.
* vault \- improved vault filter documentation by adding missing example content for dump\_template\_data\.j2\, refining examples for clarity\, and ensuring variable consistency \([https\://github\.com/ansible/ansible/issues/83583](https\://github\.com/ansible/ansible/issues/83583)\)\.
* warnings \- All warnings \(including deprecation warnings\) issued during a task\'s execution are now accessible via the <code>warnings</code> and <code>deprecations</code> keys on the task result\.
* when the <code>dict</code> lookup is given a non\-dict argument\, show the value of the argument and its type in the error message\.
* windows \- add hard minimum limit for PowerShell to 5\.1\. Ansible dropped support for older versions of PowerShell in the 2\.16 release but this requirement is now enforced at runtime\.
* windows \- refactor windows exec runner to improve efficiency and add better error reporting on failures\.
* winrm \- Remove need for pexpect on macOS hosts when using <code>kinit</code> to retrieve the Kerberos TGT\. By default the code will now only use the builtin <code>subprocess</code> library which should handle issues with select and a high fd count and also simplify the code\.

<a id="amazon-aws-6"></a>
#### amazon\.aws

* autoscaling\_group \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* autoscaling\_group\_info \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_instance\_refresh \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_instance\_refresh\_info \- adds <code>group\_name</code> as an alias for the <code>name</code> parameter \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* ec2\_ami \- avoid redefining <code>delete\_snapshot</code> inside <code>DeregisterImage\.do</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* ec2\_instance \- Fix the issue when trying to run instances using launch template in an AWS environment where no default subnet is defined\([https\://github\.com/ansible\-collections/amazon\.aws/issues/2321](https\://github\.com/ansible\-collections/amazon\.aws/issues/2321)\)\.
* ec2\_metadata\_facts \- add <code>ansible\_ec2\_instance\_tags</code> to return values \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2398](https\://github\.com/ansible\-collections/amazon\.aws/pull/2398)\)\.
* ec2\_transit\_gateway \- avoid assignment to unused <code>retry\_decorator</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_transit\_gateway \- handle empty description while deleting transit gateway \([https\://github\.com/ansible\-collections/community\.aws/pull/2086](https\://github\.com/ansible\-collections/community\.aws/pull/2086)\)\.
* ec2\_vpc\_egress\_igw \- avoid assignment to unused <code>vpc\_id</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_vpc\_nacl \- avoid assignment to unused <code>result</code> variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* ec2\_vpc\_vpn \- minor linting fixups \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2444](https\://github\.com/ansible\-collections/amazon\.aws/pull/2444)\)\.
* iam\_password\_policy \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* iam\_role \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.
* inventory/aws\_ec2 \- Support jinja2 expression in <code>hostnames</code> variable\([https\://github\.com/ansible\-collections/amazon\.aws/issues/2402](https\://github\.com/ansible\-collections/amazon\.aws/issues/2402)\)\.
* inventory/aws\_ec2 \- Update templating mechanism to support ansible\-core 2\.19 changes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2552](https\://github\.com/ansible\-collections/amazon\.aws/pull/2552)\)\.
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
* s3\_object \- support passing metadata in <code>create</code> mode \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2529](https\://github\.com/ansible\-collections/amazon\.aws/pull/2529)\)\.
* s3\_object \- use the <code>copy</code> rather than <code>copy\_object</code> method when performing an S3 to S3 copy \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2117](https\://github\.com/ansible\-collections/amazon\.aws/issues/2117)\)\.
* s3\_object\_info \- add support to list objects under a specific prefix \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2477](https\://github\.com/ansible\-collections/amazon\.aws/issues/2477)\)\.
* s3\_object\_info \- avoid assignment to unused variable in except block \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2464](https\://github\.com/ansible\-collections/amazon\.aws/pull/2464)\)\.

<a id="ansible-netcommon-2"></a>
#### ansible\.netcommon

* Exposes new libssh options to configure publickey\_accepted\_algorithms and hostkeys\. This requires ansible\-pylibssh v1\.1\.0 or higher\.

<a id="ansible-posix"></a>
#### ansible\.posix

* authorized\_keys \- allow using absolute path to a file as a SSH key\(s\) source \([https\://github\.com/ansible\-collections/ansible\.posix/pull/568](https\://github\.com/ansible\-collections/ansible\.posix/pull/568)\)
* callback plugins \- Add recap information to timer\, profile\_roles and profile\_tasks callback outputs \([https\://github\.com/ansible\-collections/ansible\.posix/pull/387](https\://github\.com/ansible\-collections/ansible\.posix/pull/387)\)\.

<a id="ansible-windows-5"></a>
#### ansible\.windows

* Added support for Windows Server 2025
* setup \- Added <code>ansible\_os\_install\_date</code> as the OS installation date in the ISO 8601 format <code>yyyy\-MM\-ddTHH\:mm\:ssZ</code>\. This date is represented in the UTC timezone \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/663](https\://github\.com/ansible\-collections/ansible\.windows/issues/663)
* setup \- Remove dependency on shared function loaded by Ansible
* win\_get\_url \- Added <code>checksum</code> and <code>checksum\_algorithm</code> to verify the package before installation\. Also returns <code>checksum</code> if <code>checksum\_algorithm</code> is provided \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/596](https\://github\.com/ansible\-collections/ansible\.windows/issues/596)
* win\_get\_url \- if checksum is passed and destination file exists with different checksum file is always downloaded \([https\://github\.com/ansible\-collections/ansible\.windows/issues/717](https\://github\.com/ansible\-collections/ansible\.windows/issues/717)\)
* win\_get\_url \- if checksum is passed and destination file exists with identical checksum no download is done unless force\=yes \([https\://github\.com/ansible\-collections/ansible\.windows/issues/717](https\://github\.com/ansible\-collections/ansible\.windows/issues/717)\)
* win\_group \- Added <code>\-\-diff</code> output support\.
* win\_group \- Added <code>members</code> option to set the group membership\. This is designed to replace the functionality of the <code>win\_group\_membership</code> module\.
* win\_group \- Added <code>sid</code> return value representing the security identifier of the group when <code>state\=present</code>\.
* win\_group \- Migrate to newer Ansible\.Basic fragment for better input validation and testing support\.

<a id="arista-eos-2"></a>
#### arista\.eos

* Adds a new module <em class="title-reference">eos\_vrf\_global</em> in favor of <em class="title-reference">eos\_vrf</em> legacy module to manage VRF global configurations on Arista EOS devices\.

<a id="check-point-mgmt-1"></a>
#### check\_point\.mgmt

* added missing parameters such as \'filter\'\, \'domains\_to\_process\' and \'async\_response\' to the relevant resources modules\.
* check\_point\.mgmt\.cp\_mgmt\_lsm\_cluster \- support additional parameters \(dynamic\-objects\, tags and topology\)
* check\_point\.mgmt\.cp\_mgmt\_lsm\_gateway \- support additional parameters \(device\_id\, dynamic\-objects\, tags and topology\)

<a id="cisco-dnac-3"></a>
#### cisco\.dnac

* \.ansible\-lint is added to handle a formatting issue in Red Hat\.
* Added sample playbook for Device Configs Backup Module
* Added support for bulk operations on multiple access points in accesspoint\_workflow\_manager
* Adding Unit Test automation in github actions
* Aliases were implemented to handle v1 and v2 of the API\.
* Bug fixes in \[sda\_fabric\_sites\_zones\_workflow\_manager module
* Bug fixes in accesspoint\_workflow\_manager module
* Bug fixes in inventory\_workflow\_manager
* Bug fixes in lan\_automation\_workflow\_manager module
* Bug fixes in network\_settings\_workflow\_manager
* Bug fixes in pnp\_workflow\_manager module
* Bug fixes in sda\_fabric\_devices\_workflow\_manager
* Bug fixes in sda\_fabric\_transits\_workflow\_manager
* Bug fixes in sda\_fabric\_transits\_workflow\_manager module
* Bug fixes in sda\_fabric\_virtual\_networks\_workflow\_manager\.py
* Bug fixes in site\_workflow\_manager module
* Bug fixes in swim\_workflow\_manager module
* Bug fixes in template\_workflow\_manager module
* Bug fixes in user\_role\_workflow\_manager module
* Changes in circleci and yaml lint files
* Changes in circleci to run test cases in integration branch
* Changes in device\_credential\_workflow\_manager module
* Changes in dnac\.py file
* Changes in inventory\_workflow\_manager module
* Changes in ise\_radius\_integration\_workflow\_manager
* Changes in ise\_radius\_integration\_workflow\_manager module
* Changes in network\_compliance\_workflow\_manager
* Changes in network\_settings\_workflow\_manager
* Changes in network\_settings\_workflow\_manager module
* Changes in pnp\_workflow\_manager module
* Changes in provision\_workflow\_manager module
* Changes in sda\_extranet\_policy\_workflow\_manager
* Changes in sda\_fabric\_devices\_workflow\_manager module
* Changes in sda\_fabric\_site\_zones\_workflow\_manager module
* Changes in sda\_fabric\_virtual\_networks\_workflow\_manager module
* Changes in sda\_host\_port\_onboarding\_workflow\_manager module
* Changes in site\_workflow\_manager
* Changes in site\_workflow\_manager module
* Changes in swim\_workflow\_manager module
* Changes in swim\_workflow\_manager module to support list of images
* Changes in template\_workflow\_manager
* Enhancements in \[sda\_fabric\_virtual\_networks\_workflow\_manager module to support batch operation\.
* Enhancements in device\_configs\_backup\_workflow\_manager module to support unzipped backup file after download
* Enhancements in device\_credential\_workflow\_manager module
* Enhancements in provision\_workflow\_manager module
* Enhancements in sda\_fabric\_devices\_workflow\_manager\.py to support route distribution protocol
* Enhancements in sda\_fabric\_sites\_zones\_workflow\_manager\.py
* Enhancements in sda\_host\_port\_onboarding\_workflow\_manager module
* Fixed issues in module sda\_anycast\_gateways\_v1
* Fixed issues in module sda\_layer3\_virtual\_networks\_v1
* Modifications due to documentation errors
* Removing duplicates in the discovery\.py module\. snmpRwCommunity property\.
* Some parameters were modified in tag\_member\_v1\_info
* Supporting unmarking the devices in rma\_workflow\_manager module
* The file format was changed to conform to the requested standards\.
* Unit test modules added for pnp\_workflow\_manager module
* Update Readme
* aaa\_services\_count\_v1\_info \- new module
* aaa\_services\_id\_trend\_analytics\_v1 \- new module
* aaa\_services\_id\_v1\_info \- new module
* aaa\_services\_query\_count\_v1 \- new module
* aaa\_services\_query\_v1 \- new module
* aaa\_services\_summary\_analytics\_v1 \- new module
* aaa\_services\_top\_n\_analytics\_v1 \- new module
* aaa\_services\_trend\_analytics\_v1 \- new module
* aaa\_services\_v1\_info \- new module
* accesspoint\_workflow\_manager \- added attribute bulk\_update\_aps
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
* noqa all is used to ignore rules in some files\.
* playbooks were added
* projects\_count\_v1\_info \- new module
* projects\_project\_id\_v1 \- new module
* projects\_project\_id\_v1\_info \- new module
* projects\_v1 \- new module
* projects\_v1\_info \- new module
* qos\_policy\_setting\_v1 \- new module
* qos\_policy\_setting\_v1\_info \- new module
* sda\_fabric\_devices\_workflow\_manager \- attribute \'delete\_fabric\_device\' was removed
* sda\_fabric\_devices\_workflow\_manager \- attribute \'route\_distribution\_protocol\' was removed
* sda\_fabric\_devices\_workflow\_manager\.py \- added attribute route\_distribution\_protocol
* sda\_fabric\_site\_zones\_workflow\_manager \- attributes \'apply\_pending\_events\'\,  \'pre\_auth\_acl\'\, was added
* sda\_fabric\_sites\_zones\_workflow\_manager\.py \- added attribute site\_name\_hierarchy and removed attribute site\_name
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
* site\_workflow\_manager \- attribute \'force\_upload\_floor\_image\' was added
* sites\_site\_id\_wireless\_settings\_ssids\_id\_update\_v1 \- new module
* tags\_interfaces\_members\_associations\_bulk\_v1 \- new module
* tags\_network\_devices\_members\_associations\_bulk\_v1 \- new module
* template\_workflow\_manager \- attribute \'new\_template\_name\' was added
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

<a id="cisco-ios-4"></a>
#### cisco\.ios

* Add ios\_evpn\_ethernet resource module\.
* Added ios\_vrf\_interfaces resource module\,that helps with configuration of vrfs within interface
* Adds a new module <em class="title-reference">ios\_vrf\_address\_family</em> to manage VRFs address families on Cisco IOS devices\.
* ios\_interfaces \- Added service\-policy\, logging and snmp configuration options for interface\.
* ios\_l2\_interfaces \- Added a few switchport and spanning\-tree configuration options for interface\.
* ios\_l3\_interfaces \- Added a few ip configuration options for interface\.

<a id="cisco-iosxr-3"></a>
#### cisco\.iosxr

* Added iosxr\_vrf\_interfaces resource module\, that helps with configuration of vrfs within interface\.
* Adds support for setting local\-preference with plus/minus values in route policies

<a id="cisco-ise"></a>
#### cisco\.ise

* Fix linting issues\.

<a id="cisco-meraki-6"></a>
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

<a id="cisco-nxos-5"></a>
#### cisco\.nxos

* Add support for VRF address family via <em class="title-reference">vrf\_address\_family</em> resource module\.
* Added nxos\_vrf\_interfaces resource module\, that helps with configuration of vrfs within interface in favor of nxos\_vrf\_interface module\.
* nxos\_telemetry \- Added support for \'overridden\' state to provide complete configuration override capabilities\.
* nxos\_vpc \- Added support for peer\-switch feature configuration\.

<a id="community-aws-4"></a>
#### community\.aws

* aws\_ssm \-  Refactor <code>\_init\_clients</code> Method for Improved Clarity and Efficiency \([https\://github\.com/ansible\-collections/community\.aws/pull/2223](https\://github\.com/ansible\-collections/community\.aws/pull/2223)\)\.
* aws\_ssm \-  Refactor <code>\_prepare\_terminal\(\)</code> Method for Improved Clarity and Efficiency \([https\://github\.com/ansible\-collections/community\.aws/pull/](https\://github\.com/ansible\-collections/community\.aws/pull/)\)\.
* aws\_ssm \-  Refactor exec\_command Method for Improved Clarity and Efficiency \([https\://github\.com/ansible\-collections/community\.aws/pull/2224](https\://github\.com/ansible\-collections/community\.aws/pull/2224)\)\.
* aws\_ssm \- Add function to generate random strings for SSM CLI delimitation \([https\://github\.com/ansible\-collections/community\.aws/pull/2235](https\://github\.com/ansible\-collections/community\.aws/pull/2235)\)\.
* aws\_ssm \- Add the possibility to define <code>aws\_ssm plugin</code> variable via environment variable and by default use the version found on the \$PATH rather than require that you provide an absolute path \([https\://github\.com/ansible\-collections/community\.aws/issues/1990](https\://github\.com/ansible\-collections/community\.aws/issues/1990)\)\.
* aws\_ssm \- Refactor <code>\_exec\_transport\_commands</code>\, <code>\_generate\_commands</code>\, and <code>\_exec\_transport\_commands</code> methods for improved clarity \([https\://github\.com/ansible\-collections/community\.aws/pull/2248](https\://github\.com/ansible\-collections/community\.aws/pull/2248)\)\.
* aws\_ssm \- Refactor connection/aws\_ssm to add new S3ClientManager class and move relevant methods to the new class \([https\://github\.com/ansible\-collections/community\.aws/pull/2255](https\://github\.com/ansible\-collections/community\.aws/pull/2255)\)\.
* aws\_ssm \- Refactor display/verbosity\-related methods in aws\_ssm to simplify the code and avoid repetition \([https\://github\.com/ansible\-collections/community\.aws/pull/2264](https\://github\.com/ansible\-collections/community\.aws/pull/2264)\)\.
* dms\_endpoint \- Improve resilience of parameter comparison \([https\://github\.com/ansible\-collections/community\.aws/pull/2221](https\://github\.com/ansible\-collections/community\.aws/pull/2221)\)\.
* s3\_lifecycle \- Support for min and max object size when applying the filter rules \([https\://github\.com/ansible\-collections/community\.aws/pull/2205](https\://github\.com/ansible\-collections/community\.aws/pull/2205)\)\.
* various modules \- Linting fixups \([https\://github\.com/ansible\-collections/community\.aws/pull/2221](https\://github\.com/ansible\-collections/community\.aws/pull/2221)\)\.
* waf\_condition \- Add missing options validation to filters \([https\://github\.com/ansible\-collections/community\.aws/pull/2220](https\://github\.com/ansible\-collections/community\.aws/pull/2220)\)\.

<a id="community-ciscosmb-1"></a>
#### community\.ciscosmb

* added Catalyst 1300 to supported platforms
* parsing neighbour table allowes empty 4th column to allow Cisco Catalyst 1300 support

<a id="community-crypto-9"></a>
#### community\.crypto

* acme\_certificate \- add compatibility for ACME CAs that are not fully RFC8555 compliant and do not provide <code>challenges</code> in authz objects \([https\://github\.com/ansible\-collections/community\.crypto/issues/824](https\://github\.com/ansible\-collections/community\.crypto/issues/824)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/832](https\://github\.com/ansible\-collections/community\.crypto/pull/832)\)\.
* acme\_certificate \- add options <code>order\_creation\_error\_strategy</code> and <code>order\_creation\_max\_retries</code> which allow to configure the error handling behavior if creating a new ACME order fails\. This is particularly important when using the <code>include\_renewal\_cert\_id</code> option\, and the default value <code>auto</code> for <code>order\_creation\_error\_strategy</code> tries to gracefully handle related errors \([https\://github\.com/ansible\-collections/community\.crypto/pull/842](https\://github\.com/ansible\-collections/community\.crypto/pull/842)\)\.
* acme\_certificate \- allow to chose a profile for certificate generation\, in case the CA supports this using Internet\-Draft [draft\-aaron\-acme\-profiles](https\://datatracker\.ietf\.org/doc/draft\-aaron\-acme\-profiles/) \([https\://github\.com/ansible\-collections/community\.crypto/pull/835](https\://github\.com/ansible\-collections/community\.crypto/pull/835)\)\.
* acme\_certificate\_renewal\_info \- add <code>exists</code> and <code>parsable</code> return values and <code>treat\_parsing\_error\_as\_non\_existing</code> option \([https\://github\.com/ansible\-collections/community\.crypto/pull/838](https\://github\.com/ansible\-collections/community\.crypto/pull/838)\)\.
* luks\_device \- allow passphrases to contain newlines \([https\://github\.com/ansible\-collections/community\.crypto/pull/844](https\://github\.com/ansible\-collections/community\.crypto/pull/844)\)\.
* luks\_device \- allow to provide passphrases base64\-encoded \([https\://github\.com/ansible\-collections/community\.crypto/issues/827](https\://github\.com/ansible\-collections/community\.crypto/issues/827)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/829](https\://github\.com/ansible\-collections/community\.crypto/pull/829)\)\.
* openssl\_pkcs12 \- the module now supports <code>certificate\_content</code>/<code>other\_certificates\_content</code> for cases where the data already exists in memory and not yet in a file \([https\://github\.com/ansible\-collections/community\.crypto/issues/847](https\://github\.com/ansible\-collections/community\.crypto/issues/847)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/848](https\://github\.com/ansible\-collections/community\.crypto/pull/848)\)\.
* x509\_certificate\_convert \- add new option <code>verify\_cert\_parsable</code> which allows to check whether the certificate can actually be parsed \([https\://github\.com/ansible\-collections/community\.crypto/issues/809](https\://github\.com/ansible\-collections/community\.crypto/issues/809)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/830](https\://github\.com/ansible\-collections/community\.crypto/pull/830)\)\.

<a id="community-dns-4"></a>
#### community\.dns

* all controller code \- modernize Python code \([https\://github\.com/ansible\-collections/community\.dns/pull/231](https\://github\.com/ansible\-collections/community\.dns/pull/231)\)\.
* all filter\, inventory\, and lookup plugins\, and plugin utils \- add type hints to all Python 3 only code \([https\://github\.com/ansible\-collections/community\.dns/pull/239](https\://github\.com/ansible\-collections/community\.dns/pull/239)\)\.
* get\_public\_suffix\, get\_registrable\_domain\, remove\_public\_suffix\, and remove\_registrable\_domain filter plugin \- validate parameters\, and correctly handle byte strings when passed for input \([https\://github\.com/ansible\-collections/community\.dns/pull/239](https\://github\.com/ansible\-collections/community\.dns/pull/239)\)\.

<a id="community-docker-2"></a>
#### community\.docker

* docker\_compose\_v2 \- add <code>assume\_yes</code> parameter for <code>docker compose up</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1045](https\://github\.com/ansible\-collections/community\.docker/pull/1045)\)\.
* docker\_compose\_v2 \- add <code>ignore\_build\_events</code> option \(default value <code>true</code>\) which allows to \(not\) ignore build events for change detection \([https\://github\.com/ansible\-collections/community\.docker/issues/1005](https\://github\.com/ansible\-collections/community\.docker/issues/1005)\, [https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011](https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011)\)\.
* docker\_compose\_v2\* modules \- determine compose version with <code>docker compose version</code> and only then fall back to <code>docker info</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1021](https\://github\.com/ansible\-collections/community\.docker/pull/1021)\)\.
* docker\_image\_build \- <code>outputs\[\]\.name</code> can now be a list of strings \([https\://github\.com/ansible\-collections/community\.docker/pull/1006](https\://github\.com/ansible\-collections/community\.docker/pull/1006)\)\.
* docker\_image\_build \- the executed command is now returned in the <code>command</code> return value in case of success and some errors \([https\://github\.com/ansible\-collections/community\.docker/pull/1006](https\://github\.com/ansible\-collections/community\.docker/pull/1006)\)\.
* docker\_network \- add <code>enable\_ipv4</code> option \([https\://github\.com/ansible\-collections/community\.docker/issues/1047](https\://github\.com/ansible\-collections/community\.docker/issues/1047)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1049](https\://github\.com/ansible\-collections/community\.docker/pull/1049)\)\.
* docker\_network \- added <code>ingress</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_stack \- allow to add <code>\-\-detach\=false</code> option to <code>docker stack deploy</code> command \([https\://github\.com/ansible\-collections/community\.docker/pull/987](https\://github\.com/ansible\-collections/community\.docker/pull/987)\)\.

<a id="community-general-15"></a>
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

<a id="community-hrobot-6"></a>
#### community\.hrobot

* All modules and plugins now have a <code>rate\_limit\_retry\_timeout</code> option\, which allows to configure for how long to wait in case of rate limiting errors\. By default\, the modules wait indefinitely\. Setting the option to <code>0</code> does not retry \(this was the behavior in previous versions\)\, and a positive value sets a number of seconds to wait at most \([https\://github\.com/ansible\-collections/community\.hrobot/pull/140](https\://github\.com/ansible\-collections/community\.hrobot/pull/140)\)\.
* boot \- it is now possible to specify SSH public keys in <code>authorized\_keys</code>\. The fingerprint needed by the Robot API will be extracted automatically \([https\://github\.com/ansible\-collections/community\.hrobot/pull/134](https\://github\.com/ansible\-collections/community\.hrobot/pull/134)\)\.
* v\_switch \- the module is now part of the <code>community\.hrobot\.robot</code> action group\, despite already being documented as part of it \([https\://github\.com/ansible\-collections/community\.hrobot/pull/136](https\://github\.com/ansible\-collections/community\.hrobot/pull/136)\)\.

<a id="community-library-inventory-filtering-v1"></a>
#### community\.library\_inventory\_filtering\_v1

* Add typing information for the <code>inventory\_filter</code> plugin utils \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/22](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/22)\)\.

<a id="community-mysql-2"></a>
#### community\.mysql

* Integration tests for MariaDB 11\.4 have replaced those for 10\.5\. The previous version is now 10\.11\.
* mysql\_db \- added <code>zstd</code> \(de\)compression support for <code>import</code>/<code>dump</code> states \([https\://github\.com/ansible\-collections/community\.mysql/issues/696](https\://github\.com/ansible\-collections/community\.mysql/issues/696)\)\.
* mysql\_info \- adds the count of tables for each database to the returned values\. It is possible to exclude this new field using the <code>db\_table\_count</code> exclusion filter\. \([https\://github\.com/ansible\-collections/community\.mysql/pull/691](https\://github\.com/ansible\-collections/community\.mysql/pull/691)\)
* mysql\_query \- returns the <code>execution\_time\_ms</code> list containing execution time per query in milliseconds\.
* mysql\_user \- add <code>locked</code> option to lock/unlock users\, this is mainly used to have users that will act as definers on stored procedures\.

<a id="community-okd-2"></a>
#### community\.okd

* openshift\_auth \- fix issue where openshift\_auth module sometimes does not delete the auth token\. Based on stale PR \([https\://github\.com/openshift/community\.okd/pull/194](https\://github\.com/openshift/community\.okd/pull/194)\)\.

<a id="community-postgresql-6"></a>
#### community\.postgresql

* postgresql\_pg\_hba \- adds \'pg\_hba\_string\' which contains the string that is written to the file to the output of the module \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_pg\_hba \- adds a parameter \'sort\_rules\' that allows the user to disable sorting in the module\, the default is the previous behavior \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_pg\_hba \- changes ordering of entries that are identical except for the ip\-range\, but only if the ranges are of the same size\, this isn\'t breaking as ranges of equal size can\'t overlap \([https\://github\.com/ansible\-collections/community\.postgresql/pull/772](https\://github\.com/ansible\-collections/community\.postgresql/pull/772)\)
* postgresql\_pg\_hba \- orders auth\-options alphabetically\, this isn\'t breaking as the order of those options is not relevant to postgresql \([https\://github\.com/ansible\-collections/community\.postgresql/pull/772](https\://github\.com/ansible\-collections/community\.postgresql/pull/772)\)
* postgresql\_pg\_hba \- regarding \#795 will read all kinds of includes and add them to the end of the file in the same order as they were in the original file\, does not allow to add includes \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_pg\_hba \- show the number of the line with the issue if parsing a file fails \([https\://github\.com/ansible\-collections/community\.postgresql/pull/766](https\://github\.com/ansible\-collections/community\.postgresql/pull/766)\)
* postgresql\_publication \- add possibility of creating publication with column list \([https\://github\.com/ansible\-collections/community\.postgresql/pull/763](https\://github\.com/ansible\-collections/community\.postgresql/pull/763)\)\.
* postgresql\_publication \- added <code>rowfilters</code> parameter that adds support for row filtering on PG publications \([https\://github\.com/ansible\-collections/community\.postgresql/pull/813](https\://github\.com/ansible\-collections/community\.postgresql/pull/813)\)
* postgresql\_query \- returns the <em class="title-reference">execution\_time\_ms</em> list containing execution time per query in milliseconds \([https\://github\.com/ansible\-collections/community\.postgresql/issues/787](https\://github\.com/ansible\-collections/community\.postgresql/issues/787)\)\.
* postgresql\_user \- now there is a <code>quote\_configuration\_values</code> parameter that allows to turn off quoting for values which when set to <code>false</code> allows to set <code>search\_path</code> \([https\://github\.com/ansible\-collections/community\.postgresql/pull/806](https\://github\.com/ansible\-collections/community\.postgresql/pull/806)\)

<a id="community-rabbitmq-2"></a>
#### community\.rabbitmq

* rabbitmq\_policy \- adjust the <em class="title-reference">apply\_to</em> parameter to also accept the new options <em class="title-reference">classic\_queues</em>\, <em class="title-reference">quorum\_queues</em> and <em class="title-reference">streams</em> which are supported since rabbitmq 3\.12

<a id="community-routeros-3"></a>
#### community\.routeros

* api\_info\, api\_modify \- add missing attribute <code>require\-message\-auth</code> for the <code>radius</code> path which exists since RouterOS version 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/issues/338](https\://github\.com/ansible\-collections/community\.routeros/issues/338)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/339](https\://github\.com/ansible\-collections/community\.routeros/pull/339)\)\.
* api\_info\, api\_modify \- add missing fields <code>comment</code>\, <code>next\-pool</code> to <code>ip pool</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/327](https\://github\.com/ansible\-collections/community\.routeros/pull/327)\)\.
* api\_info\, api\_modify \- add support for the <code>ip dns forwarders</code> path implemented by RouterOS 7\.17 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/343](https\://github\.com/ansible\-collections/community\.routeros/pull/343)\)\.
* api\_info\, api\_modify \- add support for the <code>routing filter community\-list</code> path implemented by RouterOS 7 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/331](https\://github\.com/ansible\-collections/community\.routeros/pull/331)\)\.
* api\_info\, api\_modify \- add the <code>interface 6to4</code> path\. Used to manage IPv6 tunnels via tunnel\-brokers like HE\, where native IPv6 is not provided \([https\://github\.com/ansible\-collections/community\.routeros/pull/342](https\://github\.com/ansible\-collections/community\.routeros/pull/342)\)\.
* api\_info\, api\_modify \- add the <code>interface wireless access\-list</code> and <code>interface wireless connect\-list</code> paths \([https\://github\.com/ansible\-collections/community\.routeros/issues/284](https\://github\.com/ansible\-collections/community\.routeros/issues/284)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/340](https\://github\.com/ansible\-collections/community\.routeros/pull/340)\)\.
* api\_info\, api\_modify \- add the <code>use\-interface\-duid</code> option for <code>ipv6 dhcp\-client</code> path\. This option prevents issues with Fritzbox modems and routers\, when using virtual interfaces \(like VLANs\) may create duplicated records in hosts config\, this breaks original \"expose\-host\" function\. Also add the <code>script</code>\, <code>custom\-duid</code> and <code>validate\-server\-duid</code> as backport from 7\.15 version update \([https\://github\.com/ansible\-collections/community\.routeros/pull/341](https\://github\.com/ansible\-collections/community\.routeros/pull/341)\)\.
* api\_info\, api\_modify \- change default for <code>/ip/cloud/ddns\-enabled</code> for RouterOS 7\.17 and newer from <code>yes</code> to <code>auto</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/350](https\://github\.com/ansible\-collections/community\.routeros/pull/350)\)\.

<a id="community-vmware-8"></a>
#### community\.vmware

* vcenter\_standard\_key\_provider \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.
* vmware\.py \- Add logic for handling the case where the <em class="title-reference">datacenter</em> property is not provided\.
* vmware\_category \- Don\'t test for vSphere \< 7 anymore \([https\://github\.com/ansible\-collections/community\.vmware/pull/2326](https\://github\.com/ansible\-collections/community\.vmware/pull/2326)\)\.
* vmware\_guest \- Add new cutomization spec param <em class="title-reference">domainOU</em>\. \([https\://github\.com/ansible\-collections/community\.vmware/issues/2275](https\://github\.com/ansible\-collections/community\.vmware/issues/2275)\)
* vmware\_guest \- Drop unused HAS\_PYVMOMI \([https\://github\.com/ansible\-collections/community\.vmware/pull/2327](https\://github\.com/ansible\-collections/community\.vmware/pull/2327)\)\.
* vmware\_guest \- Print details about the error message when the returned task result contains \([https\://github\.com/ansible\-collections/community\.vmware/pull/2301](https\://github\.com/ansible\-collections/community\.vmware/pull/2301)\)\.
* vmware\_guest \- Speedup network search \([https\://github\.com/ansible\-collections/community\.vmware/pull/2278](https\://github\.com/ansible\-collections/community\.vmware/pull/2278)\)\.
* vmware\_guest\_info \- <em class="title-reference">datacenter</em> property is now optional as it only required in cases where the VM is not uniquely identified by <em class="title-reference">name</em>\.
* vmware\_guest\_network \- Speedup network search \([https\://github\.com/ansible\-collections/community\.vmware/pull/2277](https\://github\.com/ansible\-collections/community\.vmware/pull/2277)\)\.
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

<a id="community-windows-4"></a>
#### community\.windows

* Added support for Windows Server 2025
* This issue fixes installation of requirements as it requires a confirmation when installed as a depedency to PowershellGet\. Installing it by itself prevents this confirmation dialog and allows required components to be installed \([https\://github\.com/ansible\-collections/community\.windows/issues/147](https\://github\.com/ansible\-collections/community\.windows/issues/147)\)\.
* win\_file\_version \- Add file\_version\_raw result for cases where file\_version might be empty or in not in the right format\.
* win\_iis\_webapppool  \- this pull request fixes the portion where building an app pool with the word \"value\" in it fails unexpectedly\. [https\://github\.com/ansible\-collections/community\.windows/issues/410](https\://github\.com/ansible\-collections/community\.windows/issues/410)\.
* win\_psrepository\_copy \- Add Force option that deletes repositories that are not present in the source

<a id="community-zabbix-4"></a>
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

<a id="dellemc-enterprise-sonic"></a>
#### dellemc\.enterprise\_sonic

* sonic\_image\_management \- Add support for image GPG Key installation and verification feature in sonic\_image\_management module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/380](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/380)\)\.
* sonic\_interfaces \- Add new unreliable\-los option to interface resource module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/453](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/453)\)\.
* sonic\_ldap \- Add ldap security profile support for sonic\_ldap module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/414](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/414)\)\.
* sonic\_logging \- Add \"severity\" option to the logging module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/478](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/478)\)\.
* sonic\_logging \- Add TLS protocol in sonic\_logging module\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/423](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/423)\)\.
* sonic\_logging \- Add audit message\-type in sonic\_logging module\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/424](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/424)\)\.
* sonic\_logging \- Add new \'auditd\_system\' choice to the \'message\_type\' choices for the logging resource module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/459](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/459)\)\.
* sonic\_mgmt\_servers \- Add REST server cipher suite support for sonic\_mgmt\_servers module \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/464](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/464)\)\.
* sonic\_qos\_buffer \- Add \'buffer\_init\' attribute \([https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/444](https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/444)\)\.
* sonic\_route\_maps \- Add the set ip/ipv6 next\_hop \'native\' option \([https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/421](https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/421)\)\.
* sonic\_vxlan \- Add \'suppress\_vlan\_neigh\' vlan list option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/448](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/448)\)\.

<a id="dellemc-openmanage-8"></a>
#### dellemc\.openmanage

* idrac\_certificates \-  This module is enhanced to support SSL CSR generation for 4096 key size\.
* omevv\_firmware\_repository\_profile \- This module allows to resync the repository profiles from the OpenManage Update Manager Plug\-in\.

<a id="dellemc-powerflex-2"></a>
#### dellemc\.powerflex

* Added Ansible role to support installation and uninstallation of SDT\.
* Info module is enhanced to support the listing of SDTs and NVMe hosts\.

<a id="f5networks-f5-modules-2"></a>
#### f5networks\.f5\_modules

* bigip\_virtual\_server \- Fixed issue \- Disabling/Enabling Virtual Server does not require profiles\, type in Update

<a id="fortinet-fortimanager-3"></a>
#### fortinet\.fortimanager

* Supported FortiManager 6\.2\.13\, 6\.4\.15\, 7\.0\.13\, 7\.2\.8\, 7\.4\.5\, 7\.6\.1\. Added 1 new module\.
* Supported FortiManager 7\.2\.9\, 7\.4\.6\, 7\.6\.2\. Added 3 new modules\.
* Supported check diff for some modules except \"fmgr\_generic\"\. You can use \"ansible\-playbook \-i \<your\-host\-file\> \<your\-playbook\> \-\-check \-\-diff\" to check what changes your playbook will make to the FortiManager\.

<a id="hetzner-hcloud-4"></a>
#### hetzner\.hcloud

* server \- Add <em class="title-reference">created</em> state that creates a server but do not start it\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_replication\_policy \- Added support for disaster recovery
* ibm\_sv\_manage\_replication\_policy \- Added support for highly\-available snapshots
* ibm\_sv\_manage\_snapshot\- Add support for restoring highly\-available volumes and volumegroups from local snapshots
* ibm\_sv\_manage\_storage\_partition \- Added support for partition migration and disaster recovery
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for creating truststore for flashsystem grid
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for enabling various options \(syslog\, RESTAPI\, vasa\, ipsec\, snmp and email\) for existing truststore
* ibm\_svc\_host \- Added support for specifying host location in PBHA\, support for FDMI discovery\, suppressing offline alert\, updating IO groups\, and for specifying fcscsi and iscsi protocols during host creation
* ibm\_svc\_info \- Added support for flashsystem grid
* ibm\_svc\_initial\_setup \- Added support for flashcopy default grain size and SI \(Storage Insights\) to be able to control partition migration
* ibm\_svc\_initial\_setup \- Added support for vdisk protection settings\, iscsiauthmethod and improved REST API calls
* ibm\_svc\_manage\_flashcopy \- Added support for enabling cleanrate during flashcopy creation and update
* ibm\_svc\_manage\_portset \- Added support for linking portset of 2 clusters for PBHA
* ibm\_svc\_manage\_replication \- Added support for highly\-available snapshots
* ibm\_svc\_manage\_volume \- Added support for converting thinclone volume\(s\) to clone
* ibm\_svc\_manage\_volume \- Added support for unmapping hosts\, remote\-copy and flashcopy during volume deletion
* ibm\_svc\_manage\_volumegroup \- Added support for disaster recovery and converting thinclone volumegroup to clone
* ibm\_svc\_mdisk \- Added support for updating tier
* ibm\_svc\_mdiskgrp \- Improved probe function for storage pools

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* Bump version of ansible\-lint to minimum 24\.7\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/765](https\://github\.com/ansible\-collections/kubernetes\.core/pull/765)\)\.
* Parameter insecure\_registry added to helm\_template as equivalent of insecure\-skip\-tls\-verify \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/805](https\://github\.com/ansible\-collections/kubernetes\.core/pull/805)\)\.
* k8s \- Extend hidden\_fields to allow the expression of more complex field types to be hidden \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/872](https\://github\.com/ansible\-collections/kubernetes\.core/pull/872)\)
* k8s\_drain \- Improve error message for pod disruption budget when draining a node \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/797](https\://github\.com/ansible\-collections/kubernetes\.core/issues/797)\)\.
* k8s\_info \- Extend hidden\_fields to allow the expression of more complex field types to be hidden \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/872](https\://github\.com/ansible\-collections/kubernetes\.core/pull/872)\)
* waiter\.py \- add ClusterOperator support\. The module can now check OpenShift cluster health by verifying ClusterOperator status requiring \'Available\: True\'\, \'Degraded\: False\'\, and \'Progressing\: False\' for success\. \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/869](https\://github\.com/ansible\-collections/kubernetes\.core/issues/869)\)

<a id="lowlydba-sqlserver-1"></a>
#### lowlydba\.sqlserver

* Add new <em class="title-reference">login\_role</em> module to add/remove server roles for logins \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/293](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/293)\)\.
* Add new user\_role module to manage users\' membership to database roles \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/292](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/292)\)\.
* Added support for contained Availability Groups using dbatools 2\.1\.15 \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/249](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/249)\)\.

<a id="microsoft-ad-3"></a>
#### microsoft\.ad

* Added support for Windows Server 2025
* domain \- Added <code>replication\_source\_dc</code> to specify the domain controller to use as the replication source for the new domain \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/159](https\://github\.com/ansible\-collections/microsoft\.ad/issues/159)
* domain\_controller \- Added <code>replication\_source\_dc</code> to specify the domain controller to use as the replication source for the new domain controller \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/159](https\://github\.com/ansible\-collections/microsoft\.ad/issues/159)
* microsoft\.ad\.user \- Added <code>groups\.permissions\_failure\_action</code> to control the behaviour when failing to modify the user\'s groups \- \([https\://github\.com/ansible\-collections/microsoft\.ad/issues/140](https\://github\.com/ansible\-collections/microsoft\.ad/issues/140)\)\.

<a id="netapp-ontap-4"></a>
#### netapp\.ontap

* Multiple modules \- Standardize hostname\, username\, and password parameters to use netapp\_hostname\, netapp\_username\, and netapp\_password as values\.
* Multiple modules \- Update examples to use Fully Qualified Collection Name\.
* Update dead link in doc\_fragments\.
* all modules supporting only REST \- change in documentation for <em class="title-reference">use\_rest</em>\.
* all modules supporting only REST \- updated <em class="title-reference">extends\_documentation\_fragment</em> \& argument spec\.
* na\_ontap\_active\_directory \- return error message when attempting to modify <em class="title-reference">account\_name</em>\.
* na\_ontap\_bgp\_config \- REST only support for managing BGP configuration for a node\, requires ONTAP 9\.6 or later\.
* na\_ontap\_cifs\_privileges \- REST only support for managing privileges of the local or Active Directory user or group\, requires ONTAP 9\.10\.1 or later\.
* na\_ontap\_cifs\_server \- added new option <em class="title-reference">comment</em> for cifs server\, requires ONTAP 9\.6 or later\.
* na\_ontap\_dns \- updated documentation for <em class="title-reference">vserver</em>\.
* na\_ontap\_flexcache \- new option to enable <em class="title-reference">writeback</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_flexcache \- new options <em class="title-reference">relative\_size</em>\, <em class="title-reference">override\_encryption</em>\, <em class="title-reference">atime\_scrub</em>\, <em class="title-reference">cifs\_change\_notify\_enabled</em>\, <em class="title-reference">global\_file\_locking\_enabled</em>\, <em class="title-reference">guarantee\_type</em>\, <em class="title-reference">dr\_cache</em> added in REST\.
* na\_ontap\_rest\_cli \- Add POST and DELETE examples\.
* na\_ontap\_rest\_info \- removed example which has option <em class="title-reference">gather\_subset</em> set to <em class="title-reference">all</em> from documentation\.
* na\_ontap\_rest\_info \- updated <em class="title-reference">extends\_documentation\_fragment</em> \& argument spec\.
* na\_ontap\_s3\_buckets \- added new option <em class="title-reference">versioning\_state</em>\, requires ONTAP 9\.11\.1 or later\.
* na\_ontap\_s3\_buckets \- updated <em class="title-reference">extends\_documentation\_fragment</em> \& argument spec\.
* na\_ontap\_s3\_services \- added <em class="title-reference">is\_http\_enabled</em>\, <em class="title-reference">is\_https\_enabled</em>\, <em class="title-reference">port</em> and <em class="title-reference">secure\_port</em> option for <em class="title-reference">s3</em> service\, requires ONTAP 9\.8 or later\.
* na\_ontap\_s3\_users \- new option <em class="title-reference">regenerate\_keys</em> and <em class="title-reference">delete\_keys</em> added in REST\, <em class="title-reference">delete\_keys</em> requires ONTAP 9\.14 or later\.
* na\_ontap\_snapmirror \- new option <em class="title-reference">quiesced\_time\_out</em> added to wait for quiesce job to complete\.
* na\_ontap\_svm \- added <em class="title-reference">allowed</em> option for <em class="title-reference">s3</em> service\, requires ONTAP 9\.7 or later\.
* na\_ontap\_svm \- updated documentation for <em class="title-reference">allowed\_protocols</em> \& <em class="title-reference">services</em>\.
* na\_ontap\_volume \- new option <em class="title-reference">granular\_data</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">large\_size\_enabled</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">nas\_application\_template\.cifs\_share\_name</em> added in REST\, requires ONTAP 9\.11 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">nas\_application\_template\.snaplock\.\*</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">nas\_application\_template\.snapshot\_locking\_enabled</em> added in REST\, requires ONTAP 9\.13\.1 or later\.

<a id="netapp-storagegrid-3"></a>
#### netapp\.storagegrid

* na\_sg\_grid\_account \- new option <em class="title-reference">allow\_compliance\_mode</em> and <em class="title-reference">max\_retention\_days</em> added for tenant account\, requires storageGRID 11\.9 or later\.
* na\_sg\_grid\_gateway \- new option <em class="title-reference">enable\_tenant\_manager</em>\, <em class="title-reference">enable\_grid\_manager</em> and <em class="title-reference">node\_type</em> added to support management interfaces\.
* na\_sg\_grid\_group \- new option <em class="title-reference">read\_only</em> added for grid groups\.
* na\_sg\_grid\_info \- LB endpoints and HA group in info module\.
* na\_sg\_org\_group \- new option <em class="title-reference">read\_only</em> added for tenant groups\.

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

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* all \- Minimum <code>py\-pure\-client</code> version increased to 1\.57\.0 due to release of Realms feature
* purefa\_dsrole \- Add support for non\-system\-defined directory service roles with new parameter <em class="title-reference">name</em>
* purefa\_hg \- Added support for Fusion
* purefa\_host \- Added Fusion support
* purefa\_info \- Add <code>enabled</code> value for network subnets
* purefa\_info \- Add <code>policies\` list of dicts to \`\`filesystem</code> subset for each share\.
* purefa\_info \- Add <code>time\_remaining</code> field for non\-deleted directory snapshots
* purefa\_info \- Add performance data for network interfaces
* purefa\_info \- Added new section <code>realms</code>\.
* purefa\_info \- Added new subset <code>fleet</code>
* purefa\_info \- Deprecate <code>network\.\<interface\>\.hwaddr</code> \- replaced by <code>network\.\<interface\>\.mac\_address</code>
* purefa\_info \- Deprecate <code>network\.\<interface\>\.slaves</code> \- replaced by <code>network\.\<interface\>\.subinterfaces</code>
* purefa\_info \- Expose directory service role management access policies if they exist
* purefa\_info \- Exposed password policy information
* purefa\_info \- SnaptoNFS support removed from Purity//FA 6\.6\.0 and higher\.
* purefa\_info \- Update KMIP information collection to use REST v2\, exposing full certifcate content
* purefa\_info \- VNC feature deprecated from Purity//FA 6\.8\.0\.
* purefa\_offload \- Add support for S3 Offload <code>uri</code> and <code>auth\_region</code> parameters
* purefa\_pg \- Added Fusion support\.
* purefa\_pgsched \- Added support for Fusion\.
* purefa\_pgsnap \- Added support for Fusion\.
* purefa\_pgsnap \- Expose created protection group snapshot data in the module return dict
* purefa\_pod\_replica \- Added Fusion support\.
* purefa\_pods \- Added support for Fusion with <code>context</code> parameter\.
* purefa\_policy \- New policy type of <code>password</code> added\. Currently the only default management policy can be updated
* purefa\_smtp \- Added support for additional parameters\, including encryption mode and email prefixs and email sender name\.
* purefa\_snap \- Added Fusion support\.
* purefa\_subnet \- Remove default value for MTU t ostop restting to default on enable/disable of subnet\. Creation will still default to 1500 if not provided\.
* purefa\_timeout \- Convert to REST v2
* purefa\_user \- Added parameter for SSH public keys and API token timeout
* purefa\_user \- Converted to use REST v2
* purefa\_user \- When changing API token or timout for an existing user\, the user role must be provided or it will revert to <code>readonly</code>
* purefa\_vg \- Added support for Fusion
* purefa\_vlan \- Convert to REST v2
* purefa\_vnc \- VNC feature deprecated from Purity//FA 6\.8\.0\.
* purefa\_volume \- Added <code>context</code> parameter to support fleet operations

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* Support Kerberos/GSSAPI authentication by passing <code>use\_gssapi\: true</code> instead of <code>username</code> and <code>password</code>\.
* Support setting a specific CA file for certificate validation
* activation\_keys\, content\_credentials\, content\_view\_publish\, content\_views\, lifecycle\_environments\, repositories\, sync\_plans roles \- Allow specifying the organization for each item individually \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1653](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1653)\)
* host\, hostgroup\, domain\, operatingsystem\, subnet\, organization\, location \- support setting hidden parameters
* snapshot \- add <code>quiesce</code> option \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1810](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1810)\)
* templates\_import \- Support configuring HTTP Proxy behaviour for template import

<a id="vmware-vmware-10"></a>
#### vmware\.vmware

* \_module\_pyvmomi\_base \- Make sure to use the folder param when searching for VMs based on other common params in get\_vms\_using\_params
* \_vmware \- standardize getter method names and documentation
* added vm\_resource\_info module to collect cpu/memory facts about vms
* argument specs \- Remove redundant argument specs\. Update pyvmomi modules to use new consolidated spec
* clients/\_pyvmomi \- adds explicit init params instead of using dict
* clients/\_rest \- adds explicit init params instead of using dict
* cluster\_ha \- migrate the vmware\_cluster\_ha module from community to here
* cluster\_info \- Migrate cluster\_info module from the community\.vmware collection to here
* content\_library\_item\_info \- Migrate content\_library\_item\_info module from the vmware\.vmware\_rest collection to here
* content\_template \- Fix bad reference of library variable that was refactored to library\_id
* deploy\_content\_library\_ovf \- migrate the vmware\_content\_deploy\_ovf\_template module from community to here
* deploy\_content\_library\_ovf \- update parameters to be consistent with other deploy modules
* deploy\_content\_library\_template \- migrate the vmware\_content\_deploy\_template module from community to here
* deploy\_content\_library\_template \- update parameters to be consistent with other deploy modules
* deploy\_folder\_template \- add module to deploy a vm from a template in a vsphere folder
* doc fragments \- Remove redundant fragments\. Update pyvmomi modules to use new consolidated docs
* esxi\_connection \- migrate the vmware\_host module from community to here
* esxi\_host \- Added inventory plugin to gather info about ESXi hosts
* esxi\_host \- migrate the vmware\_host module from community to here
* esxi\_hosts \- Add inventory host filtering based on jinja statements
* esxi\_hosts inventory \- include moid property in output always
* esxi\_maintenance\_mode \- migrate esxi maintenance module from community
* folder \- migrate vmware\_folder module from community to here
* info \- Made vm\_name variable required only when state is set to present in content\_template module
* local\_content\_library \- migrate the vmware\_content\_library\_manager module from community to here
* pyvmomi \- update object search by name method to use propertycollector\, which speeds up results significantly
* pyvmomi module base \- refactor class to use the pyvmomi shared client util class as a base
* rest module base \- refactor class to use the rest shared client util class as a base
* subscribed\_content\_library \- migrate the vmware\_content\_library\_manager module from community to here
* upload\_content\_library\_ovf \- Add module to upload an ovf/ova to a content library
* vm\_powerstate \- migrate vmware\_guest\_powerstate module from community to here
* vms \- Add inventory host filtering based on jinja statements
* vms \- added vms inventory plugin\. consolidated shared docs/code with esxi hosts inventory plugin
* vms inventory \- include moid property in output always

<a id="vmware-vmware-rest-4"></a>
#### vmware\.vmware\_rest

* Deprecated modules with redundant functionality in vmware\.vmware\. The next major release is currently not planned\, so no removal date is provided\. See [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/589](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/589)
* info \- changed relative links in README\.md to absolute links

<a id="breaking-changes--porting-guide-4"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-30"></a>
#### Ansible\-core

* Support for the <code>toml</code> library has been removed from TOML inventory parsing and dumping\. Use <code>tomli</code> for parsing on Python 3\.10\. Python 3\.11 and later have built\-in support for parsing\. Use <code>tomli\-w</code> to support outputting inventory in TOML format\.
* assert \- The <code>quiet</code> argument must be a commonly\-accepted boolean value\. Previously\, unrecognized values were silently treated as False\.
* conditionals \- Conditional expressions that result in non\-boolean values are now an error by default\. Such results often indicate unintentional use of templates where they are not supported\, resulting in a conditional that is always true\. When this option is enabled\, conditional expressions which are a literal <code>None</code> or empty string will evaluate as true\, for backwards compatibility\. The error can be temporarily changed to a deprecation warning by enabling the <code>ALLOW\_BROKEN\_CONDITIONALS</code> config option\.
* first\_found lookup \- When specifying <code>files</code> or <code>paths</code> as a templated list containing undefined values\, the undefined list elements will be discarded with a warning\. Previously\, the entire list would be discarded without any warning\.
* internals \- The <code>AnsibleLoader</code> and <code>AnsibleDumper</code> classes for working with YAML are now factory functions and cannot be extended\.
* internals \- The <code>ansible\.utils\.native\_jinja</code> Python module has been removed\.
* lookup plugins \- Lookup plugins called as <em class="title-reference">with\_\(lookup\)</em> will no longer have the <em class="title-reference">\_subdir</em> attribute set\.
* lookup plugins \- <code>terms</code> will always be passed to <code>run</code> as the first positional arg\, where previously it was sometimes passed as a keyword arg when using <code>with\_</code> syntax\.
* loops \- Omit placeholders no longer leak between loop item templating and task templating\. Previously\, <code>omit</code> placeholders could remain embedded in loop items after templating and be used as an <code>omit</code> for task templating\. Now\, values resolving to <code>omit</code> are dropped immediately when loop items are templated\. To turn missing values into an <code>omit</code> for task templating\, use <code>\| default\(omit\)</code>\. This solution is backward\-compatible with previous versions of ansible\-core\.
* modules \- Ansible modules using <code>sys\.excepthook</code> must use a standard <code>try/except</code> instead\.
* plugins \- Any plugin that sources or creates templates must properly tag them as trusted\.
* plugins \- Custom Jinja plugins that accept undefined top\-level arguments must opt in to receiving them\.
* plugins \- Custom Jinja plugins that use <code>environment\.getitem</code> to retrieve undefined values will now trigger a <code>MarkerError</code> exception\. This exception must be handled to allow the plugin to return a <code>Marker</code>\, or the plugin must opt\-in to accepting <code>Marker</code> values\.
* public API \- The <code>ansible\.vars\.fact\_cache\.FactCache</code> wrapper has been removed\.
* serialization of <code>omit</code> sentinel \- Serialization of variables containing <code>omit</code> sentinels \(e\.g\.\, by the <code>to\_json</code> and <code>to\_yaml</code> filters or <code>ansible\-inventory</code>\) will fail if the variable has not completed templating\. Previously\, serialization succeeded with placeholder strings emitted in the serialized output\.
* set\_fact \- The string values \"yes\"\, \"no\"\, \"true\" and \"false\" were previously converted \(ignoring case\) to boolean values when not using Jinja2 native mode\. Since Jinja2 native mode is always used\, this conversion no longer occurs\. When boolean values are required\, native boolean syntax should be used where variables are defined\, such as in YAML\. When native boolean syntax is not an option\, the <code>bool</code> filter can be used to parse string values into booleans\.
* template lookup \- The <code>convert\_data</code> option is deprecated and no longer has any effect\. Use the <code>from\_json</code> filter on the lookup result instead\.
* templating \- Access to <code>\_</code> prefixed attributes and methods\, and methods with known side effects\, is no longer permitted\. In cases where a matching mapping key is present\, the associated value will be returned instead of an error\. This increases template environment isolation and ensures more consistent behavior between the <code>\.</code> and <code>\[\]</code> operators\.
* templating \- Conditionals and lookups which use embedded inline templates in Jinja string constants now display a warning\. These templates should be converted to their expression equivalent\.
* templating \- Many Jinja plugins \(filters\, lookups\, tests\) and methods previously silently ignored undefined inputs\, which often masked subtle errors\. Passing an undefined argument to a Jinja plugin or method that does not declare undefined support now results in an undefined value\.
* templating \- Templates are always rendered in Jinja2 native mode\. As a result\, non\-string values are no longer automatically converted to strings\.
* templating \- Templates resulting in <code>None</code> are no longer automatically converted to an empty string\.
* templating \- Templates with embedded inline templates that were not contained within a Jinja string constant now result in an error\, as support for multi\-pass templating was removed for security reasons\. In most cases\, such templates can be easily rewritten to avoid the use of embedded inline templates\.
* templating \- The <code>allow\_unsafe\_lookups</code> option no longer has any effect\. Lookup plugins are responsible for tagging strings containing templates to allow evaluation as a template\.
* templating \- The result of the <code>range\(\)</code> global function cannot be returned from a template\- it should always be passed to a filter \(e\.g\.\, <code>random</code>\)\. Previously\, range objects returned from an intermediate template were always converted to a list\, which is inconsistent with inline consumption of range objects\.
* templating \- <code>\#jinja2\:</code> overrides in templates with invalid override names or types are now templating errors\.

<a id="ansible-posix-1"></a>
#### ansible\.posix

* firewalld \- Changed the type of forward and masquerade options from str to bool \([https\://github\.com/ansible\-collections/ansible\.posix/issues/582](https\://github\.com/ansible\-collections/ansible\.posix/issues/582)\)\.
* firewalld \- Changed the type of icmp\_block\_inversion option from str to bool \([https\://github\.com/ansible\-collections/ansible\.posix/issues/586](https\://github\.com/ansible\-collections/ansible\.posix/issues/586)\)\.

<a id="community-postgresql-7"></a>
#### community\.postgresql

* postgresql\_info \- the <code>db</code> alias is deprecated and will be removed in the next major release\, use the <code>login\_db</code> argument instead\.
* postgresql\_pg\_hba \- regarding \#776 \'keep\_comments\_at\_rules\' has been deprecated and won\'t do anything\, the default is to keep the comments at the rules they are specified with\. keep\_comments\_at\_rules will be removed in 5\.0\.0 \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_user \- the <code>db</code> alias is deprecated and will be removed in the next major release\, use the <code>login\_db</code> argument instead\.

<a id="dellemc-enterprise-sonic-1"></a>
#### dellemc\.enterprise\_sonic

* sonic\_aaa \- Update AAA module to align with SONiC functionality \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/382](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/382)\)\.
* sonic\_bgp\_communities \- Change \'aann\' option as a suboption of \'members\' and update its type from string to list of strings \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/440](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/440)\)\.
* sonic\_route\_maps \- Change the \'set ip\_next\_hop\' option from a single\-line option to a dictionary \([https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/421](https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/421)\)\.
* sonic\_vlan\_mapping \- New vlan\_mapping resource module\. The users of the vlan\_mapping resource module with playbooks written for the SONiC 4\.1 will need to revise their playbooks based on the new argspec to use those playbooks for SONiC 4\.2 and later versions\. \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/296](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/296)\)\.

<a id="theforeman-foreman-3"></a>
#### theforeman\.foreman

* Drop support for Ansible 2\.9\.
* Drop support for Python 2\.7 and 3\.5\.

<a id="deprecated-features-7"></a>
### Deprecated Features

<a id="ansible-core-31"></a>
#### Ansible\-core

* CLI \- The <code>\-\-inventory\-file</code> option alias is deprecated\. Use the <code>\-i</code> or <code>\-\-inventory</code> option instead\.
* Strategy Plugins \- Use of strategy plugins not provided in <code>ansible\.builtin</code> are deprecated and do not carry any backwards compatibility guarantees going forward\. A future release will remove the ability to use external strategy plugins\. No alternative for third party strategy plugins is currently planned\.
* <code>ansible\.module\_utils\.compat\.datetime</code> \- The datetime compatibility shims are now deprecated\. They are scheduled to be removed in <code>ansible\-core</code> v2\.21\. This includes <code>UTC</code>\, <code>utcfromtimestamp\(\)</code> and <code>utcnow</code> importable from said module \([https\://github\.com/ansible/ansible/pull/81874](https\://github\.com/ansible/ansible/pull/81874)\)\.
* bool filter \- Support for coercing unrecognized input values \(including None\) has been deprecated\. Consult the filter documentation for acceptable values\, or consider use of the <code>truthy</code> and <code>falsy</code> tests\.
* cache plugins \- The <em class="title-reference">ansible\.plugins\.cache\.base</em> Python module is deprecated\. Use <em class="title-reference">ansible\.plugins\.cache</em> instead\.
* callback plugins \- The <em class="title-reference">v2\_on\_any</em> callback method is deprecated\. Use specific callback methods instead\.
* callback plugins \- The v1 callback API \(callback methods not prefixed with <em class="title-reference">v2\_</em>\) is deprecated\. Use <em class="title-reference">v2\_</em> prefixed methods instead\.
* conditionals \- Conditionals using Jinja templating delimiters \(e\.g\.\, <code>\{\{</code>\, <code>\{\%</code>\) should be rewritten as expressions without delimiters\, unless the entire conditional value is a single template that resolves to a trusted string expression\. This is useful for dynamic indirection of conditional expressions\, but is limited to trusted literal string expressions\.
* config \- The <code>ACTION\_WARNINGS</code> config has no effect\. It previously disabled command warnings\, which have since been removed\.
* config \- The <code>DEFAULT\_JINJA2\_NATIVE</code> option has no effect\. Jinja2 native mode is now the default and only option\.
* config \- The <code>DEFAULT\_NULL\_REPRESENTATION</code> option has no effect\. Null values are no longer automatically converted to another value during templating of single variable references\.
* display \- The <code>Display\.get\_deprecation\_message</code> method has been deprecated\. Call <code>Display\.deprecated</code> to display a deprecation message\, or call it with <code>removed\=True</code> to raise an <code>AnsibleError</code>\.
* file loading \- Loading text files with <code>DataLoader</code> containing data that cannot be decoded under the expected encoding is deprecated\. In most cases the encoding must be UTF\-8\, although some plugins allow choosing a different encoding\. Previously\, invalid data was silently wrapped in Unicode surrogate escape sequences\, often resulting in later errors or other data corruption\.
* first\_found lookup \- Splitting of file paths on <code>\,\;\:</code> is deprecated\. Pass a list of paths instead\. The <code>split</code> method on strings can be used to split variables into a list as needed\.
* interpreter discovery \- The <code>auto\_legacy</code> and <code>auto\_legacy\_silent</code> options for <code>INTERPRETER\_PYTHON</code> are deprecated\. Use <code>auto</code> or <code>auto\_silent</code> options instead\, as they have the same effect\.
* oneline callback \- The <code>oneline</code> callback and its associated ad\-hoc CLI args \(<code>\-o</code>\, <code>\-\-one\-line</code>\) are deprecated\.
* paramiko \- The paramiko connection plugin has been deprecated with planned removal in 2\.21\.
* playbook variables \- The <code>play\_hosts</code> variable has been deprecated\, use <code>ansible\_play\_batch</code> instead\.
* plugin error handling \- The <code>AnsibleError</code> constructor arg <code>suppress\_extended\_error</code> is deprecated\. Using <code>suppress\_extended\_error\=True</code> has the same effect as <code>show\_content\=False</code>\.
* template lookup \- The jinja2\_native option is no longer used in the Ansible Core code base\. Jinja2 native mode is now the default and only option\.
* templating \- Support for enabling Jinja2 extensions \(not plugins\) has been deprecated\.
* templating \- The <code>disable\_lookups</code> option has no effect\, since plugins must be updated to apply trust before any templating can be performed\.
* tree callback \- The <code>tree</code> callback and its associated ad\-hoc CLI args \(<code>\-t</code>\, <code>\-\-tree</code>\) are deprecated\.

<a id="amazon-aws-7"></a>
#### amazon\.aws

* autoscaling\_group \- the <code>decrement\_desired\_capacity</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Management of instances attached an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the <code>replace\_batch\_size</code>\, <code>lc\_check</code> and <code>lt\_check</code> parameters have been deprecated and will be removed in release 14\.0\.0 of this collection\. Rolling replacement of instances in an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance\_refresh</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the functionality provided through the <code>detach\_instances</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Management of instances attached an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the functionality provided through the <code>replace\_all\_instances</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Rolling replacement of instances in an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance\_refresh</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.
* autoscaling\_group \- the functionality provided through the <code>replace\_instances</code> parameter has been deprecated and will be removed in release 14\.0\.0 of this collection\. Management of instances attached an autoscaling group can be performed using the  <code>amazon\.aws\.autoscaling\_instance</code> module \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2396](https\://github\.com/ansible\-collections/amazon\.aws/pull/2396)\)\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* Added deprecation warnings for the above plugins\, displayed when running respective filter plugins\.
* <em class="title-reference">parse\_cli\_textfsm</em> filter plugin is deprecated and will be removed in a future release after 2027\-02\-01\. Use <em class="title-reference">ansible\.utils\.cli\_parse</em> with the <em class="title-reference">ansible\.utils\.textfsm\_parser</em> parser as a replacement\.
* <em class="title-reference">parse\_cli</em> filter plugin is deprecated and will be removed in a future release after 2027\-02\-01\. Use <em class="title-reference">ansible\.utils\.cli\_parse</em> as a replacement\.
* <em class="title-reference">parse\_xml</em> filter plugin is deprecated and will be removed in a future release after 2027\-02\-01\. Use <em class="title-reference">ansible\.utils\.cli\_parse</em> with the <em class="title-reference">ansible\.utils\.xml\_parser</em> parser as a replacement\.

<a id="cisco-ios-5"></a>
#### cisco\.ios

* ios\_vlans \- deprecate mtu\, please use ios\_interfaces to configure mtu to the interface where vlans is applied\.

<a id="community-crypto-10"></a>
#### community\.crypto

* Support for ansible\-core 2\.11\, 2\.12\, 2\.13\, 2\.14\, 2\.15\, and 2\.16 is deprecated\, and will be removed in the next major release \(community\.crypto 3\.0\.0\)\. Some modules might still work with some of these versions afterwards\, but we will no longer keep compatibility code that was needed to support them\. Note that this means that support for all Python versions before 3\.7 will be dropped\, also on the target side \([https\://github\.com/ansible\-collections/community\.crypto/issues/559](https\://github\.com/ansible\-collections/community\.crypto/issues/559)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/839](https\://github\.com/ansible\-collections/community\.crypto/pull/839)\)\.
* Support for cryptography \< 3\.4 is deprecated\, and will be removed in the next major release \(community\.crypto 3\.0\.0\)\. Some modules might still work with older versions of cryptography\, but we will no longer keep compatibility code that was needed to support them \([https\://github\.com/ansible\-collections/community\.crypto/issues/559](https\://github\.com/ansible\-collections/community\.crypto/issues/559)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/839](https\://github\.com/ansible\-collections/community\.crypto/pull/839)\)\.
* openssl\_pkcs12 \- the PyOpenSSL based backend is deprecated and will be removed from community\.crypto 3\.0\.0\. From that point on you need cryptography 3\.0 or newer to use this module \([https\://github\.com/ansible\-collections/community\.crypto/issues/667](https\://github\.com/ansible\-collections/community\.crypto/issues/667)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/831](https\://github\.com/ansible\-collections/community\.crypto/pull/831)\)\.

<a id="community-hrobot-7"></a>
#### community\.hrobot

* boot \- the various <code>arch</code> suboptions have been deprecated and will be removed from community\.hrobot 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/134](https\://github\.com/ansible\-collections/community\.hrobot/pull/134)\)\.

<a id="community-postgresql-8"></a>
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

<a id="community-vmware-9"></a>
#### community\.vmware

* module\_utils\.vmware \- host\_version\_at\_least is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2303](https\://github\.com/ansible\-collections/community\.vmware/pull/2303)\)\.
* plugin\_utils\.inventory \- this plugin util is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2304](https\://github\.com/ansible\-collections/community\.vmware/pull/2304)\)\.
* plugins\.httpapi \- this is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2306](https\://github\.com/ansible\-collections/community\.vmware/pull/2306)\)\.
* vcenter\_folder \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2340](https\://github\.com/ansible\-collections/community\.vmware/pull/2340)\)\.
* vm\_device\_helper\.py \- is\_nvdimm\_controller is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vm\_device\_helper\.py \- is\_nvdimm\_device is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- find\_host\_portgroup\_by\_name is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- find\_vmdk\_file is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- network\_exists\_by\_name is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware \- vmdk\_disk\_path\_split is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware\_cluster\_ha \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2321](https\://github\.com/ansible\-collections/community\.vmware/pull/2321)\)\.
* vmware\_cluster\_info \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2260](https\://github\.com/ansible\-collections/community\.vmware/pull/2260)\)\.
* vmware\_content\_deploy\_ovf\_template \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2332](https\://github\.com/ansible\-collections/community\.vmware/pull/2332)\)\.
* vmware\_content\_deploy\_template \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2332](https\://github\.com/ansible\-collections/community\.vmware/pull/2332)\)\.
* vmware\_content\_library\_manager \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2345](https\://github\.com/ansible\-collections/community\.vmware/pull/2345)\)\.
* vmware\_host \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2337](https\://github\.com/ansible\-collections/community\.vmware/pull/2337)\)\.
* vmware\_host\_inventory \- the inventory plugin is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2283](https\://github\.com/ansible\-collections/community\.vmware/pull/2283)\)\.
* vmware\_maintenancemode \- the module has been deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2293](https\://github\.com/ansible\-collections/community\.vmware/pull/2293)\)\.
* vmware\_rest\_client \- get\_folder\_by\_name is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2311](https\://github\.com/ansible\-collections/community\.vmware/pull/2311)\)\.
* vmware\_vm\_inventory \- the inventory plugin is deprecated and will be removed in community\.vmware 7\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2283](https\://github\.com/ansible\-collections/community\.vmware/pull/2283)\)\.

<a id="vmware-vmware-rest-5"></a>
#### vmware\.vmware\_rest

* content\_library\_item\_info \- the module has been deprecated and will be removed in vmware\.vmware\_rest 5\.0\.0

<a id="removed-features-previously-deprecated-3"></a>
### Removed Features \(previously deprecated\)

* The collection <code>ibm\.spectrum\_virtualize</code> has been completely removed from Ansible\.
  It has been renamed to <code>ibm\.storage\_virtualize</code>\.
  The collection will be completely removed from Ansible eventually\.
  Please update your FQCNs from <code>ibm\.spectrum\_virtualize</code> to <code>ibm\.storage\_virtualize</code>\.
* The deprecated <code>cisco\.asa</code> collection has been removed \([https\://forum\.ansible\.com/t/38960](https\://forum\.ansible\.com/t/38960)\)\.
* The deprecated <code>community\.network</code> collection has been removed \([https\://forum\.ansible\.com/t/8030](https\://forum\.ansible\.com/t/8030)\)\.
* The google\.cloud collection has been removed from Ansible 12 due to violations of the Ansible inclusion requirements\.
  The collection has [unresolved sanity test failures](https\://github\.com/ansible\-collections/google\.cloud/issues/613)\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details \([https\://forum\.ansible\.com/t/8609](https\://forum\.ansible\.com/t/8609)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install google\.cloud</code>\.
* The sensu\.sensu\_go collection has been removed from Ansible 12 due to violations of the Ansible inclusion requirements\.
  The collection has [unresolved sanity test failures](https\://github\.com/sensu/sensu\-go\-ansible/issues/362)\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details \([https\://forum\.ansible\.com/t/8380](https\://forum\.ansible\.com/t/8380)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install sensu\.sensu\_go</code>\.

<a id="ansible-core-32"></a>
#### Ansible\-core

* Remove deprecated plural form of collection path \([https\://github\.com/ansible/ansible/pull/84156](https\://github\.com/ansible/ansible/pull/84156)\)\.
* Removed deprecated STRING\_CONVERSION\_ACTION \([https\://github\.com/ansible/ansible/issues/84220](https\://github\.com/ansible/ansible/issues/84220)\)\.
* encrypt \- passing unsupported passlib hashtype now raises AnsibleFilterError\.
* manager \- remove deprecated include\_delegate\_to parameter from get\_vars API\.
* modules \- Modules returning non\-UTF8 strings now result in an error\. The <code>MODULE\_STRICT\_UTF8\_RESPONSE</code> setting can be used to disable this check\.
* removed deprecated pycompat24 and compat\.importlib\.
* selector \- remove deprecated compat\.selector related files \([https\://github\.com/ansible/ansible/pull/84155](https\://github\.com/ansible/ansible/pull/84155)\)\.
* windows \- removed common module functions <code>ConvertFrom\-AnsibleJson</code>\, <code>Format\-AnsibleException</code> from Windows modules as they are not used and add unneeded complexity to the code\.

<a id="ansible-posix-2"></a>
#### ansible\.posix

* skippy \- Remove skippy pluglin as it is no longer supported\([https\://github\.com/ansible\-collections/ansible\.posix/issues/350](https\://github\.com/ansible\-collections/ansible\.posix/issues/350)\)\.

<a id="cisco-nxos-6"></a>
#### cisco\.nxos

* This release removes all deprecated plugins that have reached their end\-of\-life\, including\:
* nxos\_snmp\_community
* nxos\_snmp\_contact
* nxos\_snmp\_host
* nxos\_snmp\_location
* nxos\_snmp\_user

<a id="junipernetworks-junos-1"></a>
#### junipernetworks\.junos

* This includes the following modules\:
* This release removes all deprecated plugins that have reached their end\-of\-life\.
* junos\_scp

<a id="security-fixes-1"></a>
### Security Fixes

<a id="ansible-core-33"></a>
#### Ansible\-core

* include\_vars action \- Ensure that result masking is correctly requested when vault\-encrypted files are read\. \(CVE\-2024\-8775\)
* task result processing \- Ensure that action\-sourced result masking \(<code>\_ansible\_no\_log\=True</code>\) is preserved\. \(CVE\-2024\-8775\)
* templating \- Ansible\'s template engine no longer processes Jinja templates in strings unless they are marked as coming from a trusted source\. Untrusted strings containing Jinja template markers are ignored with a warning\. Examples of trusted sources include playbooks\, vars files\, and many inventory sources\. Examples of untrusted sources include module results and facts\. Plugins which have not been updated to preserve trust while manipulating strings may inadvertently cause them to lose their trusted status\.
* templating \- Changes to conditional expression handling removed numerous instances of insecure multi\-pass templating \(which could result in execution of untrusted template expressions\)\.
* user action won\'t allow ssh\-keygen\, chown and chmod to run on existing ssh public key file\, avoiding traversal on existing symlinks \(CVE\-2024\-9902\)\.

<a id="cloudscale-ch-cloud-3"></a>
#### cloudscale\_ch\.cloud

* Validate API tokens before passing them to Ansible\, to ensure that a badly formed one \(i\.e\.\, one with newlines\) is not accidentally logged\.

<a id="bugfixes-9"></a>
### Bugfixes

<a id="ansible-core-34"></a>
#### Ansible\-core

* Ansible will now also warn when reserved keywords are set via a module \(set\_fact\, include\_vars\, etc\)\.
* Ansible\.Basic \- Fix <code>required\_if</code> check when the option value to check is unset or set to null\.
* Correctly return <code>False</code> when using the <code>filter</code> and <code>test</code> Jinja tests on plugin names which are not filters or tests\, respectively\. \(resolves issue [https\://github\.com/ansible/ansible/issues/82084](https\://github\.com/ansible/ansible/issues/82084)\)
* Do not run implicit <code>flush\_handlers</code> meta tasks when the whole play is excluded from the run due to tags specified\.
* Errors now preserve stacked error messages even when YAML is involved\.
* Fix a display\.debug statement with the wrong param in \_get\_diff\_data\(\) method
* Fix disabling SSL verification when installing collections and roles from git repositories\. If <code>\-\-ignore\-certs</code> isn\'t provided\, the value for the <code>GALAXY\_IGNORE\_CERTS</code> configuration option will be used \([https\://github\.com/ansible/ansible/issues/83326](https\://github\.com/ansible/ansible/issues/83326)\)\.
* Fix ipv6 pattern bug in lib/ansible/parsing/utils/addresses\.py \([https\://github\.com/ansible/ansible/issues/84237](https\://github\.com/ansible/ansible/issues/84237)\)
* Fix returning \'unreachable\' for the overall task result\. This prevents false positives when a looped task has unignored unreachable items \([https\://github\.com/ansible/ansible/issues/84019](https\://github\.com/ansible/ansible/issues/84019)\)\.
* Implicit <code>meta\: flush\_handlers</code> tasks now have a parent block to prevent potential tracebacks when calling methods like <code>get\_play\(\)</code> on them internally\.
* Improve performance on large inventories by reducing the number of implicit meta tasks\.
* Jinja plugins \- Errors raised will always be derived from <code>AnsibleTemplatePluginError</code>\.
* Optimize the way tasks from within <code>include\_tasks</code>/<code>include\_role</code> are inserted into the play\.
* Time out waiting on become is an unreachable error \([https\://github\.com/ansible/ansible/issues/84468](https\://github\.com/ansible/ansible/issues/84468)\)
* Use consistent multiprocessing context for action write locks
* Use the requested error message in the ansible\.module\_utils\.facts\.timeout timeout function instead of hardcoding one\.
* Windows \- add support for running on system where WDAC is in audit mode with <code>Dynamic Code Security</code> enabled\.
* YAML parsing \- The <em class="title-reference">\!unsafe</em> tag no longer coerces non\-string scalars to strings\.
* <code>ansible\-galaxy</code> — the collection dependency resolver now treats version specifiers starting with <code>\!\=</code> as unpinned\.
* <code>package</code>/<code>dnf</code> action plugins \- provide the reason behind the failure to gather the <code>ansible\_pkg\_mgr</code> fact to identify the package backend
* action plugins \- Action plugins that raise unhandled exceptions no longer terminate playbook loops\. Previously\, exceptions raised by an action plugin caused abnormal loop termination and loss of loop iteration results\.
* ansible\-config \- format galaxy server configs while dumping in JSON format \([https\://github\.com/ansible/ansible/issues/84840](https\://github\.com/ansible/ansible/issues/84840)\)\.
* ansible\-doc \- If none of the files in files exists\, path will be undefined and a direct reference will throw an UnboundLocalError \([https\://github\.com/ansible/ansible/pull/84464](https\://github\.com/ansible/ansible/pull/84464)\)\.
* ansible\-galaxy \- Small adjustments to URL building for <code>download\_url</code> and relative redirects\.
* ansible\-pull change detection will now work independently of callback or result format settings\.
* ansible\-test \- Enable the <code>sys\.unraisablehook</code> work\-around for the <code>pylint</code> sanity test on Python 3\.11\. Previously the work\-around was only enabled for Python 3\.12 and later\. However\, the same issue has been discovered on Python 3\.11\.
* ansible\-test \- Ensure CA certificates are installed on managed FreeBSD instances\.
* ansible\-test \- Fix support for PowerShell module\_util imports with the <code>\-Optional</code> flag\.
* ansible\-test \- Fix support for detecting PowerShell modules importing module utils with the newer <code>\#AnsibleRequires</code> format\.
* ansible\-test \- Fix traceback that occurs after an interactive command fails\.
* ansible\-test \- Fix up coverage reporting to properly translate the temporary path of integration test modules to the expected static test module path\.
* ansible\-test \- Fixed traceback when handling certain YAML errors in the <code>yamllint</code> sanity test\.
* ansible\-test \- Managed macOS instances now use the <code>sudo\_chdir</code> option for the <code>sudo</code> become plugin to avoid permission errors when dropping privileges\.
* ansible\-vault will now correctly handle <em class="title-reference">\-\-prompt</em>\, previously it would issue an error about stdin if no 2nd argument was passed
* ansible\_uptime\_second \- added ansible\_uptime\_seconds fact support for AIX \([https\://github\.com/ansible/ansible/pull/84321](https\://github\.com/ansible/ansible/pull/84321)\)\.
* apt\_key module \- prevent tests from running when apt\-key was removed
* base\.yml \- deprecated libvirt\_lxc\_noseclabel config\.
* build \- Pin <code>wheel</code> in <code>pyproject\.toml</code> to ensure compatibility with supported <code>setuptools</code> versions\.
* config \- various fixes to config lookup plugin \([https\://github\.com/ansible/ansible/pull/84398](https\://github\.com/ansible/ansible/pull/84398)\)\.
* copy \- refactor copy module for simplicity\.
* copy action now prevents user from setting internal options\.
* debconf \- set empty password values \([https\://github\.com/ansible/ansible/issues/83214](https\://github\.com/ansible/ansible/issues/83214)\)\.
* debug \- hide loop vars in debug var display \([https\://github\.com/ansible/ansible/issues/65856](https\://github\.com/ansible/ansible/issues/65856)\)\.
* default callback \- Error context is now shown for failing tasks that use the <code>debug</code> action\.
* display \- The <code>Display\.deprecated</code> method once again properly handles the <code>removed\=True</code> argument \([https\://github\.com/ansible/ansible/issues/82358](https\://github\.com/ansible/ansible/issues/82358)\)\.
* distro \- add support for Linux Mint Debian Edition \(LMDE\) \([https\://github\.com/ansible/ansible/issues/84934](https\://github\.com/ansible/ansible/issues/84934)\)\.
* distro \- detect Debian as os\_family for LMDE 6 \([https\://github\.com/ansible/ansible/issues/84934](https\://github\.com/ansible/ansible/issues/84934)\)\.
* dnf5 \- Handle forwarded exceptions from dnf5\-5\.2\.13 where a generic <code>RuntimeError</code> was previously raised
* dnf5 \- fix <code>is\_installed</code> check for packages that are not installed but listed as provided by an installed package \([https\://github\.com/ansible/ansible/issues/84578](https\://github\.com/ansible/ansible/issues/84578)\)
* dnf5 \- fix installing a package using <code>state\=latest</code> when a binary of the same name as the package is already installed \([https\://github\.com/ansible/ansible/issues/84259](https\://github\.com/ansible/ansible/issues/84259)\)
* dnf5 \- fix traceback when <code>enable\_plugins</code>/<code>disable\_plugins</code> is used on <code>python3\-libdnf5</code> versions that do not support this functionality
* dnf5 \- libdnf5 \- use <code>conf\.pkg\_gpgcheck</code> instead of deprecated <code>conf\.gpgcheck</code> which is used only as a fallback
* dnf5 \- matching on a binary can be achieved only by specifying a full path \([https\://github\.com/ansible/ansible/issues/84334](https\://github\.com/ansible/ansible/issues/84334)\)
* facts \- gather pagesize and calculate respective values depending upon architecture \([https\://github\.com/ansible/ansible/issues/84773](https\://github\.com/ansible/ansible/issues/84773)\)\.
* facts \- skip if distribution file path is directory\, instead of raising error \([https\://github\.com/ansible/ansible/issues/84006](https\://github\.com/ansible/ansible/issues/84006)\)\.
* find \- skip ENOENT error code while recursively enumerating files\. find module will now be tolerant to race conditions that remove files or directories from the target it is currently inspecting\. \([https\://github\.com/ansible/ansible/issues/84873](https\://github\.com/ansible/ansible/issues/84873)\)\.
* first\_found lookup \- Corrected return value documentation to reflect None \(not empty string\) for no files found\.
* gather\_facts action now defaults to <em class="title-reference">ansible\.legacy\.setup</em> if <em class="title-reference">smart</em> was set\, no network OS was found and no other alias for <em class="title-reference">setup</em> was present\.
* gather\_facts action will now issues errors and warnings as appropriate if a network OS is detected but no facts modules are defined for it\.
* gather\_facts action\, will now add setup when \'smart\' appears with other modules in the FACTS\_MODULES setting \(\#84750\)\.
* get\_url \- add support for BSD\-style checksum digest file \([https\://github\.com/ansible/ansible/issues/84476](https\://github\.com/ansible/ansible/issues/84476)\)\.
* get\_url \- fix honoring <code>filename</code> from the <code>content\-disposition</code> header even when the type is <code>inline</code> \([https\://github\.com/ansible/ansible/issues/83690](https\://github\.com/ansible/ansible/issues/83690)\)
* host\_group\_vars \- fixed defining the \'key\' variable if the get\_vars method is called with cache\=False \([https\://github\.com/ansible/ansible/issues/84384](https\://github\.com/ansible/ansible/issues/84384)\)
* include\_vars \- fix including previously undefined hash variables with hash\_behaviour merge \([https\://github\.com/ansible/ansible/issues/84295](https\://github\.com/ansible/ansible/issues/84295)\)\.
* iptables \- Allows the wait parameter to be used with iptables chain creation \([https\://github\.com/ansible/ansible/issues/84490](https\://github\.com/ansible/ansible/issues/84490)\)
* linear strategy \- fix executing <code>end\_role</code> meta tasks for each host\, instead of handling these as implicit run\_once tasks \([https\://github\.com/ansible/ansible/issues/84660](https\://github\.com/ansible/ansible/issues/84660)\)\.
* local connection plugin \- Become timeout errors now include all received data\. Previously\, the most recently\-received data was discarded\.
* local connection plugin \- Ensure <code>become</code> success validation always occurs\, even when an active plugin does not set <code>prompt</code>\.
* local connection plugin \- Fixed cases where the internal <code>BECOME\-SUCCESS</code> message appeared in task output\.
* local connection plugin \- Fixed hang or spurious failure when data arrived concurrently on stdout and stderr during a successful <code>become</code> operation validation\.
* local connection plugin \- Fixed hang when a become plugin expects a prompt but a password was not provided\.
* local connection plugin \- Fixed hang when an active become plugin incorrectly signals lack of prompt\.
* local connection plugin \- Fixed hang when an internal become read timeout expired before the password prompt was written\.
* local connection plugin \- Fixed hang when only one of stdout or stderr was closed by the <code>become\_exe</code> subprocess\.
* local connection plugin \- Fixed long timeout/hang for <code>become</code> plugins that repeat their prompt on failure \(e\.g\.\, <code>sudo</code>\, some <code>su</code> implementations\)\.
* local connection plugin \- Fixed silent ignore of <code>become</code> failures and loss of task output when data arrived concurrently on stdout and stderr during <code>become</code> operation validation\.
* local connection plugin \- Fixed task output header truncation when post\-become data arrived before <code>become</code> operation validation had completed\.
* lookup plugins \- The <code>terms</code> arg to the <code>run</code> method is now always a list\. Previously\, there were cases where a non\-list could be received\.
* module arg templating \- When using a templated raw task arg and a templated <code>args</code> keyword\, args are now merged\. Previously use of templated raw task args silently ignored all values from the templated <code>args</code> keyword\.
* module defaults \- Module defaults are no longer templated unless they are used by a task that does not override them\. Previously\, all module defaults for all modules were templated for every task\.
* module respawn \- limit to supported Python versions
* package\_facts module when using \'auto\' will return the first package manager found that provides an output\, instead of just the first one\, as this can be foreign and not have any packages\.
* psrp \- Improve stderr parsing when running raw commands that emit error records or stderr lines\.
* regex\_search filter \- Corrected return value documentation to reflect None \(not empty string\) for no match\.
* respawn \- use copy of env variables to update existing PYTHONPATH value \([https\://github\.com/ansible/ansible/issues/84954](https\://github\.com/ansible/ansible/issues/84954)\)\.
* runas become \- Fix up become logic to still get the SYSTEM token with the most privileges when running as SYSTEM\.
* sequence lookup \- sequence query/lookups without positional arguments now return a valid list if their kwargs comprise a valid sequence expression \([https\://github\.com/ansible/ansible/issues/82921](https\://github\.com/ansible/ansible/issues/82921)\)\.
* service\_facts \- skip lines which does not contain service names in openrc output \([https\://github\.com/ansible/ansible/issues/84512](https\://github\.com/ansible/ansible/issues/84512)\)\.
* ssh \- Improve the logic for parsing CLIXML data in stderr when working with Windows host\. This fixes issues when the raw stderr contains invalid UTF\-8 byte sequences and improves embedded CLIXML sequences\.
* ssh \- Raise exception when sshpass returns error code \([https\://github\.com/ansible/ansible/issues/58133](https\://github\.com/ansible/ansible/issues/58133)\)\.
* ssh \- connection options were incorrectly templated during <code>reset\_connection</code> tasks \([https\://github\.com/ansible/ansible/pull/84238](https\://github\.com/ansible/ansible/pull/84238)\)\.
* stability \- Fixed silent process failure on unhandled IOError/OSError under <code>linear</code> strategy\.
* su become plugin \- Ensure generated regex from <code>prompt\_l10n</code> config values is properly escaped\.
* su become plugin \- Ensure that password prompts are correctly detected in the presence of leading output\. Previously\, this case resulted in a timeout or hang\.
* su become plugin \- Ensure that trailing colon is expected on all <code>prompt\_l10n</code> config values\.
* sudo become plugin \- The <em class="title-reference">sudo\_chdir</em> config option allows the current directory to be set to the specified value before executing sudo to avoid permission errors when dropping privileges\.
* sunos \- remove hard coding of virtinfo command in facts gathering code \([https\://github\.com/ansible/ansible/pull/84357](https\://github\.com/ansible/ansible/pull/84357)\)\.
* to\_yaml/to\_nice\_yaml filters \- Eliminated possibility of keyword arg collisions with internally\-set defaults\.
* unarchive \- Clamp timestamps from beyond y2038 to representible values when unpacking zip files on platforms that use 32\-bit time\_t \(e\.g\. Debian i386\)\.
* uri \- Form location correctly when the server returns a relative redirect \([https\://github\.com/ansible/ansible/issues/84540](https\://github\.com/ansible/ansible/issues/84540)\)
* uri \- Handle HTTP exceptions raised while reading the content \([https\://github\.com/ansible/ansible/issues/83794](https\://github\.com/ansible/ansible/issues/83794)\)\.
* uri \- mark <code>url</code> as required \([https\://github\.com/ansible/ansible/pull/83642](https\://github\.com/ansible/ansible/pull/83642)\)\.
* user \- Create Buildroot subclass as alias to Busybox \([https\://github\.com/ansible/ansible/issues/83665](https\://github\.com/ansible/ansible/issues/83665)\)\.
* user \- Set timeout for passphrase interaction\.
* user \- Update prompt for SSH key passphrase \([https\://github\.com/ansible/ansible/issues/84484](https\://github\.com/ansible/ansible/issues/84484)\)\.
* user \- Use higher precedence HOME\_MODE as UMASK for path provided \([https\://github\.com/ansible/ansible/pull/84482](https\://github\.com/ansible/ansible/pull/84482)\)\.
* user action will now require O\(force\) to overwrite the public part of an ssh key when generating ssh keys\, as was already the case for the private part\.
* user module now avoids changing ownership of files symlinked in provided home dir skeleton
* vars lookup \- The <code>default</code> substitution only applies when trying to look up a variable which is not defined\. If the variable is defined\, but templates to an undefined value\, the <code>default</code> substitution will not apply\. Use the <code>default</code> filter to coerce those values instead\.
* wait\_for\_connection \- a warning was displayed if any hosts used a local connection \([https\://github\.com/ansible/ansible/issues/84419](https\://github\.com/ansible/ansible/issues/84419)\)

<a id="amazon-aws-8"></a>
#### amazon\.aws

* cloudformation \- Fix bug where termination protection is not updated when create\_changeset\=true is used for stack updates \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2391](https\://github\.com/ansible\-collections/amazon\.aws/pull/2391)\)\.
* ec2\_instance \- Fix issue where EC2 instance module failed to apply security groups when both <code>network</code> and <code>vpc\_subnet\_id</code> were specified\, caused by passing <code>None</code> to discover\_security\_groups\(\) \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2488](https\://github\.com/ansible\-collections/amazon\.aws/pull/2488)\)\.
* ec2\_security\_group \- Fix the diff mode issue when creating a security group containing a rule with a managed prefix list \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2373](https\://github\.com/ansible\-collections/amazon\.aws/issues/2373)\)\.
* ec2\_vpc\_nacl\_info \- Fix failure when listing NetworkACLs and no ACLs are found \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2425](https\://github\.com/ansible\-collections/amazon\.aws/issues/2425)\)\.
* ec2\_vpc\_net \- handle ipv6\_cidr <code>false</code> and no Ipv6CidrBlockAssociationSet in vpc \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2374](https\://github\.com/ansible\-collections/amazon\.aws/pull/2374)\)\.
* elbv2 \- Fix load balancer listener comparison when DefaultActions contain any action other than forward \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2377](https\://github\.com/ansible\-collections/amazon\.aws/issues/2377)\)\.
* iam\_access\_key \- add missing requirements checks \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2465](https\://github\.com/ansible\-collections/amazon\.aws/pull/2465)\)\.
* lambda \- Remove non UTF\-8 data \(contents of Lambda ZIP file\) from the module output to avoid Ansible error \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2386](https\://github\.com/ansible\-collections/amazon\.aws/issues/2386)\)\.
* lookup/aws\_account\_attribute \- plugin should return a list when <code>wantlist\=True</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2552](https\://github\.com/ansible\-collections/amazon\.aws/pull/2552)\)\.
* module\_utils\.botocore \- fixed type aliasing \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* module\_utils/ec2 \- catch error code <code>InvalidElasticIpID\.NotFound</code> on function <code>create\_nat\_gateway\(\)</code>\, sometimes the <code>allocate\_address</code> API calls will return the ID for a new elastic IP resource before it can be consistently referenced \([https\://github\.com/ansible\-collections/amazon\.aws/issues/1872](https\://github\.com/ansible\-collections/amazon\.aws/issues/1872)\)\.
* plugin\_utils\.botocore \- fixed type aliasing \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2497](https\://github\.com/ansible\-collections/amazon\.aws/pull/2497)\)\.
* rds\_cluster \- Fix issue occurring when updating RDS cluster domain \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2390](https\://github\.com/ansible\-collections/amazon\.aws/issues/2390)\)\.
* s3\_bucket \- Do not use default region as location constraint when creating bucket on ceph cluster \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2420](https\://github\.com/ansible\-collections/amazon\.aws/issues/2420)\)\.

<a id="ansible-netcommon-4"></a>
#### ansible\.netcommon

* libssh connection plugin \- stop using long\-deprecated and now removed internal field from ansible\-core\'s base connection plugin class \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/522](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/522)\, [https\://github\.com/ansible\-collections/ansible\.netcommon/issues/690](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/690)\, [https\://github\.com/ansible\-collections/ansible\.netcommon/pull/691](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/691)\)\.

<a id="ansible-posix-3"></a>
#### ansible\.posix

* acl \- Fixed to set ACLs on paths mounted with NFS version 4 correctly \([https\://github\.com/ansible\-collections/ansible\.posix/issues/240](https\://github\.com/ansible\-collections/ansible\.posix/issues/240)\)\.
* mount \- Handle <code>boot</code> option on Linux\, NetBSD and OpenBSD correctly \([https\://github\.com/ansible\-collections/ansible\.posix/issues/364](https\://github\.com/ansible\-collections/ansible\.posix/issues/364)\)\.
* mount \- If a comment is appended to a fstab entry\, state present creates a double\-entry \([https\://github\.com/ansible\-collections/ansible\.posix/issues/595](https\://github\.com/ansible\-collections/ansible\.posix/issues/595)\)\.

<a id="ansible-windows-6"></a>
#### ansible\.windows

* ansible\.windows\.win\_powershell \- Add extra checks to avoid <code>GetType</code> error when converting the output object \- ttps\://github\.com/ansible\-collections/ansible\.windows/issues/708
* setup \- Add better detection for VMWare base virtualization platforms \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/753](https\://github\.com/ansible\-collections/ansible\.windows/issues/753)
* win\_group\_membership \- Fix bug when input <code>members</code> contained duplicate members that were not already present in the group \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/736](https\://github\.com/ansible\-collections/ansible\.windows/issues/736)
* win\_package \- Support check mode with local file path sources
* win\_powershell \- Ensure <code>\$Ansible\.Result \= \@\(\)</code> as an empty array is returned as an empty list and not null \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/686](https\://github\.com/ansible\-collections/ansible\.windows/issues/686)
* win\_updates \- Only set the Access control sections on the temporary directory created by the module\. This avoids the error when the <code>SeSecurityPrivilege</code> privilege isn\'t present\.

<a id="arista-eos-3"></a>
#### arista\.eos

* Fixed an issue in the <em class="title-reference">compare\_configs</em> method where unnecessary negate commands were generated for ACL entries already present in both <em class="title-reference">have</em> and <em class="title-reference">want</em> configurations\.
* Improved validation logic for ACL sequence numbers and content matching to ensure idempotency\.
* Prevented redundant configuration updates for Access Control Lists\.
* fix facts gathering for ebgp\-multihop attribute\.

<a id="cisco-ios-6"></a>
#### cisco\.ios

* Added a test to validate the gathered state for VLAN configuration context\, improving reliability\.
* Added support for FourHundredGigE\, FiftyGigE and FourHundredGigabitEthernet\.
* Cleaned up unit tests that were passing for the wrong reasons\. The updated tests now ensure the right config sections are verified for VLAN configurations\.
* Fix overridden state operations to ensure excluded VLANs in the provided configuration are removed\, thus overriding the VLAN configuration\.
* Fix purged state operation to enable users to completely remove VLAN configurations\.
* Fixed an issue with VLAN configuration gathering where pre\-filled data was blocking proper fetching of dynamic VLAN details\. Now VLAN facts are populated correctly for all cases\.
* Fixes an issue with facts gathering failing when an sub interface is in a deleted state\.
* Improve documentation to provide clarity on the \"shutdown\" variable\.
* Improve unit tests to align with the changes made\.
* Made improvements to ensure VLAN facts are gathered properly\, both for specific configurations and general VLAN settings\.
* ios\_acls \- Fixed issue where cisco\.ios\.ios\_acls module failed to process IPv6 ACL remarks\, causing unsupported parameter errors\.
* ios\_logging\_global \- Fixed issue where cisco\.ios\.logging\_global module was not showing idempotent behaviour when trap was set to informational\.
* ios\_route\_maps \- Fix removal of ACLs in replaced state to properly remove unspecified ACLs while leaving specified ones intact\.
* ios\_route\_maps \- Fix removal of ACLs logic in replaced state to properly remove unspecified ACLs while leaving specified ones intact\.
* ios\_route\_maps \- Fixes an issue where \'no description value\' is an invalid command on the latest devices\.
* ios\_vlans \- Defaut mtu would be captured \(1500\) and no configuration for mtu is allowed via ios\_vlans module\.
* ios\_vlans \- Fixed an issue in the <em class="title-reference">cisco\.ios\.ios\_vlans</em> module on Cisco Catalyst 9000 switches where using state\:purged generated an incorrect command syntax \(<em class="title-reference">no vlan configuration \<vlan\_id\></em> instead of <em class="title-reference">no vlan \<vlan\_id\></em>\)\.
* ios\_vlans \- Resolved a failure in the <em class="title-reference">cisco\.ios\.ios\_vlans</em> module when using state\:deleted\, where the module incorrectly attempted to remove VLANs using <em class="title-reference">no mtu \<value\></em>\, causing an invalid input error\. The fix ensures that the module does not generate <em class="title-reference">no mtu</em> commands during VLAN deletion\, aligning with the correct VLAN removal behavior on Catalyst 9000 switches\.

<a id="cisco-iosxr-4"></a>
#### cisco\.iosxr

* Fixes a bug to allow connections to IOS XRd with cliconf\.
* Fixes idempotency for static routes with encap interfaces

<a id="cisco-ise-1"></a>
#### cisco\.ise

* network\_device \- Fix mask validation to handle None values in NetworkDeviceIPList
* personas\_promote\_primary \- fix timeout issue\.

<a id="cisco-meraki-7"></a>
#### cisco\.meraki

* Ansible utils requirements updated\.
* Change alias \'message\' to \'message\_rule\' due is a reserved ansible word in meraki\_mx\_intrusion\_prevention module\.
* Changes at compare equality function\.
* Issue fixes for workflow\-ansible\-lint\.
* Old playbook tests removed\.
* README fixes\.
* Unable to create Syslog Server Object\. Action module manually fixing\.
* cisco\.meraki\.devices\_switch\_ports idempotency error fixed\.
* cisco\.meraki\.networks\_appliance\_firewall\_l3\_firewall\_rules fails with \"Unexpected failure during module execution \'rules\' \- specific \'rules\' extraction has been removed\.
* cisco\.meraki\.networks\_appliance\_traffic\_shaping\_rules Always Pushes Configuration Even When Unchanged\.
* cisco\.meraki\.networks\_appliance\_vlans\_settings fails with \"msg\" \"Object does not exists\, plugin only has update\" \- specific \'vlansEnabled\' extraction has been removed\.
* cisco\.meraki\.networks\_clients\_info \- incorrect API endpoint\, fixing info module\.
* cisco\.meraki\.networks\_devices\_claim failed with error unexpected keyword argument \'add\_atomically\' \- bad naming solved\.
* cisco\.meraki\.networks\_switch\_stacks delete stack not working\, fixing path parameters\.
* cisco\.meraki\.organizations\_login\_security module update organization security settings\.
* runtime updated requires\_ansible from 2\.14\.0 to \'\>\=2\.15\.0\'\.

<a id="cisco-nxos-7"></a>
#### cisco\.nxos

* Fixed hardware fact gathering failure for CPU utilization parsing on NX\-OS 9\.3\(3\) by handling both list and single value formats of onemin\_percent
* Fixed the invalid feature name error for port\-security by updating the feature mapping from <em class="title-reference">eth\_port\_sec</em> to <em class="title-reference">eth\-port\-sec</em>\.
* Fixes mixed usage of f\-string and format string in action plugin for consistency\.
* Fixes nxos\_user purge deleting non\-local users\,ensuring only local users are removed\.
* \[bgp\_templates\] \- fix the show commands used to ensure task does not fail if BGP is not enabled on the device\.
* lag\_interfaces \- Fix bug where lag interfaces was not erroring on command failure\. \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/923](https\://github\.com/ansible\-collections/cisco\.nxos/pull/923)\)
* nxos\_facts \- Fixes an issue in nxos\_facts where IPv6 addresses within VRF contexts were not being collected in <em class="title-reference">net\_all\_ipv6\_addresses</em>\.
* nxos\_l2\_interfaces \- Fixed handling of \'none\' value in allowed\_vlans to properly set trunk VLAN none
* nxos\_user \- fixes wrong command being generated for purge function
* nxos\_vpc \- fixes failure due to kickstart\_ver\_str not being present

<a id="community-aws-5"></a>
#### community\.aws

* aws\_ssm \- Use <code>head\_bucket</code> to access bucket locations in foreign AWS accounts \([https\://github\.com/ansible\-collections/community\.aws/pull/1987](https\://github\.com/ansible\-collections/community\.aws/pull/1987)\)\.
* ssm \- Strip Powershell <code>CLIXML</code> from <code>stdout</code> \([https\://github\.com/ansible\-collections/community\.aws/issues/1952](https\://github\.com/ansible\-collections/community\.aws/issues/1952)\)\.

<a id="community-crypto-11"></a>
#### community\.crypto

* crypto\_info \- when running the module on Fedora 41 with <code>cryptography</code> installed from the package repository\, the module crashed apparently due to some elliptic curves being removed from libssl against which cryptography is running\, which cryptography did not expect \([https\://github\.com/ansible\-collections/community\.crypto/pull/834](https\://github\.com/ansible\-collections/community\.crypto/pull/834)\)\.

<a id="community-dns-5"></a>
#### community\.dns

* Fix various issues and potential bugs pointed out by linters \([https\://github\.com/ansible\-collections/community\.dns/pull/242](https\://github\.com/ansible\-collections/community\.dns/pull/242)\, [https\://github\.com/ansible\-collections/community\.dns/pull/243](https\://github\.com/ansible\-collections/community\.dns/pull/243)\)\.
* Update Public Suffix List\.

<a id="community-docker-3"></a>
#### community\.docker

* Fix label sanitization code to avoid crashes in case of errors \([https\://github\.com/ansible\-collections/community\.docker/issues/1028](https\://github\.com/ansible\-collections/community\.docker/issues/1028)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1029](https\://github\.com/ansible\-collections/community\.docker/pull/1029)\)\.
* docker\_compose\_v2 \- fix version check for <code>assume\_yes</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1054](https\://github\.com/ansible\-collections/community\.docker/pull/1054)\)\.
* docker\_compose\_v2 \- rename flag for <code>assume\_yes</code> parameter for <code>docker compose up</code> to <code>\-y</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1054](https\://github\.com/ansible\-collections/community\.docker/pull/1054)\)\.
* docker\_compose\_v2 \- use <code>\-\-yes</code> instead of <code>\-y</code> from Docker Compose 2\.34\.0 on \([https\://github\.com/ansible\-collections/community\.docker/pull/1060](https\://github\.com/ansible\-collections/community\.docker/pull/1060)\)\.
* docker\_compose\_v2 \- when using Compose 2\.31\.0 or newer\, revert to the old behavior that image rebuilds\, for example if <code>rebuild\=always</code>\, only result in <code>changed</code> if a container has been restarted \([https\://github\.com/ansible\-collections/community\.docker/issues/1005](https\://github\.com/ansible\-collections/community\.docker/issues/1005)\, [https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011](https\://github\.com/ansible\-collections/community\.docker/issues/pull/1011)\)\.
* docker\_compose\_v2\_exec\, docker\_compose\_v2\_run \- fix missing <code>\-\-env</code> flag while assembling env arguments \([https\://github\.com/ansible\-collections/community\.docker/pull/992](https\://github\.com/ansible\-collections/community\.docker/pull/992)\)\.
* docker\_compose\_v2\_run \- the module has a conflict between the type of parameter it expects and the one it tries to sanitize\. Fix removes the label sanitization step because they are already validated by the parameter definition \([https\://github\.com/ansible\-collections/community\.docker/pull/1034](https\://github\.com/ansible\-collections/community\.docker/pull/1034)\)\.
* docker\_host\_info \- ensure that the module always returns <code>can\_talk\_to\_docker</code>\, and that it provides the correct value even if <code>api\_version</code> is specified \([https\://github\.com/ansible\-collections/community\.docker/issues/993](https\://github\.com/ansible\-collections/community\.docker/issues/993)\, [https\://github\.com/ansible\-collections/community\.docker/pull/995](https\://github\.com/ansible\-collections/community\.docker/pull/995)\)\.
* docker\_image\_build \- work around bug resp\. very unexpected behavior in Docker buildx that overwrites all image names in <code>\-\-output</code> parameters if <code>\-\-tag</code> is provided\, which the module did by default in the past\. The module now only supplies <code>\-\-tag</code> if <code>outputs</code> is empty\. If <code>outputs</code> has entries\, it will add an additional entry with <code>type\=image</code> if no entry of <code>type\=image</code> contains the image name specified by the <code>name</code> and <code>tag</code> options \([https\://github\.com/ansible\-collections/community\.docker/issues/1001](https\://github\.com/ansible\-collections/community\.docker/issues/1001)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1006](https\://github\.com/ansible\-collections/community\.docker/pull/1006)\)\.
* docker\_network \- added waiting while container actually disconnect from Swarm network \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_network \- containers are only reconnected to a network if they really exist \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_network \- enabled \"force\" option in Docker network container disconnect API call \([https\://github\.com/ansible\-collections/community\.docker/pull/999](https\://github\.com/ansible\-collections/community\.docker/pull/999)\)\.
* docker\_swarm\_info \- do not crash when finding Swarm jobs if <code>services\=true</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1003](https\://github\.com/ansible\-collections/community\.docker/issues/1003)\)\.
* vendored Docker SDK for Python \- do not assume that <code>KeyError</code> is always for <code>ApiVersion</code> when querying version fails \([https\://github\.com/ansible\-collections/community\.docker/issues/1033](https\://github\.com/ansible\-collections/community\.docker/issues/1033)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1034](https\://github\.com/ansible\-collections/community\.docker/pull/1034)\)\.

<a id="community-general-16"></a>
#### community\.general

* cloudlare\_dns \- handle exhausted response stream in case of HTTP errors to show nice error message to the user \([https\://github\.com/ansible\-collections/community\.general/issues/9782](https\://github\.com/ansible\-collections/community\.general/issues/9782)\, [https\://github\.com/ansible\-collections/community\.general/pull/9818](https\://github\.com/ansible\-collections/community\.general/pull/9818)\)\.
* dnf\_versionlock \- add support for dnf5 \([https\://github\.com/ansible\-collections/community\.general/issues/9556](https\://github\.com/ansible\-collections/community\.general/issues/9556)\)\.
* homebrew \- fix crash when package names include tap \([https\://github\.com/ansible\-collections/community\.general/issues/9777](https\://github\.com/ansible\-collections/community\.general/issues/9777)\, [https\://github\.com/ansible\-collections/community\.general/pull/9803](https\://github\.com/ansible\-collections/community\.general/pull/9803)\)\.
* homebrew\_cask \- handle unusual brew version strings \([https\://github\.com/ansible\-collections/community\.general/issues/8432](https\://github\.com/ansible\-collections/community\.general/issues/8432)\, [https\://github\.com/ansible\-collections/community\.general/pull/9881](https\://github\.com/ansible\-collections/community\.general/pull/9881)\)\.
* nmcli \- enable changing only the order of DNS servers or search suffixes \([https\://github\.com/ansible\-collections/community\.general/issues/8724](https\://github\.com/ansible\-collections/community\.general/issues/8724)\, [https\://github\.com/ansible\-collections/community\.general/pull/9880](https\://github\.com/ansible\-collections/community\.general/pull/9880)\)\.
* proxmox \- add missing key selection of <code>\'status\'</code> key to <code>get\_lxc\_status</code> \([https\://github\.com/ansible\-collections/community\.general/issues/9696](https\://github\.com/ansible\-collections/community\.general/issues/9696)\, [https\://github\.com/ansible\-collections/community\.general/pull/9809](https\://github\.com/ansible\-collections/community\.general/pull/9809)\)\.
* proxmox\_vm\_info \- the module no longer expects that the key <code>template</code> exists in a dictionary returned by Proxmox \([https\://github\.com/ansible\-collections/community\.general/issues/9875](https\://github\.com/ansible\-collections/community\.general/issues/9875)\, [https\://github\.com/ansible\-collections/community\.general/pull/9910](https\://github\.com/ansible\-collections/community\.general/pull/9910)\)\.
* sudoers \- display stdout and stderr raised while failed validation \([https\://github\.com/ansible\-collections/community\.general/issues/9674](https\://github\.com/ansible\-collections/community\.general/issues/9674)\, [https\://github\.com/ansible\-collections/community\.general/pull/9871](https\://github\.com/ansible\-collections/community\.general/pull/9871)\)\.

<a id="community-library-inventory-filtering-v1-1"></a>
#### community\.library\_inventory\_filtering\_v1

* inventory\_filter plugin utils \- make compatible with ansible\-core\'s Data Tagging feature \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/24](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/24)\)\.
* inventory\_plugin plugin util \- <code>parse\_filters</code> now filters <code>None</code> values with allowed keys \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/27](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/27)\)\.

<a id="community-libvirt-2"></a>
#### community\.libvirt

* libvirt\_lxc \- add configuration for libvirt\_lxc\_noseclabel\.

<a id="community-mysql-3"></a>
#### community\.mysql

* mysql\_db \- fix dump and import to find MariaDB binaries \(mariadb and mariadb\-dump\) when MariaDB 11\+ is used and symbolic links to MySQL binaries are absent\.
* mysql\_user\,mysql\_role \- The sql\_mode ANSI\_QUOTES affects how the modules mysql\_user and mysql\_role compare the existing privileges with the configured privileges\, as well as decide whether double quotes or backticks should be used in the GRANT statements\. Pointing out in issue 671\, the modules mysql\_user and mysql\_role allow users to enable/disable ANSI\_QUOTES in session variable \(within a DB session\, the session variable always overwrites the global one\)\. But due to the issue\, the modules do not check for ANSI\_MODE in the session variable\, instead\, they only check in the GLOBAL one\.That behavior is not only limiting the users\' flexibility\, but also not allowing users to explicitly disable ANSI\_MODE to work around such bugs like [https\://bugs\.mysql\.com/bug\.php\?id\=115953](https\://bugs\.mysql\.com/bug\.php\?id\=115953)\. \([https\://github\.com/ansible\-collections/community\.mysql/issues/671](https\://github\.com/ansible\-collections/community\.mysql/issues/671)\)

<a id="community-postgresql-9"></a>
#### community\.postgresql

* postgresql\_info \- fix failure when a default database is used \(neither <code>db</code> nor <code>login\_db</code> are specified\) \([https\://github\.com/ansible\-collections/community\.postgresql/issues/794](https\://github\.com/ansible\-collections/community\.postgresql/issues/794)\)\.
* postgresql\_info \- fix issue when gathering information fails if user doesn\'t have access to all databases \([https\://github\.com/ansible\-collections/community\.postgresql/pull/788](https\://github\.com/ansible\-collections/community\.postgresql/pull/788)\)\.
* postgresql\_info \- fix module failure when the <code>db</code> parameter is used instead of <code>login\_db</code> \([https\://github\.com/ansible\-collections/community\.postgresql/issues/794](https\://github\.com/ansible\-collections/community\.postgresql/issues/794)\)\.
* postgresql\_pg\_hba \- fixes \#420 by properly handling hash\-symbols in quotes \([https\://github\.com/ansible\-collections/community\.postgresql/pull/766](https\://github\.com/ansible\-collections/community\.postgresql/pull/766)\)
* postgresql\_pg\_hba \- fixes \#705 by preventing invalid strings to be written \([https\://github\.com/ansible\-collections/community\.postgresql/pull/761](https\://github\.com/ansible\-collections/community\.postgresql/pull/761)\)
* postgresql\_pg\_hba \- fixes \#730 by extending the key we use to identify a rule with the connection type \([https\://github\.com/ansible\-collections/community\.postgresql/pull/770](https\://github\.com/ansible\-collections/community\.postgresql/pull/770)\)
* postgresql\_pg\_hba \- fixes \#776 the module won\'t be adding/moving comments repeatedly if \'keep\_comments\_at\_rules\' is \'false\' \([https\://github\.com/ansible\-collections/community\.postgresql/pull/778](https\://github\.com/ansible\-collections/community\.postgresql/pull/778)\)
* postgresql\_pg\_hba \- fixes \#777 the module will ignore the \'address\' and \'netmask\' options again when the contype is \'local\' \([https\://github\.com/ansible\-collections/community\.postgresql/pull/779](https\://github\.com/ansible\-collections/community\.postgresql/pull/779)\)
* postgresql\_pg\_hba \- improves parsing of quoted strings and escaped newlines \([https\://github\.com/ansible\-collections/community\.postgresql/pull/761](https\://github\.com/ansible\-collections/community\.postgresql/pull/761)\)
* postgresql\_privs \-  fix the error occurring when trying to grant a function execution and set the schema to not\-specified \([https\://github\.com/ansible\-collections/community\.postgresql/pull/783](https\://github\.com/ansible\-collections/community\.postgresql/pull/783)\)\.
* postgresql\_table \- consider schema name when checking for table \([https\://github\.com/ansible\-collections/community\.postgresql/issues/817](https\://github\.com/ansible\-collections/community\.postgresql/issues/817)\)\.  Table names are only unique within a schema\. This allows using the same table name in multiple schemas\.
* postgresql\_user \- doesn\'t take password\_encryption into account when checking if a password should be updated \([https\://github\.com/ansible\-collections/community\.postgresql/issues/688](https\://github\.com/ansible\-collections/community\.postgresql/issues/688)\)\.

<a id="community-rabbitmq-3"></a>
#### community\.rabbitmq

* rabbitmq\_publish \- fix support for publishing headers as a part of a message \([https\://github\.com/ansible\-collections/community\.rabbitmq/pull/182](https\://github\.com/ansible\-collections/community\.rabbitmq/pull/182)\)

<a id="community-routeros-4"></a>
#### community\.routeros

* api\_info\, api\_modify \- fields <code>log</code> and <code>log\-prefix</code> in paths <code>ip firewall filter</code>\, <code>ip firewall mangle</code>\, <code>ip firewall nat</code>\, <code>ip firewall raw</code> now have the correct default values \([https\://github\.com/ansible\-collections/community\.routeros/pull/324](https\://github\.com/ansible\-collections/community\.routeros/pull/324)\)\.
* api\_info\, api\_modify \- remove the primary key <code>action</code> from the <code>interface wifi provisioning</code> path\, since RouterOS also allows to create completely duplicate entries \([https\://github\.com/ansible\-collections/community\.routeros/issues/344](https\://github\.com/ansible\-collections/community\.routeros/issues/344)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/345](https\://github\.com/ansible\-collections/community\.routeros/pull/345)\)\.

<a id="community-sops-1"></a>
#### community\.sops

* install role \- <code>sops\_install\_on\_localhost\=false</code> was not working properly if the role was running on more than one host due to a bug in ansible\-core \([https\://github\.com/ansible\-collections/community\.sops/issues/223](https\://github\.com/ansible\-collections/community\.sops/issues/223)\, [https\://github\.com/ansible\-collections/community\.sops/pull/224](https\://github\.com/ansible\-collections/community\.sops/pull/224)\)\.
* install role \- when used with Debian on ARM architecture\, the architecture name is now correctly translated from <code>aarch64</code> to <code>arm64</code> \([https\://github\.com/ansible\-collections/community\.sops/issues/220](https\://github\.com/ansible\-collections/community\.sops/issues/220)\, [https\://github\.com/ansible\-collections/community\.sops/pull/221](https\://github\.com/ansible\-collections/community\.sops/pull/221)\)\.
* load\_vars \- make evaluation compatible with Data Tagging in upcoming ansible\-core release \([https\://github\.com/ansible\-collections/community\.sops/pull/225](https\://github\.com/ansible\-collections/community\.sops/pull/225)\)\.

<a id="community-vmware-10"></a>
#### community\.vmware

* vm\_device\_helper \- Fix \'invalid configuration for device\' error caused by missing fileoperation parameter\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2009](https\://github\.com/ansible\-collections/community\.vmware/pull/2009)\)\.
* vmware\_guest \- Fix errors occuring during hardware version upgrade not being reported\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2010](https\://github\.com/ansible\-collections/community\.vmware/pull/2010)\)\.
* vmware\_guest \- Fix vmware\_guest always reporting change when using dvswitch\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2000](https\://github\.com/ansible\-collections/community\.vmware/pull/2000)\)\.
* vmware\_guest \- setting vApp properties on virtual machines without vApp options raised an AttributeError\. Fix now gracefully handles a <em class="title-reference">None</em> value for vApp options when retrieving current vApp properties \([https\://github\.com/ansible\-collections/community\.vmware/pull/2220](https\://github\.com/ansible\-collections/community\.vmware/pull/2220)\)\.
* vmware\_guest\_tools\_upgrade \- Account for all possible tools status \([https\://github\.com/ansible\-collections/community\.vmware/issues/2237](https\://github\.com/ansible\-collections/community\.vmware/issues/2237)\)\.
* vmware\_object\_role\_permission \- The module ignores changing <code>recursive</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2350](https\://github\.com/ansible\-collections/community\.vmware/pull/2350)\)\.

<a id="community-zabbix-5"></a>
#### community\.zabbix

* Java Gateway Role \- Temporary work around to solve failure on RHEL9\.
* zabbix inventory plugin \- do not require <code>login\_user</code> and <code>login\_password</code> to be present when <code>auth\_token</code> is provided \([https\://github\.com/ansible\-collections/community\.zabbix/pull/1439](https\://github\.com/ansible\-collections/community\.zabbix/pull/1439)\)\.
* zabbix\_agent Role \- Add Zabbix 7\.0 LTS in supported versions for windows\.
* zabbix\_agent Role \- Added ability to set the monitored\_by and proxy\_group values\.
* zabbix\_agent Role \- Set become parameter explicitly to false for API tasks to run without sudo on the local computer\.

<a id="containers-podman-3"></a>
#### containers\.podman

* Don\'t pull image when state is absent or pull\=never \(\#889\)
* Fix idempotency for containers with env vars containing MAX\_SIZE \(\#893\)
* Fix list tags failure in podman\_search \(\#875\)
* Fix podman\_container\_copy examples \(\#882\)
* docs\(podman\_container\) \- improve comments on network property \(\#878\)

<a id="dellemc-enterprise-sonic-2"></a>
#### dellemc\.enterprise\_sonic

* ConnectionError \- Add the needed import of the Ansible ConnectionError exception class for all files where it was previously missing\. \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/445](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/445)\)\.
* Update \'update\_url\' method to handle multiple interface names \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/455](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/455)\)\.
* Update regex search expression for \'not found\' error message in httpapi/sonic\.py \'edit\_config\' method \([https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/443](https\://github\.com/ansible\-collection/dellemc\.enterprise\_sonic/pull/443)\)\.
* sonic\_bgp\_communities \- Fix issues in merged state for standard community\-lists \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/440](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/440)\)\.
* sonic\_copp \- Update reserved CoPP names list \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/481](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/481)\)\.
* sonic\_interfaces \- Remove the restriction preventing configuration of interface speed for port channel member interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/470](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/470)\)\.
* sonic\_l3\_interfaces \- Eliminate unconditional sending of the new autoconf REST API option during replaced and overridden state handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/474](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/474)\)\.
* sonic\_mclag \- Delete any remaining PortChannel members for an mclag domain before attempting to delete the mclag domain \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/463](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/463)\)\.
* sonic\_ospf\_area \- Fix OSPF area bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/466](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/466)\)\.
* sonic\_qos\_interfaces \- Fix command deletion bug \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/473](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/473)\)\.
* sonic\_qos\_wred \- Update QoS WRED regression test case based on SONiC code changes \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/465](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/465)\)\.
* sonic\_stp \- Change the criteria for converting vlans and vlan ranges to handle vlan IDs with more than one digit \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/460](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/460)\)\.
* sonic\_stp \- Fix functionality to allow a value of 0 to be configured for the appropriate integer attributes and refactor module code\([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/477](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/477)\)\.
* sonic\_system \- Catch the ConnectionError exception caused by unconditional fetching of auditd and ip loadshare hash algorithm configuration\, and return empty configuration instead of allowing the uncaught exception to abort all \"system\" operations on SONiC images older than version 4\.4\.0 \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/441](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/441)\)\.
* sonic\_vrrp \- Update delete handling to fix regression failure \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/455](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/455)\)\.
* sonic\_vxlan \- Fix failing regression tests for sonic\_vxlan \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/471](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/471)\)\.

<a id="dellemc-openmanage-9"></a>
#### dellemc\.openmanage

* Internal defect fixes were done for the following modules \- <code>idrac\_network\_attributes</code>\, <code>idrac\_certificates</code>\, <code>idrac\_redfish\_storage\_controller</code>\, <code>idrac\_boot\_order</code> and <code>idrac\_firmware</code>
* Resolved the issue in <code>idrac\_redfish\_storage\_volume</code> module where it returns 404 error on job creation when enabling encryption for virtual drives\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues) /713\)
* idrac\_certificates \- \(Issue 737\) \- Fixed SSL CSR generation for 4096 key size\.

<a id="f5networks-f5-modules-3"></a>
#### f5networks\.f5\_modules

* bigip\_firewall\_address\_list to support both cidr and route domain
* bigip\_monitor\_external \- external monitor user\-defined variables not reflected for non\-common partition
* bigip\_profile\_server\_ssl \- Fixed bug \- create server SSL profile if SSL key is passphrase protected
* bigip\_profile\_server\_ssl to support parent\'s \[None\, \"\"\, \"None\"\] profiles
* bigip\_snmp\_community \- Allow v3 usernames that begin with a number or contains any special characters\.

<a id="fortinet-fortimanager-4"></a>
#### fortinet\.fortimanager

* Changed all input argument name in ansible built\-in documentation to the underscore format\. E\.g\.\, changed \"var\-name\" to \"var\_name\"\.
* Changed parameter type of some parameters\.
* Changed the default playbook examples for each module to pass ansible\-lint\.
* Corrected mainkey of some modules\.
* Fixed a bug where rc\_failed and rc\_succeeded did not work\.
* Improved code logic\, reduced redundant requests for system information\.
* Modified built\-in document to support sanity tests in ansible\-core 2\.18\.0\. No functionality changed\.

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fix errors in Ansible sanity test with Ansible\-core 2\.18
* Github
* Github Issue
* Mantis Issue

<a id="hetzner-hcloud-5"></a>
#### hetzner\.hcloud

* hcloud\_load\_balancer\_service \- Improve unknown certificate id or name error\.
* hcloud\_server \- Only rebuild existing servers\, skip rebuild if the server was just created\.

<a id="ibm-storage-virtualize-3"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_flashcopy \- Added support for creating flashcopy with existing target volume
* ibm\_svc\_manage\_replication \- Added checks for mutually\-exclusive parameters and policing for updating remote\-copy relationship

<a id="infoblox-nios-modules"></a>
#### infoblox\.nios\_modules

* For Host IPv6\, the mac parameter has been renamed to duid\.
* Refined Host record return fields to ensure use\_nextserver and nextserver are only included for IPv4\, as these fields are not applicable to IPv6\.

<a id="kubernetes-core-4"></a>
#### kubernetes\.core

* helm \- Helm version checks did not support RC versions\. They now accept any version tags\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/745](https\://github\.com/ansible\-collections/kubernetes\.core/pull/745)\)\.
* helm\_pull \- Apply no\_log\=True to pass\_credentials to silence false positive warning\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/796](https\://github\.com/ansible\-collections/kubernetes\.core/pull/796)\)\.
* k8s\_drain \- Fix k8s\_drain does not wait for single pod \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/769](https\://github\.com/ansible\-collections/kubernetes\.core/issues/769)\)\.
* k8s\_drain \- Fix k8s\_drain runs into a timeout when evicting a pod which is part of a stateful set  \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/792](https\://github\.com/ansible\-collections/kubernetes\.core/issues/792)\)\.
* kubeconfig option should not appear in module invocation log \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/782](https\://github\.com/ansible\-collections/kubernetes\.core/issues/782)\)\.
* kustomize \- kustomize plugin fails with deprecation warnings \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/639](https\://github\.com/ansible\-collections/kubernetes\.core/issues/639)\)\.
* waiter \- Fix waiting for daemonset when desired number of pods is 0\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/756](https\://github\.com/ansible\-collections/kubernetes\.core/pull/756)\)\.

<a id="lowlydba-sqlserver-2"></a>
#### lowlydba\.sqlserver

* Fix error that occurred when creating a login with <em class="title-reference">skip\_password\_reset</em> as true\. \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/287](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/287)\)
* Fix error when creating an agent job schedule with <em class="title-reference">enabled</em> as true\. \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/288](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/288)\)

<a id="netapp-ontap-5"></a>
#### netapp\.ontap

* Resolved Ansible lint issues\.
* all modules supporting REST \- avoid duplicate calls to api/cluster to get ONTAP version\.
* na\_ontap\_aggregate \- fix issue with \'raid\_type\' change in REST\.
* na\_ontap\_broadcast\_domain \- fix issue with port modification in REST\.
* na\_ontap\_flexcache \- fix typo error in the query \'origins\.cluster\.name\' in REST\.
* na\_ontap\_kerberos\_interface \- updated example in module documentation\.
* na\_ontap\_qtree \- fix timeout issue with qtree delete in REST\.
* na\_ontap\_rest\_info \- rectified subset name to <em class="title-reference">cluster/firmware/history</em>\.
* na\_ontap\_snapshot\_policy \- fix issue with \'retention\_period\' in REST\.

<a id="netbox-netbox-1"></a>
#### netbox\.netbox

* Fix missing netbox\_config\_template module in module\_defaults
* Fixed an isssue with module\_default parameter inheritance for modules netbox\_config\_template\, netbox\_custom\_field\_choice\_set\, netbox\_permission\, netbox\_token\, netbox\_user\, and netbox\_user\_group\.
* fix call /api/status/ instead /api/status in nb\_inventory plugin\. \([https\://github\.com/netbox\-community/ansible\_modules/issues/1335](https\://github\.com/netbox\-community/ansible\_modules/issues/1335)\)\.
* netbox\_ip\_address \- Fixed the problem preventing assignment of an IP address to a network interface

<a id="purestorage-flasharray-3"></a>
#### purestorage\.flasharray

* purefa\_alert \- Fix unreferenced variable error
* purefa\_audits \- Fix issue when <code>start</code> parameter not supplied
* purefa\_dirsnap \- Fixed issues with <code>keep\_for</code> setting and issues related to recovery of deleted snapshots
* purefa\_ds \- Fixed issue with trying to create a pre\-existing system\-defined role
* purefa\_dsrole \- Fixed bug in role creation\.
* purefa\_dsrole \- Fixed bug with DS role having no group or group base cannot be updated
* purefa\_eradication \- Fix incorrect timer settings
* purefa\_hg \- Fixed issue when <code>check\_mode \= true</code> not reporting correct status when adding new hosts to hostgroup\.
* purefa\_host \- Fix issue with no VLAN provided when Purity//FA is a recent version\.
* purefa\_host \- Fix issue with setting preferred\_arrays for a host\.
* purefa\_info \- Cater for zero used space in NFS offloads
* purefa\_info \- <code>exports</code> dict for each share changed to a list of dicts in <code>filesystm</code> subset
* purefa\_inventory \- Fixed quiet failures due to attribute errors
* purefa\_network \- Allow LACP bonds to be children of a VIF
* purefa\_network \- Fix compatability issue with <code>netaddr\>\=1\.2\.0</code>
* purefa\_ntp \- Fix issue with deletion of NTP servers
* purefa\_offload \- Corrected version check logic
* purefa\_pgsnap \- Fixed issue with overwrite failing
* purefa\_pod \- Allow pd to be deleted with contents if <code>delete\_contents</code> specified
* purefa\_pod \- Errored out when setting failover preference for pod
* purefa\_ra \- Fixed duration check logic
* purefa\_sessions \- Correctly report sessions with no start or end time
* purefa\_smtp \- Fixed SMTP deletion issue
* purefa\_snmp \- Fix issues with deleting SNMP entries
* purefa\_snmp\_agent \- Fix issues with deleting v3 agent
* purefa\_vg \- Fixed idempotency issue when clearing volume group QoS settings
* purefa\_vg \- Fixed issue with creating non\-QoS volume groups
* purefa\_vlan \- Allow LACP bonds to be subnet interfaces
* purefa\_volume \- Added error message to warn about moving protected volume
* purefa\_volume \- Errors out when pgroup and add\_to\_pgs used incorrectly
* purefa\_volume \- Fixed issue of unable to move volume from pod to vgroup
* purefa\_volume \- Fixes issue of moving protected volume into volume group

<a id="purestorage-flashblade-3"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Fixed issue with idempotency reported when <code>hard\_limit</code> not provided\.
* purefb\_info \- Fixed <code>AttributeError</code> for <code>snapshot</code> subset when snapshot had been created manually\, rather than using a snapshot policy
* purefb\_info \- Fixed issue with admin token creation time and bucket policies
* purefb\_policy \- Fixed syntax error is account name\.
* purefb\_smtp \- Fix errors that occurred after adding support for smtp encrpytion and using the module on older FlashBlades\.
* purefb\_snap \- Fixed issue where <code>target</code> incorrectly required for a regular snapshot

<a id="telekom-mms-icinga-director-3"></a>
#### telekom\_mms\.icinga\_director

* Add Icinga notification template imports \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/267](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/267)\)

<a id="theforeman-foreman-4"></a>
#### theforeman\.foreman

* callback plugin \- fix another exception when serializing secrets \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1819](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1819)\)
* inventory \- Drop fallback to Host API when Reports API fails\, as this leads to possibly wrong data being used

<a id="vmware-vmware-11"></a>
#### vmware\.vmware

* client utils \- Fixed error message when required library could not be imported
* content\_library\_item\_info \- Library name and ID are ignored if item ID is provided so updated docs and arg parse rules to reflect this
* folder \- replaced non\-existent \'storage\' type with \'datastore\' type
* module\_deploy\_vm\_base \- fix attribute error when deploying to a resource pool
* vms inventory \- fix handling of VMs within VApps

<a id="vmware-vmware-rest-6"></a>
#### vmware\.vmware\_rest

* lookup plugins \- Fixed issue where datacenter search filter was never properly set
* module\_utils \- fixed return value for vmware\.vmware\_rest\.vcenter\_vm\_guest\_filesystem\_directories module
* vcenter\_ovf\_libraryitem \- Update documentation to mention the metadata cannot be updated via conventional means\. Added example showing workaround \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/385](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/385)\)

<a id="known-issues-5"></a>
### Known Issues

<a id="dellemc-openmanage-10"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="purestorage-flasharray-4"></a>
#### purestorage\.flasharray

* All Fusion fleet members will be assumed to be at the same Purity//FA version level as the array connected to by Ansible\.
* FlashArray//CBS is not currently supported as a member of a Fusion fleet

<a id="new-plugins-3"></a>
### New Plugins

<a id="filter-2"></a>
#### Filter

* community\.dns\.reverse\_pointer \- Convert an IP address into a DNS name for reverse lookup\.
* microsoft\.ad\.split\_dn \- Splits an LDAP DistinguishedName\.

<a id="lookup-1"></a>
#### Lookup

* community\.dns\.reverse\_lookup \- Reverse\-look up IP addresses\.
* infoblox\.nios\_modules\.nios\_next\_vlan\_id \- Return the next available VLAN ID

<a id="new-modules-8"></a>
### New Modules

<a id="amazon-aws-9"></a>
#### amazon\.aws

* amazon\.aws\.ec2\_dedicated\_host \- Create\, update or delete \(release\) EC2 dedicated host
* amazon\.aws\.ec2\_dedicated\_host\_info \- Gather information about EC2 Dedicated Hosts in AWS
* amazon\.aws\.rds\_instance\_param\_group\_info \- Describes the RDS parameter group\.
* amazon\.aws\.route53\_key\_signing\_key \- Manages a key\-signing key \(KSK\)

<a id="ansible-windows-7"></a>
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

<a id="check-point-mgmt-2"></a>
#### check\_point\.mgmt

* check\_point\.mgmt\.cp\_mgmt\_user \- Manages user objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_user\_facts \- Get user objects facts on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_user\_template \- Manages user\-template objects on Checkpoint over Web Services API
* check\_point\.mgmt\.cp\_mgmt\_user\_template\_facts \- Get user\-template objects facts on Checkpoint over Web Services API

<a id="cisco-ios-7"></a>
#### cisco\.ios

* cisco\.ios\.ios\_evpn\_ethernet \- Resource module to configure L2VPN EVPN Ethernet Segment\.

<a id="cisco-iosxr-5"></a>
#### cisco\.iosxr

* cisco\.iosxr\.iosxr\_vrf\_interfaces \- Resource module to configure VRF interfaces\.

<a id="cisco-nxos-8"></a>
#### cisco\.nxos

* cisco\.nxos\.nxos\_vrf\_address\_family \- Resource module to configure VRF address family definitions\.

<a id="community-crypto-12"></a>
#### community\.crypto

* community\.crypto\.acme\_certificate\_order\_create \- Create an ACME v2 order\.
* community\.crypto\.acme\_certificate\_order\_finalize \- Finalize an ACME v2 order\.
* community\.crypto\.acme\_certificate\_order\_info \- Obtain information for an ACME v2 order\.
* community\.crypto\.acme\_certificate\_order\_validate \- Validate authorizations of an ACME v2 order\.

<a id="community-docker-4"></a>
#### community\.docker

* community\.docker\.docker\_context\_info \- Retrieve information on Docker contexts for the current user\.

<a id="community-general-17"></a>
#### community\.general

* community\.general\.pacemaker\_resource \- Manage pacemaker resources\.

<a id="community-hrobot-8"></a>
#### community\.hrobot

* community\.hrobot\.reset\_info \- Query information on the resetter of a dedicated server\.
* community\.hrobot\.storagebox \- Modify a storage box\'s basic configuration\.
* community\.hrobot\.storagebox\_info \- Query information on one or more storage boxes\.
* community\.hrobot\.storagebox\_set\_password \- \(Re\)set the password for a storage box\.
* community\.hrobot\.storagebox\_snapshot\_plan \- Modify a storage box\'s snapshot plans\.
* community\.hrobot\.storagebox\_snapshot\_plan\_info \- Query the snapshot plans for a storage box\.

<a id="community-postgresql-10"></a>
#### community\.postgresql

* community\.postgresql\.postgresql\_alter\_system \- Change a PostgreSQL server configuration parameter

<a id="community-vmware-11"></a>
#### community\.vmware

* community\.vmware\.vmware\_drs\_override \- Configure DRS behavior for a specific VM in vSphere

<a id="community-zabbix-6"></a>
#### community\.zabbix

* community\.zabbix\.zabbix\_connector \- Create/Delete/Update Zabbix connectors
* community\.zabbix\.zabbix\_regexp\_info \- Retrieve Zabbix regular expression

<a id="dellemc-enterprise-sonic-3"></a>
#### dellemc\.enterprise\_sonic

* dellemc\.enterprise\_sonic\.sonic\_ssh \- Manage SSH configurations on SONiC\.

<a id="dellemc-powerflex-3"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.nvme\_host \- Manage NVMe Hosts on Dell PowerFlex
* dellemc\.powerflex\.sdt \- Manage SDTs on Dell PowerFlex

<a id="fortinet-fortimanager-5"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_gtp\_ieallowlist \- IE allow list\.
* fortinet\.fortimanager\.fmgr\_gtp\_ieallowlist\_entries \- Entries of allow list for unknown or out\-of\-state IEs\.
* fortinet\.fortimanager\.fmgr\_pkg\_videofilter\_youtubekey \- Configure YouTube API keys\.
* fortinet\.fortimanager\.fmgr\_ums\_setting \- Ums setting

<a id="ibm-storage-virtualize-4"></a>
#### ibm\.storage\_virtualize

* ibm\.storage\_virtualize\.ibm\_sv\_manage\_flashsystem\_grid \- Manages operations of Flashsystem grid containing multiple Storage Virtualize systems

<a id="infoblox-nios-modules-1"></a>
#### infoblox\.nios\_modules

* infoblox\.nios\_modules\.nios\_adminuser \- Configure Infoblox NIOS Admin Users
* infoblox\.nios\_modules\.nios\_vlan \- Configure Infoblox NIOS VLANs

<a id="kubernetes-core-5"></a>
#### kubernetes\.core

* kubernetes\.core\.helm\_registry\_auth \- Helm registry authentication module

<a id="lowlydba-sqlserver-3"></a>
#### lowlydba\.sqlserver

* lowlydba\.sqlserver\.login\_role \- Configures a login\'s  server roles\.
* lowlydba\.sqlserver\.user\_role \- Configures a user\'s role in a database\.

<a id="netapp-ontap-6"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_bgp\_config \- NetApp ONTAP network BGP configuration
* netapp\.ontap\.na\_ontap\_cifs\_privileges \- NetApp ONTAP CIFS privileges

<a id="netapp-storagegrid-4"></a>
#### netapp\.storagegrid

* netapp\.storagegrid\.na\_sg\_grid\_ec\_profile \- Manage EC profiles on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_policy \- Manage ILM policies on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_policy\_tag \- Manage ILM policy tags on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_pool \- Manage ILM pools on StorageGRID\.
* netapp\.storagegrid\.na\_sg\_grid\_ilm\_rule \- Manage ILM rules on StorageGRID\.

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_mac\_address \- Create\, update or delete MAC addresses within NetBox

<a id="purestorage-flasharray-5"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_fleet \- Manage Fusion Fleet
* purestorage\.flasharray\.purefa\_realm \- Manage realms on Pure Storage FlashArrays

<a id="unchanged-collections-9"></a>
### Unchanged Collections

* ansible\.utils \(still version 5\.1\.2\)
* awx\.awx \(still version 24\.6\.1\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.10\.1\)
* cisco\.intersight \(still version 2\.0\.20\)
* cisco\.mso \(still version 2\.9\.0\)
* cloud\.common \(still version 4\.0\.0\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.1\.0\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* dellemc\.unity \(still version 2\.0\.0\)
* ibm\.qradar \(still version 4\.0\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* inspur\.ispim \(still version 2\.2\.3\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubevirt\.core \(still version 2\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* splunk\.es \(still version 4\.0\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 5\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)
