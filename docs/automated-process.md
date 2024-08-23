# How to release a new version of the Ansible Community Package — Automated Release Process

## Preamble

This document describes the (mostly) automated ansible community package
release process. The automated processes uses GitHub Actions to automate the
[manual release process](release-process.md).

!!! note
    Throughout this page, placeholder values in code blocks are formatted as
    `${PLACEHOLDER_VALUE}` where `PLACEHOLDER_VALUE` describes the value to
    specify.


## Trigger the workflow

1. Trigger [the automated
   workflow](https://github.com/ansible-community/ansible-build-data/actions/workflows/ansible-release.yml)
   on the **Actions** tab of the repository. This workflow has multiple inputs.
   The most important is the release version, such as `11.2.0` or `12.0.0rc1`.
   This always has to be specified.

    The following additional inputs are required for special releases. Generally
    you do not need to pass them and can rely on their defaults. Cases where you
    need these inputs are described in the [Special builds](#special-builds)
    section below.

    * You can optionally decide whether to preserve existing `.deps` files.
      The default is to regenerate them.
    * You can optionally decide whether the `.build` file should be regenerated
      during alpha and beta-1 releases.
    * You can also specify an existing branch in the [`ansible-build-data`
      repository](https://github.com/ansible-community/ansible-build-data/) to
      create the PR on.

    The process will create a PR in the [`ansible-build-data`
    repository](https://github.com/ansible-community/ansible-build-data/).
    Afterwards, it will wait for approval before continuing with uploading the
    package to PyPI. All users in the [ansible-community/release-management-wg
    group](https://github.com/orgs/ansible-community/teams/release-management-wg)[^1]
    will be informed with a notification once the approval is needed.
    The notification includes a link to the page where the upload step can be
    approved.

2. Check out the PR in your `ansible-build-data` clone and copy the updated
   porting guide from its `${MAJOR_VERSION}` directory into the
   [`docs/docsite/rst/porting_guides/`](https://github.com/ansible/ansible-documentation/tree/devel/docs/docsite/rst/porting_guides/)
   directory of the [`ansible-documentation`
   repository](https://github.com/ansible/ansible-documentation/). Create a
   PR for updating the porting guide for the `devel` branch of
   `ansible-documentation`.

3. After both PRs (in `ansible-build-data` and `ansible-documentation`) are
   approved, merge the `ansible-build-data` PR and approve the next workflow
   step (**in this order!** the next steps of the workflow require the PR to be
   merged!). This will upload the package to PyPI and tag the release in
   `ansible-build-data`.

4. Merge the porting guide PR, and backport it to the latest `stable-x`
   branches down to the ansible-core version that is included in the Ansible
   release.

5. Make sure that you have installed [`antsibull`](https://pypi.org/project/antsibull/)
   and a supported clipboard library. You can do that like this:

    ```
    pip install antsibull[clipboard]
    ```

6. Then announce the release on the Forum and Matrix by
   running the following command in the `${MAJOR_VERSION}` directory of the
   `ansible-build-data` checkout:

    ```
    antsibull-build announcements --send --data-dir . ${VERSION}
    ```

    This will open your default browser to do the announcement on the forum.
    It will also tell you where to announce this on Matrix,
    ask for the URL of the forum thread,
    and create a suitable text in your clipboard that you can copy to Matrix.

[^1]: This group is configured as "Required reviewers" for the "Configure pypi"
      build environment in GitHub Actions of the `ansible-build-data` repository.

## Special builds

### Builds with a specific release summary other than the default one

Sometimes you want to use a different release summary than the default one.
For example for the Ansible 9.5.1 release, we included some text that explained
why the release has version 9.5.1 and not 9.5.0.

For this, create a new branch in `ansible-build-data`. Add a `release_summary`
changelog entry for the new release to the `changelog.yaml` file in the major
version's directory. Make sure to follow the same basic structure of the version's
record in `changelog.yaml`. This can look as follows:
```yaml
releases:
  ...
  12.3.4:
    changes:
      release_summary: |
        Release Date: 2024-05-14

        Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_

        This is a special release because of ...
```

After that, you can start the automated workflow. You need to set the following option
next to the release version:

1. Set `existing-branch` to the branch you pushed to the `ansible-build-data`
   repository.

### Additional release candidates (rc2 etc.)

For these release candidates, you only want to bump very specific collection
versions, and not use new bugfix releases of potentially all included collections.

For this, create a new branch in `ansible-build-data` where you copy the `.deps`
file of the previous release candidate to the location of the `.deps` file of the
planned release. Then you modify the new `.deps` file with the version updates
you plan to make and update `_ansible_version`.

After that, you can start the automated workflow. You need to set the following options
next to the release version:

1. Set `preserve-deps` to `true`;

2. Set `existing-branch` to the branch you pushed to the `ansible-build-data`
   repository.

### New major release (x.0.0)

The new major release should include exactly the same dependencies as the last
release candidate.

For this, create a new branch in `ansible-build-data` where you copy the `.deps`
file of the last release candidate to the location of the `.deps` file of the
planned major release. Update `_ansible_version` in the new `.deps` file, but don't
change it in any other way.

After that, you can start the automated workflow. You need to set the following options
next to the release version:

1. Set `preserve-deps` to `true`;

2. Set `existing-branch` to the branch you pushed to the `ansible-build-data`
   repository.

When the new major release has been done, remember to prepare the directory for
the next major Ansible release. How to do this is described in [Setting up for a
new major release](new-ansible-and-freezes.md#setting-up-for-a-new-major-release).
