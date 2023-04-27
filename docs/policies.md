# Ansible Collection Policies

This doc explains the necessary ansible-build-data changes to enforce
Ansible Community Steering Committee Policies such as [Removal from Ansible][1]
and [Repository management][2].

## Removal from Ansible

TODO

## Repository management

### Background

From ansible 7.2.0 onwards, each release contains a `ansible-VERSION-tags.yaml`
data file in this repository.
This file contains a mapping of collections to their git repositories and the
git tag that corresponds to the version of a collection included in the ansible release.

The [Ansible release playbook][3] generates these files during the
`antsibull-build prepare` step and later runs
the `antsibull-build validate-tags-file` command to validate them.

It's also possible to separately run `antsibull-build validate-tags-file`.
For example, to validate [the tags file for ansible 7.5.0][4], run

``` console
$ antsibull-build validate-tags-file 7/ansible-7.5.0-tags.yaml
cisco.nso 1.0.3 is not tagged in https://github.com/CiscoDevNet/ansible-nso
hpe.nimble 1.1.4 is not tagged in https://github.com/hpe-storage/nimble-ansible-modules
mellanox.onyx 1.0.0 is not tagged in https://github.com/ansible-collections/mellanox.onyx
$ echo $?
1
```

Since these collections weren't properly tagged prior to formalizing this policy,
they are listed in the `7/validate-tags-ignores` file.
The release playbook passes that file to
`antsibull-build validate-tags-file`'s `--ignores-file` flag to ignore errors
for those collections.

``` console
$ antsibull-build validate-tags-file --ignores-file 7/validate-tags-ignores 7/ansible-7.5.0-tags.yaml
(no output)
$ echo $?
0
```

When building future ansible versions, any untagged collections will cause
`ansible-build validate-tags-file` to fail.

### Enforcement

Prior to ansible 9.0.0a1, validation errors are treated as warnings.
In ansible 9.0.0a1 and onwards, these validation errors will be considered
release blockers.
The playbook will fail if any new collection releases are not properly tagged.

> **Note**
>
> It's recommended to run the release playbook with
> [`ANSIBLE_CALLBACK_RESULT_FORMAT=yaml`][5] so error messages and any other
> playbook output are more legible.


In case of violations, the release manager must preform the following steps:

1. First, the collection must be pinned to the previous tagged release in
   the `ansible-VERSION.build` file.

   Take the `community.docker` collection as an example.
   In `8/ansible-8.build`, it has

   ```
   community.docker: >=3.4.0,<4.0.0
   ```

   `,<4.0.0` would need to be replaced with `,<= RELEASE` where `RELEASE` is
   the previous tagged version.
   For instance, if community.docker 3.9.1 is released but not properly tagged
   while community.docker 3.9.0 is properly tagged, change the line to

   ```
   community.docker: >=3.4.0,<=3.9.0
   ```
2. Commit only the changed `ansible-VERSION.build` file:

    ```
    git add 8/ansible-8.build
    git commit -m "pin community.docker to previous release"
    ```
3. Rerun the release playbook.
   In this example, the ansible distribution will be built with
   community.docker 3.9.0 even though community.docker 3.9.1 is the latest
   version.
4. Proceed with the rest of the release process as normal.
   Commit the other changed files.
   The collection release PR should be applied using the `Rebase and merge`
   option (as opposed to `Squash and merge`) so the first commit can be more
   easily reverted when/if the collection fixes the issue.
5. The release manager or another community member needs to file an issue in
   the violating collection's issue tracker.
   This part should not block the current ansible package release,
   but the issue must have been filed before the following minor release.
   The following issue template can be used:

   ``` markdown
   Hi! As part of the ansible community package release process,
   we've determined that version {VERSION} of {COLLECTION} was released to
   Ansible Galaxy but not properly tagged in this Git repository.
   This violates the [repository management][1] section of the Collection Requirements:

   [1]: https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html#repository-management

    > Every collection MUST have a public git repository. Releases of the collection MUST be tagged in said repository. This means that releases MUST be `git tag`ed and that the tag name MUST exactly match the Galaxy version number. Tag names MAY have a `v` prefix, but a collection's tag names MUST have a consistent format from release to release.
    >
    > Additionally, collection artifacts released to Galaxy MUST be built from the sources that are tagged in the collection's git repository as that release. Any changes made during the build process MUST be clearly documented so the collection artifact can be reproduced.

    Until this issue is fixed,
    ansible package releases will contain {OLD VERSION},
    the previous version of this collection that was properly tagged.
    If the collection maintainers do not respond to this issue within a
    reasonable a amount of time,
    the collection is subject to [Removal from ansible][2].

    [2]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#collections-not-satisfying-the-collection-requirements

   ```
6. Post a comment in https://github.com/ansible-community/ansible-build-data/issues/223
   with a link to the issue.


[1]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
[2]: https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html#repository-management
[3]: https://github.com/ansible-community/antsibull/blob/main/playbooks/build-single-release.yaml
[4]: https://github.com/ansible-community/ansible-build-data/blob/main/7/ansible-7.5.0-tags.yaml
[5]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/default_callback.html#parameter-result_format
