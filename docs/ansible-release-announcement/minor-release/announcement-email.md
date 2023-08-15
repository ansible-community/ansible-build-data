Release announcement : Ansible Community Package X.0.0

Hello everyone,

We're happy to announce the release of the Ansible X.0.0 package!

Ansible X.0.0 requires latest version of ansible-core a.b and includes a curated set of Ansible collections that provides a vast number of modules and plugins. This is a major release of Ansible.
  
ansible-core is a required dependency, not contained within the ansible packages. Pip install builds the
dependency, but it can be built and installed quite independently of the "ansible" distribution.

How to get it
-------------

This release is available on PyPI and can be installed with pip:

`$ python3 -m pip install ansible==X.0.0 --user`

The sources for this release can be found here:

Release tarball:


SHA256:



Wheel package:



SHA256:



Some important details
----------------------

Python wheels are now available for both Ansible 8 and ansible-core a.b resulting in significantly improved installation performance.

In addition, Ansible x no longer installs some unnecessary files from the included Ansible collections such as tests or hidden files and directories. This further improves installation performance and reduces the size on disk. These files are still available in the source tarball if needed.

The changelog for ansible-core x.x installed by this release of Ansible x can be found here:

Collections which have opted-in to being a part of the Ansible 8 unified changelog will have an entry on this page:

For collections which have not opted-in to the unified changelog, you may find more information on https://galaxy.ansible.com or the collection source repository. For example, the community.crypto collection is available at https://galaxy.ansible.com/community/crypto and you can find a link to the source repository under the "Repo" button at the top right.

What's the schedule for new Ansible releases after X.0.0?
---------------------------------------------------------

Subscribe to the Bullhorn for all future release dates, announcements, and Ansible contributor community news.

Visit this link to subscribe: https://bit.ly/subscribe-bullhorn

You can find all past Bullhorn issues on the official wiki page:
https://github.com/ansible/community/wiki/News#the-bullhorn

Porting Help
------------

A unified porting guide for collections that have opted-in is available here:
https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_8.html

Getting collection updates from Ansible X with older releases of ansible-core
-----------------------------------------------------------------------------

Ansible X includes ansible-core a.b. Based on your requirements, you can get collection updates as they ship in the Ansible "batteries included" package while continuing to use older versions of ansible-core.

An ansible-galaxy requirements file based on the collections from Ansible X has been made available for this use case:

<https://github.com/ansible-community/ansible-build-data/blob/main/8/galaxy-requirements.yaml>

After you download the requirements file, the collections can be installed by running this command:

"ansible-galaxy collection install -r galaxy-requirements.yaml"

On behalf of the Ansible community, thank you and happy automating!

Cheers
Ansible Community Team
