# Ansible Release Process

## Preamble

This document describes the ansible community package release process.

!!! note
    Throughout this page, placeholder values in code blocks are formatted as
    `${PLACEHOLDER_VALUE}` where `PLACEHOLDER_VALUE` describes the value to fill in.


## Set up container

Release managers may choose to preform the following steps inside a podman or
docker container created from the [`docker.io/library/python:3.10`][container]
image.
Make sure to mount your working directory as a volume so you don't have to set
up new repository clones every time.

```
podman run --name ansible-release -v ${PERSISTENT_DIRECTORY}:/pwd:z -w /pwd -ti docker.io/library/python:3.10 bash
```


## Set up repository clones

First, you need to set up ansible-build-data and antsibull repository clones.
This only needs to be done once.

1. [Fork][abd-fork] the [ansible-build-data] repository.

2. Checkout the antsibull and ansible-documentation repositories
   and change into antsibull.

    ```
    git clone https://github.com/ansible/ansible-documentation
    git clone https://github.com/ansible-community/antsibull
    cd antsibull
    ```

3. Checkout ansible-build-data and configure your fork.

    To checkout the repository run

    ```
    mkdir build
    cd build
    git clone https://github.com/ansible-community/ansible-build-data
    cd ansible-build-data
    ```

    Then, configure your fork.
    This guide uses your Github username as the fork remote name.

    ```
    git remote add ${GH_USERNAME} https://github.com/${GH_USERNAME}/ansible-build-data
    git fetch ${GH_USERNAME} -v
    ```

## Perform release process

1. Change into the antsibull checkout.
   Make sure you have the `main` branch checked out
   and run `git pull` to update to the latest commit.

2. Create a clean virtual environment for the release process.

    ```
    rm -rf release-venv
    python3 -m venv release-venv
    . ./release-venv/bin/activate
    python3 -m pip install -U pip
    ```

    Install the `antsibull`, `ansible-core`, and `twine` python packages,
    as well as the community.general collection.

    ```
    python3 -m pip install antsibull ansible-core twine
    ansible-galaxy collection install --force community.general
    ```

3. Run the [ansible release playbook][release-playbook]
   with the appropriate options.
   You can see the [argument spec][release-playbook-args]
   for a full breakdown, but this describes the basic usage.

    ```
    export ANSIBLE_CALLBACK_RESULT_FORMAT=yaml
    ansible-playbook playbooks/build-single-release.yaml -e antsibull_ansible_version=${VERSION}
    ```

    !!! note
        When building ansible versions greater than 9.0.0a1,
        `Validate tags file` task failures will fail the release playbook instead
        of warning and moving on.
        See [policies.md][tagging-enforcement] for how to proceed if this step fails.

4. Commit the changes and push them to your fork.

    You can run the following commands to do so

    ```
    cd build/ansible-build-data
    git switch -c release-${VERSION}
    git add ${MAJOR_VERSION}/
    git commit -m "Ansible ${VERSION}: Dependencies, changelog and porting guide"
    git push -u ${GH_USERNAME} release-${VERSION}
    ```

    Then, submit a pull request against ansible-build-data upstream.

5. Submit a PR to ansible/ansible-documentation to add the new porting guide to the docsite.
   Copy the porting guide to the ansible docsite directory
   in your ansible checkout with the following command

    ```
    cp ${MAJOR_VERSION}/porting_guide_${MAJOR_VERSION}.rst ../ansible-documentation/docs/docsite/rst/porting_guides/
    ```

    switch to the ansible checkout,
    commit and push the changes,
    and then submit a PR as you normally would.
    You can use `Add Ansible community ${VERSION} porting guide` as the commit message.

6. Once the ansible-build-data PR has been merged,
   publish the build artifacts to PyPI.
   From the antsibull repository root, run

    ```
    twine upload build/ansible-${VERSION}.tar.gz build/ansible-${VERSION}*.whl
    ```

7. Tag the release commit in the ansible-build-data repository.

    ```
    cd build/ansible-build-data
    git switch main
    git pull
    git tag ${VERSION} ${MERGED_PR_COMMIT_HASH} -a -m "Ansible ${VERSION}: Changelog, Porting Guide and Dependent Collection Details"
    git push --follow-tags
    ```

8. Announce the release on Matrix and the mailing list.
   TODO: Move announcement templates into this repository.
   Release managers can copy and paste the previous release's announcement for
   now.
   Make sure to change the version numbers and sha256sum in the announcement
   text.

[container]: https://hub.docker.com/_/python
[abd-fork]: https://github.com/ansible-community/ansible-build-data/fork
[ansible-build-data]: https://github.com/ansible-community/ansible-build-data
[release-playbook]: https://github.com/ansible-community/antsibull/blob/main/playbooks/build-single-release.yaml
[release-playbook-args]: https://github.com/ansible-community/antsibull/blob/main/roles/build-release/meta/argument_specs.yml
[tagging-enforcement]: https://github.com/gotmax23/ansible-build-data/blob/docs/docs/policies.md#enforcement
