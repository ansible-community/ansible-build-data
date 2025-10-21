# Ansible 13 Release Notes

This changelog describes changes since Ansible 12\.0\.0\.

- <a href="#v13-0-0a4">v13\.0\.0a4</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v13-0-0a3">v13\.0\.0a3</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v13-0-0a2">v13\.0\.0a2</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#changed-collections-2">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>
- <a href="#v13-0-0a1">v13\.0\.0a1</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections-1">Added Collections</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated-1">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#known-issues-1">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="v13-0-0a4"></a>
## v13\.0\.0a4

- <a href="#release-summary">Release Summary</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#community-mysql">community\.mysql</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2025\-10\-21

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 13\.0\.0a4 contains ansible\-core version 2\.20\.0rc2\.
This is a newer version than version 2\.20\.0rc1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection      | Ansible 13.0.0a3 | Ansible 13.0.0a4 | Notes                                                                                                                        |
| --------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| community.mysql | 4.0.0            | 4.0.1            |                                                                                                                              |
| cyberark.pas    | 1.0.35           | 1.0.36           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-1"></a>
#### Ansible\-core

* psrp \- ReadTimeout exceptions now mark host as unreachable instead of fatal \([https\://github\.com/ansible/ansible/issues/85966](https\://github\.com/ansible/ansible/issues/85966)\)

<a id="community-mysql"></a>
#### community\.mysql

* mysql\_info \- Fix slave status for source terminology introduced in MySQL 8\.0\.23 \([https\://github\.com/ansible\-collections/community\.mysql/issues/682](https\://github\.com/ansible\-collections/community\.mysql/issues/682)\)\.
* mysql\_user\, mysql\_role \- fix not existent grant when revoking perms on user/role which do not have any other perms than grant option \([https\://github\.com/ansible\-collections/community\.mysql/issues/664](https\://github\.com/ansible\-collections/community\.mysql/issues/664)\)\.

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.2\)
* ansible\.netcommon \(still version 8\.1\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.2\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.9\.0\)
* check\_point\.mgmt \(still version 6\.5\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.12\.0\)
* cisco\.dnac \(still version 6\.40\.0\)
* cisco\.intersight \(still version 2\.6\.0\)
* cisco\.ios \(still version 11\.1\.1\)
* cisco\.iosxr \(still version 12\.0\.0\)
* cisco\.meraki \(still version 2\.21\.8\)
* cisco\.mso \(still version 2\.11\.0\)
* cisco\.nxos \(still version 11\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.crypto \(still version 3\.0\.4\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.3\.4\)
* community\.docker \(still version 4\.8\.1\)
* community\.general \(still version 11\.4\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.0\.0\)
* community\.hrobot \(still version 2\.6\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.4\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.3\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.routeros \(still version 3\.12\.1\)
* community\.sap\_libs \(still version 1\.5\.0\)
* community\.sops \(still version 2\.2\.4\)
* community\.vmware \(still version 6\.0\.0\)
* community\.windows \(still version 3\.0\.1\)
* community\.zabbix \(still version 4\.1\.1\)
* containers\.podman \(still version 1\.18\.0\)
* cyberark\.conjur \(still version 1\.3\.8\)
* dellemc\.enterprise\_sonic \(still version 3\.2\.0\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.11\.0\)
* fortinet\.fortios \(still version 2\.4\.1\)
* google\.cloud \(still version 1\.9\.0\)
* grafana\.grafana \(still version 6\.0\.5\)
* hetzner\.hcloud \(still version 5\.4\.0\)
* hitachivantara\.vspone\_block \(still version 4\.3\.0\)
* hitachivantara\.vspone\_object \(still version 1\.0\.0\)
* ibm\.storage\_virtualize \(still version 3\.1\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.8\.0\)
* inspur\.ispim \(still version 2\.2\.3\)
* junipernetworks\.junos \(still version 11\.0\.0\)
* kaytus\.ksmanage \(still version 2\.0\.0\)
* kubernetes\.core \(still version 6\.2\.0\)
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
* purestorage\.flasharray \(still version 1\.39\.0\)
* purestorage\.flashblade \(still version 1\.22\.0\)
* ravendb\.ravendb \(still version 1\.0\.3\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.4\.0\)
* theforeman\.foreman \(still version 5\.7\.0\)
* vmware\.vmware \(still version 2\.4\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-0-0a3"></a>
## v13\.0\.0a3

- <a href="#release-summary-1">Release Summary</a>
- <a href="#ansible-core-2">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#community-hrobot">community\.hrobot</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#community-hrobot-1">community\.hrobot</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2025\-10\-15

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="ansible-core-2"></a>
### Ansible\-core

Ansible 13\.0\.0a3 contains ansible\-core version 2\.20\.0rc1\.
This is a newer version than version 2\.20\.0b2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 13.0.0a2 | Ansible 13.0.0a3 | Notes                                                                                                                                                                                                        |
| --------------------------- | ---------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cisco.ios                   | 11.1.0           | 11.1.1           |                                                                                                                                                                                                              |
| community.hrobot            | 2.5.2            | 2.6.1            |                                                                                                                                                                                                              |
| community.proxysql          | 1.6.0            | 1.7.0            |                                                                                                                                                                                                              |
| cyberark.conjur             | 1.3.7            | 1.3.8            | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| dellemc.enterprise_sonic    | 3.0.0            | 3.2.0            |                                                                                                                                                                                                              |
| grafana.grafana             | 6.0.4            | 6.0.5            |                                                                                                                                                                                                              |
| hitachivantara.vspone_block | 4.2.2            | 4.3.0            |                                                                                                                                                                                                              |
| ibm.storage_virtualize      | 3.0.0            | 3.1.0            |                                                                                                                                                                                                              |
| kubernetes.core             | 6.1.0            | 6.2.0            |                                                                                                                                                                                                              |
| purestorage.flashblade      | 1.21.2           | 1.22.0           |                                                                                                                                                                                                              |
| theforeman.foreman          | 5.6.0            | 5.7.0            |                                                                                                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Fallback to empty dict in case grafana\_ini is undefined by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/403](https\://github\.com/grafana/grafana\-ansible\-collection/pull/403)
* Fix Mimir config file validation task by \@Windos in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/428](https\://github\.com/grafana/grafana\-ansible\-collection/pull/428)
* Fixes issue by \@digiserg in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/421](https\://github\.com/grafana/grafana\-ansible\-collection/pull/421)
* Import custom dashboards only when directory exists by \@mahendrapaipuri in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/430](https\://github\.com/grafana/grafana\-ansible\-collection/pull/430)
* Updated YUM repo urls from <em class="title-reference">packages\.grafana\.com</em> to <em class="title-reference">rpm\.grafana\.com</em> by \@DejfCold in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/414](https\://github\.com/grafana/grafana\-ansible\-collection/pull/414)
* Use credentials from grafana\_ini when importing dashboards by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/402](https\://github\.com/grafana/grafana\-ansible\-collection/pull/402)
* do not skip scrape latest github version even in check\_mode by \@cmehat in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/408](https\://github\.com/grafana/grafana\-ansible\-collection/pull/408)
* fix datasource documentation by \@jeremad in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/437](https\://github\.com/grafana/grafana\-ansible\-collection/pull/437)
* fix mimir\_download\_url\_deb \& mimir\_download\_url\_rpm by \@germebl in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/400](https\://github\.com/grafana/grafana\-ansible\-collection/pull/400)
* update catalog info by \@Duologic in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/434](https\://github\.com/grafana/grafana\-ansible\-collection/pull/434)
* use deb822 for newer debian versions by \@Lukas\-Heindl in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/440](https\://github\.com/grafana/grafana\-ansible\-collection/pull/440)

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-3"></a>
#### Ansible\-core

* ansible\-test \- Default to Python 3\.14 in the <code>base</code> and <code>default</code> test containers\.
* ansible\-test \- Filter out pylint messages for invalid filenames and display a notice when doing so\.
* ansible\-test \- Update astroid imports in custom pylint checkers\.
* ansible\-test \- Update pinned <code>pip</code> version to 25\.2\.
* ansible\-test \- Update pinned sanity test requirements\, including upgrading to pylint 4\.0\.0\.

<a id="community-proxysql"></a>
#### community\.proxysql

* proxysql\_mysql\_users \- Creating users with the <code>caching\_sha2\_password</code> plugin \([https\://github\.com/ansible\-collections/community\.proxysql/pull/173](https\://github\.com/ansible\-collections/community\.proxysql/pull/173)\)\.

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

<a id="hitachivantara-vspone-block"></a>
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
* Added support for latest software version 1\.18\.1 for SDS block on AWS\, GCP and Bare metal\.
* Added support for listing storage node primary role status in the output to hv\_sds\_block\_storage\_node\_facts module\.
* Added support to \"Add storage node to the SDS cluster on AWS cloud\" to hv\_sds\_block\_cluster module\.
* Added support to \"Allow CHAP users to access the compute port\" to hv\_sds\_block\_compute\_port\_authentication module
* Added support to \"Attach multiple volumes to multiple servers in one operation\" to hv\_vsp\_one\_volume module\.
* Added support to \"Cancel compute port access permission for CHAP users\" to hv\_sds\_block\_compute\_port\_authentication module
* Added support to \"Get Drive by ID\" to hv\_sds\_block\_drives\_facts module
* Added support to \"Get Protection Domain Information by ID\" to hv\_sds\_block\_protection\_domain\_facts module
* Added support to \"Stop removing storage nodes\" to hv\_sds\_block\_cluster module\.
* Added support to take ldev input in HEX value in all hitachivantara\.vspone\_block\.vsp modules\.
* Updated input parameter name from \"saving\_setting\" to \"capacity\_saving\" in hv\_vsp\_one\_volume module\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_ip \- Changes for updating VLAN\, gateway and IP address
* ibm\_svc\_utils \- Improved error message for unreachable systems

<a id="kubernetes-core"></a>
#### kubernetes\.core

* Add support of skip\-schema\-validation in <code>helm</code> module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/995](https\://github\.com/ansible\-collections/kubernetes\.core/pull/995)\)
* kustomize \- Add support of local environ \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/786](https\://github\.com/ansible\-collections/kubernetes\.core/pull/786)\)\.

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* module\_utils/purefb \- Remove <em class="title-reference">get\_blade\(\)</em> function as not required for REST v2
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
* purefb\_snamp\_agent \- Upgraded to REST v2
* purefb\_snap \- Fusion support added
* purefb\_snap \- Upgraded to REST v2
* purefb\_snmp\_mgr \- Add new <code>state</code> of <code>test</code> to check SNMP manager configuration
* purefb\_snmp\_mgr \- Upgraded to REST v2
* purefb\_subnet \- Upgraded to REST v2
* purefb\_syslog \- Converted to REST v2
* purefb\_target \- Upgraded to REST v2
* purefb\_userpolicy \- Fusion support added
* purefb\_userquota \- Added Fusion support
* purefb\_userquota \- Upgraded to REST v2
* purefb\_virtualhost \- Fusion support added

<a id="deprecated-features"></a>
### Deprecated Features

<a id="community-hrobot"></a>
#### community\.hrobot

* storagebox\* modules \- membership in the <code>community\.hrobot\.robot</code> action group \(module defaults group\) is deprecated\; the modules will be removed from the group in community\.hrobot 3\.0\.0\. Use <code>community\.hrobot\.api</code> instead \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\* modules \- the <code>hetzner\_token</code> option for these modules will be required from community\.hrobot 3\.0\.0 on \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\* modules \- the <code>hetzner\_user</code> and <code>hetzner\_pass</code> options for these modules are deprecated\; support will be removed in community\.hrobot 3\.0\.0\. Use <code>hetzner\_token</code> instead \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_info \- the <code>storageboxes\[\]\.login</code>\, <code>storageboxes\[\]\.disk\_quota</code>\, <code>storageboxes\[\]\.disk\_usage</code>\, <code>storageboxes\[\]\.disk\_usage\_data</code>\, <code>storageboxes\[\]\.disk\_usage\_snapshot</code>\, <code>storageboxes\[\]\.webdav</code>\, <code>storageboxes\[\]\.samba</code>\, <code>storageboxes\[\]\.ssh</code>\, <code>storageboxes\[\]\.external\_reachability</code>\, and <code>storageboxes\[\]\.zfs</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_snapshot\_info \- the <code>snapshots\[\]\.timestamp</code>\, <code>snapshots\[\]\.size</code>\, <code>snapshots\[\]\.filesystem\_size</code>\, <code>snapshots\[\]\.automatic</code>\, and <code>snapshots\[\]\.comment</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_snapshot\_plan \- the <code>plans\[\]\.month</code> return value is deprecated\, since it only returns <code>null</code> with the new API and cannot be set to any other value \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_snapshot\_plan\_info \- the <code>plans\[\]\.month</code> return value is deprecated\, since it only returns <code>null</code> with the new API and cannot be set to any other value \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_subaccount \- the <code>subaccount\.homedirectory</code>\, <code>subaccount\.samba</code>\, <code>subaccount\.ssh</code>\, <code>subaccount\.external\_reachability</code>\, <code>subaccount\.webdav</code>\, <code>subaccount\.readonly</code>\, <code>subaccount\.createtime</code>\, and <code>subaccount\.comment</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.
* storagebox\_subaccount\_info \- the <code>subaccounts\[\]\.accountid</code>\, <code>subaccounts\[\]\.homedirectory</code>\, <code>subaccounts\[\]\.samba</code>\, <code>subaccounts\[\]\.ssh</code>\, <code>subaccounts\[\]\.external\_reachability</code>\, <code>subaccounts\[\]\.webdav</code>\, <code>subaccounts\[\]\.readonly</code>\, <code>subaccounts\[\]\.createtime</code>\, and <code>subaccounts\[\]\.comment</code> return values are deprecated and will be removed from community\.routeros\. Check out the documentation to find out their new names according to the new API \([https\://github\.com/ansible\-collections/community\.hrobot/pull/178](https\://github\.com/ansible\-collections/community\.hrobot/pull/178)\)\.

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-core-4"></a>
#### Ansible\-core

* SIGINT/SIGTERM Handling \- Make SIGINT/SIGTERM handling more robust by splitting concerns between forks and the parent\.

<a id="cisco-ios"></a>
#### cisco\.ios

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

<a id="community-hrobot-1"></a>
#### community\.hrobot

* Avoid using <code>ansible\.module\_utils\.six</code> in more places to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/179](https\://github\.com/ansible\-collections/community\.hrobot/pull/179)\)\.

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

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_ip \- Fixed issues with IP address probe
* ibm\_svc\_manage\_volume \- Fixed data\-type conversion issue for grainsize
* ibm\_svc\_start\_stop\_flashcopy \- Fixed flashcopy start issues when mapping belonged to flashcopy consistency group

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/998](https\://github\.com/ansible\-collections/kubernetes\.core/pull/998)\)\.
* Update the <em class="title-reference">k8s\_cp</em> module to also work for init containers \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/971](https\://github\.com/ansible\-collections/kubernetes\.core/pull/971)\)\.

<a id="new-modules"></a>
### New Modules

<a id="community-proxysql-1"></a>
#### community\.proxysql

* community\.proxysql\.proxysql\_mysql\_hostgroup\_attributes \- Manages hostgroup attributes using the ProxySQL admin interface

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

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_compute\_port \- Manages compute port on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_software\_update\_file\_facts \- Get the information of the update file of the storage software which performed transfer \(upload\) in the storage cluster\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_node\_bmc\_connection \- Manages BMC connection settings for a storage node on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_software\_update \- Manages software update and downgrade on Hitachi SDS Block storage systems\.

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_vsp\_one\_port \- Manages port configuration on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_port\_facts \- Retrieves port information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_server \- Manages servers on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_server\_facts \- Retrieves server information from Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_server\_hba\_facts \- Retrieves server HBA information from Hitachi VSP One storage systems\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\.storage\_virtualize\.ibm\_sv\_manage\_system\_certificate \- Manages system certificates and truststore for replication\, high availability and FlashSystem grid on IBM Storage Virtualize family systems

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_kmip \- Manage FlashBlade KMIP server objects

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* theforeman\.foreman\.content\_view\_history\_info \- Fetch history of a Content View

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* amazon\.aws \(still version 10\.1\.2\)
* ansible\.netcommon \(still version 8\.1\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.2\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* azure\.azcollection \(still version 3\.9\.0\)
* check\_point\.mgmt \(still version 6\.5\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.12\.0\)
* cisco\.dnac \(still version 6\.40\.0\)
* cisco\.intersight \(still version 2\.6\.0\)
* cisco\.iosxr \(still version 12\.0\.0\)
* cisco\.meraki \(still version 2\.21\.8\)
* cisco\.mso \(still version 2\.11\.0\)
* cisco\.nxos \(still version 11\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.crypto \(still version 3\.0\.4\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.dns \(still version 3\.3\.4\)
* community\.docker \(still version 4\.8\.1\)
* community\.general \(still version 11\.4\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.0\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.4\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 4\.0\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.3\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.routeros \(still version 3\.12\.1\)
* community\.sap\_libs \(still version 1\.5\.0\)
* community\.sops \(still version 2\.2\.4\)
* community\.vmware \(still version 6\.0\.0\)
* community\.windows \(still version 3\.0\.1\)
* community\.zabbix \(still version 4\.1\.1\)
* containers\.podman \(still version 1\.18\.0\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.openmanage \(still version 10\.0\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.11\.0\)
* fortinet\.fortios \(still version 2\.4\.1\)
* google\.cloud \(still version 1\.9\.0\)
* hetzner\.hcloud \(still version 5\.4\.0\)
* hitachivantara\.vspone\_object \(still version 1\.0\.0\)
* ieisystem\.inmanage \(still version 3\.0\.0\)
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
* netapp\.ontap \(still version 23\.1\.0\)
* netapp\.storagegrid \(still version 21\.15\.0\)
* netapp\_eseries\.santricity \(still version 1\.4\.1\)
* netbox\.netbox \(still version 3\.21\.0\)
* ngine\_io\.cloudstack \(still version 2\.5\.0\)
* openstack\.cloud \(still version 2\.4\.1\)
* ovirt\.ovirt \(still version 3\.2\.1\)
* purestorage\.flasharray \(still version 1\.39\.0\)
* ravendb\.ravendb \(still version 1\.0\.3\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.4\.0\)
* vmware\.vmware \(still version 2\.4\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-0-0a2"></a>
## v13\.0\.0a2

- <a href="#release-summary-2">Release Summary</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core-5">Ansible\-core</a>
- <a href="#changed-collections-2">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#grafana-grafana-1">grafana\.grafana</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-hrobot-2">community\.hrobot</a>
    - <a href="#community-library-inventory-filtering-v1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#dellemc-powerflex-2">dellemc\.powerflex</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2025\-10\-07

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="added-collections"></a>
### Added Collections

* hitachivantara\.vspone\_object \(version 1\.0\.0\)

<a id="ansible-core-5"></a>
### Ansible\-core

Ansible 13\.0\.0a2 contains ansible\-core version 2\.20\.0b2\.
This is a newer version than version 2\.20\.0b1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-2"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                               | Ansible 13.0.0a1 | Ansible 13.0.0a2 | Notes                                                                                                                        |
| ---------------------------------------- | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws                               | 10.1.1           | 10.1.2           |                                                                                                                              |
| azure.azcollection                       | 3.8.0            | 3.9.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.intersight                         | 2.3.0            | 2.6.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.ios                                | 11.0.0           | 11.1.0           |                                                                                                                              |
| cisco.meraki                             | 2.21.5           | 2.21.8           |                                                                                                                              |
| community.crypto                         | 3.0.3            | 3.0.4            |                                                                                                                              |
| community.dns                            | 3.3.3            | 3.3.4            |                                                                                                                              |
| community.docker                         | 4.7.0            | 4.8.1            |                                                                                                                              |
| community.general                        | 11.3.0           | 11.4.0           |                                                                                                                              |
| community.hrobot                         | 2.5.0            | 2.5.2            |                                                                                                                              |
| community.library_inventory_filtering_v1 | 1.1.1            | 1.1.4            |                                                                                                                              |
| community.routeros                       | 3.11.0           | 3.12.1           |                                                                                                                              |
| community.sap_libs                       | 1.4.2            | 1.5.0            |                                                                                                                              |
| community.sops                           | 2.2.2            | 2.2.4            |                                                                                                                              |
| dellemc.openmanage                       | 10.0.0           | 10.0.1           |                                                                                                                              |
| dellemc.powerflex                        | 2.6.1            | 3.0.0            |                                                                                                                              |
| f5networks.f5_modules                    | 1.38.0           | 1.39.0           | There are no changes recorded in the changelog.                                                                              |
| fortinet.fortimanager                    | 2.10.0           | 2.11.0           |                                                                                                                              |
| fortinet.fortios                         | 2.4.0            | 2.4.1            |                                                                                                                              |
| google.cloud                             | 1.8.0            | 1.9.0            |                                                                                                                              |
| grafana.grafana                          | 6.0.3            | 6.0.4            |                                                                                                                              |
| hetzner.hcloud                           | 5.2.0            | 5.4.0            |                                                                                                                              |
| hitachivantara.vspone_block              | 4.2.0            | 4.2.2            | The collection did not have a changelog in this version.                                                                     |
| hitachivantara.vspone_object             |                  | 1.0.0            | The collection was added to Ansible                                                                                          |
| purestorage.flasharray                   | 1.38.0           | 1.39.0           |                                                                                                                              |
| vmware.vmware                            | 2.3.0            | 2.4.0            |                                                                                                                              |

<a id="major-changes-1"></a>
### Major Changes

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* The OpenManage Enterprise\, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2\.19\.

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Supported new versions 7\.6\.3 and 7\.6\.4\.
* Supported the authentication method when using username and password in v7\.6\.4\.

<a id="grafana-grafana-1"></a>
#### grafana\.grafana

* Add SUSE support to Alloy role by \@pozsa in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/423](https\://github\.com/grafana/grafana\-ansible\-collection/pull/423)
* Fixes to foldersFromFilesStructure option by \@root\-expert in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/351](https\://github\.com/grafana/grafana\-ansible\-collection/pull/351)
* Migrate RedHat install to ansible\.builtin\.package by \@r65535 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/431](https\://github\.com/grafana/grafana\-ansible\-collection/pull/431)
* add macOS support to alloy role by \@l50 in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/418](https\://github\.com/grafana/grafana\-ansible\-collection/pull/418)
* replace None with \[\] for safe length checks by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/426](https\://github\.com/grafana/grafana\-ansible\-collection/pull/426)

<a id="minor-changes-1"></a>
### Minor Changes

<a id="ansible-core-6"></a>
#### Ansible\-core

* DataLoader \- Update <code>DataLoader\.get\_basedir</code> to be an abspath
* known\_hosts \- return rc and stderr when ssh\-keygen command fails for further debugging \([https\://github\.com/ansible/ansible/issues/85850](https\://github\.com/ansible/ansible/issues/85850)\)\.

<a id="cisco-ios-1"></a>
#### cisco\.ios

* ios\_config \- added answering prompt functionality while working in config mode on ios device
* ios\_facts \- Add chassis\_id value to ansible\_net\_neighbors dictionary for lldp neighbours\.

<a id="community-dns"></a>
#### community\.dns

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.dns/pull/287](https\://github\.com/ansible\-collections/community\.dns/pull/287)\)\.

<a id="community-docker"></a>
#### community\.docker

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.docker/pull/1138](https\://github\.com/ansible\-collections/community\.docker/pull/1138)\)\.
* docker\_container \- support missing fields and new mount types in <code>mounts</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1129](https\://github\.com/ansible\-collections/community\.docker/issues/1129)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1134](https\://github\.com/ansible\-collections/community\.docker/pull/1134)\)\.

<a id="community-general"></a>
#### community\.general

* github\_app\_access\_token lookup plugin \- add support for GitHub Enterprise Server \([https\://github\.com/ansible\-collections/community\.general/issues/10879](https\://github\.com/ansible\-collections/community\.general/issues/10879)\, [https\://github\.com/ansible\-collections/community\.general/pull/10880](https\://github\.com/ansible\-collections/community\.general/pull/10880)\)\.
* gitlab\_group\_variable \- add <code>description</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/10812](https\://github\.com/ansible\-collections/community\.general/pull/10812)\)\.
* gitlab\_instance\_variable \- add <code>description</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/10812](https\://github\.com/ansible\-collections/community\.general/pull/10812)\)\.
* gitlab\_project\_variable \- add <code>description</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/10812](https\://github\.com/ansible\-collections/community\.general/pull/10812)\, [https\://github\.com/ansible\-collections/community\.general/issues/8584](https\://github\.com/ansible\-collections/community\.general/issues/8584)\, [https\://github\.com/ansible\-collections/community\.general/issues/10809](https\://github\.com/ansible\-collections/community\.general/issues/10809)\)\.
* keycloak\_client \- add idempotent support for <code>optional\_client\_scopes</code> and <code>optional\_client\_scopes</code>\, and ensure consistent change detection between check mode and live run \([https\://github\.com/ansible\-collections/community\.general/issues/5495](https\://github\.com/ansible\-collections/community\.general/issues/5495)\, [https\://github\.com/ansible\-collections/community\.general/pull/10842](https\://github\.com/ansible\-collections/community\.general/pull/10842)\)\.
* pipx module\_utils \- use <code>PIPX\_USE\_EMOJI</code> to disable emojis in the output of <code>pipx</code> 1\.8\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/10874](https\://github\.com/ansible\-collections/community\.general/pull/10874)\)\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_modify \- add <code>vrf</code> for <code>system logging action</code> with a default of <code>main</code> for RouterOS 7\.19 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/401](https\://github\.com/ansible\-collections/community\.routeros/pull/401)\)\.
* api\_modify\, api\_info \- field <code>instance</code> in <code>routing bgp connection</code> path is required\, and <code>router\-id</code> has been moved to <code>routing bgp instance</code> by RouterOS 7\.20 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/404](https\://github\.com/ansible\-collections/community\.routeros/pull/404)\)\.
* api\_modify\, api\_info \- support for field <code>new\-priority</code> in API path <code>ipv6 firewall mangle\`</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/402](https\://github\.com/ansible\-collections/community\.routeros/pull/402)\)\.

<a id="community-sap-libs"></a>
#### community\.sap\_libs

* collection \- Enhance <em class="title-reference">ansible\-test\`</em> CI action\, remove Python 2 and fix detected issues \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/60](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/60)\)
* collection \- Pipeline fixes and drop test support for ansible below 2\.13 \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/43](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/43)\)
* collection \- Update documentation and changelog for <em class="title-reference">1\.5\.0</em> release \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/61](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/61)\)
* collection \- Update workflow <em class="title-reference">ansible\-test</em> to include latest versions \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/54](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/54)\)
* sap\_control\_exec \- Remove unsupported functions \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/45](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/45)\)
* sap\_hdbsql \- add \-E option to filepath command \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/42](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/42)\)

<a id="community-sops"></a>
#### community\.sops

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.sops/pull/268](https\://github\.com/ansible\-collections/community\.sops/pull/268)\)\.

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_support\_assist \- Introduced aliases for the module parameters share\_username and share\_password to align with the naming conventions used across other modules\, ensuring consistency and improving usability\.

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added support for executing activemq\, lia\, mdm and tb roles on PowerFlex Gen2\.
* Added support for executing mdm\_cluster\, nvme\_host\, sdc\, sdt and snapshot\_policy modules on PowerFlex Gen2\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Supported new schemas in FortiManager 7\.0\.14\, 7\.2\.10\, 7\.2\.11\.

<a id="google-cloud"></a>
#### google\.cloud

* iap \- added scp\_if\_ssh option \([https\://github\.com/ansible\-collections/google\.cloud/pull/716](https\://github\.com/ansible\-collections/google\.cloud/pull/716)\)\.

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* server\_type\_info \- Return new Server Type <code>category</code> property\.
* server\_type\_info \- Return new Server Type <code>locations</code> property\.
* zone \- New module to manage DNS Zones in Hetzner Cloud\.
* zone\_info \- New module to fetch DNS Zones details\.
* zone\_rrset \- New module to manage DNS Zone RRSets in the Hetzner Cloud\.
* zone\_rrset\_info \- New module to fetch DNS RRSets details\.

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* purefa\_arrayname \- Added Fusion support
* purefa\_audits \- Added Fusion support
* purefa\_banner \- Added Fusion support
* purefa\_connect \- Added Fusion support
* purefa\_console \- Added Fusion support
* purefa\_directory \- Added Fusion support
* purefa\_dirsnap \- Added Fusion support
* purefa\_ds \- Added Fusion support
* purefa\_dsrole \- Added Fusion support
* purefa\_endpoint \- Added Fusion support
* purefa\_eradication \- Added Fusion support
* purefa\_export \- Added Fusion support
* purefa\_fs \- Added Fusion support
* purefa\_maintenance \- Timeout window updated
* purefa\_messages \- Added Fusion support
* purefa\_offload \- Added Fusion support
* purefa\_policy \- Added Fusion support
* purefa\_syslog\_settings \- Added Fusion support
* purefa\_timeout \- Added Fusion support

<a id="vmware-vmware"></a>
#### vmware\.vmware

* Add module for importing iso images to content library\.
* Remove six imports from \_facts\.py and \_vsphere\_tasks\.py due to new sanity rules\. Python 2 \(already not supported\) will fail to execute these files\.
* tag\_associations \- Add module to manage tag associations with objects
* tag\_categories \- Add module to manage tag categories
* tags \- Add module to manage tags
* vms \- Add option to inventory plugin to gather cluster and ESXi host name for VMs\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/215](https\://github\.com/ansible\-collections/vmware\.vmware/issues/215)\)

<a id="deprecated-features-1"></a>
### Deprecated Features

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* The device\, info\, protection\_domain\, snapshot\, storagepool and volume modules are supported only on PowerFlex Gen1\. They are replaced by v2 modules on PowerFlex Gen2\.
* The fault\_set\, replication\_consistency\_group\, replication\_pair\, resource\_group and sds modules are not supported on PowerFlex Gen2\.

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* server\_type\_info \- Deprecate Server Type <code>deprecation</code> property\.

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

<a id="ansible-core-7"></a>
#### Ansible\-core

* ansible\-galaxy \- remove support for resolvelib \>\= 0\.5\.3\, \< 0\.8\.0\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-8"></a>
#### Ansible\-core

* Fix issue where play tags prevented executing notified handlers \([https\://github\.com/ansible/ansible/issues/85475](https\://github\.com/ansible/ansible/issues/85475)\)
* Fix issues with keywords being incorrectly validated on <code>import\_tasks</code> \([https\://github\.com/ansible/ansible/issues/85855](https\://github\.com/ansible/ansible/issues/85855)\, [https\://github\.com/ansible/ansible/issues/85856](https\://github\.com/ansible/ansible/issues/85856)\)
* Fix traceback when trying to import non\-existing file via nested <code>import\_tasks</code> \([https\://github\.com/ansible/ansible/issues/69882](https\://github\.com/ansible/ansible/issues/69882)\)
* ansible\-doc \- prevent crash when scanning collections in paths that have more than one <code>ansible\_collections</code> in it \([https\://github\.com/ansible/ansible/issues/84909](https\://github\.com/ansible/ansible/issues/84909)\, [https\://github\.com/ansible/ansible/pull/85361](https\://github\.com/ansible/ansible/pull/85361)\)\.
* fetch \- also return <code>file</code> in the result when changed is <code>True</code> \([https\://github\.com/ansible/ansible/pull/85729](https\://github\.com/ansible/ansible/pull/85729)\)\.

<a id="amazon-aws"></a>
#### amazon\.aws

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2727](https\://github\.com/ansible\-collections/amazon\.aws/pull/2727)\)\.
* amazon\.aws\.autoscaling\_instance \- setting the state to <code>terminated</code> had no effect\. The fix implements missing instance termination state \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2719](https\://github\.com/ansible\-collections/amazon\.aws/issues/2719)\)\.
* ec2\_vpc\_nacl \- Fix issue when trying to update existing Network ACL rule \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2592](https\://github\.com/ansible\-collections/amazon\.aws/issues/2592)\)\.
* s3\_object \- Honor headers for content and content\_base64 uploads by promoting supported keys \(e\.g\. ContentType\, ContentDisposition\, CacheControl\) to top\-level S3 arguments and placing remaining keys under Metadata\. This makes content uploads consistent with src uploads\. \([https\://github\.com/ansible\-collections/amazon\.aws](https\://github\.com/ansible\-collections/amazon\.aws)\)

<a id="cisco-ios-2"></a>
#### cisco\.ios

* Fixed an issue where configuration within an address family \(ipv6\) was ignored by the parser\.
* cisco\.ios\.ios\_vrf\_global \- fixed issue preventing idempotent configuration of multiple import/export route\-targets for a VRF\.
* ios\_hsrp\_interfaces \- Device defaults version to 1 if standby\_groups is present but version is not configured\. and module would also consider priority as 100 if not configured\, to maintain idempotency\.
* ios\_hsrp\_interfaces \- Fixed operation for ipv6 standby configuration\.
* ios\_static\_routes \- Fix parsing of static routes with interface and distance in gathered state

<a id="cisco-meraki"></a>
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
* networks\_switch\_qos\_rules\_order\: extend object lookup to include srcPortRange and dstPortRange when matching existing QoS rules to improve idempotency

<a id="community-crypto"></a>
#### community\.crypto

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.crypto/pull/953](https\://github\.com/ansible\-collections/community\.crypto/pull/953)\)\.

<a id="community-dns-1"></a>
#### community\.dns

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.dns/pull/287](https\://github\.com/ansible\-collections/community\.dns/pull/287)\)\.
* Update Public Suffix List\.

<a id="community-docker-1"></a>
#### community\.docker

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.docker/pull/1117](https\://github\.com/ansible\-collections/community\.docker/pull/1117)\)\.
* Avoid remaining usages of deprecated <code>ansible\.module\_utils\.six</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1133](https\://github\.com/ansible\-collections/community\.docker/pull/1133)\)\.
* Avoid usage of deprecated <code>ansible\.module\_utils\.six</code> in all code that does not have to support Python 2 \([https\://github\.com/ansible\-collections/community\.docker/pull/1137](https\://github\.com/ansible\-collections/community\.docker/pull/1137)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1139](https\://github\.com/ansible\-collections/community\.docker/pull/1139)\)\.
* Avoid usage of deprecated <code>ansible\.module\_utils\.six</code> in some of the code that still supports Python 2 \([https\://github\.com/ansible\-collections/community\.docker/pull/1138](https\://github\.com/ansible\-collections/community\.docker/pull/1138)\)\.

<a id="community-general-1"></a>
#### community\.general

* Avoid usage of deprecated <code>ansible\.module\_utils\.six</code> in all code that does not have to support Python 2 \([https\://github\.com/ansible\-collections/community\.general/pull/10873](https\://github\.com/ansible\-collections/community\.general/pull/10873)\)\.
* gem \- fix soundness issue when uninstalling default gems on Ubuntu  \([https\://github\.com/ansible\-collections/community\.general/issues/10451](https\://github\.com/ansible\-collections/community\.general/issues/10451)\, [https\://github\.com/ansible\-collections/community\.general/pull/10689](https\://github\.com/ansible\-collections/community\.general/pull/10689)\)\.
* github\_app\_access\_token lookup plugin \- fix compatibility imports for using jwt \([https\://github\.com/ansible\-collections/community\.general/issues/10807](https\://github\.com/ansible\-collections/community\.general/issues/10807)\, [https\://github\.com/ansible\-collections/community\.general/pull/10810](https\://github\.com/ansible\-collections/community\.general/pull/10810)\)\.
* github\_deploy\_key \- fix bug during error handling if no body was present in the result \([https\://github\.com/ansible\-collections/community\.general/issues/10853](https\://github\.com/ansible\-collections/community\.general/issues/10853)\, [https\://github\.com/ansible\-collections/community\.general/pull/10857](https\://github\.com/ansible\-collections/community\.general/pull/10857)\)\.
* homebrew \- do not fail when cask or formula name has changed in homebrew repo \([https\://github\.com/ansible\-collections/community\.general/issues/10804](https\://github\.com/ansible\-collections/community\.general/issues/10804)\, [https\://github\.com/ansible\-collections/community\.general/pull/10805](https\://github\.com/ansible\-collections/community\.general/pull/10805)\)\.
* keycloak\_group \- fixes an issue where module ignores realm when searching subgroups by name \([https\://github\.com/ansible\-collections/community\.general/pull/10840](https\://github\.com/ansible\-collections/community\.general/pull/10840)\)\.
* keycloak\_role \- fixes an issue where the module incorrectly returns <code>changed\=true</code> when using the alias <code>clientId</code> in composite roles \([https\://github\.com/ansible\-collections/community\.general/pull/10829](https\://github\.com/ansible\-collections/community\.general/pull/10829)\)\.
* parted \- variable is a list\, not text \([https\://github\.com/ansible\-collections/community\.general/pull/10823](https\://github\.com/ansible\-collections/community\.general/pull/10823)\, [https\://github\.com/ansible\-collections/community\.general/issues/10817](https\://github\.com/ansible\-collections/community\.general/issues/10817)\)\.
* rocketchat \- fix message delivery in Rocket Chat \>\= 7\.5\.3 by forcing <code>Content\-Type</code> header to <code>application/json</code> instead of the default <code>application/x\-www\-form\-urlencoded</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10796](https\://github\.com/ansible\-collections/community\.general/issues/10796)\, [https\://github\.com/ansible\-collections/community\.general/pull/10796](https\://github\.com/ansible\-collections/community\.general/pull/10796)\)\.
* yaml cache plugin \- make compatible with ansible\-core 2\.19 \([https\://github\.com/ansible\-collections/community\.general/issues/10849](https\://github\.com/ansible\-collections/community\.general/issues/10849)\, [https\://github\.com/ansible\-collections/community\.general/issues/10852](https\://github\.com/ansible\-collections/community\.general/issues/10852)\)\.

<a id="community-hrobot-2"></a>
#### community\.hrobot

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/174](https\://github\.com/ansible\-collections/community\.hrobot/pull/174)\)\.
* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/177](https\://github\.com/ansible\-collections/community\.hrobot/pull/177)\)\.

<a id="community-library-inventory-filtering-v1"></a>
#### community\.library\_inventory\_filtering\_v1

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/38](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/38)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/40](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/40)\)\.
* Stop using <code>ansible\.module\_utils\.six</code> to avoid user\-facing deprecation messages with ansible\-core 2\.20\, while still supporting older ansible\-core versions \([https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/39](https\://github\.com/ansible\-collections/community\.library\_inventory\_filtering/pull/39)\)\.

<a id="community-routeros-1"></a>
#### community\.routeros

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/405](https\://github\.com/ansible\-collections/community\.routeros/pull/405)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.routeros/pull/406](https\://github\.com/ansible\-collections/community\.routeros/pull/406)\)\.

<a id="community-sops-1"></a>
#### community\.sops

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.sops/pull/268](https\://github\.com/ansible\-collections/community\.sops/pull/268)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.sops/pull/269](https\://github\.com/ansible\-collections/community\.sops/pull/269)\)\.

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* Fixed the UT test execution through ansible\-test \- \(Issue 1003\) \- Tests Pass Using Tox But Not Ansible\-Test \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules)\)
* idrac\_support\_assist \- Updated module playbook examples to use the correct casing for protocol names\, for CIFS and HTTPS\.
* idrac\_system\_info \- \(Issue 1017\) \- System info not being returned on gen17s with v10\.0\.0 \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1017](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1017)\)
* redfish\_storage\_volume \- \(Issue 1027\) Module fails on force reboot\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1027](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1027)\)

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Changed the logic of getting FortiManager system information to prevent permission denied error\.
* Supported module\_defaults\. General variables can be specified in one place by using module\_defaults\.

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fix the issue in check\_modu when backend returns invallid IP address\.
* Fix the issue in configuration\_fact and monitor\_fact when omitting vdom or assigning vdom to \"\"\.

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* floating\_ip \- Wait for the Floating IP assign action to complete to reduce chances of running into <code>locked</code> errors\.
* server \- Also check server type deprecation after server creation\.

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_eradication \- Idempotency fix
* purefa\_info \- Fixed AttributeError for hgroups subset
* purefa\_pg \- Fixed AttributeError adding target to PG

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* Drop incorrect requirement on aiohttp \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/230](https\://github\.com/ansible\-collections/vmware\.vmware/pull/230)\)\.
* cluster\_ha \- Fix admission control policy not being updated when ac is disabled
* content\_template \- Fix typo in code for check mode that tried to access a module param which doesn\'t exist\.
* import\_content\_library\_ovf \- Fix large file import by using requests instead of open\_url\. Requests allows for streaming uploads\, instead of reading the entire file into memory\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/220](https\://github\.com/ansible\-collections/vmware\.vmware/issues/220)\)
* vm\_powerstate \- Ensure timeout option also applies to the shutdown\-guest state

<a id="known-issues"></a>
### Known Issues

<a id="dellemc-openmanage-3"></a>
#### dellemc\.openmanage

* Formal qualification of module ome\_smart\_fabric\_info for Ansible Core version 2\.19 is still pending\.
* idrac\_diagnostics \- This module does not support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_license \- Due to API limitation\, proxy parameters are ignored during the import operation\.
* idrac\_license \- The module will give different error messages for iDRAC9 and iDRAC10 when user imports license with invalid share name\.
* idrac\_os\_deployment \- The module continues to return a 200 response and marks the job as completed\, even when an outdated date is supplied in the Expose duration\.
* idrac\_redfish\_storage\_controller \- PatrolReadRatePercent attribute cannot be set in iDRAC10\.
* idrac\_server\_config\_profile \- When attempting to revert iDRAC settings using a previously exported SCP file\, the import operation will complete with errors if a new user was created after the export \(Instead of restoring the system to its previous state\, including the removal of newly added users\)\.
* idrac\_system\_info \- The module will show empty video list despite having Embedded VIDEO controller\.
* ome\_smart\_fabric\_uplink \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.
* redfish\_storage\_volume \- Encryption type and block\_io\_size bytes will be read only property in iDRAC9 and iDRAC10 and hence the module ignores these parameters\.

<a id="new-modules-1"></a>
### New Modules

<a id="dellemc-powerflex-2"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.device\_v2 \- Manage device on Dell PowerFlex Gen2
* dellemc\.powerflex\.info\_v2 \- Gathering information about Dell PowerFlex Gen2
* dellemc\.powerflex\.protection\_domain\_v2 \- Manage Protection Domain on Dell PowerFlex Gen2
* dellemc\.powerflex\.snapshot\_v2 \- Manage Snapshots on Dell PowerFlex Gen2
* dellemc\.powerflex\.storagepool\_v2 \- Managing Dell PowerFlex storage pool Gen2
* dellemc\.powerflex\.volume\_v2 \- Manage volumes on Dell PowerFlex Gen2

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* ansible\.netcommon \(still version 8\.1\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.0\)
* ansible\.windows \(still version 3\.2\.0\)
* arista\.eos \(still version 12\.0\.0\)
* awx\.awx \(still version 24\.6\.1\)
* check\_point\.mgmt \(still version 6\.5\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.3\)
* cisco\.aci \(still version 2\.12\.0\)
* cisco\.dnac \(still version 6\.40\.0\)
* cisco\.iosxr \(still version 12\.0\.0\)
* cisco\.mso \(still version 2\.11\.0\)
* cisco\.nxos \(still version 11\.0\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.2\)
* community\.aws \(still version 10\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.digitalocean \(still version 1\.27\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.0\.0\)
* community\.libvirt \(still version 2\.0\.0\)
* community\.mongodb \(still version 1\.7\.10\)
* community\.mysql \(still version 4\.0\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.1\.0\)
* community\.proxmox \(still version 1\.3\.0\)
* community\.proxysql \(still version 1\.6\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.vmware \(still version 6\.0\.0\)
* community\.windows \(still version 3\.0\.1\)
* community\.zabbix \(still version 4\.1\.1\)
* containers\.podman \(still version 1\.18\.0\)
* cyberark\.conjur \(still version 1\.3\.7\)
* cyberark\.pas \(still version 1\.0\.35\)
* dellemc\.enterprise\_sonic \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* ibm\.storage\_virtualize \(still version 3\.0\.0\)
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
* purestorage\.flashblade \(still version 1\.21\.2\)
* ravendb\.ravendb \(still version 1\.0\.3\)
* splunk\.es \(still version 4\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.4\.0\)
* theforeman\.foreman \(still version 5\.6\.0\)
* vmware\.vmware\_rest \(still version 4\.9\.0\)
* vultr\.cloud \(still version 1\.13\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.10\)

<a id="v13-0-0a1"></a>
## v13\.0\.0a1

- <a href="#release-summary-3">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections-1">Added Collections</a>
- <a href="#ansible-core-9">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-openmanage-4">dellemc\.openmanage</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#hitachivantara-vspone-block-2">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-3">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#ibm-storage-virtualize-4">ibm\.storage\_virtualize</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#ansible-core-13">Ansible\-core</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#purestorage-flasharray-3">purestorage\.flasharray</a>
- <a href="#removed-features-previously-deprecated-1">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-14">Ansible\-core</a>
    - <a href="#community-vmware-4">community\.vmware</a>
- <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#ansible-core-15">Ansible\-core</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#community-vmware-5">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#dellemc-openmanage-5">dellemc\.openmanage</a>
    - <a href="#google-cloud-2">google\.cloud</a>
    - <a href="#ibm-storage-virtualize-5">ibm\.storage\_virtualize</a>
    - <a href="#purestorage-flasharray-4">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
- <a href="#known-issues-1">Known Issues</a>
    - <a href="#ansible-core-16">Ansible\-core</a>
    - <a href="#dellemc-openmanage-6">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#filter">Filter</a>
    - <a href="#inventory">Inventory</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#hitachivantara-vspone-block-3">hitachivantara\.vspone\_block</a>
- <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="release-summary-3"></a>
### Release Summary

Release Date\: 2025\-09\-24

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* ibm\.qradar \(previously included version\: 4\.0\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections-1"></a>
### Added Collections

* ravendb\.ravendb \(version 1\.0\.3\)

<a id="ansible-core-9"></a>
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

<a id="major-changes-2"></a>
### Major Changes

<a id="ansible-core-10"></a>
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

<a id="dellemc-openmanage-4"></a>
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

<a id="minor-changes-2"></a>
### Minor Changes

<a id="ansible-core-11"></a>
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
* ansible\-test \- Update base/default containers to include Python 3\.14\.0\.
* ansible\-test \- Update pinned sanity test requirements\.
* ansible\-test \- Update test containers\.
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

<a id="community-general-2"></a>
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

<a id="community-mysql-1"></a>
#### community\.mysql

* <em class="title-reference">mysql\_query</em> \- add new <em class="title-reference">session\_vars</em> argument\, similar to ansible\-collections/community\.mysql\#489\.

<a id="community-routeros-2"></a>
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

<a id="google-cloud-1"></a>
#### google\.cloud

* iap \- enable use of Identity Aware Proxy ssh connections to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/709](https\://github\.com/ansible\-collections/google\.cloud/pull/709)\)\.

<a id="hitachivantara-vspone-block-2"></a>
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

<a id="ibm-storage-virtualize-3"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_flashsystem\_grid \- Added support for new FlashSystem grid APIs
* ibm\_sv\_manage\_storage\_partition \- Added support for management portset and renaming partition
* ibm\_sv\_manage\_truststore\_for\_replication \- Added support for new FlashSystem grid APIs
* ibm\_svc\_hostcluster \- Added support for partition and for managing host mappings during hostcluster deletion
* ibm\_svc\_info \- Added support for new FlashSystem grid APIs
* ibm\_svc\_manage\_ip \- Changes for management portset
* ibm\_svc\_manage\_portset \- Added support for management portset
* ibm\_svc\_manage\_volume \- Added support for HA volumes volume expansion\, volumegroup\, volume rename and grainsize

<a id="purestorage-flasharray-2"></a>
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

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purefb\_ad \- Revert removal of <code>service</code> parameter \(breaking change\)\. Added more logic to use of <code>service</code> parameter and recommend use of <code>service\_principals</code> with service incorporated\.
* purefb\_ad \- <code>service</code> parameter removed to comply with underlying API structure\. <code>service</code> should be included in the <code>service\_principals</code> strings as shown in the documentation\.
* purefb\_saml \- Added <code>entity\_id</code> parameter
* purefb\_snap \- Add support to delete/eradicate remote snapshots\, including the latest replica
* purefb\_user \- All AD users to have SSH keys and/or API tokens assigned\, even if they have never accessed the FlashArray before\. AD users must have <code>ad\_user</code> set as <code>true</code>\.

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* content\_upload \- fall\-back to rpm binary when library can\'t be imported
* registration\_command \- clarify example to show where the generated command needs to be executed

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-12"></a>
#### Ansible\-core

* powershell \- Removed code that tried to remote quotes from paths when performing Windows operations like copying and fetching file\. This should not affect normal playbooks unless a value is quoted too many times\.

<a id="community-mysql-2"></a>
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

<a id="ibm-storage-virtualize-4"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_flashsystem\_grid \- The flashsystem grid module now uses newer FlashSystem REST APIs to perform tasks\.

<a id="deprecated-features-2"></a>
### Deprecated Features

<a id="ansible-core-13"></a>
#### Ansible\-core

* Deprecated the shell plugin\'s <code>wrap\_for\_exec</code> function\. This API is not used in Ansible or any known collection and is being removed to simplify the plugin API\. Plugin authors should wrap their command to execute within an explicit shell or other known executable\.
* INJECT\_FACTS\_AS\_VARS configuration currently defaults to <code>True</code>\, this is now deprecated and it will switch to <code>False</code> by Ansible 2\.24\. You will only get notified if you are accessing \'injected\' facts \(for example\, ansible\_os\_distribution vs ansible\_facts\[\'os\_distribution\'\]\)\.
* hash\_params function in roles/\_\_init\_\_ is being deprecated as it is not in use\.
* include\_vars \- Specifying \'ignore\_files\' as a string is deprecated\.
* vars\, the internal variable cache will be removed in 2\.24\. This cache\, once used internally exposes variables in inconsistent states\, the \'vars\' and \'varnames\' lookups should be used instead\.

<a id="community-general-3"></a>
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

<a id="purestorage-flasharray-3"></a>
#### purestorage\.flasharray

* purefa\_volume\_tags \- Deprecated due to removal of REST 1\.x support\. Will be removed in Collection 2\.0\.0

<a id="removed-features-previously-deprecated-1"></a>
### Removed Features \(previously deprecated\)

* The deprecated <code>ibm\.qradar</code> collection has been removed \([https\://forum\.ansible\.com/t/44259](https\://forum\.ansible\.com/t/44259)\)\.

<a id="ansible-core-14"></a>
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

<a id="bugfixes-3"></a>
### Bugfixes

<a id="ansible-core-15"></a>
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

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* cisco\.meraki\.devices\_appliance\_uplinks\_settings \- fix idempotency error\.

<a id="community-dns-2"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-4"></a>
#### community\.general

* kdeconfig \- <code>kwriteconfig</code> executable could not be discovered automatically on systems with only <code>kwriteconfig6</code> installed\. <code>kwriteconfig6</code> can now be discovered by Ansible \([https\://github\.com/ansible\-collections/community\.general/issues/10746](https\://github\.com/ansible\-collections/community\.general/issues/10746)\, [https\://github\.com/ansible\-collections/community\.general/pull/10751](https\://github\.com/ansible\-collections/community\.general/pull/10751)\)\.
* monit \- fix crash caused by an unknown status value returned from the monit service \([https\://github\.com/ansible\-collections/community\.general/issues/10742](https\://github\.com/ansible\-collections/community\.general/issues/10742)\, [https\://github\.com/ansible\-collections/community\.general/pull/10743](https\://github\.com/ansible\-collections/community\.general/pull/10743)\)\.
* pacemaker \- use regex for matching <code>maintenance\-mode</code> output to determine cluster maintenance status \([https\://github\.com/ansible\-collections/community\.general/issues/10426](https\://github\.com/ansible\-collections/community\.general/issues/10426)\, [https\://github\.com/ansible\-collections/community\.general/pull/10707](https\://github\.com/ansible\-collections/community\.general/pull/10707)\)\.
* selective callback plugin \- specify <code>ansible\_loop\_var</code> instead of the explicit value <code>item</code> when printing task result \([https\://github\.com/ansible\-collections/community\.general/pull/10752](https\://github\.com/ansible\-collections/community\.general/pull/10752)\)\.

<a id="community-routeros-3"></a>
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

<a id="dellemc-openmanage-5"></a>
#### dellemc\.openmanage

* idrac\_server\_config\_profile \- \(Issue 959\) Can\'t export SCP \(Server configuration profile\) on iDRAC 10\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959)\)
* idrac\_system\_info \- \(Issue 967\) \- idrac\_system\_info fails on iDRAC10 with GPU\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967)\)

<a id="google-cloud-2"></a>
#### google\.cloud

* gcp\_compute\_instance \- add suppport for attaching disks to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/711](https\://github\.com/ansible\-collections/google\.cloud/pull/711)\)\.
* gcp\_secret\_manager \- use service\_account\_contents instead of service\_account\_info \([https\://github\.com/ansible\-collections/google\.cloud/pull/703](https\://github\.com/ansible\-collections/google\.cloud/pull/703)\)\.

<a id="ibm-storage-virtualize-5"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_mdiskgrp \- Removed mandatory system mask setting during pool\-linking

<a id="purestorage-flasharray-4"></a>
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

<a id="purestorage-flashblade-3"></a>
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

<a id="known-issues-1"></a>
### Known Issues

<a id="ansible-core-16"></a>
#### Ansible\-core

* templating \- Exceptions raised in a Jinja <code>set</code> or <code>with</code> block which are not accessed by the template are ignored in the same manner as undefined values\.
* templating \- Passing a container created in a Jinja <code>set</code> or <code>with</code> block to a method results in a copy of that container\. Mutations to that container which are not returned by the method will be discarded\.

<a id="dellemc-openmanage-6"></a>
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

<a id="new-modules-2"></a>
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

<a id="community-general-5"></a>
#### community\.general

* community\.general\.django\_dumpdata \- Wrapper for C\(django\-admin dumpdata\)\.
* community\.general\.django\_loaddata \- Wrapper for C\(django\-admin loaddata\)\.
* community\.general\.pacemaker\_stonith \- Manage Pacemaker STONITH\.

<a id="containers-podman-3"></a>
#### containers\.podman

* containers\.podman\.podman\_system\_connection \- Manage Podman system connections
* containers\.podman\.podman\_system\_connection\_info \- Get info about Podman system connections

<a id="hitachivantara-vspone-block-3"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block-1"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_capacity\_management\_settings\_facts \- Get capacity management settings from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_drive \- Manages drive on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_controller \- Edits the settings for the storage controller on Hitachi SDS Block storage systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_node\_bmc\_connection\_facts \- Get storage node BMC access settings from storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_pool\_estimated\_capacity\_facts \- Obtains the preliminary calculation results of the storage pool logical capacity \(unit TiB\)\.

<a id="vsp-1"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_vsp\_one\_volume \- Manages volumes on Hitachi VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_volume\_facts \- Retrieves facts about Hitachi VSP One storage system volumes\.

<a id="unchanged-collections-3"></a>
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
