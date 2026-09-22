# Ansible 15 Release Notes

This changelog describes changes since Ansible 14\.0\.0\.

- <a href="#v15-0-0a1">v15\.0\.0a1</a>
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

<a id="v15-0-0a1"></a>
## v15\.0\.0a1

- <a href="#release-summary">Release Summary</a>
- <a href="#removed-collections">Removed Collections</a>
- <a href="#added-collections">Added Collections</a>
- <a href="#ansible-core">Ansible\-core</a>
- <a href="#included-collections">Included Collections</a>
- <a href="#major-changes">Major Changes</a>
    - <a href="#ansible-core-1">Ansible\-core</a>
    - <a href="#ansible-mysql">ansible\.mysql</a>
    - <a href="#community-clickhouse">community\.clickhouse</a>
    - <a href="#community-vmware">community\.vmware</a>
    - <a href="#fortinet-fortios">fortinet\.fortios</a>
    - <a href="#netapp-ontap">netapp\.ontap</a>
    - <a href="#splunk-es">splunk\.es</a>
    - <a href="#vmware-vmware-rest">vmware\.vmware\_rest</a>
- <a href="#minor-changes">Minor Changes</a>
    - <a href="#ansible-core-2">Ansible\-core</a>
    - <a href="#amazon-aws">amazon\.aws</a>
    - <a href="#ansible-mysql-1">ansible\.mysql</a>
    - <a href="#ansible-netcommon">ansible\.netcommon</a>
    - <a href="#ansible-utils">ansible\.utils</a>
    - <a href="#ansible-windows">ansible\.windows</a>
    - <a href="#arista-eos">arista\.eos</a>
    - <a href="#cisco-ios">cisco\.ios</a>
    - <a href="#cisco-iosxr">cisco\.iosxr</a>
    - <a href="#cisco-meraki">cisco\.meraki</a>
    - <a href="#cisco-nxos">cisco\.nxos</a>
    - <a href="#cloudscale-ch-cloud">cloudscale\_ch\.cloud</a>
    - <a href="#community-aws">community\.aws</a>
    - <a href="#community-ciscosmb">community\.ciscosmb</a>
    - <a href="#community-clickhouse-1">community\.clickhouse</a>
    - <a href="#community-crypto">community\.crypto</a>
    - <a href="#community-dns">community\.dns</a>
    - <a href="#community-docker">community\.docker</a>
    - <a href="#community-general">community\.general</a>
    - <a href="#community-libvirt">community\.libvirt</a>
    - <a href="#community-okd">community\.okd</a>
    - <a href="#community-postgresql">community\.postgresql</a>
    - <a href="#community-routeros">community\.routeros</a>
    - <a href="#community-sops">community\.sops</a>
    - <a href="#community-windows">community\.windows</a>
    - <a href="#containers-podman">containers\.podman</a>
    - <a href="#dellemc-powerflex">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager">fortinet\.fortimanager</a>
    - <a href="#google-cloud">google\.cloud</a>
    - <a href="#graphiant-naas">graphiant\.naas</a>
    - <a href="#hetzner-hcloud">hetzner\.hcloud</a>
    - <a href="#hitachivantara-vspone-block">hitachivantara\.vspone\_block</a>
    - <a href="#hitachivantara-vspone-object">hitachivantara\.vspone\_object</a>
    - <a href="#ibm-storage-virtualize">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules">infoblox\.nios\_modules</a>
    - <a href="#kubernetes-core">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad">microsoft\.ad</a>
    - <a href="#microsoft-iis">microsoft\.iis</a>
    - <a href="#netapp-ontap-1">netapp\.ontap</a>
    - <a href="#netapp-eseries-santricity">netapp\_eseries\.santricity</a>
    - <a href="#ngine-io-cloudstack">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade">purestorage\.flashblade</a>
    - <a href="#splunk-es-1">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman">theforeman\.foreman</a>
    - <a href="#vmware-vmware">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-1">vmware\.vmware\_rest</a>
- <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>
    - <a href="#ansible-core-3">Ansible\-core</a>
    - <a href="#cisco-nxos-1">cisco\.nxos</a>
    - <a href="#community-okd-1">community\.okd</a>
    - <a href="#community-postgresql-1">community\.postgresql</a>
    - <a href="#hetzner-hcloud-1">hetzner\.hcloud</a>
    - <a href="#infoblox-nios-modules-1">infoblox\.nios\_modules</a>
    - <a href="#lowlydba-sqlserver-1">lowlydba\.sqlserver</a>
    - <a href="#netapp-eseries-santricity-1">netapp\_eseries\.santricity</a>
- <a href="#deprecated-features">Deprecated Features</a>
    - <a href="#ansible-core-4">Ansible\-core</a>
    - <a href="#community-clickhouse-2">community\.clickhouse</a>
    - <a href="#community-crypto-1">community\.crypto</a>
    - <a href="#community-general-1">community\.general</a>
    - <a href="#community-postgresql-2">community\.postgresql</a>
    - <a href="#community-rabbitmq">community\.rabbitmq</a>
    - <a href="#community-vmware-1">community\.vmware</a>
    - <a href="#hetzner-hcloud-2">hetzner\.hcloud</a>
    - <a href="#kubernetes-core-1">kubernetes\.core</a>
    - <a href="#netapp-eseries-santricity-2">netapp\_eseries\.santricity</a>
    - <a href="#purestorage-flashblade-1">purestorage\.flashblade</a>
    - <a href="#theforeman-foreman-1">theforeman\.foreman</a>
    - <a href="#vmware-vmware-rest-2">vmware\.vmware\_rest</a>
- <a href="#removed-features-previously-deprecated">Removed Features \(previously deprecated\)</a>
    - <a href="#ansible-core-5">Ansible\-core</a>
    - <a href="#community-postgresql-3">community\.postgresql</a>
    - <a href="#hetzner-hcloud-3">hetzner\.hcloud</a>
    - <a href="#ngine-io-cloudstack-1">ngine\_io\.cloudstack</a>
- <a href="#security-fixes">Security Fixes</a>
    - <a href="#ansible-core-6">Ansible\-core</a>
    - <a href="#ansible-posix">ansible\.posix</a>
    - <a href="#graphiant-naas-1">graphiant\.naas</a>
    - <a href="#splunk-es-2">splunk\.es</a>
- <a href="#bugfixes">Bugfixes</a>
    - <a href="#ansible-core-7">Ansible\-core</a>
    - <a href="#amazon-aws-1">amazon\.aws</a>
    - <a href="#ansible-mysql-2">ansible\.mysql</a>
    - <a href="#ansible-netcommon-1">ansible\.netcommon</a>
    - <a href="#ansible-posix-1">ansible\.posix</a>
    - <a href="#ansible-utils-1">ansible\.utils</a>
    - <a href="#ansible-windows-1">ansible\.windows</a>
    - <a href="#arista-eos-1">arista\.eos</a>
    - <a href="#cisco-ios-1">cisco\.ios</a>
    - <a href="#cisco-iosxr-1">cisco\.iosxr</a>
    - <a href="#cisco-meraki-1">cisco\.meraki</a>
    - <a href="#cisco-nxos-2">cisco\.nxos</a>
    - <a href="#cloudscale-ch-cloud-1">cloudscale\_ch\.cloud</a>
    - <a href="#community-aws-1">community\.aws</a>
    - <a href="#community-clickhouse-3">community\.clickhouse</a>
    - <a href="#community-crypto-2">community\.crypto</a>
    - <a href="#community-dns-1">community\.dns</a>
    - <a href="#community-docker-1">community\.docker</a>
    - <a href="#community-general-2">community\.general</a>
    - <a href="#community-libvirt-1">community\.libvirt</a>
    - <a href="#community-postgresql-4">community\.postgresql</a>
    - <a href="#community-sap-libs">community\.sap\_libs</a>
    - <a href="#community-vmware-2">community\.vmware</a>
    - <a href="#community-windows-1">community\.windows</a>
    - <a href="#containers-podman-1">containers\.podman</a>
    - <a href="#fortinet-fortios-1">fortinet\.fortios</a>
    - <a href="#graphiant-naas-2">graphiant\.naas</a>
    - <a href="#hetzner-hcloud-4">hetzner\.hcloud</a>
    - <a href="#ibm-storage-virtualize-1">ibm\.storage\_virtualize</a>
    - <a href="#infoblox-nios-modules-2">infoblox\.nios\_modules</a>
    - <a href="#kubernetes-core-2">kubernetes\.core</a>
    - <a href="#lowlydba-sqlserver-2">lowlydba\.sqlserver</a>
    - <a href="#microsoft-ad-1">microsoft\.ad</a>
    - <a href="#microsoft-iis-1">microsoft\.iis</a>
    - <a href="#netapp-ontap-2">netapp\.ontap</a>
    - <a href="#netapp-eseries-santricity-3">netapp\_eseries\.santricity</a>
    - <a href="#ngine-io-cloudstack-2">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-1">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-2">purestorage\.flashblade</a>
    - <a href="#splunk-es-3">splunk\.es</a>
    - <a href="#telekom-mms-icinga-director-1">telekom\_mms\.icinga\_director</a>
    - <a href="#theforeman-foreman-2">theforeman\.foreman</a>
    - <a href="#vmware-vmware-1">vmware\.vmware</a>
    - <a href="#vmware-vmware-rest-3">vmware\.vmware\_rest</a>
    - <a href="#vultr-cloud">vultr\.cloud</a>
- <a href="#known-issues">Known Issues</a>
    - <a href="#ansible-core-8">Ansible\-core</a>
- <a href="#new-plugins">New Plugins</a>
    - <a href="#callback">Callback</a>
    - <a href="#filter">Filter</a>
    - <a href="#inventory">Inventory</a>
    - <a href="#lookup">Lookup</a>
- <a href="#new-modules">New Modules</a>
    - <a href="#ansible-mysql-3">ansible\.mysql</a>
    - <a href="#ansible-windows-2">ansible\.windows</a>
    - <a href="#cloudscale-ch-cloud-2">cloudscale\_ch\.cloud</a>
    - <a href="#community-clickhouse-4">community\.clickhouse</a>
    - <a href="#community-crypto-3">community\.crypto</a>
    - <a href="#community-dns-2">community\.dns</a>
    - <a href="#community-general-3">community\.general</a>
    - <a href="#dellemc-powerflex-1">dellemc\.powerflex</a>
    - <a href="#fortinet-fortimanager-1">fortinet\.fortimanager</a>
    - <a href="#kubernetes-core-3">kubernetes\.core</a>
    - <a href="#microsoft-ad-2">microsoft\.ad</a>
    - <a href="#microsoft-iis-2">microsoft\.iis</a>
    - <a href="#netapp-ontap-3">netapp\.ontap</a>
    - <a href="#ngine-io-cloudstack-3">ngine\_io\.cloudstack</a>
    - <a href="#purestorage-flasharray-2">purestorage\.flasharray</a>
    - <a href="#purestorage-flashblade-3">purestorage\.flashblade</a>
    - <a href="#telekom-mms-icinga-director-2">telekom\_mms\.icinga\_director</a>
    - <a href="#vmware-vmware-2">vmware\.vmware</a>
- <a href="#unchanged-collections">Unchanged Collections</a>

<a id="release-summary"></a>
### Release Summary

Release Date\: 2026\-09\-22

[Porting Guide](https\://docs\.ansible\.com/projects/ansible/devel/porting\_guides\.html)

<a id="removed-collections"></a>
### Removed Collections

* cyberark\.pas \(previously included version\: 1\.0\.39\)
* netapp\.cloudmanager \(previously included version\: 21\.24\.0\)

You can still install a removed collection manually with <code>ansible\-galaxy collection install \<name\-of\-collection\></code>\.

<a id="added-collections"></a>
### Added Collections

* ansible\.mariadb \(version 6\.0\.2\)

<a id="ansible-core"></a>
### Ansible\-core

Ansible 15\.0\.0a1 contains ansible\-core version 2\.22\.0b1\.
This is a newer version than version 2\.21\.0 contained in the previous Ansible release\.

The changes are reported in the combined changelog below\.

<a id="included-collections"></a>
### Included Collections

If not mentioned explicitly\, the changes are reported in the combined changelog below\.

| Collection                   | Ansible 14.0.0 | Ansible 15.0.0a1 | Notes                                                                                                                                                                                                        |
| ---------------------------- | -------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amazon.aws                   | 11.3.0         | 11.4.0           |                                                                                                                                                                                                              |
| ansible.mariadb              |                | 6.0.2            | The collection was added to Ansible                                                                                                                                                                          |
| ansible.mysql                | 5.0.1          | 5.2.0            |                                                                                                                                                                                                              |
| ansible.netcommon            | 8.5.2          | 8.7.1            |                                                                                                                                                                                                              |
| ansible.posix                | 2.2.0          | 2.2.2            |                                                                                                                                                                                                              |
| ansible.utils                | 6.0.2          | 6.1.1            |                                                                                                                                                                                                              |
| ansible.windows              | 3.5.0          | 3.8.0            |                                                                                                                                                                                                              |
| arista.eos                   | 12.1.1         | 12.3.0           |                                                                                                                                                                                                              |
| azure.azcollection           | 3.18.0         | 4.0.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| check_point.mgmt             | 6.9.0          | 7.0.1            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.intersight             | 2.18.0         | 2.21.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| cisco.ios                    | 11.4.1         | 11.6.0           |                                                                                                                                                                                                              |
| cisco.iosxr                  | 12.3.1         | 12.5.0           |                                                                                                                                                                                                              |
| cisco.meraki                 | 2.23.2         | 2.25.1           |                                                                                                                                                                                                              |
| cisco.nxos                   | 11.2.0         | 13.0.0           |                                                                                                                                                                                                              |
| cloudscale_ch.cloud          | 2.5.3          | 2.7.0            |                                                                                                                                                                                                              |
| community.aws                | 11.0.0         | 11.1.0           |                                                                                                                                                                                                              |
| community.ciscosmb           | 1.0.11         | 1.0.12           |                                                                                                                                                                                                              |
| community.clickhouse         | 2.1.0          | 2.3.0            |                                                                                                                                                                                                              |
| community.crypto             | 3.2.1          | 3.4.0            |                                                                                                                                                                                                              |
| community.dns                | 4.0.0          | 4.1.1            |                                                                                                                                                                                                              |
| community.docker             | 5.2.0          | 5.3.0            |                                                                                                                                                                                                              |
| community.general            | 13.0.1         | 13.4.0           |                                                                                                                                                                                                              |
| community.libvirt            | 2.2.0          | 2.3.0            |                                                                                                                                                                                                              |
| community.mongodb            | 1.7.12         | 1.8.0            | There are no changes recorded in the changelog.                                                                                                                                                              |
| community.okd                | 5.0.0          | 6.0.0            |                                                                                                                                                                                                              |
| community.postgresql         | 4.2.0          | 5.0.0            |                                                                                                                                                                                                              |
| community.rabbitmq           | 1.6.0          | 1.7.0            |                                                                                                                                                                                                              |
| community.routeros           | 3.20.0         | 3.22.0           |                                                                                                                                                                                                              |
| community.sap_libs           | 1.7.0          | 1.7.1            |                                                                                                                                                                                                              |
| community.sops               | 2.3.0          | 2.4.0            |                                                                                                                                                                                                              |
| community.vmware             | 6.2.0          | 6.4.0            |                                                                                                                                                                                                              |
| community.windows            | 3.1.0          | 3.3.0            |                                                                                                                                                                                                              |
| containers.podman            | 1.20.1         | 1.20.2           |                                                                                                                                                                                                              |
| cyberark.conjur              | 1.3.9          | 1.3.12           | You can find the collection's changelog at [https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md](https://github.com/cyberark/ansible-conjur-collection/blob/master/CHANGELOG.md). |
| dellemc.openmanage           | 10.0.2         | 10.0.3           | The collection did not have a changelog in this version.                                                                                                                                                     |
| dellemc.powerflex            | 3.0.0          | 3.1.0            |                                                                                                                                                                                                              |
| f5networks.f5_modules        | 1.41.0         | 1.44.0           | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| fortinet.fortimanager        | 2.14.0         | 2.15.0           |                                                                                                                                                                                                              |
| fortinet.fortios             | 2.5.1          | 2.6.0            |                                                                                                                                                                                                              |
| google.cloud                 | 1.13.0         | 1.14.0           |                                                                                                                                                                                                              |
| graphiant.naas               | 26.4.0         | 26.8.0           |                                                                                                                                                                                                              |
| hetzner.hcloud               | 6.9.0          | 7.1.0            |                                                                                                                                                                                                              |
| hitachivantara.vspone_block  | 4.8.1          | 4.8.3            |                                                                                                                                                                                                              |
| hitachivantara.vspone_object | 1.1.1          | 1.2.0            |                                                                                                                                                                                                              |
| ibm.storage_virtualize       | 3.3.0          | 3.4.0            |                                                                                                                                                                                                              |
| infinidat.infinibox          | 1.6.3          | 1.8.6            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| infoblox.nios_modules        | 1.9.0          | 1.10.0           |                                                                                                                                                                                                              |
| kubernetes.core              | 6.4.0          | 6.6.0            |                                                                                                                                                                                                              |
| kubevirt.core                | 2.2.4          | 2.3.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| lowlydba.sqlserver           | 2.8.1          | 3.1.0            |                                                                                                                                                                                                              |
| microsoft.ad                 | 1.10.0         | 1.12.1           |                                                                                                                                                                                                              |
| microsoft.iis                | 1.1.0          | 1.3.0            |                                                                                                                                                                                                              |
| netapp.ontap                 | 23.5.0         | 23.6.0           |                                                                                                                                                                                                              |
| netapp_eseries.santricity    | 2.0.1          | 2.0.3            |                                                                                                                                                                                                              |
| ngine_io.cloudstack          | 3.0.0          | 3.3.0            |                                                                                                                                                                                                              |
| openstack.cloud              | 2.5.0          | 2.6.0            | Unfortunately, this collection does not provide changelog data in a format that can be processed by the changelog generator.                                                                                 |
| purestorage.flasharray       | 1.42.0         | 1.43.0           |                                                                                                                                                                                                              |
| purestorage.flashblade       | 1.24.0         | 1.26.0           |                                                                                                                                                                                                              |
| splunk.es                    | 6.0.0          | 6.0.1            |                                                                                                                                                                                                              |
| telekom_mms.icinga_director  | 2.5.1          | 2.6.1            |                                                                                                                                                                                                              |
| theforeman.foreman           | 5.11.0         | 5.12.0           |                                                                                                                                                                                                              |
| vmware.vmware                | 2.8.0          | 2.10.0           |                                                                                                                                                                                                              |
| vmware.vmware_rest           | 4.10.0         | 4.11.0           |                                                                                                                                                                                                              |
| vultr.cloud                  | 1.14.0         | 1.14.1           |                                                                                                                                                                                                              |

<a id="major-changes"></a>
### Major Changes

<a id="ansible-core-1"></a>
#### Ansible\-core

* Secret masking \- Ansible now automatically redacts known secret values from the output it generates\, such as <code>display</code> output \(including verbose\, warning\, deprecation\, and error output\)\, module logging\, and task results passed to callback plugins\. Masking is non\-destructive\; the real value remains available to tasks\, conditionals\, and registered variables\, only the rendered output is redacted with <code>\$REDACTED\$</code>\. Secrets shorter than 4 characters are never masked\, secrets of 4 to 6 characters are only masked when they appear as a whole word or when they overlap or are adjacent to another secret\, and secrets longer than 65536 characters are matched on their first 65536 characters\.
* Secret masking \- add the <code>ansible\.module\_utils\.secrets</code> public API for working with secrets manually\. It provides <code>register\_secret</code> and <code>register\_secrets</code> to register values that should be redacted from masked output\, and <code>mask\_secrets</code> to redact any registered secrets from a string\. The API can be used on the controller and in Python modules\; the new <code>Ansible\.Secrets</code> C\# module\_util provides the equivalent <code>\[Ansible\.Secrets\.SecretMasker\]\:\:RegisterSecret\(\)</code> and <code>MaskString\(\)</code> methods for PowerShell modules\. Secrets registered inside a module or worker process are propagated back to the controller so they are also masked there\.
* ansible \- Add support for Python 3\.15\.
* ansible \- Drop support for Python 3\.12 on the controller\.
* callback plugins \- callback plugin authors should opt into the new secret masking behaviour by setting the class attribute <code>ANSIBLE\_SUPPORTS\_MASKING \= True</code>\. A callback that sets this receives the unmasked task result and must ensure any secrets are redacted before they are written\, either by emitting output through <code>Display</code> which masks automatically\, or by passing the values through <code>ansible\.module\_utils\.secrets\.mask\_secrets\(\)</code> before writing them elsewhere\. Callbacks that do not set the attribute continue to receive task results with any registered secrets replaced by <code>\$REDACTED\$</code>\, matching the redacted results they receive today\. This implicit masking exists only for backwards compatibility with existing callbacks and will be removed in a future release\, at which point all callbacks will receive unmasked results and must mask them manually if not using <code>Display</code>\. Task\-level <code>no\_log\: true</code> continues to censor the entire result regardless of this attribute\.

<a id="ansible-mysql"></a>
#### ansible\.mysql

* MariaDB support is deprecated and is scheduled for removal in version 6\.0\.0 of this collection\. If you already use this collection with MariaDB\, please install the <em class="title-reference">ansible\.mariadb</em> collection from Ansible Galaxy and change FQCNs in tasks in your playbooks to use ansible\.mariadb equivalents\, for example\, <em class="title-reference">ansible\.mysql\.mysql\_info</em> \-\> <em class="title-reference">ansible\.mariadb\.mariadb\_info</em>\, etc\. No other changes are needed\. This collection was cloned to the <em class="title-reference">ansible\.mariadb</em> collection to allow its contributors and maintainers to focus on MariaDB\-related automation development\. This <em class="title-reference">ansible\.mysql</em> collection still supports MariaDB \(only bugfixes and security fixes\) until its release 6\.0\.0 \(not earlier than mid 2027\)\, then its support will be dropped\!

<a id="community-clickhouse"></a>
#### community\.clickhouse

* clickhouse\_named\_collection \- new module to add/modify/delete named collections in database\.

<a id="community-vmware"></a>
#### community\.vmware

* Bump required <code>vmware\.vmware</code> collection version to 2\.10\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.

<a id="fortinet-fortios"></a>
#### fortinet\.fortios

* Supported multiple versions of log fact modules\.
* Supported new versions 7\.6\.7 and 8\.0\.0\.
* Updated the Q\&A for importing a certificate in the fortios\_certificate\_remote module\.

<a id="netapp-ontap"></a>
#### netapp\.ontap

* na\_ontap\_cg\_snapshot \- AWS Lambda support added to the module\.
* na\_ontap\_cli\_timeout \- AWS Lambda support added to the module\.
* na\_ontap\_ems\_config \- AWS Lambda support added to the module\.
* na\_ontap\_ems\_destination \- AWS Lambda support added to the module\.
* na\_ontap\_ems\_filter \- AWS Lambda support added to the module\.
* na\_ontap\_fdsd \- AWS Lambda support added to the module\.
* na\_ontap\_fdsp \- AWS Lambda support added to the module\.
* na\_ontap\_fdspt \- AWS Lambda support added to the module\.
* na\_ontap\_fdss \- AWS Lambda support added to the module\.
* na\_ontap\_file\_security\_permissions\_acl \- AWS Lambda support added to the module\.
* na\_ontap\_fpolicy\_event \- AWS Lambda support added to the module\.
* na\_ontap\_fpolicy\_ext\_engine \- AWS Lambda support added to the module\.
* na\_ontap\_fpolicy\_policy \- AWS Lambda support added to the module\.
* na\_ontap\_fpolicy\_scope \- AWS Lambda support added to the module\.
* na\_ontap\_fpolicy\_status \- AWS Lambda support added to the module\.
* na\_ontap\_kerberos\_interface \- AWS Lambda support added to the module\.
* na\_ontap\_kerberos\_realm \- AWS Lambda support added to the module\.
* na\_ontap\_login\_messages \- AWS Lambda support added to the module\.
* na\_ontap\_nvme\_namespace \- AWS Lambda support added to the module\.
* na\_ontap\_publickey \- AWS Lambda support added to the module\.
* na\_ontap\_rest\_cli \- AWS Lambda support added to the module\.
* na\_ontap\_security\_key\_manager \- AWS Lambda support added to the module\.
* na\_ontap\_security\_ssh \- AWS Lambda support added to the module\.
* na\_ontap\_snaplock\_clock \- AWS Lambda support added to the module\.
* na\_ontap\_unix\_group \- AWS Lambda support added to the module\.
* na\_ontap\_unix\_user \- AWS Lambda support added to the module\.
* na\_ontap\_user \- AWS Lambda support added to the module\.
* na\_ontap\_user\_role \- AWS Lambda support added to the module\.
* na\_ontap\_vscan \- AWS Lambda support added to the module\.
* na\_ontap\_vscan\_on\_access\_policy \- AWS Lambda support added to the module\.
* na\_ontap\_vscan\_on\_demand\_task \- AWS Lambda support added to the module\.
* na\_ontap\_vscan\_scanner\_pool \- AWS Lambda support added to the module\.
* na\_ontap\_vserver\_audit \- AWS Lambda support added to the module\.

<a id="splunk-es"></a>
#### splunk\.es

* ci \- integration tests now run against both Splunk Server 9\.4 and 10\.4 with Enterprise Security \(ES\)\, providing full coverage across supported major versions and catching regressions against real Splunk ES instances\.

<a id="vmware-vmware-rest"></a>
#### vmware\.vmware\_rest

* Update minimum required ansible\-core version to 2\.16 in meta/runtime\.yml

<a id="minor-changes"></a>
### Minor Changes

<a id="ansible-core-2"></a>
#### Ansible\-core

* Add new OrderedSet class for situations a unique ordered list is needed
* Role and play argument spec validation now supports <code>no\_log</code>\. Variables labeled as <code>no\_log</code> are redacted from masked output\. \([https\://github\.com/ansible/ansible/issues/84498](https\://github\.com/ansible/ansible/issues/84498)\)
* Secret masking \- add the internal <code>\_SECRETS\_INPUT\_FILES</code> config option to pre\-seed values to redact from the output of <code>ansible</code>\, <code>ansible\-playbook</code>\, and <code>ansible\-console</code>\. Each file is YAML or JSON containing a mapping with a <code>version</code> key \(currently only <code>1</code>\) and a <code>secrets</code> key listing the string values to mask\. A file with the executable bit set is run instead of read\, and its stdout is parsed as the document\.
* Secret masking \- the following values are now automatically registered as secrets and redacted from masked output\: vault passwords provided by prompt\, file\, or script\; the decrypted plaintext of vault encrypted values and every string or numeric value in a vault encrypted vars file\; passwords entered for <code>\-\-ask\-pass</code> and <code>\-\-ask\-become\-pass</code>\; <code>no\_log</code> module option values\; the <code>become\_pass</code> option of the <code>sudo</code>\, <code>su</code>\, and <code>runas</code> become plugins\; the <code>password</code>\, <code>private\_key</code>\, and <code>private\_key\_passphrase</code> options of the <code>ssh</code> connection plugin\; the <code>password</code> option of the <code>winrm</code> and <code>psrp</code> connection plugins and the <code>certificate\_key\_password</code> option of <code>psrp</code>\; the <code>password</code> option of the <code>url</code> lookup\; the values returned by the <code>password</code> and <code>unvault</code> lookups\; the secret passed to the <code>vault</code> and <code>unvault</code> filters\; the user input of the <code>pause</code> action when <code>echo</code> is <code>false</code>\; and values entered for a play <code>vars\_prompt</code> when <code>private</code> is <code>true</code> \(the default\)\.
* ansible\-galaxy \- sort the FILES\.json for ansible galaxy build based on name\. \([https\://github\.com/ansible/ansible/issues/82792](https\://github\.com/ansible/ansible/issues/82792)\)\.
* ansible\-test \- Added a timeout callback that dumps thread stacks when the test execution deadline defined by <code>ansible\-test env \-\-timeout</code> is approaching\.
* ansible\-test \- Generate <code>dist\_info</code> when running tests\.
* ansible\-test \- Remove support for Windows Server 2016 managed remote\.
* ansible\-test \- Replace Alpine 3\.23 container and remote with 3\.24\.
* ansible\-test \- Replace Fedora 43 container and remote with 44\.
* ansible\-test \- Replace FreeBSD 14\.4 remote with 14\.5\.
* ansible\-test \- Replace FreeBSD 15\.0 remote with 15\.1\.
* ansible\-test \- Replace RHEL 10\.1 remote with 10\.2\.
* ansible\-test \- Replace RHEL 9\.7 remote with 9\.8\.
* ansible\-test \- Replace Ubuntu 22\.04 container and remote with 26\.04\.
* ansible\-test \- Update ansible\-test utility containers \(http\-test\-container\, pypi\-test\-container\, ansible\-test\-utility\-container\)\.
* ansible\-test \- Update sanity test requirements\.
* ansible\-test \- Upgrade <code>coverage</code> for Python 3\.10 and later\.
* ansible\-test \- Upgrade the distro\-specific test containers\.
* config \- add a <code>secret</code> boolean keyword to plugin configuration option definitions\. When set to <code>true</code>\, the resolved value of the option is automatically registered as a secret for output masking\, regardless of the source it was set from \(env\, ini\, vars\, CLI\, or plugin arguments\)\. It is only supported for the <code>str</code>\, <code>string</code>\, and <code>list</code> types \(string elements of a list are registered\)\; using it with any other type raises an error when the plugin configuration is loaded\.
* debugging \- Add signal \(<code>USR1</code>\) handler to provide insight into executing code stacks \([https\://github\.com/ansible/ansible/issues/84451](https\://github\.com/ansible/ansible/issues/84451)\)
* distribution facts \- add the <code>ansible\_distribution\_cpe\_name</code> fact\, exposing the <code>CPE\_NAME</code> published in the os\-release file when the distribution provides one\.
* dnf \- clarify that the <code>exclude</code> parameter works with all <code>state</code> values\, not just <code>present</code> and <code>latest</code> \([https\://github\.com/ansible/ansible/issues/87026](https\://github\.com/ansible/ansible/issues/87026)\)
* dnf5 \- clarify that the <code>exclude</code> parameter works with all <code>state</code> values\, not just <code>present</code> and <code>latest</code> \([https\://github\.com/ansible/ansible/issues/87026](https\://github\.com/ansible/ansible/issues/87026)\)
* filter \- <code>regex\_escape</code> implement <code>re\_type\=posix\_extended</code> for POSIX ERE literal escaping \([https\://github\.com/ansible/ansible/pull/86949](https\://github\.com/ansible/ansible/pull/86949)\)\.
* is\_mac \- add a <code>strict</code> keyword\-only argument that anchors the validation regex with <code>\\Z</code> instead of <code>\$</code>\, rejecting a MAC address with a trailing newline\. The default \(<code>strict\=False</code>\) preserves the historical behavior \([https\://github\.com/ansible/ansible/pull/87420](https\://github\.com/ansible/ansible/pull/87420)\)\.
* jsonfile cache plugin \- add <code>persist\_metadata</code> option to configure whether or not to preserve metadata like deprecation notices\. Setting the option to <code>False</code> restores the filename and format used prior to ansible\-core 2\.19\.
* mask\_url function in module\_utils to allow for masking of auth data embedded in urls\.
* module\_utils\.urls \- Added <code>is\_fetch\_success\(\)</code> function for protocol\-aware success detection of <code>fetch\_url\(\)</code> responses\.
* parallel fact gathering \- the async wrapper now considers the timeout when determining whether to kill the process running the module\. Previously\, a 5 second sleep occurred twice before checking if the job had remaining time\.
* psrp connection plugin \- Remove explicit error handling support for Windows Server 2016\.
* setup module now adds \'by\-path\' information to device\_links\.
* ssh connection plugin \- inspect <code>SSH\_ASKPASS\_PROMPT</code> in <code>SSH\_ASKPASS</code> script for reliability \([https\://github\.com/ansible/ansible/issues/86319](https\://github\.com/ansible/ansible/issues/86319)\)
* ssh\, winrm\, and psrp connection plugins \- the raw stdout and stderr of executed commands are no longer displayed at increased verbosity \(<code>\-vvv</code> for <code>ssh</code>\, <code>\-vvvvv</code> for <code>winrm</code> and <code>psrp</code>\)\, only the return code is shown\. Module output can contain secrets\, such as <code>no\_log</code> option values\, which are only registered for masking once the result has been parsed\, so displaying the raw output before then could leak them\. The raw output is still available with <code>ANSIBLE\_DEBUG\=1</code> if needed for debugging purposes\.
* task results \- Python and Powershell modules do not include the <code>invocation</code> task result key by default\. Injection of the <code>invocation</code> task result key for Python and Powershell modules may be enabled with the var\-settable <code>INJECT\_INVOCATION</code> config item\. Most callbacks mask <code>invocation</code> when displaying a task or loop item result\.
* url <em class="title-reference">multipart/form\-data</em> \- Replace Python <code>email</code> multipart generator with custom generator\, allowing for binary content without <code>Content\-Transfer\-Encoding</code>
* user \- add support for move\_home in Alpine Linux \([https\://github\.com/ansible/ansible/issues/85521](https\://github\.com/ansible/ansible/issues/85521)\)\.
* validate\-modules sanity test \- allow lookups to use <code>positional</code> to mark which options are actually positional arguments\, similar to test and filter plugins \([https\://github\.com/ansible/ansible/pull/86986](https\://github\.com/ansible/ansible/pull/86986)\)\.
* windows \- Compress input data sent over for module execution to reduce the amount of data transferred per module execution\.
* winrm connection plugin \- improved error message to include target host when stdin transfer fails \([https\://github\.com/ansible/ansible/issues/86749](https\://github\.com/ansible/ansible/issues/86749)\)
* worker process \- When controller and forked child workers must share a TTY\, the <code>WORKER\_SESSION\_ISOLATION</code> config item can be set to <code>false</code> \(via variable/config/envvar\) to disable forked worker session isolation\.

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

<a id="ansible-mysql-1"></a>
#### ansible\.mysql

* CI \- MySQL 8\.0\.38 has been removed from the CI test matrix because MySQL 8\.0 reached End of Life in April 2026\. The collection still supports MySQL 8\.0 at runtime through version\-conditional code paths\.
* CI \- PyMySQL 0\.9\.3 and 1\.0\.2 have been removed from the CI test matrix\. PyMySQL 0\.9\.3 is unmaintained and has an unfixed CVE\-2024\-36039\. PyMySQL 1\.0\.2 is redundant with 1\.1\.1 as both cover the same code path\. PyMySQL 0\.10\.1 has been promoted to the main test matrix\.
* modules \- add a warning to redirect users to use ansible\.mariadb when a MariaDB server is detected \([https\://github\.com/ansible\-collections/ansible\.mysql/issues/845](https\://github\.com/ansible\-collections/ansible\.mysql/issues/845)\)\.

<a id="ansible-netcommon"></a>
#### ansible\.netcommon

* Remediate deprecated <code>ansible\.module\_utils\.common\.\_collections\_compat</code> module and replaced with <code>collections\.abc</code> from the Python standard library\.
* Remediate deprecated <code>ansible\.module\_utils\.six</code> module and replaced it with native Python 3 equivalents like <code>pickle</code>\, <code>zip</code>\, <code>urllib\.parse</code>\, <code>urllib\.error</code> etc\.
* Remediate deprecated <code>to\_text</code> and <code>to\_bytes</code> from <code>ansible\.module\_utils\.\_text</code> and replaced with <code>ansible\.module\_utils\.common\.text\.converters</code>\.
* Remediate deprecated <code>warnings</code> parameter in <code>exit\_json</code> calls by introducing <code>emit\_warnings</code> and <code>warn\_and\_exit</code> utility functions in <code>plugins/module\_utils/network/common/utils\.py</code> to centralize warning emission logic\. The following modules were updated to use <code>warn\_and\_exit</code> \- <code>cli\_backup</code>\, <code>cli\_command</code>\, <code>cli\_config</code>\, <code>cli\_restore</code>\, <code>grpc\_config</code>\, <code>grpc\_get</code>\, <code>netconf\_config</code>\, <code>netconf\_get</code>\, <code>netconf\_rpc</code>\, <code>restconf\_config</code>\, <code>restconf\_get</code>\. <code>ResourceModule</code> base class in <code>rm\_base/resource\_module\.py</code> was updated to use <code>emit\_warnings</code>\, which automatically addresses the deprecation for all downstream collections \(e\.g\. cisco\.iosxr\, cisco\.ios\, arista\.eos\)\.
* network\_cli \- Add transcript recording support to capture command/response pairs exchanged over SSH sessions\. Enable via <code>ANSIBLE\_NETWORK\_CLI\_RECORD\=1</code> environment variable\. Recordings are written as JSONL files to <code>/tmp/transcript\-recordings/</code> \(configurable via <code>ANSIBLE\_NETWORK\_CLI\_RECORD\_PATH</code>\)\. Useful for generating offline test fixtures for CISSHGO\-based integration testing\.

<a id="ansible-utils"></a>
#### ansible\.utils

* remove warning message about potential instability of ipaddr \(it has been stable for years\)

<a id="ansible-windows"></a>
#### ansible\.windows

* reboot \- Replace deprecated <code>datetime\.datetime\.utcnow\(\)</code> with <code>datetime\.now\(timezone\.utc\)</code> for Python 3\.12\+ compatibility\.
* win\_acl \- Add check mode support so the module reports whether changes would be made without modifying ACL permissions \([https\://github\.com/ansible\-collections/ansible\.windows/issues/911](https\://github\.com/ansible\-collections/ansible\.windows/issues/911)\)\.
* win\_copy \- Add diff support to win\_copy and win\_template when copying single files only\. Copying multiple files will still not produce any diff output \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/16](https\://github\.com/ansible\-collections/ansible\.windows/issues/16)
* win\_dhcp\_lease \- add support for computername parameter\.
* win\_dns\_zone \- Added <code>directory\_partition</code> parameter to support storing AD\-integrated zones in custom application directory partitions for fine\-grained replication control \([https\://github\.com/ansible\-collections/ansible\.windows/issues/901](https\://github\.com/ansible\-collections/ansible\.windows/issues/901)\)\.
* win\_ping \- Added support for running on non\-Windows targets
* win\_powershell \- Added support for running on non\-Windows targets
* win\_powershell \- Allow sensitive\_parameters entries with neither <code>value</code> nor <code>username</code>/<code>password</code> specified\, passing <code>\$null</code> as the parameter value instead of an empty SecureString\.
* win\_tempfile \- Added support for running on non\-Windows targets
* win\_tempfile \- Changed the default for <code>path</code> to be <code>None</code> rather than <code>\%TEMP\%</code>\. The module will instead use the result of <code>\[System\.IO\.Path\]\:\:GetTempPath\(\)</code> to determine the temporary directory to use which on Windows will typically be the same as <code>\%TEMP\%</code>\.
* win\_updates \- Add maximum\_retries\_on\_failed\_updates option to control how many attempts the module can take at installing a rolled back update\. \(Fixes [https\://github\.com/ansible\-collections/ansible\.windows/issues/762](https\://github\.com/ansible\-collections/ansible\.windows/issues/762)\)
* windows \- Validated that the collection works correctly with Python 3\.12 \([https\://issues\.redhat\.com/browse/ACA\-5197](https\://issues\.redhat\.com/browse/ACA\-5197)\)\.

<a id="arista-eos"></a>
#### arista\.eos

* Remediate deprecated <code>warnings</code> parameter in <code>exit\_json</code> calls by using <code>emit\_warnings</code> from <code>ansible\.netcommon</code> across all arista\.eos modules to address deprecation warning from ansible\-core 2\.23\.
* Remediate deprecated <em class="title-reference">ansible\.module\_utils\.common\.\_collections\_compat</em> module and replaced with <em class="title-reference">collections\.abc</em> from the Python standard library\.
* Updated all <code>ConfigBase</code>\-based resource modules \(<code>eos\_acl\_interfaces</code>\, <code>eos\_acls</code>\, <code>eos\_interfaces</code>\, <code>eos\_l2\_interfaces</code>\, <code>eos\_l3\_interfaces</code>\, <code>eos\_lacp</code>\, <code>eos\_lacp\_interfaces</code>\, <code>eos\_lag\_interfaces</code>\, <code>eos\_lldp\_global</code>\, <code>eos\_lldp\_interfaces</code>\, <code>eos\_ospfv2</code>\, <code>eos\_static\_routes</code>\, <code>eos\_vlans</code>\) to emit warnings via <code>AnsibleModule\.warn\(\)</code> before calling <code>exit\_json</code>\.
* Updated all standalone modules \(<code>eos\_banner</code>\, <code>eos\_command</code>\, <code>eos\_config</code>\, <code>eos\_eapi</code>\, <code>eos\_facts</code>\, <code>eos\_lldp</code>\, <code>eos\_user</code>\, <code>eos\_vrf</code>\) to emit warnings via <code>AnsibleModule\.warn\(\)</code> before calling <code>exit\_json</code>\.

<a id="cisco-ios"></a>
#### cisco\.ios

* Remediate deprecated <code>warnings</code> parameter in <code>exit\_json</code> calls by using <code>emit\_warnings</code> from <code>ansible\.netcommon</code> across cisco\.ios modules to address deprecation warning from ansible\-core 2\.23\.
* Remove <code>ansible\.module\_utils\.six</code> usage in favour of Python 3 builtins to prepare for ansible\-core 2\.24 removal\.
* Replace deprecated <code>ansible\.module\_utils\.\_text</code> imports with <code>ansible\.module\_utils\.common\.text\.converters</code>\.
* Replace deprecated <code>ansible\.module\_utils\.common\.\_collections\_compat</code> with <code>collections\.abc</code> from the Python standard library\.
* Updated all <code>ResourceModule</code>\-based resource modules to emit warnings via <code>AnsibleModule\.warn\(\)</code> before calling <code>exit\_json</code>\.
* Updated standalone modules \(<code>ios\_banner</code>\, <code>ios\_command</code>\, <code>ios\_config</code>\, <code>ios\_facts</code>\, <code>ios\_ping</code>\, <code>ios\_system</code>\, <code>ios\_user</code>\, <code>ios\_vrf</code>\) to emit warnings via <code>AnsibleModule\.warn\(\)</code> before calling <code>exit\_json</code>\.
* ios\_snmp\_server \- add <code>traps\.vrrpv3</code> bool parameter to configure <code>snmp\-server enable traps vrrpv3</code>\.

<a id="cisco-iosxr"></a>
#### cisco\.iosxr

* Fixed for iosxr\_lldp\_interfaces\, iosxr\_lldp\_global\, iosxr\_lag\_interfaces\, iosxr\_lacp\_interfaces\, iosxr\_lacp\, iosxr\_l3\_interfaces\, iosxr\_l2\_interfaces\, iosxr\_interfaces\, iosxr\_acls\, iosxr\_static\_routes\, iosxr\_ping\, iosxr\_banner\, iosxr\_config\, iosxr\_system\, iosxr\_command\, iosxr\_user\, iosxr\_netconf
* For iosxr\_vrf\_interfaces\, iosxr\_vrf\_global\, iosxr\_vrf\_address\_family\, iosxr\_snmp\_server\, iosxr\_route\_maps\, iosxr\_prefix\_lists\, iosxr\_ospfv3\, iosxr\_ospfv2\, iosxr\_ospf\_interfaces\, iosxr\_ntp\_global\, iosxr\_logging\_global\, iosxr\_hostname\, iosxr\_bgp\_templates\, iosxr\_bgp\_neighbor\_address\_family\, iosxr\_bgp\_global\, iosxr\_bgp\_address\_family\, iosxr\_acl\_interfaces modules\, fix will be done via netcommon ResourceModule\.result change \(Upstream to iosxr\)
* No changes for fail\_json since it uses msg format already\, except for ping module where currently warning is not being set\.
* Remediate deprecated \'to\_bytes\' from \'ansible\.module\_utils\.\_text\' and replaced with ansible\.module\_utils\.common\.text\.converters\.
* Remediate deprecated \'to\_text\' from \'ansible\.module\_utils\.\_text\' and replaced with ansible\.module\_utils\.common\.text\.converters\.
* Remediate deprecated <code>warnings</code> parameter in <code>exit\_json</code> calls by using <code>AnsibleModule\.warn\(\)</code> across all iosxr modules to address deprecation warning from ansible\-core 2\.23\.
* Remediate deprecated <em class="title-reference">ansible\.module\_utils\.common\.\_collections\_compat</em> module and replaced with <em class="title-reference">collections\.abc</em> from the Python standard library\.

<a id="cisco-meraki"></a>
#### cisco\.meraki

* Fixed problem with networks\_wireless\_ssids module\.
* devices\_appliance\_interfaces\_ports\_update \- Added new plugin to update appliance interface port settings on a device\.
* devices\_appliance\_performance\_info \- Updated documentation terminology from <em class="title-reference">MX</em> to <em class="title-reference">Secure Appliance or Secure Router</em>\.
* devices\_appliance\_uplinks\_settings \- Updated documentation terminology from <em class="title-reference">MX appliance</em> to <em class="title-reference">secure router or security appliance</em>\.
* devices\_camera\_clip\_info \- Added new plugin to retrieve camera clip information\.
* devices\_camera\_clip\_info \- Clarified the <em class="title-reference">imagerId</em> parameter documentation for multi\-imager cameras\.
* devices\_cellular\_geolocations \- Added new plugin to update cellular geolocation settings on a device\.
* devices\_cellular\_uplinks\_bands\_masks\_update \- Added new plugin to update cellular uplink band masks on a device\.
* devices\_live\_tools\_ports\_cycle \- Added new plugin to request a live port cycle on a device\.
* devices\_live\_tools\_ports\_cycle\_info \- Added new plugin to retrieve the results of a live port cycle request\.
* devices\_live\_tools\_ports\_status \- Added new plugin to request live port status information for a device\.
* devices\_live\_tools\_ports\_status\_info \- Added new plugin to retrieve the results of a live port status request\.
* devices\_live\_tools\_power\_usage \- Added new plugin to request live power usage information for a device\.
* devices\_live\_tools\_power\_usage\_info \- Added new plugin to retrieve the results of a live power usage request\.
* devices\_live\_tools\_routing\_table\_lookups \- Added new plugin to request a live routing table lookup on a device\.
* devices\_live\_tools\_routing\_table\_lookups\_info \- Added new plugin to retrieve the results of a routing table lookup request\.
* devices\_live\_tools\_routing\_table\_summaries \- Added new plugin to request a live routing table summary on a device\.
* devices\_live\_tools\_routing\_table\_summaries\_info \- Added new plugin to retrieve the results of a routing table summary request\.
* devices\_switch\_ports\_cycle \- Clarified that this module targets non\-Catalyst MS devices\; use devices\_live\_tools\_ports\_cycle for Catalyst support\.
* devices\_switch\_routing\_interfaces \- Added support for the new <em class="title-reference">mtu</em> parameter on switch routing interfaces\.
* networks\_appliance\_devices\_redundancy \- Added new plugin to manage appliance device redundancy settings\.
* networks\_appliance\_devices\_redundancy\_swap \- Added new plugin to swap the primary and warm spare appliance in a redundant pair\.
* networks\_appliance\_firewall\_l7\_firewall\_rules \- Documented the <em class="title-reference">rules\.value</em> shape per rule type\, including the new allowedCountries/blockedCountries values and their backward\-compatible whitelistedCountries/blacklistedCountries aliases\.
* networks\_appliance\_interfaces\_l3 \- Added new plugin to manage layer 3 appliance interfaces\.
* networks\_appliance\_ports \- Added support for the new <em class="title-reference">sgt</em> \(Security Group Tag\) parameter\.
* networks\_appliance\_prefixes\_delegated\_statics \- Clarified that the <em class="title-reference">interfaces</em> suboption is required when the prefix origin type is <em class="title-reference">internet</em>\.
* networks\_appliance\_umbrella\_domains\_exclusions \- Added new plugin to manage Cisco Umbrella domain exclusions\.
* networks\_appliance\_umbrella\_policies\_add \- Added new plugin to add Cisco Umbrella protection policies\.
* networks\_appliance\_umbrella\_policies\_remove \- Added new plugin to remove Cisco Umbrella protection policies\.
* networks\_appliance\_umbrella\_protection \- Added new plugin to manage Cisco Umbrella protection settings\.
* networks\_appliance\_uplinks\_nat \- Added new plugin to manage appliance uplink NAT settings\.
* networks\_appliance\_vlans \- Added support for the new <em class="title-reference">sgt</em> \(Security Group Tag\) and <em class="title-reference">vrf</em> configuration options on VLANs\.
* networks\_appliance\_vpn\_bgp \- Clarified that the <em class="title-reference">asNumber</em> setting is only configurable for Auto VPN BGP networks\.
* networks\_appliance\_vpn\_site\_to\_site\_vpn \- Added support for the new <em class="title-reference">sgt</em> \(Security Group Tag\) parameter for site\-to\-site VPN peers\.
* networks\_camera\_quality\_retention\_profiles \- Added quality and retention support for additional camera models \(MV14\, MV24\, MV34\, MV44X\, MV54N\, MV64\, MV74\, MV94\) and documented the new <em class="title-reference">axisVideoQuality</em> response field\.
* networks\_devices\_syslog\_servers \- Added new plugin to update network device syslog server settings\.
* networks\_snmp \- Added support for the new <em class="title-reference">authentication</em> and <em class="title-reference">privacy</em> SNMPv3 parameters\.
* networks\_switch\_settings \- Added support for the new <em class="title-reference">portChannelFallback</em> parameter\.
* networks\_switch\_stacks \- Added support for the new <em class="title-reference">members</em> parameter to manage switch stack membership\.
* networks\_switch\_stacks\_routing\_interfaces \- Added support for the new <em class="title-reference">mtu</em> parameter on switch stack routing interfaces\.
* networks\_syslog\_servers \- Documented that this plugin is deprecated in favor of networks\_devices\_syslog\_servers\.
* networks\_syslog\_servers\_info \- Documented that this plugin is deprecated in favor of organizations\_devices\_syslog\_servers\_by\_network\_info\.
* networks\_webhooks\_http\_servers \- Documented the new built\-in Push payload template \(<em class="title-reference">wpt\_00008</em>\)\.
* networks\_wireless\_rf\_profiles \- Added support for the new 320 MHz channel width option on the 6 GHz radio band\.
* networks\_wireless\_ssids \- Added support for the new <em class="title-reference">security</em> parameter\, including WPA3 encryption settings \(<em class="title-reference">akms</em> and <em class="title-reference">ciphers</em>\)\.
* networks\_wireless\_ssids\_info \- Documented additional read\-only SSID response fields\, including <em class="title-reference">psk</em>\, <em class="title-reference">dot11w</em>\, <em class="title-reference">dot11r</em>\, RADIUS server <em class="title-reference">id</em>/<em class="title-reference">radsecEnabled</em>\, and the new <em class="title-reference">security</em> block\.
* networks\_wireless\_ssids\_splash\_settings \- Added support for the new <em class="title-reference">userConsent</em> parameter \(consent message and required flag\)\.
* organizations \- Added support for the new <em class="title-reference">privacy</em> parameter\.
* organizations\_api\_rest\_provisioning\_pipelines\_jobs\_info \- Added new plugin to retrieve REST API provisioning pipeline job information\.
* organizations\_api\_rest\_provisioning\_pipelines\_jobs\_overviews\_by\_pipeline\_info \- Added new plugin\.
* organizations\_api\_rest\_provisioning\_pipelines\_jobs\_overviews\_by\_pipeline\_info \- Documented the new <em class="title-reference">byJobOperation</em> breakdown in the pipeline jobs overview response\.
* organizations\_appliance\_devices\_interfaces\_l3\_info \- Added new plugin to retrieve layer 3 appliance interfaces across an organization\.
* organizations\_appliance\_devices\_interfaces\_ports\_by\_device\_info \- Added new plugin to retrieve appliance interface ports by device across an organization\.
* organizations\_appliance\_devices\_ports\_transceivers\_readings\_history\_by\_device\_info \- Added new plugin to retrieve appliance port transceiver reading history by device\.
* organizations\_appliance\_devices\_redundancy\_by\_network\_info \- Added new plugin to retrieve appliance device redundancy status by network\.
* organizations\_appliance\_interfaces\_packets\_overviews\_by\_device\_info \- Added new plugin to retrieve appliance interface packet overviews by device\.
* organizations\_appliance\_routing\_vrfs\_settings \- Added new plugin to manage appliance VRF routing settings\.
* organizations\_appliance\_routing\_vrfs\_settings\_info \- Added new plugin to retrieve appliance VRF routing settings\.
* organizations\_appliance\_uplinks\_nat\_by\_network\_info \- Added new plugin\.
* organizations\_appliance\_vpn\_third\_party\_vpn\_peers \- Added the new umbrella\_short\_lived and secure IPsec policy presets\, and documented the new BGP <em class="title-reference">receiveLimit</em> field\.
* organizations\_assurance\_alerts\_dismiss \- Clarified that missing or inaccessible alert IDs return a 404\.
* organizations\_assurance\_alerts\_overview\_by\_type\_info \- Added the new <em class="title-reference">includeDeviceTags</em> and <em class="title-reference">includeNetworks</em> query parameters and documented the expanded alert overview response fields\.
* organizations\_assurance\_alerts\_restore \- Clarified that missing or inaccessible alert IDs return a 404\.
* organizations\_devices\_cellular\_data\_devices\_info \- Added new plugin to retrieve devices eligible for cellular data plans\.
* organizations\_devices\_cellular\_data\_profiles \- Added new plugin to manage cellular data profiles\.
* organizations\_devices\_cellular\_data\_profiles\_assignments\_batch\_create \- Added new plugin to batch create cellular data profile assignments\.
* organizations\_devices\_cellular\_data\_profiles\_assignments\_bulk\_delete \- Added new plugin to bulk delete cellular data profile assignments\.
* organizations\_devices\_cellular\_data\_profiles\_assignments\_info \- Added new plugin to retrieve cellular data profile assignments\.
* organizations\_devices\_cellular\_data\_profiles\_info \- Added new plugin to retrieve cellular data profiles\.
* organizations\_devices\_cellular\_data\_usage\_by\_device\_info \- Added new plugin to retrieve current cellular data usage by device\.
* organizations\_devices\_cellular\_data\_usage\_history\_by\_device\_by\_interval\_info \- Added new plugin to retrieve historical cellular data usage by device and interval\.
* organizations\_devices\_cellular\_geolocations\_info \- Added new plugin to retrieve the latest cellular geolocation for devices\.
* organizations\_devices\_cellular\_uplinks\_bands\_by\_device\_info \- Added new plugin to retrieve cellular uplink bands by device\.
* organizations\_devices\_cellular\_uplinks\_towers\_by\_device\_info \- Added new plugin to retrieve cellular uplink tower information by device\.
* organizations\_devices\_syslog\_servers\_by\_network\_info \- Added new plugin to retrieve device syslog servers by network\.
* organizations\_devices\_syslog\_servers\_roles\_by\_network\_info \- Added new plugin to retrieve device syslog server roles by network\.
* organizations\_inventory\_orders\_preview \- Documented the new <em class="title-reference">resolution</em> field in the inventory order preview response\.
* organizations\_login\_security \- Added support for the new <em class="title-reference">enforceLockedIpSessions</em> parameter\.
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
* organizations\_policy\_objects \- Documented that the <em class="title-reference">ipAndMask</em> policy object type is deprecated in favor of <em class="title-reference">cidr</em>\.
* organizations\_sase\_connectors\_batch\_create \- Added new plugin to batch create SASE connectors\.
* organizations\_sase\_connectors\_batch\_delete \- Added new plugin to batch delete SASE connectors\.
* organizations\_sase\_connectors\_info \- Added new plugin to retrieve SASE connector information\.
* organizations\_sase\_integrations \- Added new plugin to manage SASE integrations\.
* organizations\_sase\_integrations\_info \- Added new plugin to retrieve SASE integrations\.
* organizations\_sase\_regions\_info \- Added new plugin to retrieve SASE region information\.
* organizations\_sase\_sites \- Added new plugin to manage SASE sites\.
* organizations\_sase\_sites\_attach \- Added new plugin to attach networks to SASE sites\.
* organizations\_sase\_sites\_connectivity\_history\_by\_site\_info \- Added new plugin to retrieve SASE site connectivity history\.
* organizations\_sase\_sites\_connectivity\_overview\_info \- Added new plugin to retrieve SASE site connectivity overview\.
* organizations\_sase\_sites\_detach \- Added new plugin to detach networks from SASE sites\.
* organizations\_sase\_sites\_info \- Added new plugin to retrieve SASE site information\.

<a id="cisco-nxos"></a>
#### cisco\.nxos

* Add significant number of testcases across multiple modules that were not covered due to which sonar coverage failures were being caused
* All legacy modules \- add <code>emit\_warnings\(\)</code> call from <code>ansible\_collections\.ansible\.netcommon\.plugins\.module\_utils\.network\.common\.utils</code> before <code>module\.exit\_json\(\)</code> to pop and emit the <code>warnings</code> key via <code>module\.warn\(\)</code>\, suppressing the deprecation warning raised by ansible\-core 2\.23\+\.
* All legacy modules that already imported from <code>ansible\_collections\.ansible\.netcommon\.plugins\.module\_utils\.network\.common\.utils</code> \- extend the existing import block to include <code>emit\_warnings</code>\.
* The following files \- <code>plugins/cliconf/nxos\.py</code>\, <code>plugins/httpapi/nxos\.py</code>\, <code>plugins/module\_utils/network/nxos/nxos\.py</code>\, <code>plugins/module\_utils/network/nxos/facts/snmp\_server/snmp\_server\.py</code> \- replace deprecated <code>ansible\.module\_utils\.\_text</code> and <code>ansible\.module\_utils\.common\.\_collections\_compat</code> imports with their modern equivalents \(<code>ansible\.module\_utils\.common\.text\.converters</code> and <code>collections\.abc</code>\)\.
* nxos\_hsrp\_interfaces \- Adds an additional parameter called <code>hold\_msec</code> to separately support hold interval values in milliseconds
* nxos\_hsrp\_interfaces \- In <code>replaced</code> and <code>overridden</code> states\, negate removed sub\-options for <code>preempt</code> before applying the desired configuration\. This aligns command generation with NX\-OS additive CLI behavior when only part of a preempt delay setting is specified\.

<a id="cloudscale-ch-cloud"></a>
#### cloudscale\_ch\.cloud

* Add missing load\_balancer parameter to the floating IP module\.

<a id="community-aws"></a>
#### community\.aws

* ecs\_task \- Add <code>wait\_complete</code> parameter to wait for tasks to stop and return container exit codes after <code>run</code> or <code>start</code> operations \([https\://github\.com/ansible\-collections/community\.aws/pull/2409](https\://github\.com/ansible\-collections/community\.aws/pull/2409)\)\.
* msk\_cluster \- Fix tags on cluster creation \([https\://github\.com/ansible\-collections/community\.aws/pull/2324](https\://github\.com/ansible\-collections/community\.aws/pull/2324)\)\.
* route53\_wait \- make <code>skipped</code> and <code>invocation</code> keys optional in result validation to support modern Ansible loop structures \([https\://github\.com/ansible\-collections/community\.aws/pull/2447](https\://github\.com/ansible\-collections/community\.aws/pull/2447)\)\.

<a id="community-ciscosmb"></a>
#### community\.ciscosmb

* Solve CI doesn\'t satisfy ACP requirements
* Update unit tests to use collection\-local helpers instead of community\.internal\_test\_tools\, and make set\_module\_args compatible with current Ansible module argument serialization\.

<a id="community-clickhouse-1"></a>
#### community\.clickhouse

* Added warning about using unsupported server version\.
* Fetch server version only once during opening connection to a database\.
* Refactored user/role settings for better maintainability and improved idempotency\. Since now settings option accepts both list\(old\) argument or dictionary\(new\)\. Profiles are moved to a separate option\. \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/178](https\://github\.com/ansible\-collections/community\.clickhouse/pull/178)\)\.
* clickhouse\_client \- Change how server errors are handled\. Previously\, error code 497 \(ACCESS\_DENIED / not enough privileges\) was always treated as success with no way to disable this behavior\. Old behavior is preserved by default\. It is now possible to control which error codes are treated as success using the new <code>success\_on</code> parameter \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/117](https\://github\.com/ansible\-collections/community\.clickhouse/issues/117)\)\.
* clickhouse\_db \- check if passed engine is supported before executing query\. Module checks if passed name exists in system\.database\_engines \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/214](https\://github\.com/ansible\-collections/community\.clickhouse/pull/214)\)\.
* clickhouse\_db \- support for changing database comment\. Requires ClickHouse server version \>\= 25\.8 \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/189](https\://github\.com/ansible\-collections/community\.clickhouse/issues/189)\)\.
* clickhouse\_db \- validate passed identifiers\. Close them in backticks to keep it consistent with other modules \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/214](https\://github\.com/ansible\-collections/community\.clickhouse/pull/214)\)\.
* clickhouse\_grants \- pass cluster name in ON CLUSTER clause in backticks\.
* clickhouse\_named\_collection \- improve SQL injection protection with parameterized queries\, identifier validation\, and new <em class="title-reference">query\_parameters</em> output\.
* clickhouse\_quota \- inherit cluster documentation and spec option\.
* clickhouse\_quota \- pass quota and cluster name in backticks in queries\.
* clickhouse\_role \- added the <code>profile</code> argument to apply settings profiles to role \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/196](https\://github\.com/ansible\-collections/community\.clickhouse/pull/196)\)\.
* clickhouse\_role \- close names in backticks\. Now names for roles and cluster will be validated\. Those containing \` or will be rejected\. Other will eb safe passed without risk of breaking query\.
* clickhouse\_user \- added the <code>profile</code> argument to apply settings profiles to user \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/196](https\://github\.com/ansible\-collections/community\.clickhouse/pull/196)\)\.
* clickhouse\_user \- module on success returns query\_parameters with password used for query\.
* clickhouse\_user \- normalize generating query\. Now identifiers like user names will be closed in backticks\.
* clickhouse\_user \- pass password to ClickHouse using query parameters\. Prevent breaking query when containing soem special characters\.

<a id="community-crypto"></a>
#### community\.crypto

* Update vendored list of OID names from OpenSSL \([https\://github\.com/ansible\-collections/community\.crypto/pull/1057](https\://github\.com/ansible\-collections/community\.crypto/pull/1057)\)\.
* openssl\_privatekey\*\, openssl\_publickey\*\, openssl\_csr\*\, x509\_certificate\* \- support ML\-DSA\-\{44\,65\,87\} private keys \([https\://github\.com/ansible\-collections/community\.crypto/issues/1056](https\://github\.com/ansible\-collections/community\.crypto/issues/1056)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/1058](https\://github\.com/ansible\-collections/community\.crypto/pull/1058)\)\.

<a id="community-dns"></a>
#### community\.dns

* hetzner\_dns\_record\_info\, hetzner\_dns\_record\_set\_info \- if <code>zone\_name</code> is provided together with <code>record</code> for the new JSON API\, and <code>what</code> is not <code>all\_records</code>\, also filter by prefix\. This was already done if <code>prefix</code> had been specified \([https\://github\.com/ansible\-collections/community\.dns/pull/340](https\://github\.com/ansible\-collections/community\.dns/pull/340)\)\.\"
* unquote\_txt filter plugin \- a new <code>lenient</code> option allows to be more lenient when decoding TXT values\. Right now this allows missing ending double quotation marks \([https\://github\.com/ansible\-collections/community\.dns/pull/339](https\://github\.com/ansible\-collections/community\.dns/pull/339)\)\.

<a id="community-docker"></a>
#### community\.docker

* docker\_swarm\_service \- add <code>command\_as\_args</code> option\. When set to <code>true</code>\, <code>command</code> and <code>args</code> are concatenated and mapped to <code>ContainerSpec\.Args</code> \(matching <code>docker service create IMAGE \[COMMAND\] \[ARG\.\.\.\]</code>\)\, preserving the image <code>ENTRYPOINT</code>\. The default remains <code>false</code> \(historical mapping of <code>command</code> to <code>ContainerSpec\.Command</code> and <code>args</code> to <code>ContainerSpec\.Args</code>\) for backward compatibility \([https\://github\.com/ansible\-collections/community\.docker/issues/1044](https\://github\.com/ansible\-collections/community\.docker/issues/1044)\, [https\://github\.com/ansible\-collections/community\.docker/issues/212](https\://github\.com/ansible\-collections/community\.docker/issues/212)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1307](https\://github\.com/ansible\-collections/community\.docker/pull/1307)\)\.

<a id="community-general"></a>
#### community\.general

* The collection now depends on community\.library\_inventory\_filtering\_v1\. This runtime dependency is used by inventory plugins only\, and will be automatically installed by <code>ansible\-galaxy collection install</code>\. If you install community\.general by cloning its repository or extracting its release tarball to a specific location\, you also need to make sure to install community\.library\_inventory\_filtering\_v1 manually if you use one of the affected inventory plugins \([https\://github\.com/ansible\-collections/community\.general/pull/12302](https\://github\.com/ansible\-collections/community\.general/pull/12302)\)\.
* archive \- add <code>zstd</code> as a format choice \([https\://github\.com/ansible\-collections/community\.general/issues/3455](https\://github\.com/ansible\-collections/community\.general/issues/3455)\, [https\://github\.com/ansible\-collections/community\.general/pull/12497](https\://github\.com/ansible\-collections/community\.general/pull/12497)\)\.
* archive \- use context managers when reading tar checksums \([https\://github\.com/ansible\-collections/community\.general/pull/12569](https\://github\.com/ansible\-collections/community\.general/pull/12569)\)\.
* bitwarden lookup plugin \- add <code>sync</code> option to sync items from the vault before lookup \([https\://github\.com/ansible\-collections/community\.general/pull/12377](https\://github\.com/ansible\-collections/community\.general/pull/12377)\)\.
* consul modules \- add a <code>url</code> option taking the address of the Consul agent as a whole\; the existing <code>host</code>\, <code>port</code> and <code>scheme</code> options each override the matching component of it\. This does not cover <code>community\.general\.consul</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12216](https\://github\.com/ansible\-collections/community\.general/pull/12216)\)\.
* consul modules \- connection options now fall back to the <code>CONSUL\_HTTP\_ADDR</code>\, <code>CONSUL\_HTTP\_SSL</code>\, <code>CONSUL\_HTTP\_SSL\_VERIFY</code>\, <code>CONSUL\_HTTP\_TOKEN</code> and <code>CONSUL\_CACERT</code> environment variables when not specified\. This applies to all consul modules except <code>community\.general\.consul</code>\, which does not use the shared connection option handling yet \([https\://github\.com/ansible\-collections/community\.general/pull/12216](https\://github\.com/ansible\-collections/community\.general/pull/12216)\)\.
* consul\_kv \- refactored KV store helpers into shared <code>\_ConsulModule</code> methods to prepare for the <code>consul\_kv\_info</code> module \([https\://github\.com/ansible\-collections/community\.general/pull/12515](https\://github\.com/ansible\-collections/community\.general/pull/12515)\)\.
* consul\_kv \- the module no longer requires the <code>py\-consul</code> Python library\, and is now part of the <code>community\.general\.consul</code> action group \([https\://github\.com/ansible\-collections/community\.general/pull/12221](https\://github\.com/ansible\-collections/community\.general/pull/12221)\)\.
* consul\_kv lookup plugin \- add <code>empty\_value</code> option to control what is returned for null Consul values \([https\://github\.com/ansible\-collections/community\.general/issues/11039](https\://github\.com/ansible\-collections/community\.general/issues/11039)\, [https\://github\.com/ansible\-collections/community\.general/pull/12120](https\://github\.com/ansible\-collections/community\.general/pull/12120)\)\.
* dnf\_config\_manager \- lookup path to the <code>dnf</code> binary in <code>PATH</code>\. It used to be fixed to <code>/usr/bin/dnf</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12219](https\://github\.com/ansible\-collections/community\.general/pull/12219)\)\.
* filesystem \- adds GFS2 support \([https\://github\.com/ansible\-collections/community\.general/pull/12285](https\://github\.com/ansible\-collections/community\.general/pull/12285)\)\.
* filesystem \- print a warning if <code>blkid \-c</code> probe fails and show the error message from <code>blkid</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12500](https\://github\.com/ansible\-collections/community\.general/pull/12500)\)\.
* github\_repo \- added <code>visibility</code> option to set repository visibility to <code>public</code>\, <code>private</code>\, or <code>internal</code> \([https\://github\.com/ansible\-collections/community\.general/issues/6219](https\://github\.com/ansible\-collections/community\.general/issues/6219)\, [https\://github\.com/ansible\-collections/community\.general/pull/12557](https\://github\.com/ansible\-collections/community\.general/pull/12557)\)\.
* gitlab\_hook \- add <code>branch\_filter\_strategy</code> option to control how <code>push\_events\_branch\_filter</code> filters push events\, which allows filtering branches by a regular expression \([https\://github\.com/ansible\-collections/community\.general/pull/12618](https\://github\.com/ansible\-collections/community\.general/pull/12618)\)\.
* gitlab\_hook \- add <code>custom\_webhook\_template</code> option to configure a custom webhook payload template on project hooks \([https\://github\.com/ansible\-collections/community\.general/issues/11233](https\://github\.com/ansible\-collections/community\.general/issues/11233)\, [https\://github\.com/ansible\-collections/community\.general/pull/12496](https\://github\.com/ansible\-collections/community\.general/pull/12496)\)\.
* gitlab\_runners inventory plugin \- wrap the Gitlab API object in a context mananger\, and only create the <code>gitlab\_runners</code> group after the API request was successful \([https\://github\.com/ansible\-collections/community\.general/pull/12378](https\://github\.com/ansible\-collections/community\.general/pull/12378)\)\.
* homebrew\_tap \- add <code>trust</code> option to control whether Homebrew trusts the tapped repositories \([https\://github\.com/ansible\-collections/community\.general/issues/12220](https\://github\.com/ansible\-collections/community\.general/issues/12220)\, [https\://github\.com/ansible\-collections/community\.general/pull/12503](https\://github\.com/ansible\-collections/community\.general/pull/12503)\)\.
* incus connection plugin \- add <code>remote\_user\_id\_command</code> option to configure the command used to retrieve the UID and GID of the remote user \([https\://github\.com/ansible\-collections/community\.general/pull/12646](https\://github\.com/ansible\-collections/community\.general/pull/12646)\)\.
* influxdb\_user \- add <code>force\_password\_update</code> option to always update the password when <code>user\_password</code> is set\, working around InfluxDB installations that do not enforce authentication \([https\://github\.com/ansible\-collections/community\.general/issues/3824](https\://github\.com/ansible\-collections/community\.general/issues/3824)\, [https\://github\.com/ansible\-collections/community\.general/pull/12654](https\://github\.com/ansible\-collections/community\.general/pull/12654)\)\.
* ini\_file \- use named groups in the internal option\-matching regular expressions \([https\://github\.com/ansible\-collections/community\.general/pull/12493](https\://github\.com/ansible\-collections/community\.general/pull/12493)\)\.
* keycloak\_realm \- add <code>max\_secondary\_auth\_failures</code> parameter to configure brute force detection for secondary authentication mechanisms \([https\://github\.com/ansible\-collections/community\.general/pull/12087](https\://github\.com/ansible\-collections/community\.general/pull/12087)\)\.
* kopia\_repository\, kopia\_repository\_info \- normalize handling of CLI parameters across all <code>kopia\_\*</code> modules \([https\://github\.com/ansible\-collections/community\.general/pull/12360](https\://github\.com/ansible\-collections/community\.general/pull/12360)\)\.
* mail \- add the <code>inline</code> option to embed images in the message body via <code>Content\-ID</code>\, so an HTML body can reference them with <code>cid\:\.\.\.</code> instead of an external URL \([https\://github\.com/ansible\-collections/community\.general/pull/12480](https\://github\.com/ansible\-collections/community\.general/pull/12480)\)\.
* maven\_artifact \- add <code>keep\_name\_only\_when\_resolved</code> option to opt in to the documented scope of <code>keep\_name</code>\, where it only controls the destination filename when <code>version</code> is resolved dynamically \(<code>latest</code> or <code>version\_by\_spec</code>\)\; previously <code>keep\_name</code> also affected the filename with a fixed <code>version</code>\, contradicting its documentation \([https\://github\.com/ansible\-collections/community\.general/pull/12606](https\://github\.com/ansible\-collections/community\.general/pull/12606)\, [https\://github\.com/ansible\-collections/community\.general/issues/4796](https\://github\.com/ansible\-collections/community\.general/issues/4796)\)\.
* maven\_artifact \- use Ansible construct to express the default value of parameter \([https\://github\.com/ansible\-collections/community\.general/pull/12411](https\://github\.com/ansible\-collections/community\.general/pull/12411)\)\.
* nmap inventory plugin \- allow <code>address</code> to be a list of networks/IP ranges to scan\, in addition to a single string \([https\://github\.com/ansible\-collections/community\.general/issues/12379](https\://github\.com/ansible\-collections/community\.general/issues/12379)\, [https\://github\.com/ansible\-collections/community\.general/pull/12384](https\://github\.com/ansible\-collections/community\.general/pull/12384)\)\.
* odbc \- add <code>autocommit</code> option to support statements that must run outside of a transaction \([https\://github\.com/ansible\-collections/community\.general/issues/4173](https\://github\.com/ansible\-collections/community\.general/issues/4173)\, [https\://github\.com/ansible\-collections/community\.general/issues/8577](https\://github\.com/ansible\-collections/community\.general/issues/8577)\, [https\://github\.com/ansible\-collections/community\.general/pull/12595](https\://github\.com/ansible\-collections/community\.general/pull/12595)\)\.
* one\_vm \- add <code>update\_attributes</code> parameter to merge USER\_TEMPLATE key/value pairs onto existing VMs via the <code>one\.vm\.update</code> API with append/merge semantics\, enabling idempotent attribute updates on running VMs without teardown \([https\://github\.com/ansible\-collections/community\.general/issues/12498](https\://github\.com/ansible\-collections/community\.general/issues/12498)\, [https\://github\.com/ansible\-collections/community\.general/pull/12536](https\://github\.com/ansible\-collections/community\.general/pull/12536)\)\.
* opennebula inventory plugin \- add <code>prefer\_existing\_ansible\_host</code> option to skip setting <code>ansible\_host</code> when the host already has one from an earlier inventory source \([https\://github\.com/ansible\-collections/community\.general/pull/12417](https\://github\.com/ansible\-collections/community\.general/pull/12417)\)\.
* opennebula inventory plugin \- add new option <code>filter</code> that allows to filter hosts by variables \([https\://github\.com/ansible\-collections/community\.general/pull/12302](https\://github\.com/ansible\-collections/community\.general/pull/12302)\)\.
* opennebula inventory plugin \- expose <code>UNAME</code> \(VM owner\) and <code>GNAME</code> \(VM group\) as host variables\, enabling <code>keyed\_groups</code> based on ownership \([https\://github\.com/ansible\-collections/community\.general/pull/12417](https\://github\.com/ansible\-collections/community\.general/pull/12417)\)\.
* pacemaker\_cluster \- add support for unmaintenance state \([https\://github\.com/ansible\-collections/community\.general/issues/12362](https\://github\.com/ansible\-collections/community\.general/issues/12362)\, [https\://github\.com/ansible\-collections/community\.general/pull/12364](https\://github\.com/ansible\-collections/community\.general/pull/12364)\)\.
* passwordstore lookup plugin \- add <code>keep\_trailing\_newline</code> option to preserve the trailing newline when <code>returnall\=true</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12589](https\://github\.com/ansible\-collections/community\.general/pull/12589)\, [https\://github\.com/ansible\-collections/community\.general/issues/3616](https\://github\.com/ansible\-collections/community\.general/issues/3616)\)\.
* passwordstore lookup plugin \- make <code>directory</code> configurable through <code>ansible\.cfg</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12298](https\://github\.com/ansible\-collections/community\.general/pull/12298)\)\.
* slack \- add <code>reply\_broadcast</code> option to allow a threaded reply \(<code>thread\_id</code>\) to also be broadcast to the main channel \([https\://github\.com/ansible\-collections/community\.general/pull/12535](https\://github\.com/ansible\-collections/community\.general/pull/12535)\)\.
* slack \- added support for uploading files to channels and threads using the new Slack WebAPI \([https\://github\.com/ansible\-collections/community\.general/pull/12032](https\://github\.com/ansible\-collections/community\.general/pull/12032)\)\.
* sudoers \- add <code>defaults</code> parameter to allow specifying <code>Defaults</code> directives scoped to the user or group in the generated sudoers file \([https\://github\.com/ansible\-collections/community\.general/pull/12186](https\://github\.com/ansible\-collections/community\.general/pull/12186)\)\.
* tss lookup plugin \- cache the <code>TSSClient</code> per process and credential identity so OAuth2 token grants are reused across lookups \(rebuilding the client and retrying the lookup once on a stale\-token 4xx\, while 5xx and other errors propagate unchanged\)\, and add a <code>token\_path\_source</code> option whose <code>auto</code> value lets <code>python\-tss\-sdk</code> auto\-detect the Secret Server or Delinea Platform token endpoint \([https\://github\.com/ansible\-collections/community\.general/pull/12328](https\://github\.com/ansible\-collections/community\.general/pull/12328)\)\.
* vmadm \- add <code>bootrom</code> option to support UEFI boot for <code>bhyve</code> VMs \([https\://github\.com/ansible\-collections/community\.general/pull/12601](https\://github\.com/ansible\-collections/community\.general/pull/12601)\, [https\://github\.com/ansible\-collections/community\.general/issues/4282](https\://github\.com/ansible\-collections/community\.general/issues/4282)\)\.
* xbps \- include <code>stdout</code> and <code>stderr</code> from the last executed command in module output \([https\://github\.com/ansible\-collections/community\.general/issues/2478](https\://github\.com/ansible\-collections/community\.general/issues/2478)\, [https\://github\.com/ansible\-collections/community\.general/pull/12234](https\://github\.com/ansible\-collections/community\.general/pull/12234)\)\.
* xenserver\_guest\_info \- add VDI <code>uuid</code> and <code>vdi\_type</code> \(VHD/QCOW2\) fields to disk info output \([https\://github\.com/ansible\-collections/community\.general/issues/11998](https\://github\.com/ansible\-collections/community\.general/issues/11998)\, [https\://github\.com/ansible\-collections/community\.general/pull/12119](https\://github\.com/ansible\-collections/community\.general/pull/12119)\)\.
* zypper \- add <code>install\_recommends</code> option to explicitly control installation of recommended packages \([https\://github\.com/ansible\-collections/community\.general/issues/3497](https\://github\.com/ansible\-collections/community\.general/issues/3497)\, [https\://github\.com/ansible\-collections/community\.general/pull/12648](https\://github\.com/ansible\-collections/community\.general/pull/12648)\)\.

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

<a id="community-okd"></a>
#### community\.okd

* Add sanity test ignore files for ansible\-core 2\.20 and 2\.21 \([https\://github\.com/openshift/community\.okd/pull/286](https\://github\.com/openshift/community\.okd/pull/286)\)\.
* Replace <code>ansible\.module\_utils\.six\.moves\.urllib\_parse</code> import with Python 3 <code>urllib\.parse</code> in <code>openshift\_auth</code> module \([https\://github\.com/openshift/community\.okd/pull/291](https\://github\.com/openshift/community\.okd/pull/291)\)\.
* Replace <code>ansible\.module\_utils\.six</code> imports \(<code>iteritems</code>\, <code>string\_types</code>\) with Python 3 stdlib equivalents \([https\://github\.com/openshift/community\.okd/pull/286](https\://github\.com/openshift/community\.okd/pull/286)\)\.
* Replace deprecated <code>ansible\.module\_utils\.\_text</code> imports with <code>ansible\.module\_utils\.common\.text\.converters</code> to fix compatibility with ansible\-core 2\.24\+ \([https\://github\.com/openshift/community\.okd/issues/275](https\://github\.com/openshift/community\.okd/issues/275)\)\.

<a id="community-postgresql"></a>
#### community\.postgresql

* Replace the deprecated <code>ansible\.module\_utils\.six</code> compatibility shims with their Python standard library equivalents\. <code>ansible\.module\_utils\.six</code> is deprecated in ansible\-core 2\.21 and is scheduled for removal in 2\.24\.
* postgresql\_membership \- add <code>granted\_by\_any</code>\, at the top level and per <code>memberships</code> row\, to manage every grant of a membership whoever made it\, as the deprecated <code>groups</code> option does\. <code>GRANT</code> then names no granting role\, and <code>state\=absent</code> and <code>state\=exact</code> revoke every grant of the membership\. On every version\, <code>groups</code> of <code>x</code> is <code>granted\_by\_any</code> set with a <code>memberships</code> row of <code>x</code>\.
* postgresql\_membership \- add the <code>grants</code> and <code>effective\_options</code> return values\, listing every grant of the requested pairs and the options the target role effectively holds\.
* postgresql\_membership \- add the <code>memberships</code> option\, one membership per row with its own <code>target\_roles</code>\, <code>granted\_by</code>\, <code>admin\_option</code>\, <code>inherit\_option</code> and <code>set\_option</code>\, applied in one transaction\. Mutually exclusive with <code>groups</code>\; the top\-level <code>target\_roles</code> is the default for rows that name none \([https\://github\.com/ansible\-collections/community\.postgresql/issues/757](https\://github\.com/ansible\-collections/community\.postgresql/issues/757)\)\.
* postgresql\_membership \- move <code>PgMembership</code> from the <code>postgres</code> module\_utils into a new <code>membership</code> module\_utils\, split into <code>PgMembershipByPair</code> \(the <code>groups</code> model\) and <code>PgMembershipByGrantor</code> \(the <code>memberships</code> model\)\. External importers have to follow the move\.
* postgresql\_membership \- with <code>memberships</code>\, check before emitting a <code>GRANT</code> that the connecting role has the privileges of the granting role and that the granting role holds <code>ADMIN OPTION</code> on the group\, and fail naming the roles that do hold it\. The deprecated <code>groups</code> option gets the privilege check for every granting role it finds recorded before it revokes\. A task with nothing left to do is not checked\.

<a id="community-routeros"></a>
#### community\.routeros

* api\_info\, api\_modify \- add support for the <code>dhcp\-agent\-circuit\-id</code>\, <code>dhcp\-agent\-remote\-id</code>\, <code>dhcpv6\-agent\-circuit\-id</code>\, <code>dhcpv6\-agent\-remote\-id</code>\, and <code>dhcpv6\-snooping</code> parameters in the <code>interface bridge</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/468](https\://github\.com/ansible\-collections/community\.routeros/pull/468)\)\.
* api\_info\, api\_modify \- add support for the <code>trusted\-dhcpv6</code> parameter in the <code>interface bridge port</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/468](https\://github\.com/ansible\-collections/community\.routeros/pull/468)\)\.
* api\_info\, api\_modify \- add the <code>from\-pool\-policy</code> field to the <code>ipv6 address</code> path for RouterOS 7\.23 and newer \([https\://github\.com/ansible\-collections/community\.routeros/pull/469](https\://github\.com/ansible\-collections/community\.routeros/pull/469)\)\.
* api\_info\, api\_modify \- adds support for multiple <code>restart\-\*</code> and <code>stop\-on\-unhealthy</code> parameters in the <code>container</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/474](https\://github\.com/ansible\-collections/community\.routeros/pull/474)\)\.
* api\_info\, api\_modify \- adds support for the <code>privileged</code> parameter in the <code>container</code> path for RouterOS \>\= 7\.24 \([https\://github\.com/ansible\-collections/community\.routeros/pull/474](https\://github\.com/ansible\-collections/community\.routeros/pull/474)\)\.
* api\_info\, api\_modify \- remove support for the deprecated <code>add\-dhcp\-option82</code> parameter in the <code>interface bridge</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/468](https\://github\.com/ansible\-collections/community\.routeros/pull/468)\)\.
* api\_info\, api\_modify \- removed support for the <code>auto\-restart\-interval</code> parameter in the <code>container</code> path for RouterOS \>\= 7\.23 \([https\://github\.com/ansible\-collections/community\.routeros/pull/474](https\://github\.com/ansible\-collections/community\.routeros/pull/474)\)\.
* api\_info\, api\_modify \- the <code>address</code> parameter in the <code>ip service</code> path was renamed to <code>available\-from</code> for RouterOS \>\= 7\.24\. The old name is still supported for RouterOS \< 7\.24 \([https\://github\.com/ansible\-collections/community\.routeros/pull/475](https\://github\.com/ansible\-collections/community\.routeros/pull/475)\)\.

<a id="community-sops"></a>
#### community\.sops

* Support OpenSuSE Tumbleweed \(and probably also Leap\) in the community\.sops\.install role\. Right now only Tumbleweed is tested in CI\, so support for Leap has not been verified \([https\://github\.com/ansible\-collections/community\.sops/pull/299](https\://github\.com/ansible\-collections/community\.sops/pull/299)\)\.

<a id="community-windows"></a>
#### community\.windows

* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* community\.windows\.win\_psmodule\_info \- Added <code>include\_properties</code> parameter to allow fine\-grained control over which module properties are returned\, improving performance when only specific properties are needed \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* community\.windows\.win\_psmodule\_info \- Added <code>skip\_module\_repository\_info</code> parameter to skips querying PowerShellGet for repository\-related metadata \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* community\.windows\.win\_psmodule\_info \- Automatically skips expensive PowerShellGet repository lookups when <code>include\_properties</code> is specified without repository\-related properties \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* win\_unzip \- Use <code>tar\.exe</code> from <code>\%SystemRoot\%\\System32</code> on Windows 10 build 17063 and later and Windows Server 2019 and later to extract tar\-based archives \(<code>\.tar</code>\, <code>\.tar\.gz</code>/<code>\.tgz</code>\, <code>\.tar\.bz2</code>/<code>\.tbz2</code>\, <code>\.tar\.xz</code>/<code>\.txz</code>\) without requiring PSCX\. On older systems where <code>tar\.exe</code> is not available\, PSCX remains the fallback\. PSCX is still required for passwords\, recursive extraction\, and non\-tar formats other than <code>\.zip</code>\.
* win\_xml \- add new option <code>content</code> to be able to return the content of nodes \([https\://github\.com/ansible\-collections/community\.windows/issues/54](https\://github\.com/ansible\-collections/community\.windows/issues/54)\)\.

<a id="containers-podman"></a>
#### containers\.podman

* podman\_quadlet \- Add support for aliases for Quadlets

<a id="dellemc-powerflex"></a>
#### dellemc\.powerflex

* Added the <code>device\_group</code> module to manage existing PowerFlex Gen2 device groups\. The module supports getting device group details by name or ID\, renaming a device group\, updating spare node and spare device counts\, and querying usable capacity\. Device group creation and deletion are not supported\.
* Added the <code>thin\_clone</code> module to create thin clones from a source volume or a read\-only snapshot on PowerFlex 5\.x Gen2 systems\. This module is creation\-only\; ongoing management of the resulting thin clone is handled by the <code>volume</code> module\.
* Fixed sanity and lint issues in info\_v2 module\.
* Updated GitHub Actions workflow for improved CI stability\.

<a id="fortinet-fortimanager"></a>
#### fortinet\.fortimanager

* Added 19 new modules\.
* Reduced the overall project size\.
* Supported FortiManager schemas 7\.4\.11\, 7\.6\.7\, 8\.0\.0

<a id="google-cloud"></a>
#### google\.cloud

* gcp\_alloydb\_\*\, gcp\_cloudbuild\_\*\, gcp\_colab\_\*\, gcp\_vertexai\_\* \- update to use <em class="title-reference">plugins/module\_utils/gcp\_v2\.py</em> \([https\://github\.com/ansible\-collections/google\.cloud/pull/763](https\://github\.com/ansible\-collections/google\.cloud/pull/763)\)

<a id="graphiant-naas"></a>
#### graphiant\.naas

* Backbone operations\: <code>configure</code> / <code>deconfigure</code> \(orchestrate sites \+ tunnel\-underlay phasing \+ per\-device push\)\, <code>configure\_core\_to\_core\_interfaces</code> / <code>deconfigure\_core\_to\_core\_interfaces</code> \(with VLAN sub\-interface support\)\, <code>configure\_core\_to\_core\_tunnel\_interfaces</code> / <code>deconfigure\_core\_to\_core\_tunnel\_interfaces</code>\, <code>configure\_wan\_circuits</code> / <code>deconfigure\_wan\_circuits</code>\, <code>configure\_direct\_peer\_interfaces</code> / <code>deconfigure\_direct\_peer\_interfaces</code>\, <code>configure\_syslog\_targets</code> / <code>deconfigure\_syslog\_targets</code>
* Collection version bumped to 26\.5\.0
* Deconfigure workflows are idempotent\: parent and VLAN sub\-interface existence checked via <code>gsdk\.get\_device\_info</code> before issuing deletes\; per\-VRF <code>syslogTargets</code> existence checked against <code>device\.segments\[\*\]\.syslog\_targets\[\*\]\.name</code>
* Minimum <code>graphiant\-sdk</code> raised to <code>\>\= 26\.5\.0</code> \(see <code>\_version\.py</code> <code>DEPENDENCIES</code>\)
* New <code>backbone\_interface\_template\.yaml</code> Jinja2 template covering Core <code>interface\_type</code> flavors\: <code>loopback</code>\, <code>core\_to\_core\_link</code> \(with VLAN sub\-interfaces \+ <code>ospf</code> block rendered to <code>coreNeighbor</code>\)\, <code>core\_to\_core\_ipsec\_tunnel</code>\, <code>p2mp\_tunnel</code>\, <code>isp\_circuit</code>\, <code>direct\_peer</code>\, <code>disabled</code>
* New <code>graphiant\_backbone</code> module and <code>backbone\_management\.yml</code> playbook for managing Graphiant Core \(backbone\) device configuration\; samples <code>sample\_backbone\_config\.yaml</code> and <code>sample\_backbone\_direct\_peer\_config\.yaml</code>
* New <code>graphiant\_data\_assurance</code> module and <code>data\_assurance\_management\.yml</code> playbook for managing Data Assurance policies via the portal API\; a single YAML config file drives both <code>DataAssurancePolicies</code> \(assurance policies with <code>flexAlgo</code> and block\-by\-URL/app policies\) sent to <code>/v1/data/assurance/assurances/global</code> and <code>ContentFilterPolicies</code> \(block\-by\-category policies\) sent to <code>/v1/global/content\-filters</code>\; operations <code>configure</code> / <code>deconfigure</code> \(idempotent — compares intended config against live portal state and skips unchanged policies\; deconfigure detaches sites and clears apps/rules before delete\)\; name\-based fields are validated against live portal state before push — <code>flexAlgo</code>\, <code>siteListName</code>\, and <code>lanNames</code> each fail with an error listing the available values when a name is not found\; app names are validated and <code>isDomain</code>/<code>builtinAppId</code>/<code>customAppId</code>/<code>servers</code> auto\-filled from bucket telemetry\; sample <code>sample\_data\_assurance\_policies\.yaml</code>\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns <code>details\.diff\_plan</code>\)\; unit tests for the manager and module
* New <code>graphiant\_dhcp\_relay</code> module and <code>dhcp\_relay\_interface\_management\.yml</code> playbook for DHCP relay \(IPv4/IPv6\) on main interfaces and VLAN subinterfaces\; sample <code>sample\_dhcp\_relay\_config\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code>\; idempotent comparison to live device relay server lists\; interface/subinterface existence validation before push\; deep merge when multiple VLAN subinterfaces on the same parent are configured in one run\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns accurate <code>changed</code>\, <code>details\.diff\_plan</code>\, and Ansible <code>diff</code> with per\-interface relay server <code>before</code>/<code>after</code> under <code>edge\.interfaces</code>\)\; integration tests in <code>tests/test\.py</code>
* New <code>graphiant\_edge\_services</code> module and <code>edge\_services\_management\.yml</code> playbook for Edge/Gateway DHCP subnets\, DNS mode\, LLDP\, and local web server password\; sample <code>sample\_edge\_services\.yaml</code>
* New <code>graphiant\_local\_extranet\_info</code> module for querying Local Extranet policy state — <code>policies\_summary</code>\, <code>policy\_device\_status</code> \(requires <code>policy\_name</code>\)\, <code>lan\_segments\_usage</code> \(optional <code>policy\_name</code>/<code>is\_provider</code>\)\, <code>nat\_usage</code> \(requires <code>policy\_name</code>\)\; tabulated output
* New <code>graphiant\_local\_extranet</code> module and <code>local\_extranet\_management\.yml</code> playbook for single\-tenant intra\-enterprise LAN segment sharing across sites/branches\; operations <code>create\_policies</code> / <code>update\_policies</code> / <code>delete\_policies</code>\; policy is auto\-applied to devices after create/update \(no separate apply step\)\; sample <code>sample\_local\_extranet\_policies\.yaml</code> and update sample <code>sample\_local\_extranet\_policies\_update\.yaml</code>\; idempotent create/delete and before/after comparison on update \(prefix sets\, sites\, excluded devices\, target segments all normalized\)\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns <code>details\.diff\_plan</code>\)\; unit tests for the manager and both modules plus integration tests in <code>tests/test\.py</code> covering create/update/delete idempotency
* New <code>graphiant\_macsec</code> and <code>graphiant\_macsec\_info</code> modules and <code>macsec\_management\.yml</code> playbook for interface MACsec configuration and monitoring\; sample <code>sample\_macsec\.yaml</code>
* New <code>graphiant\_nat\_policy</code> module and <code>nat\_policy\_management\.yml</code> playbook for device\-level NAT policy rulesets \(<code>edge\.natPolicy\.natRulesets</code>\) and LAN segment ruleset attachments \(<code>edge\.segments\.\<name\>\.natRuleset</code>\)\; sample <code>sample\_device\_nat\_policies\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code> / <code>attach\_to\_lan\_segments</code> / <code>detach\_from\_lan\_segments</code>\; idempotent comparison to live device state \(reads <code>natPolicyRulesets</code> from GET response\)\; <code>state\: absent</code> on ruleset or rule entries \(under <code>configure</code>\) to delete a single object without a full deconfigure\; <code>state\: absent</code> on segment entries \(under <code>attach\_to\_lan\_segments</code>\) to detach a segment from its ruleset\; pre\-flight safety check refuses to delete a ruleset still referenced by LAN segments with a clear error pointing to the detach path\; absent no\-op pruning skips payloads for rulesets/rules not present on the device\; check mode \(<code>\-\-check</code>\) bypasses the safety check and pruning so full deconfigure workflows can be previewed with <code>\-\-check \-\-diff</code>\; full diff mode with per\-ruleset rule diffs under <code>edge\.natPolicy\.natRulesets</code> and per\-segment diffs under <code>edge\.segments</code>\; inline module params \(<code>device</code>\, <code>natRulesets</code>\, <code>segments</code>\) allow single\-device and loop use without a config file\; integration tests in <code>tests/test\.py</code>
* New <code>graphiant\_ospfv2</code> module and <code>ospfv2\_management\.yml</code> playbook for OSPFv2 process configuration under <code>edge\.segments\.\*\.ospfv2</code> \(areas\, interfaces\, redistribution\)\; sample <code>sample\_ospfv2\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code>\; LAN segment and interface existence validation against live device state before push\; idempotent comparison to live device state\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns accurate <code>changed</code>\, <code>details\.diff\_plan</code>\, and Ansible <code>diff</code> with per\-segment <code>before</code>/<code>after</code>\)\; integration tests in <code>tests/test\.py</code>\, <code>graphiant\_ospfv2</code>\: new <code>vault\_ospf\_md5\_passwords</code> module param \(configure only\, <code>no\_log\: true</code>\) fills interface <code>authentication\.key</code> from Ansible Vault \(device name \-\> <code>interfaceName</code>\) when the YAML leaves it null\; YAML value still wins when non\-null
* New <code>graphiant\_prefix\_port\_list</code> module and <code>prefix\_port\_list\_mangement\.yml</code> playbook for managing Prefix and Port Lists on Edge devices\; sample <code>sample\_prefix\_and\_port\_list\.yaml</code>
* New <code>graphiant\_public\_vif\_info</code> module for querying Public VIF service state — <code>services\_summary</code> and <code>service\_details</code> \(requires <code>service\_name</code>\)\; tabulated output
* New <code>graphiant\_public\_vif</code> module and <code>public\_vif\_management\.yml</code> playbook for gateway Public VIF management\; operations <code>create\_services</code> / <code>update\_services</code> / <code>delete\_services</code>\; sample <code>sample\_public\_vif\_services\.yaml</code>\; idempotent create/delete \(skip already\-existing/\-absent\)\; <code>update\_services</code> always re\-sends the full payload and reports <code>changed\: true</code> \(no live\-state comparison\)\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns <code>details\.diff\_plan</code>\)\; unit tests for the manager and both modules\; optional <code>vault\_public\_vif\_bgp\_md5\_passwords</code> param \(<code>create\_services</code>/<code>update\_services</code> only\, <code>no\_log\: true</code>\) fills a neighbor\'s <code>gatewayBgpNeighbors\[\]\.md5Password</code> from Ansible Vault \(keyed by service name \-\> device name\) when left null/absent in the YAML\; YAML non\-null value always wins\; <code>md5Password</code> is redacted as <code>\*\*\*\*\*\*\*\*</code> in logs and <code>\-\-diff</code> output regardless of source\; <code>gatewayBgpNeighbors</code> devices validated against the current gateway appliances\; <code>gatewayBgpNeighbors</code>\'s optional entry\`\`localInterface\`\` validated against that device\'s actual interfaces/subinterfaces\, the resolved <code>lanSegment</code> validated against the LAN segments actually configured on the <code>gatewayBgpNeighbors</code> devices for the resolved <code>storageProvider</code>
* New <code>graphiant\_security\_policy</code> module and <code>security\_policies\_management\.yml</code> playbook for device\-level security rulesets \(<code>edge\.trafficPolicy\.securityRulesets</code>\) and zone pair attachments \(<code>edge\.trafficPolicy\.zones</code>\)\; sample <code>sample\_device\_security\_policies\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code> / <code>attach\_to\_zone\_pairs</code> / <code>detach\_from\_zone\_pairs</code>\; idempotent comparison to live device state\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns accurate <code>changed</code>\, <code>details\.diff\_plan</code>\, and Ansible <code>diff</code> with per\-rule <code>before</code>/<code>after</code> for pending ruleset\, zone\-pair\, and metadata changes\)
* New <code>graphiant\_traffic\_policy</code> module and <code>traffic\_policies\_management\.yml</code> playbook for device\-level traffic rulesets \(<code>edge\.trafficPolicy\.trafficRulesets</code>\) and LAN segment ruleset attachments \(<code>edge\.segments</code>\)\; sample <code>sample\_device\_traffic\_policies\.yaml</code>\; operations <code>configure</code> / <code>deconfigure</code> / <code>attach\_to\_lan\_segments</code> / <code>detach\_from\_lan\_segments</code>\; idempotent comparison to live device state\; full check mode and diff mode \(<code>\-\-check \-\-diff</code> returns accurate <code>changed</code>\, <code>details\.diff\_plan</code>\, and Ansible <code>diff</code> with per\-rule <code>before</code>/<code>after</code> for pending ruleset\, segment\, and metadata changes\)
* <code>00\_dataex\_lan\_segments\_prerequisites\.yml</code>\, <code>00\_dataex\_lan\_interface\_prerequisites\.yml</code>\, and <code>00\_dataex\_vpn\_profile\_prerequisites\.yml</code> accept <code>\-e config\_file\=</code> to override the default sample config
* <code>BackboneManager</code> registered on <code>GraphiantConfig\.backbone</code>\; payloads build the <code>core</code> branch \(counterpart to <code>graphiant\_interfaces</code> on <code>edge</code>\)\. <code>ConfigTemplates\.render\_backbone\_interface\(\)</code> and <code>ConfigUtils\.device\_backbone\_interface\(\)</code> render the new template
* <code>gcsdk\_client</code>\: bug fix — <code>get\_matched\_services\_for\_customer</code> no longer raises <code>TypeError</code> when API returns <code>None</code>
* <code>graphiant\_bgp</code>\: new BGP route aggregation support — <code>bgp\_aggregations</code> list per segment entry in the config file\; fields <code>prefix</code> \(required\)\, <code>as\_set</code> \(optional\, default false\)\, <code>summary\_only</code> \(optional\, default false\)\; aggregations and neighbors are independent — a segment may define either or both\; <code>state\: present</code> / <code>operation\: configure</code> pushes <code>bgpAggregations</code> to <code>edge\.segments\.\<name\>\.bgpAggregations</code>\; <code>state\: absent</code> / <code>operation\: deconfigure</code> nulls out listed aggregations alongside neighbors\; <code>detach\_policies</code> leaves aggregations untouched\; <code>sample\_bgp\_peering\.yaml</code> updated with aggregation examples
* <code>graphiant\_data\_exchange</code> <code>accept\_invitation</code>\: new <code>ipsecGatewayPeers</code> config key replaces <code>ipsecGatewayDetails</code> to support multiple remote VPN peers\; requires <code>graphiant\_sdk \>\= 26\.6\.0</code>
* <code>graphiant\_data\_exchange</code> <code>accept\_invitation</code>\: new <code>vault\_data\_exchange\_bgp\_md5\_passwords</code> and <code>vault\_data\_exchange\_psk</code> module params\; fetch from any secrets store and pass in memory \(<code>no\_log\: true</code>\)\; vault optional — skips gracefully when absent
* <code>graphiant\_data\_exchange</code>\: <code>accept\_invitation</code> no longer requires <code>policy\.siteToSiteVpn</code> when the matched customer is a Graphiant customer \(<code>type\: graphiant\_peer</code>\, resolved via <code>get\_matching\_customers\_for\_service</code>\) — it still is for a non\-Graphiant customer \(<code>type\: non\_graphiant\_peer</code>\)\; new sample files <code>sample\_data\_exchange\_customers\_graphiant\_peer\.yaml</code>\, <code>sample\_data\_exchange\_services\_graphiant\_peer\_client\_to\_server\.yaml</code>\, <code>sample\_data\_exchange\_matches\_graphiant\_peer\_client\_to\_server\.yaml</code>\, and <code>sample\_data\_exchange\_acceptance\_graphiant\_peer\_client\_to\_server\.yaml</code> demonstrate the full flow
* <code>graphiant\_data\_exchange</code>\: <code>create\_services</code>/<code>update\_services</code> accept <code>serviceType</code> as the primary key for a service\'s type\, matching the API field name directly\; <code>type</code> is still accepted as a legacy alias
* <code>graphiant\_data\_exchange</code>\: all Data Exchange workflow playbooks \(02–05\, 07\) support <code>\-e config\_file\=</code> to override the default config YAML\; <code>create\_customers</code> detects <code>adminEmail</code> drift via <code>\-\-check \-\-diff</code>\; <code>accept\_invitation</code> <code>matches\_file</code> is now optional\; <code>\-\-check</code> mode replaces the removed dry\-run playbook\; idempotency integration tests added for all five operations
* <code>graphiant\_data\_exchange</code>\: migrated <code>create\_services</code>\, <code>update\_services</code>\, customer create/get/edit/delete/summary\, <code>match\_service\_to\_customers</code>\, and <code>accept\_invitation</code> from the peering\-specific <code>/v1/extranets\-b2b\-peering/\*</code>/<code>/v1/extranets\-b2b\-general/\*</code> endpoints to the generic <code>/v1/extranet/b2b/\*</code> API \(<code>graphiant\-sdk \>\= 26\.7\.0</code>\)\, with check mode now validating payloads against real SDK request models\. Sample config files document the API\-aligned keys as primary — <code>sites</code> \(was <code>site</code>\)\, <code>invite\.adminEmails</code> \(was <code>invite\.adminEmail</code>\)\, <code>natTranslationMode\.peerToPeer\.prefixes</code> \(was <code>nat</code>\, <code>peering\_service</code> only\) — with the old keys still accepted as backward\-compatible aliases\, including for <code>accept\_invitation</code>\: its recommended config shape now mirrors the API payload directly \(everything nests under a top\-level <code>policy</code> key — <code>policy\.sites</code>\, <code>policy\.consumerLanSegments</code>\, <code>policy\.siteToSiteVpn</code>\, <code>policy\.natTranslationMode</code>\, <code>policy\.globalObjectOps</code>\; <code>routingPolicyTable</code> stays a top\-level sibling of <code>policy</code>\)\, while the old flat structure \(top\-level <code>siteInformation</code>\, <code>policy</code> as a list\, <code>nat</code>\, <code>siteToSiteVpn</code>\) is auto\-detected and translated internally — not a breaking change\. See <code>sample\_data\_exchange\_acceptance\.yaml</code> for the recommended shape and <code>sample\_data\_exchange\_acceptance\_legacy\.yaml</code> for the old shape and key mapping
* <code>graphiant\_data\_exchange</code>\: new <code>client\_to\_server</code> service type for <code>create\_services</code> / <code>update\_services</code> / <code>delete\_services</code> / <code>match\_service\_to\_customers</code> / <code>accept\_invitation</code>\, with per\-edge NAT pools configured via <code>policy\.natTranslationMode</code> \(validated for NAT pool coverage\, per\-device prefix uniqueness\, and CIDR alignment\) and a new <code>consumerPrefixes</code> match key in place of <code>peering\_service</code>\'s NAT translation\; <code>get\_data\_exchange\_services\_summary</code> now lists both <code>peering\_service</code> and <code>client\_to\_server</code> with a new <code>Type</code> column\, fetched entirely via <code>GET /v1/extranet/b2b/services/summary\?serviceType\=\<type\></code> \(confirmed to cover both types\) — the old <code>/v1/extranets\-b2b\-general/services\-summary</code> endpoint is no longer called\; samples <code>sample\_data\_exchange\_services\_client\_to\_server\.yaml</code>/<code>\_update\.yaml</code>\, <code>sample\_data\_exchange\_matches\_client\_to\_server\.yaml</code>\, and <code>sample\_data\_exchange\_acceptance\_client\_to\_server\.yaml</code>
* <code>graphiant\_data\_exchange</code>\: new <code>client\_to\_server</code> service type for <code>create\_services</code> / <code>update\_services</code> / <code>delete\_services</code>\, with per\-edge NAT pools configured via <code>policy\.natTranslationMode</code> and validation for NAT pool coverage\, per\-device prefix uniqueness\, and CIDR alignment\; <code>get\_data\_exchange\_services\_summary</code> now lists both <code>peering\_service</code> and <code>client\_to\_server</code> with a new <code>Type</code> column\; new <code>/v1/extranet/b2b/\*</code> endpoints called via raw API requests pending <code>graphiant\-sdk</code> bindings \(migration planned for a follow\-up MR\)\; samples <code>sample\_data\_exchange\_services\_client\_to\_server\.yaml</code> and <code>\_update\.yaml</code>
* <code>graphiant\_ntp</code>\, <code>graphiant\_static\_routes</code>\, <code>graphiant\_site\_to\_site\_vpn</code>\: <code>\-\-check \-\-diff</code> now shows before/after state via <code>diff\_plan</code>\; <code>no\_log\: true</code> removed from module tasks in all playbooks \(masking is already handled by module argument spec <code>no\_log\=True</code> and library <code>\_SENSITIVE\_LOG\_KEYS</code> — task\-level <code>no\_log</code> was suppressing <code>\-\-diff</code> output\)
* <code>graphiant\_site\_to\_site\_vpn</code>\: vault precedence aligned — YAML non\-null wins\, secrets store fills <code>null</code>/absent for <code>presharedKey</code> and <code>md5Password</code>

<a id="hetzner-hcloud"></a>
#### hetzner\.hcloud

* load\_balancer \- Print warning when creating a Load Balancer with a deprecated or unavailable Load Balancer Type\.
* load\_balancer\_info \- Added the HTTP idle timeout property to the services return values \(<code>hcloud\_load\_balancer\_info\[\]\.services\[\]\.http\.timeout\_idle</code>\)\.
* load\_balancer\_service \- Added the <code>http\.timeout\_idle</code> argument to configure the idle timeout in seconds for HTTP services\.
* load\_balancer\_type\_info \- Added the Load Balancer Type <code>deprecation</code> object to the return values \(<code>load\_balancer\_type\_info\[\]\.deprecation</code>\)\.

<a id="hitachivantara-vspone-block"></a>
#### hitachivantara\.vspone\_block

* Added a new input parameter “force\_create” in the “gad\_bulk” module to allow GAD pair creation even when resources are locked\, must be used only within the “resource\_management\_with\_lock” module\.
* Added a new playbook “remote\_replication\_gad” in the resource\_management\_with\_lock module\.
* Added a new state “forced\_present” in the gad module to allow GAD pair creation even when resources are locked\, must be used only within the “resource\_management\_with\_lock” module\.
* Added support for SVOS 10\.5\.3 NVMe\_FC management “nvm\_subsystems” and “nvm\_subsystem\_facts”\,\( with the limitation that port configuration migration from FC to NVMe\_FC\) for VSP One BHE storage models\.
* Added support for SVOS 10\.5\.4 VSP One B24/B26/B28 storage models\.
* Added support for input parameter wait\_for\_final\_state for following module hv\_snapshot\.
* Fixed an issue affecting VSM creation for B\-series storage\.
* Fixed an issue where adding an iSCSI target to a VSM returned empty output\.
* Fixed an issue where an external LDEV could not be created on the first ELUN in local storage for Hitachi UVM\.
* Fixed an issue where creating a GAD pair failed with \"No free LDEV found in the range\.\"
* Fixed an issue where external path group facts returned an empty external path\.
* Fixed an issue where the IQN was blank in iSCSI target facts\.
* Fixed an issue where the WWN was blank in host group facts\.
* Removed the input parameters “delete\_mode” and “allow\_volume\_access\_after\_force\_delete” from the “hv\_vsp\_one\_gad” module\.

<a id="hitachivantara-vspone-object"></a>
#### hitachivantara\.vspone\_object

* Added role <em class="title-reference">hv\_vspone\_object\_certificate\_upload\_role</em> to upload certificate files from a folder to VSP One Object\.
* Added role <em class="title-reference">hv\_vspone\_object\_kmip\_server\_role</em> to update HTTPS cipher strings for existing KMIP servers\.
* Added role <em class="title-reference">hv\_vspone\_object\_license\_role</em> to set serial number and upload a license file\.
* Added role <em class="title-reference">hv\_vspone\_object\_storage\_component\_role</em> to activate storage components and retrieve components filtered by used capacity\.

<a id="ibm-storage-virtualize"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_fcportsetmember \- Added support for adding autozone\-incapable port into autozone\-capable portset\.
* ibm\_sv\_manage\_snapshotpolicy \- Added support for renaming snapshot policy\.
* ibm\_svc\_host \- Added support for creating host using SAS protocol and automated storage rescans at known intervals\.
* ibm\_svc\_initial\_setup \- Added support for system\-wide autozone prefix option\.
* ibm\_svc\_manage\_portset \- Added support for enabling autozoning functionality\.

<a id="infoblox-nios-modules"></a>
#### infoblox\.nios\_modules

* WapiModule\.compare\_objects \- list\-valued fields whose order is not semantically significant \(<code>monitors</code>\, <code>members</code>\, <code>options</code>\, <code>delegate\_to</code>\, <code>forwarding\_servers</code>\, <code>stub\_members</code>\, <code>ssh\_keys</code>\, <code>vlans</code>\, <code>auth\_zones</code>\) are now compared with an order\-insensitive algorithm\, eliminating spurious <code>changed\=true</code> when NIOS returns content in a different order \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/321](https\://github\.com/infobloxopen/infoblox\-ansible/pull/321)\)\.
* module\_utils/api \- extensible attributes now support inheritance control\. An <code>extattrs</code> value may be given as a dict with <code>inheritance\_operation\: INHERIT</code> or <code>OVERRIDE</code> to revert an object to its inherited value or to explicitly override an inherited one \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/347](https\://github\.com/infobloxopen/infoblox\-ansible/pull/347)\)\.
* nios\_\* modules \- after a successful create or update \(<code>state\: present</code>\, <code>changed\: true</code>\)\, modules now return the canonical NIOS object under <code>result\.object</code>\, making lookup\-allocated values such as the IP chosen by <code>func\: nios\_next\_ip</code> accessible to downstream tasks \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/318](https\://github\.com/infobloxopen/infoblox\-ansible/pull/318)\)\.
* nios\_aaaa\_record \- added support for swapping IPv6 addresses using <code>old\_ipv6addr</code> and <code>new\_ipv6addr</code> keys in the <code>ipv6addr</code> argument\, consistent with the <code>old\_ipv4addr</code>/<code>new\_ipv4addr</code> pattern on <code>nios\_a\_record</code> \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/351](https\://github\.com/infobloxopen/infoblox\-ansible/pull/351)\)\.
* nios\_dtc\_topology \- <code>rules\[\]\.destination\_link</code> is now deprecated and will be removed in collection version <code>2\.0\.0</code>\. Use <code>rules\[\]\.destination</code> for WAPI 2\.14\+ environments \(NPA\-1840\)\.
* nios\_dtc\_topology \- added a new <code>rules\[\]\.destination</code> option \(list of <code>destination\_link</code> \+ <code>priority</code> structs\) for WAPI 2\.14\+ / NIOS 9\.1\.0\, enabling multiple prioritized destinations per rule \(NPA\-1840\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/344](https\://github\.com/infobloxopen/infoblox\-ansible/pull/344)\)\.

<a id="kubernetes-core"></a>
#### kubernetes\.core

* Remove the remaining <code>ansible\.module\_utils\.six</code> import to avoid deprecation warnings\, replacing it with the Python standard library equivalent \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1197](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1197)\)\.
* helm \- Add <code>wait\_for\_jobs</code> option to wait for all Jobs to complete before marking a Helm release as successful\. Requires Helm \>\= 3\.5\.0 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1140](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1140)\)\.
* helm \- add the <code>cleanup\_on\_fail</code> option\, mapping to the <code>\-\-cleanup\-on\-fail</code> flag\, to allow deletion of new resources created during a failed upgrade\. It complements <code>atomic</code> and can be combined with it\, but cannot be used with <code>replace</code>\, since that deploys through <code>helm install</code> which does not accept the flag \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1206](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1206)\)\.
* helm \- add the <code>server\_side</code> and <code>force\_conflicts</code> options to control Helm v4 server\-side apply when installing or upgrading a release \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164)\)\.
* helm \- warn when <code>reuse\_values</code> or <code>reset\_then\_reuse\_values</code> is requested in a combination helm ignores\, which happens by default because <code>reset\_values</code> defaults to <code>true</code>\, and whenever either is combined with <code>replace</code>\. The option descriptions and the examples now state that <code>reset\_values</code> has to be set to <code>false</code> for either option to take effect \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1230](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1230)\)\.
* helm\_plugin \- add <code>\-\-keyring</code> argument to allow changing the keyring default location\. The option is only accepted with <code>state\=present</code> \(the <code>helm plugin install</code> subcommand\)\, as that is the only implemented subcommand that supports <code>\-\-keyring</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1150](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1150)\)\.
* helm\_registry\_auth \- document that\, as of Helm 4\.2\.1\, registry success messages such as <code>Login Succeeded</code> are printed to stdout instead of stderr \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1147](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1147)\)\.
* k8s lookup \- warn when <code>ENABLE\_TURBO\_MODE</code> is set but the <code>cloud\.common</code> collection is not installed\, instead of silently falling back to the standard lookup base \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1242](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1242)\)\.
* k8s\_cp \- Add the <code>copy\_timeout</code> option \(default 300 seconds\) bounding how long the module will spend streaming an archive to a pod and waiting for the remote <code>tar</code> to finish\, so that a stalled copy fails instead of hanging indefinitely \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217)\)\.
* k8s\_cp \- Stream the tar archive to the pod chunk by chunk instead of building the whole archive in memory first\, which cuts peak memory use when copying large files \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217)\)\.
* k8s\_cp \- When copying to a pod\, the module now also uses <code>/bin/sh</code> and <code>head</code> in the container\, when present\, to confirm the copy completed\. Containers without them keep the previous behaviour and get a warning that completion could not be verified \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217)\)\.
* k8s\_info \- Support for metadata\-only fetches in k8s\_info module \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1030](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1030)\)
* kubeconfig \- add <code>remove</code> value to the <code>behavior</code> option\, allowing entries to be deleted from the kubeconfig file by name \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1123](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1123)\)\.
* meta \- Add <code>helm\_plugin</code> and <code>helm\_plugin\_info</code> to the <code>helm</code> action group\, and <code>k8s\_taint</code> to the <code>k8s</code> action group\, so that <code>module\_defaults</code> set on those groups applies to them \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1216](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1216)\)\.
* use <em class="title-reference">collections\.abc</em> instead of deprecated <em class="title-reference">ansible\.module\_utils\.common\.\_collections\_compat</em> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1057](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1057)\)\.
* waiter \- Add <code>job\_complete</code> predicate to support waiting for Job resources to reach <code>Complete</code> or <code>Failed</code> condition \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1201](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1201)\)\.

<a id="lowlydba-sqlserver"></a>
#### lowlydba\.sqlserver

* Add a Pester unit test suite under <code>tests/unit/plugins/module\_utils/</code> covering the <code>module\_utils</code> helpers \(<code>Get\-LowlyDbaSqlServerAuthSpec</code>\, <code>Get\-SqlCredential</code>\, <code>ConvertTo\-SerializableObject</code>\)\, and wire it into CI as a standalone job since <code>ansible\-test units</code> only supports Python \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/382](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/382)\)\.
* Add check\-mode assertions for the <code>backup</code> and <code>restore</code> integration test targets\, add idempotency assertions for the <code>availability\_group</code> and <code>ag\_replica</code> targets\, and exercise a non\-default <code>deployment\_method</code> in the <code>install\_script</code> targets \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/381](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/381)\)\.
* Standardize module documentation examples and correct invalid parameters\, missing required options\, and incorrect module references \([https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/399](https\://github\.com/lowlydba/lowlydba\.sqlserver/pull/399)\)\.
* login \- <code>language</code> can now be changed on an existing login\. Previously it was only applied when creating the login \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* module\_utils \- add <code>Get\-DesiredStateDiff</code> for comparing desired option values against an SMO object property by property\.

<a id="microsoft-ad"></a>
#### microsoft\.ad

* PowerShell 7 \- Add initial support for running modules against PowerShell 7 interpreters\. Support for PowerShell 7 varies across each module\, see module documentation for more information\.
* microsoft\.ad\.ldap \- Added new option <code>domain\_realm</code> that can be used to set the Kerberos realm in the SRV lookup\. This option provides a way to override the <code>krb5\.conf</code> or avoid the requirement on Kerberos for the LDAP lookup entirely\.

<a id="microsoft-iis"></a>
#### microsoft\.iis

* microsoft\.iis\.website \- Add preload support for websites using the <code>preload\_enabled</code> option

<a id="netapp-ontap-1"></a>
#### netapp\.ontap

* na\_ontap\_ems\_filter \- Added support for rule deletion in REST\.
* na\_ontap\_user \- added support for <em class="title-reference">amqp</em> application in user management\.
* na\_ontap\_volume \- new REST only options added under <em class="title-reference">event\_log</em> and <em class="title-reference">attack\_detection\_parameters</em>\.
* na\_ontap\_volume \- updated docs for volume <em class="title-reference">type</em>\.

<a id="netapp-eseries-santricity"></a>
#### netapp\_eseries\.santricity

* na\_santricity\_facts \- Add block\_size\_kb to netapp\_volumes\_by\_initiators facts\.

<a id="ngine-io-cloudstack"></a>
#### ngine\_io\.cloudstack

* firewall \- Implemented support for <code>dest\_cidrs</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/issues/76](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/issues/76)\)\.
* instance \- Added a new argument <code>match\_display\_name</code> to control whether to find instances by display name \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/164](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/164)\)\.
* instance \- Improved return values related to user data \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/168](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/168)\)\.
* instance \- Optimized API query with keyword filtering resulting in reduced time consumption in larger environments \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/164](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/164)\)\.
* inventory \- Added option to use public ip as hostname \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/116](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/116)\)\.
* inventory \- Extended projects filter to allow project\=\-1\, added project to returns \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/176](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/176)\)\.
* network \- Extended returns with <code>public\_ips</code> and <code>snat\_ip</code> \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/issues/121](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/issues/121)\)\.
* role\_permissions \- Removed version check for EOL CloudStack version \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/168](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/pull/168)\)\.

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
* purefb \- Add API\-client token authentication as an alternative to <code>api\_token</code>\, via a pre\-signed <code>id\_token</code> or a <code>private\_key\_file</code> \(with <code>client\_id</code>\, <code>key\_id</code>\, <code>issuer</code>\, <code>username</code>\)\.
* purefb \- Add comprehensive docstrings to get\_system and purefb\_argument\_spec functions \(\#494\)
* purefb\_fs \- Added <code>realm</code> parameter to support creating filesystems in realms \(requires Purity//FB 4\.6\.1\+\)
* purefb\_info \- Updated to use get\_policies\_all\(\) method and added policy type breakdown to default output

<a id="splunk-es-1"></a>
#### splunk\.es

* \.ansible\-lint \- added <code>exclude\_paths</code> entry for <code>\.ansible/</code> to prevent ansible\-lint from scanning installed collection dependencies\.
* \.yamllint \- added <code>\.ansible/</code> to the <code>ignore</code> list for the same reason\.
* Add tests to validate the collection with Ansible 2\.16 and 2\.18\.
* certification\.yml \- added Red Hat partner certification workflow running <code>ansible\-lint</code> \(profile <code>production</code>\) and <code>ansible\-test sanity</code> against Ansible stable\-2\.16\, stable\-2\.18\, and stable\-2\.20\.
* changelogs/changelog\.yaml and changelogs/config\.yaml \- added missing <code>\-\-\-</code> document\-start marker required by the <code>yaml\[document\-start\]</code> yamllint rule\.
* checks\.yml \- introduced a new dedicated workflow triggered only on <code>pull\_request\_target</code> to isolate privileged jobs \(<code>changelog</code> and <code>sonar</code>\) that require write access or secrets from the code\-testing workflow\. Each workflow now has a distinct name to differentiate them in GitHub Actions and branch protection rules\.
* meta/runtime\.yml \- lowered <code>requires\_ansible</code> from <code>\>\=2\.17\.0</code> to <code>\>\=2\.16\.0</code>

<a id="telekom-mms-icinga-director"></a>
#### telekom\_mms\.icinga\_director

* add support for managing and querying Icinga Director import sources\, jobs\, and sync rules \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/312](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/312)\)

<a id="theforeman-foreman"></a>
#### theforeman\.foreman

* activation\_key \- internally convert deprecated <code>content\_view</code>/<code>lifecycle\_environment</code> to content view environment labels for compatibility with newer Katello API versions \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1982](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1982)\)
* auth\_source\_ldap \- add <code>cacert</code> parameter to set CA certificates for LDAP server verification \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1985](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1985)\)
* host\, hostgroup \- internally convert <code>content\_view</code>/<code>lifecycle\_environment</code> to content view environment ID for compatibility with newer Katello API versions \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1977](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1977)\)

<a id="vmware-vmware"></a>
#### vmware\.vmware

* cluster\_drs\_vm\_overrides \- add module to manage DRS VM override settings on vSphere clusters
* cluster\_drs\_vm\_overrides\_info \- add module to gather DRS VM override settings for a cluster
* cluster\_ha\_vm\_overrides \- add module to manage HA VM override settings on vSphere clusters
* cluster\_ha\_vm\_overrides\_info \- add module to gather HA VM override settings for a cluster
* esxi\_service \- add module to manage the state and startup policy of services on an ESXi host \(migrated from community\.vmware\.vmware\_host\_service\_manager\) \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/396](https\://github\.com/ansible\-collections/vmware\.vmware/pull/396)\)\.
* esxi\_service\_info \- add module to gather information about the services on an ESXi host or every host in a cluster \(migrated from community\.vmware\.vmware\_host\_service\_info\) \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/396](https\://github\.com/ansible\-collections/vmware\.vmware/pull/396)\)\.
* guest\_info \- renamed to <code>vm\_info</code>\. A redirect was added so <code>vmware\.vmware\.guest\_info</code> continues to work
* inventory plugins \- Improve how properties are gathered to decrease execution time \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/318](https\://github\.com/ansible\-collections/vmware\.vmware/issues/318)\)\.
* key\_provider\_info \- add module to gather information about key providers in vCenter
* key\_provider\_native \- add module to manage native key providers in vCenter
* key\_provider\_standard \- add module to manage standard key providers and KMS servers in vCenter
* vcenter\_event\_manager \- Create EDA plugin for events in vCenter Event Manager
* vm \- Add enable\_vtpm parameter to enable or disable virtual Trusted Platform Module \(vTPM\) on virtual machines\.
* vm\_custom\_attributes \- add module to manage custom attributes for the given virtual machine \([https\://github\.com/ansible\-collections/vmware\.vmware/pull/381](https\://github\.com/ansible\-collections/vmware\.vmware/pull/381)\)\.
* vm\_info \- Add <code>vms</code> output key to mirror <code>guests</code> for consistency
* vm\_snapshot \- Add a timeout parameter to define how long the module will wait for the task to finish \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/361](https\://github\.com/ansible\-collections/vmware\.vmware/issues/361)\)\.
* vm\_snapshot \- Add relevant parent and child snapshot IDs to the returned snapshot value\.
* vm\_snapshot\_info \- Add module to gather information about snapshots and the snapshot tree\.

<a id="vmware-vmware-rest-1"></a>
#### vmware\.vmware\_rest

* Add support for ansible\-core 2\.21

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

<a id="ansible-core-3"></a>
#### Ansible\-core

* AnsibleModule \- <code>log\(\)</code> and the automatic invocation logging now only redact values registered as secrets \(such as <code>no\_log</code> option values\) and no longer apply the <code>heuristic\_log\_sanitize\(\)</code> heuristics\, for example <code>user\:password\@host</code> in URLs is no longer rewritten unless the password is a registered secret\. <code>no\_log</code> and password\-like options are logged as <code>\$REDACTED\$</code> instead of <code>NOT\_LOGGING\_PARAMETER</code> or <code>NOT\_LOGGING\_PASSWORD</code>\.
* AnsibleModule \- <code>run\_command\(\)</code> no longer rewrites the <code>cmd</code> value in a failure result to replace password\-like arguments \(such as <code>\-\-password\=\.\.\.</code>\) with <code>\*\*\*\*\*\*\*\*</code>\, and the <code>msg</code> value is no longer passed through <code>heuristic\_log\_sanitize\(\)</code>\. Registered secrets in these values are still redacted in output\. Modules that pass a secret on the command line which is not a <code>no\_log</code> option should register it with <code>ansible\.module\_utils\.secrets\.register\_secret\(\)</code>\.
* Module options that are marked as <code>no\_log\: true</code> will no longer be redacted literally as <code>\"VALUE\_SPECIFIED\_IN\_NO\_LOG\_PARAMETER\"</code> in the module result and <code>invocation\.module\_args</code>\. Instead\, the actual value is registered as a secret and is only redacted in generated output\, allowing these values to be used by subsequent tasks without any loss of data\. The value is still redacted in callback output and module logging\. Playbooks or tests that check for the <code>VALUE\_SPECIFIED\_IN\_NO\_LOG\_PARAMETER</code> placeholder in results should be updated\.
* ansible\-config \- all actions now default to <code>\-t all</code>\, so configuration files using sections owned by plugins \(for example\, <code>\[ssh\_connection\]</code>\) are no longer reported as unknown sections\, and keys within those sections are actually validated\. Use <code>\-t base</code> to retain the previous behavior \([https\://github\.com/ansible/ansible/issues/86398](https\://github\.com/ansible/ansible/issues/86398)\)\.
* uri \- response keys are no longer rewritten to strip <code>no\_log</code> values \(previously done with <code>sanitize\_keys\(\)</code>\)\; registered secrets are masked in output instead\.

<a id="cisco-nxos-1"></a>
#### cisco\.nxos

* nxos\_l2\_interfaces \- Port\-channel member interfaces are now excluded from gathered\, parsed\, and overridden/deleted states\. Attempting to configure L2 settings directly on a port\-channel member via merged\, replaced\, or deleted \(with explicit config\) states will now raise an error\. Apply L2 configuration on the port\-channel interface instead\.
* nxos\_route\_maps \- <code>match\.metric</code> elements changed from a list of integers to a list of dictionaries with required <code>value</code> and optional <code>deviation</code> \(for NX\-OS <code>match metric \<value\> \+\- \<deviation\></code>\)\. Update playbooks from <code>metric\: \[10\, 200\]</code> to <code>metric\: \[\{value\: 10\}\, \{value\: 200\}\]</code> \(or add <code>deviation</code> when needed\)\. Fixes fact\-gathering failures on that CLI\.

<a id="community-okd-1"></a>
#### community\.okd

* Minimum supported version of ansible\-core is now 2\.16 \([https\://github\.com/openshift/community\.okd/pull/292](https\://github\.com/openshift/community\.okd/pull/292)\)\.

<a id="community-postgresql-1"></a>
#### community\.postgresql

* postgresql\_membership \- <code>state\=exact</code> now reports <code>granted</code> with an entry for every requested group\, as <code>state\=present</code> does\, so <code>result\.granted \=\= \{\}</code> no longer holds on an unchanged run\.
* postgresql\_membership \- a <code>memberships</code> row must set <code>granted\_by</code> when the connecting role holds <code>ADMIN OPTION</code> on a group only through another role\, since PostgreSQL refuses a grant recorded under a role without the option\. The deprecated <code>groups</code> option is not affected\.
* postgresql\_membership \- on PostgreSQL 16 and later a <code>memberships</code> row manages the one grant recorded under its granting role\, which is the bootstrap superuser when the connecting role is a superuser\, the connecting role otherwise\, or the role named by <code>granted\_by</code>\. <code>state\=present</code> makes that grant even when another role has granted the membership\, and <code>state\=absent</code> and <code>state\=exact</code> neither revoke nor report a grant recorded under another role\. A task that was unchanged may report changed on its first run and fire its handlers\. The deprecated <code>groups</code> option keeps treating the \(group\, target role\) pair as the membership\, whoever granted it \([https\://github\.com/ansible\-collections/community\.postgresql/issues/757](https\://github\.com/ansible\-collections/community\.postgresql/issues/757)\)\.

<a id="hetzner-hcloud-1"></a>
#### hetzner\.hcloud

* Drop support for Python 3\.10
* Drop support for ansible\-core 2\.18

<a id="infoblox-nios-modules-1"></a>
#### infoblox\.nios\_modules

* nios\_next\_network lookup \- the <code>cidr</code> argument is now required and must be an integer\. Previously\, omitting <code>cidr</code> silently defaulted to <code>24</code>\; playbooks that relied on this default now fail with <code>AnsibleError\: missing required argument\: cidr</code>\. Update such playbooks to pass <code>cidr</code> explicitly \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/315](https\://github\.com/infobloxopen/infoblox\-ansible/pull/315)\)\.

<a id="lowlydba-sqlserver-1"></a>
#### lowlydba\.sqlserver

* Raise <code>requires\_ansible</code> to <code>\>\=2\.19</code>\. The previously declared floor of <code>\>\=2\.12</code> was never tested by CI\, which only runs sanity and integration tests against <code>stable\-2\.19</code> and newer \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/380](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/380)\)\.
* availability\_group \- an explicit <code>false</code> for <code>dtc\_support\_enabled</code>\, <code>basic\_availability\_group</code>\, <code>database\_health\_trigger</code> or <code>is\_distributed\_ag</code> now disables the setting on an existing availability group instead of being ignored \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* backup \- <code>compress</code>\, <code>encryption\_certificate</code>\, <code>azure\_base\_url</code> and <code>azure\_credential</code> now take effect\. Playbooks that set these options previously got an uncompressed\, unencrypted\, local backup regardless of the values supplied \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* install\_script \- <code>deployment\_method</code> now takes effect\. Playbooks that set <code>SingleTransaction</code>\, <code>TransactionPerScript</code> or <code>AlwaysRollback</code> previously ran with <code>NoTransaction</code> \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* login \- an explicit <code>false</code> for <code>password\_policy\_enforced</code> or <code>password\_expiration\_enabled</code> now disables the setting on the login instead of leaving it unchanged \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* sa \- an explicit <code>false</code> for <code>password\_policy\_enforced</code> or <code>password\_expiration\_enabled</code> now disables the setting on the login instead of leaving it unchanged \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.

<a id="netapp-eseries-santricity-1"></a>
#### netapp\_eseries\.santricity

* na\_santricity\_volume and nar\_santricity\_host \- Rename volume option raid\_level to ddp\_raid\_level for dynamic disk pool volumes\.

<a id="deprecated-features"></a>
### Deprecated Features

* The dellemc\.unity collection will be removed from Ansible 16 due to violations of the Ansible inclusion requirements\.
  No CI runs / sanity tests for 10 months\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details\, including for how this can be cancelled \([https\://forum\.ansible\.com/t/46085](https\://forum\.ansible\.com/t/46085)\)\.
  After removal\, users can still install this collection with <code>ansible\-galaxy collection install dellemc\.unity</code>\.

<a id="ansible-core-4"></a>
#### Ansible\-core

* AGNOSTIC\_BECOME\_PROMPT setting\, no external tools should need this any more\.
* Deprecate is\_module in get\_docstring API in favor of passing <code>plugin\_type\=\'module\'</code>\.
* <code>ansible\.module\_utils\.six</code> \- A runtime deprecation warning is now emitted when importing the <code>six</code> compatibility library\, deprecated in ansible\-core 2\.21 and planned for removal in ansible\-core 2\.24 \([https\://github\.com/ansible/ansible/issues/86789](https\://github\.com/ansible/ansible/issues/86789)\)\.
* action plugins \- <code>AnsibleActionSkip</code> is deprecated and will be removed in ansible\-core 2\.25\. A sanity test detects imports of this exception\. Return a results dict from action plugins and don\'t include a <code>skipped</code> key\, or raise <code>AnsibleActionNoCheckMode</code> if necessary\.
* ansible\.utils\.cmd\_functions\.run\_cmd \- the <code>live</code> argument is deprecated and will be removed in ansible\-core 2\.25 because it writes the subprocess output directly to stdout/stderr\, bypassing the built\-in secret masking applied to captured output\. Callers that need to stream output live should run the subprocess themselves and are responsible for masking any secrets\.
* module\_utils \- the <code>heuristic\_log\_sanitize\(\)</code> function in <code>ansible\.module\_utils\.basic</code> is deprecated and will be removed in ansible\-core 2\.25\. Secret values are now masked automatically\, use functions from the <code>ansible\.module\_utils\.secrets</code> module to handle secrets manually\.
* module\_utils \- the <code>remove\_values\(\)</code> and <code>sanitize\_keys\(\)</code> functions in <code>ansible\.module\_utils\.common\.parameters</code> are deprecated and will be removed in ansible\-core 2\.25\. Secret values are now masked automatically\, use functions from the <code>ansible\.module\_utils\.secrets</code> module to handle secrets manually\.
* task result \- Returning <code>skipped</code> from a module or action plugin is deprecated and will be removed in ansible\-core 2\.25\. Use task\-level conditionals \(<code>when\:</code>\) to control execution\.

<a id="community-clickhouse-2"></a>
#### community\.clickhouse

* clickhouse\_db \- deprecate pre 22\.x handling code for comments \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/217](https\://github\.com/ansible\-collections/community\.clickhouse/issues/217)\)\.
* clickhouse\_role \- list based settings and profiles are marked as deprecated and sheduled for removal in 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/218](https\://github\.com/ansible\-collections/community\.clickhouse/issues/218)\)\.
* clickhouse\_user \- <code>password</code> and <code>type\_password</code> are deprecated and will be removed in <code>community\.clickhouse 3\.0\.0</code>\, use the <code>authentication</code> instead\.
* clickhouse\_user \- list based settings and profiles are marked as deprecated and sheduled for removal in 3\.0\.0 \([https\://github\.com/ansible\-collections/community\.clickhouse/issues/218](https\://github\.com/ansible\-collections/community\.clickhouse/issues/218)\)\.
* mark ansible\-core\-2\.17 as deprecated\. Support will be removed in future\.

<a id="community-crypto-1"></a>
#### community\.crypto

* get\_certificate \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_csr \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_csr\_info \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_csr\_pipe \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_pkcs12 \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_privatekey \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_privatekey\_info \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_privatekey\_pipe \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_publickey \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_publickey\_info \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_signature \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* openssl\_signature\_info \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* x509\_certificate \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* x509\_certificate\_info \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.
* x509\_certificate\_pipe \- the <code>select\_crypto\_backend</code> option is deprecated and will be removed from community\.crypto 4\.0\.0 \([https\://github\.com/ansible\-collections/community\.crypto/pull/1072](https\://github\.com/ansible\-collections/community\.crypto/pull/1072)\)\.

<a id="community-general-1"></a>
#### community\.general

* keycloak\_authentication \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authentication</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_authentication\_required\_actions \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authentication\_required\_actions</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_authentication\_v2 \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authentication\_v2</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_authz\_authorization\_scope \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authz\_authorization\_scope</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_authz\_custom\_policy \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authz\_custom\_policy</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_authz\_permission \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authz\_permission</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_authz\_permission\_info \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_authz\_permission\_info</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_client \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_client</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_client\_rolemapping \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_client\_rolemapping</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_client\_rolescope \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_client\_rolescope</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_clientscope \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_client\_scope</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_clientscope\_rolemappings \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_client\_scope\_rolemappings</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_clientscope\_type \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_client\_scope\_type</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_clientsecret\_info \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_clientsecret\_info</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_clientsecret\_regenerate \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_clientsecret\_regenerate</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_clienttemplate \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_clienttemplate</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_component \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_component</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_component\_info \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_component\_info</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_group \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_group</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_identity\_provider \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_identity\_provider</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_realm \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_realm</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_realm\_key \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_realm\_key</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_realm\_keys\_metadata\_info \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_realm\_keys\_metadata\_info</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_realm\_localization \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_realm\_localization</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_realm\_rolemapping \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_realm\_rolemapping</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_realm\_users\_info \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_realm\_users\_info</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>ansible\_middleware\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12525](https\://github\.com/ansible\-collections/community\.general/pull/12525)\)\.
* keycloak\_role \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_role</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_user \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_user</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_user\_execute\_actions\_email \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_user\_execute\_actions\_email</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_user\_federation \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_user\_federation</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_user\_rolemapping \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_user\_rolemapping</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.
* keycloak\_userprofile \- the module is moved to <code>middleware\_automation\.keycloak\.keycloak\_userprofile</code>\. The module will be replaced by a deprecated redirect to that module in community\.general 14\.0\.0\, and the redirect will be removed in community\.general 16\.0\.0\. If you are using the module\, please consider installing and using <code>middleware\_automation\.keycloak</code> now \([https\://github\.com/ansible\-collections/community\.general/pull/12484](https\://github\.com/ansible\-collections/community\.general/pull/12484)\)\.

<a id="community-postgresql-2"></a>
#### community\.postgresql

* postgresql\_membership \- the top\-level <code>groups</code> option is deprecated and will be removed in <code>community\.postgresql 6\.0\.0</code>\. <code>granted\_by\_any</code> with the <code>groups</code> key of <code>memberships</code> behaves the same on every version\; <code>target\_roles</code> stays at the top level\, and an empty <code>memberships</code> list with <code>state\=exact</code> replaces an empty <code>groups</code> list\.

<a id="community-rabbitmq"></a>
#### community\.rabbitmq

* Support for RabbitMQ versions prior to 3\.7\.0 will be dropped in version 2\.0\.0 of this collection \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224)\)\.
* Support for ansible\-core versions prior to 2\.16\.0 will be dropped in version 2\.0\.0 of this collection \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/224)\)\.
* collection \- Python 2 support will be dropped in version 2\.0\.0 of this collection\. Make sure you have Python 3 installed on your target machines \([https\://github\.com/ansible\-collections/community\.rabbitmq/issues/214](https\://github\.com/ansible\-collections/community\.rabbitmq/issues/214)\)\.

<a id="community-vmware-1"></a>
#### community\.vmware

* plugins\.module\_utils\.vmware \- The function <code>find\_host\_by\_cluster\_datacenter</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware \- The function <code>vmware\_argument\_spec</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware \- The method <code>PyVmomi\.get\_all\_hosts\_by\_cluster</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware \- The method <code>PyVmomi\.get\_folder\_path</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware \- The method <code>PyVmomi\.vcenter\_version\_at\_least</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_cluster\_by\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_datacenter\_by\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_datastore\_by\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_host\_by\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_library\_item\_by\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_library\_item\_from\_content\_library\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_resource\_pool\_by\_name</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.get\_tags\_for\_cluster</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* plugins\.module\_utils\.vmware\_rest\_client \- The method <code>VMwareRestClient\.vmware\_client\_argument\_spec</code> is deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2599](https\://github\.com/ansible\-collections/community\.vmware/pull/2599)\)\.
* vcenter\_standard\_key\_provider \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_guest\_snapshot\_info \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_host\_facts \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_host\_powerstate \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_host\_service\_info \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_host\_service\_manager \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0
* vmware\_tag \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_tag\_manager \- the module has been deprecated and will be removed in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/pull/2568](https\://github\.com/ansible\-collections/community\.vmware/pull/2568)\)\.
* vmware\_vcenter\_settings \- The defaults are deprecated and will be removed where possible in community\.vmware 8\.0\.0 \([https\://github\.com/ansible\-collections/community\.vmware/issues/2559](https\://github\.com/ansible\-collections/community\.vmware/issues/2559)\)\.

<a id="hetzner-hcloud-2"></a>
#### hetzner\.hcloud

* datacenter\_info \- The <code>datacenter\_info</code> module is deprecated and will be removed after 1 Oct\. 2026\. Please use the <code>location\_info</code> module instead\.

<a id="kubernetes-core-1"></a>
#### kubernetes\.core

* Ansible Turbo mode \(<code>ENABLE\_TURBO\_MODE</code>\) has been deprecated and will be removed in release 8\.0\.0\, as it depends on the <code>cloud\.common</code> collection\, which is being retired \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1242](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1242)\)\.
* helm \- the <code>status\.values</code> return value has been deprecated and will be removed in version 8\.0\.0\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239)\)\.
* helm \- the <code>wait\_timeout</code> parameter has been deprecated and will be removed in version 7\.0\.0\. Use <code>timeout</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239)\)\.
* helm\_info \- the <code>status\.values</code> return value has been deprecated and will be removed in version 8\.0\.0\. Use <code>status\.release\_values</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239)\)\.
* k8s\_exec \- the <code>return\_code</code> return value has been deprecated and will be removed in version 7\.0\.0\. Use <code>rc</code> instead \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239)\)\.
* k8s\_service \- the <code>merge\_type\=json</code> option has been deprecated and will be removed in version 7\.0\.0\. Use <code>kubernetes\.core\.k8s\_json\_patch</code> module instead \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1239)\)\.

<a id="netapp-eseries-santricity-2"></a>
#### netapp\_eseries\.santricity

* na\_santricity\_volume and nar\_santricity\_host \- The <code>raid\_level</code> volume option alias is deprecated and will be removed in version 3\.0\.0\. Use <code>ddp\_raid\_level</code> instead\.

<a id="purestorage-flashblade-1"></a>
#### purestorage\.flashblade

* purefb\_fs \- The <code>nfs\_rules</code> parameter is deprecated in favour of <code>export\_policy</code> and will be removed in 2\.0\.0\. A deprecation notice is emitted when it is used\.

<a id="theforeman-foreman-1"></a>
#### theforeman\.foreman

* activation\_key \- the <code>content\_view</code> and <code>lifecycle\_environment</code> parameters are deprecated\, please use <code>content\_view\_environments</code> instead \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1982](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1982)\)

<a id="vmware-vmware-rest-2"></a>
#### vmware\.vmware\_rest

* turbo mode and the associated environment variable <code>VMWARE\_ENABLE\_TURBO</code> are deprecated and will be removed from <code>vmware\.vmware\_rest</code> 5\.0\.0 \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/639](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/pull/639)\)\.

<a id="removed-features-previously-deprecated"></a>
### Removed Features \(previously deprecated\)

* The <code>netapp\.cloudmanager</code> collection was considered unmaintained and has been removed from Ansible 15 \([https\://forum\.ansible\.com/t/44891](https\://forum\.ansible\.com/t/44891)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install netapp\.cloudmanager</code>\.
* The cyberark\.pas collection has been removed from Ansible 15 due to violations of the Ansible inclusion requirements\.
  The collection has violated the inclusion requirements multiple times\, including those surrounding repository management\. The collection maintainers did not respond to the latest violation report\.
  See [Collections Removal Process for collections not satisfying the collection requirements](https\://docs\.ansible\.com/projects/ansible/devel/community/collection\_contributors/collection\_package\_removal\.html\#collections\-not\-satisfying\-the\-collection\-requirements) for more details \([https\://forum\.ansible\.com/t/45816](https\://forum\.ansible\.com/t/45816)\)\.
  Users can still install this collection with <code>ansible\-galaxy collection install cyberark\.pas</code>\.

<a id="ansible-core-5"></a>
#### Ansible\-core

* Remove deprecated <code>ANSIBLE\_CONNECTION\_PATH</code> option
* Remove deprecated <code>DEFAULT\_LIBVIRT\_LXC\_NOSECLABEL</code> option\.
* url/uri \- remove deprecated use of <code>yes</code>/<code>no</code> values for the <code>follow\_redirects</code> option \([https\://github\.com/ansible/ansible/issues/86790](https\://github\.com/ansible/ansible/issues/86790)\)
* yum\_repository \- Removed deprecated parameters\.

<a id="community-postgresql-3"></a>
#### community\.postgresql

* postgresql modules \- the <code>login</code>\, <code>host</code>\, <code>unix\_socket</code> and <code>port</code> aliases have been removed in <code>community\.postgresql 5\.0\.0</code>\. Use the <code>login\_user</code>\, <code>login\_host</code>\, <code>login\_unix\_socket</code> and <code>login\_port</code> options instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/847](https\://github\.com/ansible\-collections/community\.postgresql/issues/847)\)\.
* postgresql\_copy \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_db \- the <code>rename</code> choice of the <code>state</code> option has been removed\. Use the <code>community\.postgresql\.postgresql\_query</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/833](https\://github\.com/ansible\-collections/community\.postgresql/issues/833)\)\.
* postgresql\_ext \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_idx \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_membership \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_owner \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_pg\_hba \- the <code>keep\_comments\_at\_rules</code> option has been removed\. It had no effect since it was deprecated \([https\://github\.com/ansible\-collections/community\.postgresql/issues/810](https\://github\.com/ansible\-collections/community\.postgresql/issues/810)\)\.
* postgresql\_ping \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_privs \- the <code>db</code> and <code>database</code> aliases of the <code>login\_db</code> option have been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_publication \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_query \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_schema \- the <code>db</code> and <code>database</code> aliases of the <code>login\_db</code> option have been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_script \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_sequence \- the <code>db</code> and <code>database</code> aliases of the <code>login\_db</code> option have been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_sequence \- the <code>rename\_to</code> option has been removed\. Use the <code>community\.postgresql\.postgresql\_query</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/833](https\://github\.com/ansible\-collections/community\.postgresql/issues/833)\)\.
* postgresql\_set \- the module has been removed\. Please use the <code>community\.postgresql\.postgresql\_alter\_system</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/823](https\://github\.com/ansible\-collections/community\.postgresql/issues/823)\)\.
* postgresql\_slot \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_subscription \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_table \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_table \- the <code>rename</code> option has been removed\. Use the <code>community\.postgresql\.postgresql\_query</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/833](https\://github\.com/ansible\-collections/community\.postgresql/issues/833)\)\.
* postgresql\_tablespace \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_tablespace \- the <code>rename\_to</code> option has been removed\. Use the <code>community\.postgresql\.postgresql\_query</code> module instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/833](https\://github\.com/ansible\-collections/community\.postgresql/issues/833)\)\.
* postgresql\_user \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.
* postgresql\_user\_obj\_stat\_info \- the <code>db</code> alias of the <code>login\_db</code> option has been removed\. Use the <code>login\_db</code> option instead \([https\://github\.com/ansible\-collections/community\.postgresql/issues/831](https\://github\.com/ansible\-collections/community\.postgresql/issues/831)\)\.

<a id="hetzner-hcloud-3"></a>
#### hetzner\.hcloud

* hcloud inventory \- The deprecated <code>hcloud\_datacenter</code> host variable was removed\. Please use the <code>hcloud\_location</code> host variable instead\.
* network\_info \- The deprecated <code>hcloud\_network\_info\[\]\.servers\[\]\.datacenter</code> return value was removed\. Please use the <code>hcloud\_network\_info\[\]\.servers\[\]\.location</code> return value instead\.
* primary\_ip \- The deprecated <code>datacenter</code> argument was removed\. Please use the <code>location</code> argument instead\.
* primary\_ip \- The deprecated <code>hcloud\_primary\_ip\.datacenter</code> return value was removed\. Please use the <code>hcloud\_primary\_ip\.location</code> return value instead\.
* primary\_ip\_info \- The deprecated <code>hcloud\_primary\_ip\_info\[\]\.datacenter</code> return value was removed\. Please use the <code>hcloud\_primary\_ip\_info\[\]\.location</code> return value instead\.
* server \- The deprecated <code>datacenter</code> argument was removed\. Please use the <code>location</code> argument instead\.
* server \- The deprecated <code>hcloud\_server\.datacenter</code> return value was removed\. Please use the <code>hcloud\_server\.location</code> return value instead\.
* server\_info \- The deprecated <code>hcloud\_server\_info\[\]\.datacenter</code> return value was removed\. Please use the <code>hcloud\_server\_info\[\]\.location</code> return value instead\.

<a id="ngine-io-cloudstack-1"></a>
#### ngine\_io\.cloudstack

* The deprecated routing to module names with <code>cs\_</code> prefix has been removed\. Use the new module names instead\.

<a id="security-fixes"></a>
### Security Fixes

<a id="ansible-core-6"></a>
#### Ansible\-core

* ansible\-galaxy install \- Ensure role requirements are passed as positional arguments to <a href="#system-message-1"><span class="problematic">\:command\:\`git clone\`</span></a>\. Previously\, a malicious role author could inject arbitrary git configuration in role dependencies\. \(CVE\-2026\-11332\)

  <details>
  <summary><strong>ERROR/3</strong> (&lt;string&gt;, line 1)</summary>

  Unknown interpreted text role \"command\"\.

  </details>
* psrp \- Do not log raw stdout/stderr on verbosity 5 when task has <code>no\_log\: true</code> set
* winrm \- Do not log raw stdout/stderr on verbosity 5 when task has <code>no\_log\: true</code> set

<a id="ansible-posix"></a>
#### ansible\.posix

* authorized\_key \- fix local privilege escalation via symlink\-following when running as root \([https\://github\.com/ansible\-collections/ansible\.posix/issues/759](https\://github\.com/ansible\-collections/ansible\.posix/issues/759)\)\.

<a id="graphiant-naas-1"></a>
#### graphiant\.naas

* Mask API keys in <code>\_SENSITIVE\_LOG\_KEYS</code> \(<code>device\_config\_common</code>\) in <code>gcsdk\_client</code> <code>put\_device\_config</code> / <code>put\_device\_config\_raw</code> and <code>show\_validated\_payload</code> log output

<a id="splunk-es-2"></a>
#### splunk\.es

* tests\.yml \- replaced <code>pull\_request\_target</code> trigger with <code>pull\_request</code> for all code\-testing jobs \(<code>sanity</code>\, <code>unit\-galaxy</code>\, <code>ansible\-lint</code>\, <code>build\-import</code>\)\. Using <code>pull\_request\_target</code> exposed repository secrets to workflows that execute untrusted fork code\, creating a potential secret\-exfiltration vector \(pwn request\)\.

<a id="bugfixes"></a>
### Bugfixes

<a id="ansible-core-7"></a>
#### Ansible\-core

* Add deprecation status to the tree and oneline callback DOCUMENTATION\. \([https\://github\.com/ansible/ansible/issues/87020](https\://github\.com/ansible/ansible/issues/87020)\)
* Fix <code>validate\_argspec</code> when tags are defined on the play\. The <code>always</code> tag is only added if the play has no tags\.
* Internal patch framework \- Defer failure on missing target patch attribute until <em class="title-reference">is\_patch\_needed</em> validator has confirmed that the behavior to be patched is present\.
* The user module\, now unlinks target ssh key files if they are symlinks to avoid overwriting their sources\.
* The user module\, will no longer remove existing public key files in check mode\.
* <code>\-\-start\-at\-task</code> \- fix starting at the requested task instead of starting at the next block or play\. Play level tasks run first\. \([https\://github\.com/ansible/ansible/issues/86268](https\://github\.com/ansible/ansible/issues/86268)\)
* <code>ansible\-doc \-t filter\|test \<plugin\></code> \- remove empty bullet point from the description\.
* ansible\-galaxy \- Fix attempting to download the collection again if the response from the server is shorter than expected\, instead of failing due to the mismatched artifact hash on the first attempt\. \([https\://github\.com/ansible/ansible/pull/86025](https\://github\.com/ansible/ansible/pull/86025)\)
* ansible\-test \- Allow root to use sudo on managed Alpine instances\.
* ansible\-test \- Ensure the bundled debugpy module from VSCode is available in the <code>\-\-dev\-debug\-on\-demand</code> environment\.
* ansible\-test \- Fix target filtering to preserve user\-specified versions that are not in the completion configuration\.
* ansible\-test \- Only add volume bind mount for <code>docker\.sock</code> when using docker
* ansible\-test remote alias \- Alias values for <code>\-\-controller</code> and <code>\-\-target</code> are properly resolved for <code>remote</code>\. Previously\, remote alias values \(e\.g\. <code>fedora/latest</code>\) resolved to the correct name only for the legacy <code>\-\-remote</code> arg\, failing with an unknown image error for the newer args\.
* apt\_key module now masks authentication information in all displays and returns of uri information\.
* apt\_repository \- treat a source line whose type is valid but which has fewer than two following fields \(for example a bare <code>deb</code>\) as invalid instead of raising an <code>IndexError</code> while parsing sources\.list files\.
* apt\_repository \- validate the line in sources\.list \([https\://github\.com/ansible/ansible/issues/85715](https\://github\.com/ansible/ansible/issues/85715)\)\.
* async \- fix error message when the async task did not complete within the requested time\.
* basic\.py \- Fix typo in deprecation message for use of the <code>get\_platform</code> function\.
* cli \- handle empty value for PAGER \([https\://github\.com/ansible/ansible/issues/86898](https\://github\.com/ansible/ansible/issues/86898)\)\.
* collection loader \- Fix the collection loader logic to correctly return Python module when calling <code>pkgutil\.iter\_modules</code> with a package that is inside a collection path and contains compiled Python extension modules\.
* config \- Include the origin in error message indicating an invalid choice in a configuration value
* config \- use correct key value for inject\_invocation setting \([https\://github\.com/ansible/ansible/issues/86999](https\://github\.com/ansible/ansible/issues/86999)\)\.
* delegate\_to \- reject a literal empty hostname consistently with a template that resolves to an empty hostname \([https\://github\.com/ansible/ansible/issues/84332](https\://github\.com/ansible/ansible/issues/84332)\)\.
* distribution facts \- classify UnionTech OS Server \(UOS Server\) as <code>RedHat</code> <code>os\_family</code> instead of <code>Debian</code>\. UOS Server is RPM\-based and built on top of openAnolis \(A version\, codename <code>kongzi</code>\) or openEuler \(E version\, codename <code>fuyu</code>\)\, and advertises <code>PLATFORM\_ID\=\"platform\:uel\*\"</code> in <code>/etc/os\-release</code>\. The Debian\-based Desktop edition is unchanged \([https\://github\.com/ansible/ansible/issues/86957](https\://github\.com/ansible/ansible/issues/86957)\)\.
* dnf5 module \- Set the dnf <code>destdir</code> configuration option from <code>download\_dir</code> when <code>download\_only</code> is true\, as documented\.
* encrypt \- fix bcrypt salt string formatting on musl libc by ensuring it is always zero\-padded to 2 digits \([https\://github\.com/ansible/ansible/issues/87180](https\://github\.com/ansible/ansible/issues/87180)\)\.
* free strategy \- Fix <code>IndexError</code> when hosts become unreachable during playbook execution \([https\://github\.com/ansible/ansible/issues/87027](https\://github\.com/ansible/ansible/issues/87027)\)\.
* free strategy \- prevent hanging on skipping a task using <code>\-\-step</code> \([https\://github\.com/ansible/ansible/issues/86656](https\://github\.com/ansible/ansible/issues/86656)\)
* get\_url module now masks authentication information in all displays and returns of uri information\.
* getent \- fail with error when service is provided on platforms using busybox like alpine \([https\://github\.com/ansible/ansible/issues/85568](https\://github\.com/ansible/ansible/issues/85568)\)\.
* git \- fix <code>force</code> parameter to properly preserve local commits when set to <code>false</code> and fail with a clear error message \([https\://github\.com/ansible/ansible/issues/83367](https\://github\.com/ansible/ansible/issues/83367)\)
* git \- remove redundant error checks after <em class="title-reference">run\_command\(check\_rc\=True\)</em>
* git \- use the branch configured in <code>\.gitmodules</code> or the remote HEAD instead of hardcoding <code>master</code> when <code>track\_submodules\=yes</code> \([https\://github\.com/ansible/ansible/issues/77691](https\://github\.com/ansible/ansible/issues/77691)\)\.
* meta pseudo\-action \- Fixed callback args passed to <code>v2\_runner\_on\_skipped</code> when any <code>meta</code> action was skipped by a <code>when</code> condition\; added test coverage\. A previous regression caused the callback dispatch to be omitted and a warning issued\.
* module\_utils \- <code>check\_type\_int</code> now raises the documented <code>TypeError</code> \(instead of an uncaught <code>OverflowError</code>\) for the string values <code>inf</code>\, <code>\-inf</code> and <code>Infinity</code>\, which <code>decimal\.Decimal</code> accepts but cannot be converted to an <code>int</code>\.
* module\_utils \- <code>is\_netmask</code> now rejects non\-contiguous netmasks such as <code>255\.255\.0\.255</code>\, where each octet is individually valid but the mask is not a contiguous run of network bits followed by host bits \([https\://github\.com/ansible/ansible/pull/87235](https\://github\.com/ansible/ansible/pull/87235)\)\.
* module\_utils \- <code>mask\_url</code> now masks the password in URLs that contain a password but no username\, such as <code>redis\://\:password\@host</code>\, instead of returning them unmasked\.
* module\_utils \- fix module initialization failures on QNX Neutrino 6\.5\.0 by specifying IPv4 stream socket hints in the <code>socket\.getaddrinfo</code> integer\-subclass compatibility probe \([https\://github\.com/ansible/ansible/issues/87496](https\://github\.com/ansible/ansible/issues/87496)\)\.
* module\_utils sanitize\_keys and remove\_value functions now sort their input to ensure matching subsets are always obscured\.
* module\_utils\.urls now all errors mask in line url authentication information\.
* module\_utils/basic\.py \- Fix <code>AnsibleModule\.run\_command\(\)</code> to handle <code>None</code> return from non\-blocking pipe reads \([https\://github\.com/ansible/ansible/issues/86920](https\://github\.com/ansible/ansible/issues/86920)\)\.
* parallel fact gathering \- fix hang caused by corrupt async job files\.
* pip \- resolve relative virtualenv paths consistently\, including when used with chdir \([https\://github\.com/ansible/ansible/issues/81522](https\://github\.com/ansible/ansible/issues/81522)\, [https\://github\.com/ansible/ansible/issues/84905](https\://github\.com/ansible/ansible/issues/84905)\)\.
* powershell exec\_wrapper \- fix handling when multiple pwsh executables match by selecting the first result \([https\://github\.com/ansible/ansible/issues/87228](https\://github\.com/ansible/ansible/issues/87228)\)\.
* rpm\_key \- Fix module failure when fetching GPG keys from FTP URLs \([https\://github\.com/ansible/ansible/issues/83321](https\://github\.com/ansible/ansible/issues/83321)\)\.
* rpm\_key \- ensure a trailing newline is present on PGP armor data before passing it to librpm for parsing\, fixing failures on systems where <code>pgpParsePkts</code> requires it \([https\://github\.com/ansible/ansible/issues/87303](https\://github\.com/ansible/ansible/issues/87303)\)\.
* rpm\_key module now masks authentication information in all displays and returns of uri information\.
* serialization \- Preserve <code>fold</code> on tagged <code>datetime\.time</code> and <code>datetime\.datetime</code> instances\.
* ssh connection \- fix an issue with become when <code>sftp\_extra\_args</code>/<code>scp\_extra\_args</code> would contain the value of <code>ssh\_executable</code> \([https\://github\.com/ansible/ansible/issues/87272](https\://github\.com/ansible/ansible/issues/87272)\)
* ssh connection plugin \- malformed <code>ssh\_args</code>/<code>ssh\_common\_args</code>/<code>ssh\_extra\_args</code> \(e\.g\. a trailing <code>\-o</code> with no value\) no longer crash the worker process \(\"A worker was found in a dead state\"\)\; the ssh client\'s own error is reported instead\.
* ssh\-agent \- cap agent response size to match OpenSSH limits
* ssh\-agent \- fix partial socket reads
* ssh\-agent \- fix wire format serialization for zero\-length values
* su become plugin \- Add recognition of password failure for BusyBox version of <code>su</code>\.
* subelements \- fix error message when an empty subelements is provided \([https\://github\.com/ansible/ansible/issues/87398](https\://github\.com/ansible/ansible/issues/87398)\)\.
* sudo become plugin is now compatible with sudo\-rs \(rust implementation\)\.
* task results \- The <code>invocation</code> item result key omitted from registered values for looped task results\, unless enabled via <code>INJECT\_INVOCATION</code>\. Previously\, it was deleted from registered non\-loop results and only available to callbacks\.
* tempfile \- reject prefix and suffix values that contain path components to prevent path traversal\.
* template action \- restore <code>failed\_when</code> support when the template source file is not found on the controller \([https\://github\.com/ansible/ansible/issues/87491](https\://github\.com/ansible/ansible/issues/87491)\)\.
* uri \- Enable multipart/form\-data requests over 2GB \([https\://github\.com/ansible/ansible/issues/76666](https\://github\.com/ansible/ansible/issues/76666)\)
* uri module now masks authentication information in all displays and returns of uri information\.
* url lookup now masks authentication information in all displays and returns of uri information\.
* user \- On BusyBox systems\, warn when an invalid shell is specified \([https\://github\.com/ansible/ansible/pull/86342](https\://github\.com/ansible/ansible/pull/86342)\)
* user \- fix <code>move\_home</code> on BusyBox/Alpine to move existing home contents before rewriting <code>/etc/passwd</code> \([https\://github\.com/ansible/ansible/pull/87044](https\://github\.com/ansible/ansible/pull/87044)\)\.
* user \- warn if move\_home is true and home directory does not exist \([https\://github\.com/ansible/ansible/issues/37398](https\://github\.com/ansible/ansible/issues/37398)\)\.
* wait\_for \- use <code>errno\.ENOENT</code> symbolic constant instead of hardcoded value for improved code portability\.

<a id="amazon-aws-1"></a>
#### amazon\.aws

* aws\_ssm \- Fixed PowerShell command execution timeouts on Windows caused by PTY echo issues\. Commands are now uploaded to S3 and executed via a small wrapper to avoid echoing large payloads to stdout \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Fixed PowerShell stdin handling for modules that require stdin input on Windows hosts \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Fixed Windows SSM connection failures when transferring files with Unicode characters in filenames or content\. The connection plugin now properly handles UTF\-8 encoding throughout the S3 upload/download process \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- Fixed stderr message accumulation across multiple command executions\. Stderr is now flushed at the start of each command to prevent error messages from previous commands appearing in subsequent command output \([https\://github\.com/ansible\-collections/amazon\.aws/pull/2909](https\://github\.com/ansible\-collections/amazon\.aws/pull/2909)\)\.
* aws\_ssm \- suppress PowerShell progress output in Windows file transfers to prevent stdout pollution that causes transfer failures \([https\://github\.com/ansible\-collections/amazon\.aws/pull/3013](https\://github\.com/ansible\-collections/amazon\.aws/pull/3013)\)\.

<a id="ansible-mysql-2"></a>
#### ansible\.mysql

* mysql\_user \- fix errors on MySQL 9\.7\.0\+ caused by removal of SHA1\(\) SQL function and mysql\_native\_password plugin\. The module now uses <code>IDENTIFIED BY</code> for password management on MySQL 9\.7\.0\+\.

<a id="ansible-netcommon-1"></a>
#### ansible\.netcommon

* cli\_config\: Apply C\(diff\_ignore\_lines\) when comparing the before/after running\-config snapshots on platforms that support neither onbox diff nor generate diff\, so volatile configuration lines no longer cause C\(changed\=true\) on every run \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/156](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/156)\)\.
* cli\_config\: Fail with a clear error instead of silently pushing configuration when the connection plugin\'s capabilities cannot be determined \(for example due to a malformed or empty response\)\, rather than treating that failure the same as a platform explicitly declaring no diff support \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/156](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/156)\)\.
* cli\_config\: Push configuration and detect changes by comparing running\-config snapshots taken before and after the change\, for platforms whose cliconf plugin supports neither onbox diff nor generate diff\. Previously the configuration was silently never pushed to the device in this scenario \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/156](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/156)\)\.
* libssh \- Use <code>persistent\_connect\_timeout</code> option for the SSH connect timeout instead of the generic play context timeout\, ensuring that <code>ansible\_connect\_timeout</code> / <code>ANSIBLE\_PERSISTENT\_CONNECT\_TIMEOUT</code> is respected \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/798](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/798)\)\.
* memory cache plugin \- Add missing <code>\_persistent</code> attribute to <code>CacheModule</code> to fix <code>\'CacheModule\' object has no attribute \'\_persistent\'</code> error with ansible\-core 2\.19\+ when <code>single\_user\_mode</code> caching is enabled \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/781](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/781)\)\.
* netconf \- Enable <code>huge\_tree\=True</code> for all XML parsing operations to support NETCONF responses containing text nodes larger than 10MB \(lxml\'s default <code>XML\_MAX\_TEXT\_LENGTH</code> limit\)\. Fixes <code>XMLSyntaxError\: Resource limit exceeded</code> when fetching or pushing large configurations via <code>netconf\_get</code> or <code>netconf\_config</code> \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/255](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/255)\)\.
* network\_cli \- Fix <code>proxy\_command</code> silently ignored with <code>ssh\_type\=paramiko</code> \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/776](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/776)\)\.
* vlan\_parser \- Fix <code>IndexError</code> when an empty list is passed as input by returning an empty list instead of crashing \([https\://github\.com/ansible\-collections/ansible\.netcommon/issues/302](https\://github\.com/ansible\-collections/ansible\.netcommon/issues/302)\)\.

<a id="ansible-posix-1"></a>
#### ansible\.posix

* README \- Added <code>Red Hat Automation Hub</code> as correct contact information for Red Hat Ansible Automation Platform subscribers\.
* sysctl \- reload sysctl only if the sysctl file is <code>/etc/sysctl\.conf</code> or <code>/etc/sysctl\.conf\.local</code> \([https\://github\.com/ansible\-collections/ansible\.posix/issues/663](https\://github\.com/ansible\-collections/ansible\.posix/issues/663)\)\.

<a id="ansible-utils-1"></a>
#### ansible\.utils

* AnsibleArgSpecValidator \- Add a <em class="title-reference">\_to\_plain</em> function to handle ansible\-core 2\.21\+ deep copy warnings by lazy containers\.
* Fix update\_fact to update a fact where a key in the referenced path contains a bracket\.

<a id="ansible-windows-1"></a>
#### ansible\.windows

* setup \- Ensure the <code>ansible\_domain</code> fact has the DNS domain name the host is registered with through the IP properties\. In the past we only returned a value for this fact when the host was joined to an Active Directory domain \- [https\://github\.com/ansible\-collections/ansible\.windows/pull/917](https\://github\.com/ansible\-collections/ansible\.windows/pull/917)
* setup \- Fix DomainInfo collection when LanmanWorkstation service is stopped or disabled on hardened Windows systems \([https\://github\.com/ansible\-collections/ansible\.windows/pull/915](https\://github\.com/ansible\-collections/ansible\.windows/pull/915)\)\.
* setup \- Fix admin checks to ensure facts that require administrator access actually run \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/900](https\://github\.com/ansible\-collections/ansible\.windows/issues/900)
* setup \- Fix failure when attempting to retrieve <code>ansible\_processor\_cores</code> and <code>ansible\_processor\_threads\_per\_core</code> on a host without the required SMBIOS data\. Admin users can still retrieve this through WMI but non\-admin users will set these facts as null and avoid the lengthy timeout and failure\.
* setup \- Fix logic for checking SMBIOS version for <code>ansible\_processor\_\*</code> facts when the host\'s SMBIOS version was greater than <code>2\.4</code> but less than <code>3\.0</code> \- [https\://github\.com/ansible\-collections/ansible\.windows/pull/919](https\://github\.com/ansible\-collections/ansible\.windows/pull/919)
* win\_copy \- Fix error when setting <code>dest</code> to just the filename\. The destination in this case will be the working directory set by the connection plugin\.
* win\_dhcp\_lease \- Fix scope filtering when searching for existing leases or reservations\: ensure the query is limited to the specified scope\. This prevents ambiguity when the same MAC address exists in multiple scopes \(e\.g\. a device with reservations in different scopes\)\.
* win\_find \- Fix depth and recursion logic that resulted in directories being skipped or depth being ignored \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/839](https\://github\.com/ansible\-collections/ansible\.windows/issues/839)
* win\_mapped\_drive \- Fixed compatibility with PowerShell 7 by fixing inline C\# declaration
* win\_package \- Favour the HTTP response\'s <code>Content\-Disposition</code> for the temporary filename when downloading a the temporary package from a URL\. This ensures the package detection mechanism on the file extension continues to work \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/503](https\://github\.com/ansible\-collections/ansible\.windows/issues/503)
* win\_powershell \- Fix support for controller side <code>path</code> lookups on Ansible 2\.18 and older
* win\_reboot \- Display warning if the reboot command returned <code>A system shutdown is in progress\. \(1115\)</code>\. This can be triggered by a service external to Ansible triggers the shutdown and Ansible attempts to reboot by running <code>shutdown\.exe</code>\.
* win\_stat / win\_find \- try/catch Access Denied when querying Win32\_Share for share info\. Non\-admin users now get warning instead of failure\. Fixes 809\.
* win\_template \- Fix issue where errors during templating\, like an undefined variable\, were ignored and the task continued without a failure \- [https\://github\.com/ansible\-collections/ansible\.windows/issues/926](https\://github\.com/ansible\-collections/ansible\.windows/issues/926)
* win\_updates \- Add additional post reboot check to ensure that Windows is still not performing more update work after a reboot is complete\.
* win\_updates \- Fix issue display warnings after data tagging changes made in Ansible 2\.19\.
* win\_updates \- Handle update task that errors with <code>ERROR\_SHUTDOWN\_IN\_PROGRESS</code> when <code>reboot\=True</code> is set\. If this error is received and the task has <code>reboot\=True</code> then the module will wait for the reboot to be complete before trying again like how other errors are handled\.

<a id="arista-eos-1"></a>
#### arista\.eos

* eos terminal plugin \- Fix on\_become enable prompt failing with TACACS\+ authentication due to missing trailing space in password prompt \([https\://github\.com/ansible\-collections/arista\.eos/issues/665](https\://github\.com/ansible\-collections/arista\.eos/issues/665)\)\.
* eos\_acls \- Fix issue where <code>state\: replaced</code> did not generate the <code>standard</code> keyword for standard ACLs \([https\://github\.com/ansible\-collections/arista\.eos/issues/608](https\://github\.com/ansible\-collections/arista\.eos/issues/608)\)\.
* eos\_acls \- Fix state replaced putting ACEs under wrong ACL context when multiple ACLs require changes and a new ACL sorts alphabetically before an existing one \([https\://github\.com/ansible\-collections/arista\.eos/issues/643](https\://github\.com/ansible\-collections/arista\.eos/issues/643)\)\.
* eos\_config \- extend multiline eAPI block detection to include <code>code</code> and <code>code unit</code> \(Routing Control Functions / RCF\) in addition to <code>banner</code>\; also bypass <code>NetworkConfig</code> in config\-replace mode which was dropping closing brace lines from RCF function bodies\, causing EOS compilation failures \([https\://github\.com/ansible\-collections/arista\.eos/issues/632](https\://github\.com/ansible\-collections/arista\.eos/issues/632)\)\.

<a id="cisco-ios-1"></a>
#### cisco\.ios

* ios\_acls \- Correct port to protocol mapping for port 5001 and 5002\.
* ios\_acls \- Fix incorrect CLI command generation for IPv6 ACL remarks\. The module now correctly generates <code>sequence N remark</code> syntax for IPv6 instead of the IPv4\-style <code>N remark</code> format\. Negation also correctly uses <code>no sequence N remark</code>\.
* ios\_acls \- Fixed ACL option fields with multi\-word names \(e\.g\, any\_options\, stream\_id \, no\_op\) failing due to missing underscore to hyphen conversion and vice\-versa in setval and getval respectively
* ios\_bgp\_address\_family \- Add <code>vpls</code> as a valid <code>safi</code> choice for the <code>l2vpn</code> address family configuration\.
* ios\_bgp\_address\_family \- Fix idempotency issue where specifying <code>remote\_as</code> for a neighbor caused the module to emit <code>neighbor X remote\-as Y</code> on every run\.  It can be specified at address\-family and at global level\, but always resides at the global level\. Hence\, the config class now correctly associates global\-level attributes with the corresponding address\-family during have\-facts comparison\.
* ios\_bgp\_address\_family \- Fix replaced state not generating <code>no neighbor X route\-map/prefix\-list</code> commands when a route\-map or prefix\-list is present in have but absent from want\.
* ios\_bgp\_address\_family \- Update <em class="title-reference">\_compare\_redist\_ospf</em> loop to read both ospf and ospfv3 as parser inputs
* ios\_bgp\_global \- fix ios\_bgp\_global and ios\_facts crash on ASDOT \(4\-byte dotted\) local\_as notation \(e\.g\. \"501\.65083\"\) by changing local\_as\.number argspec type from int to str\, consistent with remote\_as which already accepts ASDOT values
* ios\_hsrp\_interfaces \- Fixed parsed\-state integration tests to handle Ansible\-core masking <code>\$REDACTED\$</code> values while retaining compatibility with older <code>VALUE\_SPECIFIED\_IN\_NO\_LOG\_PARAMETER</code> results\.
* ios\_hsrp\_interfaces \- Fixed use\_bia\.set\:false not generating \"no standby use\-bia\" by adding compval \"use\_bia\.set\" to the parser so comparison evaluates the boolean leaf instead of the parent dict \(which is always truthy\)\.
* ios\_route\_maps \- fix bare entries \(action\+sequence only\) being silently dropped\; the cmd\_len guard in entries\_compare\(\) now emits the route\-map header command even when no sub\-commands are generated \(description/match/set absent\)\, so catch\-all rules like <code>route\-map MYMAP deny 6</code> are correctly applied\.
* ios\_route\_maps \- fix continue\_entry\.set\=true silently ignored\; bare \"continue\" command was never generated because the setval template raised UndefinedError when entry\_sequence was absent\.
* ios\_snmp\_server \- anchor the <code>traps\.vrrp</code> parser regex with <code>\$</code> so that <code>snmp\-server enable traps vrrpv3</code> lines are not incorrectly parsed as <code>traps\.vrrp</code>\.
* ios\_user \- fixed hashed\_password idempotency so that re\-applying the same type/value pair against an already\-configured user produces no commands\, preventing unnecessary password updates on repeat runs\.
* ios\_user \- parse\_hashed\_password  helper now extracts the stored hash type\, hash value from running config\, enabling proper diff\-based idempotency checks for hashed\_password\.
* ios\_user \- update\_password and password\_type are now resolved per aggregate item via get\_param\_value\, allowing each entry in the aggregate list to independently override the module\-level defaults
* plugins/modules/ios\_user\.py \- Fix matching existing SSH keys in running configurations while allowing optional trailing whitespace  when using the purge\_keys parameter\.
* terminal \- Add <code>\% IPv6 routing not enabled</code> to <code>terminal\_stderr\_re</code> so that configuring BGP IPv6/VPNv6 address\-family without <code>ipv6 unicast\-routing</code> correctly raises an error instead of silently succeeding \([https\://github\.com/ansible\-collections/cisco\.ios/issues/1301](https\://github\.com/ansible\-collections/cisco\.ios/issues/1301)\)\.

<a id="cisco-iosxr-1"></a>
#### cisco\.iosxr

* bgp\_global \- Fixed neighbor shutdown state parsing to correctly handle \'no shutdown\' command\, ensuring proper idempotency when toggling neighbor shutdown state\.
* bgp\_global \- Removed stale <em class="title-reference">\_build\_key</em> function present in <em class="title-reference">\_bgp\_list\_to\_dict</em> within the config py file\.
* iosxr\_bgp\_neighbor\_address\_family \- Fix fact gathering crash when neighbors use <code>default\-originate route\-policy</code> or <code>default\-originate inheritance\-disable</code> by only setting <code>set</code> for the bare <code>default\-originate</code> form\.
* iosxr\_ospfv2 \- Enhanced max\-metric router\-lsa support with comprehensive configuration options \(external\-lsa\, summary\-lsa\, on\-startup with wait\_for\_bgp/wait\_period\, include\-stub\)\, added mutual exclusivity validation for conflicting parameters\, corrected on\_startup\.wait\_for\_bgp parameter type from integer to boolean\, and fixed idempotency across all states\.
* netconf \- Parse large XML config strings with <code>huge\_tree\=True</code> in <code>edit\_config</code> to prevent lxml from rejecting payloads exceeding the default 10MB text\-node limit\.
* route\_maps \- Fix <code>set med \+\<N\></code> / <code>set med \-\<N\></code> parsing in <code>Route\_mapsTemplate</code> so that incremental MED statements using device\-native attached\-sign syntax are no longer silently skipped during fact gathering\.

<a id="cisco-meraki-1"></a>
#### cisco\.meraki

* Invocation parameter added to the result\.
* devices \- Renamed <em class="title-reference">organization\_id</em> to <em class="title-reference">organizationId</em> in the request object and dropped the <em class="title-reference">serial</em>/<em class="title-reference">organizationId</em> entries from the update\-comparison logic\.
* devices\_cellular\_sims \- Corrected the eSIM documentation\, replacing the fixed reference to <em class="title-reference">sim3</em> with guidance to use the device\'s actual raw eSIM slot \(e\.g\.\, sim2 or sim3\)\.
* devices\_live\_tools\_leds\_blink \- Renamed <em class="title-reference">leds\_blink\_id</em> to <em class="title-reference">ledsBlinkId</em> and removed the <em class="title-reference">ledsBlinkId</em> entry from the update\-comparison logic\.
* devices\_live\_tools\_mac\_table \- Renamed <em class="title-reference">mac\_table\_id</em> to <em class="title-reference">macTableId</em> and removed it from the update\-comparison logic\.
* devices\_live\_tools\_multicast\_routing \- Fixed the internal <em class="title-reference">multicastRoutingId</em> key mapping \(previously stored as <em class="title-reference">multicast\_routing\_id</em>\) and removed it from the update\-comparison logic\.
* devices\_live\_tools\_ping \- Removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* devices\_live\_tools\_ping\_device \- Removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* devices\_sensor\_commands \- Renamed <em class="title-reference">command\_id</em> to <em class="title-reference">commandId</em> and removed the <em class="title-reference">commandId</em> entry from the update\-comparison logic\.
* devices\_switch\_ports \- Renamed <em class="title-reference">port\_id</em> to <em class="title-reference">portId</em> and removed the <em class="title-reference">portId</em> entry from the update\-comparison logic\.
* devices\_switch\_routing\_interfaces \- Removed the erroneous <em class="title-reference">interfaceId</em> entry from the update\-comparison logic\.
* devices\_switch\_routing\_interfaces\_dhcp \- Renamed <em class="title-reference">interface\_id</em> to <em class="title-reference">interfaceId</em> and removed the <em class="title-reference">interfaceId</em> entry from the update\-comparison logic\.
* devices\_switch\_routing\_static\_routes \- Removed the <em class="title-reference">staticRouteId</em> entry from the update\-comparison logic\.
* devices\_wireless\_bluetooth\_settings \- Fixed a malformed UUID in the module\'s EXAMPLES block\.
* devices\_wireless\_zigbee\_enrollments \- Fixed the internal <em class="title-reference">enrollmentId</em> key mapping \(previously stored as <em class="title-reference">enrollment\_id</em>\) and removed it from the update\-comparison logic\.
* networks\_appliance\_content\_filtering\_categories\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_appliance\_firewall\_cellular\_firewall\_rules\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_appliance\_firewall\_firewalled\_services \- Removed the <em class="title-reference">service</em> entry from the update\-comparison logic\.
* networks\_appliance\_firewall\_l3\_firewall\_rules\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_appliance\_firewall\_l7\_firewall\_rules\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_appliance\_firewall\_one\_to\_many\_nat\_rules\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_appliance\_firewall\_one\_to\_one\_nat\_rules\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_appliance\_ports \- Fixed the internal <em class="title-reference">portId</em> parameter key mapping \(previously stored as <em class="title-reference">port\_id</em>\) and removed it from the update\-comparison logic since it is a path identifier\.
* networks\_appliance\_prefixes\_delegated\_statics \- Removed the <em class="title-reference">staticDelegatedPrefixId</em> entry from the update\-comparison logic\.
* networks\_appliance\_ssids \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_appliance\_static\_routes \- Corrected the <em class="title-reference">gatewayVlanId</em> argument type from <em class="title-reference">str</em> to <em class="title-reference">int</em>\, and removed the path\-identifier <em class="title-reference">staticRouteId</em> field from the update\-comparison logic\.
* networks\_appliance\_traffic\_shaping\_custom\_performance\_classes \- Fixed the internal <em class="title-reference">customPerformanceClassId</em> key mapping and removed it from the update\-comparison logic since it is a path identifier\.
* networks\_appliance\_vlans \- Removed <em class="title-reference">vlanId</em> from the update\-comparison logic since it is the path identifier\, not a body field to compare\.
* networks\_camera\_wireless\_profiles \- Removed the <em class="title-reference">wirelessProfileId</em> entry from the update\-comparison logic\.
* networks\_clients\_policy \- Renamed <em class="title-reference">client\_id</em> to <em class="title-reference">clientId</em> and removed the <em class="title-reference">clientId</em> entry from the update\-comparison logic\.
* networks\_clients\_splash\_authorization\_status \- Renamed <em class="title-reference">client\_id</em> to <em class="title-reference">clientId</em> and removed the <em class="title-reference">clientId</em> entry from the update\-comparison logic\.
* networks\_firmware\_upgrades\_staged\_groups \- Removed the <em class="title-reference">groupId</em> entry from the update\-comparison logic\.
* networks\_floor\_plans \- Removed the <em class="title-reference">floorPlanId</em> entry from the update\-comparison logic\.
* networks\_group\_policies \- Removed the <em class="title-reference">groupPolicyId</em> entry from the update\-comparison logic\.
* networks\_meraki\_auth\_users \- Removed the <em class="title-reference">merakiAuthUserId</em> entry from the update\-comparison logic\.
* networks\_sensor\_alerts\_profiles \- Removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* networks\_sensor\_mqtt\_brokers \- Renamed <em class="title-reference">mqtt\_broker\_id</em> to <em class="title-reference">mqttBrokerId</em> and removed the <em class="title-reference">mqttBrokerId</em> entry from the update\-comparison logic\.
* networks\_sm\_bypass\_activation\_lock\_attempts \- Fixed the internal <em class="title-reference">networkId</em>/<em class="title-reference">attemptId</em> key mapping and removed <em class="title-reference">attemptId</em> from the update\-comparison logic\.
* networks\_sm\_target\_groups \- Removed the <em class="title-reference">targetGroupId</em> entry from the update\-comparison logic\.
* networks\_sm\_user\_access\_devices\_delete \- Renamed <em class="title-reference">user\_access\_device\_id</em> to <em class="title-reference">userAccessDeviceId</em> in the request object\.
* networks\_switch\_access\_policies \- Removed the <em class="title-reference">accessPolicyNumber</em> entry from the update\-comparison logic\.
* networks\_switch\_dhcp\_server\_policy\_arp\_inspection\_trusted\_servers \- Removed the <em class="title-reference">trustedServerId</em> entry from the update\-comparison logic\.
* networks\_switch\_link\_aggregations \- Removed <em class="title-reference">linkAggregationId</em> from the update\-comparison logic since it is a path identifier\.
* networks\_switch\_port\_schedules \- Removed the <em class="title-reference">portScheduleId</em> entry from the update\-comparison logic\.
* networks\_switch\_qos\_rules\_order \- Removed the <em class="title-reference">qosRuleId</em> entry from the update\-comparison logic and deleted the line that force\-overwrote <em class="title-reference">current\_obj\[\"networkId\"\]</em> before comparison\.
* networks\_switch\_routing\_multicast\_rendezvous\_points \- Removed the <em class="title-reference">rendezvousPointId</em> entry from the update\-comparison logic\.
* networks\_switch\_stacks \- Fixed <em class="title-reference">update\(\)</em> so switch stack updates are now actually sent via updateNetworkSwitchStack instead of silently returning the unmodified previous object\, and corrected a lowercase <em class="title-reference">switchstackid</em> key typo in <em class="title-reference">delete\(\)</em>\.
* networks\_switch\_stacks\_add \- Renamed <em class="title-reference">switch\_stack\_id</em> to <em class="title-reference">switchStackId</em> in the request object\.
* networks\_switch\_stacks\_remove \- Renamed <em class="title-reference">switch\_stack\_id</em> to <em class="title-reference">switchStackId</em> in the request object\.
* networks\_switch\_stacks\_routing\_interfaces \- Removed <em class="title-reference">switchStackId</em> and <em class="title-reference">interfaceId</em> from the update\-comparison logic since they are path identifiers\, not body fields\.
* networks\_switch\_stacks\_routing\_interfaces\_dhcp \- Fixed the internal <em class="title-reference">switchStackId</em>/<em class="title-reference">interfaceId</em> key mapping and removed them from the update\-comparison logic\.
* networks\_switch\_stacks\_routing\_static\_routes \- Removed the <em class="title-reference">switchStackId</em> and <em class="title-reference">staticRouteId</em> entries from the update\-comparison logic\.
* networks\_traffic\_shaping\_application\_categories\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em>\.
* networks\_webhooks\_http\_servers \- Removed the <em class="title-reference">httpServerId</em> entry from the update\-comparison logic\.
* networks\_webhooks\_payload\_templates \- Fixed an invalid <em class="title-reference">headers</em> argument type declaration \(<em class="title-reference">\"\[\'array\'\, \'null\'\]\"</em> corrected to <em class="title-reference">list</em>\) and removed the <em class="title-reference">payloadTemplateId</em> entry from the update\-comparison logic\.
* networks\_wireless\_air\_marshal\_rules \- Renamed <em class="title-reference">rule\_id</em> to <em class="title-reference">ruleId</em> and removed the <em class="title-reference">ruleId</em> entry from the update\-comparison logic\.
* networks\_wireless\_bluetooth\_settings \- Fixed a malformed UUID in the module\'s EXAMPLES block\.
* networks\_wireless\_ethernet\_ports\_profiles \- Fixed the internal <em class="title-reference">networkId</em>/<em class="title-reference">profileId</em> key mapping and removed <em class="title-reference">profileId</em> from the update\-comparison logic\.
* networks\_wireless\_location\_scanning \- Renamed <em class="title-reference">network\_id</em> to <em class="title-reference">networkId</em> in the request object\.
* networks\_wireless\_rf\_profiles \- Removed the <em class="title-reference">rfProfileId</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids \- Corrected \"RADSEC\" casing to \"RadSec\" throughout the RADIUS accounting/authentication and RadSec tunnel documentation\.
* networks\_wireless\_ssids\_bonjour\_forwarding \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_device\_type\_group\_policies \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_eap\_override \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_firewall\_l3\_firewall\_rules \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_firewall\_l7\_firewall\_rules \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_hotspot20 \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_identity\_psks \- Removed the <em class="title-reference">number</em> and <em class="title-reference">identityPskId</em> entries from the update\-comparison logic\.
* networks\_wireless\_ssids\_schedules \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_traffic\_shaping\_rules \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* networks\_wireless\_ssids\_vpn \- Removed the <em class="title-reference">number</em> entry from the update\-comparison logic\.
* organizations \- Removed <em class="title-reference">organizationId</em> from the update\-comparison logic since it is a path identifier\.
* organizations\_action\_batches \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">actionBatchId</em> entries from the update\-comparison logic\.
* organizations\_adaptive\_policy\_acls \- Removed the <em class="title-reference">aclId</em> entry from the update\-comparison logic\.
* organizations\_adaptive\_policy\_groups \- Removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* organizations\_adaptive\_policy\_policies \- Removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* organizations\_admins \- Removed the <em class="title-reference">adminId</em> entry from the update\-comparison logic\.
* organizations\_alerts\_profiles \- Fixed the internal <em class="title-reference">organizationId</em>/<em class="title-reference">alertConfigId</em> key mapping and removed them from the update\-comparison logic\.
* organizations\_appliance\_dns\_local\_profiles \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">profileId</em> entries from the update\-comparison logic\.
* organizations\_appliance\_dns\_local\_records \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">recordId</em> entries from the update\-comparison logic\.
* organizations\_appliance\_dns\_split\_profiles \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">profileId</em> entries from the update\-comparison logic\.
* organizations\_appliance\_security\_intrusion \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_appliance\_vpn\_site\_to\_site\_ipsec\_peers\_slas \- Renamed <em class="title-reference">organization\_id</em> to <em class="title-reference">organizationId</em> and removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_appliance\_vpn\_third\_party\_vpn\_peers \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_appliance\_vpn\_vpn\_firewall\_rules \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_branding\_policies \- Removed the <em class="title-reference">brandingPolicyId</em> entry from the update\-comparison logic\.
* organizations\_camera\_custom\_analytics\_artifacts \- Renamed <em class="title-reference">artifact\_id</em> to <em class="title-reference">artifactId</em> and removed the <em class="title-reference">artifactId</em> entry from the update\-comparison logic\.
* organizations\_cellular\_gateway\_esims\_inventory \- Renamed <em class="title-reference">organization\_id</em> to <em class="title-reference">organizationId</em> and removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* organizations\_cellular\_gateway\_esims\_service\_providers\_accounts \- Fixed a duplicate <em class="title-reference">accountId</em> keyword argument that caused a Python syntax error and prevented the plugin from loading\, and removed the redundant <em class="title-reference">id</em> entry from the update\-comparison logic\.
* organizations\_config\_templates\_switch\_profiles\_ports \- Fixed the internal <em class="title-reference">configTemplateId</em>/<em class="title-reference">profileId</em>/<em class="title-reference">portId</em> key mapping and removed <em class="title-reference">profileId</em>/<em class="title-reference">portId</em> from the update\-comparison logic\.
* organizations\_devices\_controller\_migrations \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_devices\_packet\_capture\_captures \- Fixed the internal <em class="title-reference">organizationId</em>/<em class="title-reference">captureId</em> key mapping and removed them from the update\-comparison logic\.
* organizations\_devices\_packet\_capture\_captures\_download\_url\_generate \- Renamed <em class="title-reference">capture\_id</em> to <em class="title-reference">captureId</em> in the request object\.
* organizations\_devices\_packet\_capture\_captures\_stop \- Renamed <em class="title-reference">capture\_id</em> to <em class="title-reference">captureId</em> in the request object\.
* organizations\_devices\_packet\_capture\_schedules \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">scheduleId</em> entries from the update\-comparison logic\.
* organizations\_early\_access\_features\_opt\_ins \- Removed the <em class="title-reference">optInId</em> entry from the update\-comparison logic\.
* organizations\_insight\_monitored\_media\_servers \- Removed <em class="title-reference">monitoredMediaServerId</em> from the update\-comparison logic since it is a path identifier\.
* organizations\_inventory\_onboarding\_cloud\_monitoring\_imports \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_licenses \- Fixed the internal <em class="title-reference">organizationId</em>/<em class="title-reference">licenseId</em> key mapping and removed them from the update\-comparison logic\.
* organizations\_networks\_moves \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_policies\_global\_firewall\_rulesets \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">rulesetId</em> entries from the update\-comparison logic\.
* organizations\_policies\_global\_firewall\_rulesets\_rules \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">ruleId</em> entries from the update\-comparison logic\.
* organizations\_policies\_global\_group\_policies \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">policyId</em> entries from the update\-comparison logic\.
* organizations\_policies\_global\_group\_policies\_firewall\_rulesets\_assignments \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">assignmentId</em> entries from the update\-comparison logic\.
* organizations\_policy\_objects \- Removed the <em class="title-reference">policyObjectId</em> entry from the update\-comparison logic\.
* organizations\_policy\_objects\_groups \- Removed the <em class="title-reference">policyObjectGroupId</em> entry from the update\-comparison logic\.
* organizations\_saml\_idps \- Removed the <em class="title-reference">idpId</em> entry from the update\-comparison logic\.
* organizations\_saml\_roles \- Removed the <em class="title-reference">samlRoleId</em> entry from the update\-comparison logic\.
* organizations\_sase\_sites \- Fixed a duplicate <em class="title-reference">siteId</em> keyword argument in the request object that caused a Python syntax error and prevented the plugin from loading\.
* organizations\_sm\_admins\_roles \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_splash\_assets \- Fixed the internal <em class="title-reference">organizationId</em> key mapping and removed the erroneous <em class="title-reference">id</em> comparison from the update\-comparison logic\.
* organizations\_splash\_themes \- Removed the <em class="title-reference">id</em> entry from the update\-comparison logic\.
* organizations\_splash\_themes\_assets \- Renamed <em class="title-reference">theme\_identifier</em> to <em class="title-reference">themeIdentifier</em> in the request object\.
* organizations\_switch\_ports\_by\_switch\_info \- Corrected the RETURN type from <em class="title-reference">dict</em> to <em class="title-reference">list</em> to accurately reflect that the API returns one entry per switch\.
* organizations\_webhooks\_logs\_info \- Corrected the documented maximum lookback/timespan window from 90/31 days to the actual 30\-day limit\.
* organizations\_wireless\_devices\_provisioning\_deployments \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">deploymentId</em> entries from the update\-comparison logic\.
* organizations\_wireless\_devices\_radsec\_certificates\_authorities \- Corrected \"RADSEC\" casing to \"RadSec\" in the module description\.
* organizations\_wireless\_devices\_radsec\_certificates\_authorities \- Removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_wireless\_location\_scanning\_receivers \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">receiverId</em> entries from the update\-comparison logic\.
* organizations\_wireless\_mqtt\_settings \- Renamed <em class="title-reference">organization\_id</em> to <em class="title-reference">organizationId</em> and removed the <em class="title-reference">organizationId</em> entry from the update\-comparison logic\.
* organizations\_wireless\_ssids\_firewall\_isolation\_allowlist\_entries \- Removed the <em class="title-reference">organizationId</em> and <em class="title-reference">entryId</em> entries from the update\-comparison logic\.
* organizations\_wireless\_zigbee\_devices \- Renamed <em class="title-reference">organization\_id</em> to <em class="title-reference">organizationId</em> and removed the <em class="title-reference">organizationId</em> and <em class="title-reference">id</em> entries from the update\-comparison logic\.
* organizations\_wireless\_zigbee\_disenrollments \- Fixed the internal <em class="title-reference">organizationId</em>/<em class="title-reference">disenrollmentId</em> key mapping and removed them from the update\-comparison logic\.
* organizations\_wireless\_zigbee\_door\_locks \- Fixed the internal <em class="title-reference">organizationId</em>/<em class="title-reference">doorLockId</em> key mapping and removed them from the update\-comparison logic\.

<a id="cisco-nxos-2"></a>
#### cisco\.nxos

* Fix nxos\_nxapi integration test assertions to use boolean conditions compatible with ansible\-core 2\.19\+\.
* Fix nxos\_static\_routes rtt integration test assert missing <em class="title-reference">in result\.commands</em> for ansible\-core 2\.19\+\.
* Fix nxos\_telemetry integration test asserts to use boolean Jinja expressions without template delimiters for ansible\-core 2\.19\+\.
* Fix nxos\_user auth integration test assert for results\.failed\.
* Fix nxos\_user basic integration test weak\-password warnings assertions to be conditional on warnings presence for ansible\-core 2\.21\+\.
* nxos\_bgp\_address\_family \- fix <code>\_flatten\_config</code> to correctly track VRF/neighbor/template context when flattening address\-family lines \(fixes ACA\-6752\, [https\://github\.com/ansible\-collections/cisco\.nxos/issues/1082](https\://github\.com/ansible\-collections/cisco\.nxos/issues/1082)\)\.
* nxos\_bgp\_global \- Generate <code>no bfd</code>\, <code>no bfd singlehop</code>\, and <code>no bfd multihop</code> when <code>bfd\.set</code>\, <code>bfd\.singlehop</code>\, or <code>bfd\.multihop\.set</code> is false for BGP neighbors \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/1073](https\://github\.com/ansible\-collections/cisco\.nxos/pull/1073)\)\.
* nxos\_bgp\_global \- Update nxos\_bgp\_global to add prefix to <em class="title-reference">template peer\*</em> sections as to avoid issues during facts gathering\. BGP related templates are handled in nxos\_bgp\_template module\.
* nxos\_facts \- fix KeyError when show interface text output has admin preamble before the first interface on multi\-module chassis \([https\://github\.com/ansible\-collections/cisco\.nxos/pull/1076](https\://github\.com/ansible\-collections/cisco\.nxos/pull/1076)\)\.
* nxos\_hsrp\_interfaces \- Update <code>preempt</code> and <code>priority</code> templates to render optional sub\-options independently\, enabling per\-key command generation\.
* nxos\_interfaces \- Send an explicit <code>switchport</code> \(or <code>no switchport</code>\) command when creating an interface that is absent from gathered facts\, instead of treating the platform <code>system default switchport</code> value as already applied\. This allows subsequent <code>nxos\_l2\_interfaces</code> tasks to succeed on newly created Layer 2 interfaces\.
* nxos\_l2\_interfaces \- Fix <code>state\=merged</code> to use SET instead of ADD when restricting trunk VLANs on interfaces with implicit default allowed VLANs \(1\-4094\)\. Previously\, merged was a no\-op on default trunks because ADD against the synthesized full range added nothing\. Adds <code>allowed\_vlans\_implicit</code> marker in facts to distinguish synthesized defaults from explicit configuration\. <code>replaced</code>/<code>overridden</code> semantics are unchanged \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/AAP\-85469](https\://github\.com/ansible\-collections/cisco\.nxos/issues/AAP\-85469)\)\.
* nxos\_l2\_interfaces \- Fix replaced and overridden states for trunk allowed VLANs to set the full desired VLAN list instead of incremental add/remove\.
* nxos\_l2\_interfaces \- Skip port\-channel member interfaces during facts gathering and command generation\. Member interfaces inherit L2 config from the port\-channel and cannot be configured directly\.
* nxos\_l3\_interfaces \- fix spacing in DHCP relay source\-interface commands so interface type and ID are concatenated without a space \(fixes ACA\-6753\, [https\://github\.com/ansible\-collections/cisco\.nxos/issues/1059](https\://github\.com/ansible\-collections/cisco\.nxos/issues/1059)\)\.
* nxos\_lag\_interfaces \- fix <code>\'NoneType\' object is not iterable</code> when using replaced state on a port\-channel with no members \([https\://github\.com/ansible\-collections/cisco\.nxos/issues/819](https\://github\.com/ansible\-collections/cisco\.nxos/issues/819)\)\.
* nxos\_snmp\_server \- Emit each community attribute as its own CLI command so NX\-API does not reject multi\-line community configuration\.
* nxos\_snmp\_server \- Emit only configured community attribute lines so empty <code>snmp\-server community</code> commands no longer reset access to read\-only\.
* nxos\_snmp\_server \- Fix community removal on replaced\, overridden\, and deleted states by adding a remval template so deletes emit a single <code>no snmp\-server community</code> command instead of re\-adding the community\.
* nxos\_snmp\_server \- Merge multi\-line SNMP community configuration into one object per community name so group and ACL attributes round\-trip correctly\.
* nxos\_snmp\_server \- Parse <code>ro</code> and <code>rw</code> community access flags from device configuration\.
* nxos\_snmp\_server \- Re\-enable network\_cli and NX\-API integration tests\, including the deleted state\.
* nxos\_snmp\_server \- Recreate a community \(delete then set\) when replaced or overridden changes attributes on an existing community name\, so <code>no snmp\-server community NAME</code> cannot wipe the just\-applied config\.
* nxos\_snmp\_server \- parse NX\-OS 10\.4\(4\)\+ <code>priv des</code> SNMPv3 user lines \(AAP\-89723\)\. DES remains the implicit default privacy type \(<code>aes\_128</code> false\)\. The module does not render <code>priv des</code> back to the device\.
* nxos\_snmp\_server \- stop deleting an SNMPv3 user when <code>state\: replaced</code> updates that user \(AAP\-90154\)\.

<a id="cloudscale-ch-cloud-1"></a>
#### cloudscale\_ch\.cloud

* cloudscale action group \- fix a typo \(<code>loaad\_balancer\_listener</code>\) that excluded the <code>load\_balancer\_listener</code> module from the <code>cloudscale\_ch\.cloud\.cloudscale</code> action group\, and add the missing <code>volume\_snapshot</code> module to the group\.

<a id="community-aws-1"></a>
#### community\.aws

* autoscaling\_policy \- allow float type for <code>step\_adjustments</code> <code>lower\_bound</code> and <code>upper\_bound</code> parameters \([https\://github\.com/ansible\-collections/community\.aws/issues/2355](https\://github\.com/ansible\-collections/community\.aws/issues/2355)\)
* wafv2\_web\_acl \- Fixed idempotency issue where rules with rate\_based\_statement would always show as changed when evaluation\_window\_sec was not explicitly specified due to AWS returning the default value of 300 \([https\://github\.com/ansible\-collections/community\.aws/pull/2427](https\://github\.com/ansible\-collections/community\.aws/pull/2427)\)\.

<a id="community-clickhouse-3"></a>
#### community\.clickhouse

* clickhouse\_quota \- add missing on cluster for drop
* clickhouse\_role \- fix cluster for drop role \([https\://github\.com/ansible\-collections/community\.clickhouse/pull/215](https\://github\.com/ansible\-collections/community\.clickhouse/pull/215)\)\.

<a id="community-crypto-2"></a>
#### community\.crypto

* gpg\_fingerprint lookup plugin\, gpg\_fingerprint filter plugin \- prevent GnuPG from unnecessarily starting gpg\-agent \([https\://github\.com/ansible\-collections/community\.crypto/issues/1026](https\://github\.com/ansible\-collections/community\.crypto/issues/1026)\, [https\://github\.com/ansible\-collections/community\.crypto/pull/1029](https\://github\.com/ansible\-collections/community\.crypto/pull/1029)\)\.
* openssh\_\* modules \- prevent use of currently unsupported MLDSA private keys in the cryptography backend \([https\://github\.com/ansible\-collections/community\.crypto/pull/1044](https\://github\.com/ansible\-collections/community\.crypto/pull/1044)\)\.
* openssl\_pkcs12 \- prevent use of MLDSA private keys\, which are not supported by PKCS\#12\, or at least cryptography\'s implementation \([https\://github\.com/ansible\-collections/community\.crypto/pull/1044](https\://github\.com/ansible\-collections/community\.crypto/pull/1044)\)\.

<a id="community-dns-1"></a>
#### community\.dns

* Update Public Suffix List\.
* various DNS modules \- if <code>zone\_id</code> was combined with an IDN <code>prefix</code>\, the prefix was not converted to punycode \([https\://github\.com/ansible\-collections/community\.dns/pull/340](https\://github\.com/ansible\-collections/community\.dns/pull/340)\)\.

<a id="community-docker-1"></a>
#### community\.docker

* Handle empty \'docker compose images\' stdout in case of errors \([https\://github\.com/ansible\-collections/community\.docker/pull/1305](https\://github\.com/ansible\-collections/community\.docker/pull/1305)\)\.
* docker\_api connection plugin \- the environment fallbacks for <code>docker\_host</code>\, <code>tls\_hostname</code>\, <code>api\_version</code>\, <code>timeout</code>\, <code>tls</code>\, and <code>validate\_certs</code> now finally work \([https\://github\.com/ansible\-collections/community\.docker/issues/1298](https\://github\.com/ansible\-collections/community\.docker/issues/1298)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1299](https\://github\.com/ansible\-collections/community\.docker/pull/1299)\)\.
* docker\_container\_exec module\, docker\_api connection plugin \- ensure that when a command is run in a container with stdin provided\, that the actual response is closed and not a socket derived from it\. The old behavior causes warnings to be shown on Python 3\.13\+ under certain conditions \([https\://github\.com/ansible\-collections/community\.docker/issues/1247](https\://github\.com/ansible\-collections/community\.docker/issues/1247)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1260](https\://github\.com/ansible\-collections/community\.docker/pull/1260)\)\.
* docker\_containers inventory plugin \- the environment fallbacks for <code>docker\_host</code>\, <code>tls\_hostname</code>\, <code>api\_version</code>\, <code>timeout</code>\, <code>tls</code>\, and <code>validate\_certs</code> now finally work \([https\://github\.com/ansible\-collections/community\.docker/issues/1298](https\://github\.com/ansible\-collections/community\.docker/issues/1298)\, [https\://github\.com/ansible\-collections/community\.docker/pull/1299](https\://github\.com/ansible\-collections/community\.docker/pull/1299)\)\.
* docker\_image\, docker\_image\_pull\, docker\_container \- also handle errors if only <code>errorDetail</code> is set\, but not <code>error</code>\. The <code>error</code> field has been [deprecated in Moby apparently a very long time ago](https\://github\.com/moby/moby/commit/3043c2641990d94298c6377b7ef14709263a4709) \([https\://github\.com/ansible\-collections/community\.docker/pull/1302](https\://github\.com/ansible\-collections/community\.docker/pull/1302)\)\.

<a id="community-general-2"></a>
#### community\.general

* aix\_devices \- fix <code>chdev</code> command failures being incorrectly reported as successful results\, now properly fails the task when device attribute changes cannot be applied \([https\://github\.com/ansible\-collections/community\.general/pull/12185](https\://github\.com/ansible\-collections/community\.general/pull/12185)\)\.
* apache2\_module \- fix false failures when <code>ignore\_configcheck</code> is set and the configuration is broken for a reason unrelated to the module being changed \([https\://github\.com/ansible\-collections/community\.general/issues/4592](https\://github\.com/ansible\-collections/community\.general/issues/4592)\, [https\://github\.com/ansible\-collections/community\.general/pull/12597](https\://github\.com/ansible\-collections/community\.general/pull/12597)\)\.
* apk \- the <code>upgrade</code> operation no longer reports <code>changed\=true</code> when nothing was upgraded but an apk commit hook \(for example <code>mrtest</code>\, or anything installed in <code>/etc/apk/commit\_hooks\.d/</code>\) printed output before the trailing <code>OK\:</code> summary line\; the change status is now derived from the packages apk actually reports upgrading \([https\://github\.com/ansible\-collections/community\.general/issues/12223](https\://github\.com/ansible\-collections/community\.general/issues/12223)\, [https\://github\.com/ansible\-collections/community\.general/pull/12376](https\://github\.com/ansible\-collections/community\.general/pull/12376)\)\.
* composer \- restore compatibility with older compose versions when using <code>working\_dir</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12293](https\://github\.com/ansible\-collections/community\.general/issues/12293)\, [https\://github\.com/ansible\-collections/community\.general/pull/12339](https\://github\.com/ansible\-collections/community\.general/pull/12339)\)\.
* composer \- the <code>\-\-working\-dir</code> option is now always placed first on the command line\, before the subcommand\, to ensure consistent behavior across all composer commands \([https\://github\.com/ansible\-collections/community\.general/issues/5204](https\://github\.com/ansible\-collections/community\.general/issues/5204)\, [https\://github\.com/ansible\-collections/community\.general/pull/12084](https\://github\.com/ansible\-collections/community\.general/pull/12084)\)\.
* composer \- use file checksum to determine <code>changed</code> status when <code>command\=config</code>\, instead of relying on the command return output\. The module now compares SHA256 checksums of relevant configuration files \(<code>composer\.json</code>\, <code>auth\.json</code>\, or their global equivalents\) before and after running the command \([https\://github\.com/ansible\-collections/community\.general/pull/12084](https\://github\.com/ansible\-collections/community\.general/pull/12084)\)\.
* counter\_enabled callback \- fix missing output for looped tasks\, including tasks using <code>delegate\_to</code> \([https\://github\.com/ansible\-collections/community\.general/issues/8187](https\://github\.com/ansible\-collections/community\.general/issues/8187)\, [https\://github\.com/ansible\-collections/community\.general/pull/12067](https\://github\.com/ansible\-collections/community\.general/pull/12067)\)\.
* dnf\_config\_manager \- fix incompatibility with DNF5\. The module was crashing on systems with DNF5 due to CLI changes since DNF4 \([https\://github\.com/ansible\-collections/community\.general/issues/9127](https\://github\.com/ansible\-collections/community\.general/issues/9127)\, [https\://github\.com/ansible\-collections/community\.general/pull/12206](https\://github\.com/ansible\-collections/community\.general/pull/12206)\)\.
* filesystem \- handle BusyBox <code>blkid</code> output to correctly detect existing filesystems on systems like Alpine Linux \([https\://github\.com/ansible\-collections/community\.general/issues/7283](https\://github\.com/ansible\-collections/community\.general/issues/7283)\, [https\://github\.com/ansible\-collections/community\.general/pull/12235](https\://github\.com/ansible\-collections/community\.general/pull/12235)\)\.
* filesystem \- the module now also handles the output format of bcachefs\-tools v1\.38\.4 and above \([https\://github\.com/ansible\-collections/community\.general/issues/12259](https\://github\.com/ansible\-collections/community\.general/issues/12259)\, [https\://github\.com/ansible\-collections/community\.general/pull/12291](https\://github\.com/ansible\-collections/community\.general/pull/12291)\)\.
* filetree lookup plugin \- raise <code>AnsibleLookupError</code> when the <code>exclude</code> option contains an invalid regular expression instead of an uncaught <code>re\.error</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12140](https\://github\.com/ansible\-collections/community\.general/pull/12140)\)\.
* haproxy \- fix <code>state\=disabled</code> with <code>drain\=true</code> timing out instead of putting a server that is already down into maintenance mode \([https\://github\.com/ansible\-collections/community\.general/issues/9020](https\://github\.com/ansible\-collections/community\.general/issues/9020)\, [https\://github\.com/ansible\-collections/community\.general/pull/12640](https\://github\.com/ansible\-collections/community\.general/pull/12640)\)\.
* homebrew\_cask \- fix <code>brew \-\-version</code> parsing to handle version strings with more than three dot\-separated segments \(for example\, some vendor Homebrew builds report a fourth segment\)\. The previous regex could silently drop the leading segment\, misjudging whether the deprecated <code>brew cask</code> command syntax is still required and causing installs to fail with an unknown\-command error \([https\://github\.com/ansible\-collections/community\.general/pull/12559](https\://github\.com/ansible\-collections/community\.general/pull/12559)\)\.
* htpasswd \- fix <code>hash\_scheme</code> aliases and Apache\-compatible <code>bcrypt</code> hashes \([https\://github\.com/ansible\-collections/community\.general/issues/6135](https\://github\.com/ansible\-collections/community\.general/issues/6135)\, [https\://github\.com/ansible\-collections/community\.general/pull/12123](https\://github\.com/ansible\-collections/community\.general/pull/12123)\)\.
* icinga2\_host \- fix <code>JSONDecodeError</code> raised when the Icinga2 API returns an HTTP error response \([https\://github\.com/ansible\-collections/community\.general/pull/12687](https\://github\.com/ansible\-collections/community\.general/pull/12687)\, [https\://github\.com/ansible\-collections/community\.general/issues/4948](https\://github\.com/ansible\-collections/community\.general/issues/4948)\)\.
* incus connection plugin \- detect failed <code>incus file push</code>/<code>incus file pull</code> transfers and raise a clear error naming the instance and the CLI stderr\, instead of silently reporting success and failing later with a misleading <code>chmod\: No such file or directory</code> error \([https\://github\.com/ansible\-collections/community\.general/pull/12464](https\://github\.com/ansible\-collections/community\.general/pull/12464)\)\.
* incus connection plugin \- improve Windows PowerShell argv handling by stripping wrapper quotes from payload arguments for <code>\-enc</code>\, <code>\-encodedcommand</code>\, <code>\-command</code>\, <code>\-c</code>\, <code>\-file</code> and <code>\-f</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12161](https\://github\.com/ansible\-collections/community\.general/issues/12161)\, [https\://github\.com/ansible\-collections/community\.general/pull/12158](https\://github\.com/ansible\-collections/community\.general/pull/12158)\)\.
* incus connection plugin \- return <code>stdout</code>/<code>stderr</code> as bytes instead of strings to restore compatibility with ansible\-core 2\.21 module execution \([https\://github\.com/ansible\-collections/community\.general/issues/12161](https\://github\.com/ansible\-collections/community\.general/issues/12161)\, [https\://github\.com/ansible\-collections/community\.general/pull/12158](https\://github\.com/ansible\-collections/community\.general/pull/12158)\)\.
* influxdb\_retention\_policy \- fix <code>TypeError</code> when altering a retention policy without <code>shard\_group\_duration</code> set \([https\://github\.com/ansible\-collections/community\.general/issues/3897](https\://github\.com/ansible\-collections/community\.general/issues/3897)\, [https\://github\.com/ansible\-collections/community\.general/pull/12652](https\://github\.com/ansible\-collections/community\.general/pull/12652)\)\.
* ini\_file \- do not delete comment\-only lines that contain the option name \([https\://github\.com/ansible\-collections/community\.general/issues/11919](https\://github\.com/ansible\-collections/community\.general/issues/11919)\, [https\://github\.com/ansible\-collections/community\.general/pull/12083](https\://github\.com/ansible\-collections/community\.general/pull/12083)\)\.
* jabber \- do not send an unnecessary <code>muc\#user</code> tag on groupchat messages \([https\://github\.com/ansible\-collections/community\.general/pull/12658](https\://github\.com/ansible\-collections/community\.general/pull/12658)\, [https\://github\.com/ansible\-collections/community\.general/issues/5343](https\://github\.com/ansible\-collections/community\.general/issues/5343)\)\.
* java\_cert \- detect silent <code>keytool</code> failures by verifying the import outcome after the command exits with <code>rc\=0</code> \([https\://github\.com/ansible\-collections/community\.general/issues/6685](https\://github\.com/ansible\-collections/community\.general/issues/6685)\, [https\://github\.com/ansible\-collections/community\.general/pull/12238](https\://github\.com/ansible\-collections/community\.general/pull/12238)\)\.
* java\_cert \- fix <code>NullPointerException</code> when importing from a PKCS12 file with a password on Java 8 \([https\://github\.com/ansible\-collections/community\.general/issues/3023](https\://github\.com/ansible\-collections/community\.general/issues/3023)\, [https\://github\.com/ansible\-collections/community\.general/pull/12151](https\://github\.com/ansible\-collections/community\.general/pull/12151)\)\.
* jenkins\_job\_info \- fix <code>KeyError\: \'color\'</code> when filtering folder jobs by color \([https\://github\.com/ansible\-collections/community\.general/issues/12232](https\://github\.com/ansible\-collections/community\.general/issues/12232)\)\, [https\://github\.com/ansible\-collections/community\.general/pull/12369](https\://github\.com/ansible\-collections/community\.general/pull/12369)\)\.
* keycloak\_user \- fix attributes always reporting <code>changed\=true</code> due to a type mismatch between the raw Keycloak representation and the module\'s list representation \([https\://github\.com/ansible\-collections/community\.general/pull/12642](https\://github\.com/ansible\-collections/community\.general/pull/12642)\)\.
* launchd \- fix <code>restarted</code> and <code>reloaded</code> states always reporting <code>changed\=False</code> \([https\://github\.com/ansible\-collections/community\.general/issues/6199](https\://github\.com/ansible\-collections/community\.general/issues/6199)\, [https\://github\.com/ansible\-collections/community\.general/pull/12122](https\://github\.com/ansible\-collections/community\.general/pull/12122)\)\.
* ldap\_attrs \- when the server raises <code>INAPPROPRIATE\_MATCHING</code> because an attribute has no EQUALITY matching rule \(for example\, certain <code>olcTLS\*</code> attributes on older OpenLDAP versions\)\, the module now falls back to Python\-side value comparison instead of crashing \([https\://github\.com/ansible\-collections/community\.general/issues/3559](https\://github\.com/ansible\-collections/community\.general/issues/3559)\, [https\://github\.com/ansible\-collections/community\.general/issues/12596](https\://github\.com/ansible\-collections/community\.general/issues/12596)\, [https\://github\.com/ansible\-collections/community\.general/pull/12628](https\://github\.com/ansible\-collections/community\.general/pull/12628)\)\.
* lxc\_container \- fix <code>create\_script</code> to accept a single tuple argument\, resolving a <code>TypeError</code> that silently prevented <code>container\_command</code> from being executed \([https\://github\.com/ansible\-collections/community\.general/issues/11360](https\://github\.com/ansible\-collections/community\.general/issues/11360)\, [https\://github\.com/ansible\-collections/community\.general/pull/12106](https\://github\.com/ansible\-collections/community\.general/pull/12106)\)\.
* lxd connection plugin \- detect failed <code>lxc file push</code>/<code>lxc file pull</code> transfers and raise a clear error naming the instance and the CLI stderr\, instead of silently reporting success and failing later with a misleading <code>chmod\: No such file or directory</code> error \([https\://github\.com/ansible\-collections/community\.general/pull/12464](https\://github\.com/ansible\-collections/community\.general/pull/12464)\)\.
* nmcli \- add <code>bond\_mode\_behavior</code> to control whether omitted <code>mode</code> preserves the existing bond mode or uses the legacy <code>balance\-rr</code> default on existing connections \([https\://github\.com/ansible\-collections/community\.general/issues/9201](https\://github\.com/ansible\-collections/community\.general/issues/9201)\, [https\://github\.com/ansible\-collections/community\.general/pull/12114](https\://github\.com/ansible\-collections/community\.general/pull/12114)\)\.
* nmcli \- now handles connection names derived from MAC addresses\, and generally names that contain <code>\:</code> or <code>\\\\</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12386](https\://github\.com/ansible\-collections/community\.general/issues/12386)\, [https\://github\.com/ansible\-collections/community\.general/pull/12387](https\://github\.com/ansible\-collections/community\.general/pull/12387)\)\.
* npm \- fix <code>JSONDecodeError</code> when npm\'s stdout output contains warnings or notices alongside the JSON payload \([https\://github\.com/ansible\-collections/community\.general/pull/12665](https\://github\.com/ansible\-collections/community\.general/pull/12665)\, [https\://github\.com/ansible\-collections/community\.general/issues/4960](https\://github\.com/ansible\-collections/community\.general/issues/4960)\)\.
* onepassword lookup plugin \- the <code>op\://</code> secret reference lookup returned raw bytes instead of a string\, which broke passing the value into other modules \([https\://github\.com/ansible\-collections/community\.general/pull/11958](https\://github\.com/ansible\-collections/community\.general/pull/11958)\)\.
* opennebula inventory plugin \- coerce <code>SSH\_PORT</code> to an integer before setting <code>ansible\_port</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12437](https\://github\.com/ansible\-collections/community\.general/pull/12437)\)\.
* opennebula inventory plugin \- fix crash when retrieving VM without NIC \([https\://github\.com/ansible\-collections/community\.general/pull/12361](https\://github\.com/ansible\-collections/community\.general/pull/12361)\)\.
* opkg \- correctly set executable search path \([https\://github\.com/ansible\-collections/community\.general/pull/12182](https\://github\.com/ansible\-collections/community\.general/pull/12182)\)\.
* pacemaker\_cluster \- skip <code>pcs cluster start</code> in <code>state\=online</code> when the cluster is already running\, improving idempotency and allowing maintenance mode to be disabled without pcsd connectivity \([https\://github\.com/ansible\-collections/community\.general/issues/12362](https\://github\.com/ansible\-collections/community\.general/issues/12362)\, [https\://github\.com/ansible\-collections/community\.general/pull/12403](https\://github\.com/ansible\-collections/community\.general/pull/12403)\)\.
* pacemaker\_resource \- fix bug where the resource\-ready state check did not recognize all valid ready states\, causing the module to time out on resources that never reach the <code>Started</code> state \([https\://github\.com/ansible\-collections/community\.general/issues/12351](https\://github\.com/ansible\-collections/community\.general/issues/12351)\, [https\://github\.com/ansible\-collections/community\.general/pull/12355](https\://github\.com/ansible\-collections/community\.general/pull/12355)\)\.
* pamd \- handle non\-PAM lines such as authselect template directives without crashing \([https\://github\.com/ansible\-collections/community\.general/issues/5850](https\://github\.com/ansible\-collections/community\.general/issues/5850)\, [https\://github\.com/ansible\-collections/community\.general/pull/12137](https\://github\.com/ansible\-collections/community\.general/pull/12137)\)\.
* parted \- ignore MBR partition type codes \(for example <code>type\=8e</code>\) reported as flags by some parted builds \(for example on SUSE\)\, which cannot be managed via the <code>set</code> command \([https\://github\.com/ansible\-collections/community\.general/issues/6292](https\://github\.com/ansible\-collections/community\.general/issues/6292)\, [https\://github\.com/ansible\-collections/community\.general/pull/12121](https\://github\.com/ansible\-collections/community\.general/pull/12121)\)\.
* pkgng \- fix failure to install packages when the package repository has never been updated \([https\://github\.com/ansible\-collections/community\.general/pull/12507](https\://github\.com/ansible\-collections/community\.general/pull/12507)\)\.
* portage \- fix <code>depclean\: true</code> crashing with <code>AnsibleModule\.fail\_json\(\) missing 1 required positional argument\: \'msg\'</code> instead of reporting the actual emerge failure \([https\://github\.com/ansible\-collections/community\.general/pull/12168](https\://github\.com/ansible\-collections/community\.general/pull/12168)\)\.
* redfish\_command \- add workaround in <code>VirtualMediaInsert</code> for Supermicro systems to treat slots marked as <code>NotConnected</code> as empty \([https\://github\.com/ansible\-collections/community\.general/issues/6969](https\://github\.com/ansible\-collections/community\.general/issues/6969)\, [https\://github\.com/ansible\-collections/community\.general/pull/12537](https\://github\.com/ansible\-collections/community\.general/pull/12537)\)\.
* redfish\_config \- fix <code>KeyError\: \'ret\'</code> when <code>SetManagerNic</code> cannot find a matching NIC \([https\://github\.com/ansible\-collections/community\.general/issues/5892](https\://github\.com/ansible\-collections/community\.general/issues/5892)\, [https\://github\.com/ansible\-collections/community\.general/pull/12124](https\://github\.com/ansible\-collections/community\.general/pull/12124)\)\.
* sefcontext \- fix idempotence of <code>\<\<none\>\></code> file contexts \([https\://github\.com/ansible\-collections/community\.general/pull/12561](https\://github\.com/ansible\-collections/community\.general/pull/12561)\)
* snap \- fix <code>IndexError</code> when a single snap does not exist \([https\://github\.com/ansible\-collections/community\.general/issues/12375](https\://github\.com/ansible\-collections/community\.general/issues/12375)\, [https\://github\.com/ansible\-collections/community\.general/pull/12570](https\://github\.com/ansible\-collections/community\.general/pull/12570)\)\.
* supervisorctl \- treat the <code>BACKOFF</code> process state as active so that <code>state\=started</code> does not fail on a program still being retried by <code>supervisord</code> \([https\://github\.com/ansible\-collections/community\.general/issues/5599](https\://github\.com/ansible\-collections/community\.general/issues/5599)\, [https\://github\.com/ansible\-collections/community\.general/pull/12688](https\://github\.com/ansible\-collections/community\.general/pull/12688)\)\.
* terraform \- fix return value <code>command</code>\, showing terraform plan name twice \([https\://github\.com/ansible\-collections/community\.general/issues/12530](https\://github\.com/ansible\-collections/community\.general/issues/12530)\, [https\://github\.com/ansible\-collections/community\.general/pull/12540](https\://github\.com/ansible\-collections/community\.general/pull/12540)\)\.
* timezone \- no longer requires the <code>hwclock</code> executable for name\-only changes on non\-systemd systems \([https\://github\.com/ansible\-collections/community\.general/issues/12516](https\://github\.com/ansible\-collections/community\.general/issues/12516)\, [https\://github\.com/ansible\-collections/community\.general/pull/12526](https\://github\.com/ansible\-collections/community\.general/pull/12526)\)\.
* udm\_dns\_record \- normalize IPv6 addresses in <code>data</code> to expanded form to fix idempotency \([https\://github\.com/ansible\-collections/community\.general/issues/317](https\://github\.com/ansible\-collections/community\.general/issues/317)\, [https\://github\.com/ansible\-collections/community\.general/pull/12149](https\://github\.com/ansible\-collections/community\.general/pull/12149)\)\.
* ufw \- do not reload the default policy when it is already set to the requested value \([https\://github\.com/ansible\-collections/community\.general/issues/1843](https\://github\.com/ansible\-collections/community\.general/issues/1843)\, [https\://github\.com/ansible\-collections/community\.general/pull/12590](https\://github\.com/ansible\-collections/community\.general/pull/12590)\)\.
* ufw \- fix IPv6 rule determination and <code>insert\_relative\_to</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12531](https\://github\.com/ansible\-collections/community\.general/pull/12531)\)\.
* unixy callback \- handle missing <code>ansible\_host</code> in delegated vars when a task is delegated to a host without it set\, such as <code>localhost</code> \([https\://github\.com/ansible\-collections/community\.general/issues/12112](https\://github\.com/ansible\-collections/community\.general/issues/12112)\, [https\://github\.com/ansible\-collections/community\.general/pull/12113](https\://github\.com/ansible\-collections/community\.general/pull/12113)\)\.
* xenserver\_guest\_info \- use fallback chain for determining VDI format from <code>sm\_config</code> keys <code>image\-format</code>\, <code>vdi\_type</code>\, <code>type</code>\, defaulting to <code>raw</code> \([https\://github\.com/ansible\-collections/community\.general/pull/12119](https\://github\.com/ansible\-collections/community\.general/pull/12119)\, [https\://github\.com/ansible\-collections/community\.general/pull/12215](https\://github\.com/ansible\-collections/community\.general/pull/12215)\)\.
* xml \- preserve DOCTYPE declaration when writing modified XML files \([https\://github\.com/ansible\-collections/community\.general/issues/2762](https\://github\.com/ansible\-collections/community\.general/issues/2762)\, [https\://github\.com/ansible\-collections/community\.general/pull/12148](https\://github\.com/ansible\-collections/community\.general/pull/12148)\)\.
* zypper \- fix version specifier parsing when the version contains non\-numeric characters\, which caused packages to not be removed or installed \([https\://github\.com/ansible\-collections/community\.general/pull/12588](https\://github\.com/ansible\-collections/community\.general/pull/12588)\, [https\://github\.com/ansible\-collections/community\.general/issues/6564](https\://github\.com/ansible\-collections/community\.general/issues/6564)\)\.
* zypper\_repository \- fix <code>enabled</code>\, <code>autorefresh</code>\, and <code>gpgcheck</code> module parameters being overridden by values read from a <code>\.repo</code> file \([https\://github\.com/ansible\-collections/community\.general/issues/8783](https\://github\.com/ansible\-collections/community\.general/issues/8783)\, [https\://github\.com/ansible\-collections/community\.general/pull/12022](https\://github\.com/ansible\-collections/community\.general/pull/12022)\)\.

<a id="community-libvirt-1"></a>
#### community\.libvirt

* inventory \- Added checks to prevent powered\-off hosts from being issued guest agent calls\.
* plugins \- replaced deprecated imports from <code>ansible\.module\_utils\.\_text</code> with <code>ansible\.module\_utils\.common\.text\.converters</code> to avoid ansible\-core deprecation warnings and prepare for removal of the private import path in ansible\-core 2\.24\.
* virt\_cloud\_instance \- added cloud\-config header when converting cloud\-init user\-data from dictionary form\.
* virt\_cloud\_instance \- check if instance exists and not running before calling <code>create\(\)</code>\.
* virt\_install \- added cloud\-config header when converting cloud\-init user\-data from dictionary form\.
* virt\_install \- remove incorrect <code>required\=True</code> from <code>install\.os</code> parameter to allow <code>install\.no\_install\=true</code> without specifying an OS\.

<a id="community-postgresql-4"></a>
#### community\.postgresql

* postgresql\_membership \- fix <code>state\=absent</code> and <code>state\=exact</code> not removing a membership on PostgreSQL 16 and later when another role had granted it\, and reporting a change on every run\. The deprecated <code>groups</code> option now revokes every grant of the pair\, one <code>REVOKE</code> per granting role\, and fails naming the granting role when the connecting role lacks its privileges\, where it used to succeed without revoking anything \([https\://github\.com/ansible\-collections/community\.postgresql/issues/757](https\://github\.com/ansible\-collections/community\.postgresql/issues/757)\)\.
* postgresql\_membership \- fix a group named more than once being granted or revoked twice\.
* postgresql\_membership \- fix a group or role name containing a quote producing invalid SQL\.
* postgresql\_membership \- fix an empty <code>target\_roles</code> list failing with a SQL syntax error\; it is now a no\-op\.

<a id="community-sap-libs"></a>
#### community\.sap\_libs

* sapcar\_extract \- Update SAPCAR command from PATH and add explanation with HANA limitations \([https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/86](https\://github\.com/sap\-linuxlab/community\.sap\_libs/pull/86)\)

<a id="community-vmware-2"></a>
#### community\.vmware

* vmware\_guest\_network \- Fix an issue with trunked / PVLAN portgroups \([https\://github\.com/ansible\-collections/community\.vmware/issues/2567](https\://github\.com/ansible\-collections/community\.vmware/issues/2567)\)\.
* vmware\_guest\_network \- populate <code>vlan\_id</code> in gathered NIC data for Distributed Virtual Portgroup backings so check mode diff does not report a false change when the NIC is already on the requested network\.

<a id="community-windows-1"></a>
#### community\.windows

* community\.windows\.win\_psmodule \- Now retrieves module installation status of requested module instead of all modules\, which was expensive for hosts with many modules installed \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* community\.windows\.win\_psmodule\_info \- Fixed typo in documentation changing <code>procoessor\_architecture</code> to <code>processor\_architecture</code> \([https\://github\.com/ansible\-collections/community\.windows/pull/688](https\://github\.com/ansible\-collections/community\.windows/pull/688)\)\.
* laps\_password \- Migrate away from deprecated <code>to\_text</code> methods to the new public API\.
* psexec \- Migrate away from deprecated <code>to\_text</code> methods to the new public API\.
* win\_psrepository\_copy \- handle profiles with no ProfileImagePath \([https\://github\.com/ansible\-collections/community\.windows/issues/604](https\://github\.com/ansible\-collections/community\.windows/issues/604)\)\.
* win\_pssession\_configuration \- Fix compatibility with Ansible 2\.21\.
* win\_pssession\_configuration \- Fix type errors for parameters passed in New\-PSSessionConfigurationFile
* win\_regmerge \- Ensure <code>reg\.exe</code> uses the absolute location <code>C\:\\Windows\\Systme32\\reg\.exe</code>\. This ensures that misconfigured hosts won\'t use a different executable\.
* win\_scheduled\_task \- Fix issue when creating a new scheduled task when using <code>become\_user\: SYSTEM</code> \- [https\://github\.com/ansible\-collections/community\.windows/issues/633](https\://github\.com/ansible\-collections/community\.windows/issues/633)
* win\_unzip \- Use <code>\-LiteralPath</code> when calling PSCX <code>Expand\-Archive</code> so paths containing PowerShell wildcard characters \(e\.g\. <code>\[</code>\, <code>\]</code>\) are not glob\-expanded and silently resolved to an empty array\.
* win\_xml \- allow users to preserve whitespace while updating XML file \([https\://github\.com/ansible\-collections/community\.windows/issues/210](https\://github\.com/ansible\-collections/community\.windows/issues/210)\)\.
* win\_xml \- handle attribute removal correctly \([https\://github\.com/ansible\-collections/community\.windows/issues/631](https\://github\.com/ansible\-collections/community\.windows/issues/631)\)\.

<a id="containers-podman-1"></a>
#### containers\.podman

* podman\_image \- Fix build ignoring arch option

<a id="fortinet-fortios-1"></a>
#### fortinet\.fortios

* Fixed an issue to throw an user\-friendly error message when the users make the Connection protocol mismatch\. Github issue
* Fixed an issue where forwarder always returns diff when using check\_mode in the system\_dns\_database module even when no changes were made\. Github Issue
* Fixed the Github issue

<a id="graphiant-naas-2"></a>
#### graphiant\.naas

* <code>graphiant\_data\_exchange</code>\: fixed <code>accept\_invitation</code> raising <code>No VPN profiles found in acceptances</code> for a Graphiant customer that legitimately needs no Site\-to\-Site VPN \(issue \#154\)
* <code>graphiant\_ospfv2</code>\: BFD <code>multiplier</code> renamed to <code>localMultiplier</code> in <code>sample\_ospfv2\.yaml</code> and the interface payload to match the field name the API expects on write\; the device GET response still stays the same\; stopped sending the legacy flat fields when creating a new interface\.
* <code>graphiant\_ospfv2</code>\: ensure that the SDK model is used to build and validate the payload\.

<a id="hetzner-hcloud-4"></a>
#### hetzner\.hcloud

* certificate \- Fail with a clear error message when trying to change the <code>certificate</code> or <code>private\_key</code> of an existing uploaded certificate\, instead of silently reporting no change\. The Hetzner Cloud API does not support updating these fields in place\.
* firewall \- Fix <code>state is present but all of the following are missing\: name</code> error being raised when the <code>id</code> is given\.
* load\_balancer\_service \- Fix <code>health\_check</code> optional fields \(<code>interval</code>\, <code>timeout</code>\, <code>retries</code>\) not explicitly set by the user being sent to the API as <code>null</code>\, causing the request to fail with <code>invalid input in field \'health\_check\'</code>\. Note that <code>health\_check\.protocol</code> and <code>health\_check\.port</code> are still required by the API whenever <code>health\_check</code> is set\.
* load\_balancer\_service \- Fix the module always reporting a change when the <code>http</code> or <code>health\_check</code> arguments were set\, even when the current configuration already matched the desired state\.
* volume \- Fix misleading <code>only one of server or location must be provided</code> error being raised when the <code>server</code> or <code>location</code> given does not exist\, instead of a clear error stating that the resource was not found\.

<a id="ibm-storage-virtualize-1"></a>
#### ibm\.storage\_virtualize

* ibm\_sv\_manage\_snapshot \- Improved pool probe for idempotency
* ibm\_sv\_manage\_system\_certificate \- Added a fix for invalid certificate export on specific builds\.
* ibm\_svc\_manage\_drive \- Improved SVC error messaging\.

<a id="infoblox-nios-modules-2"></a>
#### infoblox\.nios\_modules

* WapiLookup\.handle\_exception \- guard against a <code>ConnectionError</code> whose <code>\.response</code> is <code>None</code> \(e\.g\. host unreachable\)\, which previously raised <code>AttributeError</code> and masked the real connection error \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/321](https\://github\.com/infobloxopen/infoblox\-ansible/pull/321)\)\.
* WapiModule \- <code>state\=absent</code> is now idempotent when the NIOS object is already missing\; a <code>NotFound</code> response during delete is treated as <code>changed\=false</code> rather than a failure \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/337](https\://github\.com/infobloxopen/infoblox\-ansible/pull/337)\)\.
* WapiModule \- <code>vlans</code> on network objects are now normalized to retain only the <code>vlan</code> reference key before comparison\, removing NIOS\-added <code>id</code> and <code>name</code> fields that caused false diffs \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/321](https\://github\.com/infobloxopen/infoblox\-ansible/pull/321)\)\.
* WapiModule \- fix transform functions being skipped when a module parameter is <code>None</code>\; default values are now applied to the WAPI payload even when the corresponding parameter is not set \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/309](https\://github\.com/infobloxopen/infoblox\-ansible/pull/309)\)\.
* WapiModule\.handle\_exception \- guard against WAPI error responses that omit the <code>Error</code> key\, which previously raised <code>KeyError</code> and masked the real failure reason \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/321](https\://github\.com/infobloxopen/infoblox\-ansible/pull/321)\)\.
* api \- attach a <code>NullHandler</code> to the <code>infoblox\_client</code> logger to suppress spurious \"No handlers could be found\" warnings and library re\-auth log noise when the consuming application has not configured logging \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/346](https\://github\.com/infobloxopen/infoblox\-ansible/pull/346)\)\.
* api \- fix <code>TypeError</code> in <code>handle\_exception</code> when the WAPI error response is not a dict \(e\.g\. bad credentials returning raw bytes\)\; non\-dict responses now fall back to a clean error message \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/346](https\://github\.com/infobloxopen/infoblox\-ansible/pull/346)\)\.
* api \- fix <code>TypeError</code> when <code>module\.params\[\'provider\'\]</code> is <code>None</code> \(credentials supplied via environment variables\)\; the provider is now treated as an empty mapping to prevent <code>argument after \*\* must be a mapping</code> errors \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/328](https\://github\.com/infobloxopen/infoblox\-ansible/pull/328)\)\.
* api\.py \- fix deprecation warning when importing <code>to\_native</code> and <code>to\_text</code> by using the updated import path \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/316](https\://github\.com/infobloxopen/infoblox\-ansible/pull/316)\)\.
* nios\_\* modules \- <code>state\=absent</code> in check mode now correctly reports <code>changed\=true</code> when the target object exists and would be deleted \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/352](https\://github\.com/infobloxopen/infoblox\-ansible/pull/352)\)\.
* nios\_\* modules \- fix error reporting so that <code>result\.msg</code> contains the actual WAPI error reason\; modules now call <code>fail\_json</code> so operators see the real failure instead of a generic message \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/350](https\://github\.com/infobloxopen/infoblox\-ansible/pull/350)\)\.
* nios\_\* modules \- fix post\-fetch object retrieval on WAPI 2\.14\+ where create/update returns a <code>\{\_ref\, uuid\}</code> dict instead of a bare <code>\_ref</code> string \(NPA\-1964\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/345](https\://github\.com/infobloxopen/infoblox\-ansible/pull/345)\)\.
* nios\_\* modules \- update path no longer calls <code>update\_object</code> in check mode\; the existing ref is preserved instead \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/318](https\://github\.com/infobloxopen/infoblox\-ansible/pull/318)\)\.
* nios\_adminuser \- exclude write\-only <code>password</code> from the idempotency comparison\. NIOS never returns the password on read\, so including it caused every run to report <code>changed\=true</code> \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/321](https\://github\.com/infobloxopen/infoblox\-ansible/pull/321)\)\.
* nios\_dtc\_lbdn \- updating the <code>types</code> or <code>patterns</code> field is no longer silently ignored\. These scalar lists are now compared by membership so adds\, removals\, and changes are correctly detected \(NPA\-1982\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/357](https\://github\.com/infobloxopen/infoblox\-ansible/pull/357)\)\.
* nios\_dtc\_monitor\_http \- fix idempotency when the <code>request</code> field is set\. NIOS auto\-appends <code>Connection\: close</code> to the stored value\; both sides are now normalized before comparison \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/348](https\://github\.com/infobloxopen/infoblox\-ansible/pull/348)\)\.
* nios\_dtc\_server \- the idempotency lookup now matches by <code>name</code> only\. Previously using <code>name</code> and <code>host</code> together caused a <code>host</code> change to miss the existing server and attempt a duplicate create \(NPA\-1840\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/344](https\://github\.com/infobloxopen/infoblox\-ansible/pull/344)\)\.
* nios\_dtc\_topology \- fix idempotency so re\-applying an unchanged topology reports <code>changed\=false</code>\. NIOS returns destination links as expanded objects\; these are now flattened to bare references before comparison \(NPA\-1840\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/344](https\://github\.com/infobloxopen/infoblox\-ansible/pull/344)\)\.
* nios\_dtc\_topology \- reordering rules is now detected as a change\. Rule order sets the priority sequence\; the previous subset\-only check missed pure reorders \(NPA\-1993\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/356](https\://github\.com/infobloxopen/infoblox\-ansible/pull/356)\)\.
* nios\_fixed\_address \- fail with an actionable error when a MAC\-only or DUID\-only fallback lookup matches more than one fixed address\, asking the user to supply <code>ipv4addr</code>/<code>ipv6addr</code> to uniquely identify the target \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/338](https\://github\.com/infobloxopen/infoblox\-ansible/pull/338)\)\.
* nios\_fixed\_address \- fix <code>state\=absent</code> silently no\-op\'ing when the delete call returns <code>NotFound</code> \(object already gone\)\; the deletion is now treated as idempotent success \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/337](https\://github\.com/infobloxopen/infoblox\-ansible/pull/337)\)\.
* nios\_fixed\_address \- fix idempotency when <code>options\: \[\]</code> is explicitly provided\; an empty list no longer triggers a spurious update when the record already has no DHCP options \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/353](https\://github\.com/infobloxopen/infoblox\-ansible/pull/353)\)\.
* nios\_fixed\_address \- look up existing records using <code>mac</code> together with <code>ipv4addr</code> \(and <code>duid</code> with <code>ipv6addr</code>\) so that <code>state\=absent</code> and updates target the correct record instead of matching by MAC/DUID alone \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/338](https\://github\.com/infobloxopen/infoblox\-ansible/pull/338)\)\.
* nios\_fixed\_address \- preserve <code>options</code> semantics\: return <code>None</code> when the parameter is not provided \(so existing DHCP options are not unintentionally cleared\) and <code>\[\]</code> only when it is explicitly set to an empty list \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/338](https\://github\.com/infobloxopen/infoblox\-ansible/pull/338)\)\.
* nios\_host\_record \- <code>use\_dns\_ea\_inheritance</code> is now gated on the WAPI version\. The field was introduced in WAPI 2\.12\.3/2\.13\.4\; sending it to an earlier WAPI is now suppressed with a warning \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/321](https\://github\.com/infobloxopen/infoblox\-ansible/pull/321)\)\.
* nios\_host\_record \- fix <code>aliases</code> always being reported as <code>changed</code> on idempotent re\-runs\. Aliases are now normalized before comparison \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/329](https\://github\.com/infobloxopen/infoblox\-ansible/pull/329)\)\.
* nios\_host\_record \- fix <code>ipv4addr</code> configured with <code>func\: nios\_next\_ip</code> always being reported as <code>changed</code> on re\-runs\. The next\-available\-IP token is now skipped during comparison \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/329](https\://github\.com/infobloxopen/infoblox\-ansible/pull/329)\)\.
* nios\_host\_record \- fix <code>state\=absent</code> silently no\-op\'ing on IPAM\-only host records \(<code>configure\_for\_dns\=false</code>\)\, which NIOS stores with <code>view\=\" \"</code> rather than <code>view\=\"default\"</code> \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/317](https\://github\.com/infobloxopen/infoblox\-ansible/pull/317)\)\.
* nios\_host\_record \- fix several idempotency and update bugs\: the matching record is now selected by IP when multiple records share the same name\, <code>use\_for\_ea\_inheritance</code> no longer causes spurious changes\, and add/remove IP operations are now idempotent \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/329](https\://github\.com/infobloxopen/infoblox\-ansible/pull/329)\)\.
* nios\_inventory \- surface a meaningful error when the Infoblox Grid cannot be queried \(wrong credentials\, unreachable host\, timeout\)\. Previously the plugin failed with the confusing \"\'Connector\' object has no attribute \'handle\_exception\'\" message \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/340](https\://github\.com/infobloxopen/infoblox\-ansible/pull/340)\)\.
* nios\_network \- fix <code>state\=absent</code> when <code>network\_view</code> is not specified\; the module now falls back to a CIDR\-only lookup so the resource can be deleted without requiring <code>network\_view</code> \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/335](https\://github\.com/infobloxopen/infoblox\-ansible/pull/335)\)\.
* nios\_network\, nios\_range \- fix multiple issues with structural DHCP options \(<code>routers</code>/num\=3\, <code>ntp\-servers</code>/num\=42\, <code>subnet\-mask</code>/num\=1\)\: <code>use\_option</code> is stripped for all structural option numbers and names\; <code>vendor\_class</code> is stripped for name\-based options to avoid \"Option DHCP\.routers is undefined\" WAPI errors \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/325](https\://github\.com/infobloxopen/infoblox\-ansible/pull/325)\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/333](https\://github\.com/infobloxopen/infoblox\-ansible/pull/333)\)\.
* nios\_next\_network lookup \- accept <code>cidr</code> as either an integer or a numeric string and reject <code>bool</code> and <code>float</code> values that previously passed through silently \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/315](https\://github\.com/infobloxopen/infoblox\-ansible/pull/315)\)\.
* nios\_nsgroup \- fix <code>AttributeError</code> crash when <code>extattrs</code> is supplied\. The argument is now declared as <code>type\=dict</code> \(NPA\-1975\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/349](https\://github\.com/infobloxopen/infoblox\-ansible/pull/349)\)\.
* nios\_nsgroup \- fix idempotency when a TSIG key is configured on nameservers\. <code>tsig\_key</code> is write\-only and <code>tsig\_key\_name</code> is stored as the <code>use\_tsig\_key\_name</code> flag\; TSIG fields are now canonicalized before comparison \(NPA\-1976\, [https\://github\.com/infobloxopen/infoblox\-ansible/pull/349](https\://github\.com/infobloxopen/infoblox\-ansible/pull/349)\)\.
* nios\_nsgroup \- fix removal of an entry from a list field \(<code>external\_primaries</code>\, <code>external\_secondaries</code>\, <code>grid\_primary</code>\, <code>grid\_secondaries</code>\) not being detected \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/339](https\://github\.com/infobloxopen/infoblox\-ansible/pull/339)\)\.
* nios\_nsgroup \- make <code>tsig\_key\_name</code> optional for external and preferred\-primaries nameservers\; TSIG is optional on NIOS but was incorrectly marked as required \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/339](https\://github\.com/infobloxopen/infoblox\-ansible/pull/339)\)\.
* nios\_range \- accept <code>/32</code> \(IPv4\) and <code>/128</code> \(IPv6\) CIDR boundary prefix lengths\, which were previously rejected by the validation logic \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/314](https\://github\.com/infobloxopen/infoblox\-ansible/pull/314)\)\.
* nios\_txt\_record \- fix <code>old\_text</code> lookup failing silently when <code>name</code> is absent from the object filter\, causing a new record to be created instead of failing with a clear error message \([https\://github\.com/infobloxopen/infoblox\-ansible/pull/355](https\://github\.com/infobloxopen/infoblox\-ansible/pull/355)\)\.

<a id="kubernetes-core-2"></a>
#### kubernetes\.core

* Ansible Turbo mode \- ignore <code>ENABLE\_TURBO\_MODE</code> on ansible\-core 2\.19\.0 and later\, where the <code>cloud\.common</code> collection is not supported\, and fall back to the standard <code>AnsibleModule</code> instead of failing with <code>byte indices must be integers or slices\, not str</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1242](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1242)\)\.
* ee \- added <code>meta/execution\-environment\.yml</code> to decouple ansible\-builder EE builds from the <code>openshift\-clients</code> system dependency declared in <code>bindep\.txt</code>\, which is not available in standard UBI repositories and caused builds to fail with <code>No package matches \'openshift\-clients\'</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1141](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1141)\)\.
* helm \- do not pass the upgrade\-only <code>\-\-reuse\-values</code> and <code>\-\-reset\-then\-reuse\-values</code> flags to <code>helm install</code>\, which rejected them with <code>unknown flag</code> whenever <code>reuse\_values</code> or <code>reset\_then\_reuse\_values</code> was combined with <code>replace</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1230](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1230)\)\.
* helm \- fix the <code>reuse\_values</code> example\, which set only <code>reuse\_values\=true</code>\. <code>reset\_values</code> defaults to <code>true</code> and helm ignores <code>\-\-reuse\-values</code> whenever <code>\-\-reset\-values</code> is passed\, so following the example reset the release values instead of reusing them \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1230](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1230)\)\.
* helm \- skip Helm\'s OCI registry progress messages when parsing the output of <code>helm show chart</code>\. As of Helm 4\.2\.1 these are printed to stdout instead of stderr \([https\://github\.com/helm/helm/pull/32056](https\://github\.com/helm/helm/pull/32056)\)\, which made installing a chart from an OCI registry fail with a YAML scanner error when the chart version contained a <code>\+</code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1223](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1223)\)\.
* helm \- use <code>\-\-server\-side\=false \-\-force\-replace</code> instead of the deprecated/removed <code>\-\-force</code> flag when <code>force\=true</code> is used with Helm v4\, preserving the Helm v3 client\-side replacement behaviour and avoiding the server\-side apply conflict \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1164)\)\.
* helm \- use the <code>\-\-rollback\-on\-failure</code> flag instead of the deprecated/removed <code>\-\-atomic</code> flag when <code>atomic\=true</code> is used with Helm v4 \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1144](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1144)\)\.
* helm\_repository \- correct handling of repository URLs with trailing slashes \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1121](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1121)\)\.
* helm\_repository \- normalize both sides of the repository URL comparison\, so that a repository already registered with a trailing slash is recognized as matching instead of failing with <code>Repository already have a repository named \<name\></code> \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1236](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1236)\)\.
* helm\_template \- strip Helm\'s OCI registry progress messages from the returned <code>stdout</code>\, which is documented to contain only the rendered templates \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1223](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1223)\)\.
* k8s lookup \- ignore <code>ENABLE\_TURBO\_MODE</code> on ansible\-core 2\.19\.0 and later\, where the <code>cloud\.common</code> collection is not supported\. Fall back to the standard <code>LookupBase</code> instead of failing with a traceback \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1253](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1253)\)\.
* k8s\_cp \- Fix silent truncation when copying to a pod\. The module closed the exec connection immediately after writing the last chunk of the tar archive\, which killed the remote <code>tar</code> before it had finished extracting\, and never checked the process exit status\, so a partial copy was reported as a success\. The archive is now bounded with <code>head \-c</code> so <code>tar</code> gets a clean EOF and exits on its own\, and the module waits for that exit and fails on a non\-zero status \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1217)\)\.
* k8s\_drain \- Fix logic for handling pods with local storage to correctly check for empty\_dir volumes in replicated pods and pods managed by DaemonSets \([https\://github\.com/ansible\-collections/kubernetes\.core/pull/1095](https\://github\.com/ansible\-collections/kubernetes\.core/pull/1095)\)\.
* k8s\_info \- Handle empty template output gracefully by returning <code>changed\=false</code> instead of failing when Jinja2 template renders to an empty string \([https\://github\.com/ansible\-collections/kubernetes\.core/issues/1042](https\://github\.com/ansible\-collections/kubernetes\.core/issues/1042)\)\.

<a id="lowlydba-sqlserver-2"></a>
#### lowlydba\.sqlserver

* ag\_listener \- <code>ip\_address</code>\, <code>subnet\_mask</code> and <code>dhcp</code> were only used when creating a new listener\, so changing them on an existing listener reported no change and left it untouched\. These settings can\'t be altered in place\, so a mismatch between the requested and current IP configuration now drops and re\-creates the listener via <code>Remove\-DbaAgListener</code> and <code>Add\-DbaAgListener</code> \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/376](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/376)\)\.
* ag\_replica \- <code>data</code> now returns the existing replica when no change is needed instead of being omitted \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* ag\_replica \- replace the <code>Compare\-Object</code> comparison between a hashtable and the SMO object with an explicit per\-property comparison so enums and bools compare cleanly against Ansible values \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* agent\_job\_step \- Fix inability to rename a step by <code>step\_id</code>\. The module now looks up the existing step by <code>step\_id</code> when <code>state\=present</code>\, instead of by <code>step\_name</code>\, so a rename \(new <code>step\_name</code>\, same <code>step\_id</code>\) is correctly detected as an update\.
* agent\_job\_step \- <code>data</code> is re\-read from the server after applying changes instead of being patched with the requested <code>output\_file</code> value \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* availability\_group \- Fix <code>changed</code> being incorrectly reported as <code>true</code> on an unchanged AG\. <code>Get\-DbaAvailabilityGroup</code>\'s SMO object never populates <code>FailureConditionLevel</code>/<code>HealthCheckTimeout</code> \(they read back as unset defaults\)\, and <code>sys\.availability\_groups</code> is a cache of the WSFC cluster resource\'s copy\, so it\'s empty for AGs with <code>cluster\_type</code> set to <code>None</code>\. Since neither source can be trusted\, both properties are now excluded from the idempotency diff\; they\'re still applied via <code>Set\-DbaAvailabilityGroup</code> whenever another property change triggers an update \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/381](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/381)\)\.
* availability\_group \- <code>data</code> now returns the existing availability group when no change is needed instead of being omitted \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* availability\_group \- <code>dtc\_support\_enabled</code>\, <code>basic\_availability\_group</code>\, <code>database\_health\_trigger</code> and <code>is\_distributed\_ag</code> were only passed to <code>Set\-DbaAvailabilityGroup</code> when <code>true</code>\, so they could not be disabled on an existing availability group \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* availability\_group \- replace the <code>Compare\-Object</code> comparison between a hashtable and the SMO object with an explicit per\-property comparison so enums and bools compare cleanly against Ansible values \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* backup \- the <code>compress</code>\, <code>encryption\_certificate</code>\, <code>azure\_base\_url</code> and <code>azure\_credential</code> options were read from the wrong variable and never passed to <code>Backup\-DbaDatabase</code> \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* backup\, restore \- Fix <code>changed</code> being reported as <code>false</code> in <code>check\_mode</code>\, since <code>Backup\-DbaDatabase</code>/<code>Restore\-DbaDatabase</code> return no output under <code>\-WhatIf</code> \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/381](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/381)\)\.
* database \- <code>data</code> is re\-read from the server after applying changes instead of echoing the requested <code>recovery\_model</code>\, <code>compatibility</code>\, <code>rcsi</code>\, <code>maxdop</code> and <code>secondary\_maxdop</code> values \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* database \- the current <code>secondary\_maxdop</code> was read from a nonexistent SMO property\, so every run with <code>secondary\_maxdop</code> set reported <code>changed</code> and re\-applied it \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* install\_script \- the <code>deployment\_method</code> option was accepted but never passed to <code>Install\-DboScript</code> \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* login \- <code>password\_policy\_enforced</code> and <code>password\_expiration\_enabled</code> set to <code>false</code> reported <code>changed</code> but never passed <code>\$false</code> to <code>Set\-DbaLogin</code>\, so the setting stayed enabled \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* login \- a changed <code>default\_database</code> on an existing login did not set <code>changed</code> and was only applied if another option also changed \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* login\, credential \- failure messages no longer include the raw parameter splat \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* resource\_governor \- omitting <code>classifier\_function</code> reported <code>changed</code> on every run when the instance already had a classifier function configured \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* restore \- the <code>azure\_credential</code> option was read from the wrong variable and never passed to <code>Restore\-DbaDatabase</code> \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* rg\_resource\_pool \- <code>data</code> now returns the existing resource pool when no change is needed instead of being omitted \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* rg\_resource\_pool \- replace the <code>Compare\-Object</code> comparison between a hashtable and the SMO object with an explicit per\-property comparison to avoid spurious changes \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* rg\_workload\_group \- replace the <code>Compare\-Object</code> comparison between a hashtable and the SMO object with an explicit per\-property comparison to avoid spurious changes \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.
* sa \- <code>password\_policy\_enforced</code> and <code>password\_expiration\_enabled</code> set to <code>false</code> reported <code>changed</code> but never passed <code>\$false</code> to <code>Set\-DbaLogin</code>\, so the setting stayed enabled \([https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374](https\://github\.com/lowlydba/lowlydba\.sqlserver/issues/374)\)\.

<a id="microsoft-ad-1"></a>
#### microsoft\.ad

* Fix bug when creating a new AD object with an attribute set to an empty value\. For example using <code>allowed\_to\_retrieve\_password\: \{set\: \[\]\}</code> on <code>microsoft\.ad\.service\_account</code> will be treated like the value was not specified at all \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/229](https\://github\.com/ansible\-collections/microsoft\.ad/issues/229)
* Removed use of deprecated <code>\_encode\_script</code> function used by the internal reboot functionality of the AD plugins\.
* domain \- Ensure that the <em class="title-reference">microsoft\.ad\.domain</em> module errors when a forest already exists\. This prevents the module from attempting to create a new forest if an existing forest is detected and prints an error message indicating that\.
* domain \- Fix PowerShell 7 compatibility
* domain\_child \- Fix PowerShell 7 compatibility
* domain\_controller \- Fix PowerShell 7 compatibility
* group \- Treat the <code>name</code> value as part of the object\'s distinguished name to avoid any false matches for a <code>userPrincipalName</code> or <code>sAMAccountName</code> pattern \- [https\://github\.com/ansible\-collections/microsoft\.ad/issues/198](https\://github\.com/ansible\-collections/microsoft\.ad/issues/198)
* object\_info \- Fix PowerShell 7 compatibility when specified property does not match the same case as the property on the found AD object
* user \- Ensure any post actions like editing the user\'s groups are performed on the correct distinguished name\. This fixes the error when changing the user\'s groups when the user was moved in the same module invocation\.

<a id="microsoft-iis-1"></a>
#### microsoft\.iis

* website \- fix <code>changed</code> not set on cert update for existing binding via <code>bindings\.add</code> \([https\://github\.com/ansible\-collections/microsoft\.iis/pull/59](https\://github\.com/ansible\-collections/microsoft\.iis/pull/59)\)\.
* website \- fix failure to set bindings \(unsupported protocols result in partial filtering\) \([https\://github\.com/ansible\-collections/microsoft\.iis/pull/71](https\://github\.com/ansible\-collections/microsoft\.iis/pull/71)\)
* website\_info \- Fix logic for determining <code>use\_ccs</code> is set to take into account new SSL flags added in Server 1809 or newer \- [https\://github\.com/ansible\-collections/microsoft\.iis/pull/57](https\://github\.com/ansible\-collections/microsoft\.iis/pull/57)

<a id="netapp-ontap-2"></a>
#### netapp\.ontap

* na\_ontap\_nvme\_namespace \- Fixed issue with NVME Namespace get operation\.
* na\_ontap\_qtree \- Fixed issue with timeout in DELETE operation and added option <em class="title-reference">rest\_timeout</em> to avoid timeout in GET\.
* na\_ontap\_volume \- Updated code to check for <em class="title-reference">aggr\_list</em> and return an error if <em class="title-reference">aggr\_list\_multiplier</em> is used without <em class="title-reference">aggr\_list</em> in ONTAP REST 9\.17 or later\.
* na\_ontap\_vserver\_create \- fixed undefined variable error\.

<a id="netapp-eseries-santricity-3"></a>
#### netapp\_eseries\.santricity

* na\_santricity\_volume and nar\_santricity\_host \- Restore backwards compatibility for the renamed <code>raid\_level</code> volume option by accepting it as an alias of <code>ddp\_raid\_level</code>\.
* nar\_santricity\_common \- Improve system API URL validation by forcing URL checks to run outside check mode and ignoring skipped URI results\.

<a id="ngine-io-cloudstack-2"></a>
#### ngine\_io\.cloudstack

* The removed routing to module names with <code>cs\_</code> prefix instroduced in 3\.1\.0 has been restored\. Backwards compatibility with existing playbooks is now ensured\.
* portforward \- Fixed rule creation for primary IP of default NIC \([https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/issues/108](https\://github\.com/ngine\-io/ansible\-collection\-cloudstack/issues/108)\)

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
* purefb\_bucket \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_bucket \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket \- Fixed issue creating bucket with no versioning incorrectly failing
* purefb\_bucket \- Fixed module\.warn\(\) calls to be compatible with Ansible 2\.15\+ by removing msg\= parameter
* purefb\_bucket \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_bucket \- Stop sending context\_names when destroying a bucket without a context\, which leaked an empty/invalid fleet context
* purefb\_bucket\_access \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_bucket\_access \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket\_access \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_bucket\_replica \- Added safety checks for empty lists before accessing \[0\] index
* purefb\_bucket\_replica \- Added validation for missing target parameter when creating new replica links
* purefb\_bucket\_replica \- Allow a replica link to be removed when its local bucket no longer exists \([https\://github\.com/Everpure\-Ansible/FlashBlade\-Collection/issues/545](https\://github\.com/Everpure\-Ansible/FlashBlade\-Collection/issues/545)\)
* purefb\_bucket\_replica \- Check actual list length instead of unreliable total\_item\_count
* purefb\_bucket\_replica \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_bucket\_replica \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_bucket\_replica \- Fixed IndexError \'list index out of range\' in get\_connected\(\) function
* purefb\_bucket\_replica \- Fixed iteration anti\-pattern using range\(len\(\)\) that could cause IndexError
* purefb\_bucket\_replica \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_certgrp \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#497\)
* purefb\_certs \- Corrects typos in the parameter name\.
* purefb\_certs \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_certs \- Fixes certificate\_type name from array to appliance
* purefb\_certs \- Fixes issue where intermediate\_certificate was not be applied to certificates\.
* purefb\_certs \- Removes immutable field certificate\_type for the patch operation\.
* purefb\_connect \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_connect \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_connect \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_connect \- Use unified time conversion from time\_utils module
* purefb\_dns \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_dns \- Use remove\_duplicates\(\) from common instead of local remove\(\) function
* purefb\_ds \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_dsrole \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_export \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_export \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_export \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_fleet \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_fs \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_fs \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_fs \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_fs \- Fixed <code>not in a fleet</code> errors on standalone arrays by only sending <code>context\_names</code> when a context is set\, and only defaulting the context for arrays that are fleet members\.
* purefb\_fs \- Fixed failure to apply policies to existing filesystems due to incorrect API check and non\-existent patch method
* purefb\_fs \- Fixed issue where NFS export policies were applied even when both nfsv3 and nfsv4 were disabled
* purefb\_fs \- Fixed issue where SMB policies were applied even when smb parameter was set to false
* purefb\_fs \- Restore the <code>nfs\_rules</code> parameter\, silently ignored since v1\.25\.0\. Inline NFS export rules are applied again on create and update for non\-realm filesystems\.
* purefb\_fs\_replica \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_groupquota \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_groupquota \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_groupquota \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#498\)
* purefb\_groupquota \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_hardware \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_info \- Fix AttributeError where the policy loop variable was overwritten with <em class="title-reference">policy\.name</em>\, breaking <em class="title-reference">gather\_subset\=policies</em> \(\#547\)
* purefb\_info \- Fixed bucket AttributeError
* purefb\_info \- Use unified time conversion from time\_utils module
* purefb\_keytabs \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_kmip \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_lag \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_lifecycle \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_lifecycle \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_lifecycle \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_lifecycle \- Use unified time conversion from time\_utils module with proper None handling
* purefb\_messages \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_network \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_ntp \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_ntp \- Use remove\_duplicates\(\) from common instead of local remove\(\) function
* purefb\_phonehome \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_pingtrace \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_policy \- Create a policy rule when the client lookup returns no match or an error\, fixing failures adding the first rule for a client while keeping the task idempotent
* purefb\_policy \- Fix UnboundLocalError when policy string is not found
* purefb\_policy \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#499\)
* purefb\_policy \- Fixed AttributeError with empty policy rules
* purefb\_policy \- Fixed NFS export policy rules not updating when only the <code>access</code> value \(e\.g\. root\-squash to no\-squash\) changed\; <code>access</code> was missing from the idempotency comparison\.
* purefb\_policy \- Fixed an object store access policy rule update referencing a non\-existent key when preserving existing source IPs\.
* purefb\_policy \- Fixed policy rule updates \(NFS export\, SMB share\, SMB client\, network access\) resetting unspecified fields to null\; patches now use merged values so omitted fields are kept\.
* purefb\_policy \- Fixed snapshot policy updates dropping the <code>at</code> time and timezone \(reverting to an interval\-only rule\) when <code>every</code> or <code>keep\_for</code> were changed without re\-specifying <code>at</code>\.
* purefb\_policy \- Only send context\_names when a context is set\, and only default it for fleet members\, avoiding empty\-context errors and \"not in a fleet\" errors on standalone arrays
* purefb\_policy \- Use unified time conversion from time\_utils module
* purefb\_proxy \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_ra \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_remote\_cred \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_remote\_cred \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_remote\_cred \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_s3acc \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_s3acc \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_s3acc \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_s3user \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_s3user \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_s3user \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_saml \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_saml \- Fixed typo in model name
* purefb\_server \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_smtp \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_snap \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_snap \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_snap \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#500\)
* purefb\_snap \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
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
* purefb\_userpolicy \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_userpolicy \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_userpolicy \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_userquota \- Consolidated duplicate get\_fs\(\) function and fixed unsafe list access \(\#493\)
* purefb\_userquota \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_userquota \- Fix unsafe res\.errors\[0\]\.message access that could cause IndexError \(\#501\)
* purefb\_userquota \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* purefb\_virtualhost \- Default context to the local array name to avoid errors from an empty context\_names on newer Purity//FB releases
* purefb\_virtualhost \- Only send context\_names when a context is set\, and only default it for fleet members\, fixing \"not in a fleet\" errors on standalone arrays
* time\_utils \- Add unified time conversion module with proper error handling and input validation

<a id="splunk-es-3"></a>
#### splunk\.es

* plugins/module\_utils/splunk\.py \- wrapped the <code>ansible\.utils</code> collection import in a <code>try/except</code> block so that <code>ansible\-test sanity \-\-test import</code> no longer raises <code>ModuleNotFoundError</code> in the isolated sanity environment\.

<a id="telekom-mms-icinga-director-1"></a>
#### telekom\_mms\.icinga\_director

* fix\: prevent simultaneous deploy handler \([https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/323](https\://github\.com/telekom\-mms/ansible\-collection\-icinga\-director/pull/323)\)

<a id="theforeman-foreman-2"></a>
#### theforeman\.foreman

* content\_view \- scope lifecycle\_environments by organization to avoid errors with duplicate names across organizations \([https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1980](https\://github\.com/theforeman/foreman\-ansible\-modules/pull/1980)\)

<a id="vmware-vmware-1"></a>
#### vmware\.vmware

* folder \- Add check mode support for create and delete operations \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/387](https\://github\.com/ansible\-collections/vmware\.vmware/issues/387)\)\.
* import\_content\_library\_iso \- Fix OOM error when uploading large local ISO files by streaming the file instead of loading it into memory \([https\://github\.com/ansible\-collections/vmware\.vmware/issues/385](https\://github\.com/ansible\-collections/vmware\.vmware/issues/385)\)\.
* inventory plugins \- Fix a bug where the customValue property was always gathered\, even when not requested
* key\_provider\_native \- Fix an <code>AttributeError</code> when gathering the default KMS cluster and no default cluster is configured\.
* module\_utils/vmware\_rest\_client \- correct python syntax and proxy url syntax\.
* tag\_associations \- Fix error when using the object\_name parameter to lookup an object Fixes \- [https\://github\.com/ansible\-collections/vmware\.vmware/issues/315](https\://github\.com/ansible\-collections/vmware\.vmware/issues/315)
* vm \- Fix incorrect parameter name in error when neither datastore nor datastore\_cluster is provided for VM creation\. Follow\-up to [https\://github\.com/ansible\-collections/vmware\.vmware/issues/334](https\://github\.com/ansible\-collections/vmware\.vmware/issues/334)\.
* vm \- Fix issue where datastore was always a required parameter for creating new vms\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/334](https\://github\.com/ansible\-collections/vmware\.vmware/issues/334)
* vm \- correct O\(delete\_from\_inventory\) documentation for C\(state\=absent\) to match module behavior\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/322](https\://github\.com/ansible\-collections/vmware\.vmware/issues/322)
* vm\_powerstate \- only attempt to answer VM questions when a question is actually pending\. Previously\, supplying the question\_answers parameter while no question had appeared yet caused the module to error out before it could wait for and answer the question\, leaving the VM stuck\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/224](https\://github\.com/ansible\-collections/vmware\.vmware/issues/224)
* vm\_powerstate \- read the authoritative live C\(runtime\.powerState\) instead of the lazily\-updated C\(summary\.runtime\.powerState\) so the module reliably waits for the VM to reach the powered off state when using the shutdown\-guest state\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/224](https\://github\.com/ansible\-collections/vmware\.vmware/issues/224)
* vm\_snapshot \- fix snapshot lookup so entire snapshot tree is accessible\, and not just the first branch\.
* vm\_snapshot \- remove empty string default for the description field\. Descriptions will only be updated if you specify one\. Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/395](https\://github\.com/ansible\-collections/vmware\.vmware/issues/395)
* vm\_snapshot\_revert \- search the snapshot tree fully to find a matching snapshot Fixes [https\://github\.com/ansible\-collections/vmware\.vmware/issues/330](https\://github\.com/ansible\-collections/vmware\.vmware/issues/330)

<a id="vmware-vmware-rest-3"></a>
#### vmware\.vmware\_rest

* module\_utils \- Avoid importing cloud\.common turbo exceptions unless turbo mode is explicitly enabled\, preventing a cloud\.common Ansible 2\.20 support warning in module runs when turbo is off \([https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/637](https\://github\.com/ansible\-collections/vmware\.vmware\_rest/issues/637)\)\.

<a id="vultr-cloud"></a>
#### vultr\.cloud

* Fixed an issue with missing Content\-Type HTTP request header\, which resulted in 400 Bad Request \([https\://github\.com/vultr/ansible\-collection\-vultr/issues/186](https\://github\.com/vultr/ansible\-collection\-vultr/issues/186)\)\.

<a id="known-issues"></a>
### Known Issues

<a id="ansible-core-8"></a>
#### Ansible\-core

* Secret masking \- when <code>ANSIBLE\_DEBUG\=1</code> is set\, the raw stdout and stderr of commands executed on the target\, including module results\, are displayed before the secrets contained in the module result have been registered for masking\. Secrets which are only known to the module\, such as <code>no\_log</code> option values\, may therefore be shown in plaintext in debug output\.

<a id="new-plugins"></a>
### New Plugins

<a id="callback"></a>
#### Callback

* community\.general\.oneline \- One\-line Ansible screen output\.

<a id="filter"></a>
#### Filter

* ansible\.builtin\.mask\_secrets \- Redact registered secrets from a string
* ansible\.builtin\.register\_secret \- Register a value as a secret so it is masked in output
* community\.general\.from\_toml \- Convert TOML string into dictionary\.

<a id="inventory"></a>
#### Inventory

* community\.dns\.infomaniak\_dns\_records \- Create inventory from Infomaniak DNS records\.

<a id="lookup"></a>
#### Lookup

* community\.general\.proton\_pass \- Fetch secrets from Proton Pass via the <code>pass\-cli</code> command\-line tool\.

<a id="new-modules"></a>
### New Modules

<a id="ansible-mysql-3"></a>
#### ansible\.mysql

* ansible\.mysql\.mysql\_binlog\_info \- Gather MySQL or MariaDB binary log information
* ansible\.mysql\.mysql\_clone \- Clone a MySQL instance from a donor server
* ansible\.mysql\.mysql\_partition \- Manage MySQL table partitions
* ansible\.mysql\.mysql\_password\_policy \- Manage MySQL or MariaDB password policy settings
* ansible\.mysql\.mysql\_perf\_schema \- Manage MySQL or MariaDB Performance Schema setup tables
* ansible\.mysql\.mysql\_replication\_filter \- Manage MySQL or MariaDB replication filters
* ansible\.mysql\.mysql\_resource\_group \- Add\, update\, or remove MySQL resource groups
* ansible\.mysql\.mysql\_resource\_group\_info \- Gather information about MySQL resource groups
* ansible\.mysql\.mysql\_slow\_log \- Manage MySQL or MariaDB slow query log settings
* ansible\.mysql\.mysql\_tablespace \- Manage MySQL InnoDB general tablespaces
* ansible\.mysql\.mysql\_tablespace\_info \- Gather MySQL tablespace information
* ansible\.mysql\.mysql\_tls \- Manage MySQL TLS runtime settings

<a id="ansible-windows-2"></a>
#### ansible\.windows

* ansible\.windows\.win\_capability \- Manage Windows capabilities
* ansible\.windows\.win\_capability\_info \- Get information about Windows capabilities
* ansible\.windows\.win\_reboot\_info \- Get reboot status information for a Windows host

<a id="cloudscale-ch-cloud-2"></a>
#### cloudscale\_ch\.cloud

* cloudscale\_ch\.cloud\.interface \- Manages network interfaces on the cloudscale\.ch IaaS service
* cloudscale\_ch\.cloud\.router \- Manages routers on the cloudscale\.ch IaaS service

<a id="community-clickhouse-4"></a>
#### community\.clickhouse

* community\.clickhouse\.clickhouse\_named\_collection \- Creates\, removes or modify a ClickHouse named collection using the clickhouse\-driver Client interface
* community\.clickhouse\.clickhouse\_row\_policy \- Creates\, removes or modify a ClickHouse row policy using the clickhouse\-driver Client interface
* community\.clickhouse\.clickhouse\_script \- Run SQL queries from a file
* community\.clickhouse\.clickhouse\_settings\_profile \- Creates\, removes or modify a ClickHouse settings profile using the clickhouse\-driver Client interface

<a id="community-crypto-3"></a>
#### community\.crypto

* community\.crypto\.openssl\_pkcs12\_extract \- Extract certificate and private key from PKCS\#12 archive\.
* community\.crypto\.openssl\_pkcs12\_info \- Return certificates and \(optionally\) private key of a PKCS\#12 file\.

<a id="community-dns-2"></a>
#### community\.dns

* community\.dns\.infomaniak\_dns\_record \- Add or delete a single record in Infomaniak DNS service\.
* community\.dns\.infomaniak\_dns\_record\_info \- Retrieve records in Infomaniak DNS service\.
* community\.dns\.infomaniak\_dns\_record\_set \- Add or delete record sets in Infomaniak DNS service\.
* community\.dns\.infomaniak\_dns\_record\_set\_info \- Retrieve record sets in Infomaniak DNS service\.
* community\.dns\.infomaniak\_dns\_record\_sets \- Bulk synchronize DNS record sets in Infomaniak DNS service\.
* community\.dns\.infomaniak\_dns\_zone\_info \- Retrieve zone information in Infomaniak DNS service\.

<a id="community-general-3"></a>
#### community\.general

* community\.general\.appimage \- Manage AppImage packages\.
* community\.general\.consul\_kv\_info \- Retrieve entries from the key/value store of a Consul cluster\.
* community\.general\.gitlab\_project\_approvals \- Manage project\-level merge request approvals settings on GitLab Server\.
* community\.general\.golang\_package \- Manage Go packages with <code>go install</code>\.
* community\.general\.google\_chat \- Send Google Chat notifications\.
* community\.general\.keycloak\_clientscope\_rolemappings \- Allows administration of Keycloak clientscope scope mappings to restrict the usage of certain roles to specific clientscopes\.
* community\.general\.keycloak\_realm\_users\_info \- Retrieve users from a Keycloak realm using the Keycloak API\.
* community\.general\.kopia\_repository \- Manage Kopia repository\.
* community\.general\.kopia\_repository\_info \- Gather information about a Kopia repository\.
* community\.general\.write\_binary\_file \- Write binary file from Base64 encoded input\.
* community\.general\.xml\_info \- Query XML files or strings\.

<a id="dellemc-powerflex-1"></a>
#### dellemc\.powerflex

* dellemc\.powerflex\.device\_group \- Manage Device Groups on Dell PowerFlex Gen2
* dellemc\.powerflex\.thin\_clone \- Create Thin Clones on Dell PowerFlex 5\.x \(Gen2\)

<a id="fortinet-fortimanager-1"></a>
#### fortinet\.fortimanager

* fortinet\.fortimanager\.fmgr\_antivirus\_profile\_websocket \- Configure WEBSOCKET AntiVirus options\.
* fortinet\.fortimanager\.fmgr\_casb\_useractivity\_match\_tenantsessionextraction \- CASB user activity tenant session extraction\.
* fortinet\.fortimanager\.fmgr\_casb\_useractivity\_match\_tenantsessionextraction\_filters \- CASB user activity session extraction filters\.
* fortinet\.fortimanager\.fmgr\_deployment\_get\_controller\_status \- Refresh status of AP/Switch/Extender controller\.
* fortinet\.fortimanager\.fmgr\_firewall\_customtag \- Define custom tag table\.
* fortinet\.fortimanager\.fmgr\_firewall\_profileprotocoloptions\_websocket \- Configure WebSocket protocol options\.
* fortinet\.fortimanager\.fmgr\_pm\_config\_pblock\_firewall\_localinpolicy \- Configure user defined IPv4 local\-in policies\.
* fortinet\.fortimanager\.fmgr\_pm\_config\_pblock\_firewall\_localinpolicy6 \- Configure user defined IPv6 local\-in policies\.
* fortinet\.fortimanager\.fmgr\_switchcontroller\_securitypolicy\_admin \- Configure fortiswitchs admin security\-policy\.
* fortinet\.fortimanager\.fmgr\_sys\_backup \- Backup FortiManager configuration\.
* fortinet\.fortimanager\.fmgr\_system\_csf\_trustedlist\_adom \- Cli system csf trusted list adom
* fortinet\.fortimanager\.fmgr\_user\_aci \- User aci
* fortinet\.fortimanager\.fmgr\_user\_azure \- User azure
* fortinet\.fortimanager\.fmgr\_user\_azure\_rule \- User azure rule
* fortinet\.fortimanager\.fmgr\_user\_guardicore \- User guardicore
* fortinet\.fortimanager\.fmgr\_user\_local\_dynamicmapping \- Configure local users\.
* fortinet\.fortimanager\.fmgr\_vpn\_ipsec\_fec\_mappings\_tos \- FEC redundancy mapping table for specific type of service
* fortinet\.fortimanager\.fmgr\_wireless\_lwprofile \- Configure LoRaWAN profile\.
* fortinet\.fortimanager\.fmgr\_ztna\_destination \- Configure ZTNA destination\.

<a id="kubernetes-core-3"></a>
#### kubernetes\.core

* kubernetes\.core\.kubeconfig \- Generate\, update\, and optionally write Kubernetes kubeconfig files

<a id="microsoft-ad-2"></a>
#### microsoft\.ad

* microsoft\.ad\.cs\_authority \- Manage CA CRL Distribution Points and Authority Information Access
* microsoft\.ad\.cs\_template \- Manage AD Certificate Services certificate templates
* microsoft\.ad\.domain\_trust \- Manage Active Directory domain trusts
* microsoft\.ad\.fs\_claim\_rule \- Manage AD FS claim rules on a Relying Party Trust
* microsoft\.ad\.fs\_trust \- Manage AD FS Relying Party Trusts
* microsoft\.ad\.gpo \- Manage Group Policy Object links
* microsoft\.ad\.kds\_root\_key \- Manages a KDS root key in a domain
* microsoft\.ad\.kds\_root\_key\_info \- Gather information about one or more KDS root keys in a domain\.
* microsoft\.ad\.pso \- Manage Active Directory Password Settings Objects
* microsoft\.ad\.site \- Manage Active Directory replication sites
* microsoft\.ad\.site\_link \- Manage Active Directory replication site links
* microsoft\.ad\.site\_subnet \- Manage Active Directory replication subnets

<a id="microsoft-iis-2"></a>
#### microsoft\.iis

* microsoft\.iis\.authentication \- Configures authentication options in IIS\.
* microsoft\.iis\.page\_order \- Configures default document order in IIS\.

<a id="netapp-ontap-3"></a>
#### netapp\.ontap

* netapp\.ontap\.na\_ontap\_user\_role\_config \- NetApp ONTAP local user account restrictions

<a id="ngine-io-cloudstack-3"></a>
#### ngine\_io\.cloudstack

* ngine\_io\.cloudstack\.api\_request \- Executes ad\-hoc Apache CloudStack API requests\.
* ngine\_io\.cloudstack\.cluster\_info \- Gathering information about clusters from Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.internal\_lb\_vm \- Manages internal load balancer instances on Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.lb\_internal \- Manages internal load balancers on Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.lb\_internal\_member \- Manages internal load balancer members on Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.pod\_info \- Gathering information about pods from Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.ssl\_cert \- Manages SSL certificates on Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.user\_data \- Manages user data on Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.vpc\_private\_gateway \- Manages private gateways for VPCs on Apache CloudStack based clouds\.
* ngine\_io\.cloudstack\.vpn\_user \- Manages VPN users on Apache CloudStack based clouds\.

<a id="purestorage-flasharray-2"></a>
#### purestorage\.flasharray

* purestorage\.flasharray\.purefa\_tgroup \- Manage topology groups on Everpure FlashArrays

<a id="purestorage-flashblade-3"></a>
#### purestorage\.flashblade

* purestorage\.flashblade\.purefb\_export \- Manage filesystem exports on Everpure FlashBlade\`
* purestorage\.flashblade\.purefb\_realm \- Manage realms on Everpure FlashBlades
* purestorage\.flashblade\.purefb\_s3\_export\_policy \- Manage FlashBlade S3 Export Policies
* purestorage\.flashblade\.purefb\_s3acc\_export \- Manage FlashBlade Object Store Account exports

<a id="telekom-mms-icinga-director-2"></a>
#### telekom\_mms\.icinga\_director

* telekom\_mms\.icinga\_director\.icinga\_importsource \- Manage import sources in Icinga2 Director

<a id="vmware-vmware-2"></a>
#### vmware\.vmware

* vmware\.vmware\.esxi\_info \- Gathers information about one or more ESXi hosts
* vmware\.vmware\.esxi\_powerstate \- Manages power states of ESXi hosts in vCenter
* vmware\.vmware\.esxi\_service \- Manage the state and startup policy of a service on an ESXi host
* vmware\.vmware\.esxi\_service\_info \- Gather information about the services on an ESXi host

<a id="unchanged-collections"></a>
### Unchanged Collections

* chocolatey\.chocolatey \(still version 1\.6\.0\)
* cisco\.aci \(still version 2\.13\.0\)
* cisco\.mso \(still version 2\.13\.0\)
* cisco\.ucs \(still version 1\.16\.0\)
* community\.grafana \(still version 2\.3\.0\)
* community\.hashi\_vault \(still version 7\.1\.0\)
* community\.hrobot \(still version 2\.7\.2\)
* community\.library\_inventory\_filtering\_v1 \(still version 1\.1\.5\)
* community\.mysql \(still version 5\.0\.2\)
* community\.proxmox \(still version 2\.0\.0\)
* community\.proxysql \(still version 1\.8\.0\)
* community\.zabbix \(still version 4\.2\.0\)
* dellemc\.enterprise\_sonic \(still version 4\.1\.0\)
* dellemc\.unity \(still version 2\.1\.0\)
* grafana\.grafana \(still version 6\.1\.0\)
* ieisystem\.inmanage \(still version 4\.0\.0\)
* inspur\.ispim \(still version 2\.2\.4\)
* kaytus\.ksmanage \(still version 4\.0\.0\)
* netapp\.storagegrid \(still version 21\.16\.0\)
* netbox\.netbox \(still version 3\.23\.0\)
* ovirt\.ovirt \(still version 3\.2\.2\)
* pcg\.alpaca\_operator \(still version 2\.2\.0\)
* ravendb\.ravendb \(still version 1\.0\.4\)
* vyos\.vyos \(still version 6\.0\.0\)
* wti\.remote \(still version 1\.0\.11\)
