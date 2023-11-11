# ansible-build-data

[![Discuss on Matrix at #community:ansible.com](https://img.shields.io/matrix/community:ansible.com.svg?server_fqdn=ansible-accounts.ems.host&label=Discuss%20on%20Matrix%20at%20%23community:ansible.com&logo=matrix)](https://matrix.to/#/#community:ansible.com)

Holds generated but persistent results from building the `ansible` community package.  This information
may be referred to by other projects and scripts.

## Issue tracker

The [issue track of this repository](https://github.com/ansible-community/ansible-build-data/issues) is to track various aspects of the `ansible` build, including:

1. Tracking release dates,
1. Tracking blockers for a release,
1. Tracking adding, renaming, and removing collections,
1. Tracking problems with a release related to the build process:
   - This includes problems that prevent the package to be installed or system packages to be built from the PyPI release;
1. Tracking and discussing other problems with the `ansible` community package:
   - This includes important problems with the included collections that are not reacted on by the collection maintainers, for example largescale incompatibilities with the current ansible-core version, violation of semantic versioning, and general violation of the [Ansible inclusion requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html);
   - This includes major or security bugs in collections with wide-reaching consequences that are not addressed by the collection maintainers, or cannot be addressed on the collection level for some reason.

This issue tracker is **not** for tracking regular bugs, feature requests, or for asking for help with collections included in the `ansible` package. **Such issues will be closed.** Instead, check out the issue trackers of the respective collections, or consider [asking for help in the Ansible forum](https://forum.ansible.com/).

## Milestones

Release engineers check the [milestones](https://github.com/ansible-community/ansible-build-data/milestones) for corresponding releases some time before releasing the package sufficient to solve all related issues.

## Blockers

In the context of the Ansible Community package release workflow, a **release blocker** is a situation which does not allow the package to be released.
It might come with a new ``ansible-core`` release and affect many of the included collections or in any other way might severely affect consistent work with the ``ansible`` package.
Severity of the impact is determined by the [Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html) in each particular case.
The release blocker must be resolved before the release can proceed.

In case of a potential release blocker, the following actions need to be done:

* Create a [community topic](https://github.com/ansible-community/community-topics/issues) describing the potential blocker.
* If the [Steering Committee](https://docs.ansible.com/ansible/devel/community/steering/community_steering_committee.html) considers the circumstances a release blocker, create an [issue](https://github.com/ansible-community/ansible-build-data/issues/new) in this repository.
* Put the ``blocker`` label on the issue.
* Add the issue to a milestone for the [affected release](https://github.com/ansible-community/ansible-build-data/milestones).

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
  `antsibull-build new-ansible` command.

* Lastly, there will be multiple, `ansible-X.Y.Z.deps` files.  Those files contain
  lines which consist of `namespace.collection` followed by a single version like::

      awx.awx: 11.2.5

  The version specifies the exact version of the collection that appeared in that
  release of Ansible.  This file will be created by the `antsibull-build single`
  command.

## Adding a new collection

### Next Ansible major release

To add a collection to the next Ansible major release that has not reached feature freeze:

* Add the collection to the `ansible.in` file in a sub-directory named with a
  corresponding number.
* In the same sub-directory, add the collection to the `collection-meta.yaml`
  file, as shown below.
  - `maintainers` (list): The Github usernames of the collection's maintainers.
  - `repository` (string): The URL of the collection's git repository.
  - `collection-directory` (string): The collection's top level directory
    relative to the Git repository root. The top level directory is where
    `galaxy.yml` is located. For most collections, this should be set to `.`.
    However, some collections, such as `awx.awx`, store the collection in a
    subdirectory. In that case, `collection-directory` should be set to
    `./SUBDIRECTORY` (`SUBDIRECTORY` is a placeholder for the actual
    directory).
  - `changelog-url` (string): If the collection does not provide a changelog in
    `changelogs/changelog.yaml`, the URL to the actual changelog needs to be
    added. Otherwise, this field should be omitted.

``` yaml
collections:
  # NAMESPACE.NAME
  community.example:
    # The Github usernames of this collection's maintainers
    maintainers:
      - person1
      - person2
    # The URL to the collection's SCM repository.
    repository: https://github.com/ansible-collections/community.example
    # This is the directory where galaxy.yml is stored relative to the
    # repository root.
    #
    # For collections stored in the repository root:
    collection-directory: "."
    # For collections stored in a subdirectory:
    collection-directory: "./SUBDIRECTORY"
    # This is an optional field that should only be populated if the collection
    # doesn't include a changelogs/changelog.yaml file.
    # changelog-url: ...
```

### The current Ansible major release

To add a collection to the next minor release of the current Ansible major version:

* Add the collection to the `ansible.in` file in a sub-directory named with a corresponding number.
* In the same sub-directory, add the collection and its version range to the `ansible-X.build` file.
* In the same sub-directory, add the collection to the `collection-meta.yaml` file.
  - The maintainer's GitHub user names need to be listed there.
  - If the collection does not provide a changelog in `changelogs/changelog.yaml`, the URL to the actual changelog needs to be added.

## Renaming a collection

In some situations, a collection included in Ansible is renamed with its content basically unchanged (up to renaming, adjusting documentation, and potentially other very small changes). In that case, the new collection can be included and the old collection removed if the following procedure is followed.

For simplicity, assume that the next minor Ansible release is X.Y.0, and that collection `foo.bar` with latest release a.b.c has been renamed to `baz.bam` with latest release A.B.C.

1. `baz.bam` A.B.C must be compatible to `foo.bar` a.b.c up to renaming plugins. No options must be renamed without backwards compatible aliases, and no defaults or semantics changed.
2. `baz.bam` A.B.C can be added to Ansible X.Y.0.
3. A deprecation warning is added to Ansible X.Y.0's changelog (`deprecated_features`) that `foo.bar` has been renamed to `baz.bam`, that Ansible (X+1).0.0 will start having deprecated redirects from `foo.bar` to `baz.bam`, and that `foo.bar` will be removed from a later major release of Ansible.
4. A new release `foo.bar` (a+1).0.0 is made which contains no more content, but only deprecated redirects to `baz.bam`. Ideally it will have a dependency on `baz.bam` so that users that install `foo.bar` will have working deprecated redirects.
5. Ansible (X+1).0.0 contains both `foo.bar` (a+1).0.0, and either a `baz.bam` A.B'.C' release or a later major release that is still compatible with `foo.bar` a.b.c as specified in 1.
6. `foo.bar` will be dropped from Ansible (X+2).0.0 (needs to be announced in its changelog as `removed_features`).
