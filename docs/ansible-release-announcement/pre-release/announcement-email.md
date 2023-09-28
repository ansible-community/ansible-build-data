Release announcement : Ansible Community Package X.0.0a1 (Pre Release)

Hello everyone,

We're happy to announce the release of the Alpha release of Ansible X.0.0a1!

This pre-release version contains the latest version of ansible-core a.b and includes a curated set of Ansible collections that provides a vast number of modules and plugins.

ansible-core is a required dependency, not contained within the ansible packages.

How to get it?
--------------

This release is available on PyPI and can be installed with pip:

`$ python3 -m pip install ansible==X.0.0a1 --user`

The source and the wheel for this release can be found here:

Release tarball:


SHA256:


Wheel package:


SHA256:


Some important details
----------------------

Python wheels are available for both Ansible X and ansible-core a.b.

In addition, Ansible x no longer installs some unnecessary files from the included Ansible collections such as tests or hidden files and directories.  This  further improves installation performance and reduces the size on disk. These files are still available in the source tarball if needed.


Collections which have opted-in to being a part of the Ansible 8 unified changelog will have an entry on this page:

For collections which have not opted-in to the unified changelog, you may find more information on https://docs.ansible.com/ansible/latest/collections or the collection source repository. For example, the community.crypto collection is available at https://docs.ansible.com/ansible/latest/collections/community/crypto/index.html and you can find a link to the source repository under the "Repository(Sources)" button.

The changelog for ansible-core a.b installed by this release of Ansible X can be found here: <changelog of ansible-core>.


What's the schedule for new Ansible releases after X.0.0a1?
---------------------------------------------------------

The next release roadmap can be found at https://docs.ansible.com/ansible/devel/roadmap/ansible_roadmap_index.html

Subscribe to the Bullhorn for all future release dates, announcements, and Ansible contributor community news.

Visit this link to subscribe: https://bit.ly/subscribe-bullhorn

You can find all past Bullhorn issues on the official wiki page:
https://github.com/ansible/community/wiki/News#the-bullhorn


Join the new Ansible Community Forum to follow along and participate in all the discssions release related discussions and announcements. Feel free to share your thoughts, ideas and concerns in there.

Register here to join the Ansible Forum:

https://forum.ansible.com

Porting Help
------------

A unified porting guide for collections that have opted-in is available here:
https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_X.html

Getting collection updates from Ansible X with older releases of ansible-core
-----------------------------------------------------------------------------

Ansible X includes ansible-core a.b. Based on your requirements, you can get collection updates as they ship in the Ansible "batteries included" package while continuing to use older versions of ansible-core.

An ansible-galaxy requirements file based on the collections from Ansible X has been made available for this use case:

<https://github.com/ansible-community/ansible-build-data/blob/main/X/galaxy-requirements.yaml>

After you download the requirements file, the collections can be installed by running this command:

"ansible-galaxy collection install -r galaxy-requirements.yaml"

On behalf of the Ansible community, thank you and happy automating!

Cheers
Ansible Community Team
