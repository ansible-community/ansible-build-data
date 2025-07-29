# How to release a new version of the Ansible Community Package — Automated Release Process

## Preamble

This document describes the (mostly) automated ansible community package
release process. The automated processes uses GitHub Actions to automate the
[manual release process](release-process.md).

!!! note
    Throughout this page, placeholder values in code blocks are formatted as
    `${PLACEHOLDER_VALUE}` where `PLACEHOLDER_VALUE` describes the value to
    specify.

## Setup for the release

### Credentials

Note that most of the following items cannot be done by yourself, but need someone from the Ansible community team to assign them to you. You need to earn some trust first before this will happen.

- Become a member of the [ansible-build-data](https://github.com/ansible-community/ansible-build-data) repo.
- Become member of the Ansible Release Management working group on Github.
- For making the announcements relating to releases, please join the following Matrix rooms:
    - [`#release-management:ansible.com`](https://matrix.to/#/#release-management:ansible.com)
    - [`#community:ansible.com`](https://matrix.to/#/#community:ansible.com)
    - [`#packaging:ansible.com`](https://matrix.to/#/#packaging:ansible.com)
    - [`#social:ansible.com`](https://matrix.to/#/#social:ansible.com) (mention `@newsbot`)
- Join Release Management Working Group in [Ansible Forum](https://forum.ansible.com/g/release-managers).


### Read about the following

- [Trusted Publisher in PyPI](https://docs.pypi.org/trusted-publishers/).
- [Examine the GitHub Actions release workflow](https://github.com/ansible-community/ansible-build-data/blob/main/.github/workflows/ansible-release.yml).
- [Talk on Using Trusted Publishing to Ansible release](https://docs.pypi.org/trusted-publishers/)
- Ask and show intention to be the Release Manager in the release-management working group.
- Shadow the release manager for 2 releases.
- [Release Roadmap](https://docs.ansible.com/ansible/devel/roadmap)

### Process summary

-  Communicate with the Community about the start and the progress on the [#release-management:ansible.com Matrix channel](https://matrix.to/#/#release-management:ansible.com).
-  Follow the release workflow as mentioned below.

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

2. To create the porting guide PR in the ansible-documentation repository, trigger [the automated
   workflow](https://github.com/ansible/ansible-documentation/actions/workflows/release-porting-guide.yml)
   on the **Actions** tab of the repository. This workflow has the following inputs:

    * **Release Branch name**. Specify the name of the branch from the newly created [ansible-build-data](https://github.com/ansible-community/ansible-build-data/) PR for the release, for example: `refs/pull/576/merge`.
    * **Exact release version**. Specify a release version such as `11.2.0` or `12.0.0rc1`.
    * **Use the workflow from** the **Branch: devel** `devel` is selected as the branch by default. Do not edit this while doing the release. This option is there to test the workflow itself.

   The process will create a PR in the [`ansible-documentation`
   repository](https://github.com/ansible/ansible-documentation/).The release manager needs to check the Porting Guide PR and change the status to 'ready to review.' Afterwards, the [ansible-community/release-management-wg
    group](https://github.com/orgs/ansible-community/teams/release-management-wg)[^1] needs to be informed in [matrix](#release-management:ansible.com) about the PR. (pinged manually with a message like this - "There is a [Porting Guide PR](PR url), can someone please go ahead and have a look, review and merge it.")


3. After both PRs (in `ansible-build-data` and `ansible-documentation`) are
   approved, merge the `ansible-build-data` PR and approve the next workflow
   step (**in this order!** the next steps of the workflow require the PR to be
   merged!). This will upload the package to PyPI and tag the release in
   `ansible-build-data`.

4. Merge the porting guide PR, and request backports to the latest `stable-x`
   branches down to the ansible-core version that is included in the Ansible
   release. Documentation mantainers can add the appropriate backport labels to enable these automatically.

5. Make sure that you have installed [`antsibull-build`](https://pypi.org/project/antsibull-build/)
   and a supported clipboard library. You can do that like this:

    ```
    pip install antsibull-build[clipboard]
    ```

6. Then announce the release on the Forum and Matrix by
   running the following command in the `${MAJOR_VERSION}` directory of the
   `ansible-build-data` checkout:

    ```
    antsibull-build announcements --send --data-dir . ${VERSION} [ --end-of-life ]
    ```

    The `--end-of-life` flag should be added if this is the final release for the
    `${MAJOR_VERSION}` major release train.

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
new major release](new-ansible.md#setting-up-for-a-new-major-release).
