# Ansible 14 Release Notes

This changelog describes changes since Ansible 13\.0\.0\.

- <a href="#v14-2-0">v14\.2\.0</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#ansible-core">Ansible\-core</a>
    - <a href="#changed-collections">Changed Collections</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#security-fixes">Security Fixes</a>
    - <a href="#bugfixes">Bugfixes</a>
    - <a href="#new-plugins">New Plugins</a>
    - <a href="#new-modules">New Modules</a>
    - <a href="#unchanged-collections">Unchanged Collections</a>
- <a href="#v14-1-0">v14\.1\.0</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#changed-collections-1">Changed Collections</a>
    - <a href="#major-changes-1">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#new-plugins-1">New Plugins</a>
    - <a href="#new-modules-1">New Modules</a>
    - <a href="#unchanged-collections-1">Unchanged Collections</a>
- <a href="#v14-0-0">v14\.0\.0</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#removed-collections">Removed Collections</a>
    - <a href="#added-collections">Added Collections</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#included-collections">Included Collections</a>
    - <a href="#major-changes-2">Major Changes</a>
    - <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#known-issues">Known Issues</a>
    - <a href="#new-plugins-2">New Plugins</a>
    - <a href="#new-modules-2">New Modules</a>
    - <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="v14-2-0"></a>
## v14\.2\.0

- <a href="#release-summary">Release Summary</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#changed-collections">Changed Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#splunk-es">splunk\.es</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#ansible-mysql">ansible\.mysql</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#community-clickhouse">community\.clickhouse</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-libvirt">community\.libvirt</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#graphiant-naas">graphiant\.naas</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#splunk-es-1">splunk\.es</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#community-clickhouse-1">community\.clickhouse</a>
    - <a href="#community-rabbitmq">community\.rabbitmq</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#ansible-posix">ansible\.posix</a>
    - <a href="#splunk-es-2">splunk\.es</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#ansible-mysql-1">ansible\.mysql</a>
    - <a href="#ansible-posix-1">ansible\.posix</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#community-clickhouse-2">community\.clickhouse</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-libvirt-1">community\.libvirt</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#microsoft-iis">microsoft\.iis</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
    - <a href="#splunk-es-3">splunk\.es</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#ansible-mysql-2">ansible\.mysql</a>
    - <a href="#community-clickhouse-3">community\.clickhouse</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2026\-07\-14

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 14\.2\.0 contains ansible\-core version 2\.21\.2\.
This is a newer version than version 2\.21\.1 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection             | Ansible 14.1.0 | Ansible 14.2.0 | Notes                                                                                                                        |
| ---------------------- | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| amazon.aws             | 11.3.0         | 11.4.0         |                                                                                                                              |
| ansible.mysql          | 5.0.1          | 5.1.0          |                                                                                                                              |
| ansible.netcommon      | 8.5.3          | 8.6.0          |                                                                                                                              |
| ansible.posix          | 2.2.0          | 2.2.2          |                                                                                                                              |
| ansible.windows        | 3.6.1          | 3.7.0          |                                                                                                                              |
| azure.azcollection     | 3.19.0         | 3.20.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.intersight       | 2.19.0         | 2.20.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator. |
| cisco.meraki           | 2.24.0         | 2.24.1         |                                                                                                                              |
| community.aws          | 11.0.0         | 11.1.0         |                                                                                                                              |
| community.clickhouse   | 2.2.0          | 2.3.0          |                                                                                                                              |
| community.crypto       | 3.2.2          | 3.3.0          |                                                                                                                              |
| community.dns          | 4.0.1          | 4.0.2          |                                                                                                                              |
| community.general      | 13.1.0         | 13.2.0         |                                                                                                                              |
| community.libvirt      | 2.2.0          | 2.3.0          |                                                                                                                              |
| community.mongodb      | 1.7.12         | 1.8.0          | There are no changes recorded in the changelog.                                                                              |
| community.rabbitmq     | 1.6.0          | 1.7.0          |                                                                                                                              |
| community.vmware       | 6.2.0          | 6.2.1          |                                                                                                                              |
| community.windows      | 3.2.0          | 3.3.0          |                                                                                                                              |
| dellemc.openmanage     | 10.0.2         | 10.0.3         | The collection did not have a changelog in this version.                                                                     |
| dellemc.powerflex      | 3.0.0          | 3.1.0          |                                                                                                                              |
| graphiant.naas         | 26.5.0         | 26.6.0         |                                                                                                                              |
| kubernetes.core        | 6.4.0          | 6.5.0          |                                                                                                                              |
| microsoft.ad           | 1.11.0         | 1.12.0         |                                                                                                                              |
| microsoft.iis          | 1.2.0          | 1.2.1          |                                                                                                                              |
| purestorage.flasharray | 1.42.0         | 1.43.0         |                                                                                                                              |
| purestorage.flashblade | 1.25.1         | 1.26.0         |                                                                                                                              |
| splunk.es              | 6.0.0          | 6.0.1          |                                                                                                                              |
| vultr.cloud            | 1.14.0         | 1.14.1         |                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="splunk-es"></a>
#### splunk\.es

* ci \- integration tests now run against both Splunk Server 9\.4 and 10\.4 with Enterprise Security \(ES\)\, providing full coverage across supported major versions and catching regressions against real Splunk ES instances\.

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-1"></a>
#### Ansible\-core

* ansible\-test \- Added a timeout callback that dumps thread stacks when the test execution deadline defined by <code>ansible\-test env \-\-timeout</code> is approaching\.
* parallel fact gathering \- the async wrapper now considers the timeout when determining whether to kill the process running the module\. Previously\, a 5 second sleep occurred twice before checking if the job had remaining time\.

<a id="amazon-aws"></a>
#### amazon\.aws

* aws\_ssm \- Added O\(endpoint\_url\) option for connecting to alternate AWS endpoints\. The alias O\(aws\_endpoint\_url\) is also supported \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Improved code organisation by extracting Windows command execution logic into a dedicated WindowsCommandExecutor class \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Refactored connection plugin to inherit from AWSConnectionBase for consistent AWS credential handling across plugins \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Renamed connection plugin options for consistency with other AWS plugins\. O\(aws\_access\_key\_id\) renamed to O\(access\_key\)\; O\(aws\_secret\_access\_key\) renamed to O\(secret\_key\)\; O\(aws\_session\_token\) renamed to O\(session\_token\)\; O\(aws\_profile\) renamed to O\(profile\)\. Old names are retained as aliases\. Additional aliases O\(access\_key\_id\) and O\(secret\_access\_key\) were also added \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* backup\_plan \- replace realistic version IDs with example UUID format in documentation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* backup\_plan\_info \- replace realistic version IDs with example UUID format in documentation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_eip \- replace AWS public IPs with RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_eni\_info \- use RFC 1918 private addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_instance \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_instance\_info \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_key\_info \- replace realistic SSH fingerprint with example value in documentation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_metadata\_facts \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_vpc\_dhcp\_option \- use public DNS servers \(8\.8\.4\.4\, 8\.8\.8\.8\) instead of RFC 5737 addresses for DNS examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_vpc\_nat\_gateway \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_vpc\_nat\_gateway\_info \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_vpc\_vpn \- replace realistic pre\-shared key with obvious example value in documentation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_vpc\_vpn \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* ec2\_vpc\_vpn\_info \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* rds\_instance \- Added support for self\-managed Active Directory parameters <code>domain\_fqdn</code>\, <code>domain\_ou</code>\, <code>domain\_auth\_secret\_arn</code>\, and <code>domain\_dns\_ips</code> to allow joining RDS instances to a self\-managed Active Directory domain \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2977](https\://github\.com/ansible\-collections/amazon\.aws/pull/2977)\)\.
* route53 \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* route53\_health\_check \- use RFC 5737 TEST\-NET addresses in documentation examples \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3008](https\://github\.com/ansible\-collections/amazon\.aws/pull/3008)\)\.
* route53\_zone \- add support for <code>wait</code> and <code>wait\_timeout</code> parameters to wait for DNSSEC state changes to propagate \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2981](https\://github\.com/ansible\-collections/amazon\.aws/issues/2981)\)\.

<a id="ansible-mysql"></a>
#### ansible\.mysql

* CI \- MySQL 8\.0\.38 has been removed from the CI test matrix because MySQL 8\.0 reached End of Life in April 2026\. The collection still supports MySQL 8\.0 at runtime through version\-conditional code paths\.
* CI \- PyMySQL 0\.9\.3 and 1\.0\.2 have been removed from the CI test matrix\. PyMySQL 0\.9\.3 is unmaintained and has an unfixed CVE\-2024\-36039\. PyMySQL 1\.0\.2 is redundant with 1\.1\.1 as both cover the same code path\. PyMySQL 0\.10\.1 has been promoted to the main test matrix\.

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* Remediate deprecated <code>ansible\.module\_utils\.common\.\_collections\_compat</code> module and replaced with <code>collections\.abc</code> from the Python standard library\.
* Remediate deprecated <code>ansible\.module\_utils\.six</code> module and replaced it with native Python 3 equivalents like <code>pickle</code>\, <code>zip</code>\, <code>urllib\.parse</code>\, <code>urllib\.error</code> etc\.
* Remediate deprecated <code>to\_text</code> and <code>to\_bytes</code> from <code>ansible\.module\_utils\.\_text</code> and replaced with <code>ansible\.module\_utils\.common\.text\.converters</code>\.
* Remediate deprecated <code>warnings</code> parameter in <code>exit\_json</code> calls by introducing <code>emit\_warnings</code> and <code>warn\_and\_exit</code> utility functions in <code>plugins/module\_utils/network/common/utils\.py</code> to centralize warning emission logic\. The following modules were updated to use <code>warn\_and\_exit</code> \- <code>cli\_backup</code>\, <code>cli\_command</code>\, <code>cli\_config</code>\, <code>cli\_restore</code>\, <code>grpc\_config</code>\, <code>grpc\_get</code>\, <code>netconf\_config</code>\, <code>netconf\_get</code>\, <code>netconf\_rpc</code>\, <code>restconf\_config</code>\, <code>restconf\_get</code>\. <code>ResourceModule</code> base class in <code>rm\_base/resource\_module\.py</code> was updated to use <code>emit\_warnings</code>\, which automatically addresses the deprecation for all downstream collections \(e\.g\. cisco\.iosxr\, cisco\.ios\, arista\.eos\)\.

<a id="ansible-windows"></a>
#### ansible\.windows

* reboot \- Replace deprecated <code>datetime\.datetime\.utcnow\(\)</code> with <code>datetime\.now\(timezone\.utc\)</code> for Python 3\.12\+ compatibility\.
* win\_acl \- Add check mode support so the module reports whether changes would be made without modifying ACL permissions \([https\://github\.com/ansible\-collections/ansible\.windows/issues/911](https\://github\.com/ansible\-collections/ansible\.windows/issues/911)\)\.
* win\_dns\_zone \- Added <code>directory\_partition</code> parameter to support storing AD\-integrated zones in custom application directory partitions for fine\-grained replication control \([https\://github\.com/ansible\-collections/ansible\.windows/issues/901](https\://github\.com/ansible\-collections/ansible\.windows/issues/901)\)\.

<a id="cisco-meraki"></a>
#### cisco\.meraki

* Fixed problem with networks\_wireless\_ssids module\.

<a id="community-aws"></a>
#### community\.aws

* ecs\_task \- Add <code>wait\_complete</code> parameter to wait for tasks to stop and return container exit codes after <code>run</code> or <code>start</code> operations \([https\://github\.com/ansible\-collections/community\.aws/pull/2409](https\://github\.com/ansible\-collections/community\.aws/pull/2409)\)\.
* msk\_cluster \- Fix tags on cluster creation \([https\://github\.com/ansible\-collections/community\.aws/pull/2324](https\://github\.com/ansible\-collections/community\.aws/pull/2324)\)\.
* route53\_wait \- make <code>skipped</code> and <code>invocation</code> keys optional in result validation to support modern Ansible loop structures \([https\://github\.com/ansible\-collections/community\.aws/pull/2447](https\://github\.com/ansible\-collections/community\.aws/pull/2447)\)\.

<a id="community-clickhouse"></a>
#### community\.clickhouse

* clickhouse\_db \- check if passed engine is supported before executing query\. Module checks if passed name exists in system\.database\_engines \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/214](https\://github\.com/ansible\-collections/community\.clickhouse/pull/214)\)\.
* clickhouse\_db \- validate passed identifiers\. Close them in backticks to keep it consistent with other modules \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/214](https\://github\.com/ansible\-collections/community\.clickhouse/pull/214)\)\.
* clickhouse\_grants \- pass cluster name in ON CLUSTER clause in backticks\.
* clickhouse\_quota \- inherit cluster documentation and spec option\.
* clickhouse\_quota \- pass quota and cluster name in backticks in queries\.
* clickhouse\_role \- close names in backticks\. Now names for roles and cluster will be validated\. Those containing \` or will be rejected\. Other will eb safe passed without risk of breaking query\.
* clickhouse\_user \- module on success returns query\_parameters with password used for query\.
* clickhouse\_user \- normalize generating query\. Now identifiers like user names will be closed in backticks\.
* clickhouse\_user \- pass password to ClickHouse using query parameters\. Prevent breaking query when containing soem special characters\.

<a id="community-crypto"></a>
#### community\.crypto

* Update vendored list of OID names from OpenSSL \([https\://github\.com/ansible\-collections/community\.crypto/pull/1057](https\://github\.com/ansible\-collections/community\.crypto/pull/1057)\)\.
* openssl\_privatekey\*\, openssl\_publickey\*\, openssl\_csr\*\, x509\_certificate\* \- support ML\-DSA\-\{44\,65\,87\} private keys \([https\://github\.com/ansible\-collections/community\.crypto/issues/1056](https\://github\.com/ansible\-collections/community\.crypto/issues/1056)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/1058](https\://github\.com/ansible\-collections/community\.crypto/pull/1058)\)\.

<a id="community-general"></a>
#### community\.general

* The collection now depends on community\.library\_inventory\_filtering\_v1\. This runtime dependency is used by inventory plugins only\, and will be automatically installed by <code>ansible\-galaxy collection install</code>\. If you install community\.general by cloning its repository or extracting its release tarball to a specific location\, you also need to make sure to install community\.library\_inventory\_filtering\_v1 manually if you use one of the affected inventory plugins \([https\://github\.com/ansible\-collections/community\.general/pull/12302](https\://github\.com/ansible\-collections/community\.general/pull/12302)\)\.
* bitwarden lookup plugin \- add <code>sync</code> option to sync items from the vault before lookup \([https\://github\.com/ansible\-collections/community\.general/pull/12377](https\://github\.com/ansible\-collections/community\.general/pull/12377)\)\.
* consul\_kv \- the module no longer requires the <code>py\-consul</code> Python library\, and is now part of the <code>community\.general\.consul</code> action group \([https\://github\.com/ansible\-collections/community\.general/pull/12221](https\://github\.com/ansible\-collections/community\.general/pull/12221)\)\.
* gitlab\_runners inventory plugin \- wrap the Gitlab API object in a context mananger\, and only create the <code>gitlab\_runners</code> group after the API request was successful \([https\://github\.com/ansible\-collections/community\.general/pull/12378](https\://github\.com/ansible\-collections/community\.general/pull/12378)\)\.
* nmap inventory plugin \- allow <code>address</code> to be a list of networks/IP ranges to scan\, in addition to a single string \([https\://github\.com/ansible\-collections/community\.general/issues/12379](https\://github\.com/ansible\-collections/community\.general/issues/12379)\, [https\://github\.com/ansible\-collections/community\.general/pull/12384](https\://github\.com/ansible\-collections/community\.general/pull/12384)\)\.
* opennebula inventory plugin \- add new option <code>filter</code> that allows to filter hosts by variables \([https\://github\.com/ansible\-collections/community\.general/pull/12302](https\://github\.com/ansible\-collections/community\.general/pull/12302)\)\.
* passwordstore lookup plugin \- make <code>directory</code> configurable through <code>ansible\.cfg</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12298](https\://github\.com/ansible\-collections/community\.general/pull/12298)\)\.
* tss lookup plugin \- cache the <code>TSSClient</code> per process and credential identity so OAuth2 token grants are reused across lookups \(rebuilding the client and retrying the lookup once on a stale\-token 4xx\, while 5xx and other errors propagate unchanged\)\, and add a <code>token\_path\_source</code> option whose <code>auto</code> value lets <code>python\-tss\-sdk</code> auto\-detect the Secret Server or Delinea Platform token endpoint \([https\://github\.com/ansible\-collections/community\.general/pull/12328](https\://github\.com/ansible\-collections/community\.general/pull/12328)\)\.

<a id="community-libvirt"></a>
#### community\.libvirt

* inventory \- added option <code>alternate\_id\_groups</code> \(default <code>true</code>\)\.
* inventory \- added option <code>filter</code> \(default <code>\.\*</code>\) to include domains by name or uuid which match regex\.
* virt \- Add <code>get\_ifaddresses</code> function to retrieve domain interface addresses\.
* virt\_cloud\_instance \- Add support for compressed base images \(gzip\, bzip2\, xz\)\.
* virt\_cloud\_instance \- add passt network support via shared network schema \([https\://github\.com/ansible\-collections/community\.libvirt/issues/231](https\://github\.com/ansible\-collections/community\.libvirt/issues/231)\)\.
* virt\_install \- add <code>wait\_timeout</code> parameter to wait for multi\-phase unattended installs to complete\.
* virt\_install \- add <code>wwn</code> parameter to disk specifications for setting the World Wide Name of a disk device \([https\://github\.com/ansible\-collections/community\.libvirt/issues/271](https\://github\.com/ansible\-collections/community\.libvirt/issues/271)\)\.
* virt\_install \- add passt network support with <code>value</code> shorthand and structured <code>type\: user</code> form \([https\://github\.com/ansible\-collections/community\.libvirt/issues/231](https\://github\.com/ansible\-collections/community\.libvirt/issues/231)\)\.

<a id="community-windows"></a>
#### community\.windows

* community\.windows\.win\_psmodule\_info \- Added <code>include\_properties</code> parameter to allow fine\-grained control over which module properties are returned\, improving performance when only specific properties are needed \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* community\.windows\.win\_psmodule\_info \- Added <code>skip\_module\_repository\_info</code> parameter to skips querying PowerShellGet for repository\-related metadata \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* community\.windows\.win\_psmodule\_info \- Automatically skips expensive PowerShellGet repository lookups when <code>include\_properties</code> is specified without repository\-related properties \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added the <code>device\_group</code> module to manage existing PowerFlex Gen2 device groups\. The module supports getting device group details by name or ID\, renaming a device group\, updating spare node and spare device counts\, and querying usable capacity\. Device group creation and deletion are not supported\.
* Added the <code>thin\_clone</code> module to create thin clones from a source volume or a read\-only snapshot on PowerFlex 5\.x Gen2 systems\. This module is creation\-only\; ongoing management of the resulting thin clone is handled by the <code>volume</code> module\.
* Fixed sanity and lint issues in info\_v2 module\.
* Updated GitHub Actions workflow for improved CI stability\.

<a id="graphiant-naas"></a>
#### graphiant\.naas

* New <code>graphiant\_security\_policy</code> module and <code>security\_policies\_management\.yml</code> playbook for device\-level security rulesets \(<code>edge\.trafficPolicy\.securityRulesets</code>\) and zone pair attachments \(<code>edge\.trafficPolicy\.zones</code>\)\; sample <code>sample\_device\_security\_policies\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code> / <code>attach\_to\_zone\_pairs</code> / <code>detach\_from\_zone\_pairs</code>\; idempotent comparison to live device state\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns accurate <code>changed</code>\, <code>details\.diff\_plan</code>\, and Ansible <code>diff</code> with per\-rule <code>before</code>/<code>after</code> for pending ruleset\, zone\-pair\, and metadata changes\)
* New <code>graphiant\_traffic\_policy</code> module and <code>traffic\_policies\_management\.yml</code> playbook for device\-level traffic rulesets \(<code>edge\.trafficPolicy\.trafficRulesets</code>\) and LAN segment ruleset attachments \(<code>edge\.segments</code>\)\; sample <code>sample\_device\_traffic\_policies\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code> / <code>attach\_to\_lan\_segments</code> / <code>detach\_from\_lan\_segments</code>\; idempotent comparison to live device state\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns accurate <code>changed</code>\, <code>details\.diff\_plan</code>\, and Ansible <code>diff</code> with per\-rule <code>before</code>/<code>after</code> for pending ruleset\, segment\, and metadata changes\)
* <code>gcsdk\_client</code>\: bug fix — <code>get\_matched\_services\_for\_customer</code> no longer raises <code>TypeError</code> when API returns <code>None</code>
* <code>graphiant\_data\_exchange</code> <code>accept\_invitation</code>\: new <code>ipsecGatewayPeers</code> config key replaces <code>ipsecGatewayDetails</code> to support multiple remote VPN peers\; requires <code>graphiant\_sdk \>\= 26\.6\.0</code>
* <code>graphiant\_data\_exchange</code> <code>accept\_invitation</code>\: new <code>vault\_data\_exchange\_bgp\_md5\_passwords</code> and <code>vault\_data\_exchange\_psk</code> module params\; fetch from any secrets store and pass in memory \(<code>no\_log\: true</code>\)\; vault optional — skips gracefully when absent
* <code>graphiant\_data\_exchange</code>\: all Data Exchange workflow playbooks \(02–05\, 07\) support <code>\-e config\_file\=</code> to override the default config YAML\; <code>create\_customers</code> detects <code>adminEmail</code> drift via <code>\-\-check \-\-diff</code>\; <code>accept\_invitation</code> <code>matches\_file</code> is now optional\; <code>\-\-check</code> mode replaces the removed dry\-run playbook\; idempotency integration tests added for all five operations
* <code>graphiant\_ntp</code>\, <code>graphiant\_static\_routes</code>\, <code>graphiant\_site\_to\_site\_vpn</code>\: <code>\-\-check \-\-diff</code> now shows before/after state via <code>diff\_plan</code>\; <code>no\_log\: true</code> removed from module tasks in all playbooks \(masking is already handled by module argument spec <code>no\_log\=True</code> and library <code>\_SENSITIVE\_LOG\_KEYS</code> — task\-level <code>no\_log</code> was suppressing <code>\-\-diff</code> output\)
* <code>graphiant\_site\_to\_site\_vpn</code>\: vault precedence aligned — YAML non\-null wins\, secrets store fills <code>null</code>/absent for <code>presharedKey</code> and <code>md5Password</code>

<a id="kubernetes-core"></a>
#### kubernetes\.core

* helm \- add the <code>server\_side</code> and <code>force\_conflicts</code> options to control Helm v4 server\-side apply when installing or upgrading a release \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164)\)\.
* helm\_plugin \- add <code>\-\-keyring</code> argument to allow changing the keyring default location\. The option is only accepted with <code>state\=present</code> \(the <code>helm plugin install</code> subcommand\)\, as that is the only implemented subcommand that supports <code>\-\-keyring</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1150](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1150)\)\.
* helm\_registry\_auth \- document that\, as of Helm 4\.2\.1\, registry success messages such as <code>Login Succeeded</code> are printed to stdout instead of stderr \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1147](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1147)\)\.
* kubeconfig \- add <code>remove</code> value to the <code>behavior</code> option\, allowing entries to be deleted from the kubeconfig file by name \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1123](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1123)\)\.

<a id="purestorage-flasharray"></a>
#### purestorage\.flasharray

* All Tier 5 modules refactored to use centralized api\_helpers for context\-aware API calls\.
* module\_utils/api\_helpers \- Added centralized API helper functions to reduce code duplication across modules
* module\_utils/api\_helpers \- Added check\_api\_version\(\) for cached API version checking
* module\_utils/api\_helpers \- Added check\_response\(\) for standardized response validation
* module\_utils/api\_helpers \- Added get\_with\_context\(\) for context\-aware API calls eliminating 500\+ duplicated patterns
* module\_utils/error\_handlers \- Added handle\_auth\_error\(\) for improved authentication error messages
* module\_utils/error\_handlers \- Added safe\_api\_call\(\) for comprehensive error handling wrapper
* module\_utils/error\_handlers \- Added standardized error handling framework with FlashArray exception hierarchy
* purefa \- Add API\-client token authentication as an alternative to <code>api\_token</code>\, via a pre\-signed <code>id\_token</code> or a <code>private\_key\_file</code> \(with <code>client\_id</code>\, <code>key\_id</code>\, <code>issuer</code>\, <code>username</code>\)\.
* purefa\_ad \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_admin \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_alert \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_apiclient \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_arrayname \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_audits \- Use get\_with\_context\(\) helper and fix duplicate code bug\.
* purefa\_banner \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_cbsexpand \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_certs \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_connect \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_console \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_default\_protection \- Use centralized api\_helpers for context\-aware API calls and error handling\.
* purefa\_directory \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_dirsnap \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_dns \- Added Fusion support
* purefa\_dns \- Use centralized api\_helpers for context\-aware API calls and error handling\.
* purefa\_ds \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_dsrole \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_dsrole\_old \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_endpoint \- Use centralized api\_helpers for error handling\.
* purefa\_eradication \- Refactored to use centralized api\_helpers for context\-aware API calls
* purefa\_eradication \- Simplified error handling using check\_response\(\) helper
* purefa\_eula \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_export \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_file \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_fleet \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_fs \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_hardware \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_hg \- Refactored to use centralized api\_helpers for error handling
* purefa\_host \- Refactored to use centralized <code>api\_helpers</code> functions \(get\_with\_context\, check\_response\) reducing code by 317 lines
* purefa\_info \- Add the tgroups gather\_subset for topology group reporting\.
* purefa\_kmip \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_maintenance \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_messages \- Use get\_with\_context\(\) helper\.
* purefa\_network \- Use centralized api\_helpers for error handling\.
* purefa\_ntp \- Use centralized api\_helpers for context\-aware API calls and error handling\.
* purefa\_offload \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_pg \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_pgsched \- Use centralized api\_helpers for context\-aware API calls and error handling\.
* purefa\_pgsnap \- Added <code>restore\=all</code> option to restore all member volumes from a protection group snapshot at once using a single API call instead of iterating through each volume individually
* purefa\_pgsnap \- Refactored to use centralized api\_helpers for error handling
* purefa\_phonehome \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_pod \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_pod\_replica \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_proxy \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_ra \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_realm \- Use centralized api\_helpers for error handling\.
* purefa\_saml \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_smis \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_smtp \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_snap \- Refactored to use centralized api\_helpers for error handling
* purefa\_snmp \- Use centralized api\_helpers for error handling\.
* purefa\_snmp\_agent \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_sso \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_subnet \- Refactored to use centralized <em class="title-reference">check\_response\(\)</em> API helper\.
* purefa\_syslog \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_syslog\_settings \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_timeout \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_token \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_user \- Use centralized api\_helpers for error handling\.
* purefa\_vg \- Refactored to use centralized api\_helpers for error handling
* purefa\_vlan \- Use centralized api\_helpers for error handling\.
* purefa\_vnc \- Refactored to use centralized check\_response\(\) helper for API error handling\.
* purefa\_volume \- Refactored error handling to use centralized check\_response\(\) helper \([https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/pull/932](https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/pull/932)\)
* purefa\_volume\_tags \- Use get\_with\_context\(\) and check\_response\(\) helpers\.
* purefa\_workload \- Added custom parameters support
* purefa\_workload \- Use centralized api\_helpers for error handling\.

<a id="purestorage-flashblade"></a>
#### purestorage\.flashblade

* purefb \- Add API\-client token authentication as an alternative to <code>api\_token</code>\, via a pre\-signed <code>id\_token</code> or a <code>private\_key\_file</code> \(with <code>client\_id</code>\, <code>key\_id</code>\, <code>issuer</code>\, <code>username</code>\)\.

<a id="splunk-es-1"></a>
#### splunk\.es

* \.ansible\-lint \- added <code>exclude\_paths</code> entry for <code>\.ansible/</code> to prevent ansible\-lint from scanning installed collection dependencies\.
* \.yamllint \- added <code>\.ansible/</code> to the <code>ignore</code> list for the same reason\.
* Add tests to validate the collection with Ansible 2\.16 and 2\.18\.
* certification\.yml \- added Red Hat partner certification workflow running <code>ansible\-lint</code> \(profile <code>production</code>\) and <code>ansible\-test sanity</code> against Ansible stable\-2\.16\, stable\-2\.18\, and stable\-2\.20\.
* changelogs/changelog\.yaml and changelogs/config\.yaml \- added missing <code>\-\-\-</code> document\-start marker required by the <code>yaml\[document\-start\]</code> yamllint rule\.
* checks\.yml \- introduced a new dedicated workflow triggered only on <code>pull\_request\_target</code> to isolate privileged jobs \(<code>changelog</code> and <code>sonar</code>\) that require write access or secrets from the code\-testing workflow\. Each workflow now has a distinct name to differentiate them in GitHub Actions and branch protection rules\.
* meta/runtime\.yml \- lowered <code>requires\_ansible</code> from <code>\>\=2\.17\.0</code> to <code>\>\=2\.16\.0</code>

<a id="deprecated-features"></a>
### Deprecated Features

<a id="community-clickhouse-1"></a>
#### community\.clickhouse

* clickhouse\_db \- deprecate pre 22\.x handling code for comments \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/217](https\://github\.com/ansible\-collections/community\.clickhouse/issues/217)\)\.
* clickhouse\_role \- list based settings and profiles are marked as deprecated and sheduled for removal in 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/218](https\://github\.com/ansible\-collections/community\.clickhouse/issues/218)\)\.
* clickhouse\_user \- list based settings and profiles are marked as deprecated and sheduled for removal in 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/218](https\://github\.com/ansible\-collections/community\.clickhouse/issues/218)\)\.
* mark ansible\-core\-2\.17 as deprecated\. Support will be removed in future\.

<a id="community-rabbitmq"></a>
#### community\.rabbitmq

* Support for RabbitMQ versions prior to 3\.7\.0 will be dropped in version 2\.0\.0 of this collection \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224)\)\.
* Support for ansible\-core versions prior to 2\.16\.0 will be dropped in version 2\.0\.0 of this collection \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224)\)\.
* collection \- Python 2 support will be dropped in version 2\.0\.0 of this collection\. Make sure you have Python 3 installed on your target machines \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/214](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/214)\)\.

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_fs \- The <code>nfs\_rules</code> parameter is deprecated in favour of <code>export\_policy</code> and will be removed in 2\.0\.0\. A deprecation notice is emitted when it is used\.

<a id="security-fixes"></a>
### Security Fixes

<a id="ansible-posix"></a>
#### ansible\.posix

* authorized\_key \- fix local privilege escalation via symlink\-following when running as root \([https\://github\.com/ansible\-collections/ansible\.posix/issues/759](https\://github\.com/ansible\-collections/ansible\.posix/issues/759)\)\.

<a id="splunk-es-2"></a>
#### splunk\.es

* tests\.yml \- replaced <code>pull\_request\_target</code> trigger with <code>pull\_request</code> for all code\-testing jobs \(<code>sanity</code>\, <code>unit\-galaxy</code>\, <code>ansible\-lint</code>\, <code>build\-import</code>\)\. Using <code>pull\_request\_target</code> exposed repository secrets to workflows that execute untrusted fork code\, creating a potential secret\-exfiltration vector \(pwn request\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-2"></a>
#### Ansible\-core

* encrypt \- fix bcrypt salt string formatting on musl libc by ensuring it is always zero\-padded to 2 digits \([https\://github\.com/ansible/ansible/issues/87180](https\://github\.com/ansible/ansible/issues/87180)\)\.
* parallel fact gathering \- fix hang caused by corrupt async job files\.

<a id="amazon-aws-1"></a>
#### amazon\.aws

* aws\_ssm \- Fixed PowerShell command execution timeouts on Windows caused by PTY echo issues\. Commands are now uploaded to S3 and executed via a small wrapper to avoid echoing large payloads to stdout \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Fixed PowerShell stdin handling for modules that require stdin input on Windows hosts \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Fixed Windows SSM connection failures when transferring files with Unicode characters in filenames or content\. The connection plugin now properly handles UTF\-8 encoding throughout the S3 upload/download process \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Fixed stderr message accumulation across multiple command executions\. Stderr is now flushed at the start of each command to prevent error messages from previous commands appearing in subsequent command output \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- suppress PowerShell progress output in Windows file transfers to prevent stdout pollution that causes transfer failures \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3013](https\://github\.com/ansible\-collections/amazon\.aws/pull/3013)\)\.

<a id="ansible-mysql-1"></a>
#### ansible\.mysql

* mysql\_user \- fix errors on MySQL 9\.7\.0\+ caused by removal of SHA1\(\) SQL function and mysql\_native\_password plugin\. The module now uses <code>IDENTIFIED BY</code> for password management on MySQL 9\.7\.0\+\.

<a id="ansible-posix-1"></a>
#### ansible\.posix

* README \- Added <code>Red Hat Automation Hub</code> as correct contact information for Red Hat Ansible Automation Platform subscribers\.
* sysctl \- reload sysctl only if the sysctl file is <code>/etc/sysctl\.conf</code> or <code>/etc/sysctl\.conf\.local</code> \([https\://github\.com/ansible\-collections/ansible\.posix/issues/663](https\://github\.com/ansible\-collections/ansible\.posix/issues/663)\)\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* setup \- Ensure the <code>ansible\_domain</code> fact has the DNS domain name the host is registered with through the IP properties\. In the past we only returned a value for this fact when the host was joined to an Active Directory domain \- [https\://github\.com/ansible\-collections/ansible\.windows/pull/917](https\://github\.com/ansible\-collections/ansible\.windows/pull/917)
* setup \- Fix DomainInfo collection when LanmanWorkstation service is stopped or disabled on hardened Windows systems \([https\://github\.com/ansible\-collections/ansible\.windows/pull/915](https\://github\.com/ansible\-collections/ansible\.windows/pull/915)\)\.
* setup \- Fix logic for checking SMBIOS version for <code>ansible\_processor\_\*</code> facts when the host\'s SMBIOS version was greater than <code>2\.4</code> but less than <code>3\.0</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/pull/919](https\://github\.com/ansible\-collections/ansible\.windows/pull/919)
* win\_mapped\_drive \- Fixed compatibility with PowerShell 7 by fixing inline C\# declaration
* win\_package \- Favour the HTTP response\'s <code>Content\-Disposition</code> for the temporary filename when downloading a the temporary package from a URL\. This ensures the package detection mechanism on the file extension continues to work \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/503](https\://github\.com/ansible\-collections/ansible\.windows/issues/503)
* win\_powershell \- Fix support for controller side <code>path</code> lookups on Ansible 2\.18 and older
* win\_template \- Fix issue where errors during templating\, like an undefined variable\, were ignored and the task continued without a failure \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/926](https\://github\.com/ansible\-collections/ansible\.windows/issues/926)
* win\_updates \- Add additional post reboot check to ensure that Windows is still not performing more update work after a reboot is complete\.
* win\_updates \- Fix issue display warnings after data tagging changes made in Ansible 2\.19\.
* win\_updates \- Handle update task that errors with <code>ERROR\_SHUTDOWN\_IN\_PROGRESS</code> when <code>reboot\=True</code> is set\. If this error is received and the task has <code>reboot\=True</code> then the module will wait for the reboot to be complete before trying again like how other errors are handled\.

<a id="community-aws-1"></a>
#### community\.aws

* autoscaling\_policy \- allow float type for <code>step\_adjustments</code> <code>lower\_bound</code> and <code>upper\_bound</code> parameters \([https\://github\.com/ansible\-collections/community\.aws/issues/2355](https\://github\.com/ansible\-collections/community\.aws/issues/2355)\)
* wafv2\_web\_acl \- Fixed idempotency issue where rules with rate\_based\_statement would always show as changed when evaluation\_window\_sec was not explicitly specified due to AWS returning the default value of 300 \([https\://github\.com/ansible\-collections/community\.aws/pull/2427](https\://github\.com/ansible\-collections/community\.aws/pull/2427)\)\.

<a id="community-clickhouse-2"></a>
#### community\.clickhouse

* clickhouse\_quota \- add missing on cluster for drop
* clickhouse\_role \- fix cluster for drop role \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/215](https\://github\.com/ansible\-collections/community\.clickhouse/pull/215)\)\.

<a id="community-dns"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-general-1"></a>
#### community\.general

* composer \- restore compatibility with older compose versions when using <code>working\_dir</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12293](https\://github\.com/ansible\-collections/community\.general/issues/12293)\, [https\://github\.com/ansible\-collections/community\.general/pull/12339](https\://github\.com/ansible\-collections/community\.general/pull/12339)\)\.
* filesystem \- the module now also handles the output format of bcachefs\-tools v1\.38\.4 and above \([https\://github\.com/ansible\-collections/community\.general/issues/12259](https\://github\.com/ansible\-collections/community\.general/issues/12259)\, [https\://github\.com/ansible\-collections/community\.general/pull/12291](https\://github\.com/ansible\-collections/community\.general/pull/12291)\)\.
* jenkins\_job\_info \- fix <code>KeyError\: \'color\'</code> when filtering folder jobs by color \([https\://github\.com/ansible\-collections/community\.general/issues/12232](https\://github\.com/ansible\-collections/community\.general/issues/12232)\)\, [https\://github\.com/ansible\-collections/community\.general/pull/12369](https\://github\.com/ansible\-collections/community\.general/pull/12369)\)\.
* nmcli \- now handles connection names derived from MAC addresses\, and generally names that contain <code>\:</code> or <code>\\\\</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12386](https\://github\.com/ansible\-collections/community\.general/issues/12386)\, [https\://github\.com/ansible\-collections/community\.general/pull/12387](https\://github\.com/ansible\-collections/community\.general/pull/12387)\)\.
* opennebula inventory plugin \- fix crash when retrieving VM without NIC \([https\://github\.com/ansible\-collections/community\.general/pull/12361](https\://github\.com/ansible\-collections/community\.general/pull/12361)\)\.
* pacemaker\_resource \- fix bug where the resource\-ready state check did not recognize all valid ready states\, causing the module to time out on resources that never reach the <code>Started</code> state \([https\://github\.com/ansible\-collections/community\.general/issues/12351](https\://github\.com/ansible\-collections/community\.general/issues/12351)\, [https\://github\.com/ansible\-collections/community\.general/pull/12355](https\://github\.com/ansible\-collections/community\.general/pull/12355)\)\.

<a id="community-libvirt-1"></a>
#### community\.libvirt

* inventory \- Added checks to prevent powered\-off hosts from being issued guest agent calls\.
* plugins \- replaced deprecated imports from <code>ansible\.module\_utils\.\_text</code> with <code>ansible\.module\_utils\.common\.text\.converters</code> to avoid ansible\-core deprecation warnings and prepare for removal of the private import path in ansible\-core 2\.24\.
* virt\_cloud\_instance \- added cloud\-config header when converting cloud\-init user\-data from dictionary form\.
* virt\_cloud\_instance \- check if instance exists and not running before calling <code>create\(\)</code>\.
* virt\_install \- added cloud\-config header when converting cloud\-init user\-data from dictionary form\.
* virt\_install \- remove incorrect <code>required\=True</code> from <code>install\.os</code> parameter to allow <code>install\.no\_install\=true</code> without specifying an OS\.

<a id="community-vmware"></a>
#### community\.vmware

* vmware\_guest\_network \- populate <code>vlan\_id</code> in gathered NIC data for Distributed Virtual Portgroup backings so check mode diff does not report a false change when the NIC is already on the requested network\.

<a id="community-windows-1"></a>
#### community\.windows

* community\.windows\.win\_psmodule \- Now retrieves module installation status of requested module instead of all modules\, which was expensive for hosts with many modules installed \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* community\.windows\.win\_psmodule\_info \- Fixed typo in documentation changing <code>procoessor\_architecture</code> to <code>processor\_architecture</code> \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* laps\_password \- Migrate away from deprecated <code>to\_text</code> methods to the new public API\.
* psexec \- Migrate away from deprecated <code>to\_text</code> methods to the new public API\.
* win\_scheduled\_task \- Fix issue when creating a new scheduled task when using <code>become\_user\: SYSTEM</code> \- [https\://github\.com/ansible\-collections/community\.windows/issues/633](https\://github\.com/ansible\-collections/community\.windows/issues/633)

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* ee \- added <code>meta/execution\-environment\.yml</code> to decouple ansible\-builder EE builds from the <code>openshift\-clients</code> system dependency declared in <code>bindep\.txt</code>\, which is not available in standard UBI repositories and caused builds to fail with <code>No package matches \'openshift\-clients\'</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1141](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1141)\)\.
* helm \- use <code>\-\-server\-side\=false \-\-force\-replace</code> instead of the deprecated/removed <code>\-\-force</code> flag when <code>force\=true</code> is used with Helm v4\, preserving the Helm v3 client\-side replacement behaviour and avoiding the server\-side apply conflict \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164)\)\.
* helm \- use the <code>\-\-rollback\-on\-failure</code> flag instead of the deprecated/removed <code>\-\-atomic</code> flag when <code>atomic\=true</code> is used with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1144](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1144)\)\.
* helm\_repository \- correct handling of repository URLs with trailing slashes \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1121](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1121)\)\.
* k8s\_drain \- Fix logic for handling pods with local storage to correctly check for empty\_dir volumes in replicated pods and pods managed by DaemonSets \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1095](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1095)\)\.

<a id="microsoft-ad"></a>
#### microsoft\.ad

* domain \- Ensure that the <em class="title-reference">microsoft\.ad\.domain</em> module errors when a forest already exists\. This prevents the module from attempting to create a new forest if an existing forest is detected and prints an error message indicating that\.
* user \- Ensure any post actions like editing the user\'s groups are performed on the correct distinguished name\. This fixes the error when changing the user\'s groups when the user was moved in the same module invocation\.

<a id="microsoft-iis"></a>
#### microsoft\.iis

* website \- fix <code>changed</code> not set on cert update for existing binding via <code>bindings\.add</code> \([https\://github\.com/ansible\-collections/microsoft\.iis/pull/59](https\://github\.com/ansible\-collections/microsoft\.iis/pull/59)\)\.
* website\_info \- Fix logic for determining <code>use\_ccs</code> is set to take into account new SSL flags added in Server 1809 or newer \- [https\://github\.com/ansible\-collections/microsoft\.iis/pull/57](https\://github\.com/ansible\-collections/microsoft\.iis/pull/57)

<a id="purestorage-flasharray-1"></a>
#### purestorage\.flasharray

* purefa\_dns \- Fixed issue with purefa\_dns not updating DNS config on remote arrays correctly
* purefa\_hg \- Default an empty context to the local array name to avoid an internal error on newer Purity \([https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005](https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005)\)
* purefa\_hg \- Only default the context to the local array name when the array is a fleet member\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_host \- Fixed issue with purefa\_host not updating host config on remote arrays correctly
* purefa\_network \- Fixed crash when clearing IP address with 0\.0\.0\.0/0 without gateway
* purefa\_network \- Fixed crash when setting gateway without an IP address configured
* purefa\_offload \- Fixed broken required\_if validation that never executed due to comparing argument\_spec dictionary to string instead of parameter value
* purefa\_pg \- Default an empty context to the local array name to avoid an internal error on newer Purity \([https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005](https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005)\)
* purefa\_pg \- Fixed adding hostgroups to empty protection group using wrong parameter
* purefa\_pg \- Only default the context to the local array name when the array is a fleet member\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_pgsched \- Fixed issue where <em class="title-reference">snap\_at</em> and <em class="title-reference">replicate\_at</em> parameters were sent to the API even when frequency was not a multiple of days\, causing API errors\.
* purefa\_pgsched \- Fixed replicate\_at \"\" and snap\_at \"\" not clearing schedule times correctly\.
* purefa\_pgsnap \- Default an empty context to the local array name to avoid an internal error on newer Purity \([https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005](https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005)\)
* purefa\_pgsnap \- Only default the context to the local array name when the array is a fleet member\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_pgsnap \- Route context\-aware API calls through the shared api\_helpers so context\_names is only sent when a context is set
* purefa\_pod \- Add idempotency checks for already promoted/demoted pods
* purefa\_pod \- Fix UnboundLocalError when promoting pod without undo\-demote pod
* purefa\_pod \- Fix undo\-demote pod handling during ActiveDR promotion
* purefa\_pod \- Fixed unreachable <code>recover\_pod\(\)</code> branch in <code>main\(\)</code> by reordering conditions to check for destroyed pods before creating new ones
* purefa\_pod \- Fixed unreachable quiescing status check in <code>update\_pod\(\)</code> that was inside a block requiring <code>promotion\_status \=\= \'demoted\'</code>
* purefa\_pod \- Removed duplicate <code>clone\_pod</code> condition in <code>main\(\)</code>
* purefa\_policy \- Added max\_password\_age to current\_pwd\_policy dictionary and PolicyPassword API calls
* purefa\_policy \- Added missing max\_password\_age parameter to DOCUMENTATION\, argument\_spec\, and password policy update logic
* purefa\_policy \- Added missing min\_password\_age parameter to DOCUMENTATION\, argument\_spec\, and password policy update logic
* purefa\_policy \- Corrected min\_password\_age range to 0\-7 days and max\_password\_age range to 0 \(disabled\) or 1\-99999 days per SDK specifications
* purefa\_policy \- Enhanced min\_password\_age and max\_password\_age to accept human\-readable time periods \(e\.g\.\, \'1d\'\, \'90d\'\, \'2h\'\) in addition to integer seconds
* purefa\_policy \- Fixed KeyError when accessing min\_password\_age and max\_password\_age parameters that were used in code but not defined in argument\_spec
* purefa\_policy \- Fixed <code>Versions options must be the same for all NFS export policy rules</code> when adding multiple clients to an existing NFS policy by adding missing <code>nfs\_version</code> parameter
* purefa\_policy \- Fixed critical runtime error in quota policy rule deletion \(line 942\) where rules\[rule\]\.notifications incorrectly used object as dictionary key
* purefa\_policy \- Fixed duplicate condition check \(line 2784\) where changed\_rule was checked twice in the same if statement
* purefa\_policy \- Fixed duplicate variable initialization in update\_policy\(\) function \(line 1509\) where changed\_rule was assigned twice
* purefa\_policy \- Fixed lockout\_duration not being applied when updating password policy
* purefa\_policy \- Fixed min\_password\_age and max\_password\_age to properly convert from human\-readable time periods to milliseconds for SDK compatibility
* purefa\_policy \- Fixed password policy params being set to None when updating other params
* purefa\_policy \- Fixed quota\_notifications normalization using wrong operator
* purefa\_smtp \- Fixed <code>KeyError \'user\_name\'</code> when configuring SMTP with authentication by correcting parameter name from <code>module\.params\[\"user\_name\"\]</code> to <code>module\.params\[\"user\"\]</code>
* purefa\_snap \- Default an empty context to the local array name to avoid an internal error on newer Purity \([https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005](https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005)\)
* purefa\_snap \- Only default the context to the local array name when the array is a fleet member\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_snap \- Only send context\_names when a context is set\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_vg \- Default an empty context to the local array name to avoid an internal error on newer Purity \([https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005](https\://github\.com/Pure\-Storage\-Ansible/FlashArray\-Collection/issues/1005)\)
* purefa\_vg \- Only default the context to the local array name when the array is a fleet member\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_volume \- Only default the context to the local array name when the array is a fleet member\, so standalone arrays do not send fleet context that would fail on stricter Purity releases
* purefa\_volume \- Route all context\-aware API calls through the shared api\_helpers so context\_names is only sent when a context is set\, and fix an inverted version check on the pod\-move path
* purefa\_workload \- Fail with a clear error when the array is not a member of a fleet\, since the module requires a Fusion fleet environment

<a id="purestorage-flashblade-2"></a>
#### purestorage\.flashblade

* purefb\_bucket \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_bucket \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_bucket \- Stop sending context\_names when destroying a bucket without a context\, which leaked an empty/invalid fleet context
* purefb\_bucket\_access \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_bucket\_access \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_bucket\_replica \- Allow a replica link to be removed when its local bucket no longer exists \([https\://github\.com/Everpure\-Ansible/FlashBlade\-Collection/issues/545](https\://github\.com/Everpure\-Ansible/FlashBlade\-Collection/issues/545)\)
* purefb\_bucket\_replica \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_bucket\_replica \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_connect \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_connect \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_export \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_export \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_fs \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_fs \- Fixed <code>not in a fleet</code> errors on standalone arrays by only sending <code>context\_names</code> when a context is set\, and only defaulting the context for arrays that are fleet members\.
* purefb\_fs \- Restore the <code>nfs\_rules</code> parameter\, silently ignored since v1\.25\.0\. Inline NFS export rules are applied again on create and update for non\-realm filesystems\.
* purefb\_groupquota \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_groupquota \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_info \- Fix AttributeError where the policy loop variable was overwritten with <em class="title-reference">policy\.name</em>\, breaking <em class="title-reference">gather\_subset\=policies</em> \(\#547\)
* purefb\_lifecycle \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_lifecycle \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_policy \- Create a policy rule when the client lookup returns no match or an error\, fixing failures adding the first rule for a client while keeping the task idempotent
* purefb\_policy \- Fixed NFS export policy rules not updating when only the <code>access</code> value \(e\.g\. root\-squash to no\-squash\) changed\; <code>access</code> was missing from the idempotency comparison\.
* purefb\_policy \- Fixed an object store access policy rule update referencing a non\-existent key when preserving existing source IPs\.
* purefb\_policy \- Fixed policy rule updates \(NFS export\, SMB share\, SMB client\, network access\) resetting unspecified fields to null\; patches now use merged values so omitted fields are kept\.
* purefb\_policy \- Fixed snapshot policy updates dropping the <code>at</code> time and timezone \(reverting to an interval\-only rule\) when <code>every</code> or <code>keep\_for</code> were changed without re\-specifying <code>at</code>\.
* purefb\_policy \- Only send context\_names when a context is set\, and only default it for fleet members\, avoiding empty\-context errors and \"not in a fleet\" errors on standalone arrays
* purefb\_remote\_cred \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_remote\_cred \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_s3acc \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_s3acc \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_s3user \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_s3user \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_snap \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_snap \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_userpolicy \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_userpolicy \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_userquota \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_userquota \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_virtualhost \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_virtualhost \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays

<a id="splunk-es-3"></a>
#### splunk\.es

* plugins/module\_utils/splunk\.py \- wrapped the <code>ansible\.utils</code> collection import in a <code>try/except</code> block so that <code>ansible\-test sanity \-\-test import</code> no longer raises <code>ModuleNotFoundError</code> in the isolated sanity environment\.

<a id="vultr-cloud"></a>
#### vultr\.cloud

* Fixed an issue with missing Content\-Type HTTP request header\, which resulted in 400 Bad Request \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/186](https\://github\.com/vultr/ansible\-collection\-vultr/issues/186)\)\.

<a id="new-plugins"></a>
### New Plugins

<a id="lookup"></a>
#### Lookup

* community\.general\.proton\_pass \- Fetch secrets from Proton Pass via the <code>pass\-cli</code> command\-line tool\.

<a id="new-modules"></a>
### New Modules

<a id="ansible-mysql-2"></a>
#### ansible\.mysql

* ansible\.mysql\.mysql\_binlog\_info \- Gather MySQL or MariaDB binary log information
* ansible\.mysql\.mysql\_clone \- Clone a MySQL instance from a donor server
* ansible\.mysql\.mysql\_perf\_schema \- Manage MySQL or MariaDB Performance Schema setup tables
* ansible\.mysql\.mysql\_resource\_group \- Add\, update\, or remove MySQL resource groups
* ansible\.mysql\.mysql\_resource\_group\_info \- Gather information about MySQL resource groups
* ansible\.mysql\.mysql\_slow\_log \- Manage MySQL or MariaDB slow query log settings

<a id="community-clickhouse-3"></a>
#### community\.clickhouse

* community\.clickhouse\.clickhouse\_settings\_profile \- Creates\, removes or modify a ClickHouse settings profile using the clickhouse\-driver Client interface

<a id="community-general-2"></a>
#### community\.general

* community\.general\.xml\_info \- Query XML files or strings\.

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.device\_group \- Manage Device Groups on Dell PowerFlex Gen2
* dellemc\.powerflex\.thin\_clone \- Create Thin Clones on Dell PowerFlex 5\.x \(Gen2\)

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* kubernetes\.core\.kubeconfig \- Generate\, update\, and optionally write Kubernetes kubeconfig files

<a id="microsoft-ad-1"></a>
#### microsoft\.ad

* microsoft\.ad\.gpo \- Manage Group Policy Object links
* microsoft\.ad\.pso \- Manage Active Directory Password Settings Objects

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_tgroup \- Manage topology groups on Everpure FlashArrays

<a id="purestorage-flashblade-3"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_s3\_export\_policy \- Manage FlashBlade S3 Export Policies
* purestorage\.flashblade\.purefb\_s3acc\_export \- Manage FlashBlade Object Store Account exports

<a id="unchanged-collections"></a>
### Unchanged Collections

* ansible\.utils \(still version 6\.0\.3\)
* arista\.eos \(still version 12\.1\.2\)
* check\_point\.mgmt \(still version 6\.9\.0\)
* chocolatey\.chocolatey \(still version 1\.6\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.ios \(still version 11\.4\.2\)
* cisco\.iosxr \(still version 12\.3\.2\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.nxos \(still version 11\.2\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.ciscosmb \(still version 1\.0\.12\)
* community\.docker \(still version 5\.2\.1\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.2\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.mysql \(still version 5\.0\.2\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 2\.0\.0\)
* community\.proxysql \(still version 1\.8\.0\)
* community\.routeros \(still version 3\.21\.0\)
* community\.sap\_libs \(still version 1\.7\.0\)
* community\.sops \(still version 2\.4\.0\)
* community\.zabbix \(still version 4\.2\.0\)
* containers\.podman \(still version 1\.20\.2\)
* cyberark\.conjur \(still version 1\.3\.12\)
* cyberark\.pas \(still version 1\.0\.39\)
* dellemc\.enterprise\_sonic \(still version 4\.1\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* f5networks\.f5\_modules \(still version 1\.42\.0\)
* fortinet\.fortimanager \(still version 2\.14\.0\)
* fortinet\.fortios \(still version 2\.5\.1\)
* google\.cloud \(still version 1\.13\.0\)
* grafana\.grafana \(still version 6\.1\.0\)
* hetzner\.hcloud \(still version 6\.10\.0\)
* hitachivantara\.vspone\_block \(still version 4\.8\.2\)
* hitachivantara\.vspone\_object \(still version 1\.2\.0\)
* ibm\.storage\_virtualize \(still version 3\.3\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.8\.1\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* kaytus\.ksmanage \(still version 4\.0\.0\)
* kubevirt\.core \(still version 2\.3\.0\)
* lowlydba\.sqlserver \(still version 2\.8\.1\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.5\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 2\.0\.1\)
* netbox\.netbox \(still version 3\.23\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.6\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* theforeman\.foreman \(still version 5\.11\.0\)
* vmware\.vmware \(still version 2\.9\.0\)
* vmware\.vmware\_rest \(still version 4\.11\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)

<a id="v14-1-0"></a>
## v14\.1\.0

- <a href="#release-summary-1">Release Summary</a>
- <a href="#ansible-core-3">Ansible\-core</a>
- <a href="#changed-collections-1">Changed Collections</a>
- <a href="#major-changes-1">Major Changes</a>
    - <a href="#community-clickhouse-4">community\.clickhouse</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
- <a href="#minor-changes-1">Minor Changes</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#community-ciscosmb">community\.ciscosmb</a>
    - <a href="#community-clickhouse-5">community\.clickhouse</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-windows-2">community\.windows</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#graphiant-naas-1">graphiant\.naas</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#hitachivantara-vspone-object">hitachivantara\.vspone\_object</a>
    - <a href="#microsoft-ad-2">microsoft\.ad</a>
    - <a href="#microsoft-iis-1">microsoft\.iis</a>
    - <a href="#purestorage-flashblade-4">purestorage\.flashblade</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#deprecated-features-1">Deprecated Features</a>
    - <a href="#community-clickhouse-6">community\.clickhouse</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#vmware-vmware-rest-2">vmware\.vmware\_rest</a>
- <a href="#security-fixes-1">Security Fixes</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#graphiant-naas-2">graphiant\.naas</a>
- <a href="#bugfixes-1">Bugfixes</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#ansible-windows-3">ansible\.windows</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general-4">community\.general</a>
    - <a href="#community-windows-3">community\.windows</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#microsoft-ad-3">microsoft\.ad</a>
    - <a href="#purestorage-flashblade-5">purestorage\.flashblade</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-3">vmware\.vmware\_rest</a>
- <a href="#new-plugins-1">New Plugins</a>
    - <a href="#filter">Filter</a>
- <a href="#new-modules-1">New Modules</a>
    - <a href="#ansible-windows-4">ansible\.windows</a>
    - <a href="#community-clickhouse-7">community\.clickhouse</a>
    - <a href="#community-general-5">community\.general</a>
    - <a href="#microsoft-ad-4">microsoft\.ad</a>
    - <a href="#purestorage-flashblade-6">purestorage\.flashblade</a>
- <a href="#unchanged-collections-1">Unchanged Collections</a>

<a id="release-summary-1"></a>
### Release Summary

Release Date\: 2026\-06\-18

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="ansible-core-3"></a>
### Ansible\-core

Ansible 14\.1\.0 contains ansible\-core version 2\.21\.1\.
This is a newer version than version 2\.21\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="changed-collections-1"></a>
### Changed Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                   | Ansible 14.0.0 | Ansible 14.1.0 | Notes                                                                                                                                                                                                        |
| ---------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ansible.netcommon            | 8.5.2          | 8.5.3          |                                                                                                                                                                                                              |
| ansible.utils                | 6.0.2          | 6.0.3          |                                                                                                                                                                                                              |
| ansible.windows              | 3.5.0          | 3.6.1          |                                                                                                                                                                                                              |
| arista.eos                   | 12.1.1         | 12.1.2         |                                                                                                                                                                                                              |
| azure.azcollection           | 3.18.0         | 3.19.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.intersight             | 2.18.0         | 2.19.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.ios                    | 11.4.1         | 11.4.2         |                                                                                                                                                                                                              |
| cisco.iosxr                  | 12.3.1         | 12.3.2         |                                                                                                                                                                                                              |
| cisco.meraki                 | 2.23.2         | 2.24.0         |                                                                                                                                                                                                              |
| community.ciscosmb           | 1.0.11         | 1.0.12         |                                                                                                                                                                                                              |
| community.clickhouse         | 2.1.0          | 2.2.0          |                                                                                                                                                                                                              |
| community.crypto             | 3.2.1          | 3.2.2          |                                                                                                                                                                                                              |
| community.dns                | 4.0.0          | 4.0.1          |                                                                                                                                                                                                              |
| community.docker             | 5.2.0          | 5.2.1          |                                                                                                                                                                                                              |
| community.general            | 13.0.1         | 13.1.0         |                                                                                                                                                                                                              |
| community.routeros           | 3.20.0         | 3.21.0         |                                                                                                                                                                                                              |
| community.sops               | 2.3.0          | 2.4.0          |                                                                                                                                                                                                              |
| community.windows            | 3.1.0          | 3.2.0          |                                                                                                                                                                                                              |
| containers.podman            | 1.20.1         | 1.20.2         |                                                                                                                                                                                                              |
| cyberark.conjur              | 1.3.9          | 1.3.12         | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| f5networks.f5_modules        | 1.41.0         | 1.42.0         | The collection did not have a changelog in this version.                                                                                                                                                     |
| graphiant.naas               | 26.4.0         | 26.5.0         |                                                                                                                                                                                                              |
| hetzner.hcloud               | 6.9.0          | 6.10.0         |                                                                                                                                                                                                              |
| hitachivantara.vspone_block  | 4.8.1          | 4.8.2          |                                                                                                                                                                                                              |
| hitachivantara.vspone_object | 1.1.1          | 1.2.0          |                                                                                                                                                                                                              |
| infinidat.infinibox          | 1.6.3          | 1.8.1          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| kubevirt.core                | 2.2.4          | 2.3.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| microsoft.ad                 | 1.10.0         | 1.11.0         |                                                                                                                                                                                                              |
| microsoft.iis                | 1.1.0          | 1.2.0          |                                                                                                                                                                                                              |
| openstack.cloud              | 2.5.0          | 2.6.0          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| purestorage.flashblade       | 1.24.0         | 1.25.1         |                                                                                                                                                                                                              |
| vmware.vmware                | 2.8.0          | 2.9.0          |                                                                                                                                                                                                              |
| vmware.vmware_rest           | 4.10.0         | 4.11.0         |                                                                                                                                                                                                              |

<a id="major-changes-1"></a>
### Major Changes

<a id="community-clickhouse-4"></a>
#### community\.clickhouse

* clickhouse\_named\_collection \- new module to add/modify/delete named collections in database\.

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* Update minimum required ansible\-core version to 2\.16 in meta/runtime\.yml

<a id="minor-changes-1"></a>
### Minor Changes

<a id="ansible-windows-2"></a>
#### ansible\.windows

* win\_dhcp\_lease \- add support for computername parameter\.
* win\_ping \- Added support for running on non\-Windows targets
* win\_powershell \- Added support for running on non\-Windows targets
* win\_powershell \- Allow sensitive\_parameters entries with neither <code>value</code> nor <code>username</code>/<code>password</code> specified\, passing <code>\$null</code> as the parameter value instead of an empty SecureString\.
* win\_tempfile \- Added support for running on non\-Windows targets
* win\_tempfile \- Changed the default for <code>path</code> to be <code>None</code> rather than <code>\%TEMP\%</code>\. The module will instead use the result of <code>\[System\.IO\.Path\]\:\:GetTempPath\(\)</code> to determine the temporary directory to use which on Windows will typically be the same as <code>\%TEMP\%</code>\.
* windows \- Validated that the collection works correctly with Python 3\.12 \([https\://issues\.redhat\.com/browse/ACA\-5197](https\://issues\.redhat\.com/browse/ACA\-5197)\)\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* devices\_camera\_clip\_info \- Added new plugin to retrieve camera clip information\.
* networks\_appliance\_uplinks\_nat \- Added new plugin to manage appliance uplink NAT settings\.
* organizations\_api\_rest\_provisioning\_pipelines\_jobs\_info \- Added new plugin to retrieve REST API provisioning pipeline job information\.
* organizations\_api\_rest\_provisioning\_pipelines\_jobs\_overviews\_by\_pipeline\_info \- Added new plugin\.
* organizations\_appliance\_uplinks\_nat\_by\_network\_info \- Added new plugin\.
* organizations\_policies\_global\_firewall\_application\_categories\_info \- Added new plugin\.
* organizations\_policies\_global\_firewall\_rulesets \- Added new plugin to manage global firewall rulesets\.
* organizations\_policies\_global\_firewall\_rulesets\_info \- Added new plugin\.
* organizations\_policies\_global\_firewall\_rulesets\_rules \- Added new plugin\.
* organizations\_policies\_global\_firewall\_rulesets\_rules\_info \- Added new plugin\.
* organizations\_policies\_global\_group\_policies \- Added new plugin to manage global group policies\.
* organizations\_policies\_global\_group\_policies\_adaptive\_policy\_groups\_assign \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_adaptive\_policy\_groups\_assignments\_info \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_adaptive\_policy\_groups\_remove \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_appliance\_vlans\_assign \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_appliance\_vlans\_assignments\_by\_vlan\_info \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_appliance\_vlans\_assignments\_info \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_appliance\_vlans\_remove \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_firewall\_rulesets\_assignments \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_firewall\_rulesets\_assignments\_info \- Added new plugin\.
* organizations\_policies\_global\_group\_policies\_info \- Added new plugin to retrieve global group policies\.
* organizations\_sase\_connectors\_batch\_create \- Added new plugin to batch create SASE connectors\.
* organizations\_sase\_connectors\_batch\_delete \- Added new plugin to batch delete SASE connectors\.
* organizations\_sase\_connectors\_info \- Added new plugin to retrieve SASE connector information\.
* organizations\_sase\_regions\_info \- Added new plugin to retrieve SASE region information\.
* organizations\_sase\_sites \- Added new plugin to manage SASE sites\.
* organizations\_sase\_sites\_attach \- Added new plugin to attach networks to SASE sites\.
* organizations\_sase\_sites\_connectivity\_history\_by\_site\_info \- Added new plugin to retrieve SASE site connectivity history\.
* organizations\_sase\_sites\_connectivity\_overview\_info \- Added new plugin to retrieve SASE site connectivity overview\.
* organizations\_sase\_sites\_detach \- Added new plugin to detach networks from SASE sites\.
* organizations\_sase\_sites\_info \- Added new plugin to retrieve SASE site information\.

<a id="community-ciscosmb"></a>
#### community\.ciscosmb

* Solve CI doesn\'t satisfy ACP requirements
* Update unit tests to use collection\-local helpers instead of community\.internal\_test\_tools\, and make set\_module\_args compatible with current Ansible module argument serialization\.

<a id="community-clickhouse-5"></a>
#### community\.clickhouse

* Added warning about using unsupported server version\.
* Fetch server version only once during opening connection to a database\.
* Refactored user/role settings for better maintainability and improved idempotency\. Since now settings option accepts both list\(old\) argument or dictionary\(new\)\. Profiles are moved to a separate option\. \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/178](https\://github\.com/ansible\-collections/community\.clickhouse/pull/178)\)\.
* clickhouse\_client \- Change how server errors are handled\. Previously\, error code 497 \(ACCESS\_DENIED / not enough privileges\) was always treated as success with no way to disable this behavior\. Old behavior is preserved by default\. It is now possible to control which error codes are treated as success using the new <code>success\_on</code> parameter \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/117](https\://github\.com/ansible\-collections/community\.clickhouse/issues/117)\)\.
* clickhouse\_db \- support for changing database comment\. Requires ClickHouse server version \>\= 25\.8 \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/189](https\://github\.com/ansible\-collections/community\.clickhouse/issues/189)\)\.
* clickhouse\_named\_collection \- improve SQL injection protection with parameterized queries\, identifier validation\, and new <em class="title-reference">query\_parameters</em> output\.
* clickhouse\_role \- added the <code>profile</code> argument to apply settings profiles to role \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/196](https\://github\.com/ansible\-collections/community\.clickhouse/pull/196)\)\.
* clickhouse\_user \- added the <code>profile</code> argument to apply settings profiles to user \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/196](https\://github\.com/ansible\-collections/community\.clickhouse/pull/196)\)\.

<a id="community-general-3"></a>
#### community\.general

* consul\_kv lookup plugin \- add <code>empty\_value</code> option to control what is returned for null Consul values \([https\://github\.com/ansible\-collections/community\.general/issues/11039](https\://github\.com/ansible\-collections/community\.general/issues/11039)\, [https\://github\.com/ansible\-collections/community\.general/pull/12120](https\://github\.com/ansible\-collections/community\.general/pull/12120)\)\.
* dnf\_config\_manager \- lookup path to the <code>dnf</code> binary in <code>PATH</code>\. It used to be fixed to <code>/usr/bin/dnf</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12219](https\://github\.com/ansible\-collections/community\.general/pull/12219)\)\.
* filesystem \- adds GFS2 support \([https\://github\.com/ansible\-collections/community\.general/pull/12285](https\://github\.com/ansible\-collections/community\.general/pull/12285)\)\.
* keycloak\_realm \- add <code>max\_secondary\_auth\_failures</code> parameter to configure brute force detection for secondary authentication mechanisms \([https\://github\.com/ansible\-collections/community\.general/pull/12087](https\://github\.com/ansible\-collections/community\.general/pull/12087)\)\.
* slack \- added support for uploading files to channels and threads using the new Slack WebAPI \([https\://github\.com/ansible\-collections/community\.general/pull/12032](https\://github\.com/ansible\-collections/community\.general/pull/12032)\)\.
* sudoers \- add <code>defaults</code> parameter to allow specifying <code>Defaults</code> directives scoped to the user or group in the generated sudoers file \([https\://github\.com/ansible\-collections/community\.general/pull/12186](https\://github\.com/ansible\-collections/community\.general/pull/12186)\)\.
* xbps \- include <code>stdout</code> and <code>stderr</code> from the last executed command in module output \([https\://github\.com/ansible\-collections/community\.general/issues/2478](https\://github\.com/ansible\-collections/community\.general/issues/2478)\, [https\://github\.com/ansible\-collections/community\.general/pull/12234](https\://github\.com/ansible\-collections/community\.general/pull/12234)\)\.
* xenserver\_guest\_info \- add VDI <code>uuid</code> and <code>vdi\_type</code> \(VHD/QCOW2\) fields to disk info output \([https\://github\.com/ansible\-collections/community\.general/issues/11998](https\://github\.com/ansible\-collections/community\.general/issues/11998)\, [https\://github\.com/ansible\-collections/community\.general/pull/12119](https\://github\.com/ansible\-collections/community\.general/pull/12119)\)\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_info\, api\_modify \- add support for the <code>dhcp\-agent\-circuit\-id</code>\, <code>dhcp\-agent\-remote\-id</code>\, <code>dhcpv6\-agent\-circuit\-id</code>\, <code>dhcpv6\-agent\-remote\-id</code>\, and <code>dhcpv6\-snooping</code> parameters in the <code>interface bridge</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/468](https\://github\.com/ansible\-collections/community\.routeros/pull/468)\)\.
* api\_info\, api\_modify \- add support for the <code>trusted\-dhcpv6</code> parameter in the <code>interface bridge port</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/468](https\://github\.com/ansible\-collections/community\.routeros/pull/468)\)\.
* api\_info\, api\_modify \- add the <code>from\-pool\-policy</code> field to the <code>ipv6 address</code> path for RouterOS 7\.23 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/469](https\://github\.com/ansible\-collections/community\.routeros/pull/469)\)\.
* api\_info\, api\_modify \- remove support for the deprecated <code>add\-dhcp\-option82</code> parameter in the <code>interface bridge</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/468](https\://github\.com/ansible\-collections/community\.routeros/pull/468)\)\.

<a id="community-sops"></a>
#### community\.sops

* Support OpenSuSE Tumbleweed \(and probably also Leap\) in the community\.sops\.install role\. Right now only Tumbleweed is tested in CI\, so support for Leap has not been verified \([https\://github\.com/ansible\-collections/community\.sops/pull/299](https\://github\.com/ansible\-collections/community\.sops/pull/299)\)\.

<a id="community-windows-2"></a>
#### community\.windows

* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* win\_unzip \- Use <code>tar\.exe</code> from <code>\%SystemRoot\%\\System32</code> on Windows 10 build 17063 and later and Windows Server 2019 and later to extract tar\-based archives \(<code>\.tar</code>\, <code>\.tar\.gz</code>/<code>\.tgz</code>\, <code>\.tar\.bz2</code>/<code>\.tbz2</code>\, <code>\.tar\.xz</code>/<code>\.txz</code>\) without requiring PSCX\. On older systems where <code>tar\.exe</code> is not available\, PSCX remains the fallback\. PSCX is still required for passwords\, recursive extraction\, and non\-tar formats other than <code>\.zip</code>\.
* win\_xml \- add new option <code>content</code> to be able to return the content of nodes \([https\://github\.com/ansible\-collections/community\.windows/issues/54](https\://github\.com/ansible\-collections/community\.windows/issues/54)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* podman\_quadlet \- Add support for aliases for Quadlets

<a id="graphiant-naas-1"></a>
#### graphiant\.naas

* Backbone operations\: <code>configure</code> / <code>deconfigure</code> \(orchestrate sites \+ tunnel\-underlay phasing \+ per\-device push\)\, <code>configure\_core\_to\_core\_interfaces</code> / <code>deconfigure\_core\_to\_core\_interfaces</code> \(with VLAN sub\-interface support\)\, <code>configure\_core\_to\_core\_tunnel\_interfaces</code> / <code>deconfigure\_core\_to\_core\_tunnel\_interfaces</code>\, <code>configure\_wan\_circuits</code> / <code>deconfigure\_wan\_circuits</code>\, <code>configure\_direct\_peer\_interfaces</code> / <code>deconfigure\_direct\_peer\_interfaces</code>\, <code>configure\_syslog\_targets</code> / <code>deconfigure\_syslog\_targets</code>
* Collection version bumped to 26\.5\.0
* Deconfigure workflows are idempotent\: parent and VLAN sub\-interface existence checked via <code>gsdk\.get\_device\_info</code> before issuing deletes\; per\-VRF <code>syslogTargets</code> existence checked against <code>device\.segments\[\*\]\.syslog\_targets\[\*\]\.name</code>
* Minimum <code>graphiant\-sdk</code> raised to <code>\>\= 26\.5\.0</code> \(see <code>\_version\.py</code> <code>DEPENDENCIES</code>\)
* New <code>backbone\_interface\_template\.yaml</code> Jinja2 template covering Core <code>interface\_type</code> flavors\: <code>loopback</code>\, <code>core\_to\_core\_link</code> \(with VLAN sub\-interfaces \+ <code>ospf</code> block rendered to <code>coreNeighbor</code>\)\, <code>core\_to\_core\_ipsec\_tunnel</code>\, <code>p2mp\_tunnel</code>\, <code>isp\_circuit</code>\, <code>direct\_peer</code>\, <code>disabled</code>
* New <code>graphiant\_backbone</code> module and <code>backbone\_management\.yml</code> playbook for managing Graphiant Core \(backbone\) device configuration\; samples <code>sample\_backbone\_config\.yaml</code> and <code>sample\_backbone\_direct\_peer\_config\.yaml</code>
* New <code>graphiant\_edge\_services</code> module and <code>edge\_services\_management\.yml</code> playbook for Edge/Gateway DHCP subnets\, DNS mode\, LLDP\, and local web server password\; sample <code>sample\_edge\_services\.yaml</code>
* New <code>graphiant\_macsec</code> and <code>graphiant\_macsec\_info</code> modules and <code>macsec\_management\.yml</code> playbook for interface MACsec configuration and monitoring\; sample <code>sample\_macsec\.yaml</code>
* New <code>graphiant\_prefix\_port\_list</code> module and <code>prefix\_port\_list\_mangement\.yml</code> playbook for managing Prefix and Port Lists on Edge devices\; sample <code>sample\_prefix\_and\_port\_list\.yaml</code>
* <code>BackboneManager</code> registered on <code>GraphiantConfig\.backbone</code>\; payloads build the <code>core</code> branch \(counterpart to <code>graphiant\_interfaces</code> on <code>edge</code>\)\. <code>ConfigTemplates\.render\_backbone\_interface\(\)</code> and <code>ConfigUtils\.device\_backbone\_interface\(\)</code> render the new template

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* load\_balancer\_info \- Added the HTTP idle timeout property to the services return values \(<code>hcloud\_load\_balancer\_info\[\]\.services\[\]\.http\.timeout\_idle</code>\)\.
* load\_balancer\_service \- Added the <code>http\.timeout\_idle</code> argument to configure the idle timeout in seconds for HTTP services\.

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Added a new input parameter “force\_create” in the “gad\_bulk” module to allow GAD pair creation even when resources are locked\, must be used only within the “resource\_management\_with\_lock” module\.
* Added a new playbook “remote\_replication\_gad” in the resource\_management\_with\_lock module\.
* Added a new state “forced\_present” in the gad module to allow GAD pair creation even when resources are locked\, must be used only within the “resource\_management\_with\_lock” module\.
* Added support for SVOS 10\.5\.3 NVMe\_FC management “nvm\_subsystems” and “nvm\_subsystem\_facts”\,\( with the limitation that port configuration migration from FC to NVMe\_FC\) for VSP One BHE storage models\.
* Added support for input parameter wait\_for\_final\_state for following module hv\_snapshot\.
* Removed the input parameters “delete\_mode” and “allow\_volume\_access\_after\_force\_delete” from the “hv\_vsp\_one\_gad” module\.

<a id="hitachivantara-vspone-object"></a>
#### hitachivantara\.vspone\_object

* Added role <em class="title-reference">hv\_vspone\_object\_certificate\_upload\_role</em> to upload certificate files from a folder to VSP One Object\.
* Added role <em class="title-reference">hv\_vspone\_object\_kmip\_server\_role</em> to update HTTPS cipher strings for existing KMIP servers\.
* Added role <em class="title-reference">hv\_vspone\_object\_license\_role</em> to set serial number and upload a license file\.
* Added role <em class="title-reference">hv\_vspone\_object\_storage\_component\_role</em> to activate storage components and retrieve components filtered by used capacity\.

<a id="microsoft-ad-2"></a>
#### microsoft\.ad

* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* microsoft\.ad\.ldap \- Added new option <code>domain\_realm</code> that can be used to set the Kerberos realm in the SRV lookup\. This option provides a way to override the <code>krb5\.conf</code> or avoid the requirement on Kerberos for the LDAP lookup entirely\.

<a id="microsoft-iis-1"></a>
#### microsoft\.iis

* microsoft\.iis\.website \- Add preload support for websites using the <code>preload\_enabled</code> option

<a id="purestorage-flashblade-4"></a>
#### purestorage\.flashblade

* Add comprehensive testing infrastructure with pytest framework \(\#502\)
* Add comprehensive unit tests for purefb\.py utilities \(get\_system\, purefb\_argument\_spec\)
* Add coverage reporting with HTML and XML artifacts \(\#503\)
* Add coverage summary to GitHub Actions job output \(\#503\)
* Add pytest configuration and shared test fixtures \(\#502\)
* Add test requirements and directory structure \(\#502\)
* Add unit test execution to GitHub Actions CI workflow \(\#503\)
* Add unit tests for common module utilities \(\#502\)
* Add unit tests for purefb\_eula module
* Add unit tests for purefb\_info module
* Add unit tests for purefb\_timeout module
* Add unit tests for simple modules \(purefb\_bladename\, purefb\_timeout\, purefb\_eula\)
* Add unit tests for time\_utils module with 100\% coverage \(\#502\)
* Expand test coverage from 15\% to improve code quality and prevent regressions
* Removed multiple un\-pythonic range iterations
* Standardize all import checks of Pure SDK to use the same variable name
* common \- Add comprehensive docstrings to human\_to\_bytes\, human\_to\_real\, and get\_local\_tz functions \(\#494\)
* common \- Add get\_error\_message\(\) utility function for safe API error extraction \(\#496\)
* purefb \- Add comprehensive docstrings to get\_system and purefb\_argument\_spec functions \(\#494\)
* purefb\_fs \- Added <code>realm</code> parameter to support creating filesystems in realms \(requires Purity//FB 4\.6\.1\+\)
* purefb\_info \- Updated to use get\_policies\_all\(\) method and added policy type breakdown to default output

<a id="vmware-vmware"></a>
#### vmware\.vmware

* cluster\_drs\_vm\_overrides \- add module to manage DRS VM override settings on vSphere clusters
* cluster\_drs\_vm\_overrides\_info \- add module to gather DRS VM override settings for a cluster
* cluster\_ha\_vm\_overrides \- add module to manage HA VM override settings on vSphere clusters
* cluster\_ha\_vm\_overrides\_info \- add module to gather HA VM override settings for a cluster
* inventory plugins \- Improve how properties are gathered to decrease execution time \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/318](https\://github\.com/ansible\-collections/vmware\.vmware/issues/318)\)\.
* key\_provider\_info \- add module to gather information about key providers in vCenter
* key\_provider\_native \- add module to manage native key providers in vCenter
* key\_provider\_standard \- add module to manage standard key providers and KMS servers in vCenter
* vm \- Add enable\_vtpm parameter to enable or disable virtual Trusted Platform Module \(vTPM\) on virtual machines\.
* vm\_snapshot \- Add a timeout parameter to define how long the module will wait for the task to finish \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/361](https\://github\.com/ansible\-collections/vmware\.vmware/issues/361)\)\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* Add support for ansible\-core 2\.21

<a id="deprecated-features-1"></a>
### Deprecated Features

<a id="community-clickhouse-6"></a>
#### community\.clickhouse

* clickhouse\_user \- <code>password</code> and <code>type\_password</code> are deprecated and will be removed in <code>community\.clickhouse 3\.0\.0</code>\, use the <code>authentication</code> instead\.

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* datacenter\_info \- The <code>datacenter\_info</code> module is deprecated and will be removed after 1 Oct\. 2026\. Please use the <code>location\_info</code> module instead\.

<a id="vmware-vmware-rest-2"></a>
#### vmware\.vmware\_rest

* turbo mode and the associated environment variable <code>VMWARE\_ENABLE\_TURBO</code> are deprecated and will be removed from <code>vmware\.vmware\_rest</code> 5\.0\.0 \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/639](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/639)\)\.

<a id="security-fixes-1"></a>
### Security Fixes

<a id="ansible-core-4"></a>
#### Ansible\-core

* ansible\-galaxy install \- Ensure role requirements are passed as positional arguments to <a href="#system-message-1"><span class="problematic">\:command\:\`git clone\`</span></a>\. Previously\, a malicious role author could inject arbitrary git configuration in role dependencies\. \(CVE\-2026\-11332\)

  <details>
  <summary><strong>ERROR/3</strong> (&lt;string&gt;, line 1)</summary>

  Unknown interpreted text role \"command\"\.

  </details>
* psrp \- Do not log raw stdout/stderr on verbosity 5 when task has <code>no\_log\: true</code> set
* winrm \- Do not log raw stdout/stderr on verbosity 5 when task has <code>no\_log\: true</code> set

<a id="graphiant-naas-2"></a>
#### graphiant\.naas

* Mask API keys in <code>\_SENSITIVE\_LOG\_KEYS</code> \(<code>device\_config\_common</code>\) in <code>gcsdk\_client</code> <code>put\_device\_config</code> / <code>put\_device\_config\_raw</code> and <code>show\_validated\_payload</code> log output

<a id="bugfixes-1"></a>
### Bugfixes

<a id="ansible-core-5"></a>
#### Ansible\-core

* cli \- handle empty value for PAGER \([https\://github\.com/ansible/ansible/issues/86898](https\://github\.com/ansible/ansible/issues/86898)\)\.
* config \- use correct key value for inject\_invocation setting \([https\://github\.com/ansible/ansible/issues/86999](https\://github\.com/ansible/ansible/issues/86999)\)\.
* free strategy \- Fix <code>IndexError</code> when hosts become unreachable during playbook execution \([https\://github\.com/ansible/ansible/issues/87027](https\://github\.com/ansible/ansible/issues/87027)\)\.
* meta pseudo\-action \- Fixed callback args passed to <code>v2\_runner\_on\_skipped</code> when any <code>meta</code> action was skipped by a <code>when</code> condition\; added test coverage\. A previous regression caused the callback dispatch to be omitted and a warning issued\.
* module\_utils sanitize\_keys and remove\_value functions now sort their input to ensure matching subsets are always obscured\.
* module\_utils/basic\.py \- Fix <code>AnsibleModule\.run\_command\(\)</code> to handle <code>None</code> return from non\-blocking pipe reads \([https\://github\.com/ansible/ansible/issues/86920](https\://github\.com/ansible/ansible/issues/86920)\)\.
* wait\_for \- use <code>errno\.ENOENT</code> symbolic constant instead of hardcoded value for improved code portability\.

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* memory cache plugin \- Add missing <code>\_persistent</code> attribute to <code>CacheModule</code> to fix <code>\'CacheModule\' object has no attribute \'\_persistent\'</code> error with ansible\-core 2\.19\+ when <code>single\_user\_mode</code> caching is enabled \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/781](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/781)\)\.
* network\_cli \- Fix <code>proxy\_command</code> silently ignored with <code>ssh\_type\=paramiko</code> \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/776](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/776)\)\.
* vlan\_parser \- Fix <code>IndexError</code> when an empty list is passed as input by returning an empty list instead of crashing \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/302](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/302)\)\.

<a id="ansible-utils"></a>
#### ansible\.utils

* Fix update\_fact to update a fact where a key in the referenced path contains a bracket\.

<a id="ansible-windows-3"></a>
#### ansible\.windows

* setup \- Fix admin checks to ensure facts that require administrator access actually run \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/900](https\://github\.com/ansible\-collections/ansible\.windows/issues/900)
* setup \- Fix failure when attempting to retrieve <code>ansible\_processor\_cores</code> and <code>ansible\_processor\_threads\_per\_core</code> on a host without the required SMBIOS data\. Admin users can still retrieve this through WMI but non\-admin users will set these facts as null and avoid the lengthy timeout and failure\.
* win\_dhcp\_lease \- Fix scope filtering when searching for existing leases or reservations\: ensure the query is limited to the specified scope\. This prevents ambiguity when the same MAC address exists in multiple scopes \(e\.g\. a device with reservations in different scopes\)\.
* win\_find \- Fix depth and recursion logic that resulted in directories being skipped or depth being ignored \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/839](https\://github\.com/ansible\-collections/ansible\.windows/issues/839)
* win\_reboot \- Display warning if the reboot command returned <code>A system shutdown is in progress\. \(1115\)</code>\. This can be triggered by a service external to Ansible triggers the shutdown and Ansible attempts to reboot by running <code>shutdown\.exe</code>\.
* win\_stat / win\_find \- try/catch Access Denied when querying Win32\_Share for share info\. Non\-admin users now get warning instead of failure\. Fixes 809\.

<a id="arista-eos"></a>
#### arista\.eos

* eos\_acls \- Fix issue where <code>state\: replaced</code> did not generate the <code>standard</code> keyword for standard ACLs \([https\://github\.com/ansible\-collections/arista\.eos/issues/608](https\://github\.com/ansible\-collections/arista\.eos/issues/608)\)\.

<a id="cisco-ios"></a>
#### cisco\.ios

* ios\_acls \- Fix incorrect CLI command generation for IPv6 ACL remarks\. The module now correctly generates <code>sequence N remark</code> syntax for IPv6 instead of the IPv4\-style <code>N remark</code> format\. Negation also correctly uses <code>no sequence N remark</code>\.
* plugins/modules/ios\_user\.py \- Fix matching existing SSH keys in running configurations while allowing optional trailing whitespace  when using the purge\_keys parameter\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* iosxr\_ospfv2 \- Enhanced max\-metric router\-lsa support with comprehensive configuration options \(external\-lsa\, summary\-lsa\, on\-startup with wait\_for\_bgp/wait\_period\, include\-stub\)\, added mutual exclusivity validation for conflicting parameters\, corrected on\_startup\.wait\_for\_bgp parameter type from integer to boolean\, and fixed idempotency across all states\.

<a id="community-crypto-1"></a>
#### community\.crypto

* gpg\_fingerprint lookup plugin\, gpg\_fingerprint filter plugin \- prevent GnuPG from unnecessarily starting gpg\-agent \([https\://github\.com/ansible\-collections/community\.crypto/issues/1026](https\://github\.com/ansible\-collections/community\.crypto/issues/1026)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/1029](https\://github\.com/ansible\-collections/community\.crypto/pull/1029)\)\.
* openssh\_\* modules \- prevent use of currently unsupported MLDSA private keys in the cryptography backend \([https\://github\.com/ansible\-collections/community\.crypto/pull/1044](https\://github\.com/ansible\-collections/community\.crypto/pull/1044)\)\.
* openssl\_pkcs12 \- prevent use of MLDSA private keys\, which are not supported by PKCS\#12\, or at least cryptography\'s implementation \([https\://github\.com/ansible\-collections/community\.crypto/pull/1044](https\://github\.com/ansible\-collections/community\.crypto/pull/1044)\)\.

<a id="community-dns-1"></a>
#### community\.dns

* Update Public Suffix List\.

<a id="community-docker"></a>
#### community\.docker

* docker\_container\_exec module\, docker\_api connection plugin \- ensure that when a command is run in a container with stdin provided\, that the actual response is closed and not a socket derived from it\. The old behavior causes warnings to be shown on Python 3\.13\+ under certain conditions \([https\://github\.com/ansible\-collections/community\.docker/issues/1247](https\://github\.com/ansible\-collections/community\.docker/issues/1247)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1260](https\://github\.com/ansible\-collections/community\.docker/pull/1260)\)\.

<a id="community-general-4"></a>
#### community\.general

* aix\_devices \- fix <code>chdev</code> command failures being incorrectly reported as successful results\, now properly fails the task when device attribute changes cannot be applied \([https\://github\.com/ansible\-collections/community\.general/pull/12185](https\://github\.com/ansible\-collections/community\.general/pull/12185)\)\.
* composer \- the <code>\-\-working\-dir</code> option is now always placed first on the command line\, before the subcommand\, to ensure consistent behavior across all composer commands \([https\://github\.com/ansible\-collections/community\.general/issues/5204](https\://github\.com/ansible\-collections/community\.general/issues/5204)\, [https\://github\.com/ansible\-collections/community\.general/pull/12084](https\://github\.com/ansible\-collections/community\.general/pull/12084)\)\.
* composer \- use file checksum to determine <code>changed</code> status when <code>command\=config</code>\, instead of relying on the command return output\. The module now compares SHA256 checksums of relevant configuration files \(<code>composer\.json</code>\, <code>auth\.json</code>\, or their global equivalents\) before and after running the command \([https\://github\.com/ansible\-collections/community\.general/pull/12084](https\://github\.com/ansible\-collections/community\.general/pull/12084)\)\.
* counter\_enabled callback \- fix missing output for looped tasks\, including tasks using <code>delegate\_to</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8187](https\://github\.com/ansible\-collections/community\.general/issues/8187)\, [https\://github\.com/ansible\-collections/community\.general/pull/12067](https\://github\.com/ansible\-collections/community\.general/pull/12067)\)\.
* dnf\_config\_manager \- fix incompatibility with DNF5\. The module was crashing on systems with DNF5 due to CLI changes since DNF4 \([https\://github\.com/ansible\-collections/community\.general/issues/9127](https\://github\.com/ansible\-collections/community\.general/issues/9127)\, [https\://github\.com/ansible\-collections/community\.general/pull/12206](https\://github\.com/ansible\-collections/community\.general/pull/12206)\)\.
* filesystem \- handle BusyBox <code>blkid</code> output to correctly detect existing filesystems on systems like Alpine Linux \([https\://github\.com/ansible\-collections/community\.general/issues/7283](https\://github\.com/ansible\-collections/community\.general/issues/7283)\, [https\://github\.com/ansible\-collections/community\.general/pull/12235](https\://github\.com/ansible\-collections/community\.general/pull/12235)\)\.
* filetree lookup plugin \- raise <code>AnsibleLookupError</code> when the <code>exclude</code> option contains an invalid regular expression instead of an uncaught <code>re\.error</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12140](https\://github\.com/ansible\-collections/community\.general/pull/12140)\)\.
* htpasswd \- fix <code>hash\_scheme</code> aliases and Apache\-compatible <code>bcrypt</code> hashes \([https\://github\.com/ansible\-collections/community\.general/issues/6135](https\://github\.com/ansible\-collections/community\.general/issues/6135)\, [https\://github\.com/ansible\-collections/community\.general/pull/12123](https\://github\.com/ansible\-collections/community\.general/pull/12123)\)\.
* incus connection plugin \- improve Windows PowerShell argv handling by stripping wrapper quotes from payload arguments for <code>\-enc</code>\, <code>\-encodedcommand</code>\, <code>\-command</code>\, <code>\-c</code>\, <code>\-file</code> and <code>\-f</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12161](https\://github\.com/ansible\-collections/community\.general/issues/12161)\, [https\://github\.com/ansible\-collections/community\.general/pull/12158](https\://github\.com/ansible\-collections/community\.general/pull/12158)\)\.
* incus connection plugin \- return <code>stdout</code>/<code>stderr</code> as bytes instead of strings to restore compatibility with ansible\-core 2\.21 module execution \([https\://github\.com/ansible\-collections/community\.general/issues/12161](https\://github\.com/ansible\-collections/community\.general/issues/12161)\, [https\://github\.com/ansible\-collections/community\.general/pull/12158](https\://github\.com/ansible\-collections/community\.general/pull/12158)\)\.
* java\_cert \- detect silent <code>keytool</code> failures by verifying the import outcome after the command exits with <code>rc\=0</code> \([https\://github\.com/ansible\-collections/community\.general/issues/6685](https\://github\.com/ansible\-collections/community\.general/issues/6685)\, [https\://github\.com/ansible\-collections/community\.general/pull/12238](https\://github\.com/ansible\-collections/community\.general/pull/12238)\)\.
* java\_cert \- fix <code>NullPointerException</code> when importing from a PKCS12 file with a password on Java 8 \([https\://github\.com/ansible\-collections/community\.general/issues/3023](https\://github\.com/ansible\-collections/community\.general/issues/3023)\, [https\://github\.com/ansible\-collections/community\.general/pull/12151](https\://github\.com/ansible\-collections/community\.general/pull/12151)\)\.
* launchd \- fix <code>restarted</code> and <code>reloaded</code> states always reporting <code>changed\=False</code> \([https\://github\.com/ansible\-collections/community\.general/issues/6199](https\://github\.com/ansible\-collections/community\.general/issues/6199)\, [https\://github\.com/ansible\-collections/community\.general/pull/12122](https\://github\.com/ansible\-collections/community\.general/pull/12122)\)\.
* lxc\_container \- fix <code>create\_script</code> to accept a single tuple argument\, resolving a <code>TypeError</code> that silently prevented <code>container\_command</code> from being executed \([https\://github\.com/ansible\-collections/community\.general/issues/11360](https\://github\.com/ansible\-collections/community\.general/issues/11360)\, [https\://github\.com/ansible\-collections/community\.general/pull/12106](https\://github\.com/ansible\-collections/community\.general/pull/12106)\)\.
* opkg \- correctly set executable search path \([https\://github\.com/ansible\-collections/community\.general/pull/12182](https\://github\.com/ansible\-collections/community\.general/pull/12182)\)\.
* pamd \- handle non\-PAM lines such as authselect template directives without crashing \([https\://github\.com/ansible\-collections/community\.general/issues/5850](https\://github\.com/ansible\-collections/community\.general/issues/5850)\, [https\://github\.com/ansible\-collections/community\.general/pull/12137](https\://github\.com/ansible\-collections/community\.general/pull/12137)\)\.
* parted \- ignore MBR partition type codes \(for example <code>type\=8e</code>\) reported as flags by some parted builds \(for example on SUSE\)\, which cannot be managed via the <code>set</code> command \([https\://github\.com/ansible\-collections/community\.general/issues/6292](https\://github\.com/ansible\-collections/community\.general/issues/6292)\, [https\://github\.com/ansible\-collections/community\.general/pull/12121](https\://github\.com/ansible\-collections/community\.general/pull/12121)\)\.
* portage \- fix <code>depclean\: true</code> crashing with <code>AnsibleModule\.fail\_json\(\) missing 1 required positional argument\: \'msg\'</code> instead of reporting the actual emerge failure \([https\://github\.com/ansible\-collections/community\.general/pull/12168](https\://github\.com/ansible\-collections/community\.general/pull/12168)\)\.
* redfish\_config \- fix <code>KeyError\: \'ret\'</code> when <code>SetManagerNic</code> cannot find a matching NIC \([https\://github\.com/ansible\-collections/community\.general/issues/5892](https\://github\.com/ansible\-collections/community\.general/issues/5892)\, [https\://github\.com/ansible\-collections/community\.general/pull/12124](https\://github\.com/ansible\-collections/community\.general/pull/12124)\)\.
* udm\_dns\_record \- normalize IPv6 addresses in <code>data</code> to expanded form to fix idempotency \([https\://github\.com/ansible\-collections/community\.general/issues/317](https\://github\.com/ansible\-collections/community\.general/issues/317)\, [https\://github\.com/ansible\-collections/community\.general/pull/12149](https\://github\.com/ansible\-collections/community\.general/pull/12149)\)\.
* unixy callback \- handle missing <code>ansible\_host</code> in delegated vars when a task is delegated to a host without it set\, such as <code>localhost</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12112](https\://github\.com/ansible\-collections/community\.general/issues/12112)\, [https\://github\.com/ansible\-collections/community\.general/pull/12113](https\://github\.com/ansible\-collections/community\.general/pull/12113)\)\.
* xenserver\_guest\_info \- use fallback chain for determining VDI format from <code>sm\_config</code> keys <code>image\-format</code>\, <code>vdi\_type</code>\, <code>type</code>\, defaulting to <code>raw</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12119](https\://github\.com/ansible\-collections/community\.general/pull/12119)\, [https\://github\.com/ansible\-collections/community\.general/pull/12215](https\://github\.com/ansible\-collections/community\.general/pull/12215)\)\.
* xml \- preserve DOCTYPE declaration when writing modified XML files \([https\://github\.com/ansible\-collections/community\.general/issues/2762](https\://github\.com/ansible\-collections/community\.general/issues/2762)\, [https\://github\.com/ansible\-collections/community\.general/pull/12148](https\://github\.com/ansible\-collections/community\.general/pull/12148)\)\.
* zypper\_repository \- fix <code>enabled</code>\, <code>autorefresh</code>\, and <code>gpgcheck</code> module parameters being overridden by values read from a <code>\.repo</code> file \([https\://github\.com/ansible\-collections/community\.general/issues/8783](https\://github\.com/ansible\-collections/community\.general/issues/8783)\, [https\://github\.com/ansible\-collections/community\.general/pull/12022](https\://github\.com/ansible\-collections/community\.general/pull/12022)\)\.

<a id="community-windows-3"></a>
#### community\.windows

* win\_psrepository\_copy \- handle profiles with no ProfileImagePath \([https\://github\.com/ansible\-collections/community\.windows/issues/604](https\://github\.com/ansible\-collections/community\.windows/issues/604)\)\.
* win\_pssession\_configuration \- Fix compatibility with Ansible 2\.21\.
* win\_pssession\_configuration \- Fix type errors for parameters passed in New\-PSSessionConfigurationFile
* win\_regmerge \- Ensure <code>reg\.exe</code> uses the absolute location <code>C\:\\Windows\\Systme32\\reg\.exe</code>\. This ensures that misconfigured hosts won\'t use a different executable\.
* win\_unzip \- Use <code>\-LiteralPath</code> when calling PSCX <code>Expand\-Archive</code> so paths containing PowerShell wildcard characters \(e\.g\. <code>\[</code>\, <code>\]</code>\) are not glob\-expanded and silently resolved to an empty array\.
* win\_xml \- allow users to preserve whitespace while updating XML file \([https\://github\.com/ansible\-collections/community\.windows/issues/210](https\://github\.com/ansible\-collections/community\.windows/issues/210)\)\.
* win\_xml \- handle attribute removal correctly \([https\://github\.com/ansible\-collections/community\.windows/issues/631](https\://github\.com/ansible\-collections/community\.windows/issues/631)\)\.

<a id="containers-podman-1"></a>
#### containers\.podman

* podman\_image \- Fix build ignoring arch option

<a id="microsoft-ad-3"></a>
#### microsoft\.ad

* Fix bug when creating a new AD object with an attribute set to an empty value\. For example using <code>allowed\_to\_retrieve\_password\: \{set\: \[\]\}</code> on <code>microsoft\.ad\.service\_account</code> will be treated like the value was not specified at all \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/229](https\://github\.com/ansible\-collections/microsoft\.ad/issues/229)
* Removed use of deprecated <code>\_encode\_script</code> function used by the internal reboot functionality of the AD plugins\.
* domain \- Fix PowerShell 7 compatibility
* domain\_child \- Fix PowerShell 7 compatibility
* domain\_controller \- Fix PowerShell 7 compatibility
* object\_info \- Fix PowerShell 7 compatibility when specified property does not match the same case as the property on the found AD object

<a id="purestorage-flashblade-5"></a>
#### purestorage\.flashblade

* common \- Add remove\_duplicates\(\) utility function for list deduplication
* common \- Consolidate duplicate \_findstr implementations to prevent UnboundLocalError
* common \- Remove deprecated time conversion functions \(replaced by time\_utils\)
* purefb \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#496\)
* purefb\_ad \- Correct encryption type from <code>arcfour\-hma</code> to <code>arcfour\-hmac</code>
* purefb\_ad \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_admin \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_alert \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_apiclient \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_banner \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bladename \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket \- Fixed issue creating bucket with no versioning incorrectly failing
* purefb\_bucket \- Fixed module\.warn\(\) calls to be compatible with Ansible 2\.15\+ by removing msg\= parameter
* purefb\_bucket\_access \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket\_replica \- Added safety checks for empty lists before accessing \[0\] index
* purefb\_bucket\_replica \- Added validation for missing target parameter when creating new replica links
* purefb\_bucket\_replica \- Check actual list length instead of unreliable total\_item\_count
* purefb\_bucket\_replica \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket\_replica \- Fixed IndexError \'list index out of range\' in get\_connected\(\) function
* purefb\_bucket\_replica \- Fixed iteration anti\-pattern using range\(len\(\)\) that could cause IndexError
* purefb\_certgrp \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_certs \- Corrects typos in the parameter name\.
* purefb\_certs \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_certs \- Fixes certificate\_type name from array to appliance
* purefb\_certs \- Fixes issue where intermediate\_certificate was not be applied to certificates\.
* purefb\_certs \- Removes immutable field certificate\_type for the patch operation\.
* purefb\_connect \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_connect \- Use unified time conversion from time\_utils module
* purefb\_dns \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_dns \- Use remove\_duplicates\(\) from common instead of local remove\(\) function
* purefb\_ds \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_dsrole \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_export \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_fleet \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_fs \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_fs \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_fs \- Fixed failure to apply policies to existing filesystems due to incorrect API check and non\-existent patch method
* purefb\_fs \- Fixed issue where NFS export policies were applied even when both nfsv3 and nfsv4 were disabled
* purefb\_fs \- Fixed issue where SMB policies were applied even when smb parameter was set to false
* purefb\_fs\_replica \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_groupquota \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_groupquota \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_hardware \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_info \- Fixed bucket AttributeError
* purefb\_info \- Use unified time conversion from time\_utils module
* purefb\_keytabs \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_kmip \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_lag \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_lifecycle \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_lifecycle \- Use unified time conversion from time\_utils module with proper None handling
* purefb\_messages \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_network \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_ntp \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_ntp \- Use remove\_duplicates\(\) from common instead of local remove\(\) function
* purefb\_phonehome \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_pingtrace \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_policy \- Fix UnboundLocalError when policy string is not found
* purefb\_policy \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_policy \- Fixed AttributeError with empty policy rules
* purefb\_policy \- Use unified time conversion from time\_utils module
* purefb\_proxy \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_ra \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_remote\_cred \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_s3acc \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_s3user \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_saml \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_saml \- Fixed typo in model name
* purefb\_server \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_smtp \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_snap \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_snap \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_snmp\_agent \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_snmp\_mgr \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_subnet \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_syslog \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_target \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_tz \- Fix UnboundLocalError when timezone string is not found
* purefb\_tz \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_user \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_user \- Fixed NameError by replacing deprecated AdminRole with ReferenceWritable when changing user roles
* purefb\_user \- Use unified time conversion from time\_utils module
* purefb\_userpolicy \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_userquota \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_userquota \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* time\_utils \- Add unified time conversion module with proper error handling and input validation

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* inventory plugins \- Fix a bug where the customValue property was always gathered\, even when not requested
* module\_utils/vmware\_rest\_client \- correct python syntax and proxy url syntax\.
* tag\_associations \- Fix error when using the object\_name parameter to lookup an object Fixes \- [https\://github\.com/ansible\-collections/vmware\.vmware/issues/315](https\://github\.com/ansible\-collections/vmware\.vmware/issues/315)
* vm \- Fix incorrect parameter name in error when neither datastore nor datastore\_cluster is provided for VM creation\. Follow\-up to [https\://github\.com/ansible\-collections/vmware\.vmware/issues/334](https\://github\.com/ansible\-collections/vmware\.vmware/issues/334)\.
* vm \- Fix issue where datastore was always a required parameter for creating new vms\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/334](https\://github\.com/ansible\-collections/vmware\.vmware/issues/334)
* vm \- correct O\(delete\_from\_inventory\) documentation for C\(state\=absent\) to match module behavior\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/322](https\://github\.com/ansible\-collections/vmware\.vmware/issues/322)
* vm\_snapshot\_revert \- search the snapshot tree fully to find a matching snapshot Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/330](https\://github\.com/ansible\-collections/vmware\.vmware/issues/330)

<a id="vmware-vmware-rest-3"></a>
#### vmware\.vmware\_rest

* module\_utils \- Avoid importing cloud\.common turbo exceptions unless turbo mode is explicitly enabled\, preventing a cloud\.common Ansible 2\.20 support warning in module runs when turbo is off \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/637](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/637)\)\.

<a id="new-plugins-1"></a>
### New Plugins

<a id="filter"></a>
#### Filter

* community\.general\.from\_toml \- Convert TOML string into dictionary\.

<a id="new-modules-1"></a>
### New Modules

<a id="ansible-windows-4"></a>
#### ansible\.windows

* ansible\.windows\.win\_capability \- Manage Windows capabilities
* ansible\.windows\.win\_capability\_info \- Get information about Windows capabilities

<a id="community-clickhouse-7"></a>
#### community\.clickhouse

* community\.clickhouse\.clickhouse\_named\_collection \- Creates\, removes or modify a ClickHouse named collection using the clickhouse\-driver Client interface
* community\.clickhouse\.clickhouse\_row\_policy \- Creates\, removes or modify a ClickHouse row policy using the clickhouse\-driver Client interface
* community\.clickhouse\.clickhouse\_script \- Run SQL queries from a file

<a id="community-general-5"></a>
#### community\.general

* community\.general\.gitlab\_project\_approvals \- Manage project\-level merge request approvals settings on GitLab Server\.
* community\.general\.golang\_package \- Manage Go packages with <code>go install</code>\.
* community\.general\.google\_chat \- Send Google Chat notifications\.
* community\.general\.keycloak\_clientscope\_rolemappings \- Allows administration of Keycloak clientscope scope mappings to restrict the usage of certain roles to specific clientscopes\.
* community\.general\.keycloak\_realm\_users\_info \- Retrieve users from a Keycloak realm using the Keycloak API\.
* community\.general\.kopia\_repository \- Manage Kopia repository\.
* community\.general\.kopia\_repository\_info \- Gather information about a Kopia repository\.

<a id="microsoft-ad-4"></a>
#### microsoft\.ad

* microsoft\.ad\.cs\_authority \- Manage CA CRL Distribution Points and Authority Information Access
* microsoft\.ad\.cs\_template \- Manage AD Certificate Services certificate templates
* microsoft\.ad\.domain\_trust \- Manage Active Directory domain trusts
* microsoft\.ad\.fs\_claim\_rule \- Manage AD FS claim rules on a Relying Party Trust
* microsoft\.ad\.fs\_trust \- Manage AD FS Relying Party Trusts
* microsoft\.ad\.kds\_root\_key \- Manages a KDS root key in a domain
* microsoft\.ad\.kds\_root\_key\_info \- Gather information about one or more KDS root keys in a domain\.
* microsoft\.ad\.site \- Manage Active Directory replication sites
* microsoft\.ad\.site\_link \- Manage Active Directory replication site links
* microsoft\.ad\.site\_subnet \- Manage Active Directory replication subnets

<a id="purestorage-flashblade-6"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_export \- Manage filesystem exports on Everpure FlashBlade\`
* purestorage\.flashblade\.purefb\_realm \- Manage realms on Everpure FlashBlades

<a id="unchanged-collections-1"></a>
### Unchanged Collections

* amazon\.aws \(still version 11\.3\.0\)
* ansible\.mysql \(still version 5\.0\.1\)
* ansible\.posix \(still version 2\.2\.0\)
* check\_point\.mgmt \(still version 6\.9\.0\)
* chocolatey\.chocolatey \(still version 1\.6\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.nxos \(still version 11\.2\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* cloudscale\_ch\.cloud \(still version 2\.5\.3\)
* community\.aws \(still version 11\.0\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.2\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.libvirt \(still version 2\.2\.0\)
* community\.mongodb \(still version 1\.7\.12\)
* community\.mysql \(still version 5\.0\.2\)
* community\.okd \(still version 5\.0\.0\)
* community\.postgresql \(still version 4\.2\.0\)
* community\.proxmox \(still version 2\.0\.0\)
* community\.proxysql \(still version 1\.8\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* community\.sap\_libs \(still version 1\.7\.0\)
* community\.vmware \(still version 6\.2\.0\)
* community\.zabbix \(still version 4\.2\.0\)
* cyberark\.pas \(still version 1\.0\.39\)
* dellemc\.enterprise\_sonic \(still version 4\.1\.0\)
* dellemc\.openmanage \(still version 10\.0\.2\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* fortinet\.fortimanager \(still version 2\.14\.0\)
* fortinet\.fortios \(still version 2\.5\.1\)
* google\.cloud \(still version 1\.13\.0\)
* grafana\.grafana \(still version 6\.1\.0\)
* ibm\.storage\_virtualize \(still version 3\.3\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infoblox\.nios\_modules \(still version 1\.9\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* kaytus\.ksmanage \(still version 4\.0\.0\)
* kubernetes\.core \(still version 6\.4\.0\)
* lowlydba\.sqlserver \(still version 2\.8\.1\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* netapp\.ontap \(still version 23\.5\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netapp\_eseries\.santricity \(still version 2\.0\.1\)
* netbox\.netbox \(still version 3\.23\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* purestorage\.flasharray \(still version 1\.42\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* splunk\.es \(still version 6\.0\.0\)
* telekom\_mms\.icinga\_director \(still version 2\.5\.1\)
* theforeman\.foreman \(still version 5\.11\.0\)
* vultr\.cloud \(still version 1\.14\.0\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)

<a id="v14-0-0"></a>
## v14\.0\.0

- <a href="#release-summary-2">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core-6">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes-2">Major Changes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#amazon-aws-2">amazon\.aws</a>
    - <a href="#chocolatey-chocolatey">chocolatey\.chocolatey</a>
    - <a href="#community-aws-2">community\.aws</a>
    - <a href="#community-proxmox">community\.proxmox</a>
    - <a href="#community-routeros-1">community\.routeros</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#containers-podman-2">containers\.podman</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#grafana-grafana">grafana\.grafana</a>
    - <a href="#kaytus-ksmanage">kaytus\.ksmanage</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#splunk-es-4">splunk\.es</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
- <a href="#minor-changes-2">Minor Changes</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
    - <a href="#amazon-aws-3">amazon\.aws</a>
    - <a href="#ansible-netcommon-2">ansible\.netcommon</a>
    - <a href="#ansible-posix-2">ansible\.posix</a>
    - <a href="#ansible-windows-5">ansible\.windows</a>
    - <a href="#arista-eos-1">arista\.eos</a>
    - <a href="#cisco-aci">cisco\.aci</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-meraki-2">cisco\.meraki</a>
    - <a href="#cisco-mso">cisco\.mso</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-aws-3">community\.aws</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-6">community\.general</a>
    - <a href="#community-libvirt-2">community\.libvirt</a>
    - <a href="#community-mysql">community\.mysql</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#community-proxmox-1">community\.proxmox</a>
    - <a href="#community-proxysql">community\.proxysql</a>
    - <a href="#community-routeros-2">community\.routeros</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#community-sops-1">community\.sops</a>
    - <a href="#community-windows-4">community\.windows</a>
    - <a href="#community-zabbix">community\.zabbix</a>
    - <a href="#containers-podman-3">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-1">hitachivantara\.vspone\_block</a>
    - <a href="#hitachivantara-vspone-object-1">hitachivantara\.vspone\_object</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#kaytus-ksmanage-1">kaytus\.ksmanage</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-5">microsoft\.ad</a>
    - <a href="#microsoft-iis-2">microsoft\.iis</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#netapp-storagegrid">netapp\.storagegrid</a>
    - <a href="#netbox-netbox">netbox\.netbox</a>
    - <a href="#ovirt-ovirt">ovirt\.ovirt</a>
    - <a href="#purestorage-flasharray-3">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-7">purestorage\.flashblade</a>
    - <a href="#splunk-es-5">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware-3">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-4">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud-1">vultr\.cloud</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-9">Ansible\-core</a>
    - <a href="#community-aws-4">community\.aws</a>
    - <a href="#community-dns-3">community\.dns</a>
    - <a href="#community-general-7">community\.general</a>
    - <a href="#community-mysql-1">community\.mysql</a>
    - <a href="#community-proxmox-2">community\.proxmox</a>
    - <a href="#dellemc-enterprise-sonic-1">dellemc\.enterprise\_sonic</a>
    - <a href="#hitachivantara-vspone-block-2">hitachivantara\.vspone\_block</a>
    - <a href="#netbox-netbox-1">netbox\.netbox</a>
    - <a href="#splunk-es-6">splunk\.es</a>
- <a href="#deprecated-features-2">Deprecated Features</a>
    - <a href="#ansible-core-10">Ansible\-core</a>
    - <a href="#amazon-aws-4">amazon\.aws</a>
    - <a href="#ansible-netcommon-3">ansible\.netcommon</a>
    - <a href="#arista-eos-2">arista\.eos</a>
    - <a href="#cisco-ios-2">cisco\.ios</a>
    - <a href="#cisco-iosxr-2">cisco\.iosxr</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-aws-5">community\.aws</a>
    - <a href="#community-general-8">community\.general</a>
    - <a href="#community-mysql-2">community\.mysql</a>
    - <a href="#community-proxmox-3">community\.proxmox</a>
    - <a href="#community-routeros-3">community\.routeros</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-3">hitachivantara\.vspone\_block</a>
    - <a href="#kubernetes-core-4">kubernetes\.core</a>
    - <a href="#vmware-vmware-rest-5">vmware\.vmware\_rest</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-11">Ansible\-core</a>
    - <a href="#community-dns-4">community\.dns</a>
    - <a href="#community-general-9">community\.general</a>
    - <a href="#community-mysql-3">community\.mysql</a>
    - <a href="#hitachivantara-vspone-block-4">hitachivantara\.vspone\_block</a>
    - <a href="#splunk-es-7">splunk\.es</a>
- <a href="#security-fixes-2">Security Fixes</a>
    - <a href="#amazon-aws-5">amazon\.aws</a>
    - <a href="#ansible-windows-6">ansible\.windows</a>
    - <a href="#kubernetes-core-5">kubernetes\.core</a>
- <a href="#bugfixes-2">Bugfixes</a>
    - <a href="#ansible-core-12">Ansible\-core</a>
    - <a href="#amazon-aws-6">amazon\.aws</a>
    - <a href="#ansible-netcommon-4">ansible\.netcommon</a>
    - <a href="#ansible-posix-3">ansible\.posix</a>
    - <a href="#ansible-utils-1">ansible\.utils</a>
    - <a href="#ansible-windows-7">ansible\.windows</a>
    - <a href="#arista-eos-3">arista\.eos</a>
    - <a href="#cisco-aci-1">cisco\.aci</a>
    - <a href="#cisco-ios-3">cisco\.ios</a>
    - <a href="#cisco-iosxr-3">cisco\.iosxr</a>
    - <a href="#cisco-meraki-3">cisco\.meraki</a>
    - <a href="#cisco-mso-1">cisco\.mso</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#community-aws-6">community\.aws</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-dns-5">community\.dns</a>
    - <a href="#community-docker-2">community\.docker</a>
    - <a href="#community-general-10">community\.general</a>
    - <a href="#community-hrobot">community\.hrobot</a>
    - <a href="#community-libvirt-3">community\.libvirt</a>
    - <a href="#community-mysql-4">community\.mysql</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#community-proxmox-4">community\.proxmox</a>
    - <a href="#community-routeros-4">community\.routeros</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#community-windows-5">community\.windows</a>
    - <a href="#community-zabbix-1">community\.zabbix</a>
    - <a href="#containers-podman-4">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-2">dellemc\.enterprise\_sonic</a>
    - <a href="#dellemc-openmanage-1">dellemc\.openmanage</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#google-cloud-1">google\.cloud</a>
    - <a href="#hetzner-hcloud-4">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block-5">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#inspur-ispim">inspur\.ispim</a>
    - <a href="#kaytus-ksmanage-2">kaytus\.ksmanage</a>
    - <a href="#kubernetes-core-6">kubernetes\.core</a>
    - <a href="#microsoft-ad-6">microsoft\.ad</a>
    - <a href="#microsoft-iis-3">microsoft\.iis</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-1">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-2">netbox\.netbox</a>
    - <a href="#ovirt-ovirt-1">ovirt\.ovirt</a>
    - <a href="#purestorage-flasharray-4">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-8">purestorage\.flashblade</a>
    - <a href="#splunk-es-8">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-4">vmware\.vmware</a>
    - <a href="#vultr-cloud-2">vultr\.cloud</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#community-docker-3">community\.docker</a>
    - <a href="#community-routeros-5">community\.routeros</a>
    - <a href="#dellemc-openmanage-2">dellemc\.openmanage</a>
- <a href="#new-plugins-2">New Plugins</a>
    - <a href="#callback">Callback</a>
    - <a href="#connection">Connection</a>
    - <a href="#filter-1">Filter</a>
- <a href="#new-modules-2">New Modules</a>
    - <a href="#amazon-aws-7">amazon\.aws</a>
    - <a href="#ansible-windows-8">ansible\.windows</a>
    - <a href="#cisco-aci-2">cisco\.aci</a>
    - <a href="#cisco-ios-4">cisco\.ios</a>
    - <a href="#cisco-mso-2">cisco\.mso</a>
    - <a href="#community-general-11">community\.general</a>
    - <a href="#community-libvirt-4">community\.libvirt</a>
    - <a href="#community-proxmox-5">community\.proxmox</a>
    - <a href="#community-proxysql-1">community\.proxysql</a>
    - <a href="#containers-podman-5">containers\.podman</a>
    - <a href="#dellemc-enterprise-sonic-3">dellemc\.enterprise\_sonic</a>
    - <a href="#fortinet-fortimanager-2">fortinet\.fortimanager</a>
    - <a href="#hitachivantara-vspone-block-6">hitachivantara\.vspone\_block</a>
    - <a href="#ibm-storage-virtualize-2">ibm\.storage\_virtualize</a>
    - <a href="#kaytus-ksmanage-3">kaytus\.ksmanage</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
    - <a href="#netapp-storagegrid-2">netapp\.storagegrid</a>
    - <a href="#netbox-netbox-3">netbox\.netbox</a>
    - <a href="#splunk-es-9">splunk\.es</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
    - <a href="#vultr-cloud-3">vultr\.cloud</a>
- <a href="#unchanged-collections-2">Unchanged Collections</a>

<a id="release-summary-2"></a>
### Release Summary

Release Date\: 2026\-06\-02

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* awx\.awx \(previously included version\: 24\.6\.1\)
* cisco\.dnac \(previously included version\: 6\.41\.0\)
* junipernetworks\.junos \(previously included version\: 11\.0\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections"></a>
### Added Collections

* ansible\.mysql \(version 5\.0\.1\)
* community\.clickhouse \(version 2\.1\.0\)
* graphiant\.naas \(version 26\.4\.0\)
* pcg\.alpaca\_operator \(version 2\.2\.0\)

<a id="ansible-core-6"></a>
### Ansible\-core

Ansible 14\.0\.0 contains ansible\-core version 2\.21\.0\.
This is a newer version than version 2\.20\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                   | Ansible 13.0.0 | Ansible 14.0.0 | Notes                                                                                                                                                                                                        |
| ---------------------------- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                   | 10.1.2         | 11.3.0         |                                                                                                                                                                                                              |
| ansible.mysql                |                | 5.0.1          | The collection was added to Ansible                                                                                                                                                                          |
| ansible.netcommon            | 8.1.0          | 8.5.2          |                                                                                                                                                                                                              |
| ansible.posix                | 2.1.0          | 2.2.0          |                                                                                                                                                                                                              |
| ansible.utils                | 6.0.0          | 6.0.2          |                                                                                                                                                                                                              |
| ansible.windows              | 3.2.0          | 3.5.0          |                                                                                                                                                                                                              |
| arista.eos                   | 12.0.0         | 12.1.1         |                                                                                                                                                                                                              |
| azure.azcollection           | 3.10.1         | 3.18.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt             | 6.6.0          | 6.9.0          | The collection did not have a changelog in this version.                                                                                                                                                     |
| chocolatey.chocolatey        | 1.5.3          | 1.6.0          |                                                                                                                                                                                                              |
| cisco.aci                    | 2.12.0         | 2.13.0         |                                                                                                                                                                                                              |
| cisco.intersight             | 2.7.0          | 2.18.0         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.ios                    | 11.1.1         | 11.4.1         |                                                                                                                                                                                                              |
| cisco.iosxr                  | 12.1.0         | 12.3.1         |                                                                                                                                                                                                              |
| cisco.meraki                 | 2.21.8         | 2.23.2         |                                                                                                                                                                                                              |
| cisco.mso                    | 2.11.0         | 2.13.0         |                                                                                                                                                                                                              |
| cisco.nxos                   | 11.0.0         | 11.2.0         |                                                                                                                                                                                                              |
| cloudscale_ch.cloud          | 2.5.2          | 2.5.3          |                                                                                                                                                                                                              |
| community.aws                | 10.0.0         | 11.0.0         |                                                                                                                                                                                                              |
| community.clickhouse         |                | 2.1.0          | The collection was added to Ansible                                                                                                                                                                          |
| community.crypto             | 3.0.5          | 3.2.1          |                                                                                                                                                                                                              |
| community.dns                | 3.4.0          | 4.0.0          |                                                                                                                                                                                                              |
| community.docker             | 5.0.1          | 5.2.0          |                                                                                                                                                                                                              |
| community.general            | 12.0.1         | 13.0.1         |                                                                                                                                                                                                              |
| community.hrobot             | 2.7.0          | 2.7.2          |                                                                                                                                                                                                              |
| community.libvirt            | 2.0.0          | 2.2.0          |                                                                                                                                                                                                              |
| community.mongodb            | 1.7.10         | 1.7.12         | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.mysql              | 4.0.1          | 5.0.2          |                                                                                                                                                                                                              |
| community.postgresql         | 4.1.0          | 4.2.0          |                                                                                                                                                                                                              |
| community.proxmox            | 1.4.0          | 2.0.0          |                                                                                                                                                                                                              |
| community.proxysql           | 1.7.0          | 1.8.0          |                                                                                                                                                                                                              |
| community.routeros           | 3.13.0         | 3.20.0         |                                                                                                                                                                                                              |
| community.sap_libs           | 1.5.0          | 1.7.0          |                                                                                                                                                                                                              |
| community.sops               | 2.2.7          | 2.3.0          |                                                                                                                                                                                                              |
| community.vmware             | 6.1.0          | 6.2.0          |                                                                                                                                                                                                              |
| community.windows            | 3.0.1          | 3.1.0          |                                                                                                                                                                                                              |
| community.zabbix             | 4.1.1          | 4.2.0          |                                                                                                                                                                                                              |
| containers.podman            | 1.18.0         | 1.20.1         |                                                                                                                                                                                                              |
| cyberark.conjur              | 1.3.8          | 1.3.9          | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| cyberark.pas                 | 1.0.36         | 1.0.39         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| dellemc.enterprise_sonic     | 3.2.0          | 4.1.0          |                                                                                                                                                                                                              |
| dellemc.openmanage           | 10.0.1         | 10.0.2         |                                                                                                                                                                                                              |
| f5networks.f5_modules        | 1.39.0         | 1.41.0         | The collection did not have a changelog in this version.                                                                                                                                                     |
| fortinet.fortimanager        | 2.11.0         | 2.14.0         |                                                                                                                                                                                                              |
| fortinet.fortios             | 2.4.2          | 2.5.1          |                                                                                                                                                                                                              |
| google.cloud                 | 1.9.0          | 1.13.0         |                                                                                                                                                                                                              |
| grafana.grafana              | 6.0.6          | 6.1.0          |                                                                                                                                                                                                              |
| graphiant.naas               |                | 26.4.0         | The collection was added to Ansible                                                                                                                                                                          |
| hetzner.hcloud               | 6.0.0          | 6.9.0          |                                                                                                                                                                                                              |
| hitachivantara.vspone_block  | 4.4.0          | 4.8.1          |                                                                                                                                                                                                              |
| hitachivantara.vspone_object | 1.0.0          | 1.1.1          |                                                                                                                                                                                                              |
| ibm.storage_virtualize       | 3.1.0          | 3.3.0          |                                                                                                                                                                                                              |
| infoblox.nios_modules        | 1.8.0          | 1.9.0          |                                                                                                                                                                                                              |
| inspur.ispim                 | 2.2.3          | 2.2.4          |                                                                                                                                                                                                              |
| kaytus.ksmanage              | 2.0.0          | 4.0.0          |                                                                                                                                                                                                              |
| kubernetes.core              | 6.2.0          | 6.4.0          |                                                                                                                                                                                                              |
| kubevirt.core                | 2.2.3          | 2.2.4          | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| lowlydba.sqlserver           | 2.7.0          | 2.8.1          |                                                                                                                                                                                                              |
| microsoft.ad                 | 1.9.2          | 1.10.0         |                                                                                                                                                                                                              |
| microsoft.iis                | 1.0.3          | 1.1.0          |                                                                                                                                                                                                              |
| netapp.ontap                 | 23.2.0         | 23.5.0         |                                                                                                                                                                                                              |
| netapp.storagegrid           | 21.15.0        | 21.16.0        |                                                                                                                                                                                                              |
| netapp_eseries.santricity    | 1.4.1          | 2.0.1          | The collection did not have a changelog in this version.                                                                                                                                                     |
| netbox.netbox                | 3.21.0         | 3.23.0         |                                                                                                                                                                                                              |
| ovirt.ovirt                  | 3.2.1          | 3.2.2          |                                                                                                                                                                                                              |
| pcg.alpaca_operator          |                | 2.2.0          | The collection was added to Ansible                                                                                                                                                                          |
| purestorage.flasharray       | 1.39.0         | 1.42.0         |                                                                                                                                                                                                              |
| purestorage.flashblade       | 1.22.0         | 1.24.0         |                                                                                                                                                                                                              |
| splunk.es                    | 4.0.0          | 6.0.0          |                                                                                                                                                                                                              |
| telekom_mms.icinga_director  | 2.4.0          | 2.5.1          |                                                                                                                                                                                                              |
| theforeman.foreman           | 5.7.0          | 5.11.0         |                                                                                                                                                                                                              |
| vmware.vmware                | 2.4.0          | 2.8.0          |                                                                                                                                                                                                              |
| vmware.vmware_rest           | 4.9.0          | 4.10.0         |                                                                                                                                                                                                              |
| vultr.cloud                  | 1.13.0         | 1.14.0         |                                                                                                                                                                                                              |
| wti.remote                   | 1.0.10         | 1.0.11         | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |

<a id="major-changes-2"></a>
### Major Changes

<a id="ansible-core-7"></a>
#### Ansible\-core

* <code>ansible\-galaxy install</code> and <code>ansible\-galaxy collection install\|download</code> \- collections that declare a <code>requires\_ansible</code> version that is not compatible with the running ansible\-core version are now excluded from installation and download by default\. In previous versions\, ansible\-galaxy would install such collections even if doing so resulted in an error at load time\. To restore the previous behavior\, set <code>COLLECTIONS\_ON\_ANSIBLE\_VERSION\_MISMATCH</code> to <code>ignore</code> in your configuration\. \([https\://github\.com/ansible/ansible/issues/78539](https\://github\.com/ansible/ansible/issues/78539)\)
* action plugins \- Actions can directly register variables at several precedence layers using the <code>register\_host\_variables</code> method on <code>ActionBase</code>\. Previously\, variable registration could only be simulated by user action plugins by returning <code>ansible\_facts</code> with insecure fact injection\.
* register projections \- The <code>register</code> task keyword allows mapping multiple variable names to Jinja expressions to transform task results and other variables\. The mapping form can replace many usages of <code>set\_fact</code> and allows order\-independent chained access to other variable expressions within the same task\.
* task implicit object \- A new <code>\_task</code> implicit object is available for use in <code>register</code> and task conditional expressions \(e\.g\.\, <code>failed\_when</code>\)\. The result of the current task can be accessed via the <code>\_task\.result</code> property\, without the use of <code>register</code>\. Under a loop\, <code>\_task\.result</code> is the most recently completed result and <code>\_task\.loop\_result</code> provides access to accumulated loop results\. The <code>\_task\.polymorphic\_result</code> property provides compatibility with classic name\-only <code>register</code> in loops\. The value is the result of the most recent loop iteration\, then becomes the final list loop result once the loop is complete\.

<a id="amazon-aws-2"></a>
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

<a id="community-aws-2"></a>
#### community\.aws

* community\.aws collection \- <code>awscli</code> version has been bumped to 1\.34\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2375](https\://github\.com/ansible\-collections/community\.aws/pull/2375)\)\.
* community\.aws collection \- <code>botocore</code> and <code>boto3</code> versions have been bumped to 1\.35\.0 \([https\://github\.com/ansible\-collections/community\.aws/pull/2375](https\://github\.com/ansible\-collections/community\.aws/pull/2375)\)\.

<a id="community-proxmox"></a>
#### community\.proxmox

* proxmox \- Add ca\_path option to specify a ca\-certificate for tls validation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/256](https\://github\.com/ansible\-collections/community\.proxmox/pull/256)\)\.

<a id="community-routeros-1"></a>
#### community\.routeros

* api\_info\, api\_modify \- multiple parameters can no longer be disabled for the\`\`tool netwatch\`\` path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- parameter <code>name\-format</code> can no longer be disabled for the <code>interface wifi provisioning</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- parameter <code>script</code> can no longer be disabled for the <code>ip dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* Bump required <code>vmware\.vmware</code> collection version to 2\.5\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2503](https\://github\.com/ansible\-collections/community\.vmware/pull/2503)\)\.

<a id="containers-podman-2"></a>
#### containers\.podman

* Add podman Quadlet modules
* Rewrite podman and buildah connections

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Added a generic <em class="title-reference">headers</em> parameter to <em class="title-reference">fortios\_json\_generic</em> to support admin\-password confirmation headers and future custom request headers\.
* Supported new versions 7\.6\.5 and 7\.6\.6\.
* Updated FAQ to illustrate the use of <em class="title-reference">headers</em> in <em class="title-reference">fortios\_json\_generic</em> module\.
* Updated deprecated import of to\_text from ansible\.module\_utils\.\_text to the supported implementation\.
* Updated the Q\&A for using the default\_group feature in modules\.

<a id="grafana-grafana"></a>
#### grafana\.grafana

* Run molecule only when required by \@voidquark in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/441](https\://github\.com/grafana/grafana\-ansible\-collection/pull/441)
* migrate stack create/update/delete to stacks\-api by \@KucicM in [https\://github\.com/grafana/grafana\-ansible\-collection/pull/494](https\://github\.com/grafana/grafana\-ansible\-collection/pull/494)

<a id="kaytus-ksmanage"></a>
#### kaytus\.ksmanage

* Add new modules upload\_ssl\,ssl\_info\,generate\_ssl\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/34](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/34)\)\.
* Change the name of the used SDK\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/37](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/37)\)\.
* Modify the URL address path when the owner is changed\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/38](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/38)\)\.
* The edit\_m6\_log\_setting\.py module has added the \'server\_status\' attribute\; The edit\_network\_bond\.py module modifies the attribute descriptions\; The edit\_snmp\.py and edit\_snmp\_trap\.py module modifies the allowable value ranges for the auth\_protocol and priv\_protocol attributes\. \([https\://github\.com/ieisystem/kaytus\.ksmanage/pull/33](https\://github\.com/ieisystem/kaytus\.ksmanage/pull/33)\)\.

<a id="netapp-ontap"></a>
#### netapp\.ontap

* Updated ONTAP personality check functionality\.
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
* na\_ontap\_debug \- AWS Lambda support added to the module\.
* na\_ontap\_dns \- AWS Lambda support added to the module\.
* na\_ontap\_domain\_tunnel \- AWS Lambda support added to the module\.
* na\_ontap\_efficiency\_policy \- AWS Lambda support added to the module\.
* na\_ontap\_export\_policy \- AWS Lambda support added to the module\.
* na\_ontap\_export\_policy\_rule \- AWS Lambda support added to the module\.
* na\_ontap\_flexcache \- AWS Lambda support added to the module\.
* na\_ontap\_igroup \- AWS Lambda support added to the module\.
* na\_ontap\_igroup\_initiator \- AWS Lambda support added to the module\.
* na\_ontap\_interface \- AWS Lambda support added to the module\.
* na\_ontap\_iscsi \- AWS Lambda support added to the module\.
* na\_ontap\_iscsi\_security \- AWS Lambda support added to the module\.
* na\_ontap\_job\_schedule \- AWS Lambda support added to the module\.
* na\_ontap\_ldap\_client \- AWS Lambda support added to the module\.
* na\_ontap\_local\_hosts \- AWS Lambda support added to the module\.
* na\_ontap\_lun \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_copy \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_map \- AWS Lambda support added to the module\.
* na\_ontap\_lun\_map\_reporting\_nodes \- AWS Lambda support added to the module\.
* na\_ontap\_name\_mappings \- AWS Lambda support added to the module\.
* na\_ontap\_name\_service\_switch \- AWS Lambda support added to the module\.
* na\_ontap\_nfs \- AWS Lambda support added to the module\.
* na\_ontap\_qos\_policy\_group \- AWS Lambda support added to the module\.
* na\_ontap\_qtree \- AWS Lambda support added to the module\.
* na\_ontap\_quotas \- AWS Lambda support added to the module\.
* na\_ontap\_rest\_info \- AWS Lambda support added to the module\.
* na\_ontap\_restit \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_buckets \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_groups \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_policies \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_services \- AWS Lambda support added to the module\.
* na\_ontap\_s3\_users \- AWS Lambda support added to the module\.
* na\_ontap\_snapmirror \- AWS Lambda support added to the module\.
* na\_ontap\_snapmirror\_policy \- AWS Lambda support added to the module\.
* na\_ontap\_snapshot \- AWS Lambda support added to the module\.
* na\_ontap\_snapshot\_policy \- AWS Lambda support added to the module\.
* na\_ontap\_svm \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_autosize \- AWS Lambda support added to the module\.
* na\_ontap\_volume\_clone \- AWS Lambda support added to the module\.
* na\_ontap\_vserver\_peer \- AWS Lambda support added to the module\.
* na\_ontap\_vserver\_peer\_permissions \- AWS Lambda support added to the module\.
* na\_ontap\_wait\_for\_condition \- AWS Lambda support added to the module\.

<a id="splunk-es-4"></a>
#### splunk\.es

* Bumped the minimum supported Ansible version to <code>\>\=2\.17\.0</code> \(Ansible 2\.15/2\.16 are EoL\)\.
* Remove dependency on the <code>ansible\.netcommon</code> collection\. Utility functions \(<code>remove\_empties</code>\, <code>dict\_diff</code>\, <code>dict\_merge</code>\) are now bundled locally\, and the httpapi plugin inherits directly from ansible\-core\'s <code>HttpApiBase</code>\.

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* Replace <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/268](https\://github\.com/ansible\-collections/vmware\.vmware/issues/268)\)\.
* Replace <code>ansible\.module\_utils\.common\.\_collections\_compat</code> \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/271](https\://github\.com/ansible\-collections/vmware\.vmware/issues/271)\)\.

<a id="minor-changes-2"></a>
### Minor Changes

<a id="ansible-core-8"></a>
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
* ansible\-test \- Generate <code>dist\_info</code> when running tests\.
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
* ansible\-test \- Upgrade the distro\-specific test containers\.
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
* task results \- Python and Powershell modules do not include the <code>invocation</code> task result key by default\. Injection of the <code>invocation</code> task result key for Python and Powershell modules may be enabled with the var\-settable <code>INJECT\_INVOCATION</code> config item\. Most callbacks mask <code>invocation</code> when displaying a task or loop item result\.
* to\_yaml / to\_nice\_yaml filters \- Add optional <code>vault\_behavior</code> argument to configure how vaulted values are rendered\.
* worker process \- When controller and forked child workers must share a TTY\, the <code>WORKER\_SESSION\_ISOLATION</code> config item can be set to <code>false</code> \(via variable/config/envvar\) to disable forked worker session isolation\.

<a id="amazon-aws-3"></a>
#### amazon\.aws

* Add support for the io2 storage type for RDS \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2748](https\://github\.com/ansible\-collections/amazon\.aws/pull/2748)\)\.
* Various modules and utilities \- migrated from deprecated <code>ansible\.module\_utils\.\_text</code> to <code>ansible\.module\_utils\.common\.text\.converters</code> \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2860](https\://github\.com/ansible\-collections/amazon\.aws/pull/2860)\)\.
* amazon\.aws\.cloudformation \- Fixed an issue where creating a changeset in check mode would fail if the stack is not in a ready state \(e\.g\.\, UPDATE\_IN\_PROGRESS\)\. The module now waits for the stack to be in a ready state \(UPDATE\_COMPLETE\) before creating the changeset \([https\://github\.com/ansible\-collections/amazon\.aws/pull/1910](https\://github\.com/ansible\-collections/amazon\.aws/pull/1910)\)
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
* elb\_application\_lb\_info \- Fixed return value documentation to correctly reflect actual types and added missing fields \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2939](https\://github\.com/ansible\-collections/amazon\.aws/issues/2939)\)\.
* extensions/eda/plugins/event\_source/aws\_sqs\_queue\.py \- Added optional support for feedback so that the event can be removed from the SQS Queue on receipt of acknowledgement from ansible\-rulebook\.
* indirect node count \- Add support for querying RDS database resources \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2825](https\://github\.com/ansible\-collections/amazon\.aws/pull/2825)\)\.
* indirect node count \- Create query for networking load balancer resources \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2818](https\://github\.com/ansible\-collections/amazon\.aws/pull/2818)\)\.
* indirect node count \- create query for ec2 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2807](https\://github\.com/ansible\-collections/amazon\.aws/pull/2807)\)\.
* indirect node count \- create query for networking resources vpc\, subnet\, nat gateway\, internet gateway\, virtual gateway\, route table\, vpn\, vpc peering \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2811](https\://github\.com/ansible\-collections/amazon\.aws/pull/2811)\)\.
* indirect node count \- create query for storage resources S3 bucket and Object \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2811](https\://github\.com/ansible\-collections/amazon\.aws/pull/2811)\)\.
* meta/runtime\.yml \- Lowered the <code>ansible\-core</code> minimum version to <code>2\.16</code>\. This expands compatibility and does not change or remove existing functionality\.
* module\_utils\.s3 \- added \"501\" to the list of error codes thrown by S3 replacements \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2447](https\://github\.com/ansible\-collections/amazon\.aws/issues/2447)\)\.
* module\_utils/\_s3/common \- use <code>is\_boto3\_error\_httpstatus</code> to handle HTTP 403 and 501 status codes from S3\-compatible services \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2776](https\://github\.com/ansible\-collections/amazon\.aws/pull/2776)\)\.
* module\_utils/botocore \- add <code>is\_boto3\_error\_httpstatus</code> helper function to catch boto3 exceptions based on HTTP status codes \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2776](https\://github\.com/ansible\-collections/amazon\.aws/pull/2776)\)\.
* module\_utils/errors \- Add support for f\-string style parameter interpolation in error handler descriptions to provide more detailed error messages \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2944](https\://github\.com/ansible\-collections/amazon\.aws/pull/2944)\)\.
* module\_utils/s3 \- refactored S3 module utilities to consolidate duplicate code\, add comprehensive type hints and docstrings\, and improve maintainability \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* plugin\_utils/inventory \- add error handling for ClientError and BotoCoreError in \_freeze\_iam\_role method \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2902](https\://github\.com/ansible\-collections/amazon\.aws/pull/2902)\)\.
* plugin\_utils/inventory \- extract role session name generation into separate method to improve code organisation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2902](https\://github\.com/ansible\-collections/amazon\.aws/pull/2902)\)\.
* requirements\.txt \- Added <code>aiobotocore</code> as a dependency for the event source plugins only \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2816](https\://github\.com/ansible\-collections/amazon\.aws/pull/2816)\)\.
* route53 \- added <code>record\_values</code> key to <code>resource\_record\_sets</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* route53 \- added <code>routing\_region</code> parameter to explicitly specify the region for latency\-based resource record sets \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2893](https\://github\.com/ansible\-collections/amazon\.aws/issues/2893)\)\.
* route53 \- added temporary <code>aws\_region</code> parameter to allow specifying the AWS region for API requests while the <code>region</code> parameter is being transitioned \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2893](https\://github\.com/ansible\-collections/amazon\.aws/issues/2893)\)\.
* route53 \- refactored module utility to use decorator\-based error handling\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2892](https\://github\.com/ansible\-collections/amazon\.aws/pull/2892)\)
* route53\_health\_check \- refactored module to improve testability and type safety\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2892](https\://github\.com/ansible\-collections/amazon\.aws/pull/2892)\)
* s3\_bucket \- Added O\(account\_regional\) parameter to support creating buckets in the account\-regional namespace\. Requires at least botocore version 1\.42\.67 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2960](https\://github\.com/ansible\-collections/amazon\.aws/pull/2960)\)\.
* s3\_bucket \- Added support for managing bucket logging configuration \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2855](https\://github\.com/ansible\-collections/amazon\.aws/pull/2855)\)\.
* s3\_bucket \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* s3\_bucket\_info \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* s3\_object \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* s3\_object\_info \- refactored to use centralized S3 wrapper functions from module\_utils and consistently use S3ErrorHandler \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2782](https\://github\.com/ansible\-collections/amazon\.aws/pull/2782)\)\.
* sts\_assume\_role \- improve error handling for <code>MalformedPolicyDocument</code> errors by providing a clearer error message when an invalid policy document is provided \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2778](https\://github\.com/ansible\-collections/amazon\.aws/pull/2778)\)\.

<a id="ansible-netcommon-2"></a>
#### ansible\.netcommon

* Exposes new libssh option to configure key\_exchange\_algorithms\. This requires ansible\-pylibssh v1\.3\.0 or higher\.
* Option to use libssh as transport while using netconf\, is added\.
* The dependency on ansible\-pylibssh \(for ssh\_type\=libssh / network\_cli\) is now ansible\-pylibssh\>\=1\.4\.0 in requirements\.txt\, raised from the previous \>\=0\.2\.0 requirement\. Installations still on ansible\-pylibssh 0\.x or 1\.x below 1\.4\.0 must upgrade to use the libssh connection path with this collection release\.
* The ssh\-python module is needed\, which will ensure libssh as transport for netconf operations\. When use\_libssh is enabled\.
* libssh connection \- When log\_path is set \(e\.g\. via ANSIBLE\_LOG\_PATH or log\_path in ansible\.cfg\)\, the plugin now routes ansible\-pylibssh \(libssh\) logs into the same Ansible log file\. Log level is derived from display\.verbosity using Python standard logging\: verbosity 0 \-\> WARNING\, 1\-2 \-\> INFO\, 3\+ \-\> DEBUG\. This allows SSH/libssh debug and trace output to appear in the configured log file for troubleshooting without changing ansible\-pylibssh configuration manually\.
* network\_cli \- The in\-collection paramiko path supports the same host key policy behavior \(including host\_key\_auto\_add and known\_hosts handling\) and persistent connection caching as the previous ansible\-core paramiko integration\.
* network\_cli \- When ssh\_type is set to paramiko\, the connection plugin now uses an in\-collection paramiko implementation instead of loading ansible\-core\'s paramiko connection plugin\. This allows network\_cli to work with versions of ansible\-core\, where the paramiko connection plugin was removed\.

<a id="ansible-posix-2"></a>
#### ansible\.posix

* acl \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* authorized\_key \- fix deprecated <code>ansible\.module\_utils\.\_text</code> and <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* cgroup\_perf\_recap callback \- fix deprecated <code>ansible\.module\_utils\.\_text</code> and <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* csh shell plugin \- fix deprecated <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* firewalld\_info \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* firewalld\_info \- use module\.warn instead of passing <code>warnings</code> to <code>exit\_json</code> \([https\://github\.com/ansible\-collections/ansible\.posix/issues/710](https\://github\.com/ansible\-collections/ansible\.posix/issues/710)\)\.
* fish shell plugin \- fix deprecated <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* json callback \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* jsonl callback \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* mount \- fix deprecated <code>ansible\.module\_utils\.\_text</code> and <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* patch \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* profile\_roles callback \- fix deprecated <code>ansible\.module\_utils\.six</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* profile\_tasks \- Add option to provide a different date/time format \([https\://github\.com/ansible\-collections/ansible\.posix/issues/279](https\://github\.com/ansible\-collections/ansible\.posix/issues/279)\)\.
* profile\_tasks callback \- fix deprecated <code>ansible\.module\_utils\.six</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* removed ANSIBLE\_METADATA from remaining plugins\.
* rhel\_rpm\_ostree \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* rpm\_ostree\_upgrade \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* seboolean \- fix deprecated <code>ansible\.module\_utils\.\_text</code> import \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* synchronize \- fix deprecated <code>ansible\.module\_utils\.\_text</code>\, <code>ansible\.module\_utils\.common\.\_collections\_compat</code>\, and <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.
* sysctl \- fix deprecated <code>ansible\.module\_utils\.\_text</code> and <code>ansible\.module\_utils\.six</code> imports \([https\://github\.com/ansible\-collections/ansible\.posix/issues/686](https\://github\.com/ansible\-collections/ansible\.posix/issues/686)\)\.

<a id="ansible-windows-5"></a>
#### ansible\.windows

* Add official support for Ansible 2\.20
* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* ansible\.windows\.win\_package \- Add optional Authenticode signature validation for installer files via the new <code>verify\_signature</code> parameter\.
* win\_environment \- Add the return value <code>env\_values</code> which is a copy of the existing <code>values</code> return value\. The documentation for <code>values</code> has been removed to discourage use of that version due to the inability to use <code>values</code> with dot notation in a Jinja2 template due to the conflict with the Python <code>values</code> attribute\.
* win\_file \- is aligned with <code>ansible\.builtin\.file</code> and now supports options <code>access\_time</code>\, <code>access\_time\_format</code>\, <code>modification\_time</code>\, and <code>modification\_time\_format</code>\. \([https\://github\.com/ansible\-collections/ansible\.windows/issues/798](https\://github\.com/ansible\-collections/ansible\.windows/issues/798)\)
* win\_shell \- Add <code>cmd</code> module option that can be used instead of the free form input\. This aligns the options to the POSIX <code>shell</code> module\.
* win\_shell \- Support using <code>pwsh\.exe</code> as the executable in a mode similar to how <code>powershell\.exe</code> is run\.

<a id="arista-eos-1"></a>
#### arista\.eos

* Added <code>content</code> parameter to support pre\-rendered template configurations in eos\_config module
* Replace deprecated imports from ansible\.module\_utils\.\_text with ansible\.module\_utils\.common\.text\.converters\.
* Updated ansible\.netcommon dependency minimum required version from \>\=8\.1\.0 to \>\=8\.5\.2\.
* which provides a cleaner alternative to the deprecated template auto\-processing behavior of the <code>src</code> parameter\.

<a id="cisco-aci"></a>
#### cisco\.aci

* Add contract\_type option to aci\_contract\_subject\_to\_filter and aci\_contract\_subject\.
* Add l3out\, l3out\_tenant\, external\_epg and redistribute options to aci\_l4l7\_device\_selection\_interface\_context\.
* Add normalize\_payload\_values option to aci\_rest for Ansible Core 2\.19 support\.
* Add set\_communities\, set\_as\_path and set\_policy\_tag options to aci\_tenant\_action\_rule\_profile\.

<a id="cisco-ios-1"></a>
#### cisco\.ios

* Adds a new Resource Module <em class="title-reference">ios\_bfd\_interfaces</em> to configure BFD on interfaces\.
* Adds a new Resource Module <em class="title-reference">ios\_bfd\_templates</em> to configure BFD  using templates\.
* Updated ansible\.netcommon dependency minimum required version from \>\=8\.1\.0 to \>\=8\.5\.1\.
* Updated ansible\.netcommon dependency minimum required version from \>\=8\.5\.1 to \>\=8\.5\.2\.
* ci \- Updated integration test matrix to add stable\-2\.20 coverage and drop stable\-2\.16 for libssh integration tests\.
* ios\_config \- Add <code>content</code> parameter to support pre\-rendered template configurations\. This provides a cleaner alternative to the deprecated template auto\-processing behavior of the <code>src</code> parameter\.
* ios\_l2\_interfaces \- Added xconnect and encapsulation attributes for L2VPN pseudowire and MPLS services configuration\.
* ios\_l3\_interfaces \- Add support for \'redirects\' and \'unreachables\' attributes to configure ICMP redirect and unreachable messages\.
* ios\_user module adds purge\_keys parameter to manage multiple SSH keys per user\. Cisco IOS devices support maximum 2 SSH keys per user\. The purge\_keys parameter enables removal of existing keys not in the sshkey list when provisioning new keys\.

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* Added <code>content</code> parameter to support pre\-rendered template configurations in iosxr\_config module which provides a cleaner alternative to the deprecated template auto\-processing behavior of the <code>src</code> parameter\.
* Bump minimum <code>ansible\.netcommon</code> dependency from <code>\>\=8\.1\.0</code> to <code>\>\=8\.5\.1</code> in <code>galaxy\.yml</code>\.
* Updated ansible\.netcommon dependency minimum required version from \>\=8\.5\.1 to \>\=8\.5\.2\.
* iosxr\_l3\_interfaces \- Added support for <em class="title-reference">flow\.ipv4\.direction</em> and <em class="title-reference">flow\.ipv6\.direction</em> value <em class="title-reference">bidirectional</em>\. The module now expands bidirectional flow configuration into both ingress and egress IOS\-XR flow monitor commands\.

<a id="cisco-meraki-2"></a>
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

* Added <code>content</code> parameter to support pre\-rendered template configurations in nxos\_config module
* Added alias for mode option as switchport\_mode for nxos\_l2\_interfaces
* Updated ansible\.netcommon dependency minimum required version from \>\=8\.1\.0 to \>\=8\.5\.1\.
* Updated ansible\.netcommon dependency minimum required version from \>\=8\.5\.1 to \>\=8\.5\.2\.
* nxos\_l2\_interfaces \- Add <em class="title-reference">trunk\.allowed\_vlans\_none</em> option to explicitly configure <em class="title-reference">switchport trunk allowed vlan none</em> on interfaces\.
* which provides a cleaner alternative to the deprecated template auto\-processing behavior of the <code>src</code> parameter\.

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Added missing param when creating a health monitor

<a id="community-aws-3"></a>
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

* acme\_\* modules \- experimentally support <code>dns\-account\-01</code> challenge type according to [acme\-dns\-account\-label draft 02](https\://datatracker\.ietf\.org/doc/html/draft\-ietf\-acme\-dns\-account\-label\-02)\. Note that breaking changes to this challenge type can also happen in minor releases until the acme\-dns\-account\-label draft has been finalized as an RFC \([https\://github\.com/ansible\-collections/community\.crypto/pull/996](https\://github\.com/ansible\-collections/community\.crypto/pull/996)\)\.
* acme\_\* modules \- experimentally support <code>dns\-persist\-01</code> challenge type according to [acme\-dns\-persist draft 01](https\://www\.ietf\.org/archive/id/draft\-ietf\-acme\-dns\-persist\-01\.html)\. Note that breaking changes to this challenge type can also happen in minor releases until the acme\-dns\-persist draft has been finalized as an RFC \([https\://github\.com/ansible\-collections/community\.crypto/pull/997](https\://github\.com/ansible\-collections/community\.crypto/pull/997)\)\.
* luks\_device \- add support for TPM2 enrollment using <code>systemd\-cryptsetup</code> \([https\://github\.com/ansible\-collections/community\.crypto/issues/850](https\://github\.com/ansible\-collections/community\.crypto/issues/850)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/972](https\://github\.com/ansible\-collections/community\.crypto/pull/972)\)\.
* luks\_device \- add support for keyslot priority \([https\://github\.com/ansible\-collections/community\.crypto/issues/850](https\://github\.com/ansible\-collections/community\.crypto/issues/850)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/972](https\://github\.com/ansible\-collections/community\.crypto/pull/972)\)\.

<a id="community-dns-2"></a>
#### community\.dns

* Hetzner DNS modules and plugins \- support the [new Hetzner DNS API](https\://docs\.hetzner\.com/networking/dns/faq/beta/) \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* Migrate codebase to Python 3 only \([https\://github\.com/ansible\-collections/community\.dns/pull/319](https\://github\.com/ansible\-collections/community\.dns/pull/319)\, [https\://github\.com/ansible\-collections/community\.dns/pull/320](https\://github\.com/ansible\-collections/community\.dns/pull/320)\, [https\://github\.com/ansible\-collections/community\.dns/pull/321](https\://github\.com/ansible\-collections/community\.dns/pull/321)\)\.

<a id="community-docker-1"></a>
#### community\.docker

* docker\_compose\_v2\_pull \- adds <code>ignore\_pull\_failures</code> parameter that passes <code>\-\-ignore\-pull\-failures</code> to the <code>docker compose pull</code> call when set to <code>true</code> \([https\://github\.com/ansible\-collections/community\.docker/pull/1248](https\://github\.com/ansible\-collections/community\.docker/pull/1248)\)\.
* docker\_image\_export \- adds <code>platform</code> parameter to allow exporting a specific platform variant from a multi\-arch image \([https\://github\.com/ansible\-collections/community\.docker/issues/1064](https\://github\.com/ansible\-collections/community\.docker/issues/1064)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1251](https\://github\.com/ansible\-collections/community\.docker/pull/1251)\)\.

<a id="community-general-6"></a>
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
* campfire \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* chef\_databag lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* chroot connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* chroot connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* circonus\_annotation \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* cloudflare\_dns \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* cmd\_runner module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* cobbler inventory plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* cobbler inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* cobbler\_sync \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* cobbler\_sync \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* cobbler\_sync \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* cobbler\_system \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* cobbler\_system \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* cobbler\_system \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11105](https\://github\.com/ansible\-collections/community\.general/pull/11105)\)\.
* collection\_version lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* composer \- add <code>force</code> parameter\; when <code>command\=create\-project</code>\, the module now checks whether a <code>composer\.json</code> already exists in <code>working\_dir</code> and skips the command if so\, making the task idempotent\. Set <code>force\=true</code> to always run the command regardless \([https\://github\.com/ansible\-collections/community\.general/issues/725](https\://github\.com/ansible\-collections/community\.general/issues/725)\, [https\://github\.com/ansible\-collections/community\.general/pull/11689](https\://github\.com/ansible\-collections/community\.general/pull/11689)\)\.
* composer \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* consul module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* consul\_kv \- add <code>ca\_path</code> option to specify a CA bundle for HTTPS connections \([https\://github\.com/ansible\-collections/community\.general/pull/11817](https\://github\.com/ansible\-collections/community\.general/pull/11817)\)\.
* consul\_kv lookup plugin \- add <code>ca\_path</code> option to specify a CA bundle for HTTPS connections \([https\://github\.com/ansible\-collections/community\.general/issues/2876](https\://github\.com/ansible\-collections/community\.general/issues/2876)\, [https\://github\.com/ansible\-collections/community\.general/pull/11817](https\://github\.com/ansible\-collections/community\.general/pull/11817)\)\.
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
* datetime module utils \- remove code for unsupported Python version \([https\://github\.com/ansible\-collections/community\.general/pull/11048](https\://github\.com/ansible\-collections/community\.general/pull/11048)\)\.
* dconf \- add support for C\(dbus\-broker\) \([https\://github\.com/ansible\-collections/community\.general/issues/495](https\://github\.com/ansible\-collections/community\.general/issues/495)\, [https\://github\.com/ansible\-collections/community\.general/pull/11772](https\://github\.com/ansible\-collections/community\.general/pull/11772)\)\.
* dconf \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* decompress \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* dependent lookup plugin \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* dependent lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* deps module utils \- change the internal representaion of dependency state \([https\://github\.com/ansible\-collections/community\.general/pull/11242](https\://github\.com/ansible\-collections/community\.general/pull/11242)\)\.
* deps module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* dig lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* dimensiondata\_network \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* dimensiondata\_network modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* dnf\_config\_manager \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* dnsimple\_info \- use Ansible construct to validate parameters \([https\://github\.com/ansible\-collections/community\.general/pull/11052](https\://github\.com/ansible\-collections/community\.general/pull/11052)\)\.
* dnstxt lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* doas become plugin \- add new option <code>allow\_pipelining</code> to explicitly allow the use of pipelining with this plugin\. This should only be set to <code>true</code> with ansible\-core 2\.19\+ when <code>doas</code> does not require a password \([https\://github\.com/ansible\-collections/community\.general/issues/11411](https\://github\.com/ansible\-collections/community\.general/issues/11411)\, [https\://github\.com/ansible\-collections/community\.general/pull/11481](https\://github\.com/ansible\-collections/community\.general/pull/11481)\)\.
* dsv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* elastic callback plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* elasticsearch\_plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* etcd3 lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* exceptions module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* filesize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* filesize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* filesystem \- migrate <code>LVM\.get\_fs\_size\(\)</code> to use <code>CmdRunner</code>\, ensuring locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/pull/11888](https\://github\.com/ansible\-collections/community\.general/pull/11888)\)\.
* flatpak \- add new parameter <code>from\_url</code> to install a flatpak from a <code>\.flatpakref</code> URL \([https\://github\.com/ansible\-collections/community\.general/issues/4000](https\://github\.com/ansible\-collections/community\.general/issues/4000)\, [https\://github\.com/ansible\-collections/community\.general/pull/11748](https\://github\.com/ansible\-collections/community\.general/pull/11748)\)\.
* flatpak \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* flatpak\_remote \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* fqdn\_valid test plugin \- add proper parameter checking\, and add type hints \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* from\_csv filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* from\_ini filter plugin \- add <code>delimiters</code> parameter to allow correctly parsing more INI documents \([https\://github\.com/ansible\-collections/community\.general/issues/11506](https\://github\.com/ansible\-collections/community\.general/issues/11506)\, [https\://github\.com/ansible\-collections/community\.general/pull/11512](https\://github\.com/ansible\-collections/community\.general/pull/11512)\)\.
* from\_ini filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* gandi\_livedns \- add support for diff mode\, showing before and after state of DNS records \([https\://github\.com/ansible\-collections/community\.general/issues/4927](https\://github\.com/ansible\-collections/community\.general/issues/4927)\, [https\://github\.com/ansible\-collections/community\.general/pull/11934](https\://github\.com/ansible\-collections/community\.general/pull/11934)\)\.
* gandi\_livedns\_api module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* gandi\_livedns\_api module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* gem \- add <code>override\_platform\_install\_dir</code> option to work around OS\-injected platform install dir defaults on distributions such as Fedora \([https\://github\.com/ansible\-collections/community\.general/issues/3259](https\://github\.com/ansible\-collections/community\.general/issues/3259)\, [https\://github\.com/ansible\-collections/community\.general/pull/11873](https\://github\.com/ansible\-collections/community\.general/pull/11873)\)\.
* gem \- refactor module to use <code>CmdRunner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11733](https\://github\.com/ansible\-collections/community\.general/pull/11733)\)\.
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
* gitlab\_user \- add the <code>sshkey\_update\_mode</code> option to control whether same\-name SSH keys are preserved\, updated when unique\, or deduplicated before replacement \([https\://github\.com/ansible\-collections/community\.general/issues/6516](https\://github\.com/ansible\-collections/community\.general/issues/6516)\, [https\://github\.com/ansible\-collections/community\.general/pull/11996](https\://github\.com/ansible\-collections/community\.general/pull/11996)\)\.
* grove \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* gunicorn \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* haproxy \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* hashids filter \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* hashids filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* hg \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* hg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* homebrew\_services \- remove various redundancies including dead state validation\, unused return values\, and unnecessary locale environment variables \([https\://github\.com/ansible\-collections/community\.general/pull/11839](https\://github\.com/ansible\-collections/community\.general/pull/11839)\)\.
* homebrew\_services \- replace <code>NamedTuple</code> with dataclass \([https\://github\.com/ansible\-collections/community\.general/pull/12094](https\://github\.com/ansible\-collections/community\.general/pull/12094)\)\.
* homebrew\_tap \- avoid redundant <code>brew tap</code> calls when processing multiple taps by fetching the tap list once upfront \([https\://github\.com/ansible\-collections/community\.general/pull/11848](https\://github\.com/ansible\-collections/community\.general/pull/11848)\)\.
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
* infinity \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* influxdb\_query \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* influxdb\_user \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* influxdb\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* influxdb\_write \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ini\_file \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
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
* ipa\_dnsrecord \- add <code>exclusive</code> parameter to allow appending values to existing records without replacing them \([https\://github\.com/ansible\-collections/community\.general/issues/682](https\://github\.com/ansible\-collections/community\.general/issues/682)\, [https\://github\.com/ansible\-collections/community\.general/pull/11694](https\://github\.com/ansible\-collections/community\.general/pull/11694)\)\.
* ipa\_dnsrecord \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_dnszone \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_group \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_hbacrule \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_host \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_hostgroup \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_otpconfig \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* ipa\_otptoken \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
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
* irc \- use proper boolean value in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11076](https\://github\.com/ansible\-collections/community\.general/pull/11076)\)\.
* iso\_create \- add <code>boot\_options</code> parameter to support creating bootable ISOs using El Torito boot records \([https\://github\.com/ansible\-collections/community\.general/issues/1685](https\://github\.com/ansible\-collections/community\.general/issues/1685)\, [https\://github\.com/ansible\-collections/community\.general/pull/11991](https\://github\.com/ansible\-collections/community\.general/pull/11991)\)\.
* iso\_customize \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* jail connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* jail connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* java\_cert \- support proxy authentication when <code>https\_proxy</code> environment variable includes credentials \([https\://github\.com/ansible\-collections/community\.general/issues/4126](https\://github\.com/ansible\-collections/community\.general/issues/4126)\, [https\://github\.com/ansible\-collections/community\.general/pull/11753](https\://github\.com/ansible\-collections/community\.general/pull/11753)\)\.
* jc filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* jenkins\_credential \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jenkins\_job \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* jenkins\_job\_info \- remove conditional code handling SSL for unsupported versions of Python \([https\://github\.com/ansible\-collections/community\.general/pull/11078](https\://github\.com/ansible\-collections/community\.general/pull/11078)\)\.
* jenkins\_node \- remove code for unsupported Python version \([https\://github\.com/ansible\-collections/community\.general/pull/11048](https\://github\.com/ansible\-collections/community\.general/pull/11048)\)\.
* jenkins\_plugin \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* jenkins\_plugin \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jenkins\_plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* jenkins\_plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* jenkins\_plugin modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* jenkins\_script \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* jenkins\_script \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jira \- add <code>cloud</code> option to support Jira Cloud\'s new search endpoint <code>/rest/api/2/search/jql</code>\, since the legacy <code>/rest/api/2/search</code> endpoint has been removed on Jira Cloud \([https\://github\.com/ansible\-collections/community\.general/issues/10786](https\://github\.com/ansible\-collections/community\.general/issues/10786)\, [https\://github\.com/ansible\-collections/community\.general/pull/11701](https\://github\.com/ansible\-collections/community\.general/pull/11701)\)\.
* jira \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11104](https\://github\.com/ansible\-collections/community\.general/pull/11104)\)\.
* jira \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* jira \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* jira \- when <code>cloud\=true</code>\, user\-type fields \(<code>assignee</code>\, <code>reporter</code>\, and any listed in the new <code>custom\_user\_fields</code> parameter\) containing an email address are automatically resolved to Jira Cloud account IDs \([https\://github\.com/ansible\-collections/community\.general/issues/11734](https\://github\.com/ansible\-collections/community\.general/issues/11734)\, [https\://github\.com/ansible\-collections/community\.general/pull/11735](https\://github\.com/ansible\-collections/community\.general/pull/11735)\)\.
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
* keys\_filter plugin utils \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
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
* lists filter plugin \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* lists\_mergeby filter plugin \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* lldp \- the module has been renamed to <code>community\.general\.lldp\_facts</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11980](https\://github\.com/ansible\-collections/community\.general/pull/11980)\)\.
* lldp \- the module now supports check mode \([https\://github\.com/ansible\-collections/community\.general/pull/11980](https\://github\.com/ansible\-collections/community\.general/pull/11980)\)\.
* lmdb\_kv lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* locale\_gen \- extend the search for available locales to include <code>/usr/local/share/i18n/SUPPORTED</code> in Debian and Ubuntu systems \([https\://github\.com/ansible\-collections/community\.general/issues/10964](https\://github\.com/ansible\-collections/community\.general/issues/10964)\, [https\://github\.com/ansible\-collections/community\.general/pull/11046](https\://github\.com/ansible\-collections/community\.general/pull/11046)\)\.
* locale\_gen \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* logentries \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* logentries callback plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* logrotate \- adds optional <code>backup</code> parameter to create a backup of the existing configuration file before writing changes \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logrotate \- allow hourly logrotate \([https\://github\.com/ansible\-collections/community\.general/pull/11939](https\://github\.com/ansible\-collections/community\.general/pull/11939)\)\.
* lookup plugin passwordstore \- modernize internal <code>check\_output2\(\)</code> helper using <code>subprocess\.run\(\)</code> and rename it to <code>run\_backend\_cmd\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11655](https\://github\.com/ansible\-collections/community\.general/pull/11655)\)\.
* lvg \- migrate to <code>CmdRunner</code>\, removing direct <code>run\_command</code> calls and <code>run\_command\_environ\_update</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11835](https\://github\.com/ansible\-collections/community\.general/pull/11835)\)\.
* lvm\_pv \- migrate to <code>CmdRunner</code> using shared runners from <code>module\_utils/\_lvm</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11811](https\://github\.com/ansible\-collections/community\.general/pull/11811)\)\.
* lvm\_pv \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11343](https\://github\.com/ansible\-collections/community\.general/pull/11343)\)\.
* lvol \- migrate to <code>CmdRunner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11887](https\://github\.com/ansible\-collections/community\.general/pull/11887)\)\.
* lxc connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxc connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxc\_container \- refactor function <code>create\_script</code>\, using <code>subprocess\.Popen\(\)</code>\, to a new module\_utils <code>\_lxc</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11204](https\://github\.com/ansible\-collections/community\.general/pull/11204)\)\.
* lxc\_container \- use <code>tempfile\.TemporaryDirectory\(\)</code> instead of <code>mkdtemp\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11323](https\://github\.com/ansible\-collections/community\.general/pull/11323)\)\.
* lxc\_container \- use shared LVM runners from <code>\_lvm</code> module utils instead of direct <code>run\_command</code> calls for LVM2 commands \([https\://github\.com/ansible\-collections/community\.general/pull/11920](https\://github\.com/ansible\-collections/community\.general/pull/11920)\)\.
* lxca\_cmms \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* lxca\_nodes \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* lxd connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxd inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* lxd module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* lxd module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* lxd module utils \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* lxd\_container \- improve code by using native Python construct \([https\://github\.com/ansible\-collections/community\.general/pull/11215](https\://github\.com/ansible\-collections/community\.general/pull/11215)\)\.
* macports \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* mail \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* manageiq module utils \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* manageiq module utils \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* manageiq\_alert\_profiles \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* manageiq\_alert\_profiles \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* manageiq\_alerts \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* mattermost\, rocketchat\, slack \- update default <code>icon\_url</code> to ansible favicon \([https\://github\.com/ansible\-collections/community\.general/pull/11909](https\://github\.com/ansible\-collections/community\.general/pull/11909)\)\.
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
* nmap inventory plugin \- add <code>skip\_host\_discovery</code> option to skip nmap host discovery phase \(<code>\-Pn</code>\) \([https\://github\.com/ansible\-collections/community\.general/issues/7893](https\://github\.com/ansible\-collections/community\.general/issues/7893)\, [https\://github\.com/ansible\-collections/community\.general/pull/11955](https\://github\.com/ansible\-collections/community\.general/pull/11955)\)\.
* nmap inventory plugin \- added <code>set\_name\_variable</code> option to control whether the <code>name</code> variable is set for each host\, allowing users to avoid the \"Found variable using reserved name\" warning while maintaining backward compatibility \([https\://github\.com/ansible\-collections/community\.general/pull/11893](https\://github\.com/ansible\-collections/community\.general/pull/11893)\, [https\://github\.com/ansible\-collections/community\.general/issues/11766](https\://github\.com/ansible\-collections/community\.general/issues/11766)\)\.
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
* nomad\_job \- use <code>\_nomad</code> module utils for common Nomad connection logic \([https\://github\.com/ansible\-collections/community\.general/issues/7688](https\://github\.com/ansible\-collections/community\.general/issues/7688)\, [https\://github\.com/ansible\-collections/community\.general/pull/11957](https\://github\.com/ansible\-collections/community\.general/pull/11957)\)\.
* nomad\_job\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nomad\_job\_info \- use <code>\_nomad</code> module utils for common Nomad connection logic \([https\://github\.com/ansible\-collections/community\.general/issues/7688](https\://github\.com/ansible\-collections/community\.general/issues/7688)\, [https\://github\.com/ansible\-collections/community\.general/pull/11957](https\://github\.com/ansible\-collections/community\.general/pull/11957)\)\.
* nomad\_token \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* nomad\_token \- use <code>\_nomad</code> module utils for common Nomad connection logic \([https\://github\.com/ansible\-collections/community\.general/issues/7688](https\://github\.com/ansible\-collections/community\.general/issues/7688)\, [https\://github\.com/ansible\-collections/community\.general/pull/11957](https\://github\.com/ansible\-collections/community\.general/pull/11957)\)\.
* nosh \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* nosh \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* nsupdate \- add <code>timeout</code> parameter to control the DNS query timeout \([https\://github\.com/ansible\-collections/community\.general/issues/9906](https\://github\.com/ansible\-collections/community\.general/issues/9906)\, [https\://github\.com/ansible\-collections/community\.general/pull/12012](https\://github\.com/ansible\-collections/community\.general/pull/12012)\)\.
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
* one\_service \- replace function\-local <code>namedtuple</code> with module\-level dataclass \([https\://github\.com/ansible\-collections/community\.general/pull/12094](https\://github\.com/ansible\-collections/community\.general/pull/12094)\)\.
* one\_vm \- move <code>import</code> statemetns to the top of the file \([https\://github\.com/ansible\-collections/community\.general/pull/11396](https\://github\.com/ansible\-collections/community\.general/pull/11396)\)\.
* one\_vm \- replace function\-local <code>namedtuple</code> with module\-level dataclass \([https\://github\.com/ansible\-collections/community\.general/pull/12094](https\://github\.com/ansible\-collections/community\.general/pull/12094)\)\.
* one\_vm \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* oneandone\_firewall\_policy \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_load\_balancer \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_monitoring\_policy \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_private\_network \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* oneandone\_server \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11231](https\://github\.com/ansible\-collections/community\.general/pull/11231)\)\.
* oneandone\_server modules \- mark <code>\%</code> templating as <code>noqa</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* onepassword \- add support for <code>op\://</code> secret references in the OnePassword lookup plugin \([https\://github\.com/ansible\-collections/community\.general/issues/7586](https\://github\.com/ansible\-collections/community\.general/issues/7586)\, [https\://github\.com/ansible\-collections/community\.general/pull/11958](https\://github\.com/ansible\-collections/community\.general/pull/11958)\)\.
* onepassword lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* onepassword\_info \- execute external commands using Ansible construct \([https\://github\.com/ansible\-collections/community\.general/pull/11193](https\://github\.com/ansible\-collections/community\.general/pull/11193)\)\.
* onepassword\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* onepassword\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* oneview module utils \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* oneview module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* oneview\_san\_manager \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* online inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* online module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\)\.
* opendj\_backendprop \- refactor to use <code>CmdRunner</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11728](https\://github\.com/ansible\-collections/community\.general/pull/11728)\)\.
* opendj\_backendprop \- use Ansible construct to perform check for external commands \([https\://github\.com/ansible\-collections/community\.general/pull/11072](https\://github\.com/ansible\-collections/community\.general/pull/11072)\)\.
* opennebula inventory plugin \- replace function\-local <code>namedtuple</code> with module\-level dataclass \([https\://github\.com/ansible\-collections/community\.general/pull/12094](https\://github\.com/ansible\-collections/community\.general/pull/12094)\)\.
* opennebula inventory plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* opennebula inventory plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* opentelemetry callback plugin \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* osx\_defaults \- add support for <code>dict</code> type values\, including <code>dict\_mode</code> option to merge keys into an existing dictionary \([https\://github\.com/ansible\-collections/community\.general/issues/238](https\://github\.com/ansible\-collections/community\.general/issues/238)\, [https\://github\.com/ansible\-collections/community\.general/pull/11659](https\://github\.com/ansible\-collections/community\.general/pull/11659)\)\.
* osx\_defaults \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_device \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* packet\_device \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11231](https\://github\.com/ansible\-collections/community\.general/pull/11231)\)\.
* packet\_device modules \- mark <code>\%</code> templating as <code>noqa</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* packet\_ip\_subnet \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* packet\_ip\_subnet \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_project \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* packet\_sshkey \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* packet\_volume \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* packet\_volume \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* pacman \- add <code>root</code>\, <code>cachedir</code>\, and <code>config</code> options to support installing packages into an alternative root directory \([https\://github\.com/ansible\-collections/community\.general/issues/438](https\://github\.com/ansible\-collections/community\.general/issues/438)\, [https\://github\.com/ansible\-collections/community\.general/pull/11681](https\://github\.com/ansible\-collections/community\.general/pull/11681)\)\.
* pacman \- replace <code>namedtuple</code> with dataclass for <code>VersionTuple</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12094](https\://github\.com/ansible\-collections/community\.general/pull/12094)\)\.
* pam\_limits \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* pamd \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* pamd \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* parted \- add <code>unit\_preserve\_case</code> option to control the case of the <code>unit</code> field in the return value\, fixing the round\-trip use case where the returned unit is fed back as input \([https\://github\.com/ansible\-collections/community\.general/issues/1860](https\://github\.com/ansible\-collections/community\.general/issues/1860)\, [https\://github\.com/ansible\-collections/community\.general/pull/11813](https\://github\.com/ansible\-collections/community\.general/pull/11813)\)\.
* parted \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* parted \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* passwordstore lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* pear \- fix cases of unused variables in loops \([https\://github\.com/ansible\-collections/community\.general/pull/11115](https\://github\.com/ansible\-collections/community\.general/pull/11115)\)\.
* pids \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pids \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* pipx \- small refactor\, no behavior affected \([https\://github\.com/ansible\-collections/community\.general/pull/11640](https\://github\.com/ansible\-collections/community\.general/pull/11640)\)\.
* pipx module utils \- small refactor\, no behavior affected \([https\://github\.com/ansible\-collections/community\.general/pull/11640](https\://github\.com/ansible\-collections/community\.general/pull/11640)\)\.
* pipx\_info \- small refactor\, no behavior affected \([https\://github\.com/ansible\-collections/community\.general/pull/11640](https\://github\.com/ansible\-collections/community\.general/pull/11640)\)\.
* pmem \- simplify text tests without using regular expression \([https\://github\.com/ansible\-collections/community\.general/pull/11388](https\://github\.com/ansible\-collections/community\.general/pull/11388)\)\.
* portage \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* pritunl\_org \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_org\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_user \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pritunl\_user\_info \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* pubnub\_blocks \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
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
* redfish\_utils module utils \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* redfish\_utils module utils \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11112](https\://github\.com/ansible\-collections/community\.general/pull/11112)\)\.
* redfish\_utils module utils \- use Python\-defined constants for HTTP return codes \([https\://github\.com/ansible\-collections/community\.general/pull/11561](https\://github\.com/ansible\-collections/community\.general/pull/11561)\, [https\://github\.com/ansible\-collections/community\.general/pull/11573](https\://github\.com/ansible\-collections/community\.general/pull/11573)\)\.
* redhat\_subscription \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* redhat\_subscription \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* redhat\_subscription \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* redis cache plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* redis lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* revbitspss lookup plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* rhevm \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* rhevm \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11097](https\://github\.com/ansible\-collections/community\.general/pull/11097)\)\.
* rhsm\_repository \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* riak \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* rocketchat \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
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
* slack \- consolidate double and triple whitespaces \([https\://github\.com/ansible\-collections/community\.general/pull/11029](https\://github\.com/ansible\-collections/community\.general/pull/11029)\)\.
* slack \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11908](https\://github\.com/ansible\-collections/community\.general/pull/11908)\)\.
* slack \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* slackpkg \- refactor function <code>query\_packages\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11390](https\://github\.com/ansible\-collections/community\.general/pull/11390)\)\.
* slackpkg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* snap \- add <code>devmode</code> option to support installing snaps in developer mode \([https\://github\.com/ansible\-collections/community\.general/pull/11952](https\://github\.com/ansible\-collections/community\.general/pull/11952)\, [https\://github\.com/ansible\-collections/community\.general/issues/8155](https\://github\.com/ansible\-collections/community\.general/issues/8155)\)\.
* snap \- add <code>revision</code> parameter to install a specific snap revision \([https\://github\.com/ansible\-collections/community\.general/issues/11467](https\://github\.com/ansible\-collections/community\.general/issues/11467)\, [https\://github\.com/ansible\-collections/community\.general/pull/11984](https\://github\.com/ansible\-collections/community\.general/pull/11984)\)\.
* snap \- add support for <code>system</code> as a special configuration target\, allowing <code>snap set system</code> to be used via the <code>options</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/11266](https\://github\.com/ansible\-collections/community\.general/issues/11266)\, [https\://github\.com/ansible\-collections/community\.general/pull/12025](https\://github\.com/ansible\-collections/community\.general/pull/12025)\)\.
* snap \- improve templating of strings \([https\://github\.com/ansible\-collections/community\.general/pull/11189](https\://github\.com/ansible\-collections/community\.general/pull/11189)\)\.
* snmp\_facts \- simplify and improve code using standard Ansible validations \([https\://github\.com/ansible\-collections/community\.general/pull/11148](https\://github\.com/ansible\-collections/community\.general/pull/11148)\)\.
* solaris\_zone \- execute external commands using Ansible construct \([https\://github\.com/ansible\-collections/community\.general/pull/11192](https\://github\.com/ansible\-collections/community\.general/pull/11192)\)\.
* solaris\_zone \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* solaris\_zone \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* sorcery \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* spectrum\_model\_attrs \- convert <code>\%</code> templating to f\-string \([https\://github\.com/ansible\-collections/community\.general/pull/11229](https\://github\.com/ansible\-collections/community\.general/pull/11229)\)\.
* spotinst\_aws\_elastigroup \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* ssh\_config \- add support for the <code>AddressFamily</code> option \([https\://github\.com/ansible\-collections/community\.general/pull/11968](https\://github\.com/ansible\-collections/community\.general/pull/11968)\)\.
* statusio\_maintenance \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11102](https\://github\.com/ansible\-collections/community\.general/pull/11102)\)\.
* sudoers \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11098](https\://github\.com/ansible\-collections/community\.general/pull/11098)\)\.
* sudoers \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* supervisorctl \- added an additional condition for generating the error \'no such process\' \([https\://github\.com/ansible\-collections/community\.general/issues/11621](https\://github\.com/ansible\-collections/community\.general/issues/11621)\, [https\://github\.com/ansible\-collections/community\.general/pull/11632](https\://github\.com/ansible\-collections/community\.general/pull/11632)\)\.
* supervisorctl \- when <code>name\=all</code>\, dispatch a single <code>supervisorctl start/stop/restart all</code> command \([https\://github\.com/ansible\-collections/community\.general/issues/8159](https\://github\.com/ansible\-collections/community\.general/issues/8159)\, [https\://github\.com/ansible\-collections/community\.general/pull/11953](https\://github\.com/ansible\-collections/community\.general/pull/11953)\)\.
* svc \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/1114](https\://github\.com/ansible\-collections/community\.general/pull/1114)\)\.
* svc \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* svr4pkg \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* swupd \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* terraform \- minor code cleanup \([https\://github\.com/ansible\-collections/community\.general/pull/11879](https\://github\.com/ansible\-collections/community\.general/pull/11879)\)\.
* timestamp callback plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* timezone \- replace <code>list\(map\(\.\.\.\)\)</code> constructs with Python comprehensions \([https\://github\.com/ansible\-collections/community\.general/pull/11590](https\://github\.com/ansible\-collections/community\.general/pull/11590)\)\.
* timezone \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* to\_ini filter plugin \- add <code>no\_extra\_spaces</code> parameter \([https\://github\.com/ansible\-collections/community\.general/issues/8576](https\://github\.com/ansible\-collections/community\.general/issues/8576)\, [https\://github\.com/ansible\-collections/community\.general/pull/12059](https\://github\.com/ansible\-collections/community\.general/pull/12059)\)\.
* to\_ini filter plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* tss lookup plugin \- fixed <code>AccessTokenAuthorizer</code> initialization to include <code>base\_url</code> parameter for proper token authentication \([https\://github\.com/ansible\-collections/community\.general/pull/11031](https\://github\.com/ansible\-collections/community\.general/pull/11031)\)\.
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
* xenserver\_guest \- use <code>enumerate\(\)</code> instead of manual index variable in <code>for</code> loop \([https\://github\.com/ansible\-collections/community\.general/pull/11721](https\://github\.com/ansible\-collections/community\.general/pull/11721)\)\.
* xenserver\_guest modules \- replace <code>\%</code> templating with f\-strings or <code>format\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11223](https\://github\.com/ansible\-collections/community\.general/pull/11223)\)\.
* xfs\_quota \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* xml \- add <code>create\_if\_missing</code> option to control whether a node is created when <code>value</code> is set and <code>xpath</code> finds no match \([https\://github\.com/ansible\-collections/community\.general/issues/8730](https\://github\.com/ansible\-collections/community\.general/issues/8730)\, [https\://github\.com/ansible\-collections/community\.general/pull/12031](https\://github\.com/ansible\-collections/community\.general/pull/12031)\)\.
* xml \- add <code>huge\_tree</code> option to support processing of very large XML files \([https\://github\.com/ansible\-collections/community\.general/issues/4897](https\://github\.com/ansible\-collections/community\.general/issues/4897)\, [https\://github\.com/ansible\-collections/community\.general/pull/11940](https\://github\.com/ansible\-collections/community\.general/pull/11940)\)\.
* xml \- remove redundant conversions to unicode \([https\://github\.com/ansible\-collections/community\.general/pull/11106](https\://github\.com/ansible\-collections/community\.general/pull/11106)\)\.
* xml \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* yaml cache plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* yum\_versionlock \- remove redundant conversion to unicode in command output \([https\://github\.com/ansible\-collections/community\.general/pull/11093](https\://github\.com/ansible\-collections/community\.general/pull/11093)\)\.
* zfs \- simplify return of boolean values in functions \([https\://github\.com/ansible\-collections/community\.general/pull/11119](https\://github\.com/ansible\-collections/community\.general/pull/11119)\)\.
* zfs\_facts \- use Ansible construct to check result of external command \([https\://github\.com/ansible\-collections/community\.general/pull/11054](https\://github\.com/ansible\-collections/community\.general/pull/11054)\)\.
* zone connection plugin \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11341](https\://github\.com/ansible\-collections/community\.general/pull/11341)\)\.
* zone connection plugin \- use <code>raise \.\.\. from \.\.\.</code> when passing on exceptions \([https\://github\.com/ansible\-collections/community\.general/pull/11095](https\://github\.com/ansible\-collections/community\.general/pull/11095)\)\.
* zypper \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.
* zypper\_repository \- update to Python 3\.7 idioms \([https\://github\.com/ansible\-collections/community\.general/pull/11344](https\://github\.com/ansible\-collections/community\.general/pull/11344)\)\.

<a id="community-libvirt-2"></a>
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
* proxmox \- add <code>destroy\_unreferenced\_disks</code> parameter \([https\://github\.com/ansible\-collections/community\.proxmox/pull/422](https\://github\.com/ansible\-collections/community\.proxmox/pull/422)\)\.
* proxmox \- add <code>totp</code> authentification support \([https\://github\.com/ansible\-collections/community\.proxmox/pull/265](https\://github\.com/ansible\-collections/community\.proxmox/pull/265)\)\.
* proxmox \- add a new helper <em class="title-reference">create\_proxmox\_module\(\)</em> which adds generic auth args and constraints\, and merges in the module\-specific args and options \([https\://github\.com/ansible\-collections/community\.proxmox/pull/289](https\://github\.com/ansible\-collections/community\.proxmox/pull/289)\)\.
* proxmox \- adds <code>cmode</code> parameter for supporting console modes \([https\://github\.com/ansible\-collections/community\.proxmox/pull/420](https\://github\.com/ansible\-collections/community\.proxmox/pull/420)  / issue [https\://github\.com/ansible\-collections/community\.proxmox/issues/65](https\://github\.com/ansible\-collections/community\.proxmox/issues/65)\)\.
* proxmox \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox \- set <code>state</code> as not <code>required</code> and set default value <code>present</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/292](https\://github\.com/ansible\-collections/community\.proxmox/pull/292)\)\.
* proxmox \- update <code>proxmoxer</code> required dependencies to <code>\>\=2\.3</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/265](https\://github\.com/ansible\-collections/community\.proxmox/pull/265)\)\.
* proxmox inventory \- add <code>templates</code> group to the inventory \([https\://github\.com/ansible\-collections/community\.proxmox/pull/399](https\://github\.com/ansible\-collections/community\.proxmox/pull/399)\)\.
* proxmox\_acme\_account \- set <code>no\_log</code> on sensitive value <code>eab\_kid</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/418](https\://github\.com/ansible\-collections/community\.proxmox/pull/418)\)\.
* proxmox\_disk \- change disk size units to GiB \([https\://github\.com/ansible\-collections/community\.proxmox/pull/236](https\://github\.com/ansible\-collections/community\.proxmox/pull/236)\)\.
* proxmox\_kvm \- add <code>destroy\_unreferenced\_disks</code> parameter \([https\://github\.com/ansible\-collections/community\.proxmox/pull/422](https\://github\.com/ansible\-collections/community\.proxmox/pull/422)\)\.
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
* proxmox\_storage \- add <code>preallocation</code> parameter on <code>cifs</code> storage backend \([https\://github\.com/ansible\-collections/community\.proxmox/pull/386](https\://github\.com/ansible\-collections/community\.proxmox/pull/386)\)\.
* proxmox\_storage \- add <code>preallocation</code> parameter on <code>nfs</code> storage backend \([https\://github\.com/ansible\-collections/community\.proxmox/pull/390](https\://github\.com/ansible\-collections/community\.proxmox/pull/390)\)\.
* proxmox\_storage \- add <code>snapshot\_as\_volume\_chain</code> parameter on <code>cifs</code> storage backend \([https\://github\.com/ansible\-collections/community\.proxmox/pull/387](https\://github\.com/ansible\-collections/community\.proxmox/pull/387)\)\.
* proxmox\_storage \- add alias <code>subdirectory</code> for <code>subdir</code> on cifs backend \([https\://github\.com/ansible\-collections/community\.proxmox/pull/388](https\://github\.com/ansible\-collections/community\.proxmox/pull/388)\)\.
* proxmox\_storage \- add feature of subdirectory in CIFS share\. \([https\://github\.com/ansible\-collections/community\.proxmox/pull/214](https\://github\.com/ansible\-collections/community\.proxmox/pull/214)\)\.
* proxmox\_storage \- add support of <code>encryption\_key</code> on <code>pbs</code> storage backend \([https\://github\.com/ansible\-collections/community\.proxmox/pull/389](https\://github\.com/ansible\-collections/community\.proxmox/pull/389)\)\.
* proxmox\_storage \- enhanced error handling and parameters validation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- fix passing nfs\_options to API payload \([https\://github\.com/ansible\-collections/community\.proxmox/issues/203](https\://github\.com/ansible\-collections/community\.proxmox/issues/203)\, [https\://github\.com/ansible\-collections/community\.proxmox/pull/221](https\://github\.com/ansible\-collections/community\.proxmox/pull/221)\)\.
* proxmox\_storage \- fixed CIFS authentication by sending username and password parameters to proxmoxer \([https\://github\.com/ansible\-collections/community\.proxmox/pull/214](https\://github\.com/ansible\-collections/community\.proxmox/pull/214)\)\.
* proxmox\_storage \- refactor the validation of storage options \([https\://github\.com/ansible\-collections/community\.proxmox/pull/266](https\://github\.com/ansible\-collections/community\.proxmox/pull/266)\)\.
* proxmox\_storage \- the parameter <code>state</code> now has a default value of <code>present</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- when <code>state\=present</code> parameters <code>content</code> and <code>nodes</code> are now not required \([https\://github\.com/ansible\-collections/community\.proxmox/pull/315](https\://github\.com/ansible\-collections/community\.proxmox/pull/315)\)\.
* proxmox\_storage\_contents\_info \- Add support for content type <code>import</code> \([https\://github\.com/ansible\-collections/community\.proxmox/pull/260](https\://github\.com/ansible\-collections/community\.proxmox/pull/260)\)\.
* proxmox\_zone\, proxmox\_vnet\, proxmox\_subnet \- make sdn modules compatible with pve8 \([https\://github\.com/ansible\-collections/community\.proxmox/pull/254](https\://github\.com/ansible\-collections/community\.proxmox/pull/254)\)\.

<a id="community-proxysql"></a>
#### community\.proxysql

* Add PostgreSQL support with the new <code>proxysql\_pgsql\_users</code>\, <code>proxysql\_pgsql\_servers</code>\, <code>proxysql\_pgsql\_hostgroup\_attributes</code>\, <code>proxysql\_pgsql\_query\_rules</code>\, <code>proxysql\_pgsql\_query\_rules\_fast\_routing</code>\, and <code>proxysql\_pgsql\_replication\_hostgroups</code> modules\.

<a id="community-routeros-2"></a>
#### community\.routeros

* api\_info \- add missing <code>numbers</code> parameter across numerous existing paths for RouterOS \>\= 7\.15\.2 \([https\://github\.com/ansible\-collections/community\.routeros/pull/458](https\://github\.com/ansible\-collections/community\.routeros/pull/458)\)\.
* api\_info \- add support for the <code>interface dot1x server active</code>\, <code>ip hotspot active</code>\, <code>ip ipsec active\-peers</code>\, <code>ip proxy cache\-contents</code>\, <code>ip socks connections</code>\, <code>user active</code>\, and <code>user\-manager session</code> paths as info\-only \(read\-only\) paths \([https\://github\.com/ansible\-collections/community\.routeros/pull/458](https\://github\.com/ansible\-collections/community\.routeros/pull/458)\)\.
* api\_info \- adds support for additional read\-only parameters in the <code>app</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- add 46 new parameters to the <code>interface ethernet switch port</code> path for RouterOS \>\= 7\.15 \(CRS1xx/2xx variant\) including QoS\, mirroring\, VLAN\, and learning control parameters \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add <code>2g\-probe\-delay</code> field to path <code>interface wifi steering</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>aaa\.\*</code>\, <code>channel\.\*</code>\, <code>datapath\.\*</code>\, <code>interworking\.\*</code>\, <code>security\.\*</code>\, <code>steering\.\*</code> sub\-fields to path <code>interface wifi configuration</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>color</code> parameter to the <code>zerotier interface</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>comment</code>\, <code>disabled</code>\, <code>independent\-learning</code>\, <code>qos\-group</code>\, <code>svl</code>\, and <code>switch</code> parameters to the <code>interface ethernet switch vlan</code> path for RouterOS \>\= 7\.15 \(CRS1xx/2xx variant\) \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add <code>current\-defaults</code> parameter to the <code>ip dns</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>deprioritize\-unii\-3\-4</code>\, <code>reselect\-interval</code>\, <code>reselect\-time</code> fields to path <code>interface wifi channel</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>mld\-datapath</code> parameter to the <code>interface wifi cap</code> path for RouterOS \>\= 7\.22\.1 \([https\://github\.com/ansible\-collections/community\.routeros/pull/459](https\://github\.com/ansible\-collections/community\.routeros/pull/459)\)\.
* api\_info\, api\_modify \- add <code>multi\-passphrase\-group</code> field to path <code>interface wifi security</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/428](https\://github\.com/ansible\-collections/community\.routeros/pull/428)\)\.
* api\_info\, api\_modify \- add <code>prefix\-pool</code> field to and fix default of <code>address\-pool</code> for <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/430](https\://github\.com/ansible\-collections/community\.routeros/pull/430)\)\.
* api\_info\, api\_modify \- add <code>send\-email\-from</code>\, <code>send\-email\-to</code> and <code>send\-smtp\-server</code> to <code>system watchdog</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/429](https\://github\.com/ansible\-collections/community\.routeros/pull/429)\)\.
* api\_info\, api\_modify \- add <code>switch\-all\-ports</code> parameter in the <code>interface ethernet switch</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/463](https\://github\.com/ansible\-collections/community\.routeros/pull/463)\)\.
* api\_info\, api\_modify \- add <code>traffic\-processing</code> field to path <code>interface wifi datapath</code> and <code>interface wifi configuration</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/424](https\://github\.com/ansible\-collections/community\.routeros/pull/424)\)\.
* api\_info\, api\_modify \- add <code>use\-bfd</code> to <code>routing ospf interface\-template</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/425](https\://github\.com/ansible\-collections/community\.routeros/pull/425)\)\.
* api\_info\, api\_modify \- add <code>vrf</code> to <code>ip service</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/426](https\://github\.com/ansible\-collections/community\.routeros/pull/426)\)\.
* api\_info\, api\_modify \- add default values for fields <code>ciphers</code> in <code>ip ssh</code>\, <code>mvrp</code> in  <code>interface vlan</code>\, and <code>mvrp\-forbidden</code> in <code>interface bridge vlan</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/439/](https\://github\.com/ansible\-collections/community\.routeros/pull/439/)\)\.
* api\_info\, api\_modify \- add missing attribute <code>radsec\-timeout</code> for the <code>radius</code> path which exists since RouterOS version 7\.19\.6 \([https\://github\.com/ansible\-collections/community\.routeros/pull/412](https\://github\.com/ansible\-collections/community\.routeros/pull/412)\)\.
* api\_info\, api\_modify \- add missing parameters to path <code>interface bridge</code> and <code>interface bridge port</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/423](https\://github\.com/ansible\-collections/community\.routeros/pull/423)\)\.
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
* api\_info\, api\_modify \- add support for path <code>disk settings</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/422](https\://github\.com/ansible\-collections/community\.routeros/pull/422)\)\.
* api\_info\, api\_modify \- add support for path <code>interface dot1x client</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/414](https\://github\.com/ansible\-collections/community\.routeros/pull/414)\)\.
* api\_info\, api\_modify \- add support for path <code>interface dot1x server</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/413](https\://github\.com/ansible\-collections/community\.routeros/pull/413)\)\.
* api\_info\, api\_modify \- add support for path <code>ip socks access</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/431](https\://github\.com/ansible\-collections/community\.routeros/pull/431)\)\.
* api\_info\, api\_modify \- add support for paths <code>ip hotspot</code>\, <code>ip hotspot profile</code>\, <code>ip hotspot user</code>\, <code>ip hotspot user profile</code>\, <code>ip hotspot walled\-garden</code>\, and <code>ip hotspot walled\-garden ip</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/418](https\://github\.com/ansible\-collections/community\.routeros/pull/418)\)\.
* api\_info\, api\_modify \- adds default value and removes required being true for parameter <code>address\-pool</code> in the <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for multiple <code>healthcheck\-\*</code> parameters in the <code>container</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for new <code>input\.add\-path</code> and <code>output\.add\-path</code> parameters replacing <code>add\-path\-out</code> in BGP\-related paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the  <code>lacp\-mode</code> \(\>\= 7\.19\)\, <code>lacp\-system\-id</code> \(\>\= 7\.21\) and <code>lacp\-system\-priority</code> \(\>\= 7\.21\) parameters in the <code>interface bonding</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>3gpp\-info\-raw</code> \(\>\= 7\.21\)\, and <code>realms\-raw</code> \(\>\= 7\.21\) parameters in the <code>interface wifi interworking</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-prefix\-without\-address</code> \(\>\= 7\.20\)\, <code>allow\-reconfigure</code> \(\>\= 7\.17\)\, <code>check\-gateway</code> \(\>\= 7\.19\)\, <code>custom\-iana\-id</code> \(\>\= 7\.20\)\, <code>custom\-iapd\-id</code> \(\>\= 7\.20\)\, <code>default\-route\-tables</code> \(\>\= 7\.19\)\, <code>prefix\-address\-lists</code> \(\>\= 7\.17\) and <code>rapid\-commit</code> \(\>\= 7\.17\) parameters in the <code>ipv6 dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-proto\-version</code>\, <code>accept\-pseudowire\-type</code>\, <code>l2tpv3\-circuit\-id</code>\, <code>l2tpv3\-cookie\-length</code>\, <code>l2tpv3\-digest\-hash</code> and <code>l2tpv3\-ether\-interface\-list</code> parameters in the <code>interface l2tp\-server server</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-router\-advertisements\-on</code> parameters in the <code>ipv6 settings</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>accept\-untagged</code> \(\>\= 7\.20\)\, and <code>pppoe\-over\-vlan\-range</code> \(\>\= 7\.17\) parameters in the <code>interface pppoe\-server server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>add\-arp</code> \(\>\= 7\.15\)\, <code>address\-lists</code> \(\>\= 7\.17\) and <code>use\-reconfigure</code> \(\>\= 7\.19\) parameters in the <code>ip dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>add\-topics\-string</code> and <code>script</code> parameters in the <code>system logging action</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>address\-list\-extra\-time</code> and <code>vrf</code> parameters in the <code>ip dns</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>address\-lists</code> \(\>\= 7\.17\)\, <code>ignore\-ia\-na\-bindings</code> \(\>\= 7\.20\)\, <code>prefix\-pool</code> \(\>\= 7\.17\) and <code>use\-reconfigure</code> \(\>\= 7\.17\) parameters in the <code>ipv6 dhcp\-server</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>agent\-circuit\-id</code> and <code>agent\-remote\-id</code> parameters in the <code>ip dhcp\-server lease</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>allow\-dual\-stack\-queue</code>\, <code>block\-access</code>\, <code>dhcp\-option\-set</code>\, <code>lease\-time</code>\, <code>parent\-queue</code>\, <code>queue\-type</code>\, <code>rate\-limit</code>\, <code>routes</code> and <code>use\-src\-mac</code> parameters in the <code>ip dhcp\-server lease</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>allow\-reconfigure</code> \(\>\= 7\.19\)\, <code>check\-gateway</code> \(\>\= 7\.19\)\, <code>default\-route\-tables</code> \(\>\= 7\.18\)\, <code>dscp</code> \(\>\= 7\.20\)\, <code>use\-broadcast</code> \(\>\= 7\.20\) and <code>vlan\-priority</code> \(\>\= 7\.20\) parameters in the <code>ip dhcp\-client</code> path \([https\://github\.com/ansible\-collections/community\.routeros/issues/407](https\://github\.com/ansible\-collections/community\.routeros/issues/407)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>allowed\-addresses4</code> and <code>allowed\-addresses6</code> parameters in the <code>tool bandwidth\-server</code> path for RouterOS \>\= 7\.18 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>app settings</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>app\-store\-urls</code> parameter in the <code>app settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>chain</code>\, <code>realm</code>\, and <code>vrf</code> parameters in the <code>routing rule</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>channel\.deprioritize\-unii\-3\-4</code> \(\>\= 7\.20\)\, <code>channel\.reselect\-interval</code> \(\>\= 7\.15\)\, <code>channel\.reselect\-time</code> \(\>\= 7\.19\)\, <code>configuration\.distance</code> \(\>\= 7\.15\)\, <code>configuration\.installation</code> \(\>\= 7\.17\)\, <code>configuration\.max\-clients</code> \(\>\=7\.18\)\, <code>configuration\.station\-roaming</code> \(\>\= 7\.17\)\, <code>configuration\.tx\-chains</code> \(\>\= 7\.15\)\, <code>datapath\.openflow\-switch</code> \(\>\= 7\.20\)\, <code>security\.multi\-passphrase\-group</code> \(\>\= 7\.17\) and <code>steering\.2g\-probe\-delay</code> \(\>\=7\.18\) parameters in the <code>interface wifi</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>channel\.preamble\-puncturing</code> parameter in the <code>interface wifi configuration</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>channel\.preamble\-puncturing</code>\, <code>mld\-interface</code>\, and <code>mld\-name</code> parameters in the <code>interface wifi</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>comment</code> parameter in the <code>system logging</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>ddos\-cookie\-threshold</code> parameter in the <code>ip ipsec settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>dhcp\-server\-vrf</code> \(\>\= 7\.15\) and <code>local\-address\-as\-src\-ip</code> \(\>\= 7\.17\) parameters in the <code>ip dhcp\-relay</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>dhcp6\-pd\-preferred</code> parameter in the <code>ipv6 nd prefix</code> and <code>ipv6 nd prefix default</code> paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>from\-pool</code> parameter in the <code>ipv6 pool</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>interface wifi network</code> and <code>interface wifi network radio</code> paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wifi radio settings</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wifi security multi\-passphrase</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless channels</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless interworking\-profiles</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless nstreme\-dual</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interface wireless wds</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>interframe\-gap</code> parameter in the <code>iot modbus</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>ip reverse\-proxy</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>mlag\-heartbeat</code>\, <code>mlag\-peer\-port</code>\, <code>mlag\-priority</code>\, and <code>ra\-guard</code> parameters in the <code>interface bridge</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>mld\-static</code> parameter in the <code>interface wifi cap</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls ldp local\-mapping</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls ldp neighbor</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls ldp remote\-mapping</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls mangle</code> path for RouterOS \>\= 7\.17 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls settings</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls traffic\-eng interface</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls traffic\-eng path</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mpls traffic\-eng tunnel</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>multi\-link\-mode</code> and <code>supported\-hw\-caps</code> parameters in the <code>interface wifi provisioning</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>multipath</code> parameter in the <code>routing bgp instance</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>mvrp\-forbidden</code> parameter in the <code>interface bridge vlan</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>mvrp</code> \(\>\= 7\.15\) and <code>l3\-hw\-offloading</code> \(\>\= 7\.21\) parameters in the <code>interface vlan</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>name</code> parameter in the <code>ip dhcp\-client</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>otp\-secret</code> parameter in the <code>ip hotspot user</code> path for RouterOS \>\= 7\.21\.3 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>password\-authentication</code> and <code>publickey\-authentication\-options</code> parameters in the <code>ip ssh</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>password</code> parameter in the <code>interface dot1x client</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>password</code> parameter in the <code>system package local\-update update\-package\-source</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>policy\-rules</code> parameter in the <code>routing settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>polling</code> \(\>\= 7\.16\)\, <code>remove\-sent\-sms\-after\-send</code> \(\>\= 7\.20\) and <code>sms\-storage</code> \(\>\= 7\.15\) parameters in the <code>tool sms</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ppk\-secret</code> parameter in the <code>ip ipsec peer</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ppk</code> parameter in the <code>ip ipsec profile</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>ppp l2tp\-secret</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>preamble\-puncturing</code> parameter in the <code>interface wifi channel</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>pref\-src</code> \(\>\= 7\.20\)\, <code>suppress\-hw\-offload</code> \(\>\= 7\.15\) parameters in the <code>ipv6 route</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>preferred\-architecture</code> parameter in the <code>system routerboard settings</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>push\-routes\-ipv6</code> parameter in the <code>interface ovpn\-server server</code> path for RouterOS \>\= 7\.21 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>pvid</code>\, <code>use\-https</code>\, and <code>yaml</code> parameters in the <code>app</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
* api\_info\, api\_modify \- adds support for the <code>radius\-password</code> parameters in the <code>ip dhcp\-server config</code> path for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>regex</code> \(\>\= 7\.17\) parameter in the <code>system logging</code> path \([https\://github\.com/ansible\-collections/community\.routeros/pull/433](https\://github\.com/ansible\-collections/community\.routeros/pull/433)\)\.
* api\_info\, api\_modify \- adds support for the <code>request\-interval</code> parameter in the <code>interface detect\-internet</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adds support for the <code>trusted\-ra</code> parameter in the <code>interface bridge port</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- adjusts handling of required parameters in the <code>interface wifi</code> path by removing <code>default\-name</code> from <code>required\_one\_of</code> for RouterOS \>\= 7\.15 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- removed support for the <code>add\-path\-out</code> parameter in BGP\-related paths for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_info\, api\_modify \- removed support for the <code>system package local\-update</code> path for RouterOS \>\= 7\.22 \([https\://github\.com/ansible\-collections/community\.routeros/pull/457](https\://github\.com/ansible\-collections/community\.routeros/pull/457)\)\.
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
* api\_modify\, api\_info \- sort versioned buckets numerically so tighter bounds match before broader ones \([https\://github\.com/ansible\-collections/community\.routeros/pull/456](https\://github\.com/ansible\-collections/community\.routeros/pull/456)\)\.

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

* all modules and plugins \- allow retrieving private age keys and private SSH keys through commands with the new <code>age\_key\_cmd</code> and <code>age\_ssh\_private\_key\_cmd</code> options \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.
* all modules and plugins \- allow to configure GCP access with the <code>gcp\_oauth\_access\_token</code> and <code>gcp\_kms\_client\_type</code> options \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.
* load\_vars \- now supports ansible\-core 2\.21\'s way of actually loading variables\, instead of returning <code>ansible\_facts</code>\. The behavior for this can be controlled through the new <code>return\_method</code> option\, which is by default set to <code>auto</code>\. On ansible\-core 2\.21\+\, <code>auto</code> behaves the same as <code>vars\-only</code> \(return proper variables\)\, and for ansible\-core before 2\.21 the same as <code>facts\-only</code> \(return <code>ansible\_facts</code>\) \([https\://github\.com/ansible\-collections/community\.sops/pull/283](https\://github\.com/ansible\-collections/community\.sops/pull/283)\)\.
* sops\_encrypt \- support providing HuaweiCloud KMS key IDs with the <code>huawei\_cloud\_kms</code> option \([https\://github\.com/ansible\-collections/community\.sops/issues/282](https\://github\.com/ansible\-collections/community\.sops/issues/282)\, [https\://github\.com/ansible\-collections/community\.sops/pull/286](https\://github\.com/ansible\-collections/community\.sops/pull/286)\)\.

<a id="community-windows-4"></a>
#### community\.windows

* Add official support for Ansible 2\.20

<a id="community-zabbix"></a>
#### community\.zabbix

* host \- Added support for vault passwords\.
* web role \- added support for IPv6
* zabbix frontend and server encryption support\: [https\://www\.zabbix\.com/documentation/7\.4/en/manual/introduction/whatsnew\#tls\-encryption\-between\-frontend\-and\-server](https\://www\.zabbix\.com/documentation/7\.4/en/manual/introduction/whatsnew\#tls\-encryption\-between\-frontend\-and\-server) \& [https\://www\.zabbix\.com/documentation/current/en/manual/appendix/install/frontend\_encrypt](https\://www\.zabbix\.com/documentation/current/en/manual/appendix/install/frontend\_encrypt)
* zabbix\_agent \- \[WINDOWS\] Add INSTALLFOLDER parameter to msi install
* zabbix\_agent \- add variable for customizing releases url \([https\://services\.zabbix\.com/updates/v1](https\://services\.zabbix\.com/updates/v1)\)
* zabbix\_triggerprototype \- use templated and templateid\=0 when host\_name is given\, only templated for template\_name
* zabbix\_valuemap \- add value mappings type suboption which specifies the mapping match type \([https\://github\.com/ansible\-collections/community\.zabbix/issues/1636](https\://github\.com/ansible\-collections/community\.zabbix/issues/1636)\)\.

<a id="containers-podman-3"></a>
#### containers\.podman

* Add \-\-platform option to podman\_image
* Add configuration for new Ansible release
* Fix CI of Podman Search modul
* Fix tests for new Podman
* Fix version in galaxy
* add passthrough and none log driver options
* podman\_prune \- Add idempotency support

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

* Added 22 new modules\.
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
* primary\_ip \- Primary IP support upcoming <code>assignee\_type</code> behavior change\.
* primary\_ip \- Unassign Primary IP before deleting it\.
* primary\_ip \- Unassign primary\_ip if <code>server</code> is null\.
* primary\_ip\_info \- Added the Primary IPs <code>location</code> name to the return values \(<code>hcloud\_primary\_ip\_info\[\]\.location</code>\)\.
* server \- Rebuilding a Server now supports the <code>user\_data</code> argument\.
* server\_network \- Add <code>ip\_range</code> argument to attach a load balancer to a specific subnet\.
* server\_type\_info \- Added the Server Type Location <code>available</code> property to the return values \(<code>hcloud\_server\_type\_info\[\]\.locations\[\]\.available</code>\)\.
* server\_type\_info \- Added the Server Type Location <code>recommended</code> property to the return values \(<code>hcloud\_server\_type\_info\[\]\.locations\[\]\.recommended</code>\)\.
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

<a id="hitachivantara-vspone-block-1"></a>
#### hitachivantara\.vspone\_block

* Added \"playbooks/vsp\_direct/vsp\_storage\_connection\_session\_example\.yml\" as a sample playbook demonstrating session\-based storage operations\.
* Added a new \"hv\_gad\_bulk\" module for batch creation of multiple GAD pairs on VSP block storage systems\.
* Added a new \"hv\_hg\_bulk\" module for bulk host group management operations with multithreading support for parallel processing across multiple ports on VSP block storage systems\.
* Added a new \"hv\_hur\_bulk\" module for bulk creation of HUR pairs on VSP block storage systems\.
* Added a new \"hv\_iscsi\_target\_bulk\" module for bulk iSCSI target management operations with multithreading support for parallel processing across multiple ports on VSP block storage systems\.
* Added a new \"hv\_ldev\_bulk\" module for bulk operations on logical devices \(LDEVs\) on VSP block storage systems\.
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
* Added a new \"hv\_truecopy\_bulk\" module for bulk creation of TrueCopy pairs in VSP block storage systems\.
* Added a new \"hv\_vclone\_parent\_volume\_facts\" module to retrieve information about virtual clone parent volume from VSP block storage systems\.
* Added a new \"hv\_vsp\_one\_gad\" module for creation\, suspend\, resync and delete of GAD pairs on VSP one BHE storages\.
* Added a new \"hv\_vsp\_one\_gad\_consistency\_group\" module for suspend and resync of GAD pairs in a consistency group on VSP one BHE storages\.
* Added a new \"hv\_vsp\_one\_gad\_consistency\_group\_facts\" module for getting the GAD pair details in a consistency group on VSP one BHE Storages\.
* Added a new \"hv\_vsp\_one\_gad\_facts\" module for getting the GAD pair details on VSP one BHE Storages\.
* Added following tasks to \"hv\_gad\_bulk\" module \- Batch create GAD pairs with host groups with matching volume IDs
* Added following tasks to \"hv\_hur\_bulk\" module \- Create HUR pair in bulk mode with matching volume IDs
* Added new \"hv\_vsp\_create\_primary\_and\_secondary\_diskless\_quorum\_disk\" role for automated diskless quorum disk creation on VSP block storage systems\.
* Added new \"hv\_vsp\_create\_primary\_and\_secondary\_quorum\_disk\" role for automated disk\-based quorum disk creation on VSP block storage systems\.
* Added new \"hv\_vsp\_gad\_pairs\_creation\" role to automate GAD pairs provisioning on VSP block storage systems\.
* Added new \"hv\_vsp\_hur\_pairs\_creation\" role to automate HUR pairs provisioning on VSP block storage systems\.
* Added new \"hv\_vsp\_primary\_secondary\_journal\_creation\" role for automated journal creation on VSP block storage systems\.
* Added notes to module documentation indicating that a few modules are not supported for BHE and higher models\.
* Added support for Ansible core version 2\.20\.
* Added support for Mainframe z16\.
* Added support for SVOS 10\.5\.1\.
* Added support for SVOS 10\.5\.2 for VSP One B24/B26/B28 storage models\.
* Added support for SVOS 10\.5\.3 for VSP One BHE storage models\.
* Added support for SVOS 9\.8\.7 for VSP 5100/5500 \& VSP 5200/5600 storage models\.
* Added support for VSP One SDS Block version 1\.19\.00\.
* Added support for input parameter \"copy\_pace\" to the \"hv\_shadow\_image\_pair\"\, \"hv\_gad\"\, \"hv\_hur\"\, \"hv\_truecopy\"\, and \"hv\_journal\" modules\.
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
* Added support to \"hv\_ldev\" module to create ldev on a specific resource group\.
* Added support to \"hv\_ldev\" module to stop the normal format for all volumes\.
* Added support to \"hv\_ldev\_facts\" module output to include Mainframe\, vClone and other new properties\.
* Added support to \"hv\_ldev\_facts\" module to get information about multiple LDEVs by their IDs\.
* Added support to \"hv\_paritygroup\_facts\" module output to include Mainframe and other new properties\.
* Added support to \"hv\_resource\_group\" module to add multiple hostgroups by ids of a port to an existing Resource Group by ID\.
* Added support to \"hv\_resource\_group\" module to add multiple hostgroups by providing a range of IDs of a port to an existing Resource Group by ID\.
* Added support to \"hv\_resource\_group\" module to remove multiple hostgroups by ids of a port from an existing Resource Group by ID\.
* Added support to \"hv\_resource\_group\" module to remove multiple hostgroups by providing a range of IDs of a port from an existing Resource Group by ID\.
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
* Adjusted galaxy\.yml to exclude development configurations \(like \.ansible\-lint\) from the collection tarball\.
* Enhanced the performance of the \"hv\_gad\_facts\" module\'s task by implementing thread pool and batch processing\.
* Enhanced the performance of the \"hv\_hg\_facts\" module\'s task by implementing parallel calls\.
* Enhanced the performance of the \"hv\_ldev\_facts\" module\'s task by implementing thread pool and batch processing\.
* Modified \.ansible\-lint configuration to remove the \'command\-instead\-of\-module\' skip\-list rule to comply with Red Hat standards\.
* Other minor bug fixes\.
* Updated README\.md to reference meta/runtime\.yml for ansible\-core versioning\.

<a id="hitachivantara-vspone-object-1"></a>
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

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* Remove deprecated import from <code>ansible\.module\_utils\.\_text</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1053](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1053)\)\.
* helm \- add <code>release\_values</code> key to <code>status</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_info \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_info \- add <code>release\_values</code> key to <code>status</code> return value that can be accessed using Jinja2 dot notation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_plugin \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_plugin\_info \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_pull \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_registry\_auth \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* helm\_registry\_auth \- add new option plain\_http to allow insecure http connection when running <code>helm registry login</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1090](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1090)\)\.
* helm\_repository \- Ensure compatibility with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1038)\)\.
* k8s\_drain \- Add support for <code>check\_mode</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1086](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1086)\)\.
* k8s\_drain \- Convert module warnings into informational displays when users explicitly request the deletion of unmanaged pods\, pods with local storage\, or those managed by a <code>DaemonSet</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1037](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1037)\)\.

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* user\_role \- Added <code>roles</code> parameter with <code>add</code>/<code>remove</code>/<code>set</code> pattern to manage multiple roles\. The existing <code>role</code> parameter is deprecated and will be removed in 3\.0\.0\. \(\#352\)

<a id="microsoft-ad-5"></a>
#### microsoft\.ad

* Add official support for Ansible 2\.20

<a id="microsoft-iis-2"></a>
#### microsoft\.iis

* Add official support for Ansible 2\.20

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* na\_ontap\_ems\_filter \- new option <em class="title-reference">parameter\_criteria</em> added in REST\, requires ONTAP 9\.13\.1 or later\.
* na\_ontap\_lun \- updated documentation for unsupported REST parameters\.
* na\_ontap\_net\_ifgrp \- Update <em class="title-reference">mode</em> parameter to specify allowed values\.
* na\_ontap\_nfs \- new option <em class="title-reference">credential\_cache</em> added in REST\.
* na\_ontap\_s3\_users \- new options <em class="title-reference">access\_key</em> \& <em class="title-reference">secret\_key</em> added\.
* na\_ontap\_security\_certificates \- Added support to generate certificate signing requests \(CSRs\) in REST\.
* na\_ontap\_snapmirror \- new options <em class="title-reference">time\_out</em>\, <em class="title-reference">wait\_for\_completion</em> added in REST\.
* na\_ontap\_snapmirror \- updated documentation for <em class="title-reference">identity\_preserve</em> and <em class="title-reference">max\_transfer\_rate</em>\.
* na\_ontap\_svm \- Added option <em class="title-reference">anti\_ransomware\_default\_volume\_state</em> in REST\.
* na\_ontap\_volume \- new option <em class="title-reference">anti\_ransomware\.state</em> added in REST\, requires ONTAP 9\.10 or later\.
* na\_ontap\_volume \- updated docs for <em class="title-reference">tiering\_policy</em>\.
* na\_ontap\_volume\_efficiency\- AWS Lambda support added to the module\.
* na\_ontap\_volume\_efficiency\- Added <em class="title-reference">wait\_for\_completion</em> and <em class="title-reference">time\_out</em> parameters to fix time out errors for long running operations\.
* updated <em class="title-reference">README</em> with information on ASA r2 support\.

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

* Add NetBox v4\.4 integration tests to CI matrix
* Add NetBox v4\.5 support to CI matrix \(netbox\-docker 4\.0\.2\)
* Add <em class="title-reference">module\_type</em> as supported to <em class="title-reference">netbox\_front\_port\_template</em>
* Add <em class="title-reference">module\_type</em> as supported to <em class="title-reference">netbox\_rear\_port\_template</em>
* Add integration tests for contact groups
* Add local integration test runner \(hacking/integration\-test\.sh\)
* Add support for custom headers for all modules
* Change <em class="title-reference">netbox\_contact\.contact\_group</em> to <em class="title-reference">contact\_groups</em>
* Fix ansible\-bad\-import\-from pylint errors
* Fix broken code path when using old api path on old netbox systems
* Fix linting issues with newly released black version
* Make the unit\-test data structures more flexible\.
* Remove abandoned unit\-test data\.
* Update netbox\_front\_port and netbox\_front\_port\_template modules to handle v4\.5 removal of rear\_port/rear\_port\_position fields \(replaced by PortMapping model\)
* Update netbox\_token module to support v4\.5 v2 tokens with description\-based lookup
* Update netbox\_user module to strip is\_staff field on v4\.5\+ \(removed from User model\)
* Use <em class="title-reference">ansible\.module\_utils\.common\.text\.converters</em> instead of the deprecated <em class="title-reference">ansible\.module\_utils\.\_text</em>
* add workaround to \_build\_query\_params for services and Netbox 4\.3\.0 \- 4\.4\.3 \(wrong parent\_object\_type data type\)
* add yamllint to project pipeline\.
* improve version\_check\_greater to be more universal
* netbox\_circuit\_termination \- Add parameters termination\_id and termination\_type for NetBox 4\.2\+
* netbox\_tag \- Add support for object\_types on tags
* netbox\_vlan\_group \- Add tenant field support \([https\://github\.com/netbox\-community/ansible\_modules/issues/1446](https\://github\.com/netbox\-community/ansible\_modules/issues/1446)\)
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

<a id="purestorage-flasharray-3"></a>
#### purestorage\.flasharray

* purefa\_connection \- Add new parameters for key refresh and connection refresh\, as well as ability to update existing connection
* purefa\_info \- Added more data to hostgroup volume information to support NVMe connections
* purefa\_info \- Added tags info to entities that support them
* purefa\_network \- Addressed issues found in update\_interface
* purefa\_phonehome \- Added <code>excludes</code> parameter\, supported from Purity//FA 6\.10\.0
* purefa\_pod \- Fixed pydantic issue from lastest SDK version
* purefa\_policy \- Added Continuous Availability support for SMB policies

<a id="purestorage-flashblade-7"></a>
#### purestorage\.flashblade

* purefa\_ad \- Added support for local servers using the <code>server</code> parameter\.
* purefb\_ad \- Added test and rotate states
* purefb\_ad \- Remove doc references to FQDNs as SPNs are the required method\.
* purefb\_ad \- Updated encryption algorithms to use correct values
* purefb\_ds \- Allow directory services to be modified for internal NFS servers
* purefb\_ds \- Update test state to allow specific tests to be run
* purefb\_info \- Added MAC address information for LAGs

<a id="splunk-es-5"></a>
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
* ci \- Add ansible\-core version matrix \(stable\-2\.16 through stable\-2\.21\) to the network integration test workflow\, aligning with the ITSI pattern\. Lower minimum supported ansible\-core version to 2\.16\.0\.
* splunk\_notes \- new module to manage notes for findings\, investigations\, and response plan tasks\.
* splunk\_notes\_info \- new module to query notes from findings\, investigations\, and response plan tasks\.

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* Feat\: add some parameters to the icinga service module \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/289](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/289)\)

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* Support OAuth1 authentication by passing <code>oauth1\_consumer\_key</code> and <code>oauth1\_consumer\_secret</code> instead of <code>username</code> and <code>password</code>\.
* activation\_key \- add <code>content\_view\_environments</code> parameter to support multi CV \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1935](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1935)\)
* content\_view \- add support for lifecycle environments in rolling content views
* convert2rhel role \- removed subscription support as it\'s been unused since Katello 4\.12 \(05/2024\)
* job\_invocation \- add <code>feature</code> parameter \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1923](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1923)\)
* locations role \- Added <code>state</code> parameter to manage resource presence\.
* registration\_command \- add support for the setup\_container\_registry\_certs parameter \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1966](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1966)\)

<a id="vmware-vmware-3"></a>
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

<a id="vmware-vmware-rest-4"></a>
#### vmware\.vmware\_rest

* Disable check mode for all non\-info modules in this collection\. Check mode was never supported for these modules\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/363](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/363)

<a id="vultr-cloud-1"></a>
#### vultr\.cloud

* Added pagination support by adding <code>api\_results\_per\_page</code> to the common attributes\.
* bare\_metal \- Added support for multi\-disk operation mode by adding <code>mdisk\_mode</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/165](https\://github\.com/vultr/ansible\-collection\-vultr/issues/165)\)\.
* object\_storage \- Object storage subscriptions require specifying a tier upon creation\, added <code>tier</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/135](https\://github\.com/vultr/ansible\-collection\-vultr/issues/135)\)\.
* snapshot \- Added UEFI support adding <code>uefi</code> to the attributes \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/160](https\://github\.com/vultr/ansible\-collection\-vultr/pull/160)\)\.

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-9"></a>
#### Ansible\-core

* psrp \- Changed the default of <code>negotiate\_service</code> used to build the Kerberos Service Principal Name from <code>WSMAN</code> to <code>host</code>\. This aligns the defaults to how the native PowerShell PSRemoting client works on Windows and ensures that Kerberos can be used by more Windows targets by default\. No deprecation period is used for this change as <code>host</code> is a builtin SPN to Windows and should improve compatibility out of the box\. To go back to the old behaviour for any reason\, set <code>ansible\_psrp\_negotiate\_service\=WSMAN</code> in the host vars\.

<a id="community-aws-4"></a>
#### community\.aws

* community\.aws collection \- Due to the AWS SDKs announcing the end of support for Python less than 3\.8 \([https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/](https\://aws\.amazon\.com/blogs/developer/python\-support\-policy\-updates\-for\-aws\-sdks\-and\-tools/)\)\, support for Python less than 3\.8 by this collection has been deprecated and will be removed in release 10\.0\.0\. \([https\://github\.com/ansible\-collections/community\.aws/pull/2304](https\://github\.com/ansible\-collections/community\.aws/pull/2304)\)\.

<a id="community-dns-3"></a>
#### community\.dns

* Ansible\-core versions before 2\.17 are no longer supported by the collection\. This also means that all Python versions before 3\.8 are no longer supported \([https\://github\.com/ansible\-collections/community\.dns/pull/317](https\://github\.com/ansible\-collections/community\.dns/pull/317)\)\.

<a id="community-general-7"></a>
#### community\.general

* Since community\.general 13\.0\.0\, all module utils\, plugin utils\, and doc fragments contained in this collection are private to the collection\. This means that if another collection wants to use these\, there is no longer any guarantee that there are no breaking changes\, even in bugfix releases\. This has no practical impact on any other use of the collection\, that is\, everyone using modules or plugins from the collections will not notice any difference \([https\://github\.com/ansible\-collections/community\.general/issues/11312](https\://github\.com/ansible\-collections/community\.general/issues/11312)\, [https\://github\.com/ansible\-collections/community\.general/pull/11896](https\://github\.com/ansible\-collections/community\.general/pull/11896)\)\.
* The collection no longer supports ansible\-core 2\.17 \([https\://github\.com/ansible\-collections/community\.general/pull/11906](https\://github\.com/ansible\-collections/community\.general/pull/11906)\)\.
* all lookup plugins \- if a keyword argument <code>\_terms</code> is passed\, the plugin rejects the call and tells the user to use positional arguments instead\. <code>\_terms</code> was never used\, and is used in documentation as a placeholder for positional arguments \([https\://github\.com/ansible\-collections/community\.general/pull/12060](https\://github\.com/ansible\-collections/community\.general/pull/12060)\)\.
* github\_app\_access\_token lookup plugin \- the plugin no longer accepts positional arguments\. They were never used anyway \([https\://github\.com/ansible\-collections/community\.general/pull/12060](https\://github\.com/ansible\-collections/community\.general/pull/12060)\)\.
* github\_repo \- the default for the <code>force\_defaults</code> option changed from <code>true</code> to <code>false</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* onepassword\* lookup plugins \- drop support for <code>op</code> version 1 \([https\://github\.com/ansible\-collections/community\.general/pull/12061](https\://github\.com/ansible\-collections/community\.general/pull/12061)\)\.
* random\_pet lookup plugin \- the plugin no longer accepts positional arguments\. They were never used anyway \([https\://github\.com/ansible\-collections/community\.general/pull/12060](https\://github\.com/ansible\-collections/community\.general/pull/12060)\)\.
* random\_string lookup plugin \- the plugin no longer accepts positional arguments\. They were never used anyway \([https\://github\.com/ansible\-collections/community\.general/pull/12060](https\://github\.com/ansible\-collections/community\.general/pull/12060)\)\.
* random\_words lookup plugin \- the plugin no longer accepts positional arguments\. They were never used anyway \([https\://github\.com/ansible\-collections/community\.general/pull/12060](https\://github\.com/ansible\-collections/community\.general/pull/12060)\)\.
* rocketchat \- the default for the <code>is\_pre740</code> option changed from <code>true</code> to <code>false</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.

<a id="community-mysql-1"></a>
#### community\.mysql

* All modules and plugins have been removed from this collection\. They have been migrated to the [ansible\.mysql](https\://galaxy\.ansible\.com/ui/repo/published/ansible/mysql/) collection\. Redirections have been provided\.
  Please install <code>ansible\.mysql</code> and adjust the FQCNs in your playbooks \(<code>community\.mysql\.mysql\_info</code> → <code>ansible\.mysql\.mysql\_info</code>\)\.
* Update imports from ansible\.module\_utils\.six to use their python3 equivalent\. This change will make this collection incompatible for managed hosts on python2\.7\.

<a id="community-proxmox-2"></a>
#### community\.proxmox

* proxmox\_pool\_member \- move <em class="title-reference">member</em> parameter to a <em class="title-reference">members</em> list to manage multiple pool members at once\. Add a new <em class="title-reference">exclusive</em> parameter to switch between full and incremental mode \([https\://github\.com/ansible\-collections/community\.proxmox/pull/373](https\://github\.com/ansible\-collections/community\.proxmox/pull/373) / issue [https\://github\.com/ansible\-collections/community\.proxmox/issues/320](https\://github\.com/ansible\-collections/community\.proxmox/issues/320)\)\.

<a id="dellemc-enterprise-sonic-1"></a>
#### dellemc\.enterprise\_sonic

* sonic\_qos\_wred \- Add support for yellow and red colors \([https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/574](https\://github\.com/ansible\-collections/dellemc\.enterprise\_sonic/pull/574)\)\.

<a id="hitachivantara-vspone-block-2"></a>
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

<a id="netbox-netbox-1"></a>
#### netbox\.netbox

* This changes the behavior for generating slugs\. If you were relying on the previous behavior\, you need to be aware that this behavior has changed\.

<a id="splunk-es-6"></a>
#### splunk\.es

* Removed deprecated modules that were scheduled for removal on 2024\-09\-01
* adaptive\_response\_notable\_event \- Use splunk\.es\.splunk\_adaptive\_response\_notable\_events instead
* correlation\_search \- Use splunk\.es\.splunk\_correlation\_searches instead
* data\_input\_monitor \- Use splunk\.es\.splunk\_data\_inputs\_monitor instead
* data\_input\_network \- Use splunk\.es\.splunk\_data\_inputs\_network instead

<a id="deprecated-features-2"></a>
### Deprecated Features

* The <code>netapp\.cloudmanager</code> collection is considered unmaintained and will be removed from Ansible 15 if no one starts maintaining it again before Ansible 15\.
  See [Collections Removal Process for unmaintained collections](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#unmaintained\-collections) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/44891](https\://forum\.ansible\.com/t/44891)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install netapp\.cloudmanager</code>\.
* The collection <code>community\.mysql</code> was renamed to <code>ansible\.mysql</code>\.
  For now both collections are included in Ansible\.
  The content in <code>community\.mysql</code> has been replaced by deprecated redirects in Ansible 14\.0\.0\.
  The collection will be completely removed from Ansible 17\.
  Please update your FQCNs from <code>community\.mysql</code> to <code>ansible\.mysql</code> \([https\://forum\.ansible\.com/t/45798](https\://forum\.ansible\.com/t/45798)\)\.
* The cyberark\.pas collection will be removed from Ansible 15 due to violations of the Ansible inclusion requirements\.
  The collection has violated the inclusion requirements multiple times\, including those surrounding repository management\. The collection maintainers did not respond to the latest violation report\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/45816](https\://forum\.ansible\.com/t/45816)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install cyberark\.pas</code>\.

<a id="ansible-core-10"></a>
#### Ansible\-core

* The <code>get\_all\_subclasses\(\)</code> function from <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.24\. Use <code>get\_all\_subclasses\(\)</code> from <code>ansible\.module\_utils\.common\.\_utils</code> instead\.
* The <code>get\_platfrom\(\)</code> function from <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.24\. Use <code>platform\.system\(\)</code> from the Python standard library instead\.
* The <code>load\_platform\_subclass\(\)</code> function from <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.24\. Use <code>get\_platform\_subclass\(\)</code> from <code>ansible\.module\_utils\.common\.sys\_info</code> instead\.
* <code>PluginLoader</code> \- Deprecate unused <code>aliases</code> attribute\. Plugins in a collection should define aliases in the <code>meta/runtime\.yml</code> file using the <code>redirect</code> field instead\.
* <code>ansible\.module\_utils\.six</code> \- The <code>six</code> compatibility library provided at <code>ansible\.module\_utils\.six</code> is deprecated\, and planned for removal in ansible\-core 2\.24
* apt\_key \- deprecate in favor of deb822\_repository\.
* apt\_repository \- deprecate in favor of deb822\_repository\.
* connection plugins \- Added a soft deprecation on the connection attributes <code>has\_native\_async</code> and <code>always\_pipeline\_modules</code>\. Connection plugins that wish to apply custom behaviour around pipelining should instead override the method <code>is\_pipelining\_enabled\(self\, wrap\_async\=False\)</code> added in Ansible 2\.19\. For backwards compatibility no runtime deprecation warning is emitted but will be in the future\.
* task result \- Inferred task failure from a non\-zero <code>rc</code> key and absence of a <code>failed</code> key will be deprecated in Ansible Core 2\.22\. Actions and modules must explicitly communicate failure by setting the <code>failed</code> key\, using APIs that do so\, or raising an unhandled exception\. In future releases\, the <code>rc</code> key will receive no special handling during task result processing\.

<a id="amazon-aws-4"></a>
#### amazon\.aws

* aws\_ec2 \- the <code>tags</code> host variable has been deprecated to avoid conflicts with Ansible reserved variable names and will be removed in a release after 2026\-12\-01\. Use <code>ec2\_tags</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2847](https\://github\.com/ansible\-collections/amazon\.aws/pull/2847)\)\.
* aws\_ec2 \- the <code>use\_contrib\_script\_compatible\_ec2\_tag\_keys</code> option has been deprecated and will be removed in a release after 2026\-12\-01\. Use the <code>ec2\_tags</code> structure instead\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2854](https\://github\.com/ansible\-collections/amazon\.aws/pull/2854)\)
* aws\_ec2 \- the <code>use\_contrib\_script\_compatible\_sanitization</code> option has been deprecated and will be removed in a release after 2026\-12\-01\. Use Ansible\'s default group name sanitization instead\. \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2854](https\://github\.com/ansible\-collections/amazon\.aws/pull/2854)\)
* aws\_rds \- the <code>tags</code> host variable has been deprecated to avoid conflicts with Ansible reserved variable names and will be removed in a release after 2026\-12\-01\. Use <code>rds\_tags</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2847](https\://github\.com/ansible\-collections/amazon\.aws/pull/2847)\)\.
* ec2\_vpc\_dhcp\_option \- the <code>dhcp\_config</code> return value has been deprecated and will be removed in a release after 2026\-12\-01\. Use <code>dhcp\_options</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* ec2\_vpc\_dhcp\_option\_info \- the <code>dhcp\_config</code> return value has been deprecated and will be removed in a release after 2026\-12\-01\. Use <code>dhcp\_options</code> instead \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* route53 \- the <code>region</code> parameter for latency\-based routing has been deprecated and will be removed in a release after 2027\-06\-01\. The <code>routing\_region</code> parameter behaves exactly as <code>region</code> behaves today and should be used instead \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2893](https\://github\.com/ansible\-collections/amazon\.aws/issues/2893)\)\.
* route53 \- the <code>values</code> key in the <code>resource\_record\_sets</code> return value has been deprecated in favor of <code>record\_values</code> for Jinja2 compatibility\. The <code>values</code> key will be removed in a release after 2026\-12\-01 \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.

<a id="ansible-netcommon-3"></a>
#### ansible\.netcommon

* network\_cli \- The in\-collection paramiko support \(used when ssh\_type is paramiko\) is a compatibility layer for environments where ansible\-core\'s paramiko connection is no longer available\. This layer is deprecated and will be removed in a release after 2028\-02\-01\. Migrate to ssh\_type\=libssh by installing the ansible\-pylibssh package\.

<a id="arista-eos-2"></a>
#### arista\.eos

* The <code>src</code> parameter\'s automatic Jinja2 template processing is deprecated and will be removed in march 2028 from eos\_config module
* Use the <code>content</code> parameter with <code>ansible\.builtin\.template</code> lookup instead\.

<a id="cisco-ios-2"></a>
#### cisco\.ios

* ios\_config \- The <code>src</code> parameter\'s automatic Jinja2 template processing is deprecated and will be removed in March 2028\. Use the <code>content</code> parameter with <code>ansible\.builtin\.template</code> lookup instead\.

<a id="cisco-iosxr-2"></a>
#### cisco\.iosxr

* The <code>src</code> parameter\'s automatic Jinja2 template processing is deprecated and will be removed in March 2028 from iosxr\_config module\. Use the <code>content</code> parameter with <code>ansible\.builtin\.template</code> lookup instead\.

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* The <code>src</code> parameter\'s automatic Jinja2 template processing is deprecated and will be removed in March 2028 from nxos\_config module
* Use the <code>content</code> parameter with <code>ansible\.builtin\.template</code> lookup instead\.

<a id="community-aws-5"></a>
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

<a id="community-general-8"></a>
#### community\.general

* aix\_devices \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_filesystem \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_inittab \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_lvg \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* aix\_lvol \- module is superseded by equivalent in <code>ibm\.power\_aix</code> collection\. It will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11290](https\://github\.com/ansible\-collections/community\.general/issues/11290)\, [https\://github\.com/ansible\-collections/community\.general/pull/11540](https\://github\.com/ansible\-collections/community\.general/pull/11540)\)\.
* datadog\_monitor \- the <code>mute</code> and <code>unmute</code> states are deprecated and will be removed in community\.general 15\.0\.0\; use the <code>community\.general\.datadog\_downtime</code> module to manage monitor downtimes instead \([https\://github\.com/ansible\-collections/community\.general/issues/1535](https\://github\.com/ansible\-collections/community\.general/issues/1535)\, [https\://github\.com/ansible\-collections/community\.general/pull/11988](https\://github\.com/ansible\-collections/community\.general/pull/11988)\)\.
* dconf \- deprecate fallback mechanism when <code>gi\.repository</code> is not available\; fallback will be removed in community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11088](https\://github\.com/ansible\-collections/community\.general/pull/11088)\)\.
* installp \- deprecated and scheduled for removal in community\.general 15\.0\.0\. Use <code>ibm\.power\_aix\.installp</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/11910](https\://github\.com/ansible\-collections/community\.general/pull/11910)\)\.
* layman \- ClearLinux was made EOL in July 2025\.\; the module will be removed from community\.general 15\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11087](https\://github\.com/ansible\-collections/community\.general/pull/11087)\)\.
* layman \- Gentoo deprecated <code>layman</code> in mid\-2023\; the module will be removed from community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11070](https\://github\.com/ansible\-collections/community\.general/pull/11070)\)\.
* loganalytics callback plugin \- is deprecated in favor of <code>community\.general\.loganalytics\_ingestion</code> due to upcoming API changes in Azure Monitor \([https\://github\.com/ansible\-collections/community\.general/pull/11505](https\://github\.com/ansible\-collections/community\.general/pull/11505)\)\.
* monit \- support for Monit version 5\.18 or older is deprecated and will be removed in community\.general 14\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/pull/11254](https\://github\.com/ansible\-collections/community\.general/pull/11254)\)\.
* pfexec become plugin \- the default value of the <code>wrap\_exe</code> option will change from <code>false</code> to <code>true</code> in community\.general 14\.0\.0\. The current default only works in very limited cases because <code>pfexec</code> does not interpret shell constructs internally\. Set <code>wrap\_exe</code> explicitly to silence the deprecation warning \([https\://github\.com/ansible\-collections/community\.general/pull/11623](https\://github\.com/ansible\-collections/community\.general/pull/11623)\)\.
* puppet \- the <code>timeout</code> parameter is deprecated and will be removed in community\.general 14\.0\.0\. \([https\://github\.com/ansible\-collections/community\.general/pull/11658](https\://github\.com/ansible\-collections/community\.general/pull/11658)\)\.

<a id="community-mysql-2"></a>
#### community\.mysql

* All modules in this collection have been deprecated and will be removed in version 5\.0\.0\. The content has been moved to the <code>ansible\.mysql</code> collection as\-is\. Please use <code>ansible\.mysql</code> instead\. After installing it\, change FQCN parts in module names in your playbooks from <code>community\.mysql</code> to <code>ansible\.mysql</code>\, for example\, <code>community\.mysql\.mysql\_info</code> to <code>ansible\.mysql\.mysql\_info</code>\.

<a id="community-proxmox-3"></a>
#### community\.proxmox

* proxmox \- Certificate verification default changes from <code>false</code> to <code>true</code> with version 2\.0\.0 \([https\://github\.com/ansible\-collections/community\.proxmox/pull/256](https\://github\.com/ansible\-collections/community\.proxmox/pull/256)\)\.

<a id="community-routeros-3"></a>
#### community\.routeros

* api\_find\_and\_modify \- the current defaults for <code>ignore\_dynamic</code> and <code>ignore\_builtin</code> \(both <code>false</code>\) have been deprecated and will change to <code>true</code> in community\.routeros 4\.0\.0\. To avoid deprecation messages\, please set the value explicitly to <code>true</code> or <code>false</code>\, if you have not already done so\. We recommend to set them to <code>true</code>\, unless you have a good reason to set them to <code>false</code> \([https\://github\.com/ansible\-collections/community\.routeros/pull/399](https\://github\.com/ansible\-collections/community\.routeros/pull/399)\)\.
* api\_modify \- all existing <code>numbers</code> fields are deprecated for writing and support for them will be removed in community\.routeros 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.routeros/pull/460](https\://github\.com/ansible\-collections/community\.routeros/pull/460)\)\.
* api\_modify \- in <code>routing bfd configuration</code>\, the fields <code>copy\-from</code> and <code>place\-before</code> are deprecated for writing and support for them will be removed in community\.routeros 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.routeros/pull/460](https\://github\.com/ansible\-collections/community\.routeros/pull/460)\)\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* datacenter\_info \- The <code>hcloud\_datacenter\_info\[\]\.server\_types</code> return value is deprecated and will be removed after 1 October 2026\. Please use the <code>hcloud\_server\_type\_info\[\]\.locations\[\]\.available</code> return value instead\.
* hcloud inventory \- The <code>hcloud\_datacenter</code> host variable is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_location</code> host variable instead\.
* network\_info \- The <code>hcloud\_network\_info\[\]\.servers\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_network\_info\[\]\.servers\[\]\.location</code> return value instead\.
* primary\_ip \- The <code>datacenter</code> argument is deprecated and will be removed after 1 July 2026\. Please use the <code>location</code> argument instead\.
* primary\_ip \- The <code>hcloud\_primary\_ip\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_primary\_ip\.location</code> return value instead\.
* primary\_ip\_info \- The <code>hcloud\_primary\_ip\_info\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_primary\_ip\_info\[\]\.location</code> return value instead\.
* server \- The <code>datacenter</code> argument is deprecated and will be removed after 1 July 2026\. Please use the <code>location</code> argument instead\.
* server \- The <code>hcloud\_server\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_server\.location</code> return value instead\.
* server\_info \- The <code>hcloud\_server\_info\[\]\.datacenter</code> return value is deprecated and will be removed after 1 July 2026\. Please use the <code>hcloud\_server\_info\[\]\.location</code> return value instead\.

<a id="hitachivantara-vspone-block-3"></a>
#### hitachivantara\.vspone\_block

* The old parameter names renamed in this release are retained as aliases for backward compatibility but will be removed in the next major release\. Affected parameters across modules are \- \"start\_ldev\"\, \"end\_ldev\"\, \"parity\_groups\"\, \"ports\"\, \"port\" \(hv\_resource\_group\, hv\_resource\_group\_facts\)\, \"ports\"\, \"port\" \(hv\_storage\_port\, hv\_storage\_port\_facts\)\, \"mirror\_unit\" \(hv\_sds\_block\_journal\)\, \"nick\_name\"\, \"should\_delete\_all\_ldevs\" \(hv\_hg\, hv\_iscsi\_target\)\, \"nick\_name\" \(hv\_hg\_facts\, hv\_iscsi\_target\_facts\, hv\_sds\_block\_compute\_port\, hv\_vsp\_one\_server\, hv\_vsp\_one\_server\_facts\, hv\_vsp\_one\_server\_hba\_facts\)\, \"parity\_group\" \(hv\_ldev\, hv\_ldev\_facts\)\, \"remote\_ip\_address\" \(hv\_sds\_block\_remote\_iscsi\_port\)\, \"start\_volume\_id\" \(hv\_vsp\_one\_volume\_facts\)\, \"mirror\_unit\_id\"\, \"primary\_journal\_pool\"\, \"secondary\_journal\_pool\" \(hv\_hur\)\, \"mirror\_unit\_id\"\, \"pvol\_status\"\, \"svol\_status\"\, \"primary\_storage\_serial\"\, \"secondary\_storage\_serial\"\, \"primary\_journal\_pool\"\, \"secondary\_journal\_pool\" \(hv\_hur\_facts\)\, \"mu\_number\" \(hv\_gad\)\, \"pvol\_status\"\, \"svol\_status\"\, \"storage\_serial\_number\" \(hv\_truecopy\, hv\_truecopy\_facts\, hv\_hur\)\, \"secondary\_storage\_serial\" \(hv\_hur\)\, \"primary\_volume\_storage\_id\"\, \"secondary\_volume\_storage\_id\" \(hv\_gad\, hv\_gad\_facts\)\, \"mirror\_unit\_id\" \(hv\_snapshot\, hv\_snapshot\_group\, hv\_snapshot\_facts\, hv\_snapshot\_group\_facts\)\, \"pvol\_host\_groups\"\, \"pvol\_iscsi\_targets\"\, \"pvol\_nvm\_subsystem\_name\"\, \"svol\_host\_groups\"\, \"svol\_iscsi\_targets\"\, \"svol\_nvm\_subsystem\_name\"\, \"pvol\_processing\_status\"\, \"svol\_processing\_status\" \(hv\_snapshot\_facts\)\, \"pvol\_mu\_number\"\, \"copy\_pace\_track\_size\" \(hv\_shadow\_image\_pair\)\, \"mirror\_unit\_id\"\, \"pvol\_host\_groups\"\, \"pvol\_iscsi\_targets\"\, \"pvol\_nvm\_subsystem\_name\"\, \"svol\_host\_groups\"\, \"svol\_iscsi\_targets\"\, \"svol\_nvm\_subsystem\_name\" \(hv\_shadow\_image\_pair\_facts\)\.

<a id="kubernetes-core-4"></a>
#### kubernetes\.core

* helm \- the <code>status\.values</code> return value has been deprecated and will be removed in a release after 2027\-01\-08\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* helm\_info \- the <code>status\.values</code> return value has been deprecated and will be removed in a release after 2027\-01\-08\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.

<a id="vmware-vmware-rest-5"></a>
#### vmware\.vmware\_rest

* Deprecate modules that have been moved to the new vmware\.vmware collection\. Includes vcenter\_vm\_guest\_customization\, vcenter\_vm\_hardware\_adapter\_sata\, vcenter\_vm\_hardware\_adapter\_scsi\, vcenter\_vm\_hardware\_cdrom\, vcenter\_vm\_hardware\_cpu\, vcenter\_vm\_hardware\_disk\, vcenter\_vm\_hardware\_ethernet\, vcenter\_vm\_hardware\_memory\, vcenter\_vm

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The awx\.awx collection has been removed from Ansible 14\.
  The collection is undergoing a heavy [refactoring](https\://forum\.ansible\.com/t/7404) and currently does not align with the standards for the community package\.
  See [the removal discussion](https\://forum\.ansible\.com/t/44706) for details\.
  Users can still install this collection with <code>ansible\-galaxy collection install awx\.awx</code>\.
* The deprecated <code>cisco\.dnac</code> collection has been removed \([https\://forum\.ansible\.com/t/45609](https\://forum\.ansible\.com/t/45609)\)\.
* The deprecated <code>junipernetworks\.junos</code> collection has been removed \([https\://forum\.ansible\.com/t/44869](https\://forum\.ansible\.com/t/44869)\)\.

<a id="ansible-core-11"></a>
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

<a id="community-dns-4"></a>
#### community\.dns

* Drop support for dnspython \< 2\.0\.0\. All modules and plugins that require dnspython will no longer work with older versions \([https\://github\.com/ansible\-collections/community\.dns/pull/323](https\://github\.com/ansible\-collections/community\.dns/pull/323)\)\.

<a id="community-general-9"></a>
#### community\.general

* atomic\_container \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* atomic\_host \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* atomic\_image \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* catapult \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* cloud module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* cpanm \- the <code>mode\=compatibility</code> is no longer available\. Migrate to <code>mode\=new</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* database module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* dimensiondata \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* dimensiondata module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* dimensiondata\_network \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* dimensiondata\_vlan \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* dimensiondata\_wait \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* django module utils \- the deprecated <code>database</code>\, <code>noinput</code>\, <code>dry\_run</code>\, and <code>check</code> parameters for the Django runner have been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* hiera lookup plugin \- the lookup has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* keycloak module utils \- the deprecated <code>KeycloakAPI\.add\_user\_in\_group\(\)</code> method has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* known\_hosts module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* locale\_gen \- support for the <code>ubuntu\_legacy</code> mechanism has been removed\. Only the <code>glibc</code> mechanism is supported by the module anymore \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oci\_vcn \- the module has been removed\. Use <code>oracle\.oci\.oci\_network\_vcn</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone\_firewall\_policy \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone\_load\_balancer \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone\_monitoring\_policy \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone\_private\_network \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone\_public\_ip \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oneandone\_server \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle\.oci\_utils module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle\_creatable\_resource \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle\_display\_name\_option \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle\_name\_option \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle\_tags \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* oracle\_wait\_options \- the doc fragment has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* pipx module utils \- the deprecated <code>make\_process\_list\(\)</code> function has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* pushbullet \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* saslprep module utils \- the module utils has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* sensu\_check \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* sensu\_client \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* sensu\_handler \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* sensu\_silence \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* sensu\_subscription \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* spotinst\_aws\_elastigroup \- the module has been removed\. Use <code>spot\.cloud\_modules\.aws\_elastigroup</code> instead \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.
* typetalk \- the module has been removed \([https\://github\.com/ansible\-collections/community\.general/pull/11834](https\://github\.com/ansible\-collections/community\.general/pull/11834)\)\.

<a id="community-mysql-3"></a>
#### community\.mysql

* All modules and plugins have been removed from this collection\. They have been migrated to the [ansible\.mysql](https\://galaxy\.ansible\.com/ui/repo/published/ansible/mysql/) collection\. Redirections have been provided\.
  Please install <code>ansible\.mysql</code> and adjust the FQCNs in your playbooks \(<code>community\.mysql\.mysql\_info</code> → <code>ansible\.mysql\.mysql\_info</code>\)\.

<a id="hitachivantara-vspone-block-4"></a>
#### hitachivantara\.vspone\_block

* Removed playbooks \"ddp\_pool\.yml\" and \"ddp\_pool\_facts\.yml\"\.

<a id="splunk-es-7"></a>
#### splunk\.es

* adaptive\_response\_notable\_event module has been removed\. Use splunk\.es\.splunk\_adaptive\_response\_notable\_events resource module instead\.
* correlation\_search module has been removed\. Use splunk\.es\.splunk\_correlation\_searches resource module instead\.
* correlation\_search\_info module has been removed\. Use splunk\.es\.splunk\_correlation\_search\_info instead\.
* data\_input\_monitor module has been removed\. Use splunk\.es\.splunk\_data\_inputs\_monitor resource module instead\.
* data\_input\_network module has been removed\. Use splunk\.es\.splunk\_data\_inputs\_network resource module instead\.

<a id="security-fixes-2"></a>
### Security Fixes

<a id="amazon-aws-5"></a>
#### amazon\.aws

* arn \- fix potential ReDoS vulnerability in ARN parsing regex by using negated character class instead of non\-greedy quantifier \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2884](https\://github\.com/ansible\-collections/amazon\.aws/pull/2884)\)\.
* ec2\_security\_group \- fix potential ReDoS vulnerability in security group ID parsing regex by using negated character classes and adding end anchor \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2884](https\://github\.com/ansible\-collections/amazon\.aws/pull/2884)\)\.

<a id="ansible-windows-6"></a>
#### ansible\.windows

* win\_dns\_record \- Fixed a security risk where <code>AllowUpdateAny</code> was hardcoded for non\-SRV records\, allowing any authenticated user to update DNS records\. Added a new parameter <code>allow\_update\_any</code> which defaults to <code>false</code> \([https\://issues\.redhat\.com/browse/ACA\-5193](https\://issues\.redhat\.com/browse/ACA\-5193)\)\.

<a id="kubernetes-core-5"></a>
#### kubernetes\.core

* Selectively redact sensitive info from kubeconfig instead of applying blanket <code>no\_log\=True</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1014](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1014)\)\.

<a id="bugfixes-2"></a>
### Bugfixes

<a id="ansible-core-12"></a>
#### Ansible\-core

* Fix Windows LIB env var corruption \([https\://github\.com/ansible\-collections/ansible\.windows/issues/297](https\://github\.com/ansible\-collections/ansible\.windows/issues/297)\)\.
* Fix <code>AnsibleModule\.human\_to\_bytes\(\)</code>\, which was never adjusted after the standalone <code>human\_to\_bytes\(\)</code> got a new parameter <code>default\_unit</code> \([https\://github\.com/ansible/ansible/pull/85259](https\://github\.com/ansible/ansible/pull/85259)\)\.
* Fix <code>validate\_argspec</code> when tags are defined on the play\. The <code>always</code> tag is only added if the play has no tags\.
* Fix interpreter discovery on delegated <code>async</code> tasks \([https\://github\.com/ansible/ansible/issues/86491](https\://github\.com/ansible/ansible/issues/86491)\)
* Fix source metadata validation \([https\://github\.com/ansible/ansible/pull/86320](https\://github\.com/ansible/ansible/pull/86320)\)\.
* Fix up <code>powershell</code> shell commands when using a connection plugin that does not support stdin/pipeline input \- [https\://github\.com/ansible/ansible/issues/86397](https\://github\.com/ansible/ansible/issues/86397)
* Fix up the Action plugin <code>\_make\_tmp\_path</code> error to only include the command run rather than the shell\'s dataclass repr from <code>mkdtemp</code>\.
* Variable loading now uses file source instead of variables when invalidly formmated vars file is loaded\.
* Windows \- ignore temporary file cleanup warning when using AnsibleModule to compile C\# utils\. This should reduce the number of warnings that can safely be ignored when running PowerShell modules \- [https\://github\.com/ansible/ansible/issues/85976](https\://github\.com/ansible/ansible/issues/85976)
* <code>\-\-start\-at\-task</code> \- fix starting at the requested task instead of starting at the next block or play\. Play level tasks run first\. \([https\://github\.com/ansible/ansible/issues/86268](https\://github\.com/ansible/ansible/issues/86268)\)
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
* ansible\-test remote alias \- Alias values for <code>\-\-controller</code> and <code>\-\-target</code> are properly resolved for <code>remote</code>\. Previously\, remote alias values \(e\.g\. <code>fedora/latest</code>\) resolved to the correct name only for the legacy <code>\-\-remote</code> arg\, failing with an unknown image error for the newer args\.
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
* git \- use the branch configured in <code>\.gitmodules</code> or the remote HEAD instead of hardcoding <code>master</code> when <code>track\_submodules\=yes</code> \([https\://github\.com/ansible/ansible/issues/77691](https\://github\.com/ansible/ansible/issues/77691)\)\.
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
* task results \- The <code>invocation</code> item result key omitted from registered values for looped task results\, unless enabled via <code>INJECT\_INVOCATION</code>\. Previously\, it was deleted from registered non\-loop results and only available to callbacks\.
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

<a id="amazon-aws-6"></a>
#### amazon\.aws

* Add retry state for 404 in S3 waiters to avoid failure on s3 bucket 404 if bucket is not immediately visible \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2984\#issuecomment\-4603538914](https\://github\.com/ansible\-collections/amazon\.aws/issues/2984\#issuecomment\-4603538914)\) \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2987](https\://github\.com/ansible\-collections/amazon\.aws/pull/2987)\)
* autoscaling\_group \- Fixed duplicate default\_cooldown assignment in properties dict \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2923](https\://github\.com/ansible\-collections/amazon\.aws/pull/2923)\)\.
* aws\_ssm \- Fixed connection being re\-established on every loop iteration\. The plugin now properly establishes a single connection for a loop \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2869](https\://github\.com/ansible\-collections/amazon\.aws/pull/2869)\)\.
* connection/aws\_ssm \- fixed ReferenceError in aws\_ssm connection plugin destructor during interpreter shutdown \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2728](https\://github\.com/ansible\-collections/amazon\.aws/issues/2728)\)\.
* elb\_application\_lb \- Listener rules are now returned sorted by priority with the default rule appearing last \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2939](https\://github\.com/ansible\-collections/amazon\.aws/issues/2939)\)\.
* elb\_application\_lb \- fixed comparison of multi\-rule default actions to properly handle the <code>Order</code> field when determining if listener modifications are needed \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2537](https\://github\.com/ansible\-collections/amazon\.aws/issues/2537)\)\.
* elb\_application\_lb \- fixed error where creating a new application load balancer with listener rules would fail with <code>Parameter validation failed\: Invalid type for parameter ListenerArn\, value\: None</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2400](https\://github\.com/ansible\-collections/amazon\.aws/issues/2400)\)\.
* elb\_application\_lb\_info \- Listener rules are now returned sorted by priority with the default rule appearing last \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2939](https\://github\.com/ansible\-collections/amazon\.aws/issues/2939)\)\.
* kms\_key \- Fixed parameter reassignment by using passed alias parameter instead of re\-fetching from module params \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2923](https\://github\.com/ansible\-collections/amazon\.aws/pull/2923)\)\.
* lambda\_info \- fixed invalid return value documentation that used dot notation \(<code>function\.TheName</code>\) which cannot be used in Jinja2 templates \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2772](https\://github\.com/ansible\-collections/amazon\.aws/pull/2772)\)\.
* module\_utils/cloudfront\_facts \- fix TypeError in CloudFrontFactsServiceManager\.describe\_cloudfront\_property \([https\://github\.com/ansible\-collections/community\.aws/issues/1915](https\://github\.com/ansible\-collections/community\.aws/issues/1915)\)\.
* s3\_bucket \- fix error when configuring AES256 bucket encryption with <code>bucket\_key\_enabled</code> explicitly set to <code>false</code> \([https\://github\.com/ansible\-collections/amazon\.aws/issues/2734](https\://github\.com/ansible\-collections/amazon\.aws/issues/2734)\)\.
* s3\_object \- fixed error when using PUT with an empty <code>content</code> string \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2810](https\://github\.com/ansible\-collections/amazon\.aws/pull/2810)\)
* s3\_object\_info \- Fixed duplicate dictionary key assignments when retrieving object facts \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2923](https\://github\.com/ansible\-collections/amazon\.aws/pull/2923)\)\.

<a id="ansible-netcommon-4"></a>
#### ansible\.netcommon

* Added support for private key passphrase in libssh connection plugin\, when using encrypted private keys specified by the C\(ansible\_private\_key\_file\) attribute\.
* Adds backward compatibility of handling src attributes\, functional consistency with ansible\-core \>\= 2\.19
* Adds deprecation warning for the jinja2 processing functionality for src attributes\, src attributes in collections would still support considering file path but they would not process template files directly once the functionality is deprecated\.
* Avoid legacy imports deprecated in ansible\-core 2\.20 \([https\://github\.com/ansible\-collections/ansible\.netcommon/pull/720](https\://github\.com/ansible\-collections/ansible\.netcommon/pull/720)\)\.
* Avoid merging module\_defaults for all ansible\.netcommon\.grpc\_\* modules\.
* It is suggested to use ansible\.builtin\.template module to process templates and use the processed template path in src attributes\.
* Set libssh logging level to DEBUG when Ansible verbosity is greater than 3\, to aid in troubleshooting connection issues\.
* filter plugins \- Add plugin\_routing redirects for <code>ipaddr</code>\, <code>ipv4</code>\, and <code>ipv6</code> to <code>ansible\.utils</code> so short names work when <code>ansible\.netcommon</code> is in the play\'s collection list \([https\://github\.com/ansible\-collections/ansible\.utils/issues/404](https\://github\.com/ansible\-collections/ansible\.utils/issues/404)\)\.
* filter plugins \- Convert filter arguments to native Python types before <code>AnsibleArgSpecValidator</code> so filters work with Ansible 2\.19\+ lazy containers that cannot be deep\-copied \(e\.g\. <code>vlan\_parser</code>\, <code>vlan\_expander</code>\, <code>hash\_salt</code>\, <code>type5\_pw</code>\, <code>comp\_type5</code>\, <code>parse\_cli</code>\, <code>parse\_cli\_textfsm</code>\, <code>parse\_xml</code>\, <code>pop\_ace</code>\)\.
* libssh connection \- Fixed test\_libssh\_put\_file unit test so the put\_file code path \(used by net\_put\, copy module\, and other file transfer over libssh\) is properly tested in CI\. The test now sets connection options and mocks Session so put\_file does not trigger a real connection attempt with an unset host \(was failing with \"Hostname required\"\)\.
* network action plugin \- Fall back when remove\_internal\_keys is not importable from ansible\.vars\.clean \(e\.g\. some ansible\-core builds\)\, so direct module execution still cleans module return data\.
* network action plugin \- initialize <code>\_PARSED\_MODULE\_ARGS</code> in <code>DirectExecutionModule\.\_load\_params</code> to avoid <code>AttributeError</code> on ansible\-core 2\.21\+ when <code>fail\_json</code> or <code>exit\_json</code> is called\.
* network\_cli \- Fixed file transfer \(net\_put / net\_get\) when ssh\_type\=libssh\. For put\_file\, no longer call\_connect\_uncached\(\) before delegating to the libssh connection the libssh plugin\'s put\_file\(\) calls \_connect\(\) internally\. For fetch\_file\, call \_connect\(\) then fetch\_file\(\) for libssh instead of \_connect\_uncached\(\)\, so connection caching and the correct flow are used\. Paramiko branch unchanged \(still uses \_connect\_uncached\(\) for scp/sftp\)\.

<a id="ansible-posix-3"></a>
#### ansible\.posix

* acl \- correctly assert needed changes when pointing to a directory and recursive is set to true\.
* ansible\.posix\.authorized\_key \- fixes error on permission denied in authorized\_key module \([https\://github\.com/ansible\-collections/ansible\.posix/issues/462](https\://github\.com/ansible\-collections/ansible\.posix/issues/462)\)\.
* firewalld\_info \- stop returning warnings as return values\; this has been deprecated by ansible\-core \([https\://github\.com/ansible\-collections/ansible\.posix/pull/670](https\://github\.com/ansible\-collections/ansible\.posix/pull/670)\)\.
* mount \- stop returning warnings as return values\; this has been deprecated by ansible\-core \([https\://github\.com/ansible\-collections/ansible\.posix/pull/670](https\://github\.com/ansible\-collections/ansible\.posix/pull/670)\)\.
* patch \- removed use of deprecated <code>\_AnsibleActionDone</code> API \([https\://github\.com/ansible\-collections/ansible\.posix/pull/687](https\://github\.com/ansible\-collections/ansible\.posix/pull/687)\)\.

<a id="ansible-utils-1"></a>
#### ansible\.utils

* Add a cleanup step that removes empty \{\} and \[\] values from lists in keep\_keys\_from\_dict\_n\_list\(\)
* cidr\_merge \- Fix filter failing when used inside a Jinja2 macro called with <code>with context</code> by unwrapping Ansible lazy template lists before validation\.
* cli\_parse \- Honor ttp\_results\.results flat\_list in TTP parser so output is a single\-level list instead of double\-wrapped \([https\://github\.com/ansible\-collections/ansible\.utils/issues/402](https\://github\.com/ansible\-collections/ansible\.utils/issues/402)\)\.
* ipaddress\_utils \- Support Python 3\.14\+ by using the public <code>version</code> attribute instead of the removed private <code>\_version</code> on <code>ipaddress</code> network objects \(bpo\-118710\)\.
* update\_fact \- Use task\_vars at top\-level instead of the deprecated <code>vars</code> key for compatibility with ansible\-core 2\.24 \(ansible/ansible issue

<a id="ansible-windows-7"></a>
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

<a id="arista-eos-3"></a>
#### arista\.eos

* Added runtime routing in <code>meta/runtime\.yml</code> to map old plugin names to the new <code>eos\_</code>\-prefixed ones\.
* Fix eos\_vrf module to properly check existing interface configuration before making changes \([https\://github\.com/ansible\-collections/arista\.eos/issues/546](https\://github\.com/ansible\-collections/arista\.eos/issues/546)\)
* Removed deprecated action plugins for modules that no longer exist \(static\_route\, vlan\, linkagg\, l2\_interface\, l3\_interface\, logging\, interface\, bgp\)\.
* Removed sanity ignore files for EOL ansible\-core versions \(2\.14 through 2\.22\)\.
* Renamed all remaining action plugins with <code>eos\_</code> prefix to follow naming conventions\.
* Trimmed obsolete entries from remaining sanity ignore files\.
* eos\_bgp\_global \- Support specifying both incoming and outgoing route\-maps per BGP neighbor\. Added <code>route\_maps</code> \(list of dicts with <code>name</code> and <code>direction</code>\) so users can set e\.g\. <code>route\-map MAP\_IN in</code> and <code>route\-map MAP\_OUT out</code> for the same neighbor\. The single <code>route\_map</code> option is deprecated in favor of <code>route\_maps</code>\. Fixes [https\://github\.com/ansible\-collections/arista\.eos/issues/538](https\://github\.com/ansible\-collections/arista\.eos/issues/538)\.
* eos\_static\_routes \- Fix issue where <code>state\: replaced</code> did not delete routes not present in the config \([https\://github\.com/ansible\-collections/arista\.eos/issues/532](https\://github\.com/ansible\-collections/arista\.eos/issues/532)\)\.

<a id="cisco-aci-1"></a>
#### cisco\.aci

* Fix allowed ranges of interface option in aci\_interface\_config module\.
* Fix descriptions of options in aci\_maintenance\_policy\.
* Fix querying description in aci\_l4l7\_service\_graph\_template\.

<a id="cisco-ios-3"></a>
#### cisco\.ios

* Fixed delete and purged state function for ios\_bfd\_templates
* action plugins \- Remove orphaned legacy action plugins <code>bgp\.py</code>\, <code>linkagg\.py</code>\, <code>lldp\.py</code> and <code>logging\.py</code> that had no corresponding module\.
* action plugins \- Rename multiple resource module action plugins to use the <code>ios\_</code> prefix to match their module names and fix <code>action\-plugin\-docs</code> sanity failures blocking Automation Hub certification\.
* cisco\.ios\.ios\_acls \- Added support for converting numeric protocol values to real protocol options when gathered from the device\.
* cisco\.ios\.ios\_acls \- Gathered state showing incomplete configuration\.
* cisco\.ios\.ios\_hsrp\_intefaces \- Considers version 1 as default if configuration does not specify version\.
* cisco\.ios\.ios\_hsrp\_intefaces \- Corrects idempotency issue when version is not specified in configuration\.
* cisco\.ios\.ios\_l2\_interfaces \- Moved mode parser to below the trunk parsers\.
* ios\_acls \- Fixed <code>\'int\' object has no attribute \'split\'</code> error when processing ACL configurations with TCP entries\. The parser regex for <code>icmp\_igmp\_protocol</code> could capture trailing numeric values for non\-ICMP/IGMP protocols\. Fixed by restricting <code>icmp\_igmp\_protocol</code> to only apply when the protocol is <code>icmp</code> or <code>igmp</code> in the parser template\, with a defensive type check in facts processing\.
* ios\_config \- Fix multi\-range interface commands for ios\_config module\.
* ios\_snmp\_users \- Fixed authentication option to correctly handle authentication protocol configuration\.
* ios\_static\_routes \- Fix gather crash when \"ip route static bfd\" is present on the device\.
* meta/runtime\.yml \- Add <code>plugin\_routing\.action</code> redirects for all short\-name aliases so alias\-based invocations continue to resolve the renamed action plugins\.
* plugins/action/ios\.py \- Remove unused <code>warnings</code> list and unreachable dead code block that never executed due to <code>warnings</code> always being empty\.
* sanity \- Remove stale <code>action\-plugin\-docs</code> ignore entries and delete <code>ignore\-2\.14\.txt</code> and <code>ignore\-2\.15\.txt</code> as the collection requires <code>ansible\>\=2\.16\.0</code>\.
* terminal\_stderr\_re \- Updated to support variation of command rejected error from appliance\.

<a id="cisco-iosxr-3"></a>
#### cisco\.iosxr

* Fixed iosxr\_user module to correctly handle MD5 hashed passwords when updating user credentials\.
* action plugins \- Remove orphaned legacy action plugins <code>bgp\.py</code>\, <code>interface\.py</code>\, and <code>logging\.py</code> that had no corresponding module\.
* action plugins \- Rename all 32 resource module action plugins to use the <code>iosxr\_</code> prefix to match their module names and fix <code>action\-plugin\-docs</code> sanity failures blocking Automation Hub certification\.
* iosxr\_bgp\_address\_family \- Fixed label generation command handling under <em class="title-reference">address\_family</em> configuration\.
* iosxr\_bgp\_global\, iosxr\_bgp\_templates\, iosxr\_facts \- treat BGP neighbor <code>remote\_as</code> as a string so ASDOT notation \(e\.g\. <code>5467\.8</code> per RFC 5396\) is not coerced to float and rejected during facts or resource validation \([https\://github\.com/ansible\-collections/cisco\.iosxr/issues](https\://github\.com/ansible\-collections/cisco\.iosxr/issues)\)\. This is not a deprecation of <code>remote\_as</code> — existing playbooks passing integer ASPLAIN values \(e\.g\. <code>remote\_as\: 65001</code>\) continue to work because Ansible automatically coerces integers to strings\. However\, the module now returns <code>remote\_as</code> as a string in parsed/gathered facts\, so any playbook assertions comparing <code>remote\_as</code> against an integer literal \(e\.g\. <code>result\.after\.remote\_as \=\= 65001</code>\) should be updated to compare against a string \(<code>\"65001\"</code>\) instead\.
* meta/runtime\.yml \- Add <code>plugin\_routing\.action</code> redirects for all short\-name aliases so alias\-based invocations continue to resolve the renamed action plugins\.
* plugins/action/iosxr\.py \- Remove unused <code>warnings</code> list and unreachable dead code block that never executed due to <code>warnings</code> always being empty\.
* sanity \- Remove 35 stale <code>action\-plugin\-docs</code> ignore entries and delete <code>ignore\-2\.15\.txt</code> as the collection requires <code>ansible\>\=2\.16\.0</code>\.

<a id="cisco-meraki-3"></a>
#### cisco\.meraki

* Fix parameter naming in organizations\_inventory\_claim\.py to use camelCase for consistency with existing code\.
* Fixing problem of naming in organizations\_appliance\_vpn\_third\_party\_vpnpeers\_info\.
* Restructuring README\.md file\.
* administered\_licensing\_subscription\_subscriptions\_bind \- Fixed parameter naming from \'subscription\_id\' to \'subscriptionId\' for proper API compatibility
* devices\_switch\_ports \- Fixed AttributeError crash in <code>update\(\)</code> caused by <code>get\_object\_by\_name</code> returning the full port list instead of <code>None</code> when no port matched by name\. Added <code>isinstance\(prev\_obj\_name\, dict\)</code> guard to prevent calling <code>\.get\(\)</code> on a list\.
* devices\_switch\_ports \- Fixed idempotency regression where the module always reported <code>changed</code> due to <code>serial</code> and <code>portId</code> being incorrectly included in the <code>requires\_update</code> comparison\.
* meraki\.py plugin utils \- Added type checking in has\_diff\_elem2 function to prevent errors when comparing lists of non\-dictionary elements
* networks\_appliance\_content\_filtering \- Enhanced idempotency by extracting category IDs from blockedUrlCategories before comparison
* networks\_appliance\_static\_routes \- Added new plugin\.
* networks\_appliance\_static\_routes\_info \- Added new plugin\.

<a id="cisco-mso-1"></a>
#### cisco\.mso

* Fix updates of multicast\_route\_map\_policy in mso\_schema\_template\_vrf\_rp\.
* Fix updates of multicast\_route\_map\_source\_filter and multicast\_route\_map\_destination\_filter in mso\_schema\_template\_bd\.

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* Fixed nxos\_facts module so it can handle VLAN interface facts without any issue even if addr is not defined
* Fixed nxos\_static\_routes module so to handle replaced and overridden state with vrf configuration\.
* action plugins \- Remove orphaned legacy action plugins <code>acl\_interface\.py acl\.py bgp\_af\.py</code>\, <code>bgp\_neighbor\_af\.py bgp\_neighbor\.py bgp\.py interface\.py l2\_interface\.py l3\_interface\.py</code>\, <code>linkagg\.py lldp\.py logging\.py ntp\_auth\.py ntp\_options\.py ntp\.py ospf\_vrf\.py smu\.py</code>\, <code>snmp\_community\.py snmp\_contact\.py snmp\_host\.py snmp\_location\.py snmp\_traps\.py snmp\_user\.py</code>\, <code>static\_route\.py vlan\.py ospf\.py</code> that had no corresponding module\.
* action plugins \- Rename multiple resource module action plugins to use the <code>nxos\_</code> prefix to match their module names and fix <code>action\-plugin\-docs</code> sanity failures blocking Automation Hub certification\.
* cisco\.nxos\.nxos\_facts \- Fix AttributeError when interface has multiple IPv6 addrs and handle ROW\_addr as list\.
* cisco\.nxos\.nxos\_facts \- Fix handling of facts for httapi type connection\.
* cisco\.nxos\.nxos\_hsrp\_intefaces \- Considers version 1 as default if configuration does not specify version\.
* cisco\.nxos\.nxos\_hsrp\_intefaces \- Corrects idempotency issue when version is not specified in configuration\.
* cisco\.nxos\.nxos\_hsrp\_interfaces \- Fix parsers for preempt and priority
* cisco\.nxos\.nxos\_l2\_interfaces \- Fix cdp\_enable config parsing\.
* cisco\.nxos\.nxos\_l3\_interfaces \- Improved the code logic for handling redirects\.
* cisco\.nxos\.nxos\_snmp\_server \- fixed communities parsing issue
* cisco\.nxos\.nxos\_static\_routes \- Fix facts parser to filter inline VRF routes from global route collection preventing incorrect VRF route deletion\.
* meta/runtime\.yml \- Add <code>plugin\_routing\.action</code> redirects for all short\-name aliases so alias\-based invocations continue to resolve the renamed action plugins\.
* nxos\_l2\_interfaces \- Fix VLAN range sorting to use numeric order instead of lexicographic string sorting\, which caused incorrect range generation \(e\.g\.\, \"1\,10\,100\,11\" instead of \"1\-100\"\)\.
* nxos\_l2\_interfaces \- Fix default allowed VLANs handling \- trunk interfaces now correctly assume 1\-4094 as default when no explicit allowed\_vlans is configured\.
* nxos\_l2\_interfaces \- Fix state handling logic for merged\, replaced\, overridden\, and deleted states to correctly add/remove VLANs based on the desired state\.
* nxos\_l2\_interfaces \- Fix to facts parsing when multiple vlan add lines are sent/parsed\. These lines are now instead merged into a single command first via \_flatten\_vlan function\, and then sent as data to be parsed
* nxos\_static\_routes \- Fixed incorrect deletion of route in VRF even when VRF is not specified\.
* plugins/action/nxos\.py \- Remove unused <code>warnings</code> list and unreachable dead code block that never executed due to <code>warnings</code> always being empty\.

<a id="community-aws-6"></a>
#### community\.aws

* Remove <code>ansible\.module\_utils\.six</code> imports to avoid warnings \([https\://github\.com/ansible\-collections/community\.aws/pull/2338](https\://github\.com/ansible\-collections/community\.aws/pull/2338)\)\.
* ec2\_customer\_gateway \- Fix documentation for the return block \([https\://github\.com/ansible\-collections/community\.aws/pull/2354](https\://github\.com/ansible\-collections/community\.aws/pull/2354)\)\.

<a id="community-crypto-3"></a>
#### community\.crypto

* acme\_\* modules \- adjust OpenSSL RSA private key output parsing to OpenSSL 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1005](https\://github\.com/ansible\-collections/community\.crypto/pull/1005)\)\.
* acme\_\* modules \- improve handling of authz deactivation\, and improve error message in case of bad authz states \([https\://github\.com/ansible\-collections/community\.crypto/pull/998](https\://github\.com/ansible\-collections/community\.crypto/pull/998)\)\.
* acme\_challenge\_cert\_helper \- adjust private key check for new private key types in cryptography 47\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1007](https\://github\.com/ansible\-collections/community\.crypto/pull/1007)\)\.
* crypto\_info\, openssl\_privatekey\, openssl\_privatekey\_pipe \- fix detection of EC support for cryptography 46\.0\.5\+ \([https\://github\.com/ansible\-collections/community\.crypto/pull/981](https\://github\.com/ansible\-collections/community\.crypto/pull/981)\)\.

<a id="community-dns-5"></a>
#### community\.dns

* Update Public Suffix List\.
* converter module utils \- add <code>stacklevel\=2</code> to Python warnings\. This affects third\-party users of the module utils outside this collection \([https\://github\.com/ansible\-collections/community\.dns/pull/310](https\://github\.com/ansible\-collections/community\.dns/pull/310)\)\.
* hetzner\_\* modules and hetzner\_dns\_records inventory plugin \- retry on network problems and certain HTTP codes \(502\, 503\, 504\) \([https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hetzner\_dns\_record\_set\, hosttech\_dns\_record\_set \- fix <code>on\_existing \!\= \'replace\'</code> mis\-triggering when <code>state\=absent</code> and the values to delete do not show up in the list of records \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* hetzner\_dns\_record\_sets \- when doing batch updates\, do not request status updates for too many actions at once \([https\://github\.com/ansible\-collections/community\.dns/issues/312](https\://github\.com/ansible\-collections/community\.dns/issues/312)\, [https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hosttech\_\* modules and hosttech\_dns\_records inventory plugin \- when using the JSON API\, retry on network problems and certain HTTP codes \(502\, 503\, 504\) \([https\://github\.com/ansible\-collections/community\.dns/pull/313](https\://github\.com/ansible\-collections/community\.dns/pull/313)\)\.
* hosttech\_record\_sets\, hetzner\_record\_sets \- ensure stable order also with Python \< 3\.6 \([https\://github\.com/ansible\-collections/community\.dns/pull/301](https\://github\.com/ansible\-collections/community\.dns/pull/301)\)\.
* lookup\_rfc8427 lookup plugin \- remove unused code \([https\://github\.com/ansible\-collections/community\.dns/pull/308](https\://github\.com/ansible\-collections/community\.dns/pull/308)\)\.
* nameserver\_info\, nameserver\_record\_info\, wait\_for\_txt \- fix handling of DNSPython <code>Nameserver</code> objects when default resolver addresses are used \([https\://github\.com/ansible\-collections/community\.dns/pull/321](https\://github\.com/ansible\-collections/community\.dns/pull/321)\)\.
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

<a id="community-general-10"></a>
#### community\.general

* \_filelock module utils \- add type hints\. Fix bug if <code>set\_lock\(\)</code> is called with <code>lock\_timeout\=None</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11222](https\://github\.com/ansible\-collections/community\.general/pull/11222)\)\.
* \_filelock module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* aerospike\_migrations \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* aix\_filesystem \- remove compatibility code for ancient Python versions \([https\://github\.com/ansible\-collections/community\.general/pull/11232](https\://github\.com/ansible\-collections/community\.general/pull/11232)\)\.
* aix\_lvol \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ali\_instance \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* ali\_instance \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ali\_instance\_info \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* alternatives \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* ansible\_type plugin utils \- avoid potential concatenation of non\-strings when <code>alias</code> has non\-string values \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* ansible\_type test plugin \- fix parameter checking \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* apache2\_module \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* apk \- fix <code>packages</code> return value for apk\-tools \>\= 3 \(Alpine 3\.23\) \([https\://github\.com/ansible\-collections/community\.general/issues/11264](https\://github\.com/ansible\-collections/community\.general/issues/11264)\)\.
* apk \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* apt\_repo \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.
* apt\_rpm \- do not fail when <code>update\_kernel</code> finds no new kernel available \([https\://github\.com/ansible\-collections/community\.general/issues/10055](https\://github\.com/ansible\-collections/community\.general/issues/10055)\, [https\://github\.com/ansible\-collections/community\.general/pull/11949](https\://github\.com/ansible\-collections/community\.general/pull/11949)\)\.
* apt\_rpm \- fix upgrade of local RPM not present in repository \([https\://github\.com/ansible\-collections/community\.general/issues/9161](https\://github\.com/ansible\-collections/community\.general/issues/9161)\, [https\://github\.com/ansible\-collections/community\.general/pull/12039](https\://github\.com/ansible\-collections/community\.general/pull/12039)\)\.
* apt\_rpm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* apt\_rpm \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* apt\_rpm \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* awall \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11784](https\://github\.com/ansible\-collections/community\.general/pull/11784)\)\.
* beadm \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* bower \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11783](https\://github\.com/ansible\-collections/community\.general/pull/11783)\)\.
* btrfs module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* btrfs module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* btrfs module\_utils \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> environment variables to <code>C</code> in all <code>run\_command\(\)</code> calls \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11787](https\://github\.com/ansible\-collections/community\.general/pull/11787)\)\.
* btrfs\_subvolume \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* btrfs\_subvolume \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* bundler \- replace deprecated <code>\-\-deployment</code>\, <code>\-\-without</code>\, <code>\-\-path</code>\, <code>\-\-clean</code>\, and <code>\-\-binstubs</code> flags with <code>BUNDLE\_\*</code> environment variables\, fixing compatibility with Bundler 4 \([https\://github\.com/ansible\-collections/community\.general/issues/4583](https\://github\.com/ansible\-collections/community\.general/issues/4583)\, [https\://github\.com/ansible\-collections/community\.general/issues/11380](https\://github\.com/ansible\-collections/community\.general/issues/11380)\, [https\://github\.com/ansible\-collections/community\.general/pull/12024](https\://github\.com/ansible\-collections/community\.general/pull/12024)\)\.
* bundler \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11783](https\://github\.com/ansible\-collections/community\.general/pull/11783)\)\.
* bzr \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11785](https\://github\.com/ansible\-collections/community\.general/pull/11785)\)\.
* capabilities \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11779](https\://github\.com/ansible\-collections/community\.general/pull/11779)\)\.
* cargo \- fix <code>state\=latest</code> always reporting <code>changed</code> due to greedy regex capturing description text instead of version string \([https\://github\.com/ansible\-collections/community\.general/issues/8949](https\://github\.com/ansible\-collections/community\.general/issues/8949)\, [https\://github\.com/ansible\-collections/community\.general/pull/12064](https\://github\.com/ansible\-collections/community\.general/pull/12064)\)\.
* cargo \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* chef\_databag lookup plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* cloudflare\_dns \- also allow <code>flag\=128</code> for CAA records \([https\://github\.com/ansible\-collections/community\.general/issues/11355](https\://github\.com/ansible\-collections/community\.general/issues/11355)\, [https\://github\.com/ansible\-collections/community\.general/pull/11377](https\://github\.com/ansible\-collections/community\.general/pull/11377)\)\.
* cobbler\_system \- compare the version as a float which is the type returned by the Cobbler API \([https\://github\.com/ansible\-collections/community\.general/issues/11044](https\://github\.com/ansible\-collections/community\.general/issues/11044)\)\.
* cobbler\_system \- fix <code>KeyError</code> when adding a new interface to an existing system that does not yet have it defined \([https\://github\.com/ansible\-collections/community\.general/issues/7007](https\://github\.com/ansible\-collections/community\.general/issues/7007)\, [https\://github\.com/ansible\-collections/community\.general/pull/11995](https\://github\.com/ansible\-collections/community\.general/pull/11995)\)\.
* composer \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* consul \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* consul\_kv lookup plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* counter\_enabled callback plugin \- fix plugin not observing <code>display\_ok\_hosts</code> option \([https\://github\.com/ansible\-collections/community\.general/issues/3978](https\://github\.com/ansible\-collections/community\.general/issues/3978)\, [https\://github\.com/ansible\-collections/community\.general/pull/11656](https\://github\.com/ansible\-collections/community\.general/pull/11656)\)\.
* cronvar \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* cronvar \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* crypttab \- fix parsing of options whose value contains an equal sign \([https\://github\.com/ansible\-collections/community\.general/issues/4963](https\://github\.com/ansible\-collections/community\.general/issues/4963)\, [https\://github\.com/ansible\-collections/community\.general/pull/11926](https\://github\.com/ansible\-collections/community\.general/pull/11926)\)\.
* datadog\_downtime \- fix <code>TypeError</code> when returning API response with <code>datadog\-api\-client</code> \>\= 2\.28\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/9079](https\://github\.com/ansible\-collections/community\.general/issues/9079)\, [https\://github\.com/ansible\-collections/community\.general/pull/12019](https\://github\.com/ansible\-collections/community\.general/pull/12019)\)\.
* datetime module utils \- fix bug in <code>fromtimestamp\(\)</code> that caused the function to crash\. This function is not used in community\.general \([https\://github\.com/ansible\-collections/community\.general/pull/11206](https\://github\.com/ansible\-collections/community\.general/pull/11206)\)\.
* dconf \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11765](https\://github\.com/ansible\-collections/community\.general/pull/11765)\)\.
* discord \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* dnf\_versionlock \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* dnf\_versionlock \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* dnsmadeeasy \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* dpkg\_divert \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* dpkg\_divert \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* easy\_install \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.
* elastic callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* etcd3 lookup plugin \- improve HTTPS endpoint handling by stripping URL schemes from the <code>host</code> option and warning when <code>ca\_cert</code> is not provided for HTTPS endpoints \([https\://github\.com/ansible\-collections/community\.general/issues/1664](https\://github\.com/ansible\-collections/community\.general/issues/1664)\, [https\://github\.com/ansible\-collections/community\.general/pull/11861](https\://github\.com/ansible\-collections/community\.general/pull/11861)\)\.
* facter\_facts \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* filesystem \- avoid false positive change detection on XFS resize due to unusable slack space \([https\://github\.com/ansible\-collections/community\.general/pull/11033](https\://github\.com/ansible\-collections/community\.general/pull/11033)\)\.
* filesystem \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* flatpak \- fix removal of runtimes\, which was broken because the module was filtering the installed flatpak list to apps only\, so runtimes could never be matched for uninstallation \([https\://github\.com/ansible\-collections/community\.general/issues/553](https\://github\.com/ansible\-collections/community\.general/issues/553)\, [https\://github\.com/ansible\-collections/community\.general/pull/11688](https\://github\.com/ansible\-collections/community\.general/pull/11688)\)\.
* flatpak \- fix reporting <code>changed</code> on already present flatpaks with a dash in the last part of the ID \([https\://github\.com/ansible\-collections/community\.general/issues/12062](https\://github\.com/ansible\-collections/community\.general/issues/12062)\, [https\://github\.com/ansible\-collections/community\.general/pull/12063](https\://github\.com/ansible\-collections/community\.general/pull/12063)\)\.
* flatpak \- support new output message when an update resulted in no action that appears on Fedora 44 \([https\://github\.com/ansible\-collections/community\.general/pull/11836](https\://github\.com/ansible\-collections/community\.general/pull/11836)\)\.
* flatpak\_remote \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* gem \- add compatibility with Ruby 4 rubygems \([https\://github\.com/ansible\-collections/community\.general/issues/11397](https\://github\.com/ansible\-collections/community\.general/issues/11397)\, [https\://github\.com/ansible\-collections/community\.general/pull/11442](https\://github\.com/ansible\-collections/community\.general/pull/11442)\)\.
* git\_config \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* git\_config\_info \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11738](https\://github\.com/ansible\-collections/community\.general/pull/11738)\)\.
* gitlab module utils \- add type hints\. Pass API version to python\-gitlab as string and not as integer \([https\://github\.com/ansible\-collections/community\.general/pull/11222](https\://github\.com/ansible\-collections/community\.general/pull/11222)\)\.
* gitlab module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_branch \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_group\_members \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_hook \- now properly passes the <code>releases\_events</code> parameter to the GitLab API on hook creation\, fixing a 500 Internal Server Error when the parameter was not specified \([https\://github\.com/ansible\-collections/community\.general/issues/11269](https\://github\.com/ansible\-collections/community\.general/issues/11269)\, [https\://github\.com/ansible\-collections/community\.general/pull/11917](https\://github\.com/ansible\-collections/community\.general/pull/11917)\)\.
* gitlab\_issue \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* gitlab\_merge\_request \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* gitlab\_project \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* gitlab\_project\_members \- fail with a clear error when multiple projects match the given name\, instead of silently operating on the first result \([https\://github\.com/ansible\-collections/community\.general/issues/2767](https\://github\.com/ansible\-collections/community\.general/issues/2767)\, [https\://github\.com/ansible\-collections/community\.general/pull/11851](https\://github\.com/ansible\-collections/community\.general/pull/11851)\)\.
* gitlab\_project\_members \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_project\_variable \- use <code>find\_project\(\)</code> from module utils for project lookup\, consistent with all other GitLab modules in the collection \([https\://github\.com/ansible\-collections/community\.general/issues/3157](https\://github\.com/ansible\-collections/community\.general/issues/3157)\, [https\://github\.com/ansible\-collections/community\.general/pull/11878](https\://github\.com/ansible\-collections/community\.general/pull/11878)\)\.
* gitlab\_protected\_branch \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* gitlab\_user \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* haproxy \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* hg \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11773](https\://github\.com/ansible\-collections/community\.general/pull/11773)\)\.
* homebrew \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* homebrew \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* homebrew\_cask \- fix <code>sudo\_password</code> failing when the password contains single quotes or other special shell characters \([https\://github\.com/ansible\-collections/community\.general/issues/4957](https\://github\.com/ansible\-collections/community\.general/issues/4957)\, [https\://github\.com/ansible\-collections/community\.general/pull/11850](https\://github\.com/ansible\-collections/community\.general/pull/11850)\)\.
* homebrew\_cask \- fix failure when <code>brew \-\-version</code> returns a placeholder version string \([https\://github\.com/ansible\-collections/community\.general/issues/4708](https\://github\.com/ansible\-collections/community\.general/issues/4708)\, [https\://github\.com/ansible\-collections/community\.general/pull/11849](https\://github\.com/ansible\-collections/community\.general/pull/11849)\)\.
* homebrew\_cask \- fix false task failure when upgrading casks with <code>version\=latest</code>\; the post\-upgrade check incorrectly re\-ran <code>brew outdated</code> \(which always lists <code>latest</code> casks as outdated under <code>\-\-greedy</code>\)\, now uses the command exit code instead \([https\://github\.com/ansible\-collections/community\.general/issues/1647](https\://github\.com/ansible\-collections/community\.general/issues/1647)\, [https\://github\.com/ansible\-collections/community\.general/pull/11838](https\://github\.com/ansible\-collections/community\.general/pull/11838)\)\.
* homebrew\_cask \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* homebrew\_service \- slightly refactor code \([https\://github\.com/ansible\-collections/community\.general/pull/11168](https\://github\.com/ansible\-collections/community\.general/pull/11168)\)\.
* homebrew\_services \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* homebrew\_tap \- fix <code>None</code> being passed as a command argument when adding a tap without a URL \([https\://github\.com/ansible\-collections/community\.general/pull/11848](https\://github\.com/ansible\-collections/community\.general/pull/11848)\)\.
* homectl \- allow to use passlib instead of legacycrypt for Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/pull/11860](https\://github\.com/ansible\-collections/community\.general/pull/11860)\)\.
* homectl \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* hpilo\_boot \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* icinga2\_feature \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* imgadm \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* incus connection plugin \- fix parsing of commands for Windows\, enforcing a <code>\\</code> after the drive letter and colon symbol \([https\://github\.com/ansible\-collections/community\.general/pull/11347](https\://github\.com/ansible\-collections/community\.general/pull/11347)\)\.
* incus connection plugin \- work when the active become plugin sets <code>require\_tty</code> instead of failing silently \([https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* infinity \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ini\_file \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* interfaces\_file \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ip\_netns \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11779](https\://github\.com/ansible\-collections/community\.general/pull/11779)\)\.
* ipa module utils \- fix failure to detect errors reported in the <code>failed</code> field of the IPA API response\, which is returned with HTTP 200 on partial or full failures in member add/remove operations \([https\://github\.com/ansible\-collections/community\.general/issues/1239](https\://github\.com/ansible\-collections/community\.general/issues/1239)\, [https\://github\.com/ansible\-collections/community\.general/pull/11698](https\://github\.com/ansible\-collections/community\.general/pull/11698)\)\.
* ipa\_dnsrecord \- fix errors when module is used with existing record with default TTL \([https\://github\.com/ansible\-collections/community\.general/pull/11717](https\://github\.com/ansible\-collections/community\.general/pull/11717)\)\.
* ipa\_dnsrecord \- fix idempotency bug when using <code>dnsttl</code> due to wrong Python types \([https\://github\.com/ansible\-collections/community\.general/pull/11559](https\://github\.com/ansible\-collections/community\.general/pull/11559)\)\.
* ipa\_group \- fix idempotency when <code>external\: false</code> on an existing non\-external group \([https\://github\.com/ansible\-collections/community\.general/issues/5061](https\://github\.com/ansible\-collections/community\.general/issues/5061)\, [https\://github\.com/ansible\-collections/community\.general/pull/11933](https\://github\.com/ansible\-collections/community\.general/pull/11933)\)\.
* ipa\_group \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ipa\_host \- fix logic to disable existing hosts \([https\://github\.com/ansible\-collections/community\.general/issues/11483](https\://github\.com/ansible\-collections/community\.general/issues/11483)\, [https\://github\.com/ansible\-collections/community\.general/pull/11487](https\://github\.com/ansible\-collections/community\.general/pull/11487)\)\.
* ipa\_otptoken \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* ipa\_vault \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ipinfoio\_facts \- fix handling of HTTP errors consulting the service \([https\://github\.com/ansible\-collections/community\.general/pull/11145](https\://github\.com/ansible\-collections/community\.general/pull/11145)\)\.
* ipmi\_boot \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* iptables\_state \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* iptables\_state \- refactor code to avoid unnecessary unused variables and improve internal state handling \([https\://github\.com/ansible\-collections/community\.general/pull/12093](https\://github\.com/ansible\-collections/community\.general/pull/12093)\)\.
* iptables\_state \- refactor code to avoid writing unnecessary temporary files \([https\://github\.com/ansible\-collections/community\.general/pull/11258](https\://github\.com/ansible\-collections/community\.general/pull/11258)\)\.
* iso\_extract \- retry <code>umount</code> up to 5 times preventing <code>OSError</code> on cleanup \([https\://github\.com/ansible\-collections/community\.general/issues/5333](https\://github\.com/ansible\-collections/community\.general/issues/5333)\, [https\://github\.com/ansible\-collections/community\.general/pull/11837](https\://github\.com/ansible\-collections/community\.general/pull/11837)\)\.
* iso\_extract \- strip leading path separator from file entries so files with a leading <code>/</code> are extracted correctly \([https\://github\.com/ansible\-collections/community\.general/issues/5283](https\://github\.com/ansible\-collections/community\.general/issues/5283)\, [https\://github\.com/ansible\-collections/community\.general/pull/11825](https\://github\.com/ansible\-collections/community\.general/pull/11825)\)\.
* java\_cert \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* java\_keystore \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* jenkins\_build \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* jenkins\_build\_info \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* jenkins\_credential \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* jenkins\_plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* jenkins\_plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* json\_patch filter plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* kea\_command \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak module utils \- fix <code>TypeError</code> crash when managing users whose username or email contains special characters such as <code>\+</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10305](https\://github\.com/ansible\-collections/community\.general/issues/10305)\, [https\://github\.com/ansible\-collections/community\.general/pull/11472](https\://github\.com/ansible\-collections/community\.general/pull/11472)\)\.
* keycloak module utils \- use proper URL encoding \(<code>urllib\.parse\.quote</code>\) for query parameters in authorization permission name searches\, replacing fragile manual space replacement \([https\://github\.com/ansible\-collections/community\.general/pull/11472](https\://github\.com/ansible\-collections/community\.general/pull/11472)\)\.
* keycloak\_authentication \- fix <code>TypeError</code> crash when a flow is defined without <code>authenticationExecutions</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11547](https\://github\.com/ansible\-collections/community\.general/issues/11547)\, [https\://github\.com/ansible\-collections/community\.general/pull/11548](https\://github\.com/ansible\-collections/community\.general/pull/11548)\)\.
* keycloak\_authz\_permission \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_client \- fix idempotency bug caused by <code>null</code> client attribute value differences for non\-existing client attributes \([https\://github\.com/ansible\-collections/community\.general/issues/11443](https\://github\.com/ansible\-collections/community\.general/issues/11443)\, [https\://github\.com/ansible\-collections/community\.general/pull/11444](https\://github\.com/ansible\-collections/community\.general/pull/11444)\)\.
* keycloak\_client \- fix idempotency bug caused by <code>null</code> flow overrides value differences for non\-existing flow overrides \([https\://github\.com/ansible\-collections/community\.general/issues/11430](https\://github\.com/ansible\-collections/community\.general/issues/11430)\, [https\://github\.com/ansible\-collections/community\.general/pull/11455](https\://github\.com/ansible\-collections/community\.general/pull/11455)\)\.
* keycloak\_client \- remove IDs as change from diff result for protocol mappers \([https\://github\.com/ansible\-collections/community\.general/issues/11453](https\://github\.com/ansible\-collections/community\.general/issues/11453)\, [https\://github\.com/ansible\-collections/community\.general/pull/11454](https\://github\.com/ansible\-collections/community\.general/pull/11454)\)\.
* keycloak\_clientscope\_type \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_component \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* keycloak\_realm \- fixed crash in <code>sanitize\_cr\(\)</code> when <code>realmrep</code> was <code>None</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11260](https\://github\.com/ansible\-collections/community\.general/pull/11260)\)\.
* keycloak\_realm\_key \- fix <code>KeyError</code> crash when managing realm keys where Keycloak does not return <code>active</code>\, <code>enabled</code>\, or <code>algorithm</code> fields in the config response \([https\://github\.com/ansible\-collections/community\.general/issues/11459](https\://github\.com/ansible\-collections/community\.general/issues/11459)\, [https\://github\.com/ansible\-collections/community\.general/pull/11470](https\://github\.com/ansible\-collections/community\.general/pull/11470)\)\.
* keycloak\_realm\_key \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* keycloak\_user\_execute\_actions\_email \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_user\_federation \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* keycloak\_user\_federation \- mapper config item can be an array \([https\://github\.com/ansible\-collections/community\.general/issues/11502](https\://github\.com/ansible\-collections/community\.general/issues/11502)\, [https\://github\.com/ansible\-collections/community\.general/pull/11515](https\://github\.com/ansible\-collections/community\.general/pull/11515)\)\.
* keycloak\_user\_rolemapping \- fix <code>TypeError</code> crash when adding a client role to a user who has no existing roles for that client \([https\://github\.com/ansible\-collections/community\.general/issues/10960](https\://github\.com/ansible\-collections/community\.general/issues/10960)\, [https\://github\.com/ansible\-collections/community\.general/pull/11471](https\://github\.com/ansible\-collections/community\.general/pull/11471)\)\.
* keycloak\_user\_rolemapping module \- fixed crash when assigning roles to users without an existing role \([https\://github\.com/ansible\-collections/community\.general/issues/10960](https\://github\.com/ansible\-collections/community\.general/issues/10960)\, [https\://github\.com/ansible\-collections/community\.general/pull/11256](https\://github\.com/ansible\-collections/community\.general/pull/11256)\)\.
* keycloak\_userprofile \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* keyring \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* keyring\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11786](https\://github\.com/ansible\-collections/community\.general/pull/11786)\)\.
* keys\_filter\.py plugin utils \- fixed requirements check so that other sequences than lists and strings are checked\, and corrected broken formatting during error reporting \([https\://github\.com/ansible\-collections/community\.general/pull/11167](https\://github\.com/ansible\-collections/community\.general/pull/11167)\)\.
* kibana\_plugin \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11783](https\://github\.com/ansible\-collections/community\.general/pull/11783)\)\.
* known\_hosts module utils \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* launchd \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* launchd \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* lbu \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* ldap\_attrs \- fix <code>state\=exact</code> incorrectly issuing <code>MOD\_ADD</code> instead of <code>MOD\_REPLACE</code> for attributes returned by the server with different casing \([https\://github\.com/ansible\-collections/community\.general/issues/1624](https\://github\.com/ansible\-collections/community\.general/issues/1624)\, [https\://github\.com/ansible\-collections/community\.general/pull/11990](https\://github\.com/ansible\-collections/community\.general/pull/11990)\)\.
* linode inventory plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* listen\_ports\_facts \- fix handling of empty PID lists when <code>command\=ss</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11332](https\://github\.com/ansible\-collections/community\.general/pull/11332)\)\.
* listen\_ports\_facts \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* listen\_ports\_facts \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* listen\_ports\_facts \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11774](https\://github\.com/ansible\-collections/community\.general/pull/11774)\)\.
* lldp \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11785](https\://github\.com/ansible\-collections/community\.general/pull/11785)\)\.
* locale\_gen \- add missing locale entries to <code>/etc/locale\.gen</code> when not already present \([https\://github\.com/ansible\-collections/community\.general/issues/2399](https\://github\.com/ansible\-collections/community\.general/issues/2399)\, [https\://github\.com/ansible\-collections/community\.general/pull/11824](https\://github\.com/ansible\-collections/community\.general/pull/11824)\)\.
* logentries callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* logrotate \- adds missing default values for <code>state</code> and <code>config\_dir</code> parameters\, and adds <code>required\_by</code> declarations for shred and compression parameters \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logrotate \- fixes <code>TypeError</code> when <code>shred\_cycles</code> is <code>None</code> and corrects <code>enabled\=None</code> handling in <code>get\_config\_path\(\)</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logrotate \- writes configuration files to a temporary file first and validates before atomically moving to the destination\, and properly wraps all <code>os\.remove\(\)</code> and <code>atomic\_move\(\)</code> calls in error handling \([https\://github\.com/ansible\-collections/community\.general/pull/11764](https\://github\.com/ansible\-collections/community\.general/pull/11764)\)\.
* logstash\_plugin \- fix argument order when using <code>version</code> parameter\. The plugin name must come after options like <code>\-\-version</code> for the <code>logstash\-plugin</code> CLI to work correctly \([https\://github\.com/ansible\-collections/community\.general/issues/10745](https\://github\.com/ansible\-collections/community\.general/issues/10745)\, [https\://github\.com/ansible\-collections/community\.general/pull/11440](https\://github\.com/ansible\-collections/community\.general/pull/11440)\)\.
* logstash\_plugin \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* logstash\_plugin \- use <code>http\_proxy</code>/<code>https\_proxy</code> environment variables for proxy support instead of broken JVM flags\; expose <code>stderr</code> on failure \([https\://github\.com/ansible\-collections/community\.general/issues/8650](https\://github\.com/ansible\-collections/community\.general/issues/8650)\, [https\://github\.com/ansible\-collections/community\.general/pull/11951](https\://github\.com/ansible\-collections/community\.general/pull/11951)\)\.
* lvg \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* lvol \- fix LVM version parsing \([https\://github\.com/ansible\-collections/community\.general/issues/5445](https\://github\.com/ansible\-collections/community\.general/issues/5445)\, [https\://github\.com/ansible\-collections/community\.general/pull/11823](https\://github\.com/ansible\-collections/community\.general/pull/11823)\)\.
* lvol \- fix thin\-pool creation when <code>size</code> is a percentage \([https\://github\.com/ansible\-collections/community\.general/issues/11923](https\://github\.com/ansible\-collections/community\.general/issues/11923)\, [https\://github\.com/ansible\-collections/community\.general/pull/11925](https\://github\.com/ansible\-collections/community\.general/pull/11925)\)\.
* lvol \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* lxc\_container \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* lxc\_container \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11779](https\://github\.com/ansible\-collections/community\.general/pull/11779)\)\.
* lxd\_container \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* machinectl become plugin \- prevent printing ANSI terminal color sequences \([https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* macports \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* manageiq\_alert\_profiles \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* manageiq\_provider \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* manageiq\_tenant \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* mas \- parse CLI output correctly when listing installed apps with mas 3\.0\.0\+ \([https\://github\.com/ansible\-collections/community\.general/pull/11179](https\://github\.com/ansible\-collections/community\.general/pull/11179)\)\.
* mas \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* matrix \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* maven\_artifact \- fix SNAPSHOT version resolution to pick the newest matching <code>\<snapshotVersion\></code> entry by <code>\<updated\></code> timestamp instead of the first\. Repositories like GitHub Packages keep all historical entries in <code>\<snapshotVersions\></code> \(oldest first\)\, causing the module to resolve to the oldest snapshot instead of the latest \([https\://github\.com/ansible\-collections/community\.general/issues/5117](https\://github\.com/ansible\-collections/community\.general/issues/5117)\, [https\://github\.com/ansible\-collections/community\.general/issues/11489](https\://github\.com/ansible\-collections/community\.general/issues/11489)\, [https\://github\.com/ansible\-collections/community\.general/pull/11501](https\://github\.com/ansible\-collections/community\.general/pull/11501)\)\.
* maven\_artifact \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* memset\_memstore\_info \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* memset\_server\_info \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* memset\_zone \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* modprobe \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* module\_helper module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* monit \- add delay of 0\.5 seconds after state change and check for status \([https\://github\.com/ansible\-collections/community\.general/pull/11255](https\://github\.com/ansible\-collections/community\.general/pull/11255)\)\.
* monit \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* monit \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* monit \- internal state was not reflecting when operation is \"pending\" in <code>monit</code> \([https\://github\.com/ansible\-collections/community\.general/pull/11245](https\://github\.com/ansible\-collections/community\.general/pull/11245)\)\.
* mssql\_db \- fail with a clear error message when a named instance \(<code>server\\instance</code> format\) is used together with <code>login\_port</code>\, since these are mutually exclusive connection methods \([https\://github\.com/ansible\-collections/community\.general/issues/5693](https\://github\.com/ansible\-collections/community\.general/issues/5693)\, [https\://github\.com/ansible\-collections/community\.general/pull/11664](https\://github\.com/ansible\-collections/community\.general/pull/11664)\)\.
* mssql\_script \- fail with a clear error message when a named instance \(<code>server\\instance</code> format\) is used together with <code>login\_port</code>\, since these are mutually exclusive connection methods \([https\://github\.com/ansible\-collections/community\.general/issues/5693](https\://github\.com/ansible\-collections/community\.general/issues/5693)\, [https\://github\.com/ansible\-collections/community\.general/pull/11664](https\://github\.com/ansible\-collections/community\.general/pull/11664)\)\.
* mssql\_script \- only passes <code>params</code> to <code>cursor\.execute\(\)</code> when the user actually provides them \([https\://github\.com/ansible\-collections/community\.general/issues/11699](https\://github\.com/ansible\-collections/community\.general/issues/11699)\, [https\://github\.com/ansible\-collections/community\.general/pull/11754](https\://github\.com/ansible\-collections/community\.general/pull/11754)\)\.
* netcup\_dns \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nictagadm \- add a condition to the if statement so that <code>is\_valid\_mac\(\)</code> does not get called if <code>etherstub</code> is false \([https\://github\.com/ansible\-collections/community\.general/pull/11589](https\://github\.com/ansible\-collections/community\.general/pull/11589)\)\.
* nmcli \- add missing <code>ipv6\.routing\-rules</code> to <code>settings\_type\(\)</code> list type\, preventing <code>routing\_rules6</code> list from being corrupted \([https\://github\.com/ansible\-collections/community\.general/issues/11630](https\://github\.com/ansible\-collections/community\.general/issues/11630)\, [https\://github\.com/ansible\-collections/community\.general/pull/11635](https\://github\.com/ansible\-collections/community\.general/pull/11635)\)\.
* nmcli \- fix check/diff reporting changes for bond <code>arp\_interval</code> and <code>arp\_ip\_target</code> options when they are already configured \([https\://github\.com/ansible\-collections/community\.general/issues/11588](https\://github\.com/ansible\-collections/community\.general/issues/11588)\, [https\://github\.com/ansible\-collections/community\.general/pull/12085](https\://github\.com/ansible\-collections/community\.general/pull/12085)\)\.
* nmcli \- fix incorrectly reports diff for bond connections when <code>mtu</code> is unset and NetworkManager reports no explicit MTU value \([https\://github\.com/ansible\-collections/community\.general/pull/12085](https\://github\.com/ansible\-collections/community\.general/pull/12085)\)\.
* nmcli \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nmcli \- use <code>get\_best\_parsable\_locale\(\)</code> to set locale environment for <code>run\_command\(\)</code> calls\, fixing UTF\-8 connection names being corrupted to <code>\?\?\?\?</code> under <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/10384](https\://github\.com/ansible\-collections/community\.general/issues/10384)\, [https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11742](https\://github\.com/ansible\-collections/community\.general/pull/11742)\)\.
* nomad\_job \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nosh \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* npm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* nsupdate \- fix GSS\-TSIG support \(accidentally broken by [https\://github\.com/ansible\-collections/community\.general/pull/11461](https\://github\.com/ansible\-collections/community\.general/pull/11461)\, [https\://github\.com/ansible\-collections/community\.general/pull/11712](https\://github\.com/ansible\-collections/community\.general/pull/11712)\)
* nsupdate \- fix <code>AttributeError</code> when using the module without TSIG authentication \([https\://github\.com/ansible\-collections/community\.general/issues/11460](https\://github\.com/ansible\-collections/community\.general/issues/11460)\, [https\://github\.com/ansible\-collections/community\.general/pull/11461](https\://github\.com/ansible\-collections/community\.general/pull/11461)\)\.
* odbc \- fetch rows before committing to fix <code>HY010</code> function sequence error \([https\://github\.com/ansible\-collections/community\.general/issues/5395](https\://github\.com/ansible\-collections/community\.general/issues/5395)\, [https\://github\.com/ansible\-collections/community\.general/pull/11972](https\://github\.com/ansible\-collections/community\.general/pull/11972)\)\.
* odbc \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* ohai \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11785](https\://github\.com/ansible\-collections/community\.general/pull/11785)\)\.
* one\_host \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_image \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_service \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* one\_template \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_vm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* one\_vm \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* one\_vnet \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* oneandone module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* onepassword\_info \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* onepassword\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11786](https\://github\.com/ansible\-collections/community\.general/pull/11786)\)\.
* online inventory plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* open\_iscsi \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* open\_iscsi \- fix IPv6 portal address formatting\; iscsiadm requires bracket notation for IPv6 addresses but the module was producing an incorrect format \([https\://github\.com/ansible\-collections/community\.general/issues/4467](https\://github\.com/ansible\-collections/community\.general/issues/4467)\, [https\://github\.com/ansible\-collections/community\.general/pull/11657](https\://github\.com/ansible\-collections/community\.general/pull/11657)\)\.
* openbsd\_pkg \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11767](https\://github\.com/ansible\-collections/community\.general/pull/11767)\)\.
* opendj\_backendprop \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* opennebula module utils \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* opentelemetry callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* opentelemetry callback plugin \- set span start to the actual start time of the task for the given host instead of the task start time for the first host of that task \([https\://github\.com/ansible\-collections/community\.general/pull/11434](https\://github\.com/ansible\-collections/community\.general/pull/11434)\)\.
* openwrt\_init \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11784](https\://github\.com/ansible\-collections/community\.general/pull/11784)\)\.
* osx\_defaults \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* ovh\_monthly\_billing \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* pacemaker\_resource\, pacemaker\_stonith \- fix resource and stonith creation race condition by polling PCS status \([https\://github\.com/ansible\-collections/community\.general/issues/11574](https\://github\.com/ansible\-collections/community\.general/issues/11574)\, [https\://github\.com/ansible\-collections/community\.general/pull/11750](https\://github\.com/ansible\-collections/community\.general/pull/11750)\)\.
* pacman \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* pacman\_key \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* pam\_limits \- only create backup file when the target file is actually modified \([https\://github\.com/ansible\-collections/community\.general/issues/12011](https\://github\.com/ansible\-collections/community\.general/issues/12011)\, [https\://github\.com/ansible\-collections/community\.general/pull/12014](https\://github\.com/ansible\-collections/community\.general/pull/12014)\)\.
* pam\_limits \- remove <code>\%</code> templating no longer used in f\-string \([https\://github\.com/ansible\-collections/community\.general/pull/11229](https\://github\.com/ansible\-collections/community\.general/pull/11229)\)\.
* pamd \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* parted \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11740](https\://github\.com/ansible\-collections/community\.general/pull/11740)\)\.
* pear \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.
* pfexec become plugin \- fix default <code>become\_flags</code> from <code>\-H \-S \-n</code> \(sudo flags\) to empty string\, as <code>pfexec</code> does not accept these options \([https\://github\.com/ansible\-collections/community\.general/pull/11623](https\://github\.com/ansible\-collections/community\.general/pull/11623)\)\.
* pip\_package\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11784](https\://github\.com/ansible\-collections/community\.general/pull/11784)\)\.
* pkg5 \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* pkg5\_publisher \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* pkgin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* pkgin \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* pkgng \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11765](https\://github\.com/ansible\-collections/community\.general/pull/11765)\)\.
* pkgutil \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11775](https\://github\.com/ansible\-collections/community\.general/pull/11775)\)\.
* pmem \- fix test for invalid data input \([https\://github\.com/ansible\-collections/community\.general/pull/11388](https\://github\.com/ansible\-collections/community\.general/pull/11388)\)\.
* pnpm \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* portage \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* portinstall \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* portinstall \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* pulp\_repo \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* puppet \- fix <code>TypeError</code> when writing facts data \([https\://github\.com/ansible\-collections/community\.general/issues/7932](https\://github\.com/ansible\-collections/community\.general/issues/7932)\, [https\://github\.com/ansible\-collections/community\.general/pull/11954](https\://github\.com/ansible\-collections/community\.general/pull/11954)\)\.
* python\_requirements\_info \- use <code>importlib\.metadata</code> if <code>pkg\_resources</code> from <code>setuptools</code> cannot be imported\. That module has been removed from setuptools 82\.0\.0 \([https\://github\.com/ansible\-collections/community\.general/issues/11491](https\://github\.com/ansible\-collections/community\.general/issues/11491)\, [https\://github\.com/ansible\-collections/community\.general/pull/11492](https\://github\.com/ansible\-collections/community\.general/pull/11492)\)\.
* redfish\_utils module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* redhat\_subscription \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* redhat\_subscription \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* redhat\_subscription \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* redis\_data\_incr \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* rhevm \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* rhsm\_release \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* rhsm\_repository \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* riak \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11786](https\://github\.com/ansible\-collections/community\.general/pull/11786)\)\.
* rpm\_ostree\_pkg \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* run0 become plugin \- mark the plugin as incompatible with connection pipelining \(see [https\://github\.com/ansible/ansible/issues/81254](https\://github\.com/ansible/ansible/issues/81254)\, [https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* run0 become plugin \- prevent printing ANSI terminal color sequences \([https\://github\.com/ansible\-collections/community\.general/pull/11771](https\://github\.com/ansible\-collections/community\.general/pull/11771)\)\.
* runit \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* scaleway module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* scaleway\_image\_info\, scaleway\_ip\_info\, scaleway\_organization\_info\, scaleway\_security\_group\_info\, scaleway\_server\_info\, scaleway\_snapshot\_info\, scaleway\_volume\_info \- fix <code>NoneType</code> error when the Scaleway API returns an empty or non\-JSON response body \([https\://github\.com/ansible\-collections/community\.general/issues/11361](https\://github\.com/ansible\-collections/community\.general/issues/11361)\, [https\://github\.com/ansible\-collections/community\.general/pull/11918](https\://github\.com/ansible\-collections/community\.general/pull/11918)\)\.
* scaleway\_sshkey \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* sefcontext \- flush the in\-process <code>matchpathcon</code> cache after applying changes\, so subsequent tasks running in the same process \(for example via the Mitogen connection plugin\) see the updated SELinux file context rules instead of stale cached data \([https\://github\.com/ansible\-collections/community\.general/issues/888](https\://github\.com/ansible\-collections/community\.general/issues/888)\, [https\://github\.com/ansible\-collections/community\.general/pull/11812](https\://github\.com/ansible\-collections/community\.general/pull/11812)\)\.
* selective callback plugin \- align host names in stats output by padding to the longest name \([https\://github\.com/ansible\-collections/community\.general/issues/8797](https\://github\.com/ansible\-collections/community\.general/issues/8797)\, [https\://github\.com/ansible\-collections/community\.general/pull/12065](https\://github\.com/ansible\-collections/community\.general/pull/12065)\)\.
* selective callback plugin \- route all output through <code>self\.\_display\.display\(\)</code> instead of bare <code>print\(\)</code> calls\, fixing missing output when <code>ANSIBLE\_LOG\_PATH</code> is set \([https\://github\.com/ansible\-collections/community\.general/issues/4850](https\://github\.com/ansible\-collections/community\.general/issues/4850)\, [https\://github\.com/ansible\-collections/community\.general/pull/11927](https\://github\.com/ansible\-collections/community\.general/pull/11927)\)\.
* sensu\_check \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* seport \- fix idempotency when a requested port is already covered by an existing range registered for the same setype \([https\://github\.com/ansible\-collections/community\.general/issues/10105](https\://github\.com/ansible\-collections/community\.general/issues/10105)\, [https\://github\.com/ansible\-collections/community\.general/pull/11994](https\://github\.com/ansible\-collections/community\.general/pull/11994)\)\.
* simpleinit\_msb \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* smartos\_image\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* snap \- enforce <code>snap refresh \-\-hold</code> after installing at a specific revision \([https\://github\.com/ansible\-collections/community\.general/issues/12088](https\://github\.com/ansible\-collections/community\.general/issues/12088)\, [https\://github\.com/ansible\-collections/community\.general/pull/12097](https\://github\.com/ansible\-collections/community\.general/pull/12097)\)\.
* snmp\_facts \- the module now also supports pysnmp \>\= 7\.1 \([https\://github\.com/ansible\-collections/community\.general/issues/8852](https\://github\.com/ansible\-collections/community\.general/issues/8852)\, [https\://github\.com/ansible\-collections/community\.general/pull/11683](https\://github\.com/ansible\-collections/community\.general/pull/11683)\)\.
* sorcery \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11767](https\://github\.com/ansible\-collections/community\.general/pull/11767)\)\.
* sorcery \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* spectrum\_model\_attrs \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* splunk callback plugin \- replace deprecated callback function \([https\://github\.com/ansible\-collections/community\.general/pull/11485](https\://github\.com/ansible\-collections/community\.general/pull/11485)\)\.
* spotinst\_aws\_elastigroup \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* supervisorctl \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* svc \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* svc \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* swdepot \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11780](https\://github\.com/ansible\-collections/community\.general/pull/11780)\)\.
* syslog\_json callback plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* syspatch \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* sysrc \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* sysupgrade \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11768](https\://github\.com/ansible\-collections/community\.general/pull/11768)\)\.
* telegram \- added the <code>api\_host</code> parameter to fix connectivity with self\-hosted proxies and custom API endpoints \([https\://github\.com/ansible\-collections/community\.general/pull/12040](https\://github\.com/ansible\-collections/community\.general/pull/12040)\)\.
* terraform \- ensure <code>LANGUAGE\=C</code> and <code>LC\_ALL\=C</code> are set when running commands that parse output \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11765](https\://github\.com/ansible\-collections/community\.general/pull/11765)\)\.
* terraform \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* timestamp callback plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* timezone \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* timezone \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* to\_\* time filter plugins \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* to\_prettytable filter plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* udm\_user \- allow to use passlib instead of legacycrypt for Python 3\.13\+ \([https\://github\.com/ansible\-collections/community\.general/issues/4690](https\://github\.com/ansible\-collections/community\.general/issues/4690)\, [https\://github\.com/ansible\-collections/community\.general/pull/11860](https\://github\.com/ansible\-collections/community\.general/pull/11860)\)\.
* udm\_user \- fix alias\-to\-canonical parameter name mismatch that caused all camelCase\-aliased parameters such as <code>display\_name</code> and <code>primary\_group</code> to be silently ignored \([https\://github\.com/ansible\-collections/community\.general/issues/2950](https\://github\.com/ansible\-collections/community\.general/issues/2950)\, [https\://github\.com/ansible\-collections/community\.general/issues/3691](https\://github\.com/ansible\-collections/community\.general/issues/3691)\, [https\://github\.com/ansible\-collections/community\.general/pull/11859](https\://github\.com/ansible\-collections/community\.general/pull/11859)\)\.
* ufw \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* vmadm \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* wsl connection plugin \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* wsl connection plugin \- rename variable to fix type checking \([https\://github\.com/ansible\-collections/community\.general/pull/11030](https\://github\.com/ansible\-collections/community\.general/pull/11030)\)\.
* xattr \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* xbps \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11781](https\://github\.com/ansible\-collections/community\.general/pull/11781)\)\.
* xcc\_redfish\_command \- fix templating of dictionary keys as list \([https\://github\.com/ansible\-collections/community\.general/pull/11144](https\://github\.com/ansible\-collections/community\.general/pull/11144)\)\.
* xen\_orchestra inventory plugin \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xenserver module utils \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xenserver\_guest \- fix an issue where booting from ISO is not possible because CD\-ROM device is placed in position above number 3\. Position number 3 is now reserved for CD\-ROM device and cannot be occupied by a disk \([https\://github\.com/ansible\-collections/community\.general/issues/11624](https\://github\.com/ansible\-collections/community\.general/issues/11624)\, [https\://github\.com/ansible\-collections/community\.general/pull/11702](https\://github\.com/ansible\-collections/community\.general/pull/11702)\)\.
* xenserver\_guest \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* xenserver\_guest \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xfconf \- representation of boolean properties was not consistent between Python and <code>xfconf\-query</code>\, leading to broken idempotency \([https\://github\.com/ansible\-collections/community\.general/pull/11645](https\://github\.com/ansible\-collections/community\.general/pull/11645)\)\.
* xfs\_quota \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* xml \- emit an error when <code>value</code> is not a string\, pointing to the offending xpath \([https\://github\.com/ansible\-collections/community\.general/issues/7171](https\://github\.com/ansible\-collections/community\.general/issues/7171)\, [https\://github\.com/ansible\-collections/community\.general/pull/11959](https\://github\.com/ansible\-collections/community\.general/pull/11959)\)\.
* xml \- fix <code>print\_match</code> not populating the <code>matches</code> return value \([https\://github\.com/ansible\-collections/community\.general/issues/9125](https\://github\.com/ansible\-collections/community\.general/issues/9125)\, [https\://github\.com/ansible\-collections/community\.general/pull/12013](https\://github\.com/ansible\-collections/community\.general/pull/12013)\)\.
* xml \- improve Python code by removing unnecessary variables \([https\://github\.com/ansible\-collections/community\.general/pull/11049](https\://github\.com/ansible\-collections/community\.general/pull/11049)\)\.
* yarn \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11776](https\://github\.com/ansible\-collections/community\.general/pull/11776)\)\.
* yarn \- skip Node\.js runtime warning lines \(starting with <code>\(node\:</code>\) in stderr before JSON parsing\, fixing failures with Node\.js 24 which emits <code>DeprecationWarning</code> to stderr\. The warnings are passed on to the user \([https\://github\.com/ansible\-collections/community\.general/pull/11943](https\://github\.com/ansible\-collections/community\.general/pull/11943)\)\.
* yum\_versionlock \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11777](https\://github\.com/ansible\-collections/community\.general/pull/11777)\)\.
* zfs \- mark change correctly when updating properties whose current value differs\, even if they already have a non\-default value \([https\://github\.com/ansible\-collections/community\.general/issues/11019](https\://github\.com/ansible\-collections/community\.general/issues/11019)\, [https\://github\.com/ansible\-collections/community\.general/pull/11172](https\://github\.com/ansible\-collections/community\.general/pull/11172)\)\.
* zfs \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zfs\_delegate\_admin \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zfs\_facts \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zpool\_facts \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11778](https\://github\.com/ansible\-collections/community\.general/pull/11778)\)\.
* zypper \- normalize locale environment for <code>run\_command\(\)</code> calls to <code>LANGUAGE\=C</code>\, <code>LC\_ALL\=C</code> \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11741](https\://github\.com/ansible\-collections/community\.general/pull/11741)\)\.
* zypper\_repository \- allow unreachable <code>\.repo</code> URLs and missing local paths when using <code>state\=absent</code> \([https\://github\.com/ansible\-collections/community\.general/issues/5769](https\://github\.com/ansible\-collections/community\.general/issues/5769)\, [https\://github\.com/ansible\-collections/community\.general/pull/11947](https\://github\.com/ansible\-collections/community\.general/pull/11947)\)\.
* zypper\_repository \- improve Python code \([https\://github\.com/ansible\-collections/community\.general/pull/11043](https\://github\.com/ansible\-collections/community\.general/pull/11043)\)\.
* zypper\_repository \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11777](https\://github\.com/ansible\-collections/community\.general/pull/11777)\)\.
* zypper\_repository\_info \- set <code>LANGUAGE</code> and <code>LC\_ALL</code> to <code>C</code> in <code>run\_command\(\)</code> calls to ensure locale\-independent output parsing \([https\://github\.com/ansible\-collections/community\.general/issues/11737](https\://github\.com/ansible\-collections/community\.general/issues/11737)\, [https\://github\.com/ansible\-collections/community\.general/pull/11782](https\://github\.com/ansible\-collections/community\.general/pull/11782)\)\.

<a id="community-hrobot"></a>
#### community\.hrobot

* Remove unnecessary Python 2 compatibilty code \([https\://github\.com/ansible\-collections/community\.hrobot/pull/187](https\://github\.com/ansible\-collections/community\.hrobot/pull/187)\)\.
* storagebox\* modules \- improve error reporting to ensure that method and URL of the failed request are always mentioned \([https\://github\.com/ansible\-collections/community\.hrobot/pull/190](https\://github\.com/ansible\-collections/community\.hrobot/pull/190)\)\.

<a id="community-libvirt-3"></a>
#### community\.libvirt

* libvirt\_qemu \- Vendor <code>\_parse\_clixml</code> locally to fix <code>ImportError</code> on ansible\-core devel \(2\.21\+\)\.
* virt\_install \- fixed cloud\_init configuration handling for meta\-data\, user\-data\, and network\-config\.
* virt\_install \- fixed the dict\-based options handling for events\, resource\, and sysinfo options\.

<a id="community-mysql-4"></a>
#### community\.mysql

* Add action\_groups to meta/runtime\.yml to ensure that if the community\.mysql action group is used\, it also applies to ansible\.mysql\'s action group\.
* mysql\_query \- fix <code>Value of unknown type</code> error when query results contain non\-JSON\-serializable types such as <code>decimal\.Decimal</code> or <code>datetime</code>\. Results are now round\-tripped through <code>json\.dumps\(default\=str\)</code> before being returned\, coercing unserializable values to their string representation \([https\://github\.com/ansible\-collections/community\.mysql/issues/783](https\://github\.com/ansible\-collections/community\.mysql/issues/783)\)\.
* mysql\_user \- When creating a new user\, and specifying parsec as plugin it wil generate the wrong SQL query\. It should be added to the same plugin check as ed25519 so that it generates a query using USING PASSWORDS\(\%s\) instead of BY \%s \([https\://github\.com/ansible\-collections/community\.mysql/pull/779](https\://github\.com/ansible\-collections/community\.mysql/pull/779)\)\.

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_db \- Fix connection limit not being set when value is \"0\" \([https\://github\.com/ansible\-collections/community\.postgresql/issues/879](https\://github\.com/ansible\-collections/community\.postgresql/issues/879)\)\.
* postgresql\_db \- fixed <code>session\_role</code> parameter that was being ignored for raw connections \([https\://github\.com/ansible\-collections/community\.postgresql/pull/865](https\://github\.com/ansible\-collections/community\.postgresql/pull/865)\)
* postgresql\_db \- restoring from <code>\.sql</code> files would execute the file twice\. The module now avoids using both <code>\-\-file</code> and stdin redirection simultaneously \([https\://github\.com/ansible\-collections/community\.postgresql/issues/882](https\://github\.com/ansible\-collections/community\.postgresql/issues/882)\)\.

<a id="community-proxmox-4"></a>
#### community\.proxmox

* proxmox \- fix <code>tags</code> always being reported as changed on LXC container updates because the list value was compared against Proxmox\'s semicolon\-delimited string form \([https\://github\.com/ansible\-collections/community\.proxmox/pull/415](https\://github\.com/ansible\-collections/community\.proxmox/pull/415)\)\.
* proxmox all \- add missing timeout parameter to proxmoxer object creation \([https\://github\.com/ansible\-collections/community\.proxmox/pull/218](https\://github\.com/ansible\-collections/community\.proxmox/pull/218)\)\.
* proxmox modules \- fix calls to <code>get\_storages\(\)</code> to use the correct keyword argument \([https\://github\.com/ansible\-collections/community\.proxmox/pull/401](https\://github\.com/ansible\-collections/community\.proxmox/pull/401)\)\.
* proxmox\_cluster \- make cluster join idempotent \([https\://github\.com/ansible\-collections/community\.proxmox/pull/244](https\://github\.com/ansible\-collections/community\.proxmox/pull/244)\)\.
* proxmox\_cluster\_firewall \- error message for invalid log\_ratelimit\.rate parameter \([https\://github\.com/ansible\-collections/community\.proxmox/pull/340](https\://github\.com/ansible\-collections/community\.proxmox/pull/340)\)\.
* proxmox\_disk \- add support for efidisk and tpmstate disk bus types which previously caused module failure with \"Unsupported disk bus\" error \([https\://github\.com/ansible\-collections/community\.proxmox/pull/319](https\://github\.com/ansible\-collections/community\.proxmox/pull/319)\)\.
* proxmox\_disk \- make none iso disk idempotent \([https\://github\.com/ansible\-collections/community\.proxmox/pull/288](https\://github\.com/ansible\-collections/community\.proxmox/pull/288)\)\.
* proxmox\_firewall \- Enable ipsets on vm level and fix bugs regarding the cidr notation the proxmox api expects \([https\://github\.com/ansible\-collections/community\.proxmox/pull/248](https\://github\.com/ansible\-collections/community\.proxmox/pull/248)\)\.
* proxmox\_firewall\_info \- add none guard on get\_ip\_sets to prevent crash with <code>\'NoneType\' object has no attribute \'ipset\'</code> when using <code>level\=group</code> \([https\://github\.com/ansible\-collections/community\.proxmox/issues/430](https\://github\.com/ansible\-collections/community\.proxmox/issues/430)\)\.
* proxmox\_ipam\_info \- fix bug where selecting by vmid did not work \([https\://github\.com/ansible\-collections/community\.proxmox/pull/211](https\://github\.com/ansible\-collections/community\.proxmox/pull/211)\)\.
* proxmox\_pool \- member retrieval \([https\://github\.com/ansible\-collections/community\.proxmox/pull/412](https\://github\.com/ansible\-collections/community\.proxmox/pull/412)\)\.
* proxmox\_pool \- support nested pool \([https\://github\.com/ansible\-collections/community\.proxmox/pull/316](https\://github\.com/ansible\-collections/community\.proxmox/pull/316)\)\.
* proxmox\_pool\_member \- fix pool membership operations failing for nested pool IDs \([https\://github\.com/ansible\-collections/community\.proxmox/pull/428](https\://github\.com/ansible\-collections/community\.proxmox/pull/428)\)\.
* proxmox\_pool\_member \- fix pool membership update \([https\://github\.com/ansible\-collections/community\.proxmox/pull/428](https\://github\.com/ansible\-collections/community\.proxmox/pull/428)\)\.
* proxmox\_pool\_member \- fix usage of storage member \([https\://github\.com/ansible\-collections/community\.proxmox/pull/411](https\://github\.com/ansible\-collections/community\.proxmox/pull/411)\)\.
* proxmox\_pool\_member \- member retrieval \([https\://github\.com/ansible\-collections/community\.proxmox/pull/412](https\://github\.com/ansible\-collections/community\.proxmox/pull/412)\)\.
* proxmox\_role \- when privs is omitted\, keep existing role privileges unchanged instead of treating it as no privileges \([https\://github\.com/ansible\-collections/community\.proxmox/pull/284](https\://github\.com/ansible\-collections/community\.proxmox/pull/284)\)\.
* proxmox\_snap \- fail the task when a given snapname does not exist instead of exiting \([https\://github\.com/ansible\-collections/community\.proxmox/pull/365](https\://github\.com/ansible\-collections/community\.proxmox/pull/365)\)\.
* proxmox\_storage \- backend <code>cephfs</code>\, <code>dir</code> and <code>zfspool</code> doesn\'t requires <code>content</code> parameter \([https\://github\.com/ansible\-collections/community\.proxmox/pull/315](https\://github\.com/ansible\-collections/community\.proxmox/pull/315)\)\.
* proxmox\_storage \- the parameter <code>client\_keyring</code> was ignored \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- the parameter <code>fs\_name</code> was ignored \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_storage \- the parameter <code>state</code> was optional and without default value \([https\://github\.com/ansible\-collections/community\.proxmox/pull/305](https\://github\.com/ansible\-collections/community\.proxmox/pull/305)\)\.
* proxmox\_zone \- fix validation logic for VXLAN zones to accept either <code>fabric</code> or <code>peers</code> parameter\. Previously\, only <code>fabric</code> was accepted\, but Proxmox VE also supports creating VXLAN zones with a peer address list \([https\://github\.com/ansible\-collections/community\.proxmox/issues/216](https\://github\.com/ansible\-collections/community\.proxmox/issues/216)\)\.
* remove wrong api endpoints and error messages from proxmod\_node certificate management\([https\://github\.com/ansible\-collections/community\.proxmox/pull/232](https\://github\.com/ansible\-collections/community\.proxmox/pull/232)\)\.

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
* api\_modify\, api\_info \- in the <code>routing bgp connection</code> and <code>bgp templates</code> paths\, fix spelling of the <code>output\.remove\-private\-as</code> parameter \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp instance</code> path\, fix \'Cannot add new entry to this path\' error \([https\://github\.com/ansible\-collections/community\.routeros/issues/409](https\://github\.com/ansible\-collections/community\.routeros/issues/409)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/420](https\://github\.com/ansible\-collections/community\.routeros/pull/420)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, remove <code>address\-families</code> for RouterOS 7\.19\+ \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, remove <code>router\-id</code> for RouterOS 7\.20\+ \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.
* api\_modify\, api\_info \- in the <code>routing bgp templates</code> path\, support <code>afi</code> \(RouterOS 7\.19\+\) \(RouterOS 7\.19 and before\) \([https\://github\.com/ansible\-collections/community\.routeros/issues/415](https\://github\.com/ansible\-collections/community\.routeros/issues/415)\, [https\://github\.com/ansible\-collections/community\.routeros/pull/416](https\://github\.com/ansible\-collections/community\.routeros/pull/416)\)\.

<a id="community-vmware-2"></a>
#### community\.vmware

* vmware\_guest\_storage\_policy \- Fix storage policy search to return None if no policies are found\, instead of causing an exception\. fixes [https\://github\.com/ansible\-collections/community\.vmware/issues/2527](https\://github\.com/ansible\-collections/community\.vmware/issues/2527)

<a id="community-windows-5"></a>
#### community\.windows

* Unify the TLS protocol handling logic for the modules that need it to ensure they use the configured OS policies\.
* win\_disk\_facts \- fixed an issue when a disk may not have a number \([https\://github\.com/ansible\-collections/community\.windows/pull/652](https\://github\.com/ansible\-collections/community\.windows/pull/652)\)\.
* win\_initialize\_disk \- disks that are formatted but offline cannot be brought online without erasing them \([https\://github\.com/ansible\-collections/community\.windows/issues/149](https\://github\.com/ansible\-collections/community\.windows/issues/149)\)\.
* win\_psmodule \- Improve error message\, if a module exists in multiple repositories \- [https\://github\.com/ansible\-collections/community\.windows/issues/641](https\://github\.com/ansible\-collections/community\.windows/issues/641)
* win\_psrepository\_copy \- Fix idempotence check to not rely on \.NET runtime implementation details\. This should avoid any false positive changed indicators

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

<a id="containers-podman-4"></a>
#### containers\.podman

* Fix Ansible warning about test utils
* Fix idempotency for tagging local images
* Fix image idempotency in pull
* Fix issue with \-\-rm and service in Quadlet
* fix\(podman\_prune\) set top\-level changed status
* podman\_container \- Fix quadlet\_options placement when restart\_policy is set
* podman\_network \- Add diff and idempotency to ip\_ranges in net\_config
* podman\_pod \- Fix check mode support
* podman\_quadlet\_build \- Fix and add unittests
* podman\_secret \- Fix ignoring \'data\' if it\'s an empty string

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

* Improved the login logic\.
* Improved the request sending logic in httpapi plugin\.
* Reduced the number of requests sent when workspace mode is enabled\.

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fixed an issue where parameters ending with \_dict always returned changed\, even in check mode or when no changes were made\.
* Fixed an issue where some modules could not be configured globally\.
* Fixed an issue where the generate\-key\.system\.api\-user selector in the fortios\_monitor module required an admin password to function\.
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

<a id="hitachivantara-vspone-block-5"></a>
#### hitachivantara\.vspone\_block

* Fixed performance for \"hv\_snapshot\_group\_facts\" module\.
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

<a id="kubernetes-core-6"></a>
#### kubernetes\.core

* Add idempotency for <code>helm\_pull</code> module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1055](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1055)\)\.
* Fixed a bug where setting <code>K8S\_AUTH\_VERIFY\_SSL\=true</code> \(or any string value\) caused the value to be treated as a separate <code>kubectl</code> command argument\. \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1049](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1049)\)\.
* Helm \- Allow taking ownership of existing Kubernetes resources on the first installation of a Helm release\. Previously\, the <code>take\_ownership</code> parameter was always disabled during the initial install\, preventing resource adoption \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1034](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1034)\)\.
* Limit supported versions of Helm to \<4\.0\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1039](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1039)\)\.
* Replace passing <code>warnings</code> to <code>exit\_json</code> with <code>AnsibleModule\.warn</code> in the <code>k8s\_drain</code>\, <code>k8s\_rollback\.py</code> and <code>k8s\_scale\.py</code> modules as it deprecated in <code>ansible\-core\>\=2\.19\.0</code> and will be removed in <code>ansible\-core\>\=2\.23\.0</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1033](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1033)\)\.
* k8s \- Fix return block from the module documentation \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1056)\)\.
* meta \- Add <code>k8s\_cluster\_info</code>\, <code>k8s\_json\_patch</code> and <code>k8s\_rollback</code> to k8s action group \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/992](https\://github\.com/ansible\-collections/kubernetes\.core/pull/992)\)\.

<a id="microsoft-ad-6"></a>
#### microsoft\.ad

* microsoft\.ad\.domain\_child \- Fix return document key so it displays when using the standard Ansible documentation tools\.
* microsoft\.ad\.ldap \- Fix issue where auth\_protocol config option was never used when creating the spnego client\.
* microsoft\.ad\.service\_account \- Fix return document key so it displays when using the standard Ansible documentation tools\.

<a id="microsoft-iis-3"></a>
#### microsoft\.iis

* website\_info \- Fix error when retrieving website information but none exist \- [https\://github\.com/ansible\-collections/microsoft\.iis/issues/44](https\://github\.com/ansible\-collections/microsoft\.iis/issues/44)

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* na\_ontap\_aggregate \- fixed issue with disabling software encryption in REST\.
* na\_ontap\_cg\_snapshot \- fixed issue with ZAPI by removing default value for <em class="title-reference">consistency\_type</em>\.
* na\_ontap\_cifs\_local\_group \- fixed issue with idempotency\.
* na\_ontap\_cifs\_server \- Fixed issue with updating comments when using REST API\.
* na\_ontap\_export\_policy\_rule \- Fixed issue in re\-indexing of an existing rule\.
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
* na\_ontap\_user\_role \- fixed issue when creating user role privileges with empty or null query\.
* na\_ontap\_volume \- Fixed issue with volume rename\.
* na\_ontap\_volume\_efficiency \- Fixed issue with GET timeout by adding new <em class="title-reference">rest\_timeout</em> option\.
* na\_ontap\_vserver\_audit \- updated documentation for <em class="title-reference">log</em>\.
* na\_ontap\_vserver\_delete \- Added <em class="title-reference">check\_mode</em> to the task that deletes the vserver to ensure support for dry\-run mode\.
* na\_ontap\_vserver\_delete \- Added <em class="title-reference">retry\_count</em> variable to the task that collects and deletes volumes to ensure support for retries when errors are encountered during volume deletion\.
* na\_ontap\_vserver\_delete\- Added gathering of NVMe subsystems and deletion of them before deleting the vserver to fix errors when NVMe subsystems are present\.

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

<a id="netbox-netbox-2"></a>
#### netbox\.netbox

* Add netbox version check to support service creation for netbox version prior of 4\.3
* Adjust regex pattern for character conversion for slugs
* Automatically include device and virtual\_machine scoping in sub\-object queries to prevent \"More than one result returned\" errors
* Fix integration test for circuit termination\, missing assignment
* Fix integration test for service
* Fix specifying primary\_mac\_address objects by id on vm interfaces for disambiguation
* Fix task duplicate task name in documentation that cause ansible\-lint error
* Fix typos in tag integration tests\.
* Make slug generation optional by providing <em class="title-reference">slug</em> key
* Only do slug generation in netbox\_secret if needed
* Preserve the Authorization header when creating a custom NetBox API session\, fixing authenticated requests with <em class="title-reference">validate\_certs\=false</em>
* Support for related\_object\_filter when related\_object\_type is \"object\"
* Use dedicated function to check netbox version istead of self\.full\_version for rack\.
* add parent\_object\_type and parent\_object\_id to services ALLOWED\_QUERY\_PARAMS
* nb\_device\_interface\: Fix specifying primary\_mac\_address objects by id for disambiguation
* nb\_inventory \- Fix AttributeError when <em class="title-reference">ip\_address</em> is None during DNS name lookup
* nb\_inventory \- Fix service collection for version greater than 4\.3
* nb\_inventory \- Fixed empty inventory results when netbox server URL is a non\-root path
* netbox\_service \- Fix issue 1426 \- broken netbox\_service module

<a id="ovirt-ovirt-1"></a>
#### ovirt\.ovirt

* Fix missing cluster name when starting VM \([https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/780](https\://github\.com/oVirt/ovirt\-ansible\-collection/pull/780)\)

<a id="purestorage-flasharray-4"></a>
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

<a id="purestorage-flashblade-8"></a>
#### purestorage\.flashblade

* purefb\_ad \- Ensure encryption algorithms used match the GUI values
* purefb\_alert \- Fixed issue with syntax error in update function
* purefb\_bucket\_replica \- Fixed IndexError crash in check loop
* purefb\_bucket\_replica \- Fixed issue with ItemIterator error
* purefb\_certs \- Fix the syntax to generate a CSR
* purefb\_ds \- Fixed issue when creating pre\-enabled management directory service
* purefb\_pingtrace \- Fiexed issue with XFM module when state is ping

<a id="splunk-es-8"></a>
#### splunk\.es

* Added sanity test ignore file for Ansible 2\.20 to handle pylint errors in deprecated modules\.
* Fixed ansible\-lint errors by adding missing task names in integration tests\.
* Fixed deprecated module alternatives to use fully qualified collection names \(FQCN\)\.
* Implement check mode support in action plugins\. Previously\, check mode was declared as supported but API calls were still being made\. Now all state\-changing operations \(merged\, replaced\, deleted\) properly skip API calls when running in check mode\.
* splunk\_correlation\_searches \- Fixed duplicate entries in gathered state caused by redundant loop in action plugin\.
* splunk\_finding\, splunk\_finding\_info \- Fix query by ref\_id failing to find findings due to sub\-second time precision mismatch\. The <code>earliest</code> time extracted from the ref\_id now includes a 1\-second buffer to ensure the finding falls within the search window\.

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* Fix diff in check mode by normalising the boolean values \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/295](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/295)\)
* Fix doc generation and remove need for iteritems \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/296](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/296)\)
* Fix\: remove default for states parameter in icinga\_dependency\_apply \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/290](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/290)\)

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* content\_view\_filter\_rule \- fix content\_filter\_rule\_deb\_spec to take into account desired versions

<a id="vmware-vmware-4"></a>
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

<a id="vultr-cloud-2"></a>
#### vultr\.cloud

* dns\_domain \- Removed requirement for the <code>ip</code> argument when creating a new domain \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/140](https\://github\.com/vultr/ansible\-collection\-vultr/issues/140)\)\.
* instance\, bare\_metal \- Fixed an issue where the <code>user\_data</code> response returned a JSON serialization error \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/156](https\://github\.com/vultr/ansible\-collection\-vultr/issues/156)\)\.
* startup\_script \- Fixed an issue where the <code>script</code> response returned a JSON serialization error \([https\://github\.com/vultr/ansible\-collection\-vultr/pull/162](https\://github\.com/vultr/ansible\-collection\-vultr/pull/162)\)\.

<a id="known-issues"></a>
### Known Issues

<a id="community-docker-3"></a>
#### community\.docker

* docker\_image\, docker\_image\_export \- idempotency for archiving images depends on whether the image IDs used by the image storage backend correspond to the IDs used in the tarball\'s <code>manifest\.json</code> files\. The new default backend in Docker 29 apparently uses image IDs that no longer correspond\, whence idempotency no longer works \([https\://github\.com/ansible\-collections/community\.docker/pull/1199](https\://github\.com/ansible\-collections/community\.docker/pull/1199)\)\.

<a id="community-routeros-5"></a>
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

<a id="new-plugins-2"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.loganalytics\_ingestion \- Posts task results to an Azure Log Analytics workspace using the new Logs Ingestion API\.

<a id="connection"></a>
#### Connection

* community\.proxmox\.proxmox\_qemu\_api \- Connect to QEMU VMs via the Proxmox guest agent API\.

<a id="filter-1"></a>
#### Filter

* community\.crypto\.acme\_dns\_persist\_record \- Craft a DNS record for ACME <code>dns\-persist\-01</code> challenges\.
* community\.crypto\.acme\_dns\_persist\_record\_parse \- Parse a DNS record for ACME <code>dns\-persist\-01</code> challenges\.
* community\.general\.to\_toml \- Convert variable to TOML string\.

<a id="new-modules-2"></a>
### New Modules

<a id="amazon-aws-7"></a>
#### amazon\.aws

* amazon\.aws\.ec2\_instance\_type\_info \- Retrieve information about EC2 instance types

<a id="ansible-windows-8"></a>
#### ansible\.windows

* ansible\.windows\.dsc3 \- Sets or checks DSC v3 configuration state

<a id="cisco-aci-2"></a>
#### cisco\.aci

* cisco\.aci\.aci\_fabric\_node\_decommission \- Manage the Commissioning and Decommissioning of the Fabric Node \(fabric\:RsDecommissionNode\)
* cisco\.aci\.aci\_management\_network\_instance\_profile \- Manage external management network instance profiles \(mgmt\:InstP\)\.
* cisco\.aci\.aci\_management\_network\_instance\_profile\_to\_contract \- Bind Consumed Contract to External Management Network Instance Profiles \(mgmt\:RsOoBCons\)
* cisco\.aci\.aci\_switch\_access\_config \- Manage Switch Access Policy Configuration of Leaf and Spine nodes \(infra\:NodeConfig\)\.
* cisco\.aci\.aci\_switch\_fabric\_config \- Manage Switch Fabric Policy Configuration of Leaf and Spine nodes \(fabric\:NodeConfig\)\.

<a id="cisco-ios-4"></a>
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

<a id="community-general-11"></a>
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
* community\.general\.snap\_connect \- Manages snap interface connections\.
* community\.general\.sssd\_info \- Check SSSD domain status using D\-Bus\.
* community\.general\.uv\_python \- Manage Python versions and installations using the <code>uv</code> Python package manager\.

<a id="community-libvirt-4"></a>
#### community\.libvirt

* community\.libvirt\.virt\_cloud\_instance \- Provision new virtual machines from cloud images via libvirt

<a id="community-proxmox-5"></a>
#### community\.proxmox

* community\.proxmox\.proxmox\_acme\_account \- Manages an ACME account\.
* community\.proxmox\.proxmox\_acme\_account\_info \- Retrieves information about a specific ACME account\.
* community\.proxmox\.proxmox\_acme\_accounts\_info \- Retrieves the list of ACME accounts\.
* community\.proxmox\.proxmox\_acme\_certificate \- Manages ACME SSL certificates for Proxmox VE nodes\.
* community\.proxmox\.proxmox\_acme\_certificates\_info \- Retrieves the list of certificates on a Proxmox VE node\.
* community\.proxmox\.proxmox\_acme\_plugin\_dns \- Manage ACME DNS plugins on a Proxmox VE\.
* community\.proxmox\.proxmox\_acme\_plugin\_info \- Retrieves a single ACME plugin\.
* community\.proxmox\.proxmox\_acme\_plugins\_info \- Retrieves the list of ACME plugins\.
* community\.proxmox\.proxmox\_ceph\_mds \- Add or delete Ceph Mds\.
* community\.proxmox\.proxmox\_ceph\_mgr \- Add or delete Ceph Manager\.
* community\.proxmox\.proxmox\_ceph\_mon \- Add or delete Ceph Monitor\.
* community\.proxmox\.proxmox\_ceph\_pool \- Manage Ceph Pool\.
* community\.proxmox\.proxmox\_cluster\_firewall \- Cluster\-level firewall options management for Proxmox VE cluster\.
* community\.proxmox\.proxmox\_cluster\_ha\_rules\_info \- Retrieve Proxmox VE HA rules\.
* community\.proxmox\.proxmox\_domain \- Manage authentication realms\.
* community\.proxmox\.proxmox\_domain\_sync \- Sync realms\.
* community\.proxmox\.proxmox\_node\_firewall \- Node\-level firewall options management for Proxmox VE cluster\.
* community\.proxmox\.proxmox\_node\_firewall\_info \- Get node\-level firewall options for Proxmox VE cluster\.
* community\.proxmox\.proxmox\_role \- Role management for Proxmox VE cluster\.
* community\.proxmox\.proxmox\_sendkey \- Send key presses to a Proxmox VM console\.

<a id="community-proxysql-1"></a>
#### community\.proxysql

* community\.proxysql\.proxysql\_pgsql\_hostgroup\_attributes \- Manages PostgreSQL hostgroup attributes using the ProxySQL admin interface
* community\.proxysql\.proxysql\_pgsql\_query\_rules \- Modifies pgsql query rules using the proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_query\_rules\_fast\_routing \- Modifies query rules for fast routing policies using the proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_replication\_hostgroups \- Manages replication hostgroups using the proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_servers \- Adds or removes pgsql hosts from proxysql admin interface
* community\.proxysql\.proxysql\_pgsql\_users \- Adds or removes postgresql users from proxysql admin interface

<a id="containers-podman-5"></a>
#### containers\.podman

* containers\.podman\.podman\_quadlet \- Install or remove Podman Quadlets
* containers\.podman\.podman\_quadlet\_build \- Build images for use by Podman Quadlets
* containers\.podman\.podman\_quadlet\_info \- Gather information about Podman Quadlets

<a id="dellemc-enterprise-sonic-3"></a>
#### dellemc\.enterprise\_sonic

* dellemc\.enterprise\_sonic\.sonic\_fbs\_interfaces \- Manage flow based services \(FBS\) interfaces configuration on SONiC\.
* dellemc\.enterprise\_sonic\.sonic\_mfa \- Manage Multi\-factor authentication \(MFA\) configurations on SONiC\.

<a id="fortinet-fortimanager-2"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_casb\_profile\_saasapplication\_advancedtenantcontrol \- CASB profile advanced tenant control\.
* fortinet\.fortimanager\.fmgr\_casb\_profile\_saasapplication\_advancedtenantcontrol\_attribute \- CASB advanced tenant control attribute\.
* fortinet\.fortimanager\.fmgr\_casb\_saasapplication\_inputattributes \- SaaS application input attributes\.
* fortinet\.fortimanager\.fmgr\_casb\_saasapplication\_outputattributes \- SaaS application output attributes\.
* fortinet\.fortimanager\.fmgr\_casb\_useractivity\_match\_tenantextraction \- CASB user activity tenant extraction\.
* fortinet\.fortimanager\.fmgr\_casb\_useractivity\_match\_tenantextraction\_filters \- CASB user activity tenant extraction filters\.
* fortinet\.fortimanager\.fmgr\_devprof\_log\_syslogd\_setting\_logtemplates \- System template log syslogd setting log templates
* fortinet\.fortimanager\.fmgr\_devprof\_system\_template\_interface \- System template system template interface
* fortinet\.fortimanager\.fmgr\_devprof\_system\_template\_interface\_iprange \- System template system template interface ip range
* fortinet\.fortimanager\.fmgr\_dynamic\_log\_npuserver\_servergroup \- Dynamic log npu server server group
* fortinet\.fortimanager\.fmgr\_dynamic\_log\_npuserver\_servergroup\_dynamicmapping \- Dynamic log npu server server group dynamic mapping
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_lanextension\_downlinks \- Config FortiExtender downlink interface for LAN extension\.
* fortinet\.fortimanager\.fmgr\_extensioncontroller\_extenderprofile\_lanextension\_trafficsplitservices \- Config FortiExtender traffic split interface for LAN extension\.
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
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_systemdhcpserver\_iprange \- DHCP IP range configuration\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_systemdhcpserver\_options \- DHCP options\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_managedswitch\_systeminterface \- Configure system interface on FortiSwitch\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_securitypolicy\_localaccess \- Configure allowaccess list for mgmt and internal interfaces on managed FortiSwitch units\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_switchprofile \- Configure FortiSwitch switch profile\.
* fortinet\.fortimanager\.fmgr\_system\_dnsdatabase \- Configure DNS databases\.
* fortinet\.fortimanager\.fmgr\_system\_dnsdatabase\_dnsentry \- DNS entry\.
* fortinet\.fortimanager\.fmgr\_system\_externalresource\_dynamicmapping \- System external resource dynamic mapping
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
* fortinet\.fortimanager\.fmgr\_system\_npu\_icmperrorratectrl \- Configure the rate of ICMP errors generated by this FortiGate\, which is achieved by token bucket algorithm\.
* fortinet\.fortimanager\.fmgr\_telemetrycontroller\_agent \- Configure FortiTelemetry agents managed by a FortiGate unit\.
* fortinet\.fortimanager\.fmgr\_user\_oidc \- User oidc
* fortinet\.fortimanager\.fmgr\_vpn\_certificate\_hsmlocal \- Local certificates whose keys are stored on HSM\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_manualkey \- Configure IPsec manual keys\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_phase1 \- Configure VPN remote gateway\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_phase1\_ipv4excluderange \- Configuration Method IPv4 exclude ranges\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_phase1\_ipv6excluderange \- Configuration method IPv6 exclude ranges\.
* fortinet\.fortimanager\.fmgr\_vpn\_kmipserver \- KMIP server entry configuration\.
* fortinet\.fortimanager\.fmgr\_vpn\_kmipserver\_serverlist \- KMIP server list\.
* fortinet\.fortimanager\.fmgr\_vpn\_qkd \- Configure Quantum Key Distribution servers
* fortinet\.fortimanager\.fmgr\_wanprof\_system\_sdwan\_healthcheckfortiguard \- SD\-WAN status checking or health checking\.
* fortinet\.fortimanager\.fmgr\_wanprof\_system\_sdwan\_healthcheckfortiguard\_sla \- Service level agreement
* fortinet\.fortimanager\.fmgr\_webfilter\_domainlist \- Webfilter domain list
* fortinet\.fortimanager\.fmgr\_webfilter\_domainlist\_entries \- Webfilter domain list entries
* fortinet\.fortimanager\.fmgr\_webfilter\_ftgdrisklevel \- Configure FortiGuard Web Filter risk level\.
* fortinet\.fortimanager\.fmgr\_webfilter\_profile\_ftgdwf\_risk \- FortiGuard risk level settings\.
* fortinet\.fortimanager\.fmgr\_webfilter\_urllist \- Webfilter url list
* fortinet\.fortimanager\.fmgr\_webfilter\_urllist\_entries \- Webfilter url list entries
* fortinet\.fortimanager\.fmgr\_webproxy\_explicitproxy \- Web proxy explicit proxy
* fortinet\.fortimanager\.fmgr\_webproxy\_isolatorserver \- Configure forward\-server addresses\.
* fortinet\.fortimanager\.fmgr\_webproxy\_redirectprofile \- Web proxy redirect profile
* fortinet\.fortimanager\.fmgr\_webproxy\_redirectprofile\_entries \- Web proxy redirect profile entries
* fortinet\.fortimanager\.fmgr\_ztna\_serviceconnector \- Ztna service connector
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy \- Configure ZTNA traffic forward proxy\.
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy\_quic \- Ztna traffic forward proxy quic
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy\_sslciphersuites \- Ztna traffic forward proxy ssl cipher suites
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy\_sslserverciphersuites \- Ztna traffic forward proxy ssl server cipher suites
* fortinet\.fortimanager\.fmgr\_ztna\_trafficforwardproxy\_urlroute \- Ztna traffic forward proxy url route
* fortinet\.fortimanager\.fmgr\_ztna\_webportal \- Configure ztna web\-portal\.
* fortinet\.fortimanager\.fmgr\_ztna\_webportalbookmark \- Configure ztna web\-portal bookmark\.
* fortinet\.fortimanager\.fmgr\_ztna\_webportalbookmark\_bookmarks \- Bookmark table\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy \- Configure ZTNA web\-proxy\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway \- Set IPv4 API Gateway\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6 \- Set IPv6 API Gateway\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6\_quic \- QUIC setting\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6\_realservers \- Select the real servers that this Access Proxy will distribute traffic to\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway6\_sslciphersuites \- SSL/TLS cipher suites to offer to a server\, ordered by priority\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway\_quic \- QUIC setting\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway\_realservers \- Select the real servers that this Access Proxy will distribute traffic to\.
* fortinet\.fortimanager\.fmgr\_ztna\_webproxy\_apigateway\_sslciphersuites \- SSL/TLS cipher suites to offer to a server\, ordered by priority\.

<a id="hitachivantara-vspone-block-6"></a>
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

<a id="vsp"></a>
##### Vsp

* hitachivantara\.vspone\_block\.hv\_gad\_bulk \- Manages batch GAD pairs on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_hg\_bulk \- Manages host groups in bulk on VSP block storage system with parallel processing\.
* hitachivantara\.vspone\_block\.hv\_iscsi\_target\_bulk \- Manages iscsi targets in bulk mode on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_ldev\_bulk \- Manages multiple logical devices \(LDEVs\) in bulk on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_pav\_alias \- Manages PAV \(Parallel Access Volume\) alias assignments for VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_pav\_alias\_facts \- retrieves information about PAV aliases from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_session \- Manages sessions on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_session\_facts \- Retrieves information about sessions on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_snapshot\_family\_facts \- Retrieves snapshot family information of the provided LDEV ID from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_supported\_host\_mode\_facts \- Retrieves supported host mode options information from a specified VSP block storage system\.
* hitachivantara\.vspone\_block\.hv\_truecopy\_bulk \- Manages bulk TrueCopy pairs on VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_vclone\_parent\_volume\_facts \- Retrieves virtual clone parent volume information from VSP block storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_gad \- Manages GAD pairs on VSP One block storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_gad\_consistency\_group \- Manages GAD pairs in a consistency group on VSP One block storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_gad\_consistency\_group\_facts \- Retrieves consistency group of GAD pairs from VSP One storage systems\.
* hitachivantara\.vspone\_block\.hv\_vsp\_one\_gad\_facts \- Retrieves GAD \(Global\-Active Device\) information from VSP One storage systems\.

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

<a id="netbox-netbox-3"></a>
#### netbox\.netbox

* netbox\.netbox\.netbox\_contact\_assignment \- Manage contact assignments in NetBox
* netbox\.netbox\.netbox\_data\_source \- Manage data sources in NetBox

<a id="splunk-es-9"></a>
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

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* theforeman\.foreman\.smart\_proxy\_refresh \- Refresh Smart Proxy features

<a id="vultr-cloud-3"></a>
#### vultr\.cloud

* vultr\.cloud\.load\_balancer \- Manages load balancers on Vultr
* vultr\.cloud\.load\_balancer\_info \- Get information about Vultr load balancers
* vultr\.cloud\.object\_storage\_cluster\_info \- Get information about the Vultr object storage clusters
* vultr\.cloud\.object\_storage\_info \- Get information about the Vultr object stores

<a id="unchanged-collections-2"></a>
### Unchanged Collections

* cisco\.ucs \(still version 1\.16\.0\)
* community\.ciscosmb \(still version 1\.0\.11\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.okd \(still version 5\.0\.0\)
* community\.rabbitmq \(still version 1\.6\.0\)
* dellemc\.powerflex \(still version 3\.0\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* infinidat\.infinibox \(still version 1\.6\.3\)
* netapp\.cloudmanager \(still version 21\.24\.0\)
* ngine\_io\.cloudstack \(still version 3\.0\.0\)
* openstack\.cloud \(still version 2\.5\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* vyos\.vyos \(still version 6\.0\.0\)
