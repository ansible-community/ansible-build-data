Release announcement : Ansible Community Package x.y.z

Hello everyone,

We're happy to announce the release of the Ansible x.y.z package!

Ansible x.y.z requires latest version of ansible-core 2.15 and includes a curated set of
Ansible collections that provides a vast number of modules and plugins.

ansible-core is a required dependency, not
contained within the ansible packages. Pip install builds the
dependency, but it can be built and installed quite independently of
the "ansible" distribution.

How to get it
-------------

This release is available on PyPI and can be installed with pip:

`$ python3 -m pip install ansible==x.y.z --user`

The sources for this release can be found here:

Release tarball:

https://files.pythonhosted.org/packages/87/d7/322dd9d88261e56862ade2f9b9c125d0de648857e755d7177500272d2e05/ansible-x.y.z.tar.gz

SHA256:

91f20b5bfcf5f298533c174a93881e00bc9e6b41411464f44c054a38d716a56a

Wheel package:

https://files.pythonhosted.org/packages/01/43/b5620e57e14a84d9bf257ba4797c2abfa13f7c3be04bc8cd35f86d2e6a2d/ansible-x.y.z-py3-none-any.whl

SHA256:

3bcfb06f2d65edc1c4876df33a52d4469d48d4fe534f1d8ffa196f1b0d81ab0e

Some important details
-----------------------

Python wheels are now available for both Ansible 8 and ansible-core 2.15.x, resulting in significantly improved installation performance.

In addition, Ansible 8 no longer installs some unnecessary files from the included Ansible collections such as tests or hidden files and directories to further improve installation performance and reduce the size on disk. These files are still available in the source tarball if necessary.

The changelog for ansible-core 2.15.1 installed by this release of Ansible 8 can be found here: https://github.com/ansible/ansible/blob/v2.15.1/changelogs/CHANGELOG-v2.15.rst

Collections which have opted-in to being a part of the Ansible 8 unified changelog will have an entry on this page: https://github.com/ansible-community/ansible-build-data/blob/main/8/CHANGELOG-v8.rst

For collections which have not opted-in to the unified changelog, you may find more information on https://galaxy.ansible.com or the collection source repository. For example, the community.crypto collection is available at https://galaxy.ansible.com/community/crypto and you can find a link to the source repository under the "Repo" button at the top right.

What's the schedule for new Ansible releases after x.y.z?
---------------------------------------------------------

Subscribe to the Bullhorn for all future release dates, announcements, and Ansible contributor community news.

Visit this link to subscribe: https://bit.ly/subscribe-bullhorn

You can find all past Bullhorn issues on the official wiki page:
https://github.com/ansible/community/wiki/News#the-bullhorn

Porting Help
------------

A unified porting guide for collections that have opted-in is available here:
https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_8.html

Getting collection updates from Ansible 8 with older releases of ansible-core
--------------------------------------

Ansible 8 includes ansible-core 2.15.x. Based on your requirements, you can get collection updates as they ship in the Ansible "batteries included" package while continuing to use older versions of ansible-core.

An ansible-galaxy requirements file based on the collections from
Ansible 8 has been made available for this use case:
https://github.com/ansible-community/ansible-build-data/blob/main/8/galaxy-requirements.yaml

After you download the requirements file, the collections can be installed by running this command:

"ansible-galaxy collection install -r galaxy-requirements.yaml"

On behalf of the Ansible community, thank you and happy automating!

Cheers
Ansible Community Team