# Ansible 14 Release Notes

This changelog describes changes since Ansible 13\.0\.0\.

- <a href="#v14-0-0a4">v14\.0\.0a4</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v14-0-0a3">v14\.0\.0a3</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated-1">Removed Features \(previously deprecated\)</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v14-0-0a2">v14\.0\.0a2</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#changed-collections-2">Changed Collections</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>
- <a href="#v14-0-0a1">v14\.0\.0a1</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide-2">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated-2">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-plugins-1">New Plugins</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="v14-0-0a4"></a>
## v14\.0\.0a4

- <a href="#release-summary">Release Summary</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#community-dns-1">community\.dns</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#community-dns-2">community\.dns</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#community-dns-3">community\.dns</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2026\-04\-29

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 14\.0\.0a4 contains ansible\-core version 2\.21\.0rc1\.
This is a newer version than version 2\.21\.0b3 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection         | Ansible 14.0.0a3 | Ansible 14.0.0a4 | Notes                                                                                                                        |
| ------------------ | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| azure.azcollection | 3.16.0           | 3.17.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| community.dns      | 3.5.4            | 4.0.0-b1         |                                                                                                                              |
| community.proxysql | 1.7.0            | 1.8.0            |                                                                                                                              |
| grafana.grafana    | 6.0.6            | 6.1.0            |                                                                                                                              |
| hetzner.hcloud     | 6.8.0            | 6.9.0            |                                                                                                                              |
| kubernetes.core    | 6.3.0            | 6.4.0            |                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Run molecule only when required by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/441](https\://github\.com/grafana/grafana\-ansible\-collection/pull/441)
* migrate stack create/update/delete to stacks\-api by \@KucicM in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/494](https\://github\.com/grafana/grafana\-ansible\-collection/pull/494)

<a id="minor-changes"></a>
### Minor Changes

<a id="community-dns"></a>
#### community\.dns

* Migrate codebase to Python 3 only \([https\://github\.com/ansible\-collections/community\.dns/pull/319](https\://github\.com/ansible\-collections/community\.dns/pull/319)\, [https\://github\.com/ansible\-collections/community\.dns/pull/320](https\://github\.com/ansible\-collections/community\.dns/pull/320)\, [https\://github\.com/ansible\-collections/community\.dns/pull/321](https\://github\.com/ansible\-collections/community\.dns/pull/321)\)\.

<a id="community-proxysql"></a>
#### community\.proxysql

* Add PostgreSQL support with the new <code>proxysql\_pgsql\_users</code>\, <code>proxysql\_pgsql\_servers</code>\, <code>proxysql\_pgsql\_hostgroup\_attributes</code>\, <code>proxysql\_pgsql\_query\_rules</code>\, <code>proxysql\_pgsql\_query\_rules\_fast\_routing</code>\, and <code>proxysql\_pgsql\_replication\_hostgroups</code> modules\.

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* primary\_ip \- Primary IP support upcoming <code>assignee\_type</code> behavior change\.
* server\_type\_info \- Added the Server Type Location <code>available</code> property to the return values \(<code>hcloud\_server\_type\_info\[\]\.locations\[\]\.available</code>\)\.
* server\_type\_info \- Added the Server Type Location <code>recommended</code> property to the return values \(<code>hcloud\_server\_type\_info\[\]\.locations\[\]\.recommended</code>\)\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* helm\_info \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_plugin \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_plugin\_info \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_pull \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_registry\_auth \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_registry\_auth \- add new option plain\_http to allow insecure http connection when running <code>helm registry login</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1090](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1090)\)\.
* helm\_repository \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* k8s\_drain \- Add support for <code>check\_mode</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1086](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1086)\)\.
* k8s\_drain \- Convert module warnings into informational displays when users explicitly request the deletion of unmanaged pods\, pods with local storage\, or those managed by a <code>DaemonSet</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1037](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1037)\)\.

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="community-dns-1"></a>
#### community\.dns

* Ansible\-core versions before 2\.17 are no longer supported by the collection\. This also means that all Python versions before 3\.8 are no longer supported \([https\://github\.com/ansible\-collections/community\.dns/pull/317](https\://github\.com/ansible\-collections/community\.dns/pull/317)\)\.

<a id="deprecated-features"></a>
### Deprecated Features

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* datacenter\_info \- The <code>hcloud\_datacenter\_info\[\]\.server\_types</code> return value is deprecated and will be removed after 1 October 2026\. Please use the <code>hcloud\_server\_type\_info\[\]\.locations\[\]\.available</code> return value instead\.

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

<a id="community-dns-2"></a>
#### community\.dns

* Drop support for dnspython \< 2\.0\.0\. All modules and plugins that require dnspython will no longer work with older versions \([https\://github\.com/ansible\-collections/community\.dns/pull/323](https\://github\.com/ansible\-collections/community\.dns/pull/323)\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-1"></a>
#### Ansible\-core

* git \- use the branch configured in <code>\.gitmodules</code> or the remote HEAD instead of hardcoding <code>master</code> when <code>track\_submodules\=yes</code> \([https\://github\.com/ansible/ansible/issues/77691](https\://github\.com/ansible/ansible/issues/77691)\)\.

<a id="community-dns-3"></a>
#### community\.dns

* Update Public Suffix List\.
* nameserver\_info\, nameserver\_record\_info\, wait\_for\_txt \- fix handling of DNSPython <code>Nameserver</code> objects when default resolver addresses are used \([https\://github\.com/ansible\-collections/community\.dns/pull/321](https\://github\.com/ansible\-collections/community\.dns/pull/321)\)\.

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* Helm \- Allow taking ownership of existing Kubernetes resources on the first installation of a Helm release\. Previously\, the <code>take\_ownership</code> parameter was always disabled during the initial install\, preventing resource adoption \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1034](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1034)\)\.

<a id="new-modules"></a>
### New Modules

<a id="community-proxysql-1"></a>
#### community\.proxysql

* community\.proxysql\.proxysql\_pgsql\_hostgroup\_attributes \- Manages PostgreSQL hostgroup attributes using the ProxySQL admin interface
* community\.proxysql\.proxysql\_pgsql\_query\_rules \- Modifies pgsql query rules using the proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_query\_rules\_fast\_routing \- Modifies query rules for fast routing policies using the proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_replication\_hostgroups \- Manages replication hostgroups using the proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_servers \- Adds or removes pgsql hosts from proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_users \- Adds or removes postgresql users from proxysql admin interface

<a id="unchanged-collections"></a>
### Unchanged Collections

* amazon\.aws \(still version 11\.2\.0\)
* ansible\.netcommon \(still version 8\.5\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.2\)
* ansible\.windows \(still version 3\.5\.0\)
* arista\.eos \(still version 12\.0\.1\)
* check\_point\.mgmt \(still version 6\.9\.0\)
* chocolatey\.chocolatey \(still version 1\.6\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.intersight \(still version 2\.18\.0\)
* cisco\.ios \(still version 11\.3\.0\)
* cisco\.iosxr \(still version 12\.2\.1\)
* cisco\.meraki \(still version 2\.23\.2\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.nxos \(still version 11\.1\.3\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.aws \(still version 11\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.clickhouse \(still version 2\.1\.0\)
* community\.crypto \(still version 3\.2\.0\)
* community\.docker \(still version 5\.2\.0\)
* community\.general \(still version 12\.6\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.2\.0\)
* community\.mongodb \(still version 1\.7\.12\)
* community\.mysql \(still version 4\.2\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 2\.0\.0\-beta1\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.routeros \(still version 3\.20\.0\)
* community\.sap\_libs \(still version 1\.7\.0\)
* community\.sops \(still version 2\.3\.0\)
* community\.vmware \(still version 6\.2\.0\)
* community\.windows \(still version 3\.1\.0\)
* community\.zabbix \(still version 4\.2\.0\)
* containers\.podman \(still version 1\.19\.2\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.39\)
* dellemc\.enterprise\_sonic \(still version 4\.1\.0\)
* dellemc\.openmanage \(still version 10\.0\.2\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.13\.0\)
* fortinet\.fortios \(still version 2\.5\.1\)
* google\.cloud \(still version 1\.13\.0\)
* graphiant\.naas \(still version 26\.3\.0\)
* hitachivantara\.vspone\_block \(still version 4\.7\.0\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ibm\.storage\_virtualize \(still version 3\.3\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* kaytus\.ksmanage \(still version 4\.0\.0\)
* kubevirt\.core \(still version 2\.2\.4\)
* lowlydba\.sqlserver \(still version 2\.8\.1\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.4\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 2\.0\.1\)
* netbox\.netbox \(still version 3\.22\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* purestorage\.flasharray \(still version 1\.42\.0\)
* purestorage\.flashblade \(still version 1\.24\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 6\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* theforeman\.foreman \(still version 5\.11\.0\)
* vmware\.vmware \(still version 2\.8\.0\)
* vmware\.vmware\_rest \(still version 4\.10\.0\)
* vultr\.cloud \(still version 1\.14\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)

<a id="v14-0-0a3"></a>
## v14\.0\.0a3

- <a href="#release-summary-1">Release Summary</a>
- <a href="#ansible-core-2">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#splunk-es">splunk\.es</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#splunk-es-1">splunk\.es</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
- <a href="#breaking-changes--porting-guide-1">Breaking Changes / Porting Guide</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#hitachivantara-vspone-block-2">hitachivantara\.vspone\_block</a>
- <a href="#removed-features-previously-deprecated-1">Removed Features \(previously deprecated\)</a>
    - <a href="#hitachivantara-vspone-block-3">hitachivantara\.vspone\_block</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-dns-4">community\.dns</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#hitachivantara-vspone-block-4">hitachivantara\.vspone\_block</a>
    - <a href="#splunk-es-2">splunk\.es</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#filter">Filter</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#hitachivantara-vspone-block-5">hitachivantara\.vspone\_block</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2026\-04\-21

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core-2"></a>
### Ansible\-core

Ansible 14\.0\.0a3 contains ansible\-core version 2\.21\.0b3\.
This is a newer version than version 2\.21\.0b2 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                  | Ansible 14.0.0a2 | Ansible 14.0.0a3 | Notes |
| --------------------------- | ---------------- | ---------------- | ----- |
| cisco.iosxr                 | 12.1.1           | 12.2.1           |       |
| community.crypto            | 3.1.1            | 3.2.0            |       |
| community.dns               | 3.5.3            | 3.5.4            |       |
| community.general           | 12.5.0           | 12.6.0           |       |
| community.routeros          | 3.19.0           | 3.20.0           |       |
| community.sops              | 2.3.0-b1         | 2.3.0            |       |
| community.zabbix            | 4.1.1            | 4.2.0            |       |
| fortinet.fortios            | 2.5.0            | 2.5.1            |       |
| hitachivantara.vspone_block | 4.6.1            | 4.7.0            |       |
| splunk.es                   | 5.1.0            | 6.0.0            |       |
| theforeman.foreman          | 5.10.0           | 5.11.0           |       |

<a id="major-changes-1"></a>
### Major Changes

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Added a generic <em class="title-reference">headers</em> parameter to <em class="title-reference">fortios\_json\_generic</em> to support admin\-password confirmation headers and future custom request headers\.
* Updated FAQ to illustrate the use of <em class="title-reference">headers</em> in <em class="title-reference">fortios\_json\_generic</em> module\.
* Updated deprecated import of to\_text from ansible\.module\_utils\.\_text to the supported implementation\.

<a id="splunk-es"></a>
#### splunk\.es

* Remove dependency on the <code>ansible\.netcommon</code> collection\. Utility functions \(<code>remove\_empties</code>\, <code>dict\_diff</code>\, <code>dict\_merge</code>\) are now bundled locally\, and the httpapi plugin inherits directly from ansible\-core\'s <code>HttpApiBase</code>\.

<a id="minor-changes-1"></a>
### Minor Changes

<a id="ansible-core-3"></a>
#### Ansible\-core

* task results \- Python and Powershell modules do not include the <code>invocation</code> task result key by default\. Injection of the <code>invocation</code> task result key for Python and Powershell modules may be enabled with the var\-settable <code>INJECT\_INVOCATION</code> config item\. Most callbacks mask <code>invocation</code> when displaying a task or loop item result\.
* worker process \- When controller and forked child workers must share a TTY\, the <code>WORKER\_SESSION\_ISOLATION</code> config item can be set to <code>false</code> \(via variable/config/envvar\) to disable forked worker session isolation\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* iosxr\_l3\_interfaces \- Added support for <em class="title-reference">flow\.ipv4\.direction</em> and <em class="title-reference">flow\.ipv6\.direction</em> value <em class="title-reference">bidirectional</em>\. The module now expands bidirectional flow configuration into both ingress and egress IOS\-XR flow monitor commands\.

<a id="community-crypto"></a>
#### community\.crypto

* acme\_\* modules \- experimentally support <code>dns\-account\-01</code> challenge type according to [acme\-dns\-account\-label draft 02](https\://datatracker\.ietf\.org/doc/html/draft\-ietf\-acme\-dns\-account\-label\-02)\. Note that breaking changes to this challenge type can also happen in minor releases until the acme\-dns\-account\-label draft has been finalized as an RFC \([https\://github\.com/ansible\-collections/community\.crypto/pull/996](https\://github\.com/ansible\-collections/community\.crypto/pull/996)\)\.
* acme\_\* modules \- experimentally support <code>dns\-persist\-01</code> challenge type according to [acme\-dns\-persist draft 01](https\://www\.ietf\.org/archive/id/draft\-ietf\-acme\-dns\-persist\-01\.html)\. Note that breaking changes to this challenge type can also happen in minor releases until the acme\-dns\-persist draft has been finalized as an RFC \([https\://github\.com/ansible\-collections/community\.crypto/pull/997](https\://github\.com/ansible\-collections/community\.crypto/pull/997)\)\.

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

<a id="community-routeros"></a>
#### community\.routeros

* api\_info\, api\_modify \- add 46 new parameters to the <code>interface ethernet switch port</code> path for RouterOS \>\= 7\.15 \(CRS1xx/2xx variant\) including QoS\, mirroring\, VLAN\, and learning control parameters \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add <code>comment</code>\, <code>disabled</code>\, <code>independent\-learning</code>\, <code>qos\-group</code>\, <code>svl</code>\, and <code>switch</code> parameters to the <code>interface ethernet switch vlan</code> path for RouterOS \>\= 7\.15 \(CRS1xx/2xx variant\) \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
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

<a id="community-sops"></a>
#### community\.sops

* all modules and plugins \- allow retrieving private age keys and private SSH keys through commands with the new <code>age\_key\_cmd</code> and <code>age\_ssh\_private\_key\_cmd</code> options \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.
* all modules and plugins \- allow to configure GCP access with the <code>gcp\_oauth\_access\_token</code> and <code>gcp\_kms\_client\_type</code> options \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.
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

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Added a new \"hv\_gad\_bulk\" module for batch creation of multiple GAD pairs on VSP block storage systems\.
* Added a new \"hv\_hg\_bulk\" module for bulk host group management operations with multithreading support for parallel processing across multiple ports on VSP block storage systems\.
* Added a new \"hv\_hur\_bulk\" module for bulk creation of HUR pairs on VSP block storage systems\.
* Added a new \"hv\_iscsi\_target\_bulk\" module for bulk iSCSI target management operations with multithreading support for parallel processing across multiple ports on VSP block storage systems\.
* Added a new \"hv\_ldev\_bulk\" module for bulk operations on logical devices \(LDEVs\) on VSP block storage systems\.
* Added a new \"hv\_truecopy\_bulk\" module for bulk creation of TrueCopy pairs in VSP block storage systems\.
* Added new \"hv\_vsp\_create\_primary\_and\_secondary\_diskless\_quorum\_disk\" role for automated diskless quorum disk creation on VSP block storage systems\.
* Added new \"hv\_vsp\_create\_primary\_and\_secondary\_quorum\_disk\" role for automated disk\-based quorum disk creation on VSP block storage systems\.
* Added new \"hv\_vsp\_gad\_pairs\_creation\" role to automate GAD pairs provisioning on VSP block storage systems\.
* Added new \"hv\_vsp\_hur\_pairs\_creation\" role to automate HUR pairs provisioning on VSP block storage systems\.
* Added new \"hv\_vsp\_primary\_secondary\_journal\_creation\" role for automated journal creation on VSP block storage systems\.
* Added support for Ansible core version 2\.20\.
* Added support for SVOS 10\.5\.2 for VSP One B24/B26/B28 storage models\.
* Added support for SVOS 9\.8\.7 for VSP 5100/5500 \& VSP 5200/5600 storage models\.
* Added support for VSP One SDS Block version 1\.19\.00\.
* Added support for input parameter \"copy\_pace\" to the \"hv\_shadow\_image\_pair\"\, \"hv\_gad\"\, \"hv\_hur\"\, \"hv\_truecopy\"\, and \"hv\_journal\" modules\.
* Added support to \"hv\_ldev\" module to create ldev on a specific resource group\.
* Added support to \"hv\_resource\_group\" module to add multiple hostgroups by ids of a port to an existing Resource Group by ID\.
* Added support to \"hv\_resource\_group\" module to add multiple hostgroups by providing a range of IDs of a port to an existing Resource Group by ID\.
* Added support to \"hv\_resource\_group\" module to remove multiple hostgroups by ids of a port from an existing Resource Group by ID\.
* Added support to \"hv\_resource\_group\" module to remove multiple hostgroups by providing a range of IDs of a port from an existing Resource Group by ID\.
* Added support to \"hv\_storagepool\" module to stop the shrink operation of a storage pool\.

<a id="splunk-es-1"></a>
#### splunk\.es

* ci \- Add ansible\-core version matrix \(stable\-2\.16 through stable\-2\.21\) to the network integration test workflow\, aligning with the ITSI pattern\. Lower minimum supported ansible\-core version to 2\.16\.0\.

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* Support OAuth1 authentication by passing <code>oauth1\_consumer\_key</code> and <code>oauth1\_consumer\_secret</code> instead of <code>username</code> and <code>password</code>\.
* registration\_command \- add support for the setup\_container\_registry\_certs parameter \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1966](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1966)\)

<a id="breaking-changes--porting-guide-1"></a>
### Breaking Changes / Porting Guide

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

* Renamed the following input and output parameters in the \"hv\_gad\" module \- \"mu\_number\" to \"mirror\_unit\_number\"\.
* Renamed the following input and output parameters in the \"hv\_hg\" module \- \"nick\_name\" to \"nickname\"\, \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\, \"should\_delete\_all\_ldevs\" to \"should\_delete\_all\_volumes\"\.
* Renamed the following input and output parameters in the \"hv\_hg\_facts\" module \- \"nick\_name\" to \"nickname\"\, \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following input and output parameters in the \"hv\_hur\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\, \"primary\_journal\_pool\" to \"primary\_journal\_id\"\, \"secondary\_journal\_pool\" to \"secondary\_journal\_id\"\.
* Renamed the following input and output parameters in the \"hv\_iscsi\_target\" module \- \"nick\_name\" to \"nickname\"\, \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\, \"should\_delete\_all\_ldevs\" to \"should\_delete\_all\_volumes\"\.
* Renamed the following input and output parameters in the \"hv\_iscsi\_target\_facts\" module \- \"nick\_name\" to \"nickname\"\, \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following input and output parameters in the \"hv\_ldev\" module \- \"parity\_group\" to \"parity\_group\_id\"\.
* Renamed the following input and output parameters in the \"hv\_resource\_group\" module \- \"start\_ldev\" to \"begin\_ldev\_id\"\, \"end\_ldev\" to \"end\_ldev\_id\"\, \"parity\_groups\" to \"parity\_group\_ids\"\, \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following input and output parameters in the \"hv\_resource\_group\_facts\" module \- \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following input and output parameters in the \"hv\_sds\_block\_compute\_port\" module \- \"nick\_name\" to \"nickname\"\.
* Renamed the following input and output parameters in the \"hv\_sds\_block\_journal\" module \- \"mirror\_unit\" to \"mirror\_unit\_number\"\.
* Renamed the following input and output parameters in the \"hv\_sds\_block\_remote\_iscsi\_port\" module \- \"remote\_ip\_address\" to \"remote\_storage\_port\_ip\_address\"\.
* Renamed the following input and output parameters in the \"hv\_shadow\_image\_pair\" module \- \"pvol\_mu\_number\" to \"mirror\_unit\_number\" \, \"copy\_pace\_track\_size\" to \"copy\_pace\"\.
* Renamed the following input and output parameters in the \"hv\_snapshot\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\.
* Renamed the following input and output parameters in the \"hv\_snapshot\_group\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\.
* Renamed the following input and output parameters in the \"hv\_storage\_port\" module \- \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following input and output parameters in the \"hv\_storage\_port\_facts\" module \- \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following input and output parameters in the \"hv\_vsp\_one\_server\" module \- \"nick\_name\" to \"nickname\"\.
* Renamed the following input and output parameters in the \"hv\_vsp\_one\_server\_facts\" module \- \"nick\_name\" to \"nickname\"\.
* Renamed the following input and output parameters in the \"hv\_vsp\_one\_server\_hba\_facts\" module \- \"nick\_name\" to \"nickname\"\.
* Renamed the following output parameters in the \"hv\_gad\" module \- \"primary\_volume\_storage\_id\" to \"primary\_volume\_storage\_serial\_number\"\, \"secondary\_volume\_storage\_id\" to \"secondary\_volume\_storage\_serial\_number\"\.
* Renamed the following output parameters in the \"hv\_gad\_facts\" module \- \"primary\_volume\_storage\_id\" to \"primary\_volume\_storage\_serial\_number\"\, \"secondary\_volume\_storage\_id\" to \"secondary\_volume\_storage\_serial\_number\"\.
* Renamed the following output parameters in the \"hv\_hur\" module \- \"pvol\_status\" to \"primary\_volume\_status\"\, \"svol\_status\" to \"secondary\_volume\_status\"\, \"storage\_serial\_number\" to \"primary\_volume\_storage\_serial\_number\"\, \"secondary\_storage\_serial\" to \"secondary\_volume\_storage\_serial\_number\"\.
* Renamed the following output parameters in the \"hv\_hur\_facts\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\, \"primary\_journal\_pool\" to \"primary\_journal\_id\"\, \"secondary\_journal\_pool\" to \"secondary\_journal\_id\"\, \"pvol\_status\" to \"primary\_volume\_status\"\, \"svol\_status\" to \"secondary\_volume\_status\"\, \"primary\_storage\_serial\" to \"primary\_volume\_storage\_serial\_number\"\, \"secondary\_storage\_serial\" to \"secondary\_volume\_storage\_serial\_number\"\.
* Renamed the following output parameters in the \"hv\_ldev\_facts\" module \- \"parity\_group\" to \"parity\_group\_id\"\.
* Renamed the following output parameters in the \"hv\_resource\_group\_facts\" module \- \"start\_ldev\" to \"begin\_ldev\_id\"\, \"end\_ldev\" to \"end\_ldev\_id\"\, \"parity\_groups\" to \"parity\_group\_ids\"\, \"ports\" to \"port\_ids\"\, \"port\" to \"port\_id\"\.
* Renamed the following output parameters in the \"hv\_shadow\_image\_pair\_facts\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\, \"pvol\_host\_groups\" to \"primary\_volume\_host\_groups\"\, \"pvol\_iscsi\_targets\" to \"primary\_volume\_iscsi\_targets\"\, \"pvol\_nvm\_subsystem\_name\" to \"primary\_volume\_nvm\_subsystem\_name\"\, \"svol\_host\_groups\" to \"secondary\_volume\_host\_groups\"\, \"svol\_iscsi\_targets\" to \"secondary\_volume\_iscsi\_targets\"\, \"svol\_nvm\_subsystem\_name\" to \"secondary\_volume\_nvm\_subsystem\_name\"\.
* Renamed the following output parameters in the \"hv\_snapshot\_facts\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\, \"pvol\_host\_groups\" to \"primary\_volume\_host\_groups\"\, \"pvol\_iscsi\_targets\" to \"primary\_volume\_iscsi\_targets\"\, \"pvol\_nvm\_subsystem\_name\" to \"primary\_volume\_nvm\_subsystem\_name\"\, \"svol\_host\_groups\" to \"secondary\_volume\_host\_groups\"\, \"svol\_iscsi\_targets\" to \"secondary\_volume\_iscsi\_targets\"\, \"svol\_nvm\_subsystem\_name\" to \"secondary\_volume\_nvm\_subsystem\_name\"\, \"pvol\_processing\_status\" to \"primary\_volume\_processing\_status\"\, \"svol\_processing\_status\" to \"secondary\_volume\_processing\_status\"\.
* Renamed the following output parameters in the \"hv\_snapshot\_group\_facts\" module \- \"mirror\_unit\_id\" to \"mirror\_unit\_number\"\.
* Renamed the following output parameters in the \"hv\_truecopy\" module \- \"pvol\_status\" to \"primary\_volume\_status\"\, \"svol\_status\" to \"secondary\_volume\_status\"\, \"storage\_serial\_number\" to \"primary\_volume\_storage\_serial\_number\"\.
* Renamed the following output parameters in the \"hv\_truecopy\_facts\" module \- \"pvol\_status\" to \"primary\_volume\_status\"\, \"svol\_status\" to \"secondary\_volume\_status\"\, \"storage\_serial\_number\" to \"primary\_volume\_storage\_serial\_number\"\.
* Renamed the following output parameters in the \"hv\_vsp\_one\_volume\_facts\" module \- \"start\_volume\_id\" to \"begin\_volume\_id\"\.

<a id="deprecated-features-1"></a>
### Deprecated Features

<a id="ansible-core-4"></a>
#### Ansible\-core

* task result \- Inferred task failure from a non\-zero <code>rc</code> key and absence of a <code>failed</code> key will be deprecated in Ansible Core 2\.22\. Actions and modules must explicitly communicate failure by setting the <code>failed</code> key\, using APIs that do so\, or raising an unhandled exception\. In future releases\, the <code>rc</code> key will receive no special handling during task result processing\.

<a id="hitachivantara-vspone-block-2"></a>
#### hitachivantara\.vspone\_block

* The old parameter names renamed in this release are retained as aliases for backward compatibility but will be removed in the next major release\. Affected parameters across modules are \- \"start\_ldev\"\, \"end\_ldev\"\, \"parity\_groups\"\, \"ports\"\, \"port\" \(hv\_resource\_group\, hv\_resource\_group\_facts\)\, \"ports\"\, \"port\" \(hv\_storage\_port\, hv\_storage\_port\_facts\)\, \"mirror\_unit\" \(hv\_sds\_block\_journal\)\, \"nick\_name\"\, \"should\_delete\_all\_ldevs\" \(hv\_hg\, hv\_iscsi\_target\)\, \"nick\_name\" \(hv\_hg\_facts\, hv\_iscsi\_target\_facts\, hv\_sds\_block\_compute\_port\, hv\_vsp\_one\_server\, hv\_vsp\_one\_server\_facts\, hv\_vsp\_one\_server\_hba\_facts\)\, \"parity\_group\" \(hv\_ldev\, hv\_ldev\_facts\)\, \"remote\_ip\_address\" \(hv\_sds\_block\_remote\_iscsi\_port\)\, \"start\_volume\_id\" \(hv\_vsp\_one\_volume\_facts\)\, \"mirror\_unit\_id\"\, \"primary\_journal\_pool\"\, \"secondary\_journal\_pool\" \(hv\_hur\)\, \"mirror\_unit\_id\"\, \"pvol\_status\"\, \"svol\_status\"\, \"primary\_storage\_serial\"\, \"secondary\_storage\_serial\"\, \"primary\_journal\_pool\"\, \"secondary\_journal\_pool\" \(hv\_hur\_facts\)\, \"mu\_number\" \(hv\_gad\)\, \"pvol\_status\"\, \"svol\_status\"\, \"storage\_serial\_number\" \(hv\_truecopy\, hv\_truecopy\_facts\, hv\_hur\)\, \"secondary\_storage\_serial\" \(hv\_hur\)\, \"primary\_volume\_storage\_id\"\, \"secondary\_volume\_storage\_id\" \(hv\_gad\, hv\_gad\_facts\)\, \"mirror\_unit\_id\" \(hv\_snapshot\, hv\_snapshot\_group\, hv\_snapshot\_facts\, hv\_snapshot\_group\_facts\)\, \"pvol\_host\_groups\"\, \"pvol\_iscsi\_targets\"\, \"pvol\_nvm\_subsystem\_name\"\, \"svol\_host\_groups\"\, \"svol\_iscsi\_targets\"\, \"svol\_nvm\_subsystem\_name\"\, \"pvol\_processing\_status\"\, \"svol\_processing\_status\" \(hv\_snapshot\_facts\)\, \"pvol\_mu\_number\"\, \"copy\_pace\_track\_size\" \(hv\_shadow\_image\_pair\)\, \"mirror\_unit\_id\"\, \"pvol\_host\_groups\"\, \"pvol\_iscsi\_targets\"\, \"pvol\_nvm\_subsystem\_name\"\, \"svol\_host\_groups\"\, \"svol\_iscsi\_targets\"\, \"svol\_nvm\_subsystem\_name\" \(hv\_shadow\_image\_pair\_facts\)\.

<a id="removed-features-previously-deprecated-1"></a>
### Removed Features \(previously deprecated\)

<a id="hitachivantara-vspone-block-3"></a>
#### hitachivantara\.vspone\_block

* Removed playbooks \"ddp\_pool\.yml\" and \"ddp\_pool\_facts\.yml\"\.

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-core-5"></a>
#### Ansible\-core

* ansible\-test remote alias \- Alias values for <code>\-\-controller</code> and <code>\-\-target</code> are properly resolved for <code>remote</code>\. Previously\, remote alias values \(e\.g\. <code>fedora/latest</code>\) resolved to the correct name only for the legacy <code>\-\-remote</code> arg\, failing with an unknown image error for the newer args\.
* task results \- The <code>invocation</code> item result key omitted from registered values for looped task results\, unless enabled via <code>INJECT\_INVOCATION</code>\. Previously\, it was deleted from registered non\-loop results and only available to callbacks\.

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Fixed iosxr\_user module to correctly handle MD5 hashed passwords when updating user credentials\.

<a id="community-crypto-1"></a>
#### community\.crypto

* acme\_\* modules \- improve handling of authz deactivation\, and improve error message in case of bad authz states \([https\://github\.com/ansible\-collections/community\.crypto/pull/998](https\://github\.com/ansible\-collections/community\.crypto/pull/998)\)\.

<a id="community-dns-4"></a>
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

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fixed an issue where parameters ending with \_dict always returned changed\, even in check mode or when no changes were made\.
* Fixed an issue where some modules could not be configured globally\.
* Fixed an issue where the generate\-key\.system\.api\-user selector in the fortios\_monitor module required an admin password to function\.

<a id="hitachivantara-vspone-block-4"></a>
#### hitachivantara\.vspone\_block

* Fixed performance for \"hv\_snapshot\_group\_facts\" module\.

<a id="splunk-es-2"></a>
#### splunk\.es

* splunk\_finding\, splunk\_finding\_info \- Fix query by ref\_id failing to find findings due to sub\-second time precision mismatch\. The <code>earliest</code> time extracted from the ref\_id now includes a 1\-second buffer to ensure the finding falls within the search window\.

<a id="new-plugins"></a>
### New Plugins

<a id="filter"></a>
#### Filter

* community\.crypto\.acme\_dns\_persist\_record \- Craft a DNS record for ACME <code>dns\-persist\-01</code> challenges\.
* community\.crypto\.acme\_dns\_persist\_record\_parse \- Parse a DNS record for ACME <code>dns\-persist\-01</code> challenges\.

<a id="new-modules-1"></a>
### New Modules

<a id="community-general-2"></a>
#### community\.general

* community\.general\.snap\_connect \- Manages snap interface connections\.

<a id="hitachivantara-vspone-block-5"></a>
#### hitachivantara\.vspone\_block

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_gad\_bulk \- Manages batch GAD pairs on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_hg\_bulk \- Manages host groups in bulk on VSP block storage system with parallel processing\.
* hitachivantara\.vspone\_block\.hv\_iscsi\_target\_bulk \- Manages iscsi targets in bulk mode on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_ldev\_bulk \- Manages multiple logical devices \(LDEVs\) in bulk on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_truecopy\_bulk \- Manages bulk TrueCopy pairs on VSP block storage systems\.

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* amazon\.aws \(still version 11\.2\.0\)
* ansible\.netcommon \(still version 8\.5\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.utils \(still version 6\.0\.2\)
* ansible\.windows \(still version 3\.5\.0\)
* arista\.eos \(still version 12\.0\.1\)
* azure\.azcollection \(still version 3\.16\.0\)
* check\_point\.mgmt \(still version 6\.9\.0\)
* chocolatey\.chocolatey \(still version 1\.6\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.intersight \(still version 2\.18\.0\)
* cisco\.ios \(still version 11\.3\.0\)
* cisco\.meraki \(still version 2\.23\.2\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.nxos \(still version 11\.1\.3\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.aws \(still version 11\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.clickhouse \(still version 2\.1\.0\)
* community\.docker \(still version 5\.2\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.2\.0\)
* community\.mongodb \(still version 1\.7\.12\)
* community\.mysql \(still version 4\.2\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 2\.0\.0\-beta1\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.7\.0\)
* community\.vmware \(still version 6\.2\.0\)
* community\.windows \(still version 3\.1\.0\)
* containers\.podman \(still version 1\.19\.2\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.39\)
* dellemc\.enterprise\_sonic \(still version 4\.1\.0\)
* dellemc\.openmanage \(still version 10\.0\.2\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.13\.0\)
* google\.cloud \(still version 1\.13\.0\)
* grafana\.grafana \(still version 6\.0\.6\)
* graphiant\.naas \(still version 26\.3\.0\)
* hetzner\.hcloud \(still version 6\.8\.0\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ibm\.storage\_virtualize \(still version 3\.3\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* kaytus\.ksmanage \(still version 4\.0\.0\)
* kubernetes\.core \(still version 6\.3\.0\)
* kubevirt\.core \(still version 2\.2\.4\)
* lowlydba\.sqlserver \(still version 2\.8\.1\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.4\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 2\.0\.1\)
* netbox\.netbox \(still version 3\.22\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* purestorage\.flasharray \(still version 1\.42\.0\)
* purestorage\.flashblade \(still version 1\.24\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* vmware\.vmware \(still version 2\.8\.0\)
* vmware\.vmware\_rest \(still version 4\.10\.0\)
* vultr\.cloud \(still version 1\.14\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)

<a id="v14-0-0a2"></a>
## v14\.0\.0a2

- <a href="#release-summary-2">Release Summary</a>
- <a href="#ansible-core-6">Ansible\-core</a>
- <a href="#changed-collections-2">Changed Collections</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#community-routeros-2">community\.routeros</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#containers-podman-1">containers\.podman</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2026\-04\-14

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core-6"></a>
### Ansible\-core

Ansible 14\.0\.0a2 contains ansible\-core version 2\.21\.0b2\.
This is a newer version than version 2\.21\.0b1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-2"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection         | Ansible 14.0.0a1 | Ansible 14.0.0a2 | Notes                                                                                                                        |
| ------------------ | ---------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ansible.netcommon  | 8.4.0            | 8.5.0            |                                                                                                                              |
| ansible.utils      | 6.0.1            | 6.0.2            |                                                                                                                              |
| cisco.intersight   | 2.17.0           | 2.18.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.meraki       | 2.23.1           | 2.23.2           |                                                                                                                              |
| community.docker   | 5.1.0            | 5.2.0            |                                                                                                                              |
| community.routeros | 3.18.0           | 3.19.0           |                                                                                                                              |
| containers.podman  | 1.19.0           | 1.19.2           |                                                                                                                              |
| lowlydba.sqlserver | 2.7.0            | 2.8.1            |                                                                                                                              |

<a id="minor-changes-2"></a>
### Minor Changes

<a id="ansible-core-7"></a>
#### Ansible\-core

* ansible\-test \- Generate <code>dist\_info</code> when running tests\.
* ansible\-test \- Upgrade the distro\-specific test containers\.

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* The dependency on ansible\-pylibssh \(for ssh\_type\=libssh / network\_cli\) is now ansible\-pylibssh\>\=1\.4\.0 in requirements\.txt\, raised from the previous \>\=0\.2\.0 requirement\. Installations still on ansible\-pylibssh 0\.x or 1\.x below 1\.4\.0 must upgrade to use the libssh connection path with this collection release\.
* libssh connection \- When log\_path is set \(e\.g\. via ANSIBLE\_LOG\_PATH or log\_path in ansible\.cfg\)\, the plugin now routes ansible\-pylibssh \(libssh\) logs into the same Ansible log file\. Log level is derived from display\.verbosity using Python standard logging\: verbosity 0 \-\> WARNING\, 1\-2 \-\> INFO\, 3\+ \-\> DEBUG\. This allows SSH/libssh debug and trace output to appear in the configured log file for troubleshooting without changing ansible\-pylibssh configuration manually\.
* network\_cli \- The in\-collection paramiko path supports the same host key policy behavior \(including host\_key\_auto\_add and known\_hosts handling\) and persistent connection caching as the previous ansible\-core paramiko integration\.
* network\_cli \- When ssh\_type is set to paramiko\, the connection plugin now uses an in\-collection paramiko implementation instead of loading ansible\-core\'s paramiko connection plugin\. This allows network\_cli to work with versions of ansible\-core\, where the paramiko connection plugin was removed\.

<a id="community-docker"></a>
#### community\.docker

* docker\_image\_export \- adds <code>platform</code> parameter to allow exporting a specific platform variant from a multi\-arch image \([https\://github\.com/ansible\-collections/community\.docker/issues/1064](https\://github\.com/ansible\-collections/community\.docker/issues/1064)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1251](https\://github\.com/ansible\-collections/community\.docker/pull/1251)\)\.

<a id="community-routeros-1"></a>
#### community\.routeros

* api\_info \- add missing <code>numbers</code> parameter across numerous existing paths for RouterOS \>\= 7\.15\.2 \([https\://github\.com/ansible\-collections/community\.routeros/pull/458](https\://github\.com/ansible\-collections/community\.routeros/pull/458)\)\.
* api\_info \- add support for the <code>interface dot1x server active</code>\, <code>ip hotspot active</code>\, <code>ip ipsec active\-peers</code>\, <code>ip proxy cache\-contents</code>\, <code>ip socks connections</code>\, <code>user active</code>\, and <code>user\-manager session</code> paths as info\-only \(read\-only\) paths \([https\://github\.com/ansible\-collections/community\.routeros/pull/458](https\://github\.com/ansible\-collections/community\.routeros/pull/458)\)\.
* api\_info \- adds support for additional read\-only parameters in the <code>app</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- add <code>color</code> parameter to the <code>zerotier interface</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>current\-defaults</code> parameter to the <code>ip dns</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>mld\-datapath</code> parameter to the <code>interface wifi cap</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
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

<a id="containers-podman"></a>
#### containers\.podman

* Add \-\-platform option to podman\_image

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* user\_role \- Added <code>roles</code> parameter with <code>add</code>/<code>remove</code>/<code>set</code> pattern to manage multiple roles\. The existing <code>role</code> parameter is deprecated and will be removed in 3\.0\.0\. \(\#352\)

<a id="deprecated-features-2"></a>
### Deprecated Features

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* network\_cli \- The in\-collection paramiko support \(used when ssh\_type is paramiko\) is a compatibility layer for environments where ansible\-core\'s paramiko connection is no longer available\. This layer is deprecated and will be removed in a release after 2028\-02\-01\. Migrate to ssh\_type\=libssh by installing the ansible\-pylibssh package\.

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_modify \- all existing <code>numbers</code> fields are deprecated for writing and support for them will be removed in community\.routeros 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.routeros/pull/460](https\://github\.com/ansible\-collections/community\.routeros/pull/460)\)\.
* api\_modify \- in <code>routing bfd configuration</code>\, the fields <code>copy\-from</code> and <code>place\-before</code> are deprecated for writing and support for them will be removed in community\.routeros 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.routeros/pull/460](https\://github\.com/ansible\-collections/community\.routeros/pull/460)\)\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-8"></a>
#### Ansible\-core

* Fix <code>validate\_argspec</code> when tags are defined on the play\. The <code>always</code> tag is only added if the play has no tags\.
* <code>\-\-start\-at\-task</code> \- fix starting at the requested task instead of starting at the next block or play\. Play level tasks run first\. \([https\://github\.com/ansible/ansible/issues/86268](https\://github\.com/ansible/ansible/issues/86268)\)

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

<a id="cisco-meraki"></a>
#### cisco\.meraki

* devices\_switch\_ports \- Fixed AttributeError crash in <code>update\(\)</code> caused by <code>get\_object\_by\_name</code> returning the full port list instead of <code>None</code> when no port matched by name\. Added <code>isinstance\(prev\_obj\_name\, dict\)</code> guard to prevent calling <code>\.get\(\)</code> on a list\.
* devices\_switch\_ports \- Fixed idempotency regression where the module always reported <code>changed</code> due to <code>serial</code> \(a path parameter absent from the API response\) and <code>portId</code> \(int/string type mismatch\) being incorrectly included in the <code>requires\_update</code> comparison\.

<a id="containers-podman-1"></a>
#### containers\.podman

* podman\_container \- Fix quadlet\_options placement when restart\_policy is set
* podman\_network \- Add diff and idempotency to ip\_ranges in net\_config

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* amazon\.aws \(still version 11\.2\.0\)
* ansible\.posix \(still version 2\.1\.0\)
* ansible\.windows \(still version 3\.5\.0\)
* arista\.eos \(still version 12\.0\.1\)
* azure\.azcollection \(still version 3\.16\.0\)
* check\_point\.mgmt \(still version 6\.9\.0\)
* chocolatey\.chocolatey \(still version 1\.6\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.ios \(still version 11\.3\.0\)
* cisco\.iosxr \(still version 12\.1\.1\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.nxos \(still version 11\.1\.3\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.aws \(still version 11\.0\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.clickhouse \(still version 2\.1\.0\)
* community\.crypto \(still version 3\.1\.1\)
* community\.dns \(still version 3\.5\.3\)
* community\.general \(still version 12\.5\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.1\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.2\.0\)
* community\.mongodb \(still version 1\.7\.12\)
* community\.mysql \(still version 4\.2\.0\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 2\.0\.0\-beta1\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.7\.0\)
* community\.sops \(still version 2\.3\.0\-b1\)
* community\.vmware \(still version 6\.2\.0\)
* community\.windows \(still version 3\.1\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* cyberark\.conjur \(still version 1\.3\.9\)
* cyberark\.pas \(still version 1\.0\.39\)
* dellemc\.enterprise\_sonic \(still version 4\.1\.0\)
* dellemc\.openmanage \(still version 10\.0\.2\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* fortinet\.fortimanager \(still version 2\.13\.0\)
* fortinet\.fortios \(still version 2\.5\.0\)
* google\.cloud \(still version 1\.13\.0\)
* grafana\.grafana \(still version 6\.0\.6\)
* graphiant\.naas \(still version 26\.3\.0\)
* hetzner\.hcloud \(still version 6\.8\.0\)
* hitachivantara\.vspone\_block \(still version 4\.6\.1\)
* hitachivantara\.vspone\_object \(still version 1\.1\.1\)
* ibm\.storage\_virtualize \(still version 3\.3\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* kaytus\.ksmanage \(still version 4\.0\.0\)
* kubernetes\.core \(still version 6\.3\.0\)
* kubevirt\.core \(still version 2\.2\.4\)
* microsoft\.ad \(still version 1\.10\.0\)
* microsoft\.iis \(still version 1\.1\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.4\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 2\.0\.1\)
* netbox\.netbox \(still version 3\.22\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* purestorage\.flasharray \(still version 1\.42\.0\)
* purestorage\.flashblade \(still version 1\.24\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 5\.1\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* theforeman\.foreman \(still version 5\.10\.0\)
* vmware\.vmware \(still version 2\.8\.0\)
* vmware\.vmware\_rest \(still version 4\.10\.0\)
* vultr\.cloud \(still version 1\.14\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)

<a id="v14-0-0a1"></a>
## v14\.0\.0a1

- <a href="#release-summary-3">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core-9">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#chocolatey-chocolatey">chocolatey\.chocolatey</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#community-proxmox">community\.proxmox</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#fortinet-fortios-2">fortinet\.fortios</a>
    - <a href="#kaytus-ksmanage">kaytus\.ksmanage</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#splunk-es-3">splunk\.es</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
- <a href="#minor-changes-3">Minor Changes</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-dns-5">community\.dns</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-libvirt">community\.libvirt</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#community-proxmox-1">community\.proxmox</a>
    - <a href="#community-routeros-4">community\.routeros</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-6">hitachivantara\.vspone\_block</a>
    - <a href="#hitachivantara-vspone-object">hitachivantara\.vspone\_object</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#kaytus-ksmanage-1">kaytus\.ksmanage</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#microsoft-iis">microsoft\.iis</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#netapp-storagegrid">netapp\.storagegrid</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
    - <a href="#ovirt-ovirt">ovirt\.ovirt</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#splunk-es-4">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
- <a href="#breaking-changes--porting-guide-2">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#community-aws-2">community\.aws</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#splunk-es-5">splunk\.es</a>
- <a href="#deprecated-features-3">Deprecated Features</a>
    - <a href="#ansible-core-13">Ansible\-core</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#community-aws-3">community\.aws</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-proxmox-2">community\.proxmox</a>
    - <a href="#community-routeros-5">community\.routeros</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#removed-features-previously-deprecated-2">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-14">Ansible\-core</a>
    - <a href="#splunk-es-6">splunk\.es</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#amazon-aws-3">amazon\.aws</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#kubernetes-core-4">kubernetes\.core</a>
- <a href="#bugfixes-3">Bugfixes</a>
    - <a href="#ansible-core-15">Ansible\-core</a>
    - <a href="#amazon-aws-4">amazon\.aws</a>
    - <a href="#ansible-netcommon-4">ansible\.netcommon</a>
    - <a href="#ansible-utils-1">ansible\.utils</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-iosxr-2">cisco\.iosxr</a>
    - <a href="#cisco-meraki-2">cisco\.meraki</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-aws-4">community\.aws</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-dns-6">community\.dns</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-libvirt-1">community\.libvirt</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#community-proxmox-3">community\.proxmox</a>
    - <a href="#community-routeros-6">community\.routeros</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#containers-podman-4">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-3">fortinet\.fortios</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#hetzner-hcloud-4">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-7">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#inspur-ispim">inspur\.ispim</a>
    - <a href="#kaytus-ksmanage-2">kaytus\.ksmanage</a>
    - <a href="#kubernetes-core-5">kubernetes\.core</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#microsoft-iis-1">microsoft\.iis</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-1">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
    - <a href="#ovirt-ovirt-1">ovirt\.ovirt</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#splunk-es-7">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
    - <a href="#vultr-cloud-1">vultr\.cloud</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-routeros-7">community\.routeros</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
- <a href="#new-plugins-1">New Plugins</a>
    - <a href="#callback">Callback</a>
    - <a href="#filter-1">Filter</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#amazon-aws-5">amazon\.aws</a>
    - <a href="#ansible-windows-3">ansible\.windows</a>
    - <a href="#cisco-aci-2">cisco\.aci</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#cisco-mso-2">cisco\.mso</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#community-libvirt-2">community\.libvirt</a>
    - <a href="#community-proxmox-4">community\.proxmox</a>
    - <a href="#containers-podman-5">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-3">dellemc\.enterprise\_sonic</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#hitachivantara-vspone-block-8">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#kaytus-ksmanage-3">kaytus\.ksmanage</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-2">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
    - <a href="#splunk-es-8">splunk\.es</a>
    - <a href="#theforeman-foreman-3">theforeman\.foreman</a>
    - <a href="#vultr-cloud-2">vultr\.cloud</a>
- <a href="#unchanged-collections-3">Unchanged Collections</a>

<a id="release-summary-3"></a>
### Release Summary

Release Date\: 2026\-04\-07

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* awx\.awx \(previously included version\: 24\.6\.1\)
* cisco\.dnac \(previously included version\: 6\.41\.0\)
* junipernetworks\.junos \(previously included version\: 11\.0\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections"></a>
### Added Collections

* community\.clickhouse \(version 2\.1\.0\)
* graphiant\.naas \(version 26\.3\.0\)
* pcg\.alpaca\_operator \(version 2\.2\.0\)

<a id="ansible-core-9"></a>
### Ansible\-core

Ansible 14\.0\.0a1 contains ansible\-core version 2\.21\.0b1\.
This is a newer version than version 2\.20\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                   | Ansible 13.0.0 | Ansible 14.0.0a1 | Notes                                                                                                                                                                                                        |
| ---------------------------- | -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                   | 10.1.2         | 11.2.0           |                                                                                                                                                                                                              |
| ansible.netcommon            | 8.1.0          | 8.4.0            |                                                                                                                                                                                                              |
| ansible.utils                | 6.0.0          | 6.0.1            |                                                                                                                                                                                                              |
| ansible.windows              | 3.2.0          | 3.5.0            |                                                                                                                                                                                                              |
| arista.eos                   | 12.0.0         | 12.0.1           |                                                                                                                                                                                                              |
| azure.azcollection           | 3.10.1         | 3.16.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt             | 6.6.0          | 6.9.0            | The collection did not have a changelog in this version.                                                                                                                                                     |
| chocolatey.chocolatey        | 1.5.3          | 1.6.0            |                                                                                                                                                                                                              |
| cisco.aci                    | 2.12.0         | 2.13.0           |                                                                                                                                                                                                              |
| cisco.intersight             | 2.7.0          | 2.17.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.ios                    | 11.1.1         | 11.3.0           |                                                                                                                                                                                                              |
| cisco.iosxr                  | 12.1.0         | 12.1.1           |                                                                                                                                                                                                              |
| cisco.meraki                 | 2.21.8         | 2.23.1           |                                                                                                                                                                                                              |
| cisco.mso                    | 2.11.0         | 2.13.0           |                                                                                                                                                                                                              |
| cisco.nxos                   | 11.0.0         | 11.1.3           |                                                                                                                                                                                                              |
| cloudscale_ch.cloud          | 2.5.2          | 2.5.3            |                                                                                                                                                                                                              |
| community.aws                | 10.0.0         | 11.0.0           |                                                                                                                                                                                                              |
| community.clickhouse         |                | 2.1.0            | The collection was added to Ansible                                                                                                                                                                          |
| community.crypto             | 3.0.5          | 3.1.1            |                                                                                                                                                                                                              |
| community.dns                | 3.4.0          | 3.5.3            |                                                                                                                                                                                                              |
| community.docker             | 5.0.1          | 5.1.0            |                                                                                                                                                                                                              |
| community.general            | 12.0.1         | 12.5.0           |                                                                                                                                                                                                              |
| community.hrobot             | 2.7.0          | 2.7.1            |                                                                                                                                                                                                              |
| community.libvirt            | 2.0.0          | 2.2.0            |                                                                                                                                                                                                              |
| community.mongodb            | 1.7.10         | 1.7.12           | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.mysql              | 4.0.1          | 4.2.0            |                                                                                                                                                                                                              |
| community.postgresql         | 4.1.0          | 4.2.0            |                                                                                                                                                                                                              |
| community.proxmox            | 1.4.0          | 2.0.0-beta1      |                                                                                                                                                                                                              |
| community.routeros           | 3.13.0         | 3.18.0           |                                                                                                                                                                                                              |
| community.sap_libs           | 1.5.0          | 1.7.0            |                                                                                                                                                                                                              |
| community.sops               | 2.2.7          | 2.3.0-b1         |                                                                                                                                                                                                              |
| community.vmware             | 6.1.0          | 6.2.0            |                                                                                                                                                                                                              |
| community.windows            | 3.0.1          | 3.1.0            |                                                                                                                                                                                                              |
| containers.podman            | 1.18.0         | 1.19.0           |                                                                                                                                                                                                              |
| cyberark.conjur              | 1.3.8          | 1.3.9            | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| cyberark.pas                 | 1.0.36         | 1.0.39           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| dellemc.enterprise_sonic     | 3.2.0          | 4.1.0            |                                                                                                                                                                                                              |
| dellemc.openmanage           | 10.0.1         | 10.0.2           |                                                                                                                                                                                                              |
| fortinet.fortimanager        | 2.11.0         | 2.13.0           |                                                                                                                                                                                                              |
| fortinet.fortios             | 2.4.2          | 2.5.0            |                                                                                                                                                                                                              |
| google.cloud                 | 1.9.0          | 1.13.0           |                                                                                                                                                                                                              |
| graphiant.naas               |                | 26.3.0           | The collection was added to Ansible                                                                                                                                                                          |
| hetzner.hcloud               | 6.0.0          | 6.8.0            |                                                                                                                                                                                                              |
| hitachivantara.vspone_block  | 4.4.0          | 4.6.1            |                                                                                                                                                                                                              |
| hitachivantara.vspone_object | 1.0.0          | 1.1.1            |                                                                                                                                                                                                              |
| ibm.storage_virtualize       | 3.1.0          | 3.3.0            |                                                                                                                                                                                                              |
| infoblox.nios_modules        | 1.8.0          | 1.9.0            |                                                                                                                                                                                                              |
| inspur.ispim                 | 2.2.3          | 2.2.4            |                                                                                                                                                                                                              |
| kaytus.ksmanage              | 2.0.0          | 4.0.0            |                                                                                                                                                                                                              |
| kubernetes.core              | 6.2.0          | 6.3.0            |                                                                                                                                                                                                              |
| kubevirt.core                | 2.2.3          | 2.2.4            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| microsoft.ad                 | 1.9.2          | 1.10.0           |                                                                                                                                                                                                              |
| microsoft.iis                | 1.0.3          | 1.1.0            |                                                                                                                                                                                                              |
| netapp.ontap                 | 23.2.0         | 23.4.0           |                                                                                                                                                                                                              |
| netapp.storagegrid           | 21.15.0        | 21.16.0          |                                                                                                                                                                                                              |
| netapp_eseries.santricity    | 1.4.1          | 2.0.1            | The collection did not have a changelog in this version.                                                                                                                                                     |
| netbox.netbox                | 3.21.0         | 3.22.0           |                                                                                                                                                                                                              |
| ovirt.ovirt                  | 3.2.1          | 3.2.2            |                                                                                                                                                                                                              |
| pcg.alpaca_operator          |                | 2.2.0            | The collection was added to Ansible                                                                                                                                                                          |
| purestorage.flasharray       | 1.39.0         | 1.42.0           |                                                                                                                                                                                                              |
| purestorage.flashblade       | 1.22.0         | 1.24.0           |                                                                                                                                                                                                              |
| splunk.es                    | 4.0.0          | 5.1.0            |                                                                                                                                                                                                              |
| telekom_mms.icinga_director  | 2.4.0          | 2.5.1            |                                                                                                                                                                                                              |
| theforeman.foreman           | 5.7.0          | 5.10.0           |                                                                                                                                                                                                              |
| vmware.vmware                | 2.4.0          | 2.8.0            |                                                                                                                                                                                                              |
| vmware.vmware_rest           | 4.9.0          | 4.10.0           |                                                                                                                                                                                                              |
| vultr.cloud                  | 1.13.0         | 1.14.0           |                                                                                                                                                                                                              |
| wti.remote                   | 1.0.10         | 1.0.11           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |

<a id="major-changes-2"></a>
### Major Changes

<a id="ansible-core-10"></a>
#### Ansible\-core

* <code>ansible\-galaxy install</code> and <code>ansible\-galaxy collection install\|download</code> \- collections that declare a <code>requires\_ansible</code> version that is not compatible with the running ansible\-core version are now excluded from installation and download by default\. In previous versions\, ansible\-galaxy would install such collections even if doing so resulted in an error at load time\. To restore the previous behavior\, set <code>COLLECTIONS\_ON\_ANSIBLE\_VERSION\_MISMATCH</code> to <code>ignore</code> in your configuration\. \([https\://github\.com/ansible/ansible/issues/78539](https\://github\.com/ansible/ansible/issues/78539)\)
* action plugins \- Actions can directly register variables at several precedence layers using the <code>register\_host\_variables</code> method on <code>ActionBase</code>\. Previously\, variable registration could only be simulated by user action plugins by returning <code>ansible\_facts</code> with insecure fact injection\.
* register projections \- The <code>register</code> task keyword allows mapping multiple variable names to Jinja expressions to transform task results and other variables\. The mapping form can replace many usages of <code>set\_fact</code> and allows order\-independent chained access to other variable expressions within the same task\.
* task implicit object \- A new <code>\_task</code> implicit object is available for use in <code>register</code> and task conditional expressions \(e\.g\.\, <code>failed\_when</code>\)\. The result of the current task can be accessed via the <code>\_task\.result</code> property\, without the use of <code>register</code>\. Under a loop\, <code>\_task\.result</code> is the most recently completed result and <code>\_task\.loop\_result</code> provides access to accumulated loop results\. The <code>\_task\.polymorphic\_result</code> property provides compatibility with classic name\-only <code>register</code> in loops\. The value is the result of the most recent loop iteration\, then becomes the final list loop result once the loop is complete\.

<a id="amazon-aws"></a>
#### amazon\.aws

* amazon\.aws collection \- <code>awscli</code> version has been bumped to 1\.34\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2774](https\://github\.com/ansible\-collections/amazon\.aws/pull/2774)\)\.
* amazon\.aws collection \- <code>botocore</code> and <code>boto3</code> versions have been bumped to 1\.35\.0 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2774](https\://github\.com/ansible\-collections/amazon\.aws/pull/2774)\)\.
* ec2\_security\_group \- Support for passing nested lists of strings to <code>rules\.cidr\_ip</code> and <code>rules\.cidr\_ipv6</code> have been removed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.
* iam\_user \- Support for <code>iam\_user</code> return key has been removed\; only <code>user</code> is now returned \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.
* lambda\_info \- Support for <code>function</code> has been removed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.
* route53\_info \- Support for CamelCased lists \(<code>ResourceRecordSets</code>\, <code>HostedZones</code>\, <code>HealthChecks</code>\, <code>CheckerIpRanges</code>\, <code>DelegationSets</code>\, <code>HealthCheck</code>\) have been removed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.
* s3\_object \- Support for <code>list</code> mode has been removed\; use <code>s3\_object\_info</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.
* s3\_object \- Support for passing the leading <code>/</code> has been removed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.
* s3\_object\_info \- Support for passing <code>dualstack</code> and <code>endpoint\_url</code> at the same time has been removed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2777](https\://github\.com/ansible\-collections/amazon\.aws/issues/2777)\)\.

<a id="chocolatey-chocolatey"></a>
#### chocolatey\.chocolatey

* win\_chocolatey \- add option to ignore pinned status of pinned packages

<a id="community-aws"></a>
#### community\.aws

* community\.aws collection \- <code>awscli</code> version has been bumped to 1\.34\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2375](https\://github\.com/ansible\-collections/community\.aws/pull/2375)\)\.
* community\.aws collection \- <code>botocore</code> and <code>boto3</code> versions have been bumped to 1\.35\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2375](https\://github\.com/ansible\-collections/community\.aws/pull/2375)\)\.

<a id="community-proxmox"></a>
#### community\.proxmox

* proxmox \- Add ca\_path option to specify a ca\-certificate for tls validation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/256](https\://github\.com/ansible\-collections/community\.proxmox/pull/256)\)\.

<a id="community-routeros-3"></a>
#### community\.routeros

* api\_info\, api\_modify \- multiple parameters can no longer be disabled for the\`\`tool netwatch\`\` path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- parameter <code>name\-format</code> can no longer be disabled for the <code>interface wifi provisioning</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- parameter <code>script</code> can no longer be disabled for the <code>ip dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.

<a id="community-vmware"></a>
#### community\.vmware

* Bump required <code>vmware\.vmware</code> collection version to 2\.5\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2503](https\://github\.com/ansible\-collections/community\.vmware/pull/2503)\)\.

<a id="containers-podman-2"></a>
#### containers\.podman

* Add podman Quadlet modules
* Rewrite podman and buildah connections

<a id="fortinet-fortios-2"></a>
#### fortinet\.fortios

* Supported new versions 7\.6\.5 and 7\.6\.6\.
* Updated the Q\&A for using the default\_group feature in modules\.

<a id="kaytus-ksmanage"></a>
#### kaytus\.ksmanage

* Add new modules upload\_ssl\,ssl\_info\,generate\_ssl\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/34](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/34)\)\.
* Change the name of the used SDK\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/37](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/37)\)\.
* Modify the URL address path when the owner is changed\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/38](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/38)\)\.
* The edit\_m6\_log\_setting\.py module has added the \'server\_status\' attribute\; The edit\_network\_bond\.py module modifies the attribute descriptions\; The edit\_snmp\.py and edit\_snmp\_trap\.py module modifies the allowable value ranges for the auth\_protocol and priv\_protocol attributes\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/33](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/33)\)\.

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
* na\_ontap\_interface \- AWS Lambda support added to the module\.
* na\_ontap\_lun \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_copy \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_map \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_map\_reporting\_nodes \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_buckets \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_groups \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_policies \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_services \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_users \- AWS Lambda support added to the module\.
* na\_ontap\_snapmirror \- AWS Lambda support added to the module\.
* na\_ontap\_snapshot \- AWS Lambda support added to the module\.
* na\_ontap\_svm \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_autosize \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_clone \- AWS Lambda support added to the module\.
* na\_ontap\_vserver\_peer \- AWS Lambda support added to the module\.

<a id="splunk-es-3"></a>
#### splunk\.es

* Bumped the minimum supported Ansible version to <code>\>\=2\.17\.0</code> \(Ansible 2\.15/2\.16 are EoL\)\.

<a id="vmware-vmware"></a>
#### vmware\.vmware

* Replace <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/268](https\://github\.com/ansible\-collections/vmware\.vmware/issues/268)\)\.
* Replace <code>ansible\.module\_utils\.common\.\_collections\_compat</code> \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/271](https\://github\.com/ansible\-collections/vmware\.vmware/issues/271)\)\.

<a id="minor-changes-3"></a>
### Minor Changes

<a id="ansible-core-11"></a>
#### Ansible\-core

* DataLoader \- Update <code>DataLoader</code> to deal exclusively in str
* PowerShell 7 \- Add support for running PowerShell written modules on POSIX hosts\. PowerShell modules run with the <code>pwsh</code> interpreter and can access the same module utils that Windows PowerShell modules can use\. Some PowerShell based module utils may not be compatible due to their reliance on Windows APIs but <code>Ansible\.Basic\.cs</code> for module input and output handling works\.
* PowerShell AddType Util \- Will only include the debug information when <code>DISPLAY\_TRACEBACK</code> contains <code>error</code> or <code>always</code>\. In the past the debug information would have been included if <code>\-vvv</code> or higher was used but this new behavior aligns the logic with the new option added in Ansible 2\.19\.
* The minimum required <code>setuptools</code> version is now <code>77\.0\.3</code>\, as it is needed for the new PEP 639 license format
* ansiballz \- Add tech preview to embed arbitrary files\, not relying on python <code>import</code>
* ansible\-playbook \- consolidated block and task loading code to remove duplicated logic \([https\://github\.com/ansible/ansible/pull/86603](https\://github\.com/ansible/ansible/pull/86603)\)\.
* ansible\-test \- Add PowerShell support to managed containers and remotes\.
* ansible\-test \- Add container/remote aliases for more loosely specifying managed test environments\.
* ansible\-test \- Add limited RHEL8 integration test remote supporting Python 3\.12 only
* ansible\-test \- Add support for using the Ansible Core CI service from GitHub Actions\.
* ansible\-test \- Expand functions covered by the <code>unwanted</code> rule for the <code>pylint</code> sanity test\. It now includes various <code>os\.\*</code> and <code>subprocess\.\*</code> subprocess functions in Ansible modules and module\_utils\.
* ansible\-test \- Optimize DNF configuration for managed remote RHEL instances\.
* ansible\-test \- Remove <code>use\-run\-command\-not\-popen</code> and <code>use\-run\-command\-not\-os\-call</code> error codes from the <code>validate\-modules</code> sanity test\. These scenarios are now covered by the <code>pylint</code> sanity test\.
* ansible\-test \- Remove pylint check for <code>urllib2</code> usage\.
* ansible\-test \- Remove support for an obsolete remote authentication method\.
* ansible\-test \- Replace Alpine 3\.22 container and remote with 3\.23\.
* ansible\-test \- Replace Fedora 42 with 43\.
* ansible\-test \- Replace FreeBSD 13\.5 remote with 15\.0\.
* ansible\-test \- Replace FreeBSD 14\.3 remote with 14\.4\.
* ansible\-test \- Replace RHEL 10\.0 remote with 10\.1\.
* ansible\-test \- Replace RHEL 9\.6 remote with 9\.7\.
* ansible\-test \- Replace macOS 15\.3 remote with macOS 26\.3\.
* ansible\-test \- Replace the <code>parallels</code> managed macOS provider with a new <code>mac</code> provider\.
* ansible\-test \- Support automatic loading of test collections in core integration tests\.
* ansible\-test \- Switch managed macOS remotes from x86\_64 to aarch64\.
* ansible\-test \- Update URL used to download FreeBSD wheels for managed remotes\.
* ansible\-test \- Update ansible\-test\-utility\-container\.
* ansible\-test \- Update base and default containers\.
* ansible\-test \- Update http\-test\-container\.
* ansible\-test \- Update pypi\-test\-container\.
* ansible\-test \- Update sanity test requirements\.
* ansible\-test \- Update the pylint sanity test to pylint 4\.0\.2\.
* ansible\-test \- Use the new API endpoint for the Ansible Core CI service\.
* ansible\-test \- add <code>\.winrm</code> and <code>\.networking</code> as valid JSON/YAML inventory file extensions\. This should not affect any public facing code as it is used internally for inventories generated by <code>ansible\-test</code>\.
* ansible\-test \- update galaxy\_ng container to current version deployed to galaxy\.ansible\.com
* ansible\-test acme cloud plugin \- update to the 2\.4\.0 ACME test image\, which upgrades Pebble to 2\.10\.0\, Go to 1\.26\, and Python to 3\.14\, and generally updates all contained Python dependencies \([https\://github\.com/ansible/ansible/pull/86740](https\://github\.com/ansible/ansible/pull/86740)\)\.
* ansible\-test validate\-modules sanity test \- now reports bad return value keys that cannot be used with the dot notation in Jinja expressions \([https\://github\.com/ansible/ansible/issues/86079](https\://github\.com/ansible/ansible/issues/86079)\)\.
* ansible\-vault \- improved error messages for better clarity and context when vault operations fail\, helping users diagnose configuration or file access issues more easily \([https\://github\.com/ansible/ansible/pull/86602](https\://github\.com/ansible/ansible/pull/86602)\)\.
* ansible\-vault \- keep the original contents when the EDITOR returns failure when using <code>ansible\-vault edit</code>\.
* break\_when \- A <code>break\_when\_result</code> key is always present in results when a <code>break\_when</code> expression is used\.
* break\_when \- A <code>break\_when\_suppressed\_exception</code> key is added to a result when a <code>break\_when</code> expression fails and masks an existing exception in a result\.
* break\_when \- A failed <code>break\_when</code> expression now preserves the loop structure of a result and any loop item results\.
* callback \- filter key starting with \_ansible\_ from debug messages \([https\://github\.com/ansible/ansible/issues/69731](https\://github\.com/ansible/ansible/issues/69731)\)\.
* callback plugins \- support configuration using extra variables\.
* changed\_when \- A <code>changed\_when\_result</code> key is always present in results when a <code>changed\_when</code> expression is used\.
* changed\_when \- A <code>changed\_when\_suppressed\_exception</code> key is added to a result when a <code>changed\_when</code> expression fails and masks an existing exception in a result\.
* core \- The <code>ActionBase\.\_low\_level\_execute\_command</code> method no longer adds <code>\&\& sleep 0</code> to commands\. This was a work\-around for a 10\+ year old Linux kernel bug affecting OpenSSH\. By August of 2016 the fix had been included in kernel versions 4\.1\.26\, 4\.4\.12\, 4\.5\.6\, 4\.6\.1 and 4\.7\. Linux kernel bug report\: [https\://lore\.kernel\.org/lkml/alpine\.LNX\.2\.00\.1512091358290\.9574\@fanir\.tuyoix\.net/](https\://lore\.kernel\.org/lkml/alpine\.LNX\.2\.00\.1512091358290\.9574\@fanir\.tuyoix\.net/) OpenSSH bug report\: [https\://bugzilla\.mindrot\.org/show\_bug\.cgi\?id\=2492](https\://bugzilla\.mindrot\.org/show\_bug\.cgi\?id\=2492)
* deb822\_repository \- add include and exclude parameter arguments \([https\://github\.com/ansible/ansible/issues/86155](https\://github\.com/ansible/ansible/issues/86155)\)
* default callback \- add <code>display\_included\_hosts</code> option to control the <code>included\:</code> banner lines for <code>include\_tasks</code>/<code>include\_role</code> \([https\://github\.com/ansible/ansible/issues/84499](https\://github\.com/ansible/ansible/issues/84499)\)\.
* default callback plugin \- add option to configure line width for YAML output\. This allows to disable line wrapping \([https\://github\.com/ansible/ansible/issues/84657](https\://github\.com/ansible/ansible/issues/84657)\, [https\://github\.com/ansible/ansible/pull/85498](https\://github\.com/ansible/ansible/pull/85498)\)\.
* default callback plugin \- add variable configuration for <code>display\_skipped\_hosts</code> \([https\://github\.com/ansible/ansible/issues/84469](https\://github\.com/ansible/ansible/issues/84469)\)\.
* display \- replace few words with more inclusive word list such as denylist\, FilterDenyList \([https\://github\.com/ansible/ansible/pull/86304](https\://github\.com/ansible/ansible/pull/86304)\)\.
* dnf \- Separate module into module and utility script
* executor \- remove unused RETURN\_VARS
* file \- return disk\_usage\_bytes fact \([https\://github\.com/ansible/ansible/issues/70834](https\://github\.com/ansible/ansible/issues/70834)\)\.
* filter \- Use datetime\.strftime instead of time\.strftime in strftime \([https\://github\.com/ansible/ansible/issues/86260](https\://github\.com/ansible/ansible/issues/86260)\)\.
* find \- add locale encoding in err msg when none is given
* generator \- add support for extra vars \([https\://github\.com/ansible/ansible/issues/83270](https\://github\.com/ansible/ansible/issues/83270)\)\.
* group \- Add warning message when invalid priority values are provided to Group\.set\_priority\(\) method \([https\://github\.com/ansible/ansible/pull/85468](https\://github\.com/ansible/ansible/pull/85468)\)\.
* ignore\_errors \- Invalid values for <code>ignore\_errors</code> will always be treated as <code>False</code>
* ignore\_errors \- Templated values for the <code>ignore\_errors</code> keyword behave more consistently in looped tasks\. If <code>ignore\_errors</code> resolves <code>True</code> for any loop item\, errors will be ignored for the entire task\.
* ignore\_unreachable \- Templated values for the <code>ignore\_unreachable</code> keyword behave more consistently in looped tasks\. If <code>ignore\_unreachable</code> resolves <code>True</code> for any loop item\, unreachable hosts will be ignored for the entire task\.
* include\_role has new option <em class="title-reference">rescuable</em> to allow it to toggle between task failure and syntax errors\.
* loops \- The <code>break\_when</code> keyword is now validated when the value is falsey\.
* loops \- The registered result of a loop task no longer contains the <code>skipped</code> key when it would be <code>False</code>\.
* module/action results \- A <code>results</code> key returned from an action or module is always preserved\. Previously the <code>results</code> key was sometimes removed\, depending on the type of its value\.
* package\_facts \- Switch from rpm python to rpm CLI to list packages
* package\_facts \- use apk query instead of apk info for gathering package facts in Alpine \([https\://github\.com/ansible/ansible/issues/86579](https\://github\.com/ansible/ansible/issues/86579)\)\.
* password hashing \- Add support back for using the <code>crypt</code> implementation from the C library used to build Python\, or with expanded functionality using <code>libxcrypt</code>
* psrp \- Added the <code>certificate\_key\_password</code> option through the variable <code>ansible\_psrp\_certificate\_key\_password</code> that can be used to decrypt the key specified by <code>certificate\_key\_pem</code>\. This option requires <code>pypsrp\>\=0\.9\.0</code> to be installed in the Ansible environment\.
* psrp \- Added the <code>no\_profile</code> option through the variable <code>ansible\_psrp\_no\_profile</code> that can stop the remote Windows host from loading the user profile on the Ansible tasks\. This option requires <code>pypsrp\>\=0\.9\.0</code> to be installed in the Ansible environment\.
* script \- remove the currently unsupported <code>decrypt</code> argument from the module documentation \([https\://github\.com/ansible/ansible/issues/86067](https\://github\.com/ansible/ansible/issues/86067)\)\.
* service \- add support for GNU Hurd systems\, which use SysV init scripts \([https\://github\.com/ansible/ansible/pull/86622](https\://github\.com/ansible/ansible/pull/86622)\)\.
* slurp module gets new C\(armor\) option to allow user to disable base64 encoding\.
* stat \- return disk\_usage\_bytes fact \([https\://github\.com/ansible/ansible/issues/70834](https\://github\.com/ansible/ansible/issues/70834)\)\.
* to\_yaml / to\_nice\_yaml filters \- Add optional <code>vault\_behavior</code> argument to configure how vaulted values are rendered\.

<a id="amazon-aws-1"></a>
#### amazon\.aws

* Add support for the io2 storage type for RDS \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2748](https\://github\.com/ansible\-collections/amazon\.aws/pull/2748)\)\.
* autoscaling\_group \- Added a boolean parameter <code>protected\_from\_scale\_in</code> to toggle protection from scale\-in\. This allows users to enable or disable scale\-in protection for instances in an autoscaling group\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2207](https\://github\.com/ansible\-collections/amazon\.aws/pull/2207)\)
* aws\_cloudtrail \- Ported the event source plugin from <code>ansible\.eda</code> to <code>amazon\.aws</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2816](https\://github\.com/ansible\-collections/amazon\.aws/pull/2816)\)\.
* aws\_cloudtrail \- replace deprecated <code>datetime\.utcnow\(\)</code> with timezone\-aware <code>datetime\.now\(tz\=timezone\.utc\)</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2858](https\://github\.com/ansible\-collections/amazon\.aws/pull/2858)\)\.
* aws\_ec2 \- added \"ec2\_tags\" host variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2847](https\://github\.com/ansible\-collections/amazon\.aws/pull/2847)\)\.
* aws\_ec2 \- remove explicit <code>disable\_lookups\=False</code> parameter from template calls as it is deprecated and False is the default value \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2864](https\://github\.com/ansible\-collections/amazon\.aws/pull/2864)\)\.
* aws\_inventory\_base \- remove explicit <code>disable\_lookups\=False</code> parameter from template calls as it is deprecated and False is the default value \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2864](https\://github\.com/ansible\-collections/amazon\.aws/pull/2864)\)\.
* aws\_rds \- added \"rds\_tags\" host variable \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2847](https\://github\.com/ansible\-collections/amazon\.aws/pull/2847)\)\.
* aws\_resource\_actions \- remove redundant <code>list\(\)</code> call when using <code>sorted\(\)</code>\, improving efficiency by allowing sorted\(\) to consume the generator expression directly \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2882](https\://github\.com/ansible\-collections/amazon\.aws/pull/2882)\)\.
* aws\_sqs\_queue \- Ported the event source plugin from <code>ansible\.eda</code> to <code>amazon\.aws</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2816](https\://github\.com/ansible\-collections/amazon\.aws/pull/2816)\)\.
* ec2\_launch\_template \- increase GP3 volume <code>throughput</code> limits in line with updated AWS limits \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2749](https\://github\.com/ansible\-collections/amazon\.aws/pull/2749)\)\.
* ec2\_vol \- added <code>volume\_initialization\_rate</code> optional parameter to support Provisioned Initialization Rate when creating a volume from snapshots\. \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2665](https\://github\.com/ansible\-collections/amazon\.aws/issues/2665)\)
* ec2\_vol \- increase <code>throughput</code> and <code>iops</code> limits for GP3 volumes in line with updated AWS limits \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2749](https\://github\.com/ansible\-collections/amazon\.aws/pull/2749)\)\.
* ec2\_vpc\_endpoint \- replace deprecated <code>datetime\.utcnow\(\)</code> with timezone\-aware <code>datetime\.now\(datetime\.timezone\.utc\)</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2866](https\://github\.com/ansible\-collections/amazon\.aws/pull/2866)\)\.
* ec2\_vpc\_nat\_gateway \- replace deprecated <code>datetime\.utcnow\(\)</code> with timezone\-aware <code>datetime\.now\(datetime\.timezone\.utc\)</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2866](https\://github\.com/ansible\-collections/amazon\.aws/pull/2866)\)\.
* indirect node count \- Add support for querying RDS database resources \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2825](https\://github\.com/ansible\-collections/amazon\.aws/pull/2825)\)\.
* indirect node count \- Create query for networking load balancer resources \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2818](https\://github\.com/ansible\-collections/amazon\.aws/pull/2818)\)\.
* indirect node count \- create query for ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2807](https\://github\.com/ansible\-collections/amazon\.aws/pull/2807)\)\.
* indirect node count \- create query for networking resources vpc\, subnet\, nat gateway\, internet gateway\, virtual gateway\, route table\, vpn\, vpc peering \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2811](https\://github\.com/ansible\-collections/amazon\.aws/pull/2811)\)\.
* indirect node count \- create query for storage resources S3 bucket and Object \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2811](https\://github\.com/ansible\-collections/amazon\.aws/pull/2811)\)\.
* module\_utils\.s3 \- added \"501\" to the list of error codes thrown by S3 replacements \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2447](https\://github\.com/ansible\-collections/amazon\.aws/issues/2447)\)\.
* module\_utils/\_s3/common \- use <code>is\_boto3\_error\_httpstatus</code> to handle HTTP 403 and 501 status codes from S3\-compatible services \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2776](https\://github\.com/ansible\-collections/amazon\.aws/pull/2776)\)\.
* module\_utils/botocore \- add <code>is\_boto3\_error\_httpstatus</code> helper function to catch boto3 exceptions based on HTTP status codes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2776](https\://github\.com/ansible\-collections/amazon\.aws/pull/2776)\)\.
* module\_utils/s3 \- refactored S3 module utilities to consolidate duplicate code\, add comprehensive type hints and docstrings\, and improve maintainability \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* plugin\_utils/inventory \- add error handling for ClientError and BotoCoreError in \_freeze\_iam\_role method \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2902](https\://github\.com/ansible\-collections/amazon\.aws/pull/2902)\)\.
* plugin\_utils/inventory \- extract role session name generation into separate method to improve code organisation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2902](https\://github\.com/ansible\-collections/amazon\.aws/pull/2902)\)\.
* requirements\.txt \- Added <code>aiobotocore</code> as a dependency for the event source plugins only \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2816](https\://github\.com/ansible\-collections/amazon\.aws/pull/2816)\)\.
* route53 \- added <code>record\_values</code> key to <code>resource\_record\_sets</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* route53 \- added <code>routing\_region</code> parameter to explicitly specify the region for latency\-based resource record sets \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2893](https\://github\.com/ansible\-collections/amazon\.aws/issues/2893)\)\.
* route53 \- added temporary <code>aws\_region</code> parameter to allow specifying the AWS region for API requests while the <code>region</code> parameter is being transitioned \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2893](https\://github\.com/ansible\-collections/amazon\.aws/issues/2893)\)\.
* route53 \- refactored module utility to use decorator\-based error handling\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2892](https\://github\.com/ansible\-collections/amazon\.aws/pull/2892)\)
* route53\_health\_check \- refactored module to improve testability and type safety\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2892](https\://github\.com/ansible\-collections/amazon\.aws/pull/2892)\)
* s3\_bucket \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* s3\_bucket\_info \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* s3\_object \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* s3\_object\_info \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* sts\_assume\_role \- improve error handling for <code>MalformedPolicyDocument</code> errors by providing a clearer error message when an invalid policy document is provided \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2778](https\://github\.com/ansible\-collections/amazon\.aws/pull/2778)\)\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* Exposes new libssh option to configure key\_exchange\_algorithms\. This requires ansible\-pylibssh v1\.3\.0 or higher\.
* Option to use libssh as transport while using netconf\, is added\.
* The ssh\-python module is needed\, which will ensure libssh as transport for netconf operations\. When use\_libssh is enabled\.

<a id="ansible-windows"></a>
#### ansible\.windows

* Add official support for Ansible 2\.20
* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* ansible\.windows\.win\_package \- Add optional Authenticode signature validation for installer files via the new <code>verify\_signature</code> parameter\.
* win\_environment \- Add the return value <code>env\_values</code> which is a copy of the existing <code>values</code> return value\. The documentation for <code>values</code> has been removed to discourage use of that version due to the inability to use <code>values</code> with dot notation in a Jinja2 template due to the conflict with the Python <code>values</code> attribute\.
* win\_file \- is aligned with <code>ansible\.builtin\.file</code> and now supports options <code>access\_time</code>\, <code>access\_time\_format</code>\, <code>modification\_time</code>\, and <code>modification\_time\_format</code>\. \([https\://github\.com/ansible\-collections/ansible\.windows/issues/798](https\://github\.com/ansible\-collections/ansible\.windows/issues/798)\)
* win\_shell \- Add <code>cmd</code> module option that can be used instead of the free form input\. This aligns the options to the POSIX <code>shell</code> module\.
* win\_shell \- Support using <code>pwsh\.exe</code> as the executable in a mode similar to how <code>powershell\.exe</code> is run\.

<a id="cisco-aci"></a>
#### cisco\.aci

* Add contract\_type option to aci\_contract\_subject\_to\_filter and aci\_contract\_subject\.
* Add l3out\, l3out\_tenant\, external\_epg and redistribute options to aci\_l4l7\_device\_selection\_interface\_context\.
* Add normalize\_payload\_values option to aci\_rest for Ansible Core 2\.19 support\.
* Add set\_communities\, set\_as\_path and set\_policy\_tag options to aci\_tenant\_action\_rule\_profile\.

<a id="cisco-ios"></a>
#### cisco\.ios

* Adds a new Resource Module <em class="title-reference">ios\_bfd\_interfaces</em> to configure BFD on interfaces\.
* Adds a new Resource Module <em class="title-reference">ios\_bfd\_templates</em> to configure BFD  using templates\.
* ios\_l2\_interfaces \- Added xconnect and encapsulation attributes for L2VPN pseudowire and MPLS services configuration\.
* ios\_l3\_interfaces \- Add support for \'redirects\' and \'unreachables\' attributes to configure ICMP redirect and unreachable messages\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* Added new modules and action plugins for Cisco Umbrella account connect/disconnect\, Wireless AutoRF \(RRM\) settings\, third\-party VPN peers\, organization integrations\, inventory EoX overview\, network moves\, SASE eligible networks\, and wireless device provisioning deployments\.
* Updated with v1\.66\.0 dashboard API\, adding new plugins and fixing bugs\.
* networks\_wireless\_settings\: added multicast\-to\-unicast conversion support\.
* organizations\_inventory\_devices\_info\: added eoxStatuses filtering and included EoX fields in returned inventory device data\.

<a id="cisco-mso"></a>
#### cisco\.mso

* Add parent\_type\, node\_id\, path\, port\_channel\, virtual\_port\_channel\, encapsulation\_type and encapsulation\_value options to ndo\_l3out\_bgp\_peer\.
* Add ptp option to ndo\_l3out\_routed\_interface and ndo\_l3out\_routed\_sub\_interface\.
* Add support to deploy and undeploy non\-schema templates in ndo\_template\_deploy \(formerly ndo\_schema\_template\_deploy\)\.

<a id="cisco-nxos"></a>
#### cisco\.nxos

* Added alias for mode option as switchport\_mode for nxos\_l2\_interfaces

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Added missing param when creating a health monitor

<a id="community-aws-1"></a>
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

<a id="community-crypto-2"></a>
#### community\.crypto

* luks\_device \- add support for TPM2 enrollment using <code>systemd\-cryptsetup</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/850](https\://github\.com/ansible\-collections/community\.crypto/issues/850)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/972](https\://github\.com/ansible\-collections/community\.crypto/pull/972)\)\.
* luks\_device \- add support for keyslot priority \([https\://github\.com/ansible\-collections/community\.crypto/issues/850](https\://github\.com/ansible\-collections/community\.crypto/issues/850)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/972](https\://github\.com/ansible\-collections/community\.crypto/pull/972)\)\.

<a id="community-dns-5"></a>
#### community\.dns

* Hetzner DNS modules and plugins \- support the [new Hetzner DNS API](https\://docs\.hetzner\.com/networking/dns/faq/beta/) \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.

<a id="community-docker-1"></a>
#### community\.docker

* docker\_compose\_v2\_pull \- adds <code>ignore\_pull\_failures</code> parameter that passes <code>\-\-ignore\-pull\-failures</code> to the <code>docker compose pull</code> call when set to <code>true</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1248](https\://github\.com/ansible\-collections/community\.docker/pull/1248)\)\.

<a id="community-general-3"></a>
#### community\.general

* ModuleHelper module utils \- allow to ignore specific exceptions in <code>module\_fails\_on\_exception</code> decorator \([https\://github\.com/ansible\-collections/community\.general/pull/11488](https\://github\.com/ansible\-collections/community\.general/pull/11488)\)\.
* The last code included in the collection that was licensed under the PSF 2\.0 license was removed form the collection\. This means that now all code is either GPLv3\+ licensed\, MIT licensed\, or BSD\-2\-clause licensed \([https\://github\.com/ansible\-collections/community\.general/pull/11232](https\://github\.com/ansible\-collections/community\.general/pull/11232)\)\.
* \_mount module utils \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* \_stormssh module utils \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* a\_module test plugin \- add proper parameter checking and type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* aerospike\_migrations \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* aix\_filesystem \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* ali\_instance \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* alicloud\_ecs module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* android\_sdk \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* ansible\_galaxy\_install \- add parameter <code>executable</code> \([https\://github\.com/ansible\-collections/community\.general/issues/7261](https\://github\.com/ansible\-collections/community\.general/issues/7261)\, [https\://github\.com/ansible\-collections/community\.general/pull/11646](https\://github\.com/ansible\-collections/community\.general/pull/11646)\)\.
* ansible\_type plugin utils \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* ansible\_type test plugin \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* api module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* apk \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* apt\_rpm \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* apt\_rpm \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* archive \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
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
* bitbucket module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* bitbucket\_access\_key modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* bitbucket\_pipeline\_key\_pair modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* bitbucket\_pipeline\_known\_host \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* bitbucket\_pipeline\_known\_host modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* bitbucket\_pipeline\_variable modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* btrfs module utils \- make execution of external commands safer by passing arguments as list \([https\://github\.com/ansible\-collections/community\.general/pull/11240](https\://github\.com/ansible\-collections/community\.general/pull/11240)\)\.
* chef\_databag lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* chroot connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* chroot connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* circonus\_annotation \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* cloudflare\_dns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* cmd\_runner module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* cobbler inventory plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* cobbler inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* cobbler\_sync \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* cobbler\_sync \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* cobbler\_system \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* cobbler\_system \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* collection\_version lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* composer \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* consul module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* consul\_kv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* copr \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* counter filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* credstash lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* cronvar \- simplify handling unknown exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11340](https\://github\.com/ansible\-collections/community\.general/pull/11340)\)\.
* cronvar \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* cronvar \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* crypttab \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* crypttab \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
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
* deps module utils \- change the internal representaion of dependency state \([https\://github\.com/ansible\-collections/community\.general/pull/11242](https\://github\.com/ansible\-collections/community\.general/pull/11242)\)\.
* deps module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* dig lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* dimensiondata\_network \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* dimensiondata\_network modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* dnf\_config\_manager \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* dnstxt lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* doas become plugin \- add new option <code>allow\_pipelining</code> to explicitly allow the use of pipelining with this plugin\. This should only be set to <code>true</code> with ansible\-core 2\.19\+ when <code>doas</code> does not require a password \([https\://github\.com/ansible\-collections/community\.general/issues/11411](https\://github\.com/ansible\-collections/community\.general/issues/11411)\, [https\://github\.com/ansible\-collections/community\.general/pull/11481](https\://github\.com/ansible\-collections/community\.general/pull/11481)\)\.
* dsv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* elastic callback plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* elasticsearch\_plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* etcd3 lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* exceptions module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* filesize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* filesize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* flatpak \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* flatpak\_remote \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* fqdn\_valid test plugin \- add proper parameter checking\, and add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* from\_csv filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* from\_ini filter plugin \- add <code>delimiters</code> parameter to allow correctly parsing more INI documents \([https\://github\.com/ansible\-collections/community\.general/issues/11506](https\://github\.com/ansible\-collections/community\.general/issues/11506)\, [https\://github\.com/ansible\-collections/community\.general/pull/11512](https\://github\.com/ansible\-collections/community\.general/pull/11512)\)\.
* from\_ini filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* gandi\_livedns\_api module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* gandi\_livedns\_api module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* github\_app\_access\_token lookup plugin \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* github\_app\_access\_token lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* gitlab\_group \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_group\_access\_token \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* gitlab\_group\_members \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* gitlab\_issue \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_merge\_request \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_project \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* gitlab\_project\_access\_token \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* gitlab\_project\_members \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* gitlab\_runner \- allow maximum timeout to be disabled by passing <code>0</code> to <code>maximum\_timeout</code>  \([https\://github\.com/ansible\-collections/community\.general/pull/11174](https\://github\.com/ansible\-collections/community\.general/pull/11174)\)\.
* gitlab\_runners inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* gunicorn \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* haproxy \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hashids filter \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* hashids filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* hg \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* hg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* hpilo\_info \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hpilo\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* htpasswd \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* htpasswd \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* hwc\_ecs\_instance \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hwc\_utils module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* hwc\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* hwc\_utils module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* hwc\_vpc\_port \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* ibm\_sa\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* icinga2 inventory plugin \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* icinga2 inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* icinga2\_host \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* identity\.keycloak\.keycloak module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* idrac\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* idrac\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* idrac\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* idrac\_redfish\_info \- add multiple manager support to <code>GetManagerAttributes</code> command \([https\://github\.com/ansible\-collections/community\.general/pull/11294](https\://github\.com/ansible\-collections/community\.general/pull/11294)\)\.
* idrac\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* idrac\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* ilo\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* ilo\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* ilo\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* ilo\_redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* imc\_rest \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* imc\_rest modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* incus connection plugin \- add support for Windows virtual machines \([https\://github\.com/ansible\-collections/community\.general/pull/11199](https\://github\.com/ansible\-collections/community\.general/pull/11199)\)\.
* incus connection plugin \- improve code readability \([https\://github\.com/ansible\-collections/community\.general/pull/11346](https\://github\.com/ansible\-collections/community\.general/pull/11346)\)\.
* incus connection plugin \- simplify regular expression matching commands \([https\://github\.com/ansible\-collections/community\.general/pull/11347](https\://github\.com/ansible\-collections/community\.general/pull/11347)\)\.
* incus inventory plugin \- add support for constructing project\-independent FQDNs \([https\://github\.com/ansible\-collections/community\.general/pull/11555](https\://github\.com/ansible\-collections/community\.general/pull/11555)\)\.
* influxdb\_query \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* influxdb\_user \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* influxdb\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* influxdb\_write \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ini\_file \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* interfaces\_file \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* iocage inventory plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* ip\_netns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* ip\_netns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* ip\_netns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ipa module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* ipa module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
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
* iptables\_state \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* iptables\_state action plugin \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* iso\_customize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* jail connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* jail connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* jc filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* jenkins\_credential \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jenkins\_job \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* jenkins\_job\_info \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* jenkins\_plugin \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* jenkins\_plugin \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jenkins\_plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jenkins\_plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* jenkins\_plugin modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* jenkins\_script \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* jenkins\_script \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jira \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* jira \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jira \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* json\_query filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* kdeconfig \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* keycloak module utils \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* keycloak module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* keycloak module\_utils \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* keycloak\_authentication \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_client \- add <code>valid\_post\_logout\_redirect\_uris</code> option to configure post logout redirect URIs for a client\, and <code>backchannel\_logout\_url</code> option to configure the backchannel logout URL for a client \([https\://github\.com/ansible\-collections/community\.general/issues/6812](https\://github\.com/ansible\-collections/community\.general/issues/6812)\, [https\://github\.com/ansible\-collections/community\.general/issues/4892](https\://github\.com/ansible\-collections/community\.general/issues/4892)\, [https\://github\.com/ansible\-collections/community\.general/pull/11473](https\://github\.com/ansible\-collections/community\.general/pull/11473)\)\.
* keycloak\_client\_rolemapping \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_client\_rolemapping\, keycloak\_realm\_rolemapping\, keycloak\_group \- optimize retrieval of groups by name to use Keycloak search API with exact matching instead of fetching all groups \([https\://github\.com/ansible\-collections/community\.general/pull/11503](https\://github\.com/ansible\-collections/community\.general/pull/11503)\)\.
* keycloak\_component \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_realm \- add <code>first\_broker\_login\_flow</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/11622](https\://github\.com/ansible\-collections/community\.general/pull/11622)\)\.
* keycloak\_realm \- add <code>webAuthnPolicyPasswordlessPasskeysEnabled</code> parameter \([https\://github\.com/ansible\-collections/community\.general/pull/11197](https\://github\.com/ansible\-collections/community\.general/pull/11197)\)\.
* keycloak\_realm \- add support for <code>localizationTexts</code> option in Keycloak realms \([https\://github\.com/ansible\-collections/community\.general/pull/11513](https\://github\.com/ansible\-collections/community\.general/pull/11513)\)\.
* keycloak\_realm\_key \- add support for auto\-generated key providers \(<code>rsa\-generated</code>\, <code>rsa\-enc\-generated</code>\, <code>hmac\-generated</code>\, <code>aes\-generated</code>\, <code>ecdsa\-generated</code>\, <code>ecdh\-generated</code>\, <code>eddsa\-generated</code>\)\, <code>java\-keystore</code> provider\, additional algorithms \(HMAC\, ECDSA\, ECDH\, EdDSA\, AES\)\, and new config options \(<code>secret\_size</code>\, <code>key\_size</code>\, <code>elliptic\_curve</code>\, <code>keystore</code>\, <code>keystore\_password</code>\, <code>key\_alias</code>\, <code>key\_password</code>\)\. Also makes <code>config\.private\_key</code> and <code>config\.certificate</code> optional as they are only required for imported key providers \([https\://github\.com/ansible\-collections/community\.general/pull/11468](https\://github\.com/ansible\-collections/community\.general/pull/11468)\)\.
* keycloak\_realm\_key \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_realm\_rolemapping \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_user\_rolemapping \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keycloak\_userprofile \- add support for <code>selector</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/11309](https\://github\.com/ansible\-collections/community\.general/pull/11309)\)\.
* keycloak\_userprofile \- add support for additional user profile attribute\-validations available in Keycloak \([https\://github\.com/ansible\-collections/community\.general/issues/9048](https\://github\.com/ansible\-collections/community\.general/issues/9048)\, [https\://github\.com/ansible\-collections/community\.general/pull/11285](https\://github\.com/ansible\-collections/community\.general/pull/11285)\)\.
* keycloak\_userprofile \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* keys\_filter plugin\_utils plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* keys\_filter\.py plugin utils \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* known\_hosts module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* known\_hosts module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* layman \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* layman \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* ldap module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* ldap\_attrs \- add <code>binary\_attributes</code> and <code>honor\_binary</code> parameters to handle binary attribute values \([https\://github\.com/ansible\-collections/community\.general/pull/11558](https\://github\.com/ansible\-collections/community\.general/pull/11558)\)\.
* ldap\_attrs \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* ldap\_entry \- add <code>binary\_attributes</code> and <code>honor\_binary</code> parameters to handle creating objects with attributes set to binary values \([https\://github\.com/ansible\-collections/community\.general/pull/11558](https\://github\.com/ansible\-collections/community\.general/pull/11558)\)\.
* ldap\_entry \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* ldap\_inc \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* ldap\_search \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* ldap\_search \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* linode \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* linode inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* linode inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* listen\_ports\_facts \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* listen\_ports\_facts \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* listen\_ports\_facts \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* lmdb\_kv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* locale\_gen \- extend the search for available locales to include <code>/usr/local/share/i18n/SUPPORTED</code> in Debian and Ubuntu systems \([https\://github\.com/ansible\-collections/community\.general/issues/10964](https\://github\.com/ansible\-collections/community\.general/issues/10964)\, [https\://github\.com/ansible\-collections/community\.general/pull/11046](https\://github\.com/ansible\-collections/community\.general/pull/11046)\)\.
* locale\_gen \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* logentries \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* logentries callback plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lookup plugin passwordstore \- modernize internal <code>check\_output2\(\)</code> helper using <code>subprocess\.run\(\)</code> and rename it to <code>run\_backend\_cmd\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11655](https\://github\.com/ansible\-collections/community\.general/pull/11655)\)\.
* lvm\_pv \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* lxc connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxc connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxc\_container \- refactor function <code>create\_script</code>\, using <code>subprocess\.Popen\(\)</code>\, to a new module\_utils <code>\_lxc</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11204](https\://github\.com/ansible\-collections/community\.general/pull/11204)\)\.
* lxc\_container \- use <code>tempfile\.TemporaryDirectory\(\)</code> instead of <code>mkdtemp\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11323](https\://github\.com/ansible\-collections/community\.general/pull/11323)\)\.
* lxd connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxd inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* lxd module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxd module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* lxd\_container \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* macports \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* mail \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* manageiq module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* manageiq\_alert\_profiles \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* maven\_artifact \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* memset module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* merge\_variables \- extend type detection failure message to allow users for easier failure debugging \([https\://github\.com/ansible\-collections/community\.general/pull/11107](https\://github\.com/ansible\-collections/community\.general/pull/11107)\)\.
* merge\_variables lookup plugin \- extended merging capabilities added \([https\://github\.com/ansible\-collections/community\.general/pull/11536](https\://github\.com/ansible\-collections/community\.general/pull/11536)\)\.
* merge\_variables lookup plugin \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* modprobe \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* modprobe \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* monit \- add <code>monit\_version</code> return value also when the module has succeeded \([https\://github\.com/ansible\-collections/community\.general/pull/11255](https\://github\.com/ansible\-collections/community\.general/pull/11255)\)\.
* monit \- use <code>Enum</code> to represent the possible states \([https\://github\.com/ansible\-collections/community\.general/pull/11245](https\://github\.com/ansible\-collections/community\.general/pull/11245)\)\.
* mssql\_db \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* nagios \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* net\_tools\.pritunl\.api module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* netcup\_dns \- support diff mode \([https\://github\.com/ansible\-collections/community\.general/pull/11376](https\://github\.com/ansible\-collections/community\.general/pull/11376)\)\.
* nmap inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* nmcli \- add idempotency check \([https\://github\.com/ansible\-collections/community\.general/pull/11114](https\://github\.com/ansible\-collections/community\.general/pull/11114)\)\.
* nmcli \- add support for IPv6 routing rules \([https\://github\.com/ansible\-collections/community\.general/issues/7094](https\://github\.com/ansible\-collections/community\.general/issues/7094)\, [https\://github\.com/ansible\-collections/community\.general/pull/11413](https\://github\.com/ansible\-collections/community\.general/pull/11413)\)\.
* nmcli \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* nmcli \- fix comparison of type \([https\://github\.com/ansible\-collections/community\.general/pull/11121](https\://github\.com/ansible\-collections/community\.general/pull/11121)\)\.
* nmcli \- fix idempotency for MAC VLAN interfaces when using <code>macvlan\.tap</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11551](https\://github\.com/ansible\-collections/community\.general/pull/11551)\)\.
* nmcli module \- add <code>vxlan\_parent</code> option required for multicast <code>vxlan\_remote</code> addresses\; add <code>vxlan</code> to list of bridgeable devices \([https\://github\.com/ansible\-collections/community\.general/pull/11182](https\://github\.com/ansible\-collections/community\.general/pull/11182)\)\.
* nmcli modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* nomad\_job \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nomad\_job \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* nomad\_job\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nomad\_token \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nosh \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* nosh \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* nsupdate \- add support for server FQDN and the GSS\-TSIG key algorithm \([https\://github\.com/ansible\-collections/community\.general/issues/5730](https\://github\.com/ansible\-collections/community\.general/issues/5730)\, [https\://github\.com/ansible\-collections/community\.general/pull/11425](https\://github\.com/ansible\-collections/community\.general/pull/11425)\)\.
* nsupdate \- replace <code>list\(map\(\.\.\.\)\)</code> constructs with Python comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/11590](https\://github\.com/ansible\-collections/community\.general/pull/11590)\)\.
* nsupdate modules plugin \- replace aliased errors with proper Python error \([https\://github\.com/ansible\-collections/community\.general/pull/11391](https\://github\.com/ansible\-collections/community\.general/pull/11391)\)\.
* ocapi\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ocapi\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* ocapi\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* ocapi\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* ocapi\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* oci\_utils module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* oci\_utils module utils \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* oci\_utils module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* oci\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* omapi\_host \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* one\_image \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_image\_info \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_service \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_vm \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_vm \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
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
* online module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* opennebula inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* opennebula inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* opentelemetry callback plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* osx\_defaults \- add support for <code>dict</code> type values\, including <code>dict\_mode</code> option to merge keys into an existing dictionary \([https\://github\.com/ansible\-collections/community\.general/issues/238](https\://github\.com/ansible\-collections/community\.general/issues/238)\, [https\://github\.com/ansible\-collections/community\.general/pull/11659](https\://github\.com/ansible\-collections/community\.general/pull/11659)\)\.
* osx\_defaults \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_device \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11231](https\://github\.com/ansible\-collections/community\.general/pull/11231)\)\.
* packet\_device modules \- mark <code>\%</code> templating as <code>noqa</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* packet\_ip\_subnet \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_project \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* packet\_sshkey \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_volume \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* packet\_volume \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* pam\_limits \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pamd \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* pamd \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* parted \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* parted \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* passwordstore lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* pear \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* pids \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pids \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* pmem \- simplify text tests without using regular expression \([https\://github\.com/ansible\-collections/community\.general/pull/11388](https\://github\.com/ansible\-collections/community\.general/pull/11388)\)\.
* portage \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* pritunl\_org \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_org\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_user\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pubnub\_blocks \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pulp\_repo \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pushbullet modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* read\_csv \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* read\_csv \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* redfish\_config \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* redfish\_info \- add Redfish Root data to results of successful <code>CheckAvailability</code> command \([https\://github\.com/ansible\-collections/community\.general/pull/11504](https\://github\.com/ansible\-collections/community\.general/pull/11504)\)\.
* redfish\_utils module utils \- adds support of <code>\@Redfish\.Settings</code> in <code>ComputerSystem</code> attributes for <code>set\_boot\_override</code> function \([https\://github\.com/ansible\-collections/community\.general/issues/11297](https\://github\.com/ansible\-collections/community\.general/issues/11297)\, [https\://github\.com/ansible\-collections/community\.general/pull/11322](https\://github\.com/ansible\-collections/community\.general/pull/11322)\)\.
* redfish\_utils module utils \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* redfish\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* redfish\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* redhat\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* redhat\_subscription \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* redhat\_subscription \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* redis cache plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* redis lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* revbitspss lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* rhevm \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* rhsm\_repository \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* riak \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* rundeck module utils \- improve handling the return value <code>exception</code>\. It now contains the full stack trace of the exception\, while the message is included in <code>msg</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11149](https\://github\.com/ansible\-collections/community\.general/pull/11149)\)\.
* rundeck module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* runit \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* scaleway inventory plugin \- added support for <code>SCW\_PROFILE</code> environment variable for the <code>scw\_profile</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/11310](https\://github\.com/ansible\-collections/community\.general/issues/11310)\, [https\://github\.com/ansible\-collections/community\.general/pull/11311](https\://github\.com/ansible\-collections/community\.general/pull/11311)\)\.
* scaleway inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* scaleway module utils \- added <code>scw\_profile</code> parameter with <code>SCW\_PROFILE</code> environment variable support \([https\://github\.com/ansible\-collections/community\.general/issues/11313](https\://github\.com/ansible\-collections/community\.general/issues/11313)\, [https\://github\.com/ansible\-collections/community\.general/pull/11314](https\://github\.com/ansible\-collections/community\.general/pull/11314)\)\.
* scaleway module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* scaleway\_ip \- added <code>project</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/11367](https\://github\.com/ansible\-collections/community\.general/issues/11367)\, [https\://github\.com/ansible\-collections/community\.general/pull/11368](https\://github\.com/ansible\-collections/community\.general/pull/11368)\)\.
* scaleway\_security\_group \- added <code>project</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/11364](https\://github\.com/ansible\-collections/community\.general/issues/11364)\, [https\://github\.com/ansible\-collections/community\.general/pull/11366](https\://github\.com/ansible\-collections/community\.general/pull/11366)\)\.
* scaleway\_user\_data modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* selinux\_permissive \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sensu\_check \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sensu\_check \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sensu\_client \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sensu\_handler \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sensu\_silence \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* sensu\_silence modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* sensu\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sensu\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* sensu\_subscription \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* seport \- adds support for DCCP and SCTP protocols \([https\://github\.com/ansible\-collections/community\.general/pull/11486](https\://github\.com/ansible\-collections/community\.general/pull/11486)\)\.
* seport \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* serverless \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* shelvefile lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* shutdown action plugin \- add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* shutdown action plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* slack \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* slackpkg \- refactor function <code>query\_packages\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11390](https\://github\.com/ansible\-collections/community\.general/pull/11390)\)\.
* slackpkg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* snap \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* snmp\_facts \- simplify and improve code using standard Ansible validations \([https\://github\.com/ansible\-collections/community\.general/pull/11148](https\://github\.com/ansible\-collections/community\.general/pull/11148)\)\.
* solaris\_zone \- execute external commands using Ansible construct \([https\://github\.com/ansible\-collections/community\.general/pull/11192](https\://github\.com/ansible\-collections/community\.general/pull/11192)\)\.
* solaris\_zone \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* solaris\_zone \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sorcery \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* spectrum\_model\_attrs \- convert <code>\%</code> templating to f\-string \([https\://github\.com/ansible\-collections/community\.general/pull/11229](https\://github\.com/ansible\-collections/community\.general/pull/11229)\)\.
* spotinst\_aws\_elastigroup \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* statusio\_maintenance \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* sudoers \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sudoers \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* supervisorctl \- added an additional condition for generating the error \'no such process\' \([https\://github\.com/ansible\-collections/community\.general/issues/11621](https\://github\.com/ansible\-collections/community\.general/issues/11621)\, [https\://github\.com/ansible\-collections/community\.general/pull/11632](https\://github\.com/ansible\-collections/community\.general/pull/11632)\)\.
* svc \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* svc \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* svr4pkg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* swupd \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* timestamp callback plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* timezone \- replace <code>list\(map\(\.\.\.\)\)</code> constructs with Python comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/11590](https\://github\.com/ansible\-collections/community\.general/pull/11590)\)\.
* timezone \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* to\_ini filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* tss lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* univention\_umc module utils \- update code to Python 3 \([https\://github\.com/ansible\-collections/community\.general/pull/11122](https\://github\.com/ansible\-collections/community\.general/pull/11122)\)\.
* univention\_umc module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
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
* utm\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
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
* wakeonlan \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* wdc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* wdc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* wdc\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* wdc\_redfish\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* wsl connection plugin \- add option <code>wsl\_remote\_ssh\_shell\_type</code>\. Support PowerShell in addition to cmd as the Windows shell \([https\://github\.com/ansible\-collections/community\.general/issues/11307](https\://github\.com/ansible\-collections/community\.general/issues/11307)\, [https\://github\.com/ansible\-collections/community\.general/pull/11308](https\://github\.com/ansible\-collections/community\.general/pull/11308)\)\.
* wsl connection plugin \- adjust variable name for integration tests \([https\://github\.com/ansible\-collections/community\.general/pull/11190](https\://github\.com/ansible\-collections/community\.general/pull/11190)\)\.
* wsl connection plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* wsl connection plugin \- replace aliased errors with proper Python error \([https\://github\.com/ansible\-collections/community\.general/pull/11391](https\://github\.com/ansible\-collections/community\.general/pull/11391)\)\.
* wsl connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* wsl connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* xbps \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* xbps \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* xcc\_redfish\_command \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* xcc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11110](https\://github\.com/ansible\-collections/community\.general/pull/11110)\)\.
* xcc\_redfish\_command \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* xenserver module utils \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* xenserver module utils \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* xenserver\_guest modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* xfs\_quota \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* xml \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* xml \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* yaml cache plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* yum\_versionlock \- remove redundant conversion to unicode in command output \([https\://github\.com/ansible\-collections/community\.general/pull/11093](https\://github\.com/ansible\-collections/community\.general/pull/11093)\)\.
* zfs \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* zone connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* zone connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* zypper \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* zypper\_repository \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.

<a id="community-libvirt"></a>
#### community\.libvirt

* virt\_cloud\_instance \- added commands return field to provide visibility into executed commands during VM provisioning\.
* virt\_install \- added commands return field to provide visibility into executed commands during VM provisioning\.
* virt\_install \- added support for memoryBacking source type configuration\, including memfd for shared memory \([https\://github\.com/ansible\-collections/community\.libvirt/issues/228](https\://github\.com/ansible\-collections/community\.libvirt/issues/228)\)\.
* virt\_install \- added support for primary value attribute \(\_value or value\) in dynamic dict options that require a primary value alongside additional attributes\.
* virt\_install \- enhanced cloud\_init configuration handling for sub\-options \(meta\-data\, user\-data\, and network\-config\) to support both string and dictionary inputs\.
* virt\_install \- refactored common virt\-install functionality into module\_utils and doc\_fragments to enable code reuse between modules\.
* virt\_volume \- New return key/value pairs \'Type\'\, \'Capacity\' and \'Allocation\' were added to command \'list\_volumes\' \([https\://github\.com/ansible\-collections/community\.libvirt/issues/187](https\://github\.com/ansible\-collections/community\.libvirt/issues/187)\)
* virt\_volume \- added ability to resize volumes if defined capacity is different\. If volume already exists and defined capacity in XML differs a resize is attempted\.

<a id="community-mysql"></a>
#### community\.mysql

* Update imports from ansible\.module\_utils\.\_text to use ansible\.module\_utils\.common\.text\.converters
* mysql\_role \- add <code>sql\_log\_bin</code> option to disable binary logging for the connection \([https\://github\.com/ansible\-collections/community\.mysql/issues/742](https\://github\.com/ansible\-collections/community\.mysql/issues/742)\)\.

<a id="community-postgresql"></a>
#### community\.postgresql

* postgresql\_privs \- support MAINTAIN privilege on tables \(added in PostgreSQL 17\) \([https\://github\.com/ansible\-collections/community\.postgresql/pull/888](https\://github\.com/ansible\-collections/community\.postgresql/pull/888)\)\.

<a id="community-proxmox-1"></a>
#### community\.proxmox

* inventory plugin \- add want\_post\_filtering\_facts to delay fact gathering until filtering has completed \([https\://github\.com/ansible\-collections/community\.proxmox/pull/261](https\://github\.com/ansible\-collections/community\.proxmox/pull/261)\)\.
* inventory plugin\, plugin\_utils \- replace deprecated <code>ansible\.module\_utils\.common\.\_collections\_compat</code> imports with <code>collections\.abc</code> from the Python standard library \([https\://github\.com/ansible\-collections/community\.proxmox/issues/241](https\://github\.com/ansible\-collections/community\.proxmox/issues/241)\)\.
* proxmox \- Add api\_timeout option for all modules \([https\://github\.com/ansible\-collections/community\.proxmox/pull/253](https\://github\.com/ansible\-collections/community\.proxmox/pull/253)\)\.
* proxmox \- add <code>totp</code> authentification support \([https\://github\.com/ansible\-collections/community\.proxmox/pull/265](https\://github\.com/ansible\-collections/community\.proxmox/pull/265)\)\.
* proxmox \- add a new helper <em class="title-reference">create\_proxmox\_module\(\)</em> which adds generic auth args and constraints\, and merges in the module\-specific args and options \([https\://github\.com/ansible\-collections/community\.proxmox/pull/289](https\://github\.com/ansible\-collections/community\.proxmox/pull/289)\)\.
* proxmox \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox \- set <code>state</code> as not <code>required</code> and set default value <code>present</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/292](https\://github\.com/ansible\-collections/community\.proxmox/pull/292)\)\.
* proxmox \- update <code>proxmoxer</code> required dependencies to <code>\>\=2\.3</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/265](https\://github\.com/ansible\-collections/community\.proxmox/pull/265)\)\.
* proxmox\_disk \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox\_kvm \- add option to migrate local disks as well \([https\://github\.com/ansible\-collections/community\.proxmox/pull/240](https\://github\.com/ansible\-collections/community\.proxmox/pull/240)\)\.
* proxmox\_kvm \- add qemu parameter <code>spice\_enhancements</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/324](https\://github\.com/ansible\-collections/community\.proxmox/pull/324)\)\.
* proxmox\_kvm \- add qemu parameter <code>virtiofs</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/336](https\://github\.com/ansible\-collections/community\.proxmox/pull/336)\)\.
* proxmox\_kvm \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox\_node \- add alias <code>certificate\_file\_path</code> for <code>cert</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/331](https\://github\.com/ansible\-collections/community\.proxmox/pull/331)\)\.
* proxmox\_node \- add alias <code>node</code> for <code>node\_name</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/331](https\://github\.com/ansible\-collections/community\.proxmox/pull/331)\)\.
* proxmox\_node \- add alias <code>private\_key\_file\_path</code> for <code>key</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/331](https\://github\.com/ansible\-collections/community\.proxmox/pull/331)\)\.
* proxmox\_node \- add new parameter <code>certificate</code> to pass raw PEM encoded certificate \([https\://github\.com/ansible\-collections/community\.proxmox/pull/331](https\://github\.com/ansible\-collections/community\.proxmox/pull/331)\)\.
* proxmox\_node \- add new parameter <code>private\_key</code> to pass raw PEM encoded private key \([https\://github\.com/ansible\-collections/community\.proxmox/pull/331](https\://github\.com/ansible\-collections/community\.proxmox/pull/331)\)\.
* proxmox\_node\_info \- add information on node network interfaces to node information output \([https\://github\.com/ansible\-collections/community\.proxmox/pull/220](https\://github\.com/ansible\-collections/community\.proxmox/pull/220)\)\.
* proxmox\_node\_info \- add information on node\'s PVE version \([https\://github\.com/ansible\-collections/community\.proxmox/pull/225](https\://github\.com/ansible\-collections/community\.proxmox/pull/225)\)\.
* proxmox\_role \- add role\'s privs on the return data \([https\://github\.com/ansible\-collections/community\.proxmox/pull/283](https\://github\.com/ansible\-collections/community\.proxmox/pull/283)\)\.
* proxmox\_snap\_info \- Adds a new module to list snapshots or a specific snapshot for VM or container \([https\://github\.com/ansible\-collections/community\.proxmox/issues/229](https\://github\.com/ansible\-collections/community\.proxmox/issues/229)\)\.
* proxmox\_storage \- Add support for RBD \(RADOS Block Device\) storage \([https\://github\.com/ansible\-collections/community\.proxmox/issues/329](https\://github\.com/ansible\-collections/community\.proxmox/issues/329)\)\.
* proxmox\_storage \- Add support for ZFS thin\-provisioning \([https\://github\.com/ansible\-collections/community\.proxmox/pull/265](https\://github\.com/ansible\-collections/community\.proxmox/pull/265)\)\.
* proxmox\_storage \- Add the option namespace for PBS storage \([https\://github\.com/ansible\-collections/community\.proxmox/pull/282](https\://github\.com/ansible\-collections/community\.proxmox/pull/282)\)
* proxmox\_storage \- add feature of subdirectory in CIFS share\. \([https\://github\.com/ansible\-collections/community\.proxmox/pull/214](https\://github\.com/ansible\-collections/community\.proxmox/pull/214)\)\.
* proxmox\_storage \- enhanced error handling and parameters validation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- fix passing nfs\_options to API payload \([https\://github\.com/ansible\-collections/community\.proxmox/issues/203](https\://github\.com/ansible\-collections/community\.proxmox/issues/203)\, [https\://github\.com/ansible\-collections/community\.proxmox/pull/221](https\://github\.com/ansible\-collections/community\.proxmox/pull/221)\)\.
* proxmox\_storage \- fixed CIFS authentication by sending username and password parameters to proxmoxer \([https\://github\.com/ansible\-collections/community\.proxmox/pull/214](https\://github\.com/ansible\-collections/community\.proxmox/pull/214)\)\.
* proxmox\_storage \- refactor the validation of storage options \([https\://github\.com/ansible\-collections/community\.proxmox/pull/266](https\://github\.com/ansible\-collections/community\.proxmox/pull/266)\)\.
* proxmox\_storage \- the parameter <code>state</code> now has a default value of <code>present</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- when <code>state\=present</code> parameters <code>content</code> and <code>nodes</code> are now not required \([https\://github\.com/ansible\-collections/community\.proxmox/pull/315](https\://github\.com/ansible\-collections/community\.proxmox/pull/315)\)\.
* proxmox\_storage\_contents\_info \- Add support for content type <code>import</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/260](https\://github\.com/ansible\-collections/community\.proxmox/pull/260)\)\.
* proxmox\_zone\, proxmox\_vnet\, proxmox\_subnet \- make sdn modules compatible with pve8 \([https\://github\.com/ansible\-collections/community\.proxmox/pull/254](https\://github\.com/ansible\-collections/community\.proxmox/pull/254)\)\.

<a id="community-routeros-4"></a>
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
* api\_info\, api\_modify \- add <code>2g\-probe\-delay</code> field to path <code>interface wifi steering</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>aaa\.\*</code>\, <code>channel\.\*</code>\, <code>datapath\.\*</code>\, <code>interworking\.\*</code>\, <code>security\.\*</code>\, <code>steering\.\*</code> sub\-fields to path <code>interface wifi configuration</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>deprioritize\-unii\-3\-4</code>\, <code>reselect\-interval</code>\, <code>reselect\-time</code> fields to path <code>interface wifi channel</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>multi\-passphrase\-group</code> field to path <code>interface wifi security</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>prefix\-pool</code> field to and fix default of <code>address\-pool</code> for <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/430](https\://github\.com/ansible\-collections/community\.routeros/pull/430)\)\.
* api\_info\, api\_modify \- add <code>send\-email\-from</code>\, <code>send\-email\-to</code> and <code>send\-smtp\-server</code> to <code>system watchdog</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/429](https\://github\.com/ansible\-collections/community\.routeros/pull/429)\)\.
* api\_info\, api\_modify \- add <code>traffic\-processing</code> field to path <code>interface wifi datapath</code> and <code>interface wifi configuration</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/424](https\://github\.com/ansible\-collections/community\.routeros/pull/424)\)\.
* api\_info\, api\_modify \- add <code>use\-bfd</code> to <code>routing ospf interface\-template</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/425](https\://github\.com/ansible\-collections/community\.routeros/pull/425)\)\.
* api\_info\, api\_modify \- add <code>vrf</code> to <code>ip service</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/426](https\://github\.com/ansible\-collections/community\.routeros/pull/426)\)\.
* api\_info\, api\_modify \- add default values for fields <code>ciphers</code> in <code>ip ssh</code>\, <code>mvrp</code> in  <code>interface vlan</code>\, and <code>mvrp\-forbidden</code> in <code>interface bridge vlan</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/439/](https\://github\.com/ansible\-collections/community\.routeros/pull/439/)\)\.
* api\_info\, api\_modify \- add missing attribute <code>radsec\-timeout</code> for the <code>radius</code> path which exists since RouterOS version 7\.19\.6 \([https\://github\.com/ansible\-collections/community\.routeros/pull/412](https\://github\.com/ansible\-collections/community\.routeros/pull/412)\)\.
* api\_info\, api\_modify \- add missing parameters to path <code>interface bridge</code> and <code>interface bridge port</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/423](https\://github\.com/ansible\-collections/community\.routeros/pull/423)\)\.
* api\_info\, api\_modify \- add support for path <code>disk settings</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/422](https\://github\.com/ansible\-collections/community\.routeros/pull/422)\)\.
* api\_info\, api\_modify \- add support for path <code>interface dot1x client</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/414](https\://github\.com/ansible\-collections/community\.routeros/pull/414)\)\.
* api\_info\, api\_modify \- add support for path <code>interface dot1x server</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/413](https\://github\.com/ansible\-collections/community\.routeros/pull/413)\)\.
* api\_info\, api\_modify \- add support for path <code>ip socks access</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/431](https\://github\.com/ansible\-collections/community\.routeros/pull/431)\)\.
* api\_info\, api\_modify \- add support for paths <code>ip hotspot</code>\, <code>ip hotspot profile</code>\, <code>ip hotspot user</code>\, <code>ip hotspot user profile</code>\, <code>ip hotspot walled\-garden</code>\, and <code>ip hotspot walled\-garden ip</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/418](https\://github\.com/ansible\-collections/community\.routeros/pull/418)\)\.
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
* api\_info\, api\_modify \- allow the <code>fib</code> parameter to be disabled for the <code>routing table</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/368](https\://github\.com/ansible\-collections/community\.routeros/issues/368)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/417](https\://github\.com/ansible\-collections/community\.routeros/pull/417)\)\.
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
* api\_info\, api\_modify \- remove primary key constraint on \'peer\' for path <code>ip ipsec identity</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/421](https\://github\.com/ansible\-collections/community\.routeros/pull/421)\)\.
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
* sap\_control\_exec \- Add local socket support \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/66](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/66)\)
* sap\_control\_exec\, sap\_hostctrl\_exec \- QoL and Error handling \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/81](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/81)\)
* sap\_control\_exec\, sap\_hostctrl\_exec \- Refactor to use shared utilities \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/78](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/78)\)
* sap\_hdbsql \- Add error handling and secure flags for hdbsql \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/75](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/75)\)
* sap\_hdbsql \- Add new parameter named properties \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/79](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/79)\)
* sap\_hostctrl\_exec \- Add new module and tests \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/67](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/67)\)
* sap\_system\_facts \- Add SID and permission check to facts module \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/73](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/73)\)
* sapcar\_extract \- Add overwrite mode and improve exist validation \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/77](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/77)\)

<a id="community-sops-1"></a>
#### community\.sops

* load\_vars \- now supports ansible\-core 2\.21\'s way of actually loading variables\, instead of returning <code>ansible\_facts</code>\. The behavior for this can be controlled through the new <code>return\_method</code> option\, which is by default set to <code>auto</code>\. On ansible\-core 2\.21\+\, <code>auto</code> behaves the same as <code>vars\-only</code> \(return proper variables\)\, and for ansible\-core before 2\.21 the same as <code>facts\-only</code> \(return <code>ansible\_facts</code>\) \([https\://github\.com/ansible\-collections/community\.sops/pull/283](https\://github\.com/ansible\-collections/community\.sops/pull/283)\)\.

<a id="community-windows"></a>
#### community\.windows

* Add official support for Ansible 2\.20

<a id="containers-podman-3"></a>
#### containers\.podman

* Add configuration for new Ansible release
* Fix CI of Podman Search modul
* Fix tests for new Podman
* add passthrough and none log driver options

<a id="dellemc-enterprise-sonic"></a>
#### dellemc\.enterprise\_sonic

* plugins \- Change all instances of \'after\(generated\)\' to \'after\_generated\' to address sanity errors \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/609](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/609)\)\.
* sonic\_aaa \- Add support for accounting options \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/559](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/559)\)\.
* sonic\_interfaces \- Support for BAM/MSA configuration \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/567](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/567)\)\.
* sonic\_lag\_interfaces \- Add support for \'speed\' and \'adv\_speed\' \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/572](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/572)\)\.
* sonic\_radius\_server \- Add support for RADIUS TLS security profile \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/615](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/615)\)\.
* sonic\_system \- Add support for banner and login exec\-timeout options \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/614](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/614)\)\.
* sonic\_vrrp \- Add support for vrrp \'preempt\_delay\' option \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/571](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/571)\)\.
* sonic\_vxlans \- Add support for QoS mode \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/611](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/611)\)\.

<a id="dellemc-openmanage"></a>
#### dellemc\.openmanage

* Added support for OpenManage Enterprise version 4\.4 and 4\.5\.
* The OpenManage Enterprise\, OpenManage Enterprise Modular and OpenManage Enterprise Integration for VMware vCenter modules are now compatible with Ansible Core version 2\.20\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Supported new environment variable \"ANSIBLE\_FORTIMANAGER\_ENABLE\_LOG\" to enable/disable logging for FortiManager Ansible Collection\.
* Supported new environment variable \"ANSIBLE\_FORTIMANAGER\_VERSION\_CHECK\" to enable/disable version checking performed by the FortiManager Ansible Collection\.
* Supported new modules to configure FortiProxy\.
* Supported new schemas in FortiManager 7\.0\.15\, 7\.4\.8\, 7\.6\.4\.
* Supported new schemas in FortiManager 7\.0\.16\, 7\.2\.12\, 7\.4\.9\, 7\.4\.10\, 7\.6\.5\, 7\.6\.6

<a id="google-cloud"></a>
#### google\.cloud

* gcp\_alloydb\_\* \- added gcp\_alloydb\_cluster\, gcp\_alloydb\_instance\, gcp\_alloydb\_backup\, and gcp\_alloydb\_user modules \([https\://github\.com/ansible\-collections/google\.cloud/pull/722](https\://github\.com/ansible\-collections/google\.cloud/pull/722)\)
* gcp\_cloudbuildv2\_\* \- added gcp\_cloudbuildv2\_connection and gcp\_cloudbuildv2\_repository modules \([https\://github\.com/ansible\-collections/google\.cloud/pull/729](https\://github\.com/ansible\-collections/google\.cloud/pull/729)\)\.
* gcp\_colab\_\* \- added four new modules \(gcp\_colab\_notebook\_execution\, gcp\_colab\_runtime\, gcp\_colab\_runtime\_template\, and gcp\_colab\_schedule\) \([https\://github\.com/ansible\-collections/google\.cloud/pull/747](https\://github\.com/ansible\-collections/google\.cloud/pull/747)\)\.
* gcp\_compute\_instance\_\* \- renamed the <em class="title-reference">tags\.items</em> field to <em class="title-reference">tags\.tag\_values</em>\. The old naming is still available but will be removed in a future release\. \([https\://github\.com/ansible\-collections/google\.cloud/pull/750](https\://github\.com/ansible\-collections/google\.cloud/pull/750)\)\.
* gcp\_sql\_instance \- add <em class="title-reference">allocated\_ip\_range</em> to <em class="title-reference">settings\.ip\_configuration</em> for private IP Cloud SQL instances \(name of the allocated IP range in the VPC\) \([https\://github\.com/ansible\-collections/google\.cloud/pull/744](https\://github\.com/ansible\-collections/google\.cloud/pull/744)\)\.
* gcp\_vertexai\_\* \- added 18 Vertex AI modules \(gcp\_vertexai\_dataset\, gcp\_vertexai\_deployment\_resource\_pool\, gcp\_vertexai\_endpoint\, gcp\_vertexai\_endpoint\_with\_model\_garden\_deployment\, gcp\_vertexai\_feature\_group\, gcp\_vertexai\_feature\_group\_feature\, gcp\_vertexai\_feature\_online\_store\, gcp\_vertexai\_feature\_online\_store\_featureview\, gcp\_vertexai\_featurestore\, gcp\_vertexai\_featurestore\_entitytype\, gcp\_vertexai\_featurestore\_entitytype\_feature\, gcp\_vertexai\_index\, gcp\_vertexai\_index\_endpoint\, gcp\_vertexai\_index\_endpoint\_deployed\_index\, gcp\_vertexai\_metadata\_store\, gcp\_vertexai\_rag\_engine\_config\, gcp\_vertexai\_reasoning\_engine\, gcp\_vertexai\_tensorboard\) \([https\://github\.com/ansible\-collections/google\.cloud/pull/743](https\://github\.com/ansible\-collections/google\.cloud/pull/743)\)\.

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* All <code>module\_utils</code> are now marked as <strong>private</strong>\. None of the modules were intended for public use\.
* DNS support is now generally available\.
* floating\_ip \- Unassign Floating IP before deleting it\.
* load\_balancer\_network \- Add <code>ip\_range</code> argument to attach a load balancer to a specific subnet\.
* primary\_ip \- Added the Primary IP <code>location</code> name to the return values \(<code>hcloud\_primary\_ip\.location</code>\)\.
* primary\_ip \- Added the <code>location</code> argument to create a Primary IP in a specific location\.
* primary\_ip \- Assign to new server if <code>server</code> is changed\.
* primary\_ip \- Unassign Primary IP before deleting it\.
* primary\_ip \- Unassign primary\_ip if <code>server</code> is null\.
* primary\_ip\_info \- Added the Primary IPs <code>location</code> name to the return values \(<code>hcloud\_primary\_ip\_info\[\]\.location</code>\)\.
* server \- Rebuilding a Server now supports the <code>user\_data</code> argument\.
* server\_network \- Add <code>ip\_range</code> argument to attach a load balancer to a specific subnet\.
* storage\_box \- New module to create and manage Storage Boxes in Hetzner\.
* storage\_box \- The module is no longer marked as experimental\.
* storage\_box\_info \- New module to gather infos about Hetzner Storage Boxes\.
* storage\_box\_info \- The module is no longer marked as experimental\.
* storage\_box\_snapshot \- New module to create and manage Storage Box Snapshots in Hetzner\.
* storage\_box\_snapshot \- The module is no longer marked as experimental\.
* storage\_box\_snapshot\_info \- New module to gather infos about Hetzner Storage Box Snapshots\.
* storage\_box\_snapshot\_info \- The module is no longer marked as experimental\.
* storage\_box\_subaccount \- New module to create and manage Storage Box Subaccounts in Hetzner\.
* storage\_box\_subaccount \- Replace the label based name workaround\, with the new Storage Box Subaccount name property in the API\.
* storage\_box\_subaccount \- The module is no longer marked as experimental\.
* storage\_box\_subaccount\_info \- New module to gather infos about Hetzner Storage Box Subaccounts\.
* storage\_box\_subaccount\_info \- Replace the label based name workaround\, with the new Storage Box Subaccount name property in the API\.
* storage\_box\_subaccount\_info \- The module is no longer marked as experimental\.
* storage\_box\_type\_info \- New module to gather infos about Hetzner Storage Box Types\.
* storage\_box\_type\_info \- The module is no longer marked as experimental\.
* txt\_record \- Add new txt\_record filter to help format TXT \, e\.g\. <code>\"\{\{ \'v\=spf1 include\:\_spf\.example\.net \~all\' \| hetzner\.hcloud\.txt\_record \}\}\"</code>\.

<a id="hitachivantara-vspone-block-6"></a>
#### hitachivantara\.vspone\_block

* Added \"playbooks/vsp\_direct/vsp\_storage\_connection\_session\_example\.yml\" as a sample playbook demonstrating session\-based storage operations\.
* Added a new \"hv\_pav\_alias\" module to manage PAV \(Parallel Access Volume\) alias assignments for Mainframe based VSP block storage systems\.
* Added a new \"hv\_pav\_alias\_facts\" module to gather facts about PAV aliases from Mainframe based VSP block storage systems\.
* Added a new \"hv\_sds\_block\_audit\_log\_setting\" module to support configuration of audit log settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_audit\_log\_setting\_facts\" module to retrieve audit log setting from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_dump\_log\_file\" module to retrieve and dump log information from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_dump\_log\_status\_facts\" module to retrieve and dump log status information from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_environment\_setting\_facts\" module to retrieve encryption environment configuration settings from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_environment\_settings\" module to enable or disable encryption functionality on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_key\" module to create and delete encryption keys on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_key\_count\_facts\" module to retrieve information about the number of encryption keys from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_encryption\_key\_facts\" module to retrieve detailed information about encryption keys from VSP One SDS Block and Cloud systems\.
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
* Added a new \"hv\_sds\_block\_protection\_domain\" module to manage protection domains including creation\, modification\, and data relocation operations on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_remote\_path\_group\" module to create remote path group\, add remote path to a remote path group\, remove remote path from remote path group\, and delete remote path group on VSP One SDS Block systems\.
* Added a new \"hv\_sds\_block\_remote\_path\_group\_facts\" module to retrieve information about remote path groups from VSP One SDS Block systems\.
* Added a new \"hv\_sds\_block\_session\" module to generate and discard session on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_session\_facts\" module to retrieve information about sessions on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_snmp\_settings\" module to manage SNMP settings including agent enablement\, version configuration\, trap settings\, authentication settings\, and system group information on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_snmp\_settings\_facts\" module to retrieve SNMP settings including agent status\, version configuration\, trap settings\, authentication settings\, and system group information from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_spare\_node\" module to manage spare node configuration including node identification\, fault domain assignment\, network configuration\, and BMC settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_spare\_node\_facts\" module to retrieves spare node information and configuration details from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_external\_auth\_server\_setting\" module to configure external authentication server settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_external\_auth\_server\_setting\_facts\" module to retrieve external authentication server settings from the VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_system\" module to manage storage system configuration including certificate management\, cache settings\, and other system\-level configurations on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_user\_auth\_setting\" module to configure external authentication server settings on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_storage\_user\_auth\_setting\_facts\" module to retrieve user authentication settings from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_user\_group\" module to Create and update user groups on VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_user\_group\_facts\" module to retrieve user groups from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_web\_server\" module to manages the web server access setting for VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_sds\_block\_web\_server\_facts\" module to retrieve the web server access setting from VSP One SDS Block and Cloud systems\.
* Added a new \"hv\_session\" module to generate and discard session on VSP block storage systems\.
* Added a new \"hv\_session\_facts\" module to retrieve information about sessions on VSP block storage systems\.
* Added a new \"hv\_snapshot\_family\_facts\" module to retrieve information about snapshot family of the provided LDEV ID from VSP block storage systems\.
* Added a new \"hv\_supported\_host\_mode\_facts\" module to retrieve detailed information about supported host mode options available in a given VSP block storage system\.
* Added a new \"hv\_vclone\_parent\_volume\_facts\" module to retrieve information about virtual clone parent volume from VSP block storage systems\.
* Added notes to module documentation indicating that a few modules are not supported for BHE and higher models\.
* Added support for Mainframe z16\.
* Added support for SVOS 10\.5\.1\.
* Added support for latest software version 01\.18\.02 for VSP One SDS Block and Cloud systems\.
* Added support to \"Add user to user groups\" to hv\_sds\_block\_user module\.
* Added support to \"Delete a user\" to hv\_sds\_block\_user module\.
* Added support to \"Disable encryption for storage pool using ID\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Disable encryption for storage pool\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Enable encryption for storage pool by ID\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Enable encryption for storage pool by name\" to hv\_sds\_block\_storage\_pool module\.
* Added support to \"Remove user from user groups\" to hv\_sds\_block\_user module\.
* Added support to \"Update user settings\" to hv\_sds\_block\_user module\.
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

<a id="hitachivantara-vspone-object"></a>
#### hitachivantara\.vspone\_object

* Enhanced <em class="title-reference">hv\_storage\_component</em> module to support storage components of type ARRAY for VSP One B20 series storage systems\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_replication\_policy \- Enabled support for logging in via partition ip
* ibm\_svc\_initial\_setup \- Added support for managing anomaly settings
* ibm\_svc\_manage\_volume \- Added support for addressing volume via UID
* ibm\_svc\_manage\_volume \- Added support for autoexpand\, preferrednode and cache parameters

<a id="infoblox-nios-modules"></a>
#### infoblox\.nios\_modules

* CI/CD \- Added PyGObject support and improved dependency handling
* nios\_dtc\_lbdn \- Added support for auth\_zones with enhanced change detection for string and object formats\, including proper handling when entries are removed

<a id="kaytus-ksmanage-1"></a>
#### kaytus\.ksmanage

* Modify the contact email in the README\.md file\. \([https\://github\.com/KSManageOSS/kaytus\.ksmanage/pull/39](https\://github\.com/KSManageOSS/kaytus\.ksmanage/pull/39)\)\.

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* Remove deprecated import from <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1053](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1053)\)\.
* helm \- add <code>release\_values</code> key to <code>status</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_info \- add <code>release\_values</code> key to <code>status</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.

<a id="microsoft-ad"></a>
#### microsoft\.ad

* Add official support for Ansible 2\.20

<a id="microsoft-iis"></a>
#### microsoft\.iis

* Add official support for Ansible 2\.20

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* na\_ontap\_ems\_filter \- new option <em class="title-reference">parameter\_criteria</em> added in REST\, requires ONTAP 9\.13\.1 or later\.
* na\_ontap\_lun \- updated documentation for unsupported REST parameters\.
* na\_ontap\_net\_ifgrp \- Update <em class="title-reference">mode</em> parameter to specify allowed values\.
* na\_ontap\_nfs \- new option <em class="title-reference">credential\_cache</em> added in REST\.
* na\_ontap\_snapmirror \- new options <em class="title-reference">time\_out</em>\, <em class="title-reference">wait\_for\_completion</em> added in REST\.
* na\_ontap\_snapmirror \- updated documentation for <em class="title-reference">identity\_preserve</em> and <em class="title-reference">max\_transfer\_rate</em>\.
* na\_ontap\_volume\_efficiency\- AWS Lambda support added to the module\.
* na\_ontap\_volume\_efficiency\- Added <em class="title-reference">wait\_for\_completion</em> and <em class="title-reference">time\_out</em> parameters to fix time out errors for long running operations\.

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

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* purefa\_connection \- Add new parameters for key refresh and connection refresh\, as well as ability to update existing connection
* purefa\_info \- Added more data to hostgroup volume information to support NVMe connections
* purefa\_info \- Added tags info to entities that support them
* purefa\_network \- Addressed issues found in update\_interface
* purefa\_phonehome \- Added <code>excludes</code> parameter\, supported from Purity//FA 6\.10\.0
* purefa\_pod \- Fixed pydantic issue from lastest SDK version
* purefa\_policy \- Added Continuous Availability support for SMB policies

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* purefa\_ad \- Added support for local servers using the <code>server</code> parameter\.
* purefb\_ad \- Added test and rotate states
* purefb\_ad \- Remove doc references to FQDNs as SPNs are the required method\.
* purefb\_ad \- Updated encryption algorithms to use correct values
* purefb\_ds \- Allow directory services to be modified for internal NFS servers
* purefb\_ds \- Update test state to allow specific tests to be run
* purefb\_info \- Added MAC address information for LAGs

<a id="splunk-es-4"></a>
#### splunk\.es

* Added <code>limit</code> parameter to splunk\_finding\_info\, splunk\_investigation\_info\, and splunk\_response\_plan\_info modules to control the maximum number of results returned\.
* Added splunk\_finding module to manage \(create/update\) Splunk Enterprise Security findings\.
* Added splunk\_finding\_info module to query information about Splunk Enterprise Security findings\.
* Added splunk\_investigation module to manage \(create/update\) Splunk Enterprise Security investigations\.
* Added splunk\_investigation\_info module to query information about Splunk Enterprise Security investigations\.
* Added splunk\_investigation\_type module to manage \(create/update\) Splunk Enterprise Security investigation types \(incident types\)\.
* Added splunk\_investigation\_type\_info module to query information about Splunk Enterprise Security investigation types\.
* Added splunk\_response\_plan module to manage \(create/update/delete\) Splunk Enterprise Security response plans\.
* Added splunk\_response\_plan\_execution module to apply/remove response plans to investigations and manage task statuses\.
* Added splunk\_response\_plan\_execution\_info module to query applied response plans and task statuses on investigations\.
* Added splunk\_response\_plan\_info module to query information about Splunk Enterprise Security response plans\.
* Modernized Python code across the collection by removing Python 2 compatibility patterns \(<code>from \_\_future\_\_ import</code> and <code>\_\_metaclass\_\_ \= type</code>\)\, updating to modern <code>super\(\)</code> syntax\, converting <code>\.format\(\)</code> calls to f\-strings\, and consolidating duplicated <code>\_check\_argspec\(\)</code> methods into the shared <code>check\_argspec\(\)</code> helper\.
* Removed legacy module support code from module\_utils/splunk\.py as all modules now use the modern action plugin architecture\.
* Removed parse\_splunk\_args function that was only used by deprecated legacy modules\.
* Simplified SplunkRequest class initialization by removing unused parameters \(module\, headers\, override\)\.
* Updated SplunkRequest to require action\_module and connection parameters\, improving code clarity and maintainability\.
* splunk\_notes \- new module to manage notes for findings\, investigations\, and response plan tasks\.
* splunk\_notes\_info \- new module to query notes from findings\, investigations\, and response plan tasks\.

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* Feat\: add some parameters to the icinga service module \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/289](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/289)\)

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* activation\_key \- add <code>content\_view\_environments</code> parameter to support multi CV \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1935](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1935)\)
* content\_view \- add support for lifecycle environments in rolling content views
* convert2rhel role \- removed subscription support as it\'s been unused since Katello 4\.12 \(05/2024\)
* job\_invocation \- add <code>feature</code> parameter \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1923](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1923)\)
* locations role \- Added <code>state</code> parameter to manage resource presence\.

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* Add module vm\_snapshot\_revert to revert a virtual machine to a snapshot\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/281](https\://github\.com/ansible\-collections/vmware\.vmware/issues/281)
* cluster\_ha \- Add value to allow disabling admission control policy Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/227](https\://github\.com/ansible\-collections/vmware\.vmware/issues/227)
* content\_library\_item\_info \- Add item storage information to item result
* esxi\_hosts \- Added option to rename reserved variables to avoid potential conflicts with ansible\-core and resolve warnings\. fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/273](https\://github\.com/ansible\-collections/vmware\.vmware/issues/273)
* module\_deploy\_vm\_base \- Removed redundant code by using new vm placement service methods in deploy modules
* vm \- Add module to manage virtual machines
* vm \- Add the ability to set the annotation of a VM\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/310](https\://github\.com/ansible\-collections/vmware\.vmware/issues/310)
* vm\_apply\_customization \- Added module to apply different customization specs to a VM
* vm\_list\_group\_by\_clusters\_info \- Add the ability to use the absolute path for the group name\. This can be used to avoid group name collisions\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/297](https\://github\.com/ansible\-collections/vmware\.vmware/issues/297)
* vms \- Add setting to disable population of ansible\_host to the inventory Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/pull/317](https\://github\.com/ansible\-collections/vmware\.vmware/pull/317)
* vms \- Added option to rename reserved variables to avoid potential conflicts with ansible\-core and resolve warnings\. fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/273](https\://github\.com/ansible\-collections/vmware\.vmware/issues/273)

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* Disable check mode for all non\-info modules in this collection\. Check mode was never supported for these modules\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/363](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/363)

<a id="vultr-cloud"></a>
#### vultr\.cloud

* Added pagination support by adding <code>api\_results\_per\_page</code> to the common attributes\.
* bare\_metal \- Added support for multi\-disk operation mode by adding <code>mdisk\_mode</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/165](https\://github\.com/vultr/ansible\-collection\-vultr/issues/165)\)\.
* object\_storage \- Object storage subscriptions require specifying a tier upon creation\, added <code>tier</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/135](https\://github\.com/vultr/ansible\-collection\-vultr/issues/135)\)\.
* snapshot \- Added UEFI support adding <code>uefi</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/160](https\://github\.com/vultr/ansible\-collection\-vultr/pull/160)\)\.

<a id="breaking-changes--porting-guide-2"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-12"></a>
#### Ansible\-core

* psrp \- Changed the default of <code>negotiate\_service</code> used to build the Kerberos Service Principal Name from <code>WSMAN</code> to <code>host</code>\. This aligns the defaults to how the native PowerShell PSRemoting client works on Windows and ensures that Kerberos can be used by more Windows targets by default\. No deprecation period is used for this change as <code>host</code> is a builtin SPN to Windows and should improve compatibility out of the box\. To go back to the old behaviour for any reason\, set <code>ansible\_psrp\_negotiate\_service\=WSMAN</code> in the host vars\.

<a id="community-aws-2"></a>
#### community\.aws

* community\.aws collection \- Due to the AWS SDKs announcing the end of support for Python less than 3\.8 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\)\, support for Python less than 3\.8 by this collection has been deprecated and will be removed in release 10\.0\.0\. \([https\://github\.com/ansible\-collections/community\.aws/pull/2304](https\://github\.com/ansible\-collections/community\.aws/pull/2304)\)\.

<a id="community-mysql-1"></a>
#### community\.mysql

* Update imports from ansible\.module\_utils\.six to use their python3 equivalent\. This change will make this collection incompatible for managed hosts on python2\.7\.

<a id="dellemc-enterprise-sonic-1"></a>
#### dellemc\.enterprise\_sonic

* sonic\_qos\_wred \- Add support for yellow and red colors \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/574](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/574)\)\.

<a id="splunk-es-5"></a>
#### splunk\.es

* Removed deprecated modules that were scheduled for removal on 2024\-09\-01
* adaptive\_response\_notable\_event \- Use splunk\.es\.splunk\_adaptive\_response\_notable\_events instead
* correlation\_search \- Use splunk\.es\.splunk\_correlation\_searches instead
* data\_input\_monitor \- Use splunk\.es\.splunk\_data\_inputs\_monitor instead
* data\_input\_network \- Use splunk\.es\.splunk\_data\_inputs\_network instead

<a id="deprecated-features-3"></a>
### Deprecated Features

* The <code>netapp\.cloudmanager</code> collection is considered unmaintained and will be removed from Ansible 15 if no one starts maintaining it again before Ansible 15\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/44891](https\://forum\.ansible\.com/t/44891)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install netapp\.cloudmanager</code>\.

<a id="ansible-core-13"></a>
#### Ansible\-core

* The <code>get\_all\_subclasses\(\)</code> function from <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.24\. Use <code>get\_all\_subclasses\(\)</code> from <code>ansible\.module\_utils\.common\.\_utils</code> instead\.
* The <code>get\_platfrom\(\)</code> function from <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.24\. Use <code>platform\.system\(\)</code> from the Python standard library instead\.
* The <code>load\_platform\_subclass\(\)</code> function from <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.24\. Use <code>get\_platform\_subclass\(\)</code> from <code>ansible\.module\_utils\.common\.sys\_info</code> instead\.
* <code>PluginLoader</code> \- Deprecate unused <code>aliases</code> attribute\. Plugins in a collection should define aliases in the <code>meta/runtime\.yml</code> file using the <code>redirect</code> field instead\.
* <code>ansible\.module\_utils\.six</code> \- The <code>six</code> compatibility library provided at <code>ansible\.module\_utils\.six</code> is deprecated\, and planned for removal in ansible\-core 2\.24
* apt\_key \- deprecate in favor of deb822\_repository\.
* apt\_repository \- deprecate in favor of deb822\_repository\.
* connection plugins \- Added a soft deprecation on the connection attributes <code>has\_native\_async</code> and <code>always\_pipeline\_modules</code>\. Connection plugins that wish to apply custom behaviour around pipelining should instead override the method <code>is\_pipelining\_enabled\(self\, wrap\_async\=False\)</code> added in Ansible 2\.19\. For backwards compatibility no runtime deprecation warning is emitted but will be in the future\.

<a id="amazon-aws-2"></a>
#### amazon\.aws

* aws\_ec2 \- the <code>tags</code> host variable has been deprecated to avoid conflicts with Ansible reserved variable names and will be removed in a release after 2026\-12\-01\. Use <code>ec2\_tags</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2847](https\://github\.com/ansible\-collections/amazon\.aws/pull/2847)\)\.
* aws\_ec2 \- the <code>use\_contrib\_script\_compatible\_ec2\_tag\_keys</code> option has been deprecated and will be removed in a release after 2026\-12\-01\. Use the <code>ec2\_tags</code> structure instead\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2854](https\://github\.com/ansible\-collections/amazon\.aws/pull/2854)\)
* aws\_ec2 \- the <code>use\_contrib\_script\_compatible\_sanitization</code> option has been deprecated and will be removed in a release after 2026\-12\-01\. Use Ansible\'s default group name sanitization instead\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2854](https\://github\.com/ansible\-collections/amazon\.aws/pull/2854)\)
* aws\_rds \- the <code>tags</code> host variable has been deprecated to avoid conflicts with Ansible reserved variable names and will be removed in a release after 2026\-12\-01\. Use <code>rds\_tags</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2847](https\://github\.com/ansible\-collections/amazon\.aws/pull/2847)\)\.
* ec2\_vpc\_dhcp\_option \- the <code>dhcp\_config</code> return value has been deprecated and will be removed in a release after 2026\-12\-01\. Use <code>dhcp\_options</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* ec2\_vpc\_dhcp\_option\_info \- the <code>dhcp\_config</code> return value has been deprecated and will be removed in a release after 2026\-12\-01\. Use <code>dhcp\_options</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* route53 \- the <code>region</code> parameter for latency\-based routing has been deprecated and will be removed in a release after 2027\-06\-01\. The <code>routing\_region</code> parameter behaves exactly as <code>region</code> behaves today and should be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2893](https\://github\.com/ansible\-collections/amazon\.aws/issues/2893)\)\.
* route53 \- the <code>values</code> key in the <code>resource\_record\_sets</code> return value has been deprecated in favor of <code>record\_values</code> for Jinja2 compatibility\. The <code>values</code> key will be removed in a release after 2026\-12\-01 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.

<a id="community-aws-3"></a>
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

<a id="community-general-4"></a>
#### community\.general

* All module utils\, plugin utils\, and doc fragments will be made <strong>private</strong> in community\.general 13\.0\.0\. This means that they will no longer be part of the public API of the collection\, and can have breaking changes even in bugfix releases\. If you depend on importing code from the module or plugin utils\, or use one of the doc fragments\, please [comment in the issue to discuss this](https\://github\.com/ansible\-collections/community\.general/issues/11312)\. Note that this does not affect any use of community\.general in task files\, roles\, or playbooks \([https\://github\.com/ansible\-collections/community\.general/issues/11312](https\://github\.com/ansible\-collections/community\.general/issues/11312)\, [https\://github\.com/ansible\-collections/community\.general/pull/11320](https\://github\.com/ansible\-collections/community\.general/pull/11320)\)\.
* aix\_devices \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_filesystem \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_inittab \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_lvg \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_lvol \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* cloud module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* database module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* dconf \- deprecate fallback mechanism when <code>gi\.repository</code> is not available\; fallback will be removed in community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11088](https\://github\.com/ansible\-collections/community\.general/pull/11088)\)\.
* known\_hosts module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* layman \- ClearLinux was made EOL in July 2025\.\; the module will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11087](https\://github\.com/ansible\-collections/community\.general/pull/11087)\)\.
* layman \- Gentoo deprecated <code>layman</code> in mid\-2023\; the module will be removed from community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11070](https\://github\.com/ansible\-collections/community\.general/pull/11070)\)\.
* monit \- support for Monit version 5\.18 or older is deprecated and will be removed in community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11254](https\://github\.com/ansible\-collections/community\.general/pull/11254)\)\.
* puppet \- the <code>timeout</code> parameter is deprecated and will be removed in community\.general 14\.0\.0\. \([https\://github\.com/ansible\-collections/community\.general/pull/11658](https\://github\.com/ansible\-collections/community\.general/pull/11658)\)\.
* pushbullet \- module relies on Python package supporting Python 3\.2 only\; the module will be removed from community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11224](https\://github\.com/ansible\-collections/community\.general/pull/11224)\)\.
* saslprep module utils \- this module utils is not used by community\.general and will thus be removed from community\.general 13\.0\.0\. If you are using it from another collection\, please copy it over \([https\://github\.com/ansible\-collections/community\.general/pull/11205](https\://github\.com/ansible\-collections/community\.general/pull/11205)\)\.
* spotinst\_aws\_elastigroup \- module relies on Python package supporting Python 2\.7 only\; the module will be removed from community\.general 13\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11069](https\://github\.com/ansible\-collections/community\.general/pull/11069)\)\.

<a id="community-proxmox-2"></a>
#### community\.proxmox

* proxmox \- Certificate verification default changes from <code>false</code> to <code>true</code> with version 2\.0\.0 \([https\://github\.com/ansible\-collections/community\.proxmox/pull/256](https\://github\.com/ansible\-collections/community\.proxmox/pull/256)\)\.

<a id="community-routeros-5"></a>
#### community\.routeros

* api\_find\_and\_modify \- the current defaults for <code>ignore\_dynamic</code> and <code>ignore\_builtin</code> \(both <code>false</code>\) have been deprecated and will change to <code>true</code> in community\.routeros 4\.0\.0\. To avoid deprecation messages\, please set the value explicitly to <code>true</code> or <code>false</code>\, if you have not already done so\. We recommend to set them to <code>true</code>\, unless you have a good reason to set them to <code>false</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/399](https\://github\.com/ansible\-collections/community\.routeros/pull/399)\)\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* hcloud inventory \- The <code>hcloud\_datacenter</code> host variable is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_location</code> host variable instead\.
* network\_info \- The <code>hcloud\_network\_info\[\]\.servers\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_network\_info\[\]\.servers\[\]\.location</code> return value instead\.
* primary\_ip \- The <code>datacenter</code> argument is deprecated and will be removed after 1 July 2026\. Please use the <code>location</code> argument instead\.
* primary\_ip \- The <code>hcloud\_primary\_ip\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_primary\_ip\.location</code> return value instead\.
* primary\_ip\_info \- The <code>hcloud\_primary\_ip\_info\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_primary\_ip\_info\[\]\.location</code> return value instead\.
* server \- The <code>datacenter</code> argument is deprecated and will be removed after 1 July 2026\. Please use the <code>location</code> argument instead\.
* server \- The <code>hcloud\_server\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_server\.location</code> return value instead\.
* server\_info \- The <code>hcloud\_server\_info\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_server\_info\[\]\.location</code> return value instead\.

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* helm \- the <code>status\.values</code> return value has been deprecated and will be removed in a release after 2027\-01\-08\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_info \- the <code>status\.values</code> return value has been deprecated and will be removed in a release after 2027\-01\-08\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* Deprecate modules that have been moved to the new vmware\.vmware collection\. Includes vcenter\_vm\_guest\_customization\, vcenter\_vm\_hardware\_adapter\_sata\, vcenter\_vm\_hardware\_adapter\_scsi\, vcenter\_vm\_hardware\_cdrom\, vcenter\_vm\_hardware\_cpu\, vcenter\_vm\_hardware\_disk\, vcenter\_vm\_hardware\_ethernet\, vcenter\_vm\_hardware\_memory\, vcenter\_vm

<a id="removed-features-previously-deprecated-2"></a>
### Removed Features \(previously deprecated\)

* The awx\.awx collection has been removed from Ansible 14\.
  The collection is undergoing a heavy [refactoring](https\://forum\.ansible\.com/t/7404) and currently does not align with the standards for the community package\.
  See [the removal discussion](https\://forum\.ansible\.com/t/44706) for details\.
  Users can still install this collection with <code>ansible\-galaxy collection install awx\.awx</code>\.
* The deprecated <code>cisco\.dnac</code> collection has been removed \([https\://forum\.ansible\.com/t/45609](https\://forum\.ansible\.com/t/45609)\)\.
* The deprecated <code>junipernetworks\.junos</code> collection has been removed \([https\://forum\.ansible\.com/t/44869](https\://forum\.ansible\.com/t/44869)\)\.

<a id="ansible-core-14"></a>
#### Ansible\-core

* Removed \'required\' option from get\_bin\_path API \([https\://github\.com/ansible/ansible/issues/85998](https\://github\.com/ansible/ansible/issues/85998)\)\.
* Removed deprecated <code>ansible\.builtin\.paramiko</code> connection plugin \([https\://github\.com/ansible/ansible/issues/86002](https\://github\.com/ansible/ansible/issues/86002)\)\. Setting the <code>connection</code> keyword to <code>persistent</code> or <code>smart</code> no longer attempts to use <code>paramiko</code>\.
* Removed deprecated <code>ansible\.module\_utils\.compat\.paramiko</code> \([https\://github\.com/ansible/ansible/issues/86001](https\://github\.com/ansible/ansible/issues/86001)\)\.
* Removed deprecated <code>handle\_stats\_and\_callbacks</code> parameter of the <code>StrategyBase\.\_load\_included\_file</code> method\. \([https\://github\.com/ansible/ansible/issues/86003](https\://github\.com/ansible/ansible/issues/86003)\)
* Removed deprecated ability to import <code>datetime</code>\, <code>signal</code>\, <code>types</code>\, <code>chain</code>\, <code>repeat</code>\, <code>map</code> and <code>shlex\_quote</code> from <code>ansible\.module\_utils\.basic</code>\.
* compat\.datetime \- removed deprecated datetime compat APIs \([https\://github\.com/ansible/ansible/issues/86000](https\://github\.com/ansible/ansible/issues/86000)\)\.
* git \- removed deprecated alias gpg\_whitelist \([https\://github\.com/ansible/ansible/issues/86004](https\://github\.com/ansible/ansible/issues/86004)\)\.
* interpreter\_discovery \- removed auto\_legacy and auto\_legacy\_slient options \([https\://github\.com/ansible/ansible/issues/85995](https\://github\.com/ansible/ansible/issues/85995)\)\.
* module\_utils \- Remove previously deprecated <code>safe\_eval</code> function \(\#85996\) \(\#85999\)

<a id="splunk-es-6"></a>
#### splunk\.es

* adaptive\_response\_notable\_event module has been removed\. Use splunk\.es\.splunk\_adaptive\_response\_notable\_events resource module instead\.
* correlation\_search module has been removed\. Use splunk\.es\.splunk\_correlation\_searches resource module instead\.
* correlation\_search\_info module has been removed\. Use splunk\.es\.splunk\_correlation\_search\_info instead\.
* data\_input\_monitor module has been removed\. Use splunk\.es\.splunk\_data\_inputs\_monitor resource module instead\.
* data\_input\_network module has been removed\. Use splunk\.es\.splunk\_data\_inputs\_network resource module instead\.

<a id="security-fixes"></a>
### Security Fixes

<a id="amazon-aws-3"></a>
#### amazon\.aws

* arn \- fix potential ReDoS vulnerability in ARN parsing regex by using negated character class instead of non\-greedy quantifier \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2884](https\://github\.com/ansible\-collections/amazon\.aws/pull/2884)\)\.
* ec2\_security\_group \- fix potential ReDoS vulnerability in security group ID parsing regex by using negated character classes and adding end anchor \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2884](https\://github\.com/ansible\-collections/amazon\.aws/pull/2884)\)\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* win\_dns\_record \- Fixed a security risk where <code>AllowUpdateAny</code> was hardcoded for non\-SRV records\, allowing any authenticated user to update DNS records\. Added a new parameter <code>allow\_update\_any</code> which defaults to <code>false</code> \([https\://issues\.redhat\.com/browse/ACA\-5193](https\://issues\.redhat\.com/browse/ACA\-5193)\)\.

<a id="kubernetes-core-4"></a>
#### kubernetes\.core

* Selectively redact sensitive info from kubeconfig instead of applying blanket <code>no\_log\=True</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1014](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1014)\)\.

<a id="bugfixes-3"></a>
### Bugfixes

<a id="ansible-core-15"></a>
#### Ansible\-core

* Fix Windows LIB env var corruption \([https\://github\.com/ansible\-collections/ansible\.windows/issues/297](https\://github\.com/ansible\-collections/ansible\.windows/issues/297)\)\.
* Fix <code>AnsibleModule\.human\_to\_bytes\(\)</code>\, which was never adjusted after the standalone <code>human\_to\_bytes\(\)</code> got a new parameter <code>default\_unit</code> \([https\://github\.com/ansible/ansible/pull/85259](https\://github\.com/ansible/ansible/pull/85259)\)\.
* Fix interpreter discovery on delegated <code>async</code> tasks \([https\://github\.com/ansible/ansible/issues/86491](https\://github\.com/ansible/ansible/issues/86491)\)
* Fix source metadata validation \([https\://github\.com/ansible/ansible/pull/86320](https\://github\.com/ansible/ansible/pull/86320)\)\.
* Fix up <code>powershell</code> shell commands when using a connection plugin that does not support stdin/pipeline input \- [https\://github\.com/ansible/ansible/issues/86397](https\://github\.com/ansible/ansible/issues/86397)
* Fix up the Action plugin <code>\_make\_tmp\_path</code> error to only include the command run rather than the shell\'s dataclass repr from <code>mkdtemp</code>\.
* Variable loading now uses file source instead of variables when invalidly formmated vars file is loaded\.
* Windows \- ignore temporary file cleanup warning when using AnsibleModule to compile C\# utils\. This should reduce the number of warnings that can safely be ignored when running PowerShell modules \- [https\://github\.com/ansible/ansible/issues/85976](https\://github\.com/ansible/ansible/issues/85976)
* <code>ansible\-galaxy collection list</code> \- issue a warning when a collection\'s namespace and name do not match its filepath\. \([https\://github\.com/ansible/ansible/issues/69813](https\://github\.com/ansible/ansible/issues/69813)\)
* <code>ansible\-galaxy collection list\|install</code> \- list collections based on reference \(the fqcn used to refer to them in a playbook\)\, not based on their documented name\. \([https\://github\.com/ansible/ansible/issues/69813](https\://github\.com/ansible/ansible/issues/69813)\)
* <code>ansible\-galaxy collection verify</code> \- fail collection verification when a collection\'s namespace and name  do not match its filepath\. \([https\://github\.com/ansible/ansible/issues/69813](https\://github\.com/ansible/ansible/issues/69813)\)
* <code>ansible\-galaxy install</code>/<code>ansible\-galaxy collection download</code> \- collections from git repositories with a tag or sha version no longer emit detached head warning messages \([https\://github\.com/ansible/ansible/issues/86169](https\://github\.com/ansible/ansible/issues/86169)\)\.
* <code>ansible\.builtin\.pip</code> \- Running the built\-in pip module with <code>check\_mode</code> and packages coming from VCS URLs\, archives\, or local filepaths now correctly outputs the <code>changed</code> status of the task\. Previously\, it was always reported as changed due to improper package name resolution\.  \([https\://github\.com/ansible/ansible/pull/85623](https\://github\.com/ansible/ansible/pull/85623)\)
* <code>ansible</code>\, <code>ansible\-console</code> \- fix executing <code>\- meta\: end\_play</code> tasks\.
* ansible\-connection \- Prevent unpickling failures in module contexts by ensuring that AnsibleTaggedObjects in pickled responses are converted to plain types in <code>JsonRpcServer</code>\.
* ansible\-galaxy \- raise an error when wrong regex value specified in collection\_skeleton\_ignore\.
* ansible\-galaxy \- warn instead of raising an error when no valid role or collections paths exist \([https\://github\.com/ansible/ansible/pull/86341](https\://github\.com/ansible/ansible/pull/86341)\)
* ansible\-galaxy collection \- Fix using the server configuration for <code>validate\_certs</code> when downloading collections\. \([https\://github\.com/ansible/ansible/issues/86694](https\://github\.com/ansible/ansible/issues/86694)\)
* ansible\-test \- Add missing bootstrapping for a target Python version in a controller container\.
* ansible\-test \- Fix docker hostname parsing
* ansible\-test \- Fix traceback when requesting windows integration tests for multiple managed hosts\.
* ansible\-test \- Missing git submodules in the source tree now result in a warning instead of an error\.
* ansible\-test \- Restore code coverage reporting for Python code residing in integration tests\.
* ansible\-test \- The runtime\-metadata sanity test now ignores pre\-release and build identifiers in collection versions\. This prevents errors if a tombstone version is <code>X\.0\.0</code>\, while the collection\'s version is <code>X\.0\.0\-prerelease</code> \([https\://github\.com/ansible/ansible/issues/85193](https\://github\.com/ansible/ansible/issues/85193)\)\.\"
* ansible\-test \- Upgrade <code>expat</code> during provisioning of Fedora 42 remote instances\.
* ansible\-test \- When using the <code>env \-\-list\-files</code> option\, non\-filename output is now sent to stderr\.
* ansible\_facts\[os\_\*\] \- Contained wrong information\, if ClearLinux parsing was tried before falling back to general os\-release parsing
* ansible\_local will no longer trigger variable injection default value deprecation\.
* ansible\_virtualization\_role and ansible\_virtualization\_type facts \- fix the detection of vms running inside FreeBSD Bhyve hypervisor and detection of jails  \([https\://github\.com/ansible/ansible/pull/85767](https\://github\.com/ansible/ansible/pull/85767)\)
* apt \- Stop the \>\= operator from being ignored for packages that are not already installed \([https\://github\.com/ansible/ansible/pull/85254](https\://github\.com/ansible/ansible/pull/85254)\)
* apt \- handle comma separated packages from recommends while installing local deb package \([https\://github\.com/ansible/ansible/issues/86609](https\://github\.com/ansible/ansible/issues/86609)\)\.
* apt \- recreate the APT lists directory \(/var/lib/apt/lists by default\) if missing \([https\://github\.com/ansible/ansible/issues/61176](https\://github\.com/ansible/ansible/issues/61176)\)\.
* basic \- fail in controlled manner when <code>run\_command\(\)</code> attempts to parse a command with broken syntax passed in as a string \([https\://github\.com/ansible/ansible/issues/85719](https\://github\.com/ansible/ansible/issues/85719)\)\.
* cache plugins based on the BaseFileCache class will now sanitize keys to avoid names that could cause issues with the storage path
* callbacks \- The value of <code>TaskResult\.task\.connection</code> properly reflects the loaded connection name used\. Previously\, incorrect values were reported in some cases\.
* config lookup now properly factors in variables and show\_origin when checking entries from the global configuration\.
* config lookup now uses preexisting constants for templating when needed\.
* copy \- honor directory\_mode when copying directories with remote\_src\=True \([https\://github\.com/ansible/ansible/issues/81292](https\://github\.com/ansible/ansible/issues/81292)\)\.
* copy \- when a single\-file local directory was specified as the source\, <code>changed</code> used to be <code>false</code> even when the source was actually copied\. It now makes sure <code>changed</code> is <code>true</code> in this case\. \([https\://github\.com/ansible/ansible/issues/85833](https\://github\.com/ansible/ansible/issues/85833)\)
* deb822\_repository \- Remove <code>Install\-Python\-Debian</code> from files outputted by the <code>deb822\_repository</code> module \([https\://github\.com/ansible/ansible/issues/86395](https\://github\.com/ansible/ansible/issues/86395)\)
* deb822\_repository no longer over\-normalizes repository names when generating sources list filenames\, preventing collisions for names that differ by case\, underscores\, or dots \([https\://github\.com/ansible/ansible/issues/86243](https\://github\.com/ansible/ansible/issues/86243)\)
* display \- Fix <code>getuser</code> fallback error handling on Python 3\.13 and later\. \([https\://github\.com/ansible/ansible/issues/86142](https\://github\.com/ansible/ansible/issues/86142)\)
* dnf \- When installing a dnf module\, install and enable when missing\, upgrade when present \([https\://github\.com/ansible/ansible/issues/73457](https\://github\.com/ansible/ansible/issues/73457)\)
* dnf \- fix package installation when specifying architecture without version \(e\.g\.\, <code>libgcc\.i686</code>\) where a different architecture of the same package is already installed \([https\://github\.com/ansible/ansible/issues/86156](https\://github\.com/ansible/ansible/issues/86156)\)\.
* dnf5 \- return failure message which occurred while running RPM scriptlet \([https\://github\.com/ansible/ansible/issues/86117](https\://github\.com/ansible/ansible/issues/86117)\)\.
* file module \- issue warning when attempting to access files/directories the user lacks permissions on instead of silently treating them as absent \([https\://github\.com/ansible/ansible/issues/57573](https\://github\.com/ansible/ansible/issues/57573)\)
* first\_found \- Correct the \"Include tasks only if one of the files exists\, otherwise skip\" example\.
* first\_found \- ensure file lookup under <code>files</code> directory when the task action cannot be resolved \([https\://github\.com/ansible/ansible/issues/85655](https\://github\.com/ansible/ansible/issues/85655)\)\.
* first\_found \- use the task action to determine the directory \(templates/vars/files\) containing the file when the lookup is not used as task loop\.
* galaxy \- previously\, some corrupted cache files could cause Ansible Galaxy to fail with a traceback\. This has been corrected to display a clear error message explaining how to resolve the problem\. \([https\://github\.com/ansible/ansible/issues/85918](https\://github\.com/ansible/ansible/issues/85918)\)
* get\_url \- fix regex for GNU Digest line which is used in comparing checksums \([https\://github\.com/ansible/ansible/issues/86132](https\://github\.com/ansible/ansible/issues/86132)\)\.
* getent \- handle non\-empty string for split parameter value \([https\://github\.com/ansible/ansible/issues/85720](https\://github\.com/ansible/ansible/issues/85720)\)\.
* git \- Correct the output of git checkmode to a failure when the <code>version</code> supplied is an invalid ref \([https\://github\.com/ansible/ansible/issues/51580](https\://github\.com/ansible/ansible/issues/51580)\)
* include\_role would emit a syntax error on X\_from options errors\, but a task failure when missing a role to make it consistent now it also emits a task failure on missing tasks\_from\, which makes it subject to error handling in the play\.
* include\_role\, would ignore missing X\_from files if the subdir \(tasks/vars/handlers/defaults\) did not exist\, now it is a proper error\.
* iptables \- The module can now detect when a extensions added with the module <code>match</code> argument have  been automatically imported by other module arguments such as <code>uid\_owner</code> and prevents duplicate extension imports which previously caused an error \([https\://github\.com/ansible/ansible/issues/84387](https\://github\.com/ansible/ansible/issues/84387)\)\.
* local connection \- Fix <code>getuser</code> fallback error handling on Python 3\.13 and later\.
* local connection \- Pass correct type to become plugins when checking password \([https\://github\.com/ansible/ansible/issues/86458](https\://github\.com/ansible/ansible/issues/86458)\)
* modules \- fix AnsiballZ wrapper code escaping of sitecustomize
* option argument deprecations now have a proper alternative help text\.
* package\, service\, gather\_facts \- fix templating module\_defaults for modules executed by these action plugins\. \([https\://github\.com/ansible/ansible/issues/85848](https\://github\.com/ansible/ansible/issues/85848)\)
* package\_facts \- typecast bytes to string while returning facts \([https\://github\.com/ansible/ansible/issues/85937](https\://github\.com/ansible/ansible/issues/85937)\)\.
* password lookup plugin \- replace random\.SystemRandom\(\) with secrets\.SystemRandom\(\) when generating passwords \([https\://github\.com/ansible/ansible/issues/85956](https\://github\.com/ansible/ansible/issues/85956)\, [https\://github\.com/ansible/ansible/pull/85971](https\://github\.com/ansible/ansible/pull/85971)\)\.
* pip \- Prevent passing <code>\-e</code> to <code>pip</code> when the <code>editable</code> and <code>requirements</code> parameters are both used\.
* pip \- When installing multiple packages with <code>editable\=True</code>\, ensure each package is editable \([https\://github\.com/ansible/ansible/issues/77755](https\://github\.com/ansible/ansible/issues/77755)\)\.
* pluginloader \- Fixed non\-collection load path for builtin non\-Jinja plugins to consult deprecation metadata\.
* psrp \- ReadTimeout exceptions now mark host as unreachable instead of fatal \([https\://github\.com/ansible/ansible/issues/85966](https\://github\.com/ansible/ansible/issues/85966)\)
* rpm\_key \- Use librpm library API instead of gpg utility to support version 6 PGP keys \([https\://github\.com/ansible/ansible/issues/86157](https\://github\.com/ansible/ansible/issues/86157)\)\.
* ssh connection plugin \- fix resource leaks when using sshpass
* task conditionals \- An error in any task conditional \(e\.g\.\, <code>when</code>\, <code>until</code>\, <code>failed\_when</code>\) always causes the task to report a descriptive failure while preserving the task result\. The resulting task failure is always recoverable via <code>ignore\_errors</code>\. Previous inconsistent error handling in task conditionals could result in warnings\, loss of completed task results\, recoverable task errors\, unrecoverable task errors\, or failure of the Ansible controller process\.
* template module \- Report the line number for Jinja syntax errors in template files\.
* templating \- Fix traceback when using <code>deepcopy</code> on an imported template \([https\://github\.com/ansible/ansible/issues/86723](https\://github\.com/ansible/ansible/issues/86723)\)\.
* to\_yaml / to\_nice\_yaml filters \- Restore pre\-2\.19 decryption behavior for vaulted values \([https\://github\.com/ansible/ansible/issues/85722](https\://github\.com/ansible/ansible/issues/85722)\)\. A regression in 2\.19\.0 previously caused vaulted values to be dumped as <code>\!vault</code>\-tagged ciphertext\.
* unarchive \- make timezone aware timestamp for comparison \([https\://github\.com/ansible/ansible/issues/85779](https\://github\.com/ansible/ansible/issues/85779)\)\.
* user \- <code>user</code> module integration tests can now run multiple times on the same freebsd host \([https\://github\.com/ansible/ansible/issues/86541](https\://github\.com/ansible/ansible/issues/86541)\)\.
* user \- create accounts in an unlocked state by default on BusyBox \([https\://github\.com/ansible/ansible/issues/68676](https\://github\.com/ansible/ansible/issues/68676)\)
* user \- emit a warning when the <code>seuser</code> parameter is set on a system where SELinux is not enabled\, instead of silently ignoring it \([https\://github\.com/ansible/ansible/issues/85542](https\://github\.com/ansible/ansible/issues/85542)\)\.
* user \- fix <code>FreeBsdUser</code> to not create <code>/nonexistent</code> directory when modifying user to add them to a group on FreeBSD \([https\://github\.com/ansible/ansible/issues/86368](https\://github\.com/ansible/ansible/issues/86368)\)
* user \- fix modifying users on BusyBox \([https\://github\.com/ansible/ansible/issues/66679](https\://github\.com/ansible/ansible/issues/66679)\)
* user \- make option group required\_by option append\.
* user \- preserve existing password when modifying accounts on BusyBox systems \([https\://github\.com/ansible/ansible/pull/86530](https\://github\.com/ansible/ansible/pull/86530)\)
* user \- raise an error if force\=true is used while deleting the group on BusyBox based distros \([https\://github\.com/ansible/ansible/issues/85565](https\://github\.com/ansible/ansible/issues/85565)\)\.
* user \- return the actual system groups the user belongs to instead of only the groups specified in the module input \([https\://github\.com/ansible/ansible/issues/80669](https\://github\.com/ansible/ansible/issues/80669)\)\.
* winrm \- Provide a better error message if a domain user is specified using a User Principal Name \(<code>UPN</code>\) but the <code>pykerberos</code> library is not installed so Kerberos is unavailable\.
* yaml loading \- Fix traceback when parsing YAML strings \(not files\) when using the pure Python implementation of PyYAML\.

<a id="amazon-aws-4"></a>
#### amazon\.aws

* aws\_ssm \- Fixed connection being re\-established on every loop iteration\. The plugin now properly establishes a single connection for a loop \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2869](https\://github\.com/ansible\-collections/amazon\.aws/pull/2869)\)\.
* connection/aws\_ssm \- fixed ReferenceError in aws\_ssm connection plugin destructor during interpreter shutdown \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2728](https\://github\.com/ansible\-collections/amazon\.aws/issues/2728)\)\.
* elb\_application\_lb \- fixed comparison of multi\-rule default actions to properly handle the <code>Order</code> field when determining if listener modifications are needed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2537](https\://github\.com/ansible\-collections/amazon\.aws/issues/2537)\)\.
* elb\_application\_lb \- fixed error where creating a new application load balancer with listener rules would fail with <code>Parameter validation failed\: Invalid type for parameter ListenerArn\, value\: None</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2400](https\://github\.com/ansible\-collections/amazon\.aws/issues/2400)\)\.
* lambda\_info \- fixed invalid return value documentation that used dot notation \(<code>function\.TheName</code>\) which cannot be used in Jinja2 templates \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* s3\_bucket \- fix error when configuring AES256 bucket encryption with <code>bucket\_key\_enabled</code> explicitly set to <code>false</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2734](https\://github\.com/ansible\-collections/amazon\.aws/issues/2734)\)\.
* s3\_object \- fixed error when using PUT with an empty <code>content</code> string \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2810](https\://github\.com/ansible\-collections/amazon\.aws/pull/2810)\)

<a id="ansible-netcommon-4"></a>
#### ansible\.netcommon

* Added support for private key passphrase in libssh connection plugin\, when using encrypted private keys specified by the C\(ansible\_private\_key\_file\) attribute\.
* Adds backward compatibility of handling src attributes\, functional consistency with ansible\-core \>\= 2\.19
* Adds deprecation warning for the jinja2 processing functionality for src attributes\, src attributes in collections would still support considering file path but they would not process template files directly once the functionality is deprecated\.
* Avoid legacy imports deprecated in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/720](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/720)\)\.
* Avoid merging module\_defaults for all ansible\.netcommon\.grpc\_\* modules\.
* It is suggested to use ansible\.builtin\.template module to process templates and use the processed template path in src attributes\.
* Set libssh logging level to DEBUG when Ansible verbosity is greater than 3\, to aid in troubleshooting connection issues\.

<a id="ansible-utils-1"></a>
#### ansible\.utils

* Add a cleanup step that removes empty \{\} and \[\] values from lists in keep\_keys\_from\_dict\_n\_list\(\)

<a id="ansible-windows-2"></a>
#### ansible\.windows

* Stop using the deprecated text module\_utils in Ansible that will be removed in Ansible <code>2\.24</code>\.
* Update various action plugin calls to avoid some deprecated or old methods\.
* win\_dhcp\_lease \- when creating a reservation\, the dns\_name will be used as reservation\_name in case that is not provided\; will be discarded otherwise as the parameter HostName is not supported by Add\-DhcpServerv4Reservation \([https\://github\.com/ansible\-collections/ansible\.windows/issues/813](https\://github\.com/ansible\-collections/ansible\.windows/issues/813)\)
* win\_file \- Fix idempotency issues when using <code>state\: touch</code> \([https\://github\.com/ansible\-collections/ansible\.windows/issues/798](https\://github\.com/ansible\-collections/ansible\.windows/issues/798)\)
* win\_get\_url \- Fix force\=no not doing HEAD request if checksum is not set
* win\_hotfix \- Fix a bug in Get\-HotfixMetadataFromKB fallback logic where it would fail to return metadata even if the hotfix was found\.
* win\_hotfix \- Fix idempotency issue where some multi\-package MSUs \(e\.g\. SSU \+ CU\) were incorrectly reported as installed by DISM even if the CU was missing\. Added a secondary check using Get\-Hotfix to verify installation\.
* win\_powershell \- Fix up async support for Ansible 2\.19 when running <code>win\_powershell</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/828](https\://github\.com/ansible\-collections/ansible\.windows/issues/828)
* win\_products\_facts \- return string for all the license related facts \([https\://github\.com/ansible\-collections/community\.windows/issues/661](https\://github\.com/ansible\-collections/community\.windows/issues/661)\)\.
* win\_reboot \- Use full path to <code>shutdown\.exe</code> to avoid relying on <code>PATH</code> lookups to find \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/826](https\://github\.com/ansible\-collections/ansible\.windows/issues/826)
* win\_reboot \- fix unhandled error when <code>\.exe</code> not present in <code>PATHEXT</code> environment variable
* win\_shell \- Ensure the default <code>executable</code> uses the absolute path to <code>powershell\.exe</code> rather than looking it up in the <code>PATH</code> environment\.

<a id="arista-eos"></a>
#### arista\.eos

* Fix eos\_vrf module to properly check existing interface configuration before making changes \([https\://github\.com/ansible\-collections/arista\.eos/issues/546](https\://github\.com/ansible\-collections/arista\.eos/issues/546)\)

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Fix allowed ranges of interface option in aci\_interface\_config module\.
* Fix descriptions of options in aci\_maintenance\_policy\.
* Fix querying description in aci\_l4l7\_service\_graph\_template\.

<a id="cisco-ios-1"></a>
#### cisco\.ios

* Fixed delete and purged state function for ios\_bfd\_templates
* cisco\.ios\.ios\_acls \- Added support for converting numeric protocol values to real protocol options when gathered from the device\.
* cisco\.ios\.ios\_acls \- Gathered state showing incomplete configuration\.
* cisco\.ios\.ios\_hsrp\_intefaces \- Considers version 1 as default if configuration does not specify version\.
* cisco\.ios\.ios\_hsrp\_intefaces \- Corrects idempotency issue when version is not specified in configuration\.
* cisco\.ios\.ios\_l2\_interfaces \- Moved mode parser to below the trunk parsers\.

<a id="cisco-iosxr-2"></a>
#### cisco\.iosxr

* iosxr\_bgp\_address\_family \- Fixed label generation command handling under <em class="title-reference">address\_family</em> configuration\.

<a id="cisco-meraki-2"></a>
#### cisco\.meraki

* Fix parameter naming in organizations\_inventory\_claim\.py to use camelCase for consistency with existing code\.
* Fixing problem of naming in organizations\_appliance\_vpn\_third\_party\_vpnpeers\_info\.
* Restructuring README\.md file\.
* administered\_licensing\_subscription\_subscriptions\_bind \- Fixed parameter naming from \'subscription\_id\' to \'subscriptionId\' for proper API compatibility
* meraki\.py plugin utils \- Added type checking in has\_diff\_elem2 function to prevent errors when comparing lists of non\-dictionary elements
* networks\_appliance\_content\_filtering \- Enhanced idempotency by extracting category IDs from blockedUrlCategories before comparison

<a id="cisco-mso-1"></a>
#### cisco\.mso

* Fix updates of multicast\_route\_map\_policy in mso\_schema\_template\_vrf\_rp\.
* Fix updates of multicast\_route\_map\_source\_filter and multicast\_route\_map\_destination\_filter in mso\_schema\_template\_bd\.

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* Fixed nxos\_facts module so it can handle VLAN interface facts without any issue even if addr is not defined
* Fixed nxos\_static\_routes module so to handle replaced and overridden state with vrf configuration\.
* cisco\.nxos\.nxos\_facts \- Fix AttributeError when interface has multiple IPv6 addrs and handle ROW\_addr as list\.
* cisco\.nxos\.nxos\_facts \- Fix handling of facts for httapi type connection\.
* cisco\.nxos\.nxos\_hsrp\_intefaces \- Considers version 1 as default if configuration does not specify version\.
* cisco\.nxos\.nxos\_hsrp\_intefaces \- Corrects idempotency issue when version is not specified in configuration\.
* cisco\.nxos\.nxos\_hsrp\_interfaces \- Fix parsers for preempt and priority
* cisco\.nxos\.nxos\_l2\_interfaces \- Fix cdp\_enable config parsing\.
* cisco\.nxos\.nxos\_l3\_interfaces \- Improved the code logic for handling redirects\.
* cisco\.nxos\.nxos\_snmp\_server \- fixed communities parsing issue
* cisco\.nxos\.nxos\_static\_routes \- Fix facts parser to filter inline VRF routes from global route collection preventing incorrect VRF route deletion\.

<a id="community-aws-4"></a>
#### community\.aws

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/community\.aws/pull/2338](https\://github\.com/ansible\-collections/community\.aws/pull/2338)\)\.
* ec2\_customer\_gateway \- Fix documentation for the return block \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.

<a id="community-crypto-3"></a>
#### community\.crypto

* crypto\_info\, openssl\_privatekey\, openssl\_privatekey\_pipe \- fix detection of EC support for cryptography 46\.0\.5\+ \([https\://github\.com/ansible\-collections/community\.crypto/pull/981](https\://github\.com/ansible\-collections/community\.crypto/pull/981)\)\.

<a id="community-dns-6"></a>
#### community\.dns

* Update Public Suffix List\.
* converter module utils \- add <code>stacklevel\=2</code> to Python warnings\. This affects third\-party users of the module utils outside this collection \([https\://github\.com/ansible\-collections/community\.dns/pull/310](https\://github\.com/ansible\-collections/community\.dns/pull/310)\)\.
* hetzner\_\* modules and hetzner\_dns\_records inventory plugin \- retry on network problems and certain HTTP codes \(502\, 503\, 504\) \([https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hetzner\_dns\_record\_set\, hosttech\_dns\_record\_set \- fix <code>on\_existing \!\= \'replace\'</code> mis\-triggering when <code>state\=absent</code> and the values to delete do not show up in the list of records \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* hetzner\_dns\_record\_sets \- when doing batch updates\, do not request status updates for too many actions at once \([https\://github\.com/ansible\-collections/community\.dns/issues/312](https\://github\.com/ansible\-collections/community\.dns/issues/312)\, [https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hosttech\_\* modules and hosttech\_dns\_records inventory plugin \- when using the JSON API\, retry on network problems and certain HTTP codes \(502\, 503\, 504\) \([https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hosttech\_record\_sets\, hetzner\_record\_sets \- ensure stable order also with Python \< 3\.6 \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* lookup\_rfc8427 lookup plugin \- remove unused code \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.
* remove\_public\_suffix filter plugin \- fix plugin name in error message \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.
* remove\_registrable\_domain filter plugin \- fix plugin name in error message \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.

<a id="community-docker-2"></a>
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
* docker\_image\_pull\, docker\_container \- fix pulled image change detection for Docker 29\.2\+ \([https\://github\.com/ansible\-collections/community\.docker/pull/1242](https\://github\.com/ansible\-collections/community\.docker/pull/1242)\)\.
* docker\_network \- fix idempotency for IPv6 addresses and networks with Docker 29\.0\.0 \([https\://github\.com/ansible\-collections/community\.docker/pull/1201](https\://github\.com/ansible\-collections/community\.docker/pull/1201)\)\.
* modules and plugins using the Docker SDK for Python \- do not automatically set <code>tls\_hostname</code> when <code>validate\_certs\=true</code> for Docker SDK for Python 7\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.docker/issues/1225](https\://github\.com/ansible\-collections/community\.docker/issues/1225)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1226](https\://github\.com/ansible\-collections/community\.docker/pull/1226)\)\.

<a id="community-general-5"></a>
#### community\.general

* \_filelock module utils \- add type hints\. Fix bug if <code>set\_lock\(\)</code> is called with <code>lock\_timeout\=None</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11222](https\://github\.com/ansible\-collections/community\.general/pull/11222)\)\.
* aix\_filesystem \- remove compatibility code for ancient Python versions \([https\://github\.com/ansible\-collections/community\.general/pull/11232](https\://github\.com/ansible\-collections/community\.general/pull/11232)\)\.
* ansible\_type plugin utils \- avoid potential concatenation of non\-strings when <code>alias</code> has non\-string values \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* ansible\_type test plugin \- fix parameter checking \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* apk \- fix <code>packages</code> return value for apk\-tools \>\= 3 \(Alpine 3\.23\) \([https\://github\.com/ansible\-collections/community\.general/issues/11264](https\://github\.com/ansible\-collections/community\.general/issues/11264)\)\.
* cloudflare\_dns \- also allow <code>flag\=128</code> for CAA records \([https\://github\.com/ansible\-collections/community\.general/issues/11355](https\://github\.com/ansible\-collections/community\.general/issues/11355)\, [https\://github\.com/ansible\-collections/community\.general/pull/11377](https\://github\.com/ansible\-collections/community\.general/pull/11377)\)\.
* cobbler\_system \- compare the version as a float which is the type returned by the Cobbler API \([https\://github\.com/ansible\-collections/community\.general/issues/11044](https\://github\.com/ansible\-collections/community\.general/issues/11044)\)\.
* counter\_enabled callback plugin \- fix plugin not observing <code>display\_ok\_hosts</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/3978](https\://github\.com/ansible\-collections/community\.general/issues/3978)\, [https\://github\.com/ansible\-collections/community\.general/pull/11656](https\://github\.com/ansible\-collections/community\.general/pull/11656)\)\.
* datetime module utils \- fix bug in <code>fromtimestamp\(\)</code> that caused the function to crash\. This function is not used in community\.general \([https\://github\.com/ansible\-collections/community\.general/pull/11206](https\://github\.com/ansible\-collections/community\.general/pull/11206)\)\.
* gem \- add compatibility with Ruby 4 rubygems \([https\://github\.com/ansible\-collections/community\.general/issues/11397](https\://github\.com/ansible\-collections/community\.general/issues/11397)\, [https\://github\.com/ansible\-collections/community\.general/pull/11442](https\://github\.com/ansible\-collections/community\.general/pull/11442)\)\.
* gitlab module utils \- add type hints\. Pass API version to python\-gitlab as string and not as integer \([https\://github\.com/ansible\-collections/community\.general/pull/11222](https\://github\.com/ansible\-collections/community\.general/pull/11222)\)\.
* homebrew\_service \- slightly refactor code \([https\://github\.com/ansible\-collections/community\.general/pull/11168](https\://github\.com/ansible\-collections/community\.general/pull/11168)\)\.
* incus connection plugin \- fix parsing of commands for Windows\, enforcing a <code>\\</code> after the drive letter and colon symbol \([https\://github\.com/ansible\-collections/community\.general/pull/11347](https\://github\.com/ansible\-collections/community\.general/pull/11347)\)\.
* ipa\_dnsrecord \- fix idempotency bug when using <code>dnsttl</code> due to wrong Python types \([https\://github\.com/ansible\-collections/community\.general/pull/11559](https\://github\.com/ansible\-collections/community\.general/pull/11559)\)\.
* ipinfoio\_facts \- fix handling of HTTP errors consulting the service \([https\://github\.com/ansible\-collections/community\.general/pull/11145](https\://github\.com/ansible\-collections/community\.general/pull/11145)\)\.
* iptables\_state \- refactor code to avoid writing unnecessary temporary files \([https\://github\.com/ansible\-collections/community\.general/pull/11258](https\://github\.com/ansible\-collections/community\.general/pull/11258)\)\.
* keycloak module utils \- fix <code>TypeError</code> crash when managing users whose username or email contains special characters such as <code>\+</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10305](https\://github\.com/ansible\-collections/community\.general/issues/10305)\, [https\://github\.com/ansible\-collections/community\.general/pull/11472](https\://github\.com/ansible\-collections/community\.general/pull/11472)\)\.
* keycloak module utils \- use proper URL encoding \(<code>urllib\.parse\.quote</code>\) for query parameters in authorization permission name searches\, replacing fragile manual space replacement \([https\://github\.com/ansible\-collections/community\.general/pull/11472](https\://github\.com/ansible\-collections/community\.general/pull/11472)\)\.
* keycloak\_authentication \- fix <code>TypeError</code> crash when a flow is defined without <code>authenticationExecutions</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11547](https\://github\.com/ansible\-collections/community\.general/issues/11547)\, [https\://github\.com/ansible\-collections/community\.general/pull/11548](https\://github\.com/ansible\-collections/community\.general/pull/11548)\)\.
* keycloak\_client \- fix idempotency bug caused by <code>null</code> client attribute value differences for non\-existing client attributes \([https\://github\.com/ansible\-collections/community\.general/issues/11443](https\://github\.com/ansible\-collections/community\.general/issues/11443)\, [https\://github\.com/ansible\-collections/community\.general/pull/11444](https\://github\.com/ansible\-collections/community\.general/pull/11444)\)\.
* keycloak\_client \- fix idempotency bug caused by <code>null</code> flow overrides value differences for non\-existing flow overrides \([https\://github\.com/ansible\-collections/community\.general/issues/11430](https\://github\.com/ansible\-collections/community\.general/issues/11430)\, [https\://github\.com/ansible\-collections/community\.general/pull/11455](https\://github\.com/ansible\-collections/community\.general/pull/11455)\)\.
* keycloak\_client \- remove IDs as change from diff result for protocol mappers \([https\://github\.com/ansible\-collections/community\.general/issues/11453](https\://github\.com/ansible\-collections/community\.general/issues/11453)\, [https\://github\.com/ansible\-collections/community\.general/pull/11454](https\://github\.com/ansible\-collections/community\.general/pull/11454)\)\.
* keycloak\_realm \- fixed crash in <code>sanitize\_cr\(\)</code> when <code>realmrep</code> was <code>None</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11260](https\://github\.com/ansible\-collections/community\.general/pull/11260)\)\.
* keycloak\_realm\_key \- fix <code>KeyError</code> crash when managing realm keys where Keycloak does not return <code>active</code>\, <code>enabled</code>\, or <code>algorithm</code> fields in the config response \([https\://github\.com/ansible\-collections/community\.general/issues/11459](https\://github\.com/ansible\-collections/community\.general/issues/11459)\, [https\://github\.com/ansible\-collections/community\.general/pull/11470](https\://github\.com/ansible\-collections/community\.general/pull/11470)\)\.
* keycloak\_user\_federation \- mapper config item can be an array \([https\://github\.com/ansible\-collections/community\.general/issues/11502](https\://github\.com/ansible\-collections/community\.general/issues/11502)\, [https\://github\.com/ansible\-collections/community\.general/pull/11515](https\://github\.com/ansible\-collections/community\.general/pull/11515)\)\.
* keycloak\_user\_rolemapping \- fix <code>TypeError</code> crash when adding a client role to a user who has no existing roles for that client \([https\://github\.com/ansible\-collections/community\.general/issues/10960](https\://github\.com/ansible\-collections/community\.general/issues/10960)\, [https\://github\.com/ansible\-collections/community\.general/pull/11471](https\://github\.com/ansible\-collections/community\.general/pull/11471)\)\.
* keycloak\_user\_rolemapping module \- fixed crash when assigning roles to users without an existing role \([https\://github\.com/ansible\-collections/community\.general/issues/10960](https\://github\.com/ansible\-collections/community\.general/issues/10960)\, [https\://github\.com/ansible\-collections/community\.general/pull/11256](https\://github\.com/ansible\-collections/community\.general/pull/11256)\)\.
* keys\_filter\.py plugin utils \- fixed requirements check so that other sequences than lists and strings are checked\, and corrected broken formatting during error reporting \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* listen\_ports\_facts \- fix handling of empty PID lists when <code>command\=ss</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11332](https\://github\.com/ansible\-collections/community\.general/pull/11332)\)\.
* logstash\_plugin \- fix argument order when using <code>version</code> parameter\. The plugin name must come after options like <code>\-\-version</code> for the <code>logstash\-plugin</code> CLI to work correctly \([https\://github\.com/ansible\-collections/community\.general/issues/10745](https\://github\.com/ansible\-collections/community\.general/issues/10745)\, [https\://github\.com/ansible\-collections/community\.general/pull/11440](https\://github\.com/ansible\-collections/community\.general/pull/11440)\)\.
* mas \- parse CLI output correctly when listing installed apps with mas 3\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.general/pull/11179](https\://github\.com/ansible\-collections/community\.general/pull/11179)\)\.
* maven\_artifact \- fix SNAPSHOT version resolution to pick the newest matching <code>\<snapshotVersion\></code> entry by <code>\<updated\></code> timestamp instead of the first\. Repositories like GitHub Packages keep all historical entries in <code>\<snapshotVersions\></code> \(oldest first\)\, causing the module to resolve to the oldest snapshot instead of the latest \([https\://github\.com/ansible\-collections/community\.general/issues/5117](https\://github\.com/ansible\-collections/community\.general/issues/5117)\, [https\://github\.com/ansible\-collections/community\.general/issues/11489](https\://github\.com/ansible\-collections/community\.general/issues/11489)\, [https\://github\.com/ansible\-collections/community\.general/pull/11501](https\://github\.com/ansible\-collections/community\.general/pull/11501)\)\.
* monit \- add delay of 0\.5 seconds after state change and check for status \([https\://github\.com/ansible\-collections/community\.general/pull/11255](https\://github\.com/ansible\-collections/community\.general/pull/11255)\)\.
* monit \- internal state was not reflecting when operation is \"pending\" in <code>monit</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11245](https\://github\.com/ansible\-collections/community\.general/pull/11245)\)\.
* nictagadm \- add a condition to the if statement so that <code>is\_valid\_mac\(\)</code> does not get called if <code>etherstub</code> is false \([https\://github\.com/ansible\-collections/community\.general/pull/11589](https\://github\.com/ansible\-collections/community\.general/pull/11589)\)\.
* nmcli \- add missing <code>ipv6\.routing\-rules</code> to <code>settings\_type\(\)</code> list type\, preventing <code>routing\_rules6</code> list from being corrupted \([https\://github\.com/ansible\-collections/community\.general/issues/11630](https\://github\.com/ansible\-collections/community\.general/issues/11630)\, [https\://github\.com/ansible\-collections/community\.general/pull/11635](https\://github\.com/ansible\-collections/community\.general/pull/11635)\)\.
* nsupdate \- fix <code>AttributeError</code> when using the module without TSIG authentication \([https\://github\.com/ansible\-collections/community\.general/issues/11460](https\://github\.com/ansible\-collections/community\.general/issues/11460)\, [https\://github\.com/ansible\-collections/community\.general/pull/11461](https\://github\.com/ansible\-collections/community\.general/pull/11461)\)\.
* open\_iscsi \- fix IPv6 portal address formatting\; iscsiadm requires bracket notation for IPv6 addresses but the module was producing an incorrect format \([https\://github\.com/ansible\-collections/community\.general/issues/4467](https\://github\.com/ansible\-collections/community\.general/issues/4467)\, [https\://github\.com/ansible\-collections/community\.general/pull/11657](https\://github\.com/ansible\-collections/community\.general/pull/11657)\)\.
* pam\_limits \- remove <code>\%</code> templating no longer used in f\-string \([https\://github\.com/ansible\-collections/community\.general/pull/11229](https\://github\.com/ansible\-collections/community\.general/pull/11229)\)\.
* pmem \- fix test for invalid data input \([https\://github\.com/ansible\-collections/community\.general/pull/11388](https\://github\.com/ansible\-collections/community\.general/pull/11388)\)\.
* python\_requirements\_info \- use <code>importlib\.metadata</code> if <code>pkg\_resources</code> from <code>setuptools</code> cannot be imported\. That module has been removed from setuptools 82\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11491](https\://github\.com/ansible\-collections/community\.general/issues/11491)\, [https\://github\.com/ansible\-collections/community\.general/pull/11492](https\://github\.com/ansible\-collections/community\.general/pull/11492)\)\.
* splunk callback plugin \- replace deprecated callback function \([https\://github\.com/ansible\-collections/community\.general/pull/11485](https\://github\.com/ansible\-collections/community\.general/pull/11485)\)\.
* xcc\_redfish\_command \- fix templating of dictionary keys as list \([https\://github\.com/ansible\-collections/community\.general/pull/11144](https\://github\.com/ansible\-collections/community\.general/pull/11144)\)\.
* xfconf \- representation of boolean properties was not consistent between Python and <code>xfconf\-query</code>\, leading to broken idempotency \([https\://github\.com/ansible\-collections/community\.general/pull/11645](https\://github\.com/ansible\-collections/community\.general/pull/11645)\)\.
* zfs \- mark change correctly when updating properties whose current value differs\, even if they already have a non\-default value \([https\://github\.com/ansible\-collections/community\.general/issues/11019](https\://github\.com/ansible\-collections/community\.general/issues/11019)\, [https\://github\.com/ansible\-collections/community\.general/pull/11172](https\://github\.com/ansible\-collections/community\.general/pull/11172)\)\.

<a id="community-hrobot"></a>
#### community\.hrobot

* Remove unnecessary Python 2 compatibilty code \([https\://github\.com/ansible\-collections/community\.hrobot/pull/187](https\://github\.com/ansible\-collections/community\.hrobot/pull/187)\)\.

<a id="community-libvirt-1"></a>
#### community\.libvirt

* libvirt\_qemu \- Vendor <code>\_parse\_clixml</code> locally to fix <code>ImportError</code> on ansible\-core devel \(2\.21\+\)\.
* virt\_install \- fixed cloud\_init configuration handling for meta\-data\, user\-data\, and network\-config\.
* virt\_install \- fixed the dict\-based options handling for events\, resource\, and sysinfo options\.

<a id="community-mysql-2"></a>
#### community\.mysql

* mysql\_user \- When creating a new user\, and specifying parsec as plugin it wil generate the wrong SQL query\. It should be added to the same plugin check as ed25519 so that it generates a query using USING PASSWORDS\(\%s\) instead of BY \%s \([https\://github\.com/ansible\-collections/community\.mysql/pull/779](https\://github\.com/ansible\-collections/community\.mysql/pull/779)\)\.

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_db \- Fix connection limit not being set when value is \"0\" \([https\://github\.com/ansible\-collections/community\.postgresql/issues/879](https\://github\.com/ansible\-collections/community\.postgresql/issues/879)\)\.
* postgresql\_db \- fixed <code>session\_role</code> parameter that was being ignored for raw connections \([https\://github\.com/ansible\-collections/community\.postgresql/pull/865](https\://github\.com/ansible\-collections/community\.postgresql/pull/865)\)
* postgresql\_db \- restoring from <code>\.sql</code> files would execute the file twice\. The module now avoids using both <code>\-\-file</code> and stdin redirection simultaneously \([https\://github\.com/ansible\-collections/community\.postgresql/issues/882](https\://github\.com/ansible\-collections/community\.postgresql/issues/882)\)\.

<a id="community-proxmox-3"></a>
#### community\.proxmox

* proxmox all \- add missing timeout parameter to proxmoxer object creation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/218](https\://github\.com/ansible\-collections/community\.proxmox/pull/218)\)\.
* proxmox\_cluster \- make cluster join idempotent \([https\://github\.com/ansible\-collections/community\.proxmox/pull/244](https\://github\.com/ansible\-collections/community\.proxmox/pull/244)\)\.
* proxmox\_cluster\_firewall \- error message for invalid log\_ratelimit\.rate parameter \([https\://github\.com/ansible\-collections/community\.proxmox/pull/340](https\://github\.com/ansible\-collections/community\.proxmox/pull/340)\)\.
* proxmox\_disk \- add support for efidisk and tpmstate disk bus types which previously caused module failure with \"Unsupported disk bus\" error \([https\://github\.com/ansible\-collections/community\.proxmox/pull/319](https\://github\.com/ansible\-collections/community\.proxmox/pull/319)\)\.
* proxmox\_disk \- make none iso disk idempotent \([https\://github\.com/ansible\-collections/community\.proxmox/pull/288](https\://github\.com/ansible\-collections/community\.proxmox/pull/288)\)\.
* proxmox\_firewall \- Enable ipsets on vm level and fix bugs regarding the cidr notation the proxmox api expects \([https\://github\.com/ansible\-collections/community\.proxmox/pull/248](https\://github\.com/ansible\-collections/community\.proxmox/pull/248)\)\.
* proxmox\_ipam\_info \- fix bug where selecting by vmid did not work \([https\://github\.com/ansible\-collections/community\.proxmox/pull/211](https\://github\.com/ansible\-collections/community\.proxmox/pull/211)\)\.
* proxmox\_pool \- support nested pool \([https\://github\.com/ansible\-collections/community\.proxmox/pull/316](https\://github\.com/ansible\-collections/community\.proxmox/pull/316)\)\.
* proxmox\_role \- when privs is omitted\, keep existing role privileges unchanged instead of treating it as no privileges \([https\://github\.com/ansible\-collections/community\.proxmox/pull/284](https\://github\.com/ansible\-collections/community\.proxmox/pull/284)\)\.
* proxmox\_snap \- fail the task when a given snapname does not exist instead of exiting \([https\://github\.com/ansible\-collections/community\.proxmox/pull/365](https\://github\.com/ansible\-collections/community\.proxmox/pull/365)\)\.
* proxmox\_storage \- backend <code>cephfs</code>\, <code>dir</code> and <code>zfspool</code> doesn\'t requires <code>content</code> parameter \([https\://github\.com/ansible\-collections/community\.proxmox/pull/315](https\://github\.com/ansible\-collections/community\.proxmox/pull/315)\)\.
* proxmox\_storage \- the parameter <code>client\_keyring</code> was ignored \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- the parameter <code>fs\_name</code> was ignored \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- the parameter <code>state</code> was optional and without default value \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_zone \- fix validation logic for VXLAN zones to accept either <code>fabric</code> or <code>peers</code> parameter\. Previously\, only <code>fabric</code> was accepted\, but Proxmox VE also supports creating VXLAN zones with a peer address list \([https\://github\.com/ansible\-collections/community\.proxmox/issues/216](https\://github\.com/ansible\-collections/community\.proxmox/issues/216)\)\.
* remove wrong api endpoints and error messages from proxmod\_node certificate management\([https\://github\.com/ansible\-collections/community\.proxmox/pull/232](https\://github\.com/ansible\-collections/community\.proxmox/pull/232)\)\.

<a id="community-routeros-6"></a>
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
* api\_modify\, api\_info \- in the <code>routing bgp connection</code> and <code>bgp templates</code> paths\, fix spelling of the <code>output\.remove\-private\-as</code> parameter \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp instance</code> path\, fix \'Cannot add new entry to this path\' error \([https\://github\.com/ansible\-collections/community\.routeros/issues/409](https\://github\.com/ansible\-collections/community\.routeros/issues/409)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/420](https\://github\.com/ansible\-collections/community\.routeros/pull/420)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, remove <code>address\-families</code> for RouterOS 7\.19\+ \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, remove <code>router\-id</code> for RouterOS 7\.20\+ \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, support <code>afi</code> \(RouterOS 7\.19\+\) \(RouterOS 7\.19 and before\) \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* vmware\_guest\_storage\_policy \- Fix storage policy search to return None if no policies are found\, instead of causing an exception\. fixes [https\://github\.com/ansible\-collections/community\.vmware/issues/2527](https\://github\.com/ansible\-collections/community\.vmware/issues/2527)

<a id="community-windows-1"></a>
#### community\.windows

* Unify the TLS protocol handling logic for the modules that need it to ensure they use the configured OS policies\.
* win\_disk\_facts \- fixed an issue when a disk may not have a number \([https\://github\.com/ansible\-collections/community\.windows/pull/652](https\://github\.com/ansible\-collections/community\.windows/pull/652)\)\.
* win\_initialize\_disk \- disks that are formatted but offline cannot be brought online without erasing them \([https\://github\.com/ansible\-collections/community\.windows/issues/149](https\://github\.com/ansible\-collections/community\.windows/issues/149)\)\.
* win\_psmodule \- Improve error message\, if a module exists in multiple repositories \- [https\://github\.com/ansible\-collections/community\.windows/issues/641](https\://github\.com/ansible\-collections/community\.windows/issues/641)
* win\_psrepository\_copy \- Fix idempotence check to not rely on \.NET runtime implementation details\. This should avoid any false positive changed indicators

<a id="containers-podman-4"></a>
#### containers\.podman

* Fix Ansible warning about test utils
* Fix idempotency for tagging local images
* Fix image idempotency in pull
* Fix issue with \-\-rm and service in Quadlet
* fix\(podman\_prune\) set top\-level changed status

<a id="dellemc-enterprise-sonic-2"></a>
#### dellemc\.enterprise\_sonic

* ansible\-core\_219\_compatibility \- Modify the required Netcommon version and UT module param setting method for ansible\-core 2\.19 compatibility \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/600](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/600)\)\.
* sonic\_bgp\_af \- Fix check mode behavior \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/613](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/613)\)\.
* sonic\_lag\_interfaces \- Fix graceful\_shutdown not disabled for existing lag interfaces \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/617](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/617)\)\.
* sonic\_qos\_buffer \- Fix check mode and refactor module code \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602)\)\.
* sonic\_qos\_interfaces \- Fix check mode and refactor module code \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/603](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/603)\)\.
* sonic\_qos\_maps \- Fix check mode and refactor module code \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602)\)\.
* sonic\_qos\_scheduler \- Fix check mode and refactor module code \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602)\)\.
* sonic\_qos\_wred \- Fix check mode and refactor module code \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602)\)\.
* sonic\_roce \- Fix check mode and refactor module code \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/602)\)\.
* sonic\_vxlans \- Fix VXLAN config/facts handling\; moving deprecated uri EVPN\_NVO to current one VXLAN\_EVPN\_NVO \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/598](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/598)\)\.
* sonic\_vxlans \- Fix check mode handling \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/611](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/611)\)\.

<a id="dellemc-openmanage-1"></a>
#### dellemc\.openmanage

* idrac\_job\_queue \- \(Issue 1067\) \- Fails to find the file in role due to incorrect name \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1067](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1067)\)
* idrac\_system\_info \- \(Issue 1044\) \- FC section is missing \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1044](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1044)\)
* idrac\_system\_info \- powersupply\.get\_red\_type\_set fails with TypeError due to unhandled None values when joining mapped redundancy types
* idrac\_user \- \(Issue 1059\) \- Bad User Privileges when creating idrac user using \"custom\_privilege\" \([https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1059](https\://github\.com/dell/dellemc\-openmanage\-ansible\-modules/issues/1059)\)

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* Improved the request sending logic in httpapi plugin\.

<a id="fortinet-fortios-3"></a>
#### fortinet\.fortios

* Fixed an issue where users were required to specify a password confirmation when using the system\_admin and system\_api\_user modules in FortiOS 7\.6\.5 and later\.
* Fixed the issue that getting an error \"BadGzipFile\" when using token for authentication in new versions of FortiOS\.

<a id="google-cloud-1"></a>
#### google\.cloud

* Fix runtime\.yml to correctly note Ansible 2\.17 minimum version \([https\://github\.com/ansible\-collections/google\.cloud/pull/730](https\://github\.com/ansible\-collections/google\.cloud/pull/730)\)
* Revert removal of Ansible 2\.16 support \([https\://github\.com/ansible\-collections/google\.cloud/pull/734](https\://github\.com/ansible\-collections/google\.cloud/pull/734)\)
* connection plugin \- fix attribute error when using reset\_connection \([https\://github\.com/ansible\-collections/google\.cloud/issues/737](https\://github\.com/ansible\-collections/google\.cloud/issues/737)\)\.
* connection plugin \- fix ssh error in tasks with loops \([https\://github\.com/ansible\-collections/google\.cloud/issues/738](https\://github\.com/ansible\-collections/google\.cloud/issues/738)\)\.
* gcp\_secret\_manager \- return the secret value as type <em class="title-reference">str</em> rather than <em class="title-reference">bytes</em> \([https\://github\.com/ansible\-collections/google\.cloud/pull/721](https\://github\.com/ansible\-collections/google\.cloud/pull/721)\)

<a id="hetzner-hcloud-4"></a>
#### hetzner\.hcloud

* Invalid redirects for Storage Box modules are now fixed by using fully qualified module names\.
* firewall \- Ensure idempotency when using non canonical ipv6 representation in Firewall rules\.
* zone\_rrset \- Records order is not guaranteed\, the module will not generate a diff if the order of records changes\.
* zone\_rrset \- Records without comments will not generate a diff anymore\.

<a id="hitachivantara-vspone-block-7"></a>
#### hitachivantara\.vspone\_block

* Resolved issue during GAD pair creation when resource lock is enabled\.
* Resolved issue with quorum disk creation on VSP One Block 85 storage systems\.
* Resolved issue with remote connection creation on VSP One Block 85 storage systems\.
* Resolved issue with storage system facts retrieval module for VSP One Block 85 storage systems\.
* Resolved resource group creation with VSP 5XXX series storage systems\.
* Various additional bug fixes and enhancements for VSP One Block 85 storage systems\.
* Various additional bug fixes and enhancements for VSP One storage systems and VSP One SDS Block storage systems\.
* Various playbook fixes and improvements\.

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_svc\_manage\_ip \- Fixed issue related to VLAN while updating

<a id="infoblox-nios-modules-1"></a>
#### infoblox\.nios\_modules

* Fixed sanity and unit test execution in CI pipeline
* Fixed transform functions to handle <code>None</code> parameters and apply default values correctly

<a id="inspur-ispim"></a>
#### inspur\.ispim

* Edit ansible devel version tests to our CI test scripts  \([https\://github\.com/ispim/inspur\.ispim/pull/39](https\://github\.com/ispim/inspur\.ispim/pull/39)\)\.
* Modify the automated tests and add support for version 2\.18\. \([https\://github\.com/ispim/inspur\.ispim/pull/40](https\://github\.com/ispim/inspur\.ispim/pull/40)\)\.
* Modify the automated tests and add support for version 2\.18\. \([https\://github\.com/ispim/inspur\.ispim/pull/45](https\://github\.com/ispim/inspur\.ispim/pull/45)\)\.
* Modify the ism\.py file in the module\_utils directory\, and change the reference path of iteritems to be a reference from within Python\. \([https\://github\.com/ispim/inspur\.ispim/pull/46](https\://github\.com/ispim/inspur\.ispim/pull/46)\)\.

<a id="kaytus-ksmanage-2"></a>
#### kaytus\.ksmanage

* Modify the automated tests and add support for version 2\.18\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/31](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/31)\)\.
* Modify the failure details returned in module\_utils \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/29](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/29)\)\.
* Modify the ksmanage\.py file in the module\_utils directory\, and change the reference path of iteritems to be a reference from within Python\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/32](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/32)\)\.

<a id="kubernetes-core-5"></a>
#### kubernetes\.core

* Add idempotency for <code>helm\_pull</code> module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1055](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1055)\)\.
* Fixed a bug where setting <code>K8S\_AUTH\_VERIFY\_SSL\=true</code> \(or any string value\) caused the value to be treated as a separate <code>kubectl</code> command argument\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1049](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1049)\)\.
* Limit supported versions of Helm to \<4\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1039](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1039)\)\.
* Replace passing <code>warnings</code> to <code>exit\_json</code> with <code>AnsibleModule\.warn</code> in the <code>k8s\_drain</code>\, <code>k8s\_rollback\.py</code> and <code>k8s\_scale\.py</code> modules as it deprecated in <code>ansible\-core\>\=2\.19\.0</code> and will be removed in <code>ansible\-core\>\=2\.23\.0</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1033](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1033)\)\.
* k8s \- Fix return block from the module documentation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* meta \- Add <code>k8s\_cluster\_info</code>\, <code>k8s\_json\_patch</code> and <code>k8s\_rollback</code> to k8s action group \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/992](https\://github\.com/ansible\-collections/kubernetes\.core/pull/992)\)\.

<a id="microsoft-ad-1"></a>
#### microsoft\.ad

* microsoft\.ad\.domain\_child \- Fix return document key so it displays when using the standard Ansible documentation tools\.
* microsoft\.ad\.ldap \- Fix issue where auth\_protocol config option was never used when creating the spnego client\.
* microsoft\.ad\.service\_account \- Fix return document key so it displays when using the standard Ansible documentation tools\.

<a id="microsoft-iis-1"></a>
#### microsoft\.iis

* website\_info \- Fix error when retrieving website information but none exist \- [https\://github\.com/ansible\-collections/microsoft\.iis/issues/44](https\://github\.com/ansible\-collections/microsoft\.iis/issues/44)

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* na\_ontap\_aggregate \- fixed issue with disabling software encryption in REST\.
* na\_ontap\_cg\_snapshot \- fixed issue with ZAPI by removing default value for <em class="title-reference">consistency\_type</em>\.
* na\_ontap\_cifs\_local\_group \- fixed issue with idempotency\.
* na\_ontap\_export\_policy\_rule \- Fixed issue where rule\_index was not being applied to create body\, and added logic to detect when a create action is actually a re\-index of an existing rule\.
* na\_ontap\_firmware\_upgrade \- Updated documentation for <em class="title-reference">node</em> parameter and added examples\.
* na\_ontap\_job\_schedule \- Fix documentation formatting issue\.
* na\_ontap\_lun \- Updated module with alias <em class="title-reference">volume\_name</em> for <em class="title-reference">flexvol\_name</em>\.
* na\_ontap\_net\_vlan \- Fixed state detection when VLAN exists but is not in broadcast domain\.
* na\_ontap\_qtree \- Updated documentation for \'unix\_permissions\' parameter to clarify its usage\.
* na\_ontap\_qtree \- Updated module with alias <em class="title-reference">volume\_name</em> for <em class="title-reference">flexvol\_name</em>\.
* na\_ontap\_service\_processor\_network \- fixed issue with interface state not being applied correctly\, resolved ipv6 comparison issue and idempotency issue with ZAPI abd REST\.
* na\_ontap\_snapmirror\_policy \- updated examples for creating and modifying snapmirror policy\.
* na\_ontap\_user\_role \- Removed special handling of <em class="title-reference">DEFAULT</em> path and normalized empty query in privileges to None for consistency\.
* na\_ontap\_volume \- Fixed issue with volume rename\.
* na\_ontap\_vserver\_audit \- updated documentation for <em class="title-reference">log</em>\.

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

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_certs \- Fix the syntax to generate a CSR
* purefa\_connect \- Fixed issue where incorrect transport type was passed\.
* purefa\_default\_protection \- Fixed issue adding new default protection group to the array scope
* purefa\_dsrole\_old \- Fixed incorrect parameter name for old version of functions
* purefa\_host \- Fixed AttributeError when deleting WWNs from a host
* purefa\_info \- Added version check to ensure tags are only used in appropriate Purity versions
* purefa\_info \- Fixed AttributeError when directory service role has no name
* purefa\_info \- Fixed AttributeError when subnet has no VLAN
* purefa\_info \- Fixed error with Resalms\-based API clients
* purefa\_info \- Fixed issue with shelf controllers not supporting uptime
* purefa\_info \- Resolved AttributeErrors in <code>default</code> info section
* purefa\_info \- Resolves issue with hosthgroup info when NVMe connected volumes are in a hostgroup
* purefa\_network \- Fixes issue caused by None meaning change in SDK
* purefa\_pgsched \- Fixed schedule deletion idempotency
* purefa\_policy \- Fixed AttributeError when modifying a password policy
* purefa\_policy \- Multiple syntax errors fixed in the password policy update section

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_ad \- Ensure encryption algorithms used match the GUI values
* purefb\_alert \- Fixed issue with syntax error in update function
* purefb\_bucket\_replica \- Fixed IndexError crash in check loop
* purefb\_bucket\_replica \- Fixed issue with ItemIterator error
* purefb\_certs \- Fix the syntax to generate a CSR
* purefb\_ds \- Fixed issue when creating pre\-enabled management directory service
* purefb\_pingtrace \- Fiexed issue with XFM module when state is ping

<a id="splunk-es-7"></a>
#### splunk\.es

* Added sanity test ignore file for Ansible 2\.20 to handle pylint errors in deprecated modules\.
* Fixed ansible\-lint errors by adding missing task names in integration tests\.
* Fixed deprecated module alternatives to use fully qualified collection names \(FQCN\)\.
* Implement check mode support in action plugins\. Previously\, check mode was declared as supported but API calls were still being made\. Now all state\-changing operations \(merged\, replaced\, deleted\) properly skip API calls when running in check mode\.
* splunk\_correlation\_searches \- Fixed duplicate entries in gathered state caused by redundant loop in action plugin\.

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* Fix diff in check mode by normalising the boolean values \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/295](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/295)\)
* Fix doc generation and remove need for iteritems \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/296](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/296)\)
* Fix\: remove default for states parameter in icinga\_dependency\_apply \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/290](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/290)\)

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* content\_view\_filter\_rule \- fix content\_filter\_rule\_deb\_spec to take into account desired versions

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* Fix issue where modules that used the proxy\_host and proxy\_port arguments were ignoring these arguments when initializing clients\. \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/259](https\://github\.com/ansible\-collections/vmware\.vmware/issues/259)\)
* Updated common VM deployment module docs to mention that name or MOID can be used for the resource pool\, cluster\, datastore\, and datastore cluster parameters\. This allows users to work around issues where the name is not unique\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/239](https\://github\.com/ansible\-collections/vmware\.vmware/issues/239)
* cluster\_info \- When a user does not specify a cluster name\, the module will now search recursively for clusters in the datacenter\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/303](https\://github\.com/ansible\-collections/vmware\.vmware/issues/303)
* cluster\_info \- When a user specifies a datacenter name\, the module will now fail if that datacenter is not found instead of silently continuing\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/303](https\://github\.com/ansible\-collections/vmware\.vmware/issues/303)
* deploy\_content\_library\_ovf \- Remove invalid storage provisioning option \'eagerzeroedthick\' from module\'s argument spec\. \(Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/278](https\://github\.com/ansible\-collections/vmware\.vmware/issues/278)\)
* deploy\_folder\_template \- Fixed issue where the vm folder was being cached in the placement service\, causing the module to skip the template folder lookup and fail\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/292](https\://github\.com/ansible\-collections/vmware\.vmware/issues/292)
* import\_content\_library\_ovf \- Fixed issue where OVFs with \.nvram files failed to import Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/257](https\://github\.com/ansible\-collections/vmware\.vmware/issues/257)
* inventory plugins \- fix handling of encrypted strings in inventory plugin username and password options for ansible\-core\<\=2\.19 fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/304](https\://github\.com/ansible\-collections/vmware\.vmware/issues/304)
* vm \- Fixed issue where error handling failed when state is absent
* vm \- Remove check that prevents memory from being decreased regardless of power state\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/298](https\://github\.com/ansible\-collections/vmware\.vmware/issues/298)
* vm\_apply\_customization \- Fixed issue where the product ID\, user name\, and user org name were required by the API but not by the module

<a id="vultr-cloud-1"></a>
#### vultr\.cloud

* dns\_domain \- Removed requirement for the <code>ip</code> argument when creating a new domain \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/140](https\://github\.com/vultr/ansible\-collection\-vultr/issues/140)\)\.
* instance\, bare\_metal \- Fixed an issue where the <code>user\_data</code> response returned a JSON serialization error \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/156](https\://github\.com/vultr/ansible\-collection\-vultr/issues/156)\)\.
* startup\_script \- Fixed an issue where the <code>script</code> response returned a JSON serialization error \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/162](https\://github\.com/vultr/ansible\-collection\-vultr/pull/162)\)\.

<a id="known-issues"></a>
### Known Issues

<a id="community-docker-3"></a>
#### community\.docker

* docker\_image\, docker\_image\_export \- idempotency for archiving images depends on whether the image IDs used by the image storage backend correspond to the IDs used in the tarball\'s <code>manifest\.json</code> files\. The new default backend in Docker 29 apparently uses image IDs that no longer correspond\, whence idempotency no longer works \([https\://github\.com/ansible\-collections/community\.docker/pull/1199](https\://github\.com/ansible\-collections/community\.docker/pull/1199)\)\.

<a id="community-routeros-7"></a>
#### community\.routeros

* api\_modify \- to create or modify entries in the <code>container</code> path\, you need librouteros 4\.0\.0 or newer due to a bug preventing older versions from setting or modifying properties named <code>cmd</code> \([https\://github\.com/ansible\-collections/community\.routeros/issues/442](https\://github\.com/ansible\-collections/community\.routeros/issues/442)\)\.

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

<a id="new-plugins-1"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.loganalytics\_ingestion \- Posts task results to an Azure Log Analytics workspace using the new Logs Ingestion API\.

<a id="filter-1"></a>
#### Filter

* community\.general\.to\_toml \- Convert variable to TOML string\.

<a id="new-modules-2"></a>
### New Modules

<a id="amazon-aws-5"></a>
#### amazon\.aws

* amazon\.aws\.ec2\_instance\_type\_info \- Retrieve information about EC2 instance types

<a id="ansible-windows-3"></a>
#### ansible\.windows

* ansible\.windows\.dsc3 \- Sets or checks DSC v3 configuration state

<a id="cisco-aci-2"></a>
#### cisco\.aci

* cisco\.aci\.aci\_fabric\_node\_decommission \- Manage the Commissioning and Decommissioning of the Fabric Node \(fabric\:RsDecommissionNode\)
* cisco\.aci\.aci\_management\_network\_instance\_profile \- Manage external management network instance profiles \(mgmt\:InstP\)\.
* cisco\.aci\.aci\_management\_network\_instance\_profile\_to\_contract \- Bind Consumed Contract to External Management Network Instance Profiles \(mgmt\:RsOoBCons\)
* cisco\.aci\.aci\_switch\_access\_config \- Manage Switch Access Policy Configuration of Leaf and Spine nodes \(infra\:NodeConfig\)\.
* cisco\.aci\.aci\_switch\_fabric\_config \- Manage Switch Fabric Policy Configuration of Leaf and Spine nodes \(fabric\:NodeConfig\)\.

<a id="cisco-ios-2"></a>
#### cisco\.ios

* cisco\.ios\.ios\_bfd\_interfaces \- Resource module to configure bfd in interfaces\.
* cisco\.ios\.ios\_bfd\_templates \- Bidirectional Forwarding Detection \(BFD\) templates configurations

<a id="cisco-mso-2"></a>
#### cisco\.mso

* cisco\.mso\.ndo\_endpoint\_ip\_tag\_policy \- Manage Endpoint IP Tag Policies on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_endpoint\_mac\_tag\_policy \- Manage Endpoint MAC Tag Policies on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
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
* cisco\.mso\.ndo\_template\_deploy \- Deploy templates to sites on Cisco Nexus Dashboard Orchestrator \(NDO\)\.
* cisco\.mso\.ndo\_tenant\_netflow\_record \- Manage NetFlow Record on Cisco Nexus Dashboard Orchestrator \(NDO\)\.

<a id="community-general-6"></a>
#### community\.general

* community\.general\.file\_remove \- Remove files matching a pattern from a directory\.
* community\.general\.github\_secrets \- Manage GitHub repository or organization secrets\.
* community\.general\.github\_secrets\_info \- List GitHub repository or organization secrets\.
* community\.general\.icinga2\_downtime \- Manages Icinga 2 downtimes\.
* community\.general\.ip2location\_info \- Retrieve IP geolocation information of a host\'s IP address\.
* community\.general\.keycloak\_authentication\_v2 \- Configure authentication flows in Keycloak in an idempotent and safe manner\.
* community\.general\.keycloak\_realm\_localization \- Allows management of Keycloak realm localization overrides via the Keycloak API\.
* community\.general\.logrotate \- Manage logrotate configurations\.
* community\.general\.lxd\_storage\_pool\_info \- Retrieve information about LXD storage pools\.
* community\.general\.lxd\_storage\_volume\_info \- Retrieve information about LXD storage volumes\.
* community\.general\.sssd\_info \- Check SSSD domain status using D\-Bus\.

<a id="community-libvirt-2"></a>
#### community\.libvirt

* community\.libvirt\.virt\_cloud\_instance \- Provision new virtual machines from cloud images via libvirt

<a id="community-proxmox-4"></a>
#### community\.proxmox

* community\.proxmox\.proxmox\_ceph\_mds \- Add or delete Ceph Mds\.
* community\.proxmox\.proxmox\_ceph\_mgr \- Add or delete Ceph Manager\.
* community\.proxmox\.proxmox\_ceph\_mon \- Add or delete Ceph Monitor\.
* community\.proxmox\.proxmox\_cluster\_firewall \- Cluster\-level firewall options management for Proxmox VE cluster\.
* community\.proxmox\.proxmox\_cluster\_ha\_rules\_info \- Retrieve Proxmox VE HA rules\.
* community\.proxmox\.proxmox\_domain \- Manage authentication realms\.
* community\.proxmox\.proxmox\_domain\_sync \- Sync realms\.
* community\.proxmox\.proxmox\_role \- Role management for Proxmox VE cluster\.
* community\.proxmox\.proxmox\_sendkey \- Send key presses to a Proxmox VM console\.

<a id="containers-podman-5"></a>
#### containers\.podman

* containers\.podman\.podman\_quadlet \- Install or remove Podman Quadlets
* containers\.podman\.podman\_quadlet\_info \- Gather information about Podman Quadlets

<a id="dellemc-enterprise-sonic-3"></a>
#### dellemc\.enterprise\_sonic

* dellemc\.enterprise\_sonic\.sonic\_fbs\_interfaces \- Manage flow based services \(FBS\) interfaces configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_mfa \- Manage Multi\-factor authentication \(MFA\) configurations on SONiC\.

<a id="fortinet-fortimanager-2"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_devprof\_log\_syslogd\_setting\_logtemplates \- System template log syslogd setting log templates
* fortinet\.fortimanager\.fmgr\_devprof\_system\_template\_interface \- System template system template interface
* fortinet\.fortimanager\.fmgr\_devprof\_system\_template\_interface\_iprange \- System template system template interface ip range
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
* fortinet\.fortimanager\.fmgr\_fmg\_script \- Fmg script
* fortinet\.fortimanager\.fmgr\_fmg\_script\_schedule \- Fmg script schedule
* fortinet\.fortimanager\.fmgr\_icap\_remoteservergroup \- Icap remote server group
* fortinet\.fortimanager\.fmgr\_icap\_remoteservergroup\_serverlist \- Icap remote server group server list
* fortinet\.fortimanager\.fmgr\_isolator\_profile \- Isolator profile
* fortinet\.fortimanager\.fmgr\_isolator\_profile\_entries \- Isolator profile entries
* fortinet\.fortimanager\.fmgr\_pkg\_firewall\_responseshapingpolicy \- Policy package firewall response shaping policy
* fortinet\.fortimanager\.fmgr\_securityconsole\_template\_validate \- Securityconsole template validate
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
* fortinet\.fortimanager\.fmgr\_system\_locallog\_tacacsaccounting\_filter \- Cli system locallog tacacs\+accounting filter
* fortinet\.fortimanager\.fmgr\_system\_locallog\_tacacsaccounting\_setting \- Cli system locallog tacacs\+accounting setting
* fortinet\.fortimanager\.fmgr\_system\_log\_apiratelimit \- Cli system log api ratelimit
* fortinet\.fortimanager\.fmgr\_system\_log\_settings\_clientcertauth \- Cli system log settings client cert auth
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

<a id="hitachivantara-vspone-block-8"></a>
#### hitachivantara\.vspone\_block

<a id="sds-block"></a>
##### Sds Block

* hitachivantara\.vspone\_block\.hv\_sds\_block\_audit\_log\_setting \- Manages Hitachi SDS block storage system audit log settings\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_audit\_log\_setting\_facts \- Get audit log setting from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_dump\_log\_file \- Dumps log information from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_dump\_log\_status\_facts \- Dumps log status information from SDS Block storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_environment\_setting\_facts \- Retrieves encryption environment settings from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_environment\_settings \- Manages encryption environment settings on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_key \- Manage encryption keys on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_key\_count\_facts \- Get encryption key count information from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_encryption\_key\_facts \- Retrieves encryption key information from VSP One SDS Block and Cloud systems\.
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
* hitachivantara\.vspone\_block\.hv\_sds\_block\_remote\_path\_group \- Manages remote path groups on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_remote\_path\_group\_facts \- Get information about remote path groups from VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_session \- Manages sessions on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_session\_facts \- Retrieves information about sessions on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_external\_auth\_server\_setting \- Manages external authentication server settings on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_external\_auth\_server\_setting\_facts \- Get external authentication server settings from the storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_user\_auth\_setting \- Manages external authentication server settings on VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_storage\_user\_auth\_setting\_facts \- Get user authentication settings from the storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_user\_group \- Create and update user groups on the storage system\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_web\_server \- Manages the web server access setting for VSP One SDS Block and Cloud systems\.
* hitachivantara\.vspone\_block\.hv\_sds\_block\_web\_server\_facts \- Get the web server access setting from VSP One SDS Block and Cloud systems\.

<a id="vsp-1"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_pav\_alias \- Manages PAV \(Parallel Access Volume\) alias assignments for VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_pav\_alias\_facts \- retrieves information about PAV aliases from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_session \- Manages sessions on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_session\_facts \- Retrieves information about sessions on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_snapshot\_family\_facts \- Retrieves snapshot family information of the provided LDEV ID from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_supported\_host\_mode\_facts \- Retrieves supported host mode options information from a specified VSP block storage system\.
* hitachivantara\.vspone\_block\.hv\_vclone\_parent\_volume\_facts \- Retrieves virtual clone parent volume information from VSP block storage systems\.

<a id="ibm-storage-virtualize-2"></a>
#### ibm\.storage\_virtualize

* ibm\.storage\_virtualize\.ibm\_sv\_manage\_clone \- This module manages clone and thinclone of volume and volumegroup\.

<a id="kaytus-ksmanage-3"></a>
#### kaytus\.ksmanage

* kaytus\.ksmanage\.generate\_ssl \- Generate SSL certificate
* kaytus\.ksmanage\.ssl\_info \- Get SSL certificate information
* kaytus\.ksmanage\.upload\_ssl \- Upload SSL certificate

<a id="netapp-ontap-3"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_autoupdate\_config \- NetApp ONTAP module to manage configurations for automatic updates\.
* netapp\.ontap\.na\_ontap\_cg \- NetApp ONTAP module to manage operations related to consistency groups\.

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

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_contact\_assignment \- Manage contact assignments in NetBox
* netbox\.netbox\.netbox\_data\_source \- Manage data sources in NetBox

<a id="splunk-es-8"></a>
#### splunk\.es

* splunk\.es\.splunk\_finding \- Manage Splunk Enterprise Security findings
* splunk\.es\.splunk\_finding\_info \- Gather information about Splunk Enterprise Security Findings
* splunk\.es\.splunk\_investigation \- Manage Splunk Enterprise Security investigations
* splunk\.es\.splunk\_investigation\_info \- Gather information about Splunk Enterprise Security Investigations
* splunk\.es\.splunk\_investigation\_type \- Manage Splunk Enterprise Security investigation types
* splunk\.es\.splunk\_investigation\_type\_info \- Gather information about Splunk Enterprise Security investigation types
* splunk\.es\.splunk\_notes \- Manage notes for findings\, investigations\, and response plan tasks
* splunk\.es\.splunk\_notes\_info \- Gather information about notes in Splunk Enterprise Security
* splunk\.es\.splunk\_response\_plan \- Manage Splunk Enterprise Security response plans
* splunk\.es\.splunk\_response\_plan\_execution \- Apply response plans to investigations and manage tasks
* splunk\.es\.splunk\_response\_plan\_execution\_info \- Gather information about applied response plans on an investigation
* splunk\.es\.splunk\_response\_plan\_info \- Gather information about Splunk Enterprise Security response plans

<a id="theforeman-foreman-3"></a>
#### theforeman\.foreman

* theforeman\.foreman\.smart\_proxy\_refresh \- Refresh Smart Proxy features

<a id="vultr-cloud-2"></a>
#### vultr\.cloud

* vultr\.cloud\.load\_balancer \- Manages load balancers on Vultr
* vultr\.cloud\.load\_balancer\_info \- Get information about Vultr load balancers
* vultr\.cloud\.object\_storage\_cluster\_info \- Get information about the Vultr object storage clusters
* vultr\.cloud\.object\_storage\_info \- Get information about the Vultr object stores

<a id="unchanged-collections-3"></a>
### Unchanged Collections

* ansible\.posix \(still version 2\.1\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.okd \(still version 5\.0\.0\)
* community\.proxysql \(still version 1\.7\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.zabbix \(still version 4\.1\.1\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.39\.0\)
* grafana\.grafana \(still version 6\.0\.6\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* lowlydba\.sqlserver \(still version 2\.7\.0\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* vyos\.vyos \(still version 6\.0\.0\)
