# Ansible Collection Policies

This doc explains the necessary ansible-build-data changes to enforce
Ansible Community Steering Committee Policies such as [Removal from Ansible][1]
and [Repository management][2].

## Removal from Ansible

### Announce removal of a collection (deprecation)

If a collection should be removed in a future Ansible version,
its removal should be announced in all current major releases,
and should also be announced in the upcoming major release
(unless it is removed from that version - [see the next subsection for that](#removing-a-collection)).

To announce removal, removal metadata needs to be added to the collection metadata in `collection-meta.yaml`.
Assume you have the following collection metadata:
```yaml
collections:
  foo.bar:
    maintainers:
      - Foo Bar
    repository: https://github.com/ansible-collections/foo.bar
```
Then a `removal` subkey needs to be added to `foo.bar` with the following fields:

- `major_version`: the major Ansible version from which the collection shall be removed.

- `reason`: can be one of:

    1. `deprecated`: the collection has been deprecated by its maintainers.
       ([Official process](
         https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#removing-a-collection-that-has-been-explicitly-deprecated-or-abandoned-by-its-former-maintainers).)

    2. `considered-unmaintained`: the collection is considered unmaintained by the Steering Committee.
       ([Official process](
        https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#identifying-and-removing-an-unmaintained-collection-that-has-not-been-deprecated-by-its-maintainers).)

    3. `renamed`: the collection has been renamed.
       The new name of the collection should be specified in `new_name`.
       Also `redirect_replacement_major_version` should be added
       with the major Ansible release that will contain only deprecated redirects to the new collections.

        Note that in this case, `major_version` can have the special value `TBD`
        for when it is not clear when the old collection will eventually be removed from Ansible yet.

        ([Official process](
         https://github.com/ansible-community/ansible-build-data/?tab=readme-ov-file#renaming-a-collection).)

    4. `guidelines-violation`: the collection has been removed by the Steering Committee due to guidelines violation.
       Further details must be provided in `removal_text`.
       ([Official process](
        https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_package_removal.html#collections-not-satisfying-the-collection-requirements).)

    5. `other`: the collection has been removed for other reasons.
       Further explanation on why the collection will be removed must be provided in `removal_text`.

- `announce_version`: optional string to indicate in which release of this Ansible major version the removal should be announced.
  When adding a new removal, use the next version that will be used for a release.
  A corresponding changelog entry will automatically be added to this version in the Ansible changelog.

- `discussion`: optional string with an URL to the removal discussion in the forum.
  This link will be mentioned in the generated changelog entries and on the docsite.

The following are a few examples of how `removal` metadata can look:
```yaml
collections:
  foo.bar_deprecated:
    # In case a collection has been deprecated/abandoned by its maintainers.
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 20
      reason: deprecated
      announce_version: 11.2.0
      discussion: https://forum.ansible.com/t/.../
  foo.bar_unmaintained:
    # In case the Steering Committee decided that a collection is effectively unmaintained.
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 20
      reason: considered-unmaintained
      announce_version: 11.2.0
      discussion: https://forum.ansible.com/t/.../
  foo.bar_renamed:
    # Use this in case a collection has been renamed.
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 20  # can be TBD if not yet known
      reason: renamed
      new_name: foo.bar_new_name
      redirect_replacement_major_version: 13  # leave away if not yet known
      announce_version: 11.2.0
      discussion: https://forum.ansible.com/t/.../
  foo.bar_guidelines_violation:
    # In case the Steering Committe decided to remove the collection for guidelines violation.
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 20
      reason: guidelines-violation
      removal_text: >-
        Extra text that must specify what happened. Can use L(Ansible markup,
        https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_documenting.html#linking-within-module-documentation).
      announce_version: 11.2.0
      discussion: https://forum.ansible.com/t/.../
  foo.bar_other:
    # If the Steering Committee decides to remove a collection for a non-predefined reason.
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 20
      reason: other
      removal_text: >-
        Text that must specify why the collection was removed. Can use L(Ansible markup,
        https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_documenting.html#linking-within-module-documentation).
      announce_version: 11.2.0
      discussion: https://forum.ansible.com/t/.../
```

You can use `antsibull-build lint-build-data --data-dir /path/to/ansible-build-data/X/ X`
(where `X` is the major version)
to validate the entries.

### Removing a collection

If a collection should be removed from the upcoming Ansible major version,
for which a metadata directory already exists but for which feature freeze has not yet happened,
the collection needs to be removed from the build metadata.
Also note that the removal should be announced in existing major versions,
[see the previous section for details on that](#announce-removal-of-a-collection-deprecation).

First, remove the collection's entries from `ansible.in`, `ansible-X.build`, and if necessary, `ansible-X.constraints`.

Then the metadata in `collections-meta.yaml` needs to be updated:

1. For that, locate the collection in the `collections` list.
   Select the entry, copy it to the clipboard, and remove it from `collections`.

2. Locate the `removed_collections` list and the position where the collection should be inserted.
   Paste the copied entry from the clipboard.

3. If `removal` already exists, edit it as follows:

     - Replace `major_version` by `version`,
       and put in the exact Ansible version from which the collection is removed.
       **Note that this should not happen after the feature freeze!**

     - If `announce_version` is present, remove it.
       This removes the corresponding changelog entry if the Ansible changelog is regenerated,
       but that entry should not have been there
       unless the major version for removal got changed
       (in that case add an explicit manual entry to `changelog.yaml` if you want to keep the old entry).

4. If `removal` does not yet exist,
   create it [as described in the previous section](#announce-removal-of-a-collection-deprecation),
   with the changes as described in the previous point.

As an example, consider the following metadata entry:
```yaml
collections:
  foo.bar:
    repository: https://github.com/ansible-collections/foo.bar
```
This should be moved to `removed_collections` and changed as follows:
```yaml
removed_collections:
  foo.bar:
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      version: 20.0.0a1
      reason: deprecated
      discussion: https://forum.ansible.com/t/.../
```

You can use `antsibull-build lint-build-data --data-dir /path/to/ansible-build-data/X/ X`
(where `X` is the major version)
to validate the entries.

### Cancel deprecation of a collection

If a collection that is scheduled for removal in an upcoming major release should be kept,
the removal metadata needs to be adjusted.
The collection needs to be re-added in the build metadata for the upcoming major release
if it has already been removed from there;
[details for this can be found in the next subsection](#re-adding-a-already-removed-collection).

Locate the `removal` entry for the collection in `collection-meta.yaml`'s `collections` list,
and update it as follows:

1. If not there, add a `updates:` subkey.

2. Add an entry with `cancelled_version` (the Ansible release where the cancelation should be announced in the changelog)
   and `reason_text` (explanation), and optionally `discussion` (if a different discussion URL should be used).

This can look as follows:
```yaml
collections:
  foo.bar:
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 20
      reason: deprecated
      announce_version: 12.3.0
      discussion: https://forum.ansible.com/t/.../
      updates:
        - cancelled_version: 12.5.0
          reason_text: Maintenance of the collection has been taken over by L(someone else, https://...).
```

You can use `antsibull-build lint-build-data --data-dir /path/to/ansible-build-data/X/ X`
(where `X` is the major version)
to validate the entries.

### Re-adding a already removed collection

If a collection that has already been removed from the upcoming major version should be kept,
the removal metadata needs to be adjusted.
The removal needs to be canceled for previous major releases,
[details for this can be found in the prevous subsection](#cancel-deprecation-of-a-collection).

First, add the collection's entries to `ansible.in` and `ansible-X.build`.

Then the metadata in `collections-meta.yaml` needs to be updated:

1. For that, locate the collection in the `removed_collections` list.
   Select the entry, copy it to the clipboard, and remove it from `removed_collections`.

2. Locate the `collections` list and the position where the collection should be inserted.
   Paste the copied entry from the clipboard.

3. If not there, add a `updates:` subkey.

4. Remove `announce_version` from the main `removal` entry and add it to a new `updates` entry with key `removed_version`.

5. Add an `updates` entry with `readded_version` (the Ansible release where the re-add should be announced in the changelog)
   and `reason_text` (explanation), and optionally `discussion` (if a different discussion URL should be used).

As an example, consider the following metadata entry:
```yaml
removed_collections:
  foo.bar:
    maintainers:
      - Foo bar
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      version: 11.0.0a1
      reason: considered-unmaintained
      discussion: https://forum.ansible.com/t/.../
      announce_version: 10.0.0a1
```
This should be moved to `collections` and changed as follows:
```yaml
collections:
  foo.bar:
    maintainers:
      - Foo bar
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 11
      reason: considered-unmaintained
      discussion: https://forum.ansible.com/t/.../
      updates:
        - removed_version: 11.0.0a1
        - readded_version: 11.0.0b2
          reason_text: Maintenance of the collection has been taken over by L(another team, https://...).
```

You can use `antsibull-build lint-build-data --data-dir /path/to/ansible-build-data/X/ X`
(where `X` is the major version)
to validate the entries.

### Re-deprecating a collection

It can happen that a collection is scheduled for removal (deprecated)
that already was scheduled for removal before (or even has been removed before),
but the removal was canceled or the removed collection re-added.
In that case, updating the build metadata is a bit different
from [announcing its removal the first time](#announce-removal-of-a-collection-deprecation).

Then the metadata in `collections-meta.yaml` needs to be updated.
The collection should be in `collections` and already have a `removal` subkey,
and that should have a `updates` subkey.

Simply add a new entry there with:

1. `redeprecated_version`: the exact Ansible version when the re-deprecation should be announced.

2. `discussion`: optional URL if a new discussion thread is used on the forum.
   If not provided, `discussion` from the `removal` entry will be used.

3. `reason`: a reason why the collection has been re-deprecated.
   Can be one of `deprecated`, `considered-unmaintained`, `renamed`, `guidelines-violation`, or `other`.

4. `reason_text`: can only be provided if `reason` is not provided, or if it is one of `other` and `guidelines-violation`.
   It always must be provided if `reason` is one of `other` and `guidelines-violation`.

For example:
```
collections:
  foo.bar:
    maintainers:
      - Foo bar
    repository: https://github.com/ansible-collections/foo.bar
    removal:
      major_version: 11
      reason: considered-unmaintained
      discussion: https://forum.ansible.com/t/.../
      updates:
        - removed_version: 11.0.0a1
        - readded_version: 11.0.0b2
          reason_text: Maintenance of the collection has been taken over by L(another team, https://...).
        - redeprecated_version: 11.3.0
          discussion: https://...
          reason: guidelines-violation
          reason_text: The guideline L(XXX, https://...) was violated.
```

You can use `antsibull-build lint-build-data --data-dir /path/to/ansible-build-data/X/ X`
(where `X` is the major version)
to validate the entries.

## Repository management

### Background

From ansible 7.2.0 onwards, each release contains a `ansible-VERSION-tags.yaml`
data file in this repository.
This file contains a mapping of collections to their git repositories and the
git tag that corresponds to the version of a collection included in the ansible release.

The [Ansible release playbook][3] generates this tags data file during the
`antsibull-build prepare` step and later runs
the `antsibull-build validate-tags-file` command to validate it.

It is also possible to separately run `antsibull-build validate-tags-file`.
For example, to validate [the tags file for ansible 7.5.0][4], run

``` console
$ antsibull-build validate-tags-file 7/ansible-7.5.0-tags.yaml
cisco.nso 1.0.3 is not tagged in https://github.com/CiscoDevNet/ansible-nso
hpe.nimble 1.1.4 is not tagged in https://github.com/hpe-storage/nimble-ansible-modules
mellanox.onyx 1.0.0 is not tagged in https://github.com/ansible-collections/mellanox.onyx
$ echo $?
1
```

Since these collections were not properly tagged prior to this policy's
formalization, they are listed in [`7/validate-tags-ignores`][4a].
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

Prior to ansible 9.0.0a1,
the release playbook treats validation errors as warnings.
In ansible 9.0.0a1 and onwards,
these validation errors constitute release blockers.
The playbook will fail if any new collection releases are not properly tagged.

> **Note**
>
> It is recommended to run the release playbook with
> [`ANSIBLE_CALLBACK_RESULT_FORMAT=yaml`][5] so error messages and any other
> playbook output are more legible.


In case of violations, the release manager must preform the following steps:

1. First, the collection must be restricted to the previous tagged release in
   the `ansible-VERSION.constraints` file.

    Take the `community.docker` collection as an example. If its version 3.9.0
    was released and correctly tagged, and 3.9.1 was released but not correctly
    tagged, add

    ```
    community.docker: <3.9.1
    ```

2. Commit only the changed `ansible-VERSION.constraints` file:

    ```
    git add 8/ansible-8.constraints
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
    Hi! As part of the ansible community package release process, we've determined that version {VERSION} of {COLLECTION} was released to Ansible Galaxy but not properly tagged in this Git repository.
    This violates the [repository management][1] section of the Collection Requirements:

    [1]: https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html#repository-management

    > Every collection MUST have a public git repository. Releases of the collection MUST be tagged in said repository. This means that releases MUST be `git tag`ed and that the tag name MUST exactly match the Galaxy version number. Tag names MAY have a `v` prefix, but a collection's tag names MUST have a consistent format from release to release.
    >
    > Additionally, collection artifacts released to Galaxy MUST be built from the sources that are tagged in the collection's git repository as that release. Any changes made during the build process MUST be clearly documented so the collection artifact can be reproduced.

    Until this issue is fixed, ansible package releases will contain {OLD VERSION}, the previous version of this collection that was properly tagged. If the collection maintainers do not respond to this issue within a reasonable amount of time, the collection is subject to [Removal from ansible][2].

    [2]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst#collections-not-satisfying-the-collection-requirements

    ```

6. Post a comment in <https://github.com/ansible-community/ansible-build-data/issues/223>
   with a link to the issue.


[1]: https://github.com/ansible-collections/overview/blob/main/removal_from_ansible.rst
[2]: https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html#repository-management
[3]: https://github.com/ansible-community/antsibull-build/blob/main/playbooks/build-single-release.yaml
[4]: https://github.com/ansible-community/ansible-build-data/blob/main/7/ansible-7.5.0-tags.yaml
[4a]: https://github.com/ansible-community/ansible-build-data/blob/main/7/validate-tags-ignores
[5]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/default_callback.html#parameter-result_format
