# How to release a new version of the Ansible Community Package - Automated Release Process

## Preamble

This document describes the (mostly) automated ansible community package release process.
The automated processes uses GitHub Actions to automate the [manual release process](release-process.md).

!!! note
    Throughout this page, placeholder values in code blocks are formatted as
    `${PLACEHOLDER_VALUE}` where `PLACEHOLDER_VALUE` describes the value to specify.


## Trigger the workflow

1. Trigger [the automated workflow](https://github.com/ansible-community/ansible-build-data/actions/workflows/ansible-release.yml) on the **Actions** tab of the repository and specify the release version, such as 11.2.0, and the major version, such as 11.
   The process will create a PR in the [`ansible-build-data` repository](https://github.com/ansible-community/ansible-build-data/), and wait for approval before continuing with uploading the package to PyPI.
   All users with commit rights in the `ansible-build-data` repository will be informed with a notification once the approval is needed.
   The notification includes a link to the page where the upload step can be approved.

2. Check out the PR in your `ansible-build-data` clone and copy the updated porting guide from its `${MAJOR_VERSION}` directory into the [`docs/docsite/rst/porting_guides/`](https://github.com/ansible/ansible-documentation/tree/devel/docs/docsite/rst/porting_guides/) directory of the [`ansible-documentation` repository](https://github.com/ansible/ansible-documentation/).
   Create a PR for updating the porting guide for the `devel` branch of `ansible-documentation`.

3. After both PRs (in `ansible-build-data` and `ansible-documentation`) are approved, merge the `ansible-build-data` PR and approve the next workflow step (**in this order!** the next steps of the workflow require the PR to be merged!).
   This will upload the package to PyPI and tag the release in `ansible-build-data`.

4. Merge the porting guide PR, and backport it to the latest `stable-x` branches down to the ansible-core version that is included in the Ansible release.

5. Announce the release on the Forum, Matrix, and the mailing list by running the following command in the `${MAJOR_VERSION}` directory of the `ansible-build-data` checkout:
    ```
    antsibull-build announcements --send --data-dir . ${VERSION}
    ```
