# Automated Ansible Release Process

## Preamble

This document describes the (mostly) automated ansible community package release process.

!!! note
    Throughout this page, placeholder values in code blocks are formatted as
    `${PLACEHOLDER_VALUE}` where `PLACEHOLDER_VALUE` describes the value to fill in.


## Trigger the workflow

1. Trigger the workflow https://github.com/ansible-community/ansible-build-data/actions/workflows/ansible-release.yml and fill in the release version (like 11.2.0) and the major version (like 11).
   The process will create a PR in the `ansible-build-data` repository, and wait for approval before continuing with uploading the package to PyPI.

2. Check out the PR in your `ansible-build-data` checkout and copy the updated porting guide into the `ansible-documentation` repository.
   Create a PR for updating the porting guide for the `devel` branch of `ansible-documentation`.

3. Once both PRs (in `ansible-build-data` and `ansible-documentation`) are approved, merge the `ansible-build-data` PR and approve the next workflow step.
   This will upload the package to PyPI and tag the release in `ansible-build-data`.

4. Merge the porting guide PR, and backport it to the latest `stable-x` branches down to the ansible-core version that is included in this Ansible release.

5. Announce the release on the Forum, Matrix, and the mailing list.

   For that, run the following in the `${MAJOR_VERSION}` directory of the `ansible-build-data` checkout:
   ```
    antsibull-build announcements --send --data-dir . ${VERSION}
   ```
