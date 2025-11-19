# Ansible 13 Release Notes

This changelog describes changes since Ansible 12\.0\.0\.

- <a href="#v13-0-0">v13\.0\.0</a>
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
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>

<a id="v13-0-0"></a>
## v13\.0\.0

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
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
    - <a href="#ieisystem-inmanage">ieisystem\.inmanage</a>
    - <a href="#ngine-io-cloudstack">ngine\_io\.cloudstack</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-hashi-vault">community\.hashi\_vault</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-proxmox">community\.proxmox</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-hrobot-1">community\.hrobot</a>
    - <a href="#community-vmware-3">community\.vmware</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-vmware-4">community\.vmware</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#community-general-4">community\.general</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#community-hrobot-2">community\.hrobot</a>
    - <a href="#community-library-inventory-filtering-v1">community\.library\_inventory\_filtering\_v1</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-proxmox-1">community\.proxmox</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-vmware-5">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#ieisystem-inmanage-1">ieisystem\.inmanage</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#ngine-io-cloudstack-1">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#community-sops-2">community\.sops</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#callback">Callback</a>
    - <a href="#filter">Filter</a>
    - <a href="#inventory">Inventory</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#community-proxmox-2">community\.proxmox</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-powerflex-2">dellemc\.powerflex</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-3">ibm\.storage\_virtualize</a>
    - <a href="#ieisystem-inmanage-2">ieisystem\.inmanage</a>
    - <a href="#ngine-io-cloudstack-2">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2025\-11\-19

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* community\.digitalocean \(previously included version\: 1\.27\.0\)
* ibm\.qradar \(previously included version\: 4\.0\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections"></a>
### Added Collections

* hitachivantara\.vspone\_object \(version 1\.0\.0\)
* ravendb\.ravendb \(version 1\.0\.4\)

<a id="ansible-core"></a>
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
* Replace <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/community\.vmware/issues/2497](https\://github\.com/ansible\-collections/community\.vmware/issues/2497)\)\.
* Replace <code>ansible\.module\_utils\.common\.\_collections\_compat</code> \([https\://github\.com/ansible\-collections/community\.vmware/issues/2497](https\://github\.com/ansible\-collections/community\.vmware/issues/2497)\)\.
* Replace <code>ansible\.module\_utils\.six</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2495](https\://github\.com/ansible\-collections/community\.vmware/pull/2495)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* Add inventory plugins for buildah and podman
* Add podman system connection modules

<a id="dellemc-openmanage"></a>
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

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Supported default\_group feature for the all of the modules\.
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

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-2"></a>
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

<a id="cisco-dnac"></a>
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

<a id="cisco-ios"></a>
#### cisco\.ios

* ios\_config \- added answering prompt functionality while working in config mode on ios device
* ios\_facts \- Add chassis\_id value to ansible\_net\_neighbors dictionary for lldp neighbours\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* Added few parameters to iosxr\_l3\_interface module to support new features\.

<a id="community-dns"></a>
#### community\.dns

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.dns/pull/287](https\://github\.com/ansible\-collections/community\.dns/pull/287)\)\.
* lookup\_\* plugins \- support <code>type\=HTTPS</code> and <code>type\=SVCB</code> \([https\://github\.com/ansible\-collections/community\.dns/issues/299](https\://github\.com/ansible\-collections/community\.dns/issues/299)\, [https\://github\.com/ansible\-collections/community\.dns/pull/300](https\://github\.com/ansible\-collections/community\.dns/pull/300)\)\.
* nameserver\_record\_info \- support <code>type\=HTTPS</code> and <code>type\=SVCB</code> \([https\://github\.com/ansible\-collections/community\.dns/issues/299](https\://github\.com/ansible\-collections/community\.dns/issues/299)\, [https\://github\.com/ansible\-collections/community\.dns/pull/300](https\://github\.com/ansible\-collections/community\.dns/pull/300)\)\.
* nameserver\_record\_info \- the return value <code>results\[\]\.result\[\]\.values</code> has been renamed to <code>results\[\]\.result\[\]\.entries</code>\. The old name will still be available for a longer time \([https\://github\.com/ansible\-collections/community\.dns/issues/289](https\://github\.com/ansible\-collections/community\.dns/issues/289)\, [https\://github\.com/ansible\-collections/community\.dns/pull/298](https\://github\.com/ansible\-collections/community\.dns/pull/298)\)\.
* wait\_for\_txt \- the option <code>records\[\]\.values</code> now has an alias <code>records\[\]\.entries</code> \([https\://github\.com/ansible\-collections/community\.dns/pull/298](https\://github\.com/ansible\-collections/community\.dns/pull/298)\)\.
* wait\_for\_txt \- the return value <code>records\[\]\.values</code> has been renamed to <code>records\[\]\.entries</code>\. The old name will still be available for a longer time \([https\://github\.com/ansible\-collections/community\.dns/issues/289](https\://github\.com/ansible\-collections/community\.dns/issues/289)\, [https\://github\.com/ansible\-collections/community\.dns/pull/298](https\://github\.com/ansible\-collections/community\.dns/pull/298)\)\.

<a id="community-docker"></a>
#### community\.docker

* Note that some new code in <code>plugins/module\_utils/\_six\.py</code> is MIT licensed \([https\://github\.com/ansible\-collections/community\.docker/pull/1138](https\://github\.com/ansible\-collections/community\.docker/pull/1138)\)\.
* docker\_container \- add <code>driver\_opts</code> option in <code>networks</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1142](https\://github\.com/ansible\-collections/community\.docker/issues/1142)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1143](https\://github\.com/ansible\-collections/community\.docker/pull/1143)\)\.
* docker\_container \- add <code>gw\_priority</code> option in <code>networks</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1142](https\://github\.com/ansible\-collections/community\.docker/issues/1142)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1143](https\://github\.com/ansible\-collections/community\.docker/pull/1143)\)\.
* docker\_container \- support missing fields and new mount types in <code>mounts</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/1129](https\://github\.com/ansible\-collections/community\.docker/issues/1129)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1134](https\://github\.com/ansible\-collections/community\.docker/pull/1134)\)\.

<a id="community-general"></a>
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

<a id="community-hrobot"></a>
#### community\.hrobot

* storagebox\_subaccount \- filter by username when looking for existing accounts by username \([https\://github\.com/ansible\-collections/community\.hrobot/pull/182](https\://github\.com/ansible\-collections/community\.hrobot/pull/182)\)\.
* storagebox\_subaccount \- use the new <code>change\_home\_directory</code> action to update a subaccount\'s home directory\, instead of using the now deprecated way using the <code>update\_access\_settings</code> action \([https\://github\.com/ansible\-collections/community\.hrobot/pull/181](https\://github\.com/ansible\-collections/community\.hrobot/pull/181)\)\.

<a id="community-mysql"></a>
#### community\.mysql

* <em class="title-reference">mysql\_query</em> \- add new <em class="title-reference">session\_vars</em> argument\, similar to ansible\-collections/community\.mysql\#489\.

<a id="community-proxmox"></a>
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

<a id="community-routeros"></a>
#### community\.routeros

* api\_find\_and\_modify\, api\_modify \- instead of comparing supplied values as\-is to values retrieved from the API and converted to some types \(int\, bool\) by librouteros\, instead compare values by converting them to strings first\, using similar conversion rules that librouteros uses \([https\://github\.com/ansible\-collections/community\.routeros/issues/389](https\://github\.com/ansible\-collections/community\.routeros/issues/389)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/370](https\://github\.com/ansible\-collections/community\.routeros/issues/370)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/325](https\://github\.com/ansible\-collections/community\.routeros/issues/325)\, [https\://github\.com/ansible\-collections/community\.routeros/issues/169](https\://github\.com/ansible\-collections/community\.routeros/issues/169)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/397](https\://github\.com/ansible\-collections/community\.routeros/pull/397)\)\.
* api\_modify \- add <code>vrf</code> for <code>snmp</code> with a default of <code>main</code> for RouterOS 7\.3 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/411](https\://github\.com/ansible\-collections/community\.routeros/pull/411)\)\.
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

<a id="community-vmware-1"></a>
#### community\.vmware

* vcenter\_license \- Add support for VCF license keys\. \([https\://github\.com/ansible\-collections/community\.vmware/pull/2451](https\://github\.com/ansible\-collections/community\.vmware/pull/2451)\)
* vmware\_dvs\_portgroup \- add <code>portgroup\_description</code> parameter \([https\://github\.com/ansible\-collections/community\.vmware/issues/2487](https\://github\.com/ansible\-collections/community\.vmware/issues/2487)\)\.
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
* iap \- enable use of Identity Aware Proxy ssh connections to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/709](https\://github\.com/ansible\-collections/google\.cloud/pull/709)\)\.

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* server\_type\_info \- Return new Server Type <code>category</code> property\.
* server\_type\_info \- Return new Server Type <code>locations</code> property\.
* zone \- New module to manage DNS Zones in Hetzner Cloud\.
* zone\_info \- New module to fetch DNS Zones details\.
* zone\_rrset \- New module to manage DNS Zone RRSets in the Hetzner Cloud\.
* zone\_rrset\_info \- New module to fetch DNS RRSets details\.

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

<a id="ibm-storage-virtualize"></a>
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

<a id="kubernetes-core"></a>
#### kubernetes\.core

* Add support of skip\-schema\-validation in <code>helm</code> module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/995](https\://github\.com/ansible\-collections/kubernetes\.core/pull/995)\)
* kustomize \- Add support of local environ \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/786](https\://github\.com/ansible\-collections/kubernetes\.core/pull/786)\)\.

<a id="netapp-ontap"></a>
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

<a id="purestorage-flasharray"></a>
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

<a id="purestorage-flashblade"></a>
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

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* content\_upload \- fall\-back to rpm binary when library can\'t be imported
* registration\_command \- clarify example to show where the generated command needs to be executed

<a id="vmware-vmware"></a>
#### vmware\.vmware

* Add module for importing iso images to content library\.
* Remove six imports from \_facts\.py and \_vsphere\_tasks\.py due to new sanity rules\. Python 2 \(already not supported\) will fail to execute these files\.
* tag\_associations \- Add module to manage tag associations with objects
* tag\_categories \- Add module to manage tag categories
* tags \- Add module to manage tags
* vms \- Add option to inventory plugin to gather cluster and ESXi host name for VMs\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/215](https\://github\.com/ansible\-collections/vmware\.vmware/issues/215)\)

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-3"></a>
#### Ansible\-core

* powershell \- Removed code that tried to remote quotes from paths when performing Windows operations like copying and fetching file\. This should not affect normal playbooks unless a value is quoted too many times\.

<a id="community-docker-1"></a>
#### community\.docker

* All doc fragments\, module utils\, and plugin utils are from now on private\. They can change at any time\, and have breaking changes even in bugfix releases \([https\://github\.com/ansible\-collections/community\.docker/pull/1144](https\://github\.com/ansible\-collections/community\.docker/pull/1144)\)\.

<a id="community-general-1"></a>
#### community\.general

* mh\.base module utils \- <code>debug</code> will now always be delegated to the underlying <code>AnsibleModule</code> object \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.
* oneview module utils \- remove import of standard library <code>os</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10644](https\://github\.com/ansible\-collections/community\.general/pull/10644)\)\.
* slack \- the default of <code>prepend\_hash</code> changed from <code>auto</code> to <code>never</code> \([https\://github\.com/ansible\-collections/community\.general/pull/10883](https\://github\.com/ansible\-collections/community\.general/pull/10883)\)\.

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

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* Drop support for Python 3\.9
* Drop support for ansible\-core 2\.17

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

<a id="community-general-2"></a>
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

<a id="community-hrobot-1"></a>
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

<a id="community-vmware-3"></a>
#### community\.vmware

* vmware\_guest\_snapshot \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2467](https\://github\.com/ansible\-collections/community\.vmware/pull/2467)\)\.

<a id="community-zabbix-1"></a>
#### community\.zabbix

* zabbix\_maintenance module \- Depreicated <em class="title-reference">minutes</em> argument for <em class="title-reference">time\_periods</em>

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* The device\, info\, protection\_domain\, snapshot\, storagepool and volume modules are supported only on PowerFlex Gen1\. They are replaced by v2 modules on PowerFlex Gen2\.
* The fault\_set\, replication\_consistency\_group\, replication\_pair\, resource\_group and sds modules are not supported on PowerFlex Gen2\.

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* server\_type\_info \- Deprecate Server Type <code>deprecation</code> property\.

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_volume\_tags \- Deprecated due to removal of REST 1\.x support\. Will be removed in Collection 2\.0\.0

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The deprecated <code>community\.digitalocean</code> collection has been removed \([https\://forum\.ansible\.com/t/44602](https\://forum\.ansible\.com/t/44602)\)\.
* The deprecated <code>ibm\.qradar</code> collection has been removed \([https\://forum\.ansible\.com/t/44259](https\://forum\.ansible\.com/t/44259)\)\.

<a id="ansible-core-5"></a>
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

<a id="community-docker-2"></a>
#### community\.docker

* Remove support for Docker SDK for Python version 1\.x\.y\, also known as <code>docker\-py</code>\. Modules and plugins that use Docker SDK for Python require version 2\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.docker/pull/1171](https\://github\.com/ansible\-collections/community\.docker/pull/1171)\)\.
* The collection no longer supports Python 3\.6 and before\. Note that this coincides with the Python requirements of ansible\-core 2\.17\+ \([https\://github\.com/ansible\-collections/community\.docker/pull/1123](https\://github\.com/ansible\-collections/community\.docker/pull/1123)\)\.
* The collection no longer supports ansible\-core 2\.15 and 2\.16\. You need ansible\-core 2\.17\.0 or newer to use community\.docker 5\.x\.y \([https\://github\.com/ansible\-collections/community\.docker/pull/1123](https\://github\.com/ansible\-collections/community\.docker/pull/1123)\)\.

<a id="community-general-3"></a>
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

<a id="community-vmware-4"></a>
#### community\.vmware

* vmware\_cluster \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_dpm \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_dpm</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_drs \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_drs</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_drs\_recommendations \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_drs\_recommendations</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.
* vmware\_cluster\_vcls \- The deprecated module has been removed\. Use <code>vmware\.vmware\.cluster\_vcls</code> instead \([https\://github\.com/ansible\-collections/community\.vmware/pull/2455](https\://github\.com/ansible\-collections/community\.vmware/pull/2455)\)\.

<a id="security-fixes"></a>
### Security Fixes

<a id="community-general-4"></a>
#### community\.general

* keycloak\_user \- the parameter <code>credentials\[\]\.value</code> is now marked as <code>no\_log\=true</code>\. Before it was logged by Ansible\, unless the task was marked as <code>no\_log\: true</code>\. Since this parameter can be used for passwords\, this resulted in credential leaking \([https\://github\.com/ansible\-collections/community\.general/issues/11000](https\://github\.com/ansible\-collections/community\.general/issues/11000)\, [https\://github\.com/ansible\-collections/community\.general/pull/11005](https\://github\.com/ansible\-collections/community\.general/pull/11005)\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-6"></a>
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

<a id="amazon-aws"></a>
#### amazon\.aws

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2727](https\://github\.com/ansible\-collections/amazon\.aws/pull/2727)\)\.
* amazon\.aws\.autoscaling\_instance \- setting the state to <code>terminated</code> had no effect\. The fix implements missing instance termination state \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2719](https\://github\.com/ansible\-collections/amazon\.aws/issues/2719)\)\.
* ec2\_vpc\_nacl \- Fix issue when trying to update existing Network ACL rule \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2592](https\://github\.com/ansible\-collections/amazon\.aws/issues/2592)\)\.
* s3\_object \- Honor headers for content and content\_base64 uploads by promoting supported keys \(e\.g\. ContentType\, ContentDisposition\, CacheControl\) to top\-level S3 arguments and placing remaining keys under Metadata\. This makes content uploads consistent with src uploads\. \([https\://github\.com/ansible\-collections/amazon\.aws](https\://github\.com/ansible\-collections/amazon\.aws)\)

<a id="cisco-ios-1"></a>
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
* cisco\.meraki\.devices\_appliance\_uplinks\_settings \- fix idempotency error\.
* networks\_switch\_qos\_rules\_order\: extend object lookup to include srcPortRange and dstPortRange when matching existing QoS rules to improve idempotency

<a id="community-crypto"></a>
#### community\.crypto

* Avoid deprecated functionality in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.crypto/pull/953](https\://github\.com/ansible\-collections/community\.crypto/pull/953)\)\.
* Smaller code cleanup \([https\://github\.com/ansible\-collections/community\.crypto/pull/963](https\://github\.com/ansible\-collections/community\.crypto/pull/963)\)\.

<a id="community-dns-1"></a>
#### community\.dns

* Avoid using <code>ansible\.module\_utils\.six</code> in more places to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.dns/pull/291](https\://github\.com/ansible\-collections/community\.dns/pull/291)\)\.
* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.dns/pull/287](https\://github\.com/ansible\-collections/community\.dns/pull/287)\)\.
* Update Public Suffix List\.

<a id="community-docker-3"></a>
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

<a id="community-general-5"></a>
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

<a id="community-hrobot-2"></a>
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

<a id="community-mysql-2"></a>
#### community\.mysql

* mysql\_info \- Fix slave status for source terminology introduced in MySQL 8\.0\.23 \([https\://github\.com/ansible\-collections/community\.mysql/issues/682](https\://github\.com/ansible\-collections/community\.mysql/issues/682)\)\.
* mysql\_user\, mysql\_role \- fix not existent grant when revoking perms on user/role which do not have any other perms than grant option \([https\://github\.com/ansible\-collections/community\.mysql/issues/664](https\://github\.com/ansible\-collections/community\.mysql/issues/664)\)\.

<a id="community-proxmox-1"></a>
#### community\.proxmox

* proxmox inventory plugin and proxmox module utils \- avoid Python 2 compatibility imports \([https\://github\.com/ansible\-collections/community\.proxmox/pull/175](https\://github\.com/ansible\-collections/community\.proxmox/pull/175)\)\.
* proxmox\_kvm \- remove limited choice for vga option in proxmox\_kvm \([https\://github\.com/ansible\-collections/community\.proxmox/pull/185](https\://github\.com/ansible\-collections/community\.proxmox/pull/185)\)
* proxmox\_kvm\, proxmox\_template \- remove <code>ansible\.module\_utils\.six</code> dependency \([https\://github\.com/ansible\-collections/community\.proxmox/pull/201](https\://github\.com/ansible\-collections/community\.proxmox/pull/201)\)\.
* proxmox\_storage \- fixed adding PBS\-type storage by ensuring its parameters \(server\, datastore\, etc\.\) are correctly sent to the Proxmox API \([https\://github\.com/ansible\-collections/community\.proxmox/pull/171](https\://github\.com/ansible\-collections/community\.proxmox/pull/171)\)\.
* proxmox\_user \- added a third case when testing for not\-yet\-existant user \([https\://github\.com/ansible\-collections/community\.proxmox/issues/163](https\://github\.com/ansible\-collections/community\.proxmox/issues/163)\)
* proxmox\_vm\_info \- do not throw exception when iterating through machines and optional api results are missing \([https\://github\.com/ansible\-collections/community\.proxmox/pull/191](https\://github\.com/ansible\-collections/community\.proxmox/pull/191)\)

<a id="community-routeros-1"></a>
#### community\.routeros

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.routeros/pull/405](https\://github\.com/ansible\-collections/community\.routeros/pull/405)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.routeros/pull/406](https\://github\.com/ansible\-collections/community\.routeros/pull/406)\)\.
* api \- allow querying for keys containing <code>id</code>\, as long as the key itself is not <code>id</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/396](https\://github\.com/ansible\-collections/community\.routeros/issues/396)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/398](https\://github\.com/ansible\-collections/community\.routeros/pull/398)\)\.

<a id="community-sops-1"></a>
#### community\.sops

* Avoid using <code>ansible\.module\_utils\.six</code> to avoid deprecation warnings with ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/community\.sops/pull/268](https\://github\.com/ansible\-collections/community\.sops/pull/268)\)\.
* Clean up plugin code that does not run on the target \([https\://github\.com/ansible\-collections/community\.sops/pull/275](https\://github\.com/ansible\-collections/community\.sops/pull/275)\)\.
* Fix accidental type extensions \([https\://github\.com/ansible\-collections/community\.sops/pull/269](https\://github\.com/ansible\-collections/community\.sops/pull/269)\)\.
* Note that the MIT licenced code in <code>plugins/module\_utils/\_six\.py</code> has been removed \([https\://github\.com/ansible\-collections/community\.sops/pull/275](https\://github\.com/ansible\-collections/community\.sops/pull/275)\)\.
* load\_vars action \- avoid another deprecated module utils from ansible\-core \([https\://github\.com/ansible\-collections/community\.sops/pull/270](https\://github\.com/ansible\-collections/community\.sops/pull/270)\)\.
* load\_vars action \- avoid deprecated import from ansible\-core that will be removed in ansible\-core 2\.21 \([https\://github\.com/ansible\-collections/community\.sops/pull/272](https\://github\.com/ansible\-collections/community\.sops/pull/272)\)\.
* sops vars plugin \- ensure that loaded vars are evaluated also with ansible\-core 2\.19\+ \([https\://github\.com/ansible\-collections/community\.sops/pull/273](https\://github\.com/ansible\-collections/community\.sops/pull/273)\)\.

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

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* Fixed the UT test execution through ansible\-test \- \(Issue 1003\) \- Tests Pass Using Tox But Not Ansible\-Test \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules)\)
* idrac\_server\_config\_profile \- \(Issue 959\) Can\'t export SCP \(Server configuration profile\) on iDRAC 10\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/959)\)
* idrac\_support\_assist \- Updated module playbook examples to use the correct casing for protocol names\, for CIFS and HTTPS\.
* idrac\_system\_info \- \(Issue 1017\) \- System info not being returned on gen17s with v10\.0\.0 \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1017](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1017)\)
* idrac\_system\_info \- \(Issue 967\) \- idrac\_system\_info fails on iDRAC10 with GPU\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/967)\)
* redfish\_storage\_volume \- \(Issue 1027\) Module fails on force reboot\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1027](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1027)\)

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Changed the logic of getting FortiManager system information to prevent permission denied error\.
* Supported module\_defaults\. General variables can be specified in one place by using module\_defaults\.

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fix the issue in check\_modu when backend returns invallid IP address\.
* Fix the issue in configuration\_fact and monitor\_fact when omitting vdom or assigning vdom to \"\"\.
* Fixed authentication issue in v7\.6\.4 when using access\_token\.

<a id="google-cloud-1"></a>
#### google\.cloud

* gcp\_compute\_instance \- add suppport for attaching disks to compute instances \([https\://github\.com/ansible\-collections/google\.cloud/pull/711](https\://github\.com/ansible\-collections/google\.cloud/pull/711)\)\.
* gcp\_secret\_manager \- use service\_account\_contents instead of service\_account\_info \([https\://github\.com/ansible\-collections/google\.cloud/pull/703](https\://github\.com/ansible\-collections/google\.cloud/pull/703)\)\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* floating\_ip \- Wait for the Floating IP assign action to complete to reduce chances of running into <code>locked</code> errors\.
* server \- Also check server type deprecation after server creation\.

<a id="ibm-storage-virtualize-2"></a>
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

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/998](https\://github\.com/ansible\-collections/kubernetes\.core/pull/998)\)\.
* Update the <em class="title-reference">k8s\_cp</em> module to also work for init containers \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/971](https\://github\.com/ansible\-collections/kubernetes\.core/pull/971)\)\.

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* Added manual utf\-8 encoding to handle unicode characters in passwords for HTTP Basic Authentication in netapp module utilities\.
* na\_ontap\_ntfs\_dacl \- fixed typo in short description\.
* na\_ontap\_rest\_info \- added error handling when API doesn\'t return zero records\.
* na\_ontap\_snapmirror \- fixed intermittent issue with creating relationship\.
* na\_ontap\_volume \- fix idempotency issue with <em class="title-reference">nas\_application\_template</em> and <em class="title-reference">size\_change\_threshold</em>\.

<a id="ngine-io-cloudstack-1"></a>
#### ngine\_io\.cloudstack

* Ensure tags are applied when creating or updating a template \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/154](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/154)\)\.

<a id="purestorage-flasharray-2"></a>
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

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* Drop incorrect requirement on aiohttp \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/230](https\://github\.com/ansible\-collections/vmware\.vmware/pull/230)\)\.
* cluster\_ha \- Fix admission control policy not being updated when ac is disabled
* content\_template \- Fix typo in code for check mode that tried to access a module param which doesn\'t exist\.
* import\_content\_library\_ovf \- Fix large file import by using requests instead of open\_url\. Requests allows for streaming uploads\, instead of reading the entire file into memory\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/220](https\://github\.com/ansible\-collections/vmware\.vmware/issues/220)\)
* vm\_powerstate \- Ensure timeout option also applies to the shutdown\-guest state

<a id="known-issues"></a>
### Known Issues

<a id="ansible-core-7"></a>
#### Ansible\-core

* templating \- Exceptions raised in a Jinja <code>set</code> or <code>with</code> block which are not accessed by the template are ignored in the same manner as undefined values\.
* templating \- Passing a container created in a Jinja <code>set</code> or <code>with</code> block to a method results in a copy of that container\. Mutations to that container which are not returned by the method will be discarded\.

<a id="community-sops-2"></a>
#### community\.sops

* When using the <code>community\.sops\.load\_vars</code> with ansible\-core 2\.20\, note that the deprecation of <code>INJECT\_FACTS\_AS\_VARS</code> causes deprecation warnings to be shown every time a variable loaded with <code>community\.sops\.load\_vars</code> is used\. This is due to ansible\-core deprecating <code>INJECT\_FACTS\_AS\_VARS</code> without providing an alternative for modules like <code>community\.sops\.load\_vars</code> to use\. If you do not like these deprecation warnings\, you have to explicitly set <code>INJECT\_FACTS\_AS\_VARS</code> to <code>true</code>\. <strong>DO NOT</strong> change the use of SOPS encrypted variables to <code>ansible\_facts</code>\. The situation will hopefully improve in ansible\-core 2\.21 through the promised API that allows action plugins to set variables\; community\.sops will adapt to use it\, which will make the warning go away\. \(The API was originally promised for ansible\-core 2\.20\, but then delayed\.\)

<a id="dellemc-openmanage-3"></a>
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

<a id="new-plugins"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.tasks\_only \- Only show tasks\.

<a id="filter"></a>
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

<a id="community-general-6"></a>
#### community\.general

* community\.general\.django\_dumpdata \- Wrapper for <code>django\-admin dumpdata</code>\.
* community\.general\.django\_loaddata \- Wrapper for <code>django\-admin loaddata</code>\.
* community\.general\.jenkins\_credential \- Manage Jenkins credentials and domains through API\.
* community\.general\.kea\_command \- Submits generic command to ISC KEA server on target\.
* community\.general\.keycloak\_user\_execute\_actions\_email \- Send a Keycloak execute\-actions email to a user\.
* community\.general\.lvm\_pv\_move\_data \- Move data between LVM Physical Volumes \(PVs\)\.
* community\.general\.pacemaker\_info \- Gather information about Pacemaker cluster\.
* community\.general\.pacemaker\_stonith \- Manage Pacemaker STONITH\.

<a id="community-proxmox-2"></a>
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

<a id="containers-podman-3"></a>
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

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block"></a>
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

<a id="vsp"></a>
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

<a id="ibm-storage-virtualize-3"></a>
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

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_kmip \- Manage FlashBlade KMIP server objects

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* theforeman\.foreman\.content\_view\_history\_info \- Fetch history of a Content View

<a id="unchanged-collections"></a>
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
