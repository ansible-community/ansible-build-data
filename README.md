# ansible-build-data
Holds generated but persistent results from building ansible.  This information
may be referred to by other projects and scripts.

## Structure of data

::

    ansible-build-data
    └── 3
        ├── ansible-3.0.0.deps
        ├── ansible-3.1.0.deps
        ├── ansible-3.build
        └── ansible.in

* Each major release of Ansible gets a subdirectory of the repository named
  according to the X.Y version number of Ansible.  (ex: `3`)

* Within each version directory, there is an `ansible.in` file which lists the
  collections that are in this release of Ansible.  The file consists of one
  `namespace.collection` per line.  This file is constructed by the person
  building Ansible for that release.

* There will also be a file, `ansible-X.build`.  This file contains lines which
  consist of `namespace.collection` followed by a version range like::

      awx.awx: >=11.0.0,<12.0.0

  The version range specifies potential versions of the collection that are
  backwards compatible with what was available when the initial Ansible-X.Y.0
  release was frozen.  Only versions of the collections within those ranges
  will be considered for Ansible minor releases.  This file will be created by the
  ``antsibull-build new-ansible`` command.

* Lastly, there will be multiple, `ansible-X.Y.Z.deps` files.  Those files contain
  lines which consist of `namespace.collection` followed by a single version like::

      awx.awx: 11.2.5

  The version specifies the exact version of the collection that appeared in that
  release of Ansible.  This file will be created by the ``antsibull-build single``
  command.

## Adding a new collection

### Next Ansible major release

To add a collection to the next Ansible major release:

* Add the collection to the `ansible.in` file in a sub-directory named with a corresponding number.

### The current Ansible major release

To add a collection to the next minor release of the current Ansible major version:

* Add the collection to the `ansible.in` file in a sub-directory named with a corresponding number.
* In the same sub-directory, add the collection and its version range to the `ansible-X.build` file.
