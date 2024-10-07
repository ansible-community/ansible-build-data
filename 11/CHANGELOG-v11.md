# Ansible 11 Release Notes

This changelog describes changes since Ansible 10\.0\.0\.

- <a href="#v11-0-0a1">v11\.0\.0a1</a>
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

<a id="v11-0-0a1"></a>
## v11\.0\.0a1

- <a href="#release-summary">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#ansible-posix">ansible\.posix</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#check-point-mgmt">check\_point\.mgmt</a>
    - <a href="#cisco-asa">cisco\.asa</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
    - <a href="#ibm-qradar">ibm\.qradar</a>
    - <a href="#junipernetworks-junos">junipernetworks\.junos</a>
    - <a href="#splunk-es">splunk\.es</a>
    - <a href="#vyos-vyos">vyos\.vyos</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#ansible-posix-1">ansible\.posix</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-dnac">cisco\.dnac</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-grafana">community\.grafana</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-okd">community\.okd</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#f5networks-f5-modules">f5networks\.f5\_modules</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#junipernetworks-junos-1">junipernetworks\.junos</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
    - <a href="#ngine-io-cloudstack">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
    - <a href="#vyos-vyos-1">vyos\.vyos</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#community-zabbix-2">community\.zabbix</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-grafana-1">community\.grafana</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-vmware-3">community\.vmware</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#ansible-posix-2">ansible\.posix</a>
    - <a href="#community-grafana-2">community\.grafana</a>
    - <a href="#community-okd-1">community\.okd</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#ansible-posix-3">ansible\.posix</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#arista-eos-1">arista\.eos</a>
    - <a href="#check-point-mgmt-1">check\_point\.mgmt</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-ios-3">cisco\.ios</a>
    - <a href="#cisco-ise">cisco\.ise</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-grafana-3">community\.grafana</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-network">community\.network</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#community-sops-2">community\.sops</a>
    - <a href="#community-vmware-4">community\.vmware</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#community-zabbix-3">community\.zabbix</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#inspur-ispim">inspur\.ispim</a>
    - <a href="#junipernetworks-junos-2">junipernetworks\.junos</a>
    - <a href="#kaytus-ksmanage">kaytus\.ksmanage</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
    - <a href="#ngine-io-cloudstack-1">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-2">vmware\.vmware\_rest</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#dellemc-openmanage-3">dellemc\.openmanage</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#filter">Filter</a>
    - <a href="#test">Test</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#check-point-mgmt-2">check\_point\.mgmt</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-grafana-4">community\.grafana</a>
    - <a href="#community-zabbix-4">community\.zabbix</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-4">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#microsoft-ad-2">microsoft\.ad</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2024\-09\-25

[Porting Guide](https\://docs\.ansible\.com/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* frr\.frr \(previously included version\: 2\.0\.2\)
* inspur\.sm \(previously included version\: 2\.3\.0\)
* netapp\.storagegrid \(previously included version\: 21\.12\.0\)
* openvswitch\.openvswitch \(previously included version\: 2\.1\.1\)
* t\_systems\_mms\.icinga\_director \(previously included version\: 2\.0\.1\)

<a id="added-collections"></a>
### Added Collections

* ieisystem\.inmanage \(version 2\.0\.0\)
* kubevirt\.core \(version 2\.1\.0\)
* vmware\.vmware \(version 1\.5\.0\)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 11\.0\.0a1 contains ansible\-core version 2\.18\.0b1\.
This is a newer version than version 2\.17\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection               | Ansible 10.0.0 | Ansible 11.0.0a1 | Notes                                                                                                                                                                                                         |
| ------------------------ | -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws               | 8.0.0          | 8.2.1            |                                                                                                                                                                                                               |
| ansible.netcommon        | 6.1.2          | 7.1.0            |                                                                                                                                                                                                               |
| ansible.posix            | 1.5.4          | 1.6.0            |                                                                                                                                                                                                               |
| ansible.windows          | 2.3.0          | 2.5.0            |                                                                                                                                                                                                               |
| arista.eos               | 9.0.0          | 10.0.0           |                                                                                                                                                                                                               |
| awx.awx                  | 24.3.1         | 24.6.1           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                  |
| azure.azcollection       | 2.3.0          | 2.7.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                  |
| check_point.mgmt         | 5.2.3          | 6.2.1            |                                                                                                                                                                                                               |
| cisco.aci                | 2.9.0          | 2.10.1           |                                                                                                                                                                                                               |
| cisco.asa                | 5.0.1          | 6.0.0            |                                                                                                                                                                                                               |
| cisco.dnac               | 6.13.3         | 6.18.0           |                                                                                                                                                                                                               |
| cisco.intersight         | 2.0.9          | 2.0.18           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                  |
| cisco.ios                | 8.0.0          | 9.0.2            |                                                                                                                                                                                                               |
| cisco.iosxr              | 9.0.0          | 10.1.0           |                                                                                                                                                                                                               |
| cisco.ise                | 2.9.1          | 2.9.3            |                                                                                                                                                                                                               |
| cisco.meraki             | 2.18.1         | 2.18.2           |                                                                                                                                                                                                               |
| cisco.mso                | 2.6.0          | 2.9.0            |                                                                                                                                                                                                               |
| cisco.nxos               | 8.0.0          | 9.2.1            |                                                                                                                                                                                                               |
| cisco.ucs                | 1.10.0         | 1.14.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                  |
| cloudscale_ch.cloud      | 2.3.1          | 2.4.0            |                                                                                                                                                                                                               |
| community.crypto         | 2.20.0         | 2.22.0           |                                                                                                                                                                                                               |
| community.digitalocean   | 1.26.0         | 1.27.0           | There are no changes recorded in the changelog.                                                                                                                                                               |
| community.dns            | 3.0.0          | 3.0.4            |                                                                                                                                                                                                               |
| community.docker         | 3.10.3         | 3.12.2           |                                                                                                                                                                                                               |
| community.general        | 9.0.1          | 9.4.0            |                                                                                                                                                                                                               |
| community.grafana        | 1.9.1          | 2.1.0            |                                                                                                                                                                                                               |
| community.hrobot         | 2.0.0          | 2.0.1            |                                                                                                                                                                                                               |
| community.mongodb        | 1.7.4          | 1.7.6            | There are no changes recorded in the changelog.                                                                                                                                                               |
| community.mysql          | 3.9.0          | 3.10.3           |                                                                                                                                                                                                               |
| community.network        | 5.0.2          | 5.0.3            |                                                                                                                                                                                                               |
| community.okd            | 3.0.1          | 4.0.0            |                                                                                                                                                                                                               |
| community.postgresql     | 3.4.1          | 3.6.1            |                                                                                                                                                                                                               |
| community.proxysql       | 1.5.1          | 1.6.0            |                                                                                                                                                                                                               |
| community.routeros       | 2.15.0         | 2.19.0           |                                                                                                                                                                                                               |
| community.sops           | 1.6.7          | 1.9.0            |                                                                                                                                                                                                               |
| community.vmware         | 4.4.0          | 5.0.0            |                                                                                                                                                                                                               |
| community.windows        | 2.2.0          | 2.3.0            |                                                                                                                                                                                                               |
| community.zabbix         | 2.4.0          | 3.1.2            |                                                                                                                                                                                                               |
| containers.podman        | 1.13.0         | 1.16.0           |                                                                                                                                                                                                               |
| cyberark.conjur          | 1.2.2          | 1.3.0            | You can find the collection's changelog at `[https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| cyberark.pas             | 1.0.25         | 1.0.27           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                  |
| dellemc.enterprise_sonic | 2.4.0          | 2.5.1            |                                                                                                                                                                                                               |
| dellemc.openmanage       | 9.2.0          | 9.6.0            |                                                                                                                                                                                                               |
| dellemc.powerflex        | 2.4.0          | 2.5.0            |                                                                                                                                                                                                               |
| f5networks.f5_modules    | 1.28.0         | 1.31.0           |                                                                                                                                                                                                               |
| fortinet.fortimanager    | 2.5.0          | 2.7.0            |                                                                                                                                                                                                               |
| fortinet.fortios         | 2.3.6          | 2.3.7            |                                                                                                                                                                                                               |
| google.cloud             | 1.3.0          | 1.4.1            |                                                                                                                                                                                                               |
| grafana.grafana          | 5.2.0          | 5.5.1            |                                                                                                                                                                                                               |
| hetzner.hcloud           | 3.1.1          | 4.2.1            |                                                                                                                                                                                                               |
| ibm.qradar               | 3.0.0          | 4.0.0            |                                                                                                                                                                                                               |
| ibm.storage_virtualize   | 2.3.1          | 2.5.0            |                                                                                                                                                                                                               |
| ieisystem.inmanage       |                | 2.0.0            | The collection was added to Ansible                                                                                                                                                                           |
| inspur.ispim             | 2.2.1          | 2.2.3            |                                                                                                                                                                                                               |
| junipernetworks.junos    | 8.0.0          | 9.1.0            |                                                                                                                                                                                                               |
| kaytus.ksmanage          | 1.2.1          | 1.2.2            |                                                                                                                                                                                                               |
| kubernetes.core          | 3.1.0          | 5.0.0            |                                                                                                                                                                                                               |
| kubevirt.core            |                | 2.1.0            | The collection was added to Ansible                                                                                                                                                                           |
| lowlydba.sqlserver       | 2.3.2          | 2.3.3            |                                                                                                                                                                                                               |
| microsoft.ad             | 1.5.0          | 1.7.1            |                                                                                                                                                                                                               |
| netapp.ontap             | 22.11.0        | 22.12.0          |                                                                                                                                                                                                               |
| netbox.netbox            | 3.18.0         | 3.20.0           |                                                                                                                                                                                                               |
| ngine_io.cloudstack      | 2.3.0          | 2.4.1            |                                                                                                                                                                                                               |
| purestorage.flasharray   | 1.28.0         | 1.31.1           |                                                                                                                                                                                                               |
| purestorage.flashblade   | 1.17.0         | 1.18.0           |                                                                                                                                                                                                               |
| splunk.es                | 3.0.0          | 4.0.0            |                                                                                                                                                                                                               |
| theforeman.foreman       | 4.0.0          | 4.2.0            |                                                                                                                                                                                                               |
| vmware.vmware            |                | 1.5.0            | The collection was added to Ansible                                                                                                                                                                           |
| vmware.vmware_rest       | 3.0.1          | 4.1.0            |                                                                                                                                                                                                               |
| vultr.cloud              | 1.12.1         | 1.13.0           |                                                                                                                                                                                                               |
| vyos.vyos                | 4.1.0          | 5.0.0            |                                                                                                                                                                                                               |
| wti.remote               | 1.0.5          | 1.0.10           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                  |

<a id="major-changes"></a>
### Major Changes

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="ansible-posix"></a>
#### ansible\.posix

* Dropping support for Ansible 2\.9\, ansible\-core 2\.15 will be minimum required version for this release

<a id="arista-eos"></a>
#### arista\.eos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em> due to the end\-of\-life status of previous <em class="title-reference">ansible\-core</em> versions\.

<a id="check-point-mgmt"></a>
#### check\_point\.mgmt

* New R82 Resource Modules
* Support relative positioning for sections

<a id="cisco-asa"></a>
#### cisco\.asa

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-ios"></a>
#### cisco\.ios

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="cisco-nxos"></a>
#### cisco\.nxos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="community-vmware"></a>
#### community\.vmware

* vmware\_guest\_tools\_upgrade \- Subsitute the deprecated <code>guest\.toolsStatus</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2174](https\://github\.com/ansible\-collections/community\.vmware/pull/2174)\)\.
* vmware\_vm\_shell \- Subsitute the deprecated <code>guest\.toolsStatus</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2174](https\://github\.com/ansible\-collections/community\.vmware/pull/2174)\)\.

<a id="community-zabbix"></a>
#### community\.zabbix

* All Roles \- Add support for openSUSE Leap 15 and SLES 15\.
* All Roles \- Separate installation of Zabbix repo from all other roles and link them together\.

<a id="containers-podman"></a>
#### containers\.podman

* Add mount and unmount for volumes
* Add multiple subnets for networks
* Add new options for podman\_container
* Add new options to pod module
* Add podman search
* Improve idempotency for networking in podman\_container
* Redesign idempotency for Podman Pod module

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* Added support to use session ID for authentication of iDRAC\, OpenManage Enterprise and OpenManage Enterprise Modular\.
* idrac\_secure\_boot \- This module allows to import the secure boot certificate\.
* idrac\_server\_config\_profile \- This module is enhanced to allow you to export and import custom defaults on iDRAC\.
* idrac\_support\_assist \- This module allows to run and export SupportAssist collection logs on iDRAC\.
* ome\_configuration\_compliance\_baseline \- This module is enhanced to schedule the remediation job and stage the reboot\.
* ome\_session \- This module allows you to create and delete the sessions on OpenManage Enterprise and OpenManage Enterprise Modular\.

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Add a sanity\_test\.yaml file to trigger CI tests in GitHub\.
* Support Ansible\-core 2\.17\.
* Support new FOS versions 7\.4\.4\.

<a id="grafana-grafana"></a>
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
* fix\:mimir molecule should use ansible core 2\.16 by \@GVengelen in https\://github\.com/grafana/grafana\-ansible\-collection/pull/254

<a id="ibm-qradar"></a>
#### ibm\.qradar

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="junipernetworks-junos"></a>
#### junipernetworks\.junos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="splunk-es"></a>
#### splunk\.es

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="vyos-vyos"></a>
#### vyos\.vyos

* Bumping <em class="title-reference">requires\_ansible</em> to <em class="title-reference">\>\=2\.15\.0</em>\, since previous ansible\-core versions are EoL now\.

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-1"></a>
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
* ansible\-test \- Update <code>pypi\-test\-container</code> to version 3\.2\.0\.
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
* s3\_bucket \- Add <code>object\_lock\_default\_retention</code> to set Object Lock default retention configuration for S3 buckets \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2062](https\://github\.com/ansible\-collections/amazon\.aws/pull/2062)\)\.
* s3\_bucket \- Add support for bucket inventories \([https\://docs\.aws\.amazon\.com/AmazonS3/latest/userguide/storage\-inventory\.html](https\://docs\.aws\.amazon\.com/AmazonS3/latest/userguide/storage\-inventory\.html)\)
* s3\_bucket \- Add support for enabling Amazon S3 Transfer Acceleration by setting the <code>accelerate\_enabled</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2046](https\://github\.com/ansible\-collections/amazon\.aws/pull/2046)\)\.
* s3\_object \- Add support for <code>expected\_bucket\_owner</code> option \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2114](https\://github\.com/ansible\-collections/amazon\.aws/issues/2114)\)\.
* ssm parameter lookup \- add new option <code>droppath</code> to drop the hierarchical search path from ssm parameter lookup results \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1756](https\://github\.com/ansible\-collections/amazon\.aws/pull/1756)\)\.

<a id="ansible-netcommon-1"></a>
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

<a id="ansible-windows"></a>
#### ansible\.windows

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Ansible\.
* owner \- Migrated to <code>Ansible\.Basic</code> format to add basic checks like invocation args checking
* win\_powershell \- Added the <code>sensitive\_parameters</code> option that can be used to pass in a SecureString or PSCredential parameter value\.
* win\_powershell \- Changed <em class="title-reference">sensitive\_parameters</em> to use <em class="title-reference">New\-Object</em>\, rather than <em class="title-reference">\:\:new\(\)</em>
* win\_setup \- Added the <code>ansible\_win\_rm\_certificate\_thumbprint</code> fact to display the thumbprint of the certificate in use
* win\_user \- Added the ability to set an account expiration date using the <code>account\_expires</code> option \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/610](https\://github\.com/ansible\-collections/ansible\.windows/issues/610)

<a id="cisco-aci"></a>
#### cisco\.aci

* Add aci\_esg\_to\_contract module for esg contract relationship objects fvRsCons \(consumer\)\, fvRsConsIf \(consumer interface\)\, fvRsProv \(provider\) and fvRsIntraEpg \(intra\_esg\)
* Add aci\_system\_connectivity\_preference module \(\#601\)
* Added suppress\-previous flag option to reduce the number of API calls\. \(\#636\)
* Enable relative path and/or filename of private key for the aci httpapi plugin\.

<a id="cisco-dnac"></a>
#### cisco\.dnac

* Added \'accesspoint\_workflow\_manager\' module to manage access point configurations\.
* Added \'fabric\_sites\_zones\_workflow\_manager\.py\' to manage fabric sites/zones and update the authentication profile template\.
* Added \'rma\_workflow\_manager\' module to manage RMA workflow\.
* Added \'sda\_extranet\_policies\_workflow\_manager\' to provide SDA Extranet Policies for managing SDA Extranet Policy\.
* Added \'user\_role\_workflow\_manager\' module to manage operations to create\, update\, and delete users and roles\.
* Added API to validate the server address
* Added Circle CI support for integration testing\.
* Added detailed documentation in network\_settings\_workflow\_manager\.py
* Added example playbooks in device\_provision\_workflow\.yml
* Added example playbooks in network\_compliance\_workflow\_manager\.py
* Added new attribute \'ise\_integration\_wait\_time\' in ise\_radius\_integration\_workflow\_manager\.py
* Added the code for creating/updating/deleting events subscription notification with specified destination and added the playbook and documentation with examples
* Adding pyzipper support in device\_configs workflow manager module\.
* Adding run\_compliance\_batch\_size support in network\_compliance module\.
* Bug fixes in user\_role\_workflow\_manager module\.
* Changes in accesspoint\_workflow\_manager module\.
* Changes in device\_configs\_backup\_workflow\_manager to support name of the site to which the device is assigned\.
* Changes in inventory and swim workflow manager modules\.
* Changes in inventory\_workflow\_manager to support maximum devices to resync\, and resync timeout\.
* Changes in network\_settings\_workflow\_manager to support reserve ip subpools\.
* Changes in provision workflow manager module\.
* Changes in provision\_workflow\_manager to support enhanced log messages\.
* Changes in rma\_workflow\_manager module to support pre check for device replacement\.
* Checking SNMP versions in events\_and\_notifications\_workflow\_manager\.py module
* Checking the device list in swim workflow manager module\.
* Exporting export\_device\_details\_limit in inventory workflow module\.
* Fix family name from userand\_roles to user\_and\_roles\.
* Fix module name from network\_device\_config\_\_info to configuration\_archive\_details\_info\.
* Minor bug fixes in device\_credential\_workflow\_manager\.py module
* UT and IT cases for worflow manager modules\.
* application\_policy\_application\_set \- new module
* application\_policy\_application\_set\_count\_info \- new module
* application\_policy\_application\_set\_info \- new module
* applications\_count\_v2\_info \- new module
* applications\_v2 \- new module
* applications\_v2\_info \- new module
* auth\_token\_create \- new module
* authentication\_policy\_servers \- new module
* device\_configs\_backup\_workflow\_manager \- New workflow manager module for device configuration backup functions\.
* device\_configs\_backup\_workflow\_manager\.py\. added attribute \'site\'\.
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

<a id="cisco-ios-1"></a>
#### cisco\.ios

* Add ios\_vrf\_global resource module in favor of ios\_vrf module \(fixes \- [https\://github\.com/ansible\-collections/cisco\.ios/pull/1055](https\://github\.com/ansible\-collections/cisco\.ios/pull/1055)\)

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Adds a new module <em class="title-reference">iosxr\_vrf\_address\_family</em> to manage VRFs address families on Cisco IOS\-XR devices \([https\://github\.com/ansible\-collections/cisco\.iosxr/pull/489](https\://github\.com/ansible\-collections/cisco\.iosxr/pull/489)\)\.
* Adds a new module <em class="title-reference">iosxr\_vrf\_global</em> to manage VRF global configurations on Cisco IOS\-XR devices \([https\://github\.com/ansible\-collections/cisco\.iosxr/pull/467](https\://github\.com/ansible\-collections/cisco\.iosxr/pull/467)\)\.

<a id="cisco-meraki"></a>
#### cisco\.meraki

* Include networks\_appliance\_traffic\_shaping\_custom\_performance\_classes\_info plugin\.

<a id="cisco-mso"></a>
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

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* Add nxos\_vrf\_global resource module in favor of nxos\_vrf module \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/870](https\://github\.com/ansible\-collections/cisco\.nxos/pull/870)\)\.
* nxos\_bgp\_global \- Deprecate local\_as with local\_as\_config which supports more configuration attributes\, under neighbor\.
* route\_maps \- support simple route\-maps that do not contain set or match statements\. it allows for the creation and management of purely basic route\-map entries like \'route\-map test\-1 permit 10\'\.

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Update source\_format of custom images with actually available choices\.

<a id="community-crypto"></a>
#### community\.crypto

* certificate\_complete\_chain \- add ability to identify Ed25519 and Ed448 complete chains \([https\://github\.com/ansible\-collections/community\.crypto/pull/777](https\://github\.com/ansible\-collections/community\.crypto/pull/777)\)\.
* get\_certificate \- adds <code>tls\_ctx\_options</code> option for specifying SSL CTX options \([https\://github\.com/ansible\-collections/community\.crypto/pull/779](https\://github\.com/ansible\-collections/community\.crypto/pull/779)\)\.
* get\_certificate \- allow to obtain the certificate chain sent by the server\, and the one used for validation\, with the new <code>get\_certificate\_chain</code> option\. Note that this option only works if the module is run with Python 3\.10 or newer \([https\://github\.com/ansible\-collections/community\.crypto/issues/568](https\://github\.com/ansible\-collections/community\.crypto/issues/568)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/784](https\://github\.com/ansible\-collections/community\.crypto/pull/784)\)\.
* openssl\_privatekey\, openssl\_privatekey\_pipe \- add default value <code>auto</code> for <code>cipher</code> option\, which happens to be the only supported value for this option anyway\. Therefore it is no longer necessary to specify <code>cipher\=auto</code> when providing <code>passphrase</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/793](https\://github\.com/ansible\-collections/community\.crypto/issues/793)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/794](https\://github\.com/ansible\-collections/community\.crypto/pull/794)\)\.

<a id="community-docker"></a>
#### community\.docker

* docker\, docker\_api connection plugins \- allow to determine the working directory when executing commands with the new <code>working\_dir</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/943](https\://github\.com/ansible\-collections/community\.docker/pull/943)\)\.
* docker\, docker\_api connection plugins \- allow to execute commands with extended privileges with the new <code>privileges</code> option \([https\://github\.com/ansible\-collections/community\.docker/pull/943](https\://github\.com/ansible\-collections/community\.docker/pull/943)\)\.
* docker\, docker\_api connection plugins \- allow to pass extra environment variables when executing commands with the new <code>extra\_env</code> option \([https\://github\.com/ansible\-collections/community\.docker/issues/937](https\://github\.com/ansible\-collections/community\.docker/issues/937)\, [https\://github\.com/ansible\-collections/community\.docker/pull/940](https\://github\.com/ansible\-collections/community\.docker/pull/940)\)\.
* docker\_compose\_v2\* modules \- support Docker Compose 2\.29\.0\'s <code>json</code> progress writer to avoid having to parse text output \([https\://github\.com/ansible\-collections/community\.docker/pull/931](https\://github\.com/ansible\-collections/community\.docker/pull/931)\)\.
* docker\_compose\_v2\_pull \- add new options <code>ignore\_buildable</code>\, <code>include\_deps</code>\, and <code>services</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/941](https\://github\.com/ansible\-collections/community\.docker/issues/941)\, [https\://github\.com/ansible\-collections/community\.docker/pull/942](https\://github\.com/ansible\-collections/community\.docker/pull/942)\)\.
* docker\_container \- add support for <code>device\_cgroup\_rules</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/910](https\://github\.com/ansible\-collections/community\.docker/pull/910)\)\.
* docker\_container \- the new <code>state\=healthy</code> allows to wait for a container to become healthy on startup\. The <code>healthy\_wait\_timeout</code> option allows to configure the maximum time to wait for this to happen \([https\://github\.com/ansible\-collections/community\.docker/issues/890](https\://github\.com/ansible\-collections/community\.docker/issues/890)\, [https\://github\.com/ansible\-collections/community\.docker/pull/921](https\://github\.com/ansible\-collections/community\.docker/pull/921)\)\.
* docker\_container \- when creating a container\, directly pass all networks to connect to to the Docker Daemon for API version 1\.44 and newer\. This makes creation more efficient and works around a bug in Docker Daemon that does not use the specified MAC address in at least some cases\, though only for creation \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.

<a id="community-general"></a>
#### community\.general

* CmdRunner module util \- argument formats can be specified as plain functions without calling <code>cmd\_runner\_fmt\.as\_func\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8479](https\://github\.com/ansible\-collections/community\.general/pull/8479)\)\.
* CmdRunner module utils \- the parameter <code>force\_lang</code> now supports the special value <code>auto</code> which will automatically try and determine the best parsable locale in the system \([https\://github\.com/ansible\-collections/community\.general/pull/8517](https\://github\.com/ansible\-collections/community\.general/pull/8517)\)\.
* MH module utils \- add parameter <code>when</code> to <code>cause\_changes</code> decorator \([https\://github\.com/ansible\-collections/community\.general/pull/8766](https\://github\.com/ansible\-collections/community\.general/pull/8766)\)\.
* MH module utils \- minor refactor in decorators \([https\://github\.com/ansible\-collections/community\.general/pull/8766](https\://github\.com/ansible\-collections/community\.general/pull/8766)\)\.
* alternatives \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* ansible\_galaxy\_install \- add upgrade feature \([https\://github\.com/ansible\-collections/community\.general/pull/8431](https\://github\.com/ansible\-collections/community\.general/pull/8431)\, [https\://github\.com/ansible\-collections/community\.general/issues/8351](https\://github\.com/ansible\-collections/community\.general/issues/8351)\)\.
* apache2\_mod\_proxy \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* apache2\_mod\_proxy \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* cargo \- add option <code>directory</code>\, which allows source directory to be specified \([https\://github\.com/ansible\-collections/community\.general/pull/8480](https\://github\.com/ansible\-collections/community\.general/pull/8480)\)\.
* cgroup\_memory\_recap\, hipchat\, jabber\, log\_plays\, loganalytics\, logentries\, logstash\, slack\, splunk\, sumologic\, syslog\_json callback plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8628](https\://github\.com/ansible\-collections/community\.general/pull/8628)\)\.
* chef\_databag\, consul\_kv\, cyberarkpassword\, dsv\, etcd\, filetree\, hiera\, onepassword\, onepassword\_doc\, onepassword\_raw\, passwordstore\, redis\, shelvefile\, tss lookup plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8626](https\://github\.com/ansible\-collections/community\.general/pull/8626)\)\.
* chroot\, funcd\, incus\, iocage\, jail\, lxc\, lxd\, qubes\, zone connection plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8627](https\://github\.com/ansible\-collections/community\.general/pull/8627)\)\.
* cmd\_runner module utils \- add decorator <code>cmd\_runner\_fmt\.stack</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8415](https\://github\.com/ansible\-collections/community\.general/pull/8415)\)\.
* cmd\_runner\_fmt module utils \- simplify implementation of <code>cmd\_runner\_fmt\.as\_bool\_not\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8512](https\://github\.com/ansible\-collections/community\.general/pull/8512)\)\.
* cobbler\, linode\, lxd\, nmap\, online\, scaleway\, stackpath\_compute\, virtualbox inventory plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8625](https\://github\.com/ansible\-collections/community\.general/pull/8625)\)\.
* consul\_acl \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* copr \- Added <code>includepkgs</code> and <code>excludepkgs</code> parameters to limit the list of packages fetched or excluded from the repository\([https\://github\.com/ansible\-collections/community\.general/pull/8779](https\://github\.com/ansible\-collections/community\.general/pull/8779)\)\.
* credstash lookup plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* csv module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* deco MH module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* doas\, dzdo\, ksu\, machinectl\, pbrun\, pfexec\, pmrun\, sesu\, sudosu become plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8623](https\://github\.com/ansible\-collections/community\.general/pull/8623)\)\.
* etcd3 \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* gconftool2 \- make use of <code>ModuleHelper</code> features to simplify code \([https\://github\.com/ansible\-collections/community\.general/pull/8711](https\://github\.com/ansible\-collections/community\.general/pull/8711)\)\.
* gio\_mime \- mute the  old <code>VarDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8776](https\://github\.com/ansible\-collections/community\.general/pull/8776)\)\.
* gitlab\_group \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* gitlab\_project \- add option <code>container\_expiration\_policy</code> to schedule container registry cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/8674](https\://github\.com/ansible\-collections/community\.general/pull/8674)\)\.
* gitlab\_project \- add option <code>issues\_access\_level</code> to enable/disable project issues \([https\://github\.com/ansible\-collections/community\.general/pull/8760](https\://github\.com/ansible\-collections/community\.general/pull/8760)\)\.
* gitlab\_project \- add option <code>model\_registry\_access\_level</code> to disable model registry \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- add option <code>pages\_access\_level</code> to disable project pages \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
* gitlab\_project \- add option <code>repository\_access\_level</code> to disable project repository \([https\://github\.com/ansible\-collections/community\.general/pull/8674](https\://github\.com/ansible\-collections/community\.general/pull/8674)\)\.
* gitlab\_project \- add option <code>service\_desk\_enabled</code> to disable service desk \([https\://github\.com/ansible\-collections/community\.general/pull/8688](https\://github\.com/ansible\-collections/community\.general/pull/8688)\)\.
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
* ipa\_dnsrecord \- adds <code>SSHFP</code> record type for managing SSH fingerprints in FreeIPA DNS \([https\://github\.com/ansible\-collections/community\.general/pull/8404](https\://github\.com/ansible\-collections/community\.general/pull/8404)\)\.
* ipa\_otptoken \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* jira \- mute the  old <code>VarDict</code> deprecation \([https\://github\.com/ansible\-collections/community\.general/pull/8776](https\://github\.com/ansible\-collections/community\.general/pull/8776)\)\.
* jira \- replace deprecated params when using decorator <code>cause\_changes</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8791](https\://github\.com/ansible\-collections/community\.general/pull/8791)\)\.
* keep\_keys filter plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* keycloak\_client \- assign auth flow by name \([https\://github\.com/ansible\-collections/community\.general/pull/8428](https\://github\.com/ansible\-collections/community\.general/pull/8428)\)\.
* keycloak\_client \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_clientscope \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_identity\_provider \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_user\_federation \- add module argument allowing users to optout of the removal of unspecified mappers\, for example to keep the keycloak default mappers \([https\://github\.com/ansible\-collections/community\.general/pull/8764](https\://github\.com/ansible\-collections/community\.general/pull/8764)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* keycloak\_user\_federation \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* linode \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* locale\_gen \- add support for multiple locales \([https\://github\.com/ansible\-collections/community\.general/issues/8677](https\://github\.com/ansible\-collections/community\.general/issues/8677)\, [https\://github\.com/ansible\-collections/community\.general/pull/8682](https\://github\.com/ansible\-collections/community\.general/pull/8682)\)\.
* lxc\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* lxd\_container \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* manageiq\_provider \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* memcached\, pickle\, redis\, yaml cache plugins \- make sure that all options are typed \([https\://github\.com/ansible\-collections/community\.general/pull/8624](https\://github\.com/ansible\-collections/community\.general/pull/8624)\)\.
* ocapi\_utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* one\_service \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* one\_vm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* onepassword lookup plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* openbsd\_pkg \- adds diff support to show changes in installed package list\. This does not yet work for check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8402](https\://github\.com/ansible\-collections/community\.general/pull/8402)\)\.
* opentelemetry callback plugin \- fix default value for <code>store\_spans\_in\_file</code> causing traces to be produced to a file named <code>None</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8566](https\://github\.com/ansible\-collections/community\.general/issues/8566)\, [https\://github\.com/ansible\-collections/community\.general/pull/8741](https\://github\.com/ansible\-collections/community\.general/pull/8741)\)\.
* passwordstore lookup plugin \- add the current user to the lockfile file name to address issues on multi\-user systems \([https\://github\.com/ansible\-collections/community\.general/pull/8689](https\://github\.com/ansible\-collections/community\.general/pull/8689)\)\.
* pids \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pipx \- add parameter <code>suffix</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8675](https\://github\.com/ansible\-collections/community\.general/pull/8675)\, [https\://github\.com/ansible\-collections/community\.general/issues/8656](https\://github\.com/ansible\-collections/community\.general/issues/8656)\)\.
* pipx \- added new states <code>install\_all</code>\, <code>uninject</code>\, <code>upgrade\_shared</code>\, <code>pin</code>\, and <code>unpin</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8809](https\://github\.com/ansible\-collections/community\.general/pull/8809)\)\.
* pipx \- added parameter <code>global</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pipx\_info \- added parameter <code>global</code> to module \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx\_info \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pkg5\_publisher \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* pkgng \- add option <code>use\_globs</code> \(default <code>true</code>\) to optionally disable glob patterns \([https\://github\.com/ansible\-collections/community\.general/issues/8632](https\://github\.com/ansible\-collections/community\.general/issues/8632)\, [https\://github\.com/ansible\-collections/community\.general/pull/8633](https\://github\.com/ansible\-collections/community\.general/pull/8633)\)\.
* proxmox \- add <code>disk\_volume</code> and <code>mount\_volumes</code> keys for better readability \([https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox \- allow specification of the API port when using proxmox\_\* \([https\://github\.com/ansible\-collections/community\.general/issues/8440](https\://github\.com/ansible\-collections/community\.general/issues/8440)\, [https\://github\.com/ansible\-collections/community\.general/pull/8441](https\://github\.com/ansible\-collections/community\.general/pull/8441)\)\.
* proxmox \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox \- translate the old <code>disk</code> and <code>mounts</code> keys to the new handling internally \([https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox inventory plugin \- add new fact for LXC interface details \([https\://github\.com/ansible\-collections/community\.general/pull/8713](https\://github\.com/ansible\-collections/community\.general/pull/8713)\)\.
* proxmox\_disk \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_kvm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* proxmox\_kvm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* proxmox\_template \- small refactor in logic for determining whether a template exists or not \([https\://github\.com/ansible\-collections/community\.general/pull/8516](https\://github\.com/ansible\-collections/community\.general/pull/8516)\)\.
* proxmox\_vm\_info \- add <code>network</code> option to retrieve current network information \([https\://github\.com/ansible\-collections/community\.general/pull/8471](https\://github\.com/ansible\-collections/community\.general/pull/8471)\)\.
* redfish\_\* modules \- adds <code>ciphers</code> option for custom cipher selection \([https\://github\.com/ansible\-collections/community\.general/pull/8533](https\://github\.com/ansible\-collections/community\.general/pull/8533)\)\.
* redfish\_command \- add <code>wait</code> and <code>wait\_timeout</code> options to allow a user to block a command until a service is accessible after performing the requested command \([https\://github\.com/ansible\-collections/community\.general/issues/8051](https\://github\.com/ansible\-collections/community\.general/issues/8051)\, [https\://github\.com/ansible\-collections/community\.general/pull/8434](https\://github\.com/ansible\-collections/community\.general/pull/8434)\)\.
* redfish\_info \- add command <code>CheckAvailability</code> to check if a service is accessible \([https\://github\.com/ansible\-collections/community\.general/issues/8051](https\://github\.com/ansible\-collections/community\.general/issues/8051)\, [https\://github\.com/ansible\-collections/community\.general/pull/8434](https\://github\.com/ansible\-collections/community\.general/pull/8434)\)\.
* redfish\_utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* redfish\_utils module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* redis cache plugin \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8833](https\://github\.com/ansible\-collections/community\.general/pull/8833)\)\.
* redis\, redis\_info \- add <code>client\_cert</code> and <code>client\_key</code> options to specify path to certificate for Redis authentication  \([https\://github\.com/ansible\-collections/community\.general/pull/8654](https\://github\.com/ansible\-collections/community\.general/pull/8654)\)\.
* redis\_info \- adds support for getting cluster info \([https\://github\.com/ansible\-collections/community\.general/pull/8464](https\://github\.com/ansible\-collections/community\.general/pull/8464)\)\.
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
* sudosu become plugin \- added an option \(<code>alt\_method</code>\) to enhance compatibility with more versions of <code>su</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8214](https\://github\.com/ansible\-collections/community\.general/pull/8214)\)\.
* ufw \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* unsafe plugin utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vardict module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* vars MH module utils \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8814](https\://github\.com/ansible\-collections/community\.general/pull/8814)\)\.
* virtualbox inventory plugin \- expose a new parameter <code>enable\_advanced\_group\_parsing</code> to change how the VirtualBox dynamic inventory parses VM groups \([https\://github\.com/ansible\-collections/community\.general/issues/8508](https\://github\.com/ansible\-collections/community\.general/issues/8508)\, [https\://github\.com/ansible\-collections/community\.general/pull/8510](https\://github\.com/ansible\-collections/community\.general/pull/8510)\)\.
* vmadm \- replace Python 2\.6 construct with dict comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/8822](https\://github\.com/ansible\-collections/community\.general/pull/8822)\)\.
* wdc\_redfish\_command \- minor change to handle upgrade file for Redfish WD platforms \([https\://github\.com/ansible\-collections/community\.general/pull/8444](https\://github\.com/ansible\-collections/community\.general/pull/8444)\)\.

<a id="community-grafana"></a>
#### community\.grafana

* Add <em class="title-reference">grafana\_contact\_point</em> module
* Add support of <em class="title-reference">grafana\_contact\_point</em> in grafana role
* Manage subfolders for <em class="title-reference">grafana\_folder</em> and specify uid
* add org switch by <em class="title-reference">org\_id</em> and <em class="title-reference">org\_name</em> in <em class="title-reference">grafana\_silence</em>

<a id="community-mysql"></a>
#### community\.mysql

* mysql\_info \- Add <code>tls\_requires</code> returned value for the <code>users\_info</code> filter \([https\://github\.com/ansible\-collections/community\.mysql/pull/628](https\://github\.com/ansible\-collections/community\.mysql/pull/628)\)\.
* mysql\_info \- return a database server engine used \([https\://github\.com/ansible\-collections/community\.mysql/issues/644](https\://github\.com/ansible\-collections/community\.mysql/issues/644)\)\.
* mysql\_replication \- Adds support for <em class="title-reference">CHANGE REPLICATION SOURCE TO</em> statement \([https\://github\.com/ansible\-collections/community\.mysql/issues/635](https\://github\.com/ansible\-collections/community\.mysql/issues/635)\)\.
* mysql\_replication \- Adds support for <em class="title-reference">SHOW BINARY LOG STATUS</em> and <em class="title-reference">SHOW BINLOG STATUS</em> on getprimary mode\.
* mysql\_replication \- Improve detection of IsReplica and IsPrimary by inspecting the dictionary returned from the SQL query instead of relying on variable types\. This ensures compatibility with changes in the connector or the output of SHOW REPLICA STATUS and SHOW MASTER STATUS\, allowing for easier maintenance if these change in the future\.
* mysql\_user \- Add salt parameter to generate static hash for <em class="title-reference">caching\_sha2\_password</em> and <em class="title-reference">sha256\_password</em> plugins\.

<a id="community-okd"></a>
#### community\.okd

* connection/oc \- added support of local enviroment variable that will be used for <code>oc</code> and may be requried for establishing connections ifself \([https\://github\.com/openshift/community\.okd/pull/225](https\://github\.com/openshift/community\.okd/pull/225)\)\.
* inventory/openshift\.py \- Defer removal of k8s inventory plugin to version 5\.0\.0 \([https\://github\.com/openshift/community\.okd/pull/224](https\://github\.com/openshift/community\.okd/pull/224)\)\.

<a id="community-postgresql"></a>
#### community\.postgresql

* postgres \- add support for postgres <code>infinity</code> timestamps by replacing them with <code>datetime\.min</code> / <code>datetime\.max</code> values \([https\://github\.com/ansible\-collections/community\.postgresql/pull/714](https\://github\.com/ansible\-collections/community\.postgresql/pull/714)\)\.
* postgresql\_privs \- adds support for granting and revoking privileges on foreign tables \([https\://github\.com/ansible\-collections/community\.postgresql/issues/724](https\://github\.com/ansible\-collections/community\.postgresql/issues/724)\)\.
* postgresql\_publication \- add the <code>tables\_in\_schema</code> argument to implement <code>FOR TABLES IN SCHEMA</code> feature \([https\://github\.com/ansible\-collections/community\.postgresql/issues/709](https\://github\.com/ansible\-collections/community\.postgresql/issues/709)\)\.
* postgresql\_subscription \- adds support for managing subscriptions in the situation where the <code>subconninfo</code> column is unavailable \(such as in CloudSQL\) \([https\://github\.com/ansible\-collections/community\.postgresql/issues/726](https\://github\.com/ansible\-collections/community\.postgresql/issues/726)\)\.
* postgresql\_user \- adds the <code>configuration</code> argument that allows to manage user\-specific default configuration \([https\://github\.com/ansible\-collections/community\.postgresql/issues/598](https\://github\.com/ansible\-collections/community\.postgresql/issues/598)\)\.

<a id="community-proxysql"></a>
#### community\.proxysql

* proxysql role \- add the pidfile location management \([https\://github\.com/ansible\-collections/community\.proxysql/pull/145](https\://github\.com/ansible\-collections/community\.proxysql/pull/145)\)\.
* role\_proxysql \- Update default proxysql version and fix small bugs \([https\://github\.com/ansible\-collections/community\.proxysql/pull/92](https\://github\.com/ansible\-collections/community\.proxysql/pull/92)\)\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_info \- allow to restrict the output by limiting fields to specific values with the new <code>restrict</code> option \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.
* api\_info\, api\_modify \- add <code>system health settings</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/294](https\://github\.com/ansible\-collections/community\.routeros/pull/294)\)\.
* api\_info\, api\_modify \- add missing path <code>/ppp secret</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/286](https\://github\.com/ansible\-collections/community\.routeros/pull/286)\)\.
* api\_info\, api\_modify \- add missing path <code>/system resource irq rps</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/295](https\://github\.com/ansible\-collections/community\.routeros/pull/295)\)\.
* api\_info\, api\_modify \- add parameter <code>host\-key\-type</code> for <code>ip ssh</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/280](https\://github\.com/ansible\-collections/community\.routeros/issues/280)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/297](https\://github\.com/ansible\-collections/community\.routeros/pull/297)\)\.
* api\_info\, api\_modify \- add support for the <code>ip dhcp\-server matcher</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/300](https\://github\.com/ansible\-collections/community\.routeros/pull/300)\)\.
* api\_info\, api\_modify \- add support for the <code>ip dns adlist</code> path implemented by RouterOS 7\.15 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/310](https\://github\.com/ansible\-collections/community\.routeros/pull/310)\)\.
* api\_info\, api\_modify \- add support for the <code>ipv6 nd prefix</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/303](https\://github\.com/ansible\-collections/community\.routeros/pull/303)\)\.
* api\_info\, api\_modify \- add support for the <code>mld\-version</code> and <code>multicast\-querier</code> properties in <code>interface bridge</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/315](https\://github\.com/ansible\-collections/community\.routeros/pull/315)\)\.
* api\_info\, api\_modify \- add support for the <code>name</code> and <code>is\-responder</code> properties under the <code>interface wireguard peers</code> path introduced in RouterOS 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/304](https\://github\.com/ansible\-collections/community\.routeros/pull/304)\)\.
* api\_info\, api\_modify \- add support for the <code>routing filter num\-list</code> path implemented by RouterOS 7 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/313](https\://github\.com/ansible\-collections/community\.routeros/pull/313)\)\.
* api\_info\, api\_modify \- add support for the <code>routing igmp\-proxy</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/309](https\://github\.com/ansible\-collections/community\.routeros/pull/309)\)\.
* api\_info\, api\_modify \- add support for the <code>routing ospf static\-neighbor</code> path in RouterOS 7 \([https\://github\.com/ansible\-collections/community\.routeros/pull/302](https\://github\.com/ansible\-collections/community\.routeros/pull/302)\)\.
* api\_info\, api\_modify \- minor changes <code>/interface ethernet</code> path fields \([https\://github\.com/ansible\-collections/community\.routeros/pull/288](https\://github\.com/ansible\-collections/community\.routeros/pull/288)\)\.
* api\_info\, api\_modify \- set default for <code>force</code> in <code>ip dhcp\-server option</code> to an explicit <code>false</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/300](https\://github\.com/ansible\-collections/community\.routeros/pull/300)\)\.
* api\_modify \- allow to restrict what is updated by limiting fields to specific values with the new <code>restrict</code> option \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.
* api\_modify\, api\_info \- add read\-only <code>default</code> field to <code>snmp community</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/311](https\://github\.com/ansible\-collections/community\.routeros/pull/311)\)\.

<a id="community-sops"></a>
#### community\.sops

* Detect SOPS 3\.9\.0 and use new <code>decrypt</code> and <code>encrypt</code> subcommands \([https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.
* decrypt filter plugin \- now supports the input and output type <code>ini</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/204](https\://github\.com/ansible\-collections/community\.sops/pull/204)\)\.
* sops lookup plugin \- new option <code>extract</code> allows extracting a single key out of a JSON or YAML file\, equivalent to sops\' <code>decrypt \-\-extract</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/200](https\://github\.com/ansible\-collections/community\.sops/pull/200)\)\.
* sops lookup plugin \- now supports the input and output type <code>ini</code> \([https\://github\.com/ansible\-collections/community\.sops/pull/204](https\://github\.com/ansible\-collections/community\.sops/pull/204)\)\.
* sops vars plugin \- allow to configure the valid extensions with an <code>ansible\.cfg</code> entry or with an environment variable \([https\://github\.com/ansible\-collections/community\.sops/pull/185](https\://github\.com/ansible\-collections/community\.sops/pull/185)\)\.
* sops vars plugin \- new option <code>handle\_unencrypted\_files</code> allows to control behavior when encountering unencrypted files with SOPS 3\.9\.0\+ \([https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* vmware\_host\_logbundle \- Add timeout parameter \([https\://github\.com/ansible\-collections/community\.vmware/pull/2092](https\://github\.com/ansible\-collections/community\.vmware/pull/2092)\)\.
* vmware\_vm\_vm\_drs\_rule \- added datacenter argument to correctly deal with multiple clusters with same name\([https\://github\.com/ansible\-collections/community\.vmware/issues/2101](https\://github\.com/ansible\-collections/community\.vmware/issues/2101)\)\.
* vsphere\_file \- Fix examples in documentation \([https\://github\.com/ansible\-collections/community\.vmware/issues/2110](https\://github\.com/ansible\-collections/community\.vmware/issues/2110)\)\.

<a id="community-windows"></a>
#### community\.windows

* Set minimum supported Ansible version to 2\.15 to align with the versions still supported by Asnible\.

<a id="community-zabbix-1"></a>
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

<a id="containers-podman-1"></a>
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

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* Added support for Python 3\.12\.
* Added time\_to\_wait option in <code>idrac\_storage\_volume</code> module\.
* idrac\_redfish\_powerstate \- This module is enhanced to support full virtual A/C power cycle\.
* idrac\_redfish\_storage\_controller \- This module is enhanced to support secure and/or cryptographic erase of the physical disk\.
* idrac\_reset \- This module is enhanced to provide default username and default password for the reset operation\.
* ome\_application\_certificate \- This module is enhanced to support the upload of certificate chain\.
* ome\_application\_network\_proxy \- This module is enhanced to manage the Proxy Exclusion List and Certificate Validation\.

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added support for PowerFlex Onyx version\(4\.6\.x\)\.
* Fixed the roles to support attaching the MDM cluster to the gateway\.
* The storage pool module has been enhanced to support more features\.

<a id="f5networks-f5-modules"></a>
#### f5networks\.f5\_modules

* bigip\_asm\_dos\_application \- add support for creating dos profile\.
* bigip\_device\_info \- virtual\-servers \- return per\_flow\_request\_access\_policy if defined\.
* bigip\_pool\_member \- Removed state from the Returnables\.
* bigip\_ucs \- Fix for bigip\_ucs module to restore UCS file on BIG\-IP devices\.
* bigip\_virtual\_server \- set per\_flow\_request\_access\_policy and stay idempotent\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Supported FortiManager 7\.4\.3\. 7 new modules\.
* Supported FortiManager 7\.6\.0\. Added 7 new modules\.
* Supported ansible\-core 2\.17\.
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

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* Use a truncated exponential backoff algorithm when polling actions from the API\.
* load\_balancer\_status \- Add new filter to compute the status of a Load Balancer based on its targets\.
* server\_type\_info \- The \'included\_traffic\' return value is deprecated and will be set to \'None\' on 5 August 2024\. See [https\://docs\.hetzner\.cloud/changelog\#2024\-07\-25\-cloud\-api\-returns\-traffic\-information\-in\-different\-format](https\://docs\.hetzner\.cloud/changelog\#2024\-07\-25\-cloud\-api\-returns\-traffic\-information\-in\-different\-format)\.

<a id="ibm-storage-virtualize"></a>
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

<a id="junipernetworks-junos-1"></a>
#### junipernetworks\.junos

* Add implementation to gather ether\-channels for gig\-ether\-options\.
* Added support for virtual\-switch instances\.
* Based on ether\-option\-type create supported commands for config module\.
* Implemented bridge\-domains configuration management for routing instances\.
* Implemented support for setting the Maximum Transmission Unit \(MTU\) in Layer 3 \(L3\) Internet Protocol \(IP\) interfaces\.
* Tested successfully on Junos MX204\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* inventory/k8s\.py \- Defer removal of k8s inventory plugin to version 5\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/723](https\://github\.com/ansible\-collections/kubernetes\.core/pull/723)\)\.
* inventory/k8s\.py \- Defer removal of k8s inventory plugin to version 6\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/734](https\://github\.com/ansible\-collections/kubernetes\.core/pull/734)\)\.
* k8s \- The module and K8sService were changed so warnings returned by the K8S API are now displayed to the user\.

<a id="microsoft-ad"></a>
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

<a id="netapp-ontap"></a>
#### netapp\.ontap

* all modules supporting ZAPI \& REST \- throw authentication error instead of falling back to ZAPI when username/password is incorrect\.
* na\_ontap\_bgp\_peer\_group \- added new option <em class="title-reference">use\_peer\_as\_next\_hop</em>\, requires ONTAP 9\.9 or later\.
* na\_ontap\_cifs \- added REST support for option <em class="title-reference">vscan\_fileop\_profile</em>\, requires ONTAP 9\.15\.1 or later\.
* na\_ontap\_rest\_cli \- return command output for GET and OPTIONS verbs during check mode\.
* na\_ontap\_security\_key\_manager \- added warning message in REST when passphrase is not changed\.
* na\_ontap\_snapshot\_policy \- new option <em class="title-reference">retention\_period</em> added in REST\, requires ONTAP 9\.12 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">activity\_tracking</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_volume \- new option <em class="title-reference">snapshot\_locking</em> added in REST\, requires ONTAP 9\.12 or later\.

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
* cs\_project \- Extended to pass <code>cleanup\=true</code> to the deleteProject API when deleting a project \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/122](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/122)\)\.

<a id="purestorage-flasharray"></a>
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

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* all \- add <code>disable\_warnings</code> parameters
* purefb\_bucket \- Add <code>safemode</code> option for <code>retention\_mode</code>
* purefb\_certs \- Update module to use REST v2 code\. This brings in new parameters for certificate management\.
* purefb\_fs \- Set default for group\_ownership to be creator
* purefb\_ra \- Add <code>duration</code> option from REST 2\.14
* purefb\_ra \- Update to REST2

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* content\_export\_\* \- document that <code>chunk\_size\_gb</code> parameter is only applicable for <code>importable</code> exports \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1738](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1738)\)
* lifecycle\_environments role \- allow setting <code>state</code> for the LCE\, allowing deletion of existing ones
* location\, locations role \- add <code>description</code> parameter to set the description
* redhat\_manifest \- report <code>changed</code> when manifest is regenerated and downloaded \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1473](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1473)\)

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

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

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-2"></a>
#### Ansible\-core

* Stopped wrapping all commands sent over SSH on a Windows target with a <code>powershell\.exe</code> executable\. This results in one less process being started on each command for Windows to improve efficiency\, simplify the code\, and make <code>raw</code> an actual raw command run with the default shell configured on the Windows sshd settings\. This should have no affect on most tasks except for <code>raw</code> which now is not guaranteed to always be running in a PowerShell shell and from having the console output codepage set to UTF\-8\. To avoid this issue either swap to using <code>ansible\.windows\.win\_command</code>\, <code>ansible\.windows\.win\_shell</code>\, <code>ansible\.windows\.win\_powershell</code> or manually wrap the raw command with the shell commands needed to set the output console encoding\.
* assert \- Nested templating may result in an inability for the conditional to be evaluated\. See the porting guide for more information\.
* persistent connection plugins \- The <code>ANSIBLE\_CONNECTION\_PATH</code> config option no longer has any effect\.

<a id="community-mysql-1"></a>
#### community\.mysql

* collection \- support of mysqlclient connector is deprecated \- use PyMySQL connector instead\! We will stop testing against it in collection version 4\.0\.0 and remove the related code in 5\.0\.0 \([https\://github\.com/ansible\-collections/community\.mysql/issues/654](https\://github\.com/ansible\-collections/community\.mysql/issues/654)\)\.
* mysql\_info \- The <code>users\_info</code> filter returned variable <code>plugin\_auth\_string</code> contains the hashed password and it\'s misleading\, it will be removed from community\.mysql 4\.0\.0\. Use the <em class="title-reference">plugin\_hash\_string</em> return value instead \([https\://github\.com/ansible\-collections/community\.mysql/pull/629](https\://github\.com/ansible\-collections/community\.mysql/pull/629)\)\.
* mysql\_user \- the <code>user</code> alias of the <code>name</code> argument has been deprecated and will be removed in collection version 5\.0\.0\. Use the <code>name</code> argument instead\.

<a id="community-vmware-2"></a>
#### community\.vmware

* Adding a dependency on the <code>vmware\.vmware</code> collection \([https\://github\.com/ansible\-collections/community\.vmware/pull/2159](https\://github\.com/ansible\-collections/community\.vmware/pull/2159)\)\.
* Depending on <code>vmware\-vcenter</code> and <code>vmware\-vapi\-common\-client</code> instead of <code>https\://github\.com/vmware/vsphere\-automation\-sdk\-python\.git</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2163](https\://github\.com/ansible\-collections/community\.vmware/pull/2163)\)\.
* Dropping support for pyVmomi \< 8\.0\.3\.0\.1 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2163](https\://github\.com/ansible\-collections/community\.vmware/pull/2163)\)\.
* Module utils \- Removed <code>vmware\.run\_command\_in\_guest\(\)</code> \([https\://github\.com/ansible\-collections/community\.vmware/pull/2175](https\://github\.com/ansible\-collections/community\.vmware/pull/2175)\)\.
* Removed support for ansible\-core version \< 2\.17\.0\.
* vmware\_dvs\_portgroup \- Removed <code>security\_override</code> alias for <code>mac\_management\_override</code> and support for <code>securityPolicyOverrideAllowed</code> which has been deprected in the vSphere API \([https\://github\.com/ansible\-collections/community\.vmware/issues/1998](https\://github\.com/ansible\-collections/community\.vmware/issues/1998)\)\.
* vmware\_dvs\_portgroup\_info \- Removed <code>security\_override</code> because it\'s deprecated in the vSphere API \([https\://github\.com/ansible\-collections/community\.vmware/issues/1998](https\://github\.com/ansible\-collections/community\.vmware/issues/1998)\)\.
* vmware\_guest\_tools\_info \- Removed deprecated <code>vm\_tools\_install\_status</code> from the result \([https\://github\.com/ansible\-collections/community\.vmware/issues/2078](https\://github\.com/ansible\-collections/community\.vmware/issues/2078)\)\.

<a id="community-zabbix-2"></a>
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

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* Drop support for ansible\-core 2\.14\.

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* Remove support for <code>ansible\-core\<2\.15</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/737](https\://github\.com/ansible\-collections/kubernetes\.core/pull/737)\)\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* Removing any support for ansible\-core \<\=2\.14

<a id="deprecated-features"></a>
### Deprecated Features

<a id="ansible-core-3"></a>
#### Ansible\-core

* Deprecate <code>ansible\.module\_utils\.basic\.AnsibleModule\.safe\_eval</code> and <code>ansible\.module\_utils\.common\.safe\_eval</code> as they are no longer used\.
* persistent connection plugins \- The <code>ANSIBLE\_CONNECTION\_PATH</code> config option no longer has any effect\, and will be removed in a future release\.
* yum\_repository \- deprecate <code>async</code> option as it has been removed in RHEL 8 and will be removed in ansible\-core 2\.22\.
* yum\_repository \- the following options are deprecated\: <code>deltarpm\_metadata\_percentage</code>\, <code>gpgcakey</code>\, <code>http\_caching</code>\, <code>keepalive</code>\, <code>metadata\_expire\_filter</code>\, <code>mirrorlist\_expire</code>\, <code>protect</code>\, <code>ssl\_check\_cert\_permissions</code>\, <code>ui\_repoid\_vars</code> as they have no effect for dnf as an underlying package manager\. The options will be removed in ansible\-core 2\.22\.

<a id="amazon-aws-1"></a>
#### amazon\.aws

* iam\_role \- support for creating and deleting IAM instance profiles using the <code>create\_instance\_profile</code> and <code>delete\_instance\_profile</code> options has been deprecated and will be removed in a release after 2026\-05\-01\.  To manage IAM instance profiles the <code>amazon\.aws\.iam\_instance\_profile</code> module can be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2221](https\://github\.com/ansible\-collections/amazon\.aws/pull/2221)\)\.

<a id="cisco-ios-2"></a>
#### cisco\.ios

* ios\_bgp\_address\_family \- deprecated attribute password in favour of password\_options within neigbhors\.
* ios\_bgp\_global \- deprecated attributes aggregate\_address\, bestpath\, inject\_map\, ipv4\_with\_subnet\, ipv6\_with\_subnet\, nopeerup\_delay\, distribute\_list\, address\, tag\, ipv6\_addresses\, password\, route\_map\, route\_server\_context and scope
* ios\_linkagg \- deprecate legacy module ios\_linkagg
* ios\_lldp \- deprecate legacy module ios\_lldp

<a id="community-docker-1"></a>
#### community\.docker

* The collection deprecates support for all ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-general-1"></a>
#### community\.general

* CmdRunner module util \- setting the value of the <code>ignore\_none</code> parameter within a <code>CmdRunner</code> context is deprecated and that feature should be removed in community\.general 12\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8479](https\://github\.com/ansible\-collections/community\.general/pull/8479)\)\.
* MH decorator cause\_changes module utils \- deprecate parameters <code>on\_success</code> and <code>on\_failure</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8791](https\://github\.com/ansible\-collections/community\.general/pull/8791)\)\.
* git\_config \- the <code>list\_all</code> option has been deprecated and will be removed in community\.general 11\.0\.0\. Use the <code>community\.general\.git\_config\_info</code> module instead \([https\://github\.com/ansible\-collections/community\.general/pull/8453](https\://github\.com/ansible\-collections/community\.general/pull/8453)\)\.
* git\_config \- using <code>state\=present</code> without providing <code>value</code> is deprecated and will be disallowed in community\.general 11\.0\.0\. Use the <code>community\.general\.git\_config\_info</code> module instead to read a value \([https\://github\.com/ansible\-collections/community\.general/pull/8453](https\://github\.com/ansible\-collections/community\.general/pull/8453)\)\.
* pipx \- support for versions of the command line tool <code>pipx</code> older than <code>1\.7\.0</code> is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.
* pipx\_info \- support for versions of the command line tool <code>pipx</code> older than <code>1\.7\.0</code> is deprecated and will be removed in community\.general 11\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/8793](https\://github\.com/ansible\-collections/community\.general/pull/8793)\)\.

<a id="community-grafana-1"></a>
#### community\.grafana

* Deprecate <em class="title-reference">grafana\_notification\_channel</em>\. It will be removed in version 3\.0\.0

<a id="community-routeros-1"></a>
#### community\.routeros

* The collection deprecates support for all Ansible/ansible\-base/ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-sops-1"></a>
#### community\.sops

* The collection deprecates support for all Ansible/ansible\-base/ansible\-core versions that are currently End of Life\, [according to the ansible\-core support matrix](https\://docs\.ansible\.com/ansible\-core/devel/reference\_appendices/release\_and\_maintenance\.html\#ansible\-core\-support\-matrix)\. This means that the next major release of the collection will no longer support Ansible 2\.9\, ansible\-base 2\.10\, ansible\-core 2\.11\, ansible\-core 2\.12\, ansible\-core 2\.13\, and ansible\-core 2\.14\.

<a id="community-vmware-3"></a>
#### community\.vmware

* vmware\_cluster \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2143](https\://github\.com/ansible\-collections/community\.vmware/pull/2143)\)\.
* vmware\_cluster\_drs \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2136](https\://github\.com/ansible\-collections/community\.vmware/pull/2136)\)\.
* vmware\_cluster\_vcls \- the module has been deprecated and will be removed in community\.vmware 6\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2156](https\://github\.com/ansible\-collections/community\.vmware/pull/2156)\)\.

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The <code>inspur\.sm</code> collection was considered unmaintained and has been removed from Ansible 11 \([https\://forum\.ansible\.com/t/2854](https\://forum\.ansible\.com/t/2854)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install inspur\.sm</code>\.
* The <code>netapp\.storagegrid</code> collection was considered unmaintained and has been removed from Ansible 11 \([https\://forum\.ansible\.com/t/2811](https\://forum\.ansible\.com/t/2811)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install netapp\.storagegrid</code>\.
* The collection <code>t\_systems\_mms\.icinga\_director</code> has been completely removed from Ansible\.
  It has been renamed to <code>telekom\_mms\.icinga\_director</code>\.
  <code>t\_systems\_mms\.icinga\_director</code> has been replaced by deprecated redirects to <code>telekom\_mms\.icinga\_director</code> in Ansible 9\.0\.0\.
  Please update your FQCNs from <code>t\_systems\_mms\.icinga\_director</code> to <code>telekom\_mms\.icinga\_director</code>\.
* The deprecated <code>frr\.frr</code> collection has been removed \([https\://forum\.ansible\.com/t/6243](https\://forum\.ansible\.com/t/6243)\)\.
* The deprecated <code>openvswitch\.openvswitch</code> collection has been removed \([https\://forum\.ansible\.com/t/6245](https\://forum\.ansible\.com/t/6245)\)\.

<a id="ansible-core-4"></a>
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

<a id="ansible-posix-2"></a>
#### ansible\.posix

* skippy \- Remove skippy pluglin as it is no longer supported\([https\://github\.com/ansible\-collections/ansible\.posix/issues/350](https\://github\.com/ansible\-collections/ansible\.posix/issues/350)\)\.

<a id="community-grafana-2"></a>
#### community\.grafana

* removed check and handling of mangled api key in <em class="title-reference">grafana\_dashboard</em> lookup
* removed deprecated <em class="title-reference">message</em> argument in <em class="title-reference">grafana\_dashboard</em>

<a id="community-okd-1"></a>
#### community\.okd

* k8s \- Support for <code>merge\_type\=json</code> has been removed in version 4\.0\.0\. Please use <code>kubernetes\.core\.k8s\_json\_patch</code> instead \([https\://github\.com/openshift/community\.okd/pull/226](https\://github\.com/openshift/community\.okd/pull/226)\)\.

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* k8s \- Support for <code>merge\_type\=json</code> has been removed in version 4\.0\.0\. Please use <code>kubernetes\.core\.k8s\_json\_patch</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/722](https\://github\.com/ansible\-collections/kubernetes\.core/pull/722)\)\.
* k8s\_exec \- the previously deprecated <code>result\.return\_code</code> return value has been removed\, consider using <code>result\.rc</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>K8sAnsibleMixin</code> class has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>configuration\_digest\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>get\_api\_client\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.
* module\_utils/common\.py \- the previously deprecated <code>unique\_string\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/726](https\://github\.com/ansible\-collections/kubernetes\.core/pull/726)\)\.

<a id="security-fixes"></a>
### Security Fixes

<a id="ansible-core-5"></a>
#### Ansible\-core

* templating \- Address issues where internal templating can cause unsafe variables to lose their unsafe designation \(CVE\-2023\-5764\)

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-6"></a>
#### Ansible\-core

* \-\> runas become \- Generate new token for the SYSTEM token to use for become\. This should result in the full SYSTEM token being used and problems starting the process that fails with <code>The process creation has been blocked</code>\.
* Add a version ceiling constraint for pypsrp to avoid potential breaking changes in the 1\.0\.0 release\.
* Add descriptions for <code>ansible\-galaxy install \-\-help\` and \`\`ansible\-galaxy role\|collection install \-\-help</code>\.
* Avoid truncating floats when casting into int\, as it can lead to truncation and unexpected results\. 0\.99999 will be 0\, not 1\.
* COLOR\_SKIP will not alter \"included\" events color display anymore\.
* Callbacks now correctly get the resolved connection plugin name as the connection used\.
* Darwin \- add unit tests for Darwin hardware fact gathering\.
* Fix <code>SemanticVersion\.parse\(\)</code> to store the version string so that <code>\_\_repr\_\_</code> reports it instead of <code>None</code> \([https\://github\.com/ansible/ansible/pull/83831](https\://github\.com/ansible/ansible/pull/83831)\)\.
* Fix a traceback when an environment variable contains certain special characters \([https\://github\.com/ansible/ansible/issues/83498](https\://github\.com/ansible/ansible/issues/83498)\)
* Fix an issue when setting a plugin name from an unsafe source resulted in <code>ValueError\: unmarshallable object</code> \([https\://github\.com/ansible/ansible/issues/82708](https\://github\.com/ansible/ansible/issues/82708)\)
* Fix an issue where registered variable was not available for templating in <code>loop\_control\.label</code> on skipped looped tasks \([https\://github\.com/ansible/ansible/issues/83619](https\://github\.com/ansible/ansible/issues/83619)\)
* Fix for <code>meta</code> tasks breaking host/fork affinity with <code>host\_pinned</code> strategy \([https\://github\.com/ansible/ansible/issues/83294](https\://github\.com/ansible/ansible/issues/83294)\)
* Fix handlers not being executed in lockstep using the linear strategy in some cases \([https\://github\.com/ansible/ansible/issues/82307](https\://github\.com/ansible/ansible/issues/82307)\)
* Fix rapid memory usage growth when notifying handlers using the <code>listen</code> keyword \([https\://github\.com/ansible/ansible/issues/83392](https\://github\.com/ansible/ansible/issues/83392)\)
* Fix the task attribute <code>resolved\_action</code> to show the FQCN instead of <code>None</code> when <code>action</code> or <code>local\_action</code> is used in the playbook\.
* Fix using <code>module\_defaults</code> with <code>local\_action</code>/<code>action</code> \([https\://github\.com/ansible/ansible/issues/81905](https\://github\.com/ansible/ansible/issues/81905)\)\.
* Fix using the current task\'s directory for looking up relative paths within roles \([https\://github\.com/ansible/ansible/issues/82695](https\://github\.com/ansible/ansible/issues/82695)\)\.
* Remove deprecated config options DEFAULT\_FACT\_PATH\, DEFAULT\_GATHER\_SUBSET\, and DEFAULT\_GATHER\_TIMEOUT in favor of setting <code>fact\_path</code>\, <code>gather\_subset</code> and <code>gather\_timeout</code> as <code>module\_defaults</code> for <code>ansible\.builtin\.setup</code>\.
  These will apply to both the <code>gather\_facts</code> play keyword\, and any <code>ansible\.builtin\.setup</code> tasks\.
  To configure these options only for the <code>gather\_facts</code> keyword\, set these options as play keywords also\.
* Set LANGUAGE environment variable is set to a non\-English locale \([https\://github\.com/ansible/ansible/issues/83608](https\://github\.com/ansible/ansible/issues/83608)\)\.
* <code>ansible\-galaxy install \-\-help</code> \- Fix the usage text and document that the requirements file passed to <code>\-r</code> can include collections and roles\.
* <code>ansible\-galaxy role install</code> \- update the default timeout to download archive URLs from 20 seconds to 60 \([https\://github\.com/ansible/ansible/issues/83521](https\://github\.com/ansible/ansible/issues/83521)\)\.
* <code>end\_host</code> \- fix incorrect return code when executing <code>end\_host</code> in the <code>rescue</code> section \([https\://github\.com/ansible/ansible/issues/83447](https\://github\.com/ansible/ansible/issues/83447)\)
* addressed issue of trailing text been ignored\, non\-ASCII characters are parsed\, enhance white space handling and fixed overly permissive issue of human\_to\_bytes filter\([https\://github\.com/ansible/ansible/issues/82075](https\://github\.com/ansible/ansible/issues/82075)\)
* ansible\-config will now properly template defaults before dumping them\.
* ansible\-doc \- fixed \"inicates\" typo in output
* ansible\-doc \- format top\-level descriptions with multiple paragraphs as multiple paragraphs\, instead of concatenating them \([https\://github\.com/ansible/ansible/pull/83155](https\://github\.com/ansible/ansible/pull/83155)\)\.
* ansible\-doc \- handle no\_fail condition for role\.
* ansible\-doc \- make colors configurable\.
* ansible\-galaxy collection install \- remove old installation info when installing collections \([https\://github\.com/ansible/ansible/issues/83182](https\://github\.com/ansible/ansible/issues/83182)\)\.
* ansible\-galaxy role install \- fix symlinks \([https\://github\.com/ansible/ansible/issues/82702](https\://github\.com/ansible/ansible/issues/82702)\, [https\://github\.com/ansible/ansible/issues/81965](https\://github\.com/ansible/ansible/issues/81965)\)\.
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
* dnf5 \- re\-introduce the <code>state\: installed</code> alias to <code>state\: present</code> \([https\://github\.com/ansible/ansible/issues/83960](https\://github\.com/ansible/ansible/issues/83960)\)
* dnf5 \- replace removed API calls
* ensure we have logger before we log when we have increased verbosity\.
* facts \- <em class="title-reference">support\_discard</em> now returns <em class="title-reference">0</em> if either <em class="title-reference">discard\_granularity</em> or <em class="title-reference">discard\_max\_hw\_bytes</em> is zero\; otherwise it returns the value of <em class="title-reference">discard\_granularity</em>\, as before \([https\://github\.com/ansible/ansible/pull/83480](https\://github\.com/ansible/ansible/pull/83480)\)\.
* facts \- add a generic detection for VMware in product name\.
* facts \- add facts about x86\_64 flags to detect microarchitecture \([https\://github\.com/ansible/ansible/issues/83331](https\://github\.com/ansible/ansible/issues/83331)\)\.
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
* vault \- handle vault password file value when it is directory \([https\://github\.com/ansible/ansible/issues/42960](https\://github\.com/ansible/ansible/issues/42960)\)\.
* vault\.is\_encrypted\_file is now optimized to be called in runtime and not for being called in tests
* vault\_encrypted test documentation\, name and examples have been fixed\, other parts were clarified
* winrm \- Add retry after exceeding commands per user quota that can occur in loops and action plugins running multiple commands\.

<a id="amazon-aws-2"></a>
#### amazon\.aws

* backup\_plan\_info \- Bugfix to enable getting info of all backup plans \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2083](https\://github\.com/ansible\-collections/amazon\.aws/pull/2083)\)\.
* cloudwatch\_metric\_alarm \- Fix idempotency when creating cloudwatch metric alarm without dimensions \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1865](https\://github\.com/ansible\-collections/amazon\.aws/pull/1865)\)\.
* ec2\_instance \- do not ignore IPv6 addresses when a single network interface is specified \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1979](https\://github\.com/ansible\-collections/amazon\.aws/pull/1979)\)\.
* ec2\_instance \- fix state processing when exact\_count is used \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1659](https\://github\.com/ansible\-collections/amazon\.aws/pull/1659)\)\.
* iam\_role \- fixes <code>EntityAlreadyExists</code> exception when <code>create\_instance\_profile</code> was set to <code>false</code> and the instance profile already existed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2102](https\://github\.com/ansible\-collections/amazon\.aws/issues/2102)\)\.
* iam\_role \- fixes issue where IAM instance profiles were created when <code>create\_instance\_profile</code> was set to <code>false</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2281](https\://github\.com/ansible\-collections/amazon\.aws/issues/2281)\)\.
* rds\_cluster \- Limit params sent to api call to DBClusterIdentifier when using state started or stopped \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2197](https\://github\.com/ansible\-collections/amazon\.aws/issues/2197)\)\.
* route53 \- modify the return value to return diff only when <code>module\.\_diff</code> is set to true \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2136](https\://github\.com/ansible\-collections/amazon\.aws/pull/2136)\)\.
* s3\_bucket \- catch <code>UnsupportedArgument</code> when calling API <code>GetBucketAccelerationConfig</code> on region where it is not supported \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2180](https\://github\.com/ansible\-collections/amazon\.aws/issues/2180)\)\.
* s3\_bucket \- change the default behaviour of the new <code>accelerate\_enabled</code> option to only update the configuration if explicitly passed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2220](https\://github\.com/ansible\-collections/amazon\.aws/issues/2220)\)\.
* s3\_bucket \- fixes <code>MethodNotAllowed</code> exceptions caused by fetching transfer acceleration state in regions that don\'t support it \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2266](https\://github\.com/ansible\-collections/amazon\.aws/issues/2266)\)\.
* s3\_bucket \- fixes <code>TypeError\: cannot unpack non\-iterable NoneType object</code> errors related to bucket versioning\, policies\, tags or encryption \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2228](https\://github\.com/ansible\-collections/amazon\.aws/pull/2228)\)\.
* s3\_object \- fixed issue which was causing <code>MemoryError</code> exceptions when downloading large files \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2107](https\://github\.com/ansible\-collections/amazon\.aws/issues/2107)\)\.

<a id="ansible-netcommon-2"></a>
#### ansible\.netcommon

* Fix get api call during scp with libssh\.
* Handle sftp error messages for file not present for routerOS\.
* The v6\.1\.2 release introduced a change in cliconfbase\'s edit\_config\(\) signature which broke many platform cliconfs\. This patch release reverts that change\.
* Updated the error message for the content\_templates parser to include the correct parser name and detailed error information\.

<a id="ansible-posix-3"></a>
#### ansible\.posix

* Bugfix in the documentation regarding the path option for authorised\_key\([https\://github\.com/ansible\-collections/ansible\.posix/issues/483](https\://github\.com/ansible\-collections/ansible\.posix/issues/483)\)\.
* seboolean \- make it work with disabled SELinux
* synchronize \- maintain proper formatting of the remote paths \([https\://github\.com/ansible\-collections/ansible\.posix/pull/361](https\://github\.com/ansible\-collections/ansible\.posix/pull/361)\)\.
* sysctl \- fix sysctl to work properly on symlinks \([https\://github\.com/ansible\-collections/ansible\.posix/issues/111](https\://github\.com/ansible\-collections/ansible\.posix/issues/111)\)\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* setup \- Better handle orphaned users when attempting to retrieve <code>ansible\_machine\_id</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/606](https\://github\.com/ansible\-collections/ansible\.windows/issues/606)
* setup \- Provide WMI/CIM fallback for facts that rely on SMBIOS when that is unavailable
* win\_owner \- Try to enable extra privileges if available to set the owner even when the caller may not have explicit rights to do so normally \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/633](https\://github\.com/ansible\-collections/ansible\.windows/issues/633)
* win\_powershell \- Fix up depth handling on <code>\$Ansible\.Result</code> when using a custom <code>executable</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/642](https\://github\.com/ansible\-collections/ansible\.windows/issues/642)
* win\_powershell \- increase open timeout for <code>executable</code> parameter to prevent exceptions on first\-run or slower targets\. \([https\://github\.com/ansible\-collections/ansible\.windows/issues/644](https\://github\.com/ansible\-collections/ansible\.windows/issues/644)\)\.
* win\_updates \- Base64 encode the update wrapper and payload to prevent locale\-specific encoding issues\.
* win\_updates \- Handle race condition when <code>Wait\-Process</code> did not handle when the process had ended \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/623](https\://github\.com/ansible\-collections/ansible\.windows/issues/623)

<a id="arista-eos-1"></a>
#### arista\.eos

* Ensure IPv6 static route definitions are correctly filtered during facts gathering\.
* This fix make sure to fetch timer with <em class="title-reference">lldp</em> string at the start\.
* Update integration tests for parse operations to ensure that ordering or address family \(AF\) does not affect assertions\.
* Update the filter to accurately retrieve relevant static route configurations\.

<a id="check-point-mgmt-1"></a>
#### check\_point\.mgmt

* module\_utils/checkpoint\.py \- Remove usage of CertificateError causing failures in ansible\-core 2\.17\.

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Remove duplicate alias name for attribute epg in aci\_epg\_subnet module

<a id="cisco-ios-3"></a>
#### cisco\.ios

* bgp\_global \- fix ebgp\_multihop recognnition and hop\_count settings
* ios\_acls \- fix incorrect mapping of port 135/udp to msrpc\.
* ios\_bgp\_address\_family \- Add support for maximum\-paths configuration\.
* ios\_bgp\_address\_family \- Add support for maximum\-secondary\-paths configuration\.
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

<a id="cisco-ise"></a>
#### cisco\.ise

* Added main\.yml to aws\_deployment role
* Update min\_ansible\_version to 2\.15\.0 in runtime\.yml and roles
* endpoint\_group \- add missing parameter parentID\.
* mnt\_session\_active\_list\_info \- fix response xml\.
* network\_device \- mask param can be string or int\, cast to int at the end\.
* reservation \- remove duplicate parameter\.
* support\_bundle\_download \- remove duplicate parameter\.
* trusted\_certificate \- fix comparison between request and current object\.

<a id="cisco-mso-1"></a>
#### cisco\.mso

* Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso\_schema\_template\_bd
* Fix to avoid making updates to attributes that are not provided which could lead to removal of configuration in mso\_schema\_template\_vrf
* Fix to be able to reference APIC only L3Out in mso\_schema\_site\_external\_epg

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* acls \- Fix lookup of range port conversion from int to string to allow strings \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/888](https\://github\.com/ansible\-collections/cisco\.nxos/pull/888)\)\.
* facts \- Fixes issue where the LLDP neighbor information returns an error when empty\.
* nxos\_l3\_interfaces \- fail if encapsulation exists on a different sub\-interface\.
* nxos\_snmp\_server \- correctly render entity traps \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/820](https\://github\.com/ansible\-collections/cisco\.nxos/issues/820)\)\.
* nxos\_static\_routes \- correctly generate command when track parameter is specified\.

<a id="community-crypto-1"></a>
#### community\.crypto

* When using cryptography \>\= 43\.0\.0\, use offset\-aware <code>datetime\.datetime</code> objects \(with timezone UTC\) instead of offset\-naive UTC timestamps for the <code>InvalidityDate</code> X\.509 CRL extension \([https\://github\.com/ansible\-collections/community\.crypto/issues/726](https\://github\.com/ansible\-collections/community\.crypto/issues/726)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/730](https\://github\.com/ansible\-collections/community\.crypto/pull/730)\)\.

<a id="community-dns"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker-2"></a>
#### community\.docker

* docker\_compose \- make sure that the module uses the <code>api\_version</code> parameter \([https\://github\.com/ansible\-collections/community\.docker/pull/881](https\://github\.com/ansible\-collections/community\.docker/pull/881)\)\.
* docker\_compose\_v2 \- handle yet another random unstructured error output from pre\-2\.29\.0 Compose versions \([https\://github\.com/ansible\-collections/community\.docker/issues/948](https\://github\.com/ansible\-collections/community\.docker/issues/948)\, [https\://github\.com/ansible\-collections/community\.docker/pull/949](https\://github\.com/ansible\-collections/community\.docker/pull/949)\)\.
* docker\_compose\_v2 \- make sure that services provided in <code>services</code> are appended to the command line after <code>\-\-</code> and not before it \([https\://github\.com/ansible\-collections/community\.docker/pull/942](https\://github\.com/ansible\-collections/community\.docker/pull/942)\)\.
* docker\_compose\_v2\* modules \- fix parsing of skipped pull messages for Docker Compose 2\.28\.x \([https\://github\.com/ansible\-collections/community\.docker/issues/911](https\://github\.com/ansible\-collections/community\.docker/issues/911)\, [https\://github\.com/ansible\-collections/community\.docker/pull/916](https\://github\.com/ansible\-collections/community\.docker/pull/916)\)\.
* docker\_compose\_v2\* modules \- there was no check to make sure that one of <code>project\_src</code> and <code>definition</code> is provided\. The modules crashed if none were provided \([https\://github\.com/ansible\-collections/community\.docker/issues/885](https\://github\.com/ansible\-collections/community\.docker/issues/885)\, [https\://github\.com/ansible\-collections/community\.docker/pull/886](https\://github\.com/ansible\-collections/community\.docker/pull/886)\)\.
* docker\_compose\_v2\* modules\, docker\_image\_build \- provide better error message when required fields are not present in <code>docker version</code> or <code>docker info</code> output\. This can happen if Podman is used instead of Docker \([https\://github\.com/ansible\-collections/community\.docker/issues/891](https\://github\.com/ansible\-collections/community\.docker/issues/891)\, [https\://github\.com/ansible\-collections/community\.docker/pull/935](https\://github\.com/ansible\-collections/community\.docker/pull/935)\)\.
* docker\_compose\_v2\*\, docker\_stack\*\, docker\_image\_build modules \- using <code>cli\_context</code> no longer leads to an invalid parameter combination being passed to the corresponding Docker CLI tool\, unless <code>docker\_host</code> is also provided\. Combining <code>cli\_context</code> and <code>docker\_host</code> is no longer allowed \([https\://github\.com/ansible\-collections/community\.docker/issues/892](https\://github\.com/ansible\-collections/community\.docker/issues/892)\, [https\://github\.com/ansible\-collections/community\.docker/pull/895](https\://github\.com/ansible\-collections/community\.docker/pull/895)\)\.
* docker\_container \- fix idempotency if <code>network\_mode\=default</code> and Docker 26\.1\.0 or later is used\. There was a breaking change in Docker 26\.1\.0 regarding normalization of <code>NetworkMode</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/934](https\://github\.com/ansible\-collections/community\.docker/issues/934)\, [https\://github\.com/ansible\-collections/community\.docker/pull/936](https\://github\.com/ansible\-collections/community\.docker/pull/936)\)\.
* docker\_container \- fix possible infinite loop if <code>removal\_wait\_timeout</code> is set \([https\://github\.com/ansible\-collections/community\.docker/pull/922](https\://github\.com/ansible\-collections/community\.docker/pull/922)\)\.
* docker\_container \- restore behavior of the module from community\.docker 2\.x\.y that passes the first network to the Docker Deamon while creating the container \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.
* docker\_image\_build \- fix <code>\-\-output</code> parameter composition for <code>type\=docker</code> and <code>type\=image</code> \([https\://github\.com/ansible\-collections/community\.docker/issues/946](https\://github\.com/ansible\-collections/community\.docker/issues/946)\, [https\://github\.com/ansible\-collections/community\.docker/pull/947](https\://github\.com/ansible\-collections/community\.docker/pull/947)\)\.
* docker\_prune \- fix handling of lists for the filter options \([https\://github\.com/ansible\-collections/community\.docker/issues/961](https\://github\.com/ansible\-collections/community\.docker/issues/961)\, [https\://github\.com/ansible\-collections/community\.docker/pull/966](https\://github\.com/ansible\-collections/community\.docker/pull/966)\)\.
* vendored Docker SDK for Python \- use <code>LooseVersion</code> instead of <code>StrictVersion</code> to compare urllib3 versions\. This is needed for development versions \([https\://github\.com/ansible\-collections/community\.docker/pull/902](https\://github\.com/ansible\-collections/community\.docker/pull/902)\)\.

<a id="community-general-2"></a>
#### community\.general

* bitwarden lookup plugin \- fix <code>KeyError</code> in <code>search\_field</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8549](https\://github\.com/ansible\-collections/community\.general/issues/8549)\, [https\://github\.com/ansible\-collections/community\.general/pull/8557](https\://github\.com/ansible\-collections/community\.general/pull/8557)\)\.
* git\_config \- fix behavior of <code>state\=absent</code> if <code>value</code> is present \([https\://github\.com/ansible\-collections/community\.general/issues/8436](https\://github\.com/ansible\-collections/community\.general/issues/8436)\, [https\://github\.com/ansible\-collections/community\.general/pull/8452](https\://github\.com/ansible\-collections/community\.general/pull/8452)\)\.
* gitlab\_group\_access\_token \- fix crash in check mode caused by attempted access to a newly created access token \([https\://github\.com/ansible\-collections/community\.general/pull/8796](https\://github\.com/ansible\-collections/community\.general/pull/8796)\)\.
* gitlab\_project \- fix <code>container\_expiration\_policy</code> not being applied when creating a new project \([https\://github\.com/ansible\-collections/community\.general/pull/8790](https\://github\.com/ansible\-collections/community\.general/pull/8790)\)\.
* gitlab\_project \- fix crash caused by old Gitlab projects not having a <code>container\_expiration\_policy</code> attribute \([https\://github\.com/ansible\-collections/community\.general/pull/8790](https\://github\.com/ansible\-collections/community\.general/pull/8790)\)\.
* gitlab\_project\_access\_token \- fix crash in check mode caused by attempted access to a newly created access token \([https\://github\.com/ansible\-collections/community\.general/pull/8796](https\://github\.com/ansible\-collections/community\.general/pull/8796)\)\.
* gitlab\_runner \- fix <code>paused</code> parameter being ignored \([https\://github\.com/ansible\-collections/community\.general/pull/8648](https\://github\.com/ansible\-collections/community\.general/pull/8648)\)\.
* homebrew\_cask \- fix <code>upgrade\_all</code> returns <code>changed</code> when nothing upgraded \([https\://github\.com/ansible\-collections/community\.general/issues/8707](https\://github\.com/ansible\-collections/community\.general/issues/8707)\, [https\://github\.com/ansible\-collections/community\.general/pull/8708](https\://github\.com/ansible\-collections/community\.general/pull/8708)\)\.
* keycloak\_clientscope \- remove IDs from clientscope and its protocol mappers on comparison for changed check \([https\://github\.com/ansible\-collections/community\.general/pull/8545](https\://github\.com/ansible\-collections/community\.general/pull/8545)\)\.
* keycloak\_realm \- add normalizations for <code>attributes</code> and <code>protocol\_mappers</code> \([https\://github\.com/ansible\-collections/community\.general/pull/8496](https\://github\.com/ansible\-collections/community\.general/pull/8496)\)\.
* keycloak\_realm\_key \- fix invalid usage of <code>parent\_id</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7850](https\://github\.com/ansible\-collections/community\.general/issues/7850)\, [https\://github\.com/ansible\-collections/community\.general/pull/8823](https\://github\.com/ansible\-collections/community\.general/pull/8823)\)\.
* keycloak\_user\_federation \- fix key error when removing mappers during an update and new mappers are specified in the module args \([https\://github\.com/ansible\-collections/community\.general/pull/8762](https\://github\.com/ansible\-collections/community\.general/pull/8762)\)\.
* keycloak\_user\_federation \- fix the <code>UnboundLocalError</code> that occurs when an ID is provided for a user federation mapper \([https\://github\.com/ansible\-collections/community\.general/pull/8831](https\://github\.com/ansible\-collections/community\.general/pull/8831)\)\.
* keycloak\_user\_federation \- get cleartext IDP <code>clientSecret</code> from full realm info to detect changes to it \([https\://github\.com/ansible\-collections/community\.general/issues/8294](https\://github\.com/ansible\-collections/community\.general/issues/8294)\, [https\://github\.com/ansible\-collections/community\.general/pull/8735](https\://github\.com/ansible\-collections/community\.general/pull/8735)\)\.
* keycloak\_user\_federation \- remove existing user federation mappers if they are not present in the federation configuration and will not be updated \([https\://github\.com/ansible\-collections/community\.general/issues/7169](https\://github\.com/ansible\-collections/community\.general/issues/7169)\, [https\://github\.com/ansible\-collections/community\.general/pull/8695](https\://github\.com/ansible\-collections/community\.general/pull/8695)\)\.
* keycloak\_user\_federation \- sort desired and after mapper list by name \(analog to before mapper list\) to minimize diff and make change detection more accurate \([https\://github\.com/ansible\-collections/community\.general/pull/8761](https\://github\.com/ansible\-collections/community\.general/pull/8761)\)\.
* launched \- correctly report changed status in check mode \([https\://github\.com/ansible\-collections/community\.general/pull/8406](https\://github\.com/ansible\-collections/community\.general/pull/8406)\)\.
* nsupdate \- fix \'index out of range\' error when changing NS records by falling back to authority section of the response \([https\://github\.com/ansible\-collections/community\.general/issues/8612](https\://github\.com/ansible\-collections/community\.general/issues/8612)\, [https\://github\.com/ansible\-collections/community\.general/pull/8614](https\://github\.com/ansible\-collections/community\.general/pull/8614)\)\.
* opennebula inventory plugin \- fix invalid reference to IP when inventory runs against NICs with no IPv4 address \([https\://github\.com/ansible\-collections/community\.general/pull/8489](https\://github\.com/ansible\-collections/community\.general/pull/8489)\)\.
* opentelemetry callback \- do not save the JSON response when using the <code>ansible\.builtin\.uri</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/8430](https\://github\.com/ansible\-collections/community\.general/pull/8430)\)\.
* opentelemetry callback \- do not save the content response when using the <code>ansible\.builtin\.slurp</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/8430](https\://github\.com/ansible\-collections/community\.general/pull/8430)\)\.
* paman \- do not fail if an empty list of packages has been provided and there is nothing to do \([https\://github\.com/ansible\-collections/community\.general/pull/8514](https\://github\.com/ansible\-collections/community\.general/pull/8514)\)\.
* proxmox \- fix idempotency on creation of mount volumes using Proxmox\' special <code>\<storage\>\:\<size\></code> syntax \([https\://github\.com/ansible\-collections/community\.general/issues/8407](https\://github\.com/ansible\-collections/community\.general/issues/8407)\, [https\://github\.com/ansible\-collections/community\.general/pull/8542](https\://github\.com/ansible\-collections/community\.general/pull/8542)\)\.
* proxmox \- fixed an issue where the new volume handling incorrectly converted <code>null</code> values into <code>\"None\"</code> strings \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox \- fixed an issue where volume strings where overwritten instead of appended to in the new <code>build\_volume\(\)</code> method \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox \- removed the forced conversion of non\-string values to strings to be consistent with the module documentation \([https\://github\.com/ansible\-collections/community\.general/pull/8646](https\://github\.com/ansible\-collections/community\.general/pull/8646)\)\.
* proxmox inventory plugin \- fixed a possible error on concatenating responses from proxmox\. In case an API call unexpectedly returned an empty result\, the inventory failed with a fatal error\. Added check for empty response \([https\://github\.com/ansible\-collections/community\.general/issues/8798](https\://github\.com/ansible\-collections/community\.general/issues/8798)\, [https\://github\.com/ansible\-collections/community\.general/pull/8794](https\://github\.com/ansible\-collections/community\.general/pull/8794)\)\.
* redfish\_utils module utils \- do not fail when language is not exactly \"en\" \([https\://github\.com/ansible\-collections/community\.general/pull/8613](https\://github\.com/ansible\-collections/community\.general/pull/8613)\)\.

<a id="community-grafana-3"></a>
#### community\.grafana

* Add missing function argument in <em class="title-reference">grafana\_contact\_point</em> for org handling
* Fix var prefixes in silence\-task in role
* Fixed check if grafana\_api\_key is defined for <em class="title-reference">grafana\_dashboard</em> lookup

<a id="community-hrobot"></a>
#### community\.hrobot

* boot \- use PHP array form encoding when sending multiple <code>authorized\_key</code> \([https\://github\.com/ansible\-collections/community\.hrobot/issues/112](https\://github\.com/ansible\-collections/community\.hrobot/issues/112)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/113](https\://github\.com/ansible\-collections/community\.hrobot/pull/113)\)\.

<a id="community-mysql-2"></a>
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

<a id="community-network"></a>
#### community\.network

* exos \- Add error handling of <code>Permission denied</code> errors \([https\://github\.com/ansible\-collections/community\.network/pull/571](https\://github\.com/ansible\-collections/community\.network/pull/571)\)\.

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgres \- psycopg2 automatically sets the datestyle on the connection to iso whenever it encounters a datestyle configuration it doesn\'t recognize\, but psycopg3 does not\. Fix now enforces iso datestyle when using psycopg3 \([https\://github\.com/ansible\-collections/community\.postgresql/issues/711](https\://github\.com/ansible\-collections/community\.postgresql/issues/711)\)\.
* postgresql\_db \- fix issues due to columns in pg\_database changing in Postgres 17\. \([https\://github\.com/ansible\-collections/community\.postgresql/issues/729](https\://github\.com/ansible\-collections/community\.postgresql/issues/729)\)\.
* postgresql\_info \- Use a server check that works on beta and rc versions as well as on actual releases\.
* postgresql\_user \- remove a comment from unit tests that breaks pre\-compile \([https\://github\.com/ansible\-collections/community\.postgresql/issues/737](https\://github\.com/ansible\-collections/community\.postgresql/issues/737)\)\.

<a id="community-proxysql-1"></a>
#### community\.proxysql

* module\_utils \- fix ProxySQL version parsing that fails when a suffix wasn\'t present in the version \([https\://github\.com/ansible\-collections/community\.proxysql/issues/154](https\://github\.com/ansible\-collections/community\.proxysql/issues/154)\)\.
* role\_proxysql \- Correct package name \(python3\-mysqldb instead of python\-mysqldb\) \([https\://github\.com/ansible\-collections/community\.proxysql/pull/89](https\://github\.com/ansible\-collections/community\.proxysql/pull/89)\)\.
* role\_proxysql \- Dynamic user/password in \.my\.cnf \([https\://github\.com/ansible\-collections/community\.proxysql/pull/89](https\://github\.com/ansible\-collections/community\.proxysql/pull/89)\)\.

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_modify\, api\_info \- change the default of <code>ingress\-filtering</code> in paths <code>interface bridge</code> and <code>interface bridge port</code> back to <code>false</code> for RouterOS before version 7 \([https\://github\.com/ansible\-collections/community\.routeros/pull/305](https\://github\.com/ansible\-collections/community\.routeros/pull/305)\)\.

<a id="community-sops-2"></a>
#### community\.sops

* Fix RPM URL for the 3\.9\.0 release \([https\://github\.com/ansible\-collections/community\.sops/pull/188](https\://github\.com/ansible\-collections/community\.sops/pull/188)\)\.
* Pass <code>config\_path</code> on SOPS 3\.9\.0 before the subcommand instead of after it \([https\://github\.com/ansible\-collections/community\.sops/issues/195](https\://github\.com/ansible\-collections/community\.sops/issues/195)\, [https\://github\.com/ansible\-collections/community\.sops/pull/197](https\://github\.com/ansible\-collections/community\.sops/pull/197)\)\.
* sops\_encrypt \- properly support <code>path\_regex</code> in <code>\.sops\.yaml</code> when SOPS 3\.9\.0 or later is used \([https\://github\.com/ansible\-collections/community\.sops/issues/153](https\://github\.com/ansible\-collections/community\.sops/issues/153)\, [https\://github\.com/ansible\-collections/community\.sops/pull/190](https\://github\.com/ansible\-collections/community\.sops/pull/190)\)\.

<a id="community-vmware-4"></a>
#### community\.vmware

* Document dependency on requests \([https\://github\.com/ansible\-collections/community\.vmware/issues/2127](https\://github\.com/ansible\-collections/community\.vmware/issues/2127)\)\.
* vcenter\_folder \- removed documentation that incorrectly said <em class="title-reference">folder\_type</em> had no effect when <em class="title-reference">parent\_folder</em> was set
* vmware\_all\_snapshots\_info \- fixed the datacenter parameter was ignored\([https\://github\.com/ansible\-collections/community\.vmware/pull/2165](https\://github\.com/ansible\-collections/community\.vmware/pull/2165)\)\.
* vmware\_cluster\_vcls \- fixed bug caused by pyvmomi \>\=7\.0\.3 returning the vlcs cluster config attribute as None when it was previously undefined\. Now if the vCLS config is not initialized on the cluster\, the module will initialize it using the user\'s desired state\.
* vmware\_guest\_disk \- round size to int\, supporting float values properly \([https\://github\.com/ansible\-collections/community\.vmware/issues/123](https\://github\.com/ansible\-collections/community\.vmware/issues/123)\)\.
* vmware\_guest\_snapshot \- Update documentation regarding snapshot\_id parameter \([https\://github\.com/ansible\-collections/community\.vmware/issues/2145](https\://github\.com/ansible\-collections/community\.vmware/issues/2145)\)\.
* vmware\_host\_logbundle \- Manifests previously was separared by \"\&\"\, thus selecting first manifest\. Fix now separates manifests with URL encoded space\, thus correctly supplying the manifests\.  \([https\://github\.com/ansible\-collections/community\.vmware/pull/2090](https\://github\.com/ansible\-collections/community\.vmware/pull/2090)\)\.

<a id="community-windows-1"></a>
#### community\.windows

* win\_mapped\_drive \- Use correct P/Invoke signature to fix mapped network drives on 32 Bit OS\.
* win\_mapped\_drive \- better handle failures when attempting to set mapped drive that already exists but was seen as a local path\.

<a id="community-zabbix-3"></a>
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
* Fix idempotency for empty values
* Fix idempotency for pod with 0\.0\.0\.0
* Fix idempotency for pods in case of systemd generation
* Fix idempotency for systemd generations
* Fix issue with pushing podman image to repo name and org
* Fix logic in Podman images
* Fix missing entries in network quadlet generated file
* Fix quadlet parameters for restart policy
* Fix quadlet parameters when container uses rootfs
* Fix transports issues in podman\_image
* Idempotency improvements
* fix for tls\_verify being ignored
* fix\(\#747\) set correct HealthCmd
* fix\(podman\_image\) \- skip empty volume items
* fix\(podman\_save\) \- always changed when force
* modify error and docs
* params gpus should be exit\_policy

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

<a id="dellemc-openmanage-2"></a>
#### dellemc\.openmanage

* Resolved the issue in <code>idrac\_certificates</code> module where subject\_alt\_name parameter was only accepting first item in list\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/584](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/584)\)
* Resolved the issue in <code>idrac\_reset</code> module where it fails when iDRAC is in busy state\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/652](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/652)\)
* Resolved the issue in <code>idrac\_virtual\_media</code> module where the Authorization request header was included in the request\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/612](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/612)\)
* Resolved the issue in <code>ome\_application\_certificate</code> module related to a padding error in generated CSR file\. \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/370](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/370)\)

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Added more description in the documentation\.
* Deleted 9 fmgr\_switchcontroller\_managedswitch\_\* modules\. Will support them in FortiManager Device Ansible\.
* Fixed Bug in \"fmgr\_fact\"
* Improved documentation\.
* Improved fmgr\_fact\, fmgr\_clone\, fmgr\_move\.

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fix some issues in sanity test\.
* Github issue
* mantis issue

<a id="google-cloud-1"></a>
#### google\.cloud

* ansible\-lint \- remove jinja templates from test assertions
* gcp\_kms\_filters \- add DOCUMENTATION string
* gcp\_secret\_manager \- make an f\-string usage backward compatible

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* server \- Keep <em class="title-reference">force\_upgrade</em> deprecated alias for another major version\.
* server \- Wait up to 30 minutes for every action returned from server create

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_callhome \- Added support to change a subset of proxy settings
* ibm\_svc\_manage\_callhome \- Setting censorcallhome does not work
* ibm\_svc\_utils \- REST API timeout due to slow response
* ibm\_svc\_utils \- Return correct error in case of error code 500

<a id="inspur-ispim"></a>
#### inspur\.ispim

* Change the ansible version in meta/runtime\.yml to 2\.15\.0\([https\://github\.com/ispim/inspur\.ispim/pull/37](https\://github\.com/ispim/inspur\.ispim/pull/37)\)\.
* Remove venv files that were accidentally bundled in 2\.2\.1 \([https\://github\.com/ispim/inspur\.ispim/pull/35](https\://github\.com/ispim/inspur\.ispim/pull/35)\)\.

<a id="junipernetworks-junos-2"></a>
#### junipernetworks\.junos

* Fix the lag\_interfaces facts for gigether supported model\.

<a id="kaytus-ksmanage"></a>
#### kaytus\.ksmanage

* Remove venv files that were accidentally bundled in 1\.2\.2\([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/23](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/23)\)\.

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* Resolve Collections util resource discovery fails when complex subresources present \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/676](https\://github\.com/ansible\-collections/kubernetes\.core/pull/676)\)\.
* align <em class="title-reference">helmdiff\_check\(\)</em> function commandline rendering with the <em class="title-reference">deploy\(\)</em> function \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/670](https\://github\.com/ansible\-collections/kubernetes\.core/pull/670)\)\.
* avoid unsafe conditions in integration tests \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/665](https\://github\.com/ansible\-collections/kubernetes\.core/pull/665)\)\.
* helm \- use <code>reuse\-values</code> when running <code>helm diff</code> command \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/680](https\://github\.com/ansible\-collections/kubernetes\.core/issues/680)\)\.
* integrations test helm\_kubeconfig \- set helm version to v3\.10\.3 to avoid incompatability with new bitnami charts \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/670](https\://github\.com/ansible\-collections/kubernetes\.core/pull/670)\)\.

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* fixed the expected type of the ip\_address\, subnet\_ip\, and subnet\_mask parameters to be lists instead of strings \(lowlydba\.sqlserver\.ag\_listener\)

<a id="microsoft-ad-1"></a>
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

<a id="netapp-ontap-1"></a>
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

<a id="netbox-netbox-1"></a>
#### netbox\.netbox

* Added ALLOWED\_QUERY\_PARAMS module\_bay by device [\#1228](https\://github\.com/netbox\-community/ansible\_modules/pull/1228)
* Added label to power outlet [\#1222](https\://github\.com/netbox\-community/ansible\_modules/pull/1222)
* Added power outlet type iec\-60320\-c21 to power outlet template and power outlet modules [\#1229](https\://github\.com/netbox\-community/ansible\_modules/issues/1229)
* Extend query param for parent\_location [\#1233](https\://github\.com/netbox\-community/ansible\_modules/issues/1233)
* If <em class="title-reference">fetch\_all</em> is <em class="title-reference">false</em>\, prefix lookup depends on site lookup\, so move it to secondary lookup \([https\://github\.com/netbox\-community/ansible\_modules/issues/733](https\://github\.com/netbox\-community/ansible\_modules/issues/733)\)

<a id="ngine-io-cloudstack-1"></a>
#### ngine\_io\.cloudstack

* Fixed a bug related to the new option <code>validate\_certs</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/135](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/135)\)\.

<a id="purestorage-flasharray-1"></a>
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

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_fs \- Fix conflict with SMB mode and ACL safeguarding
* purefb\_fs \- Fix error checking for SMB parameter in non\-SMB filesystem
* purefb\_info \- Fix space reporting issue

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* callback plugin \- correctly catch facts with vault data and replace it with <code>ENCRYPTED\_VAULT\_VALUE\_NOT\_REPORTED</code>\, preventing <code>Object of type AnsibleVaultEncryptedUnicode is not JSON serializable</code> errors
* redhat\_manifest \- do not send empty JSON bodies in GET requests which confuse the portal sometimes \([https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1768](https\://github\.com/theforeman/foreman\-ansible\-modules/issues/1768)\)

<a id="vmware-vmware-rest-2"></a>
#### vmware\.vmware\_rest

* README \- fixed various typos in documentation
* Removed the scenario guides which are pretty much unmaintained and\, therefor\, possibly outdated and misleading \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/524](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/524)\)\.
* lookup \- fixed issue where searching for datacenter contents would throw an exception instead of returning expected results

<a id="known-issues"></a>
### Known Issues

<a id="ansible-core-7"></a>
#### Ansible\-core

* ansible\-test \- When using ansible\-test containers with Podman on a Ubuntu 24\.04 host\, ansible\-test must be run as a non\-root user to avoid permission issues caused by AppArmor\.
* ansible\-test \- When using the Fedora 40 container with Podman on a Ubuntu 24\.04 host\, the <code>unix\-chkpwd</code> AppArmor profile must be disabled on the host to allow SSH connections to the container\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* libssh \- net\_put and net\_get fail when the destination file intended to be fetched is not present\.

<a id="community-docker-3"></a>
#### community\.docker

* docker\_container \- when specifying a MAC address for a container\'s network\, and the network is attached after container creation \(for example\, due to idempotency checks\)\, the MAC address is at least in some cases ignored by the Docker Daemon \([https\://github\.com/ansible\-collections/community\.docker/pull/933](https\://github\.com/ansible\-collections/community\.docker/pull/933)\)\.

<a id="community-general-3"></a>
#### community\.general

* homectl \- the module does not work under Python 3\.13 or newer\, since it relies on the removed <code>crypt</code> standard library module \([https\://github\.com/ansible\-collections/community\.general/issues/4691](https\://github\.com/ansible\-collections/community\.general/issues/4691)\, [https\://github\.com/ansible\-collections/community\.general/pull/8497](https\://github\.com/ansible\-collections/community\.general/pull/8497)\)\.
* udm\_user \- the module does not work under Python 3\.13 or newer\, since it relies on the removed <code>crypt</code> standard library module \([https\://github\.com/ansible\-collections/community\.general/issues/4690](https\://github\.com/ansible\-collections/community\.general/issues/4690)\, [https\://github\.com/ansible\-collections/community\.general/pull/8497](https\://github\.com/ansible\-collections/community\.general/pull/8497)\)\.

<a id="dellemc-openmanage-3"></a>
#### dellemc\.openmanage

* idrac\_diagnostics \- Issue\(285322\) \- This module doesn\'t support export of diagnostics file to HTTP and HTTPS share via SOCKS proxy\.
* idrac\_firmware \- Issue\(279282\) \- This module does not support firmware update using HTTP\, HTTPS\, and FTP shares with authentication on iDRAC8\.
* idrac\_storage\_volume \- Issue\(290766\) \- The module will report success instead of showing failure for new virtual creation on the BOSS\-N1 controller if a virtual disk is already present on the same controller\.
* idrac\_support\_assist \- Issue\(308550\) \- This module fails when the NFS share path contains sub directory\.
* ome\_diagnostics \- Issue\(279193\) \- Export of SupportAssist collection logs to the share location fails on OME version 4\.0\.0\.
* ome\_smart\_fabric\_uplink \- Issue\(186024\) \- The module supported by OpenManage Enterprise Modular\, however it does not allow the creation of multiple uplinks of the same name\. If an uplink is created using the same name as an existing uplink\, then the existing uplink is modified\.

<a id="new-plugins"></a>
### New Plugins

<a id="filter"></a>
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

<a id="new-modules"></a>
### New Modules

<a id="ansible-core-8"></a>
#### Ansible\-core

<a id="lib"></a>
##### Lib

<a id="ansible-modules"></a>
###### Ansible\.Modules

* ansible\.builtin\.mount\_facts \- Retrieve mount information\.

<a id="check-point-mgmt-2"></a>
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

<a id="community-general-4"></a>
#### community\.general

* community\.general\.bootc\_manage \- Bootc Switch and Upgrade\.
* community\.general\.consul\_agent\_check \- Add\, modify\, and delete checks within a consul cluster\.
* community\.general\.consul\_agent\_service \- Add\, modify and delete services within a consul cluster\.
* community\.general\.django\_check \- Wrapper for C\(django\-admin check\)\.
* community\.general\.django\_createcachetable \- Wrapper for C\(django\-admin createcachetable\)\.
* community\.general\.homebrew\_services \- Services manager for Homebrew\.
* community\.general\.keycloak\_realm\_keys\_metadata\_info \- Allows obtaining Keycloak realm keys metadata via Keycloak API\.
* community\.general\.keycloak\_userprofile \- Allows managing Keycloak User Profiles\.
* community\.general\.one\_vnet \- Manages OpenNebula virtual networks\.

<a id="community-grafana-4"></a>
#### community\.grafana

* community\.grafana\.grafana\_contact\_point \- Manage Grafana Contact Points

<a id="community-zabbix-4"></a>
#### community\.zabbix

* community\.zabbix\.zabbix\_mfa \- Create/update/delete Zabbix MFA method

<a id="containers-podman-3"></a>
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

<a id="dellemc-openmanage-4"></a>
#### dellemc\.openmanage

* dellemc\.openmanage\.ome\_session \- This module allows you to create and delete sessions on OpenManage Enterprise and OpenManage Enterprise Modular\.

<a id="fortinet-fortimanager-2"></a>
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

<a id="microsoft-ad-2"></a>
#### microsoft\.ad

* microsoft\.ad\.service\_account \- Manage Active Directory service account objects

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_permission \- Creates or removes permissions from NetBox
* netbox\.netbox\.netbox\_token \- Creates or removes tokens from NetBox
* netbox\.netbox\.netbox\_tunnel \- Create\, update or delete tunnels within NetBox
* netbox\.netbox\.netbox\_tunnel\_group \- Create\, update or delete tunnel groups within NetBox
* netbox\.netbox\.netbox\_user \- Creates or removes users from NetBox
* netbox\.netbox\.netbox\_user\_group \- Creates or removes user groups from NetBox

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_audits \- List FlashArray Audit Events
* purestorage\.flasharray\.purefa\_dsrole\_old \- Configure FlashArray Directory Service Roles \(pre\-6\.6\.3\)
* purestorage\.flasharray\.purefa\_sessions \- List FlashArray Sessions

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* theforeman\.foreman\.content\_import\_info \- List content imports
* theforeman\.foreman\.content\_import\_library \- Manage library content imports
* theforeman\.foreman\.content\_import\_repository \- Manage repository content imports
* theforeman\.foreman\.content\_import\_version \- Manage content view version content imports

<a id="unchanged-collections"></a>
### Unchanged Collections

* ansible\.utils \(still version 4\.1\.0\)
* chocolatey\.chocolatey \(still version 1\.5\.1\)
* cloud\.common \(still version 3\.0\.0\)
* community\.aws \(still version 8\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.9\)
* community\.hashi\_vault \(still version 6\.2\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.0\.1\)
* community\.libvirt \(still version 1\.3\.0\)
* community\.rabbitmq \(still version 1\.3\.0\)
* community\.sap\_libs \(still version 1\.4\.2\)
* dellemc\.unity \(still version 2\.0\.0\)
* ibm\.spectrum\_virtualize \(still version 2\.0\.0\)
* infinidat\.infinibox \(still version 1\.4\.5\)
* infoblox\.nios\_modules \(still version 1\.6\.1\)
* netapp\.cloudmanager \(still version 21\.22\.1\)
* netapp\_eseries\.santricity \(still version 1\.4\.0\)
* ngine\_io\.exoscale \(still version 1\.1\.0\)
* openstack\.cloud \(still version 2\.2\.0\)
* ovirt\.ovirt \(still version 3\.2\.0\)
* sensu\.sensu\_go \(still version 1\.14\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.1\.2\)
