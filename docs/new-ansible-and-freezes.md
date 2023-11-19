# New Ansible Releases and Freezes

## Preamble

Releasing new Ansible major versions and frozen releases requires some special
handling.
For information about the general release process,
see [Ansible Release Process](release-process.md).

## Setting up for a new major release

<!-- TODO: Write a script, playbook, or antsibull-build subcommand to automate this -->

After the release of `X.0.0`, it is necessary to create the directory
structure for Ansible `X+1`.

1. Determine the current major version and next major version

    ``` sh
    CURRENT_MAJOR_VERSION=9
    NEXT_MAJOR_VERSION=10
    ```

2. Create the major version directory

    ``` sh
    mkdir "${NEXT_MAJOR_VERSION}/"
    ```

3. Copy over the `ansible.in` and `collection-meta.yaml` files

    ``` sh
    cp "${CURRENT_MAJOR_VERSION}/ansible.in" "${CURRENT_MAJOR_VERSION}/collection-meta.yaml" \
       "${NEXT_MAJOR_VERSION}/"
    ```

4. Symlink `${CURRENT_MAJOR_VERSION}.0.0`'s deps file to
   `${NEXT_MAJOR_VERSION}/ancestor.deps`

    ``` sh
    ln -sr "${CURRENT_MAJOR_VERSION}/${CURRENT_MAJOR_VERSION}.0.0.deps" \
       "${NEXT_MAJOR_VERSION}/ancestor.deps"
    ```

5. Create a stub `changelog.yaml` file

    ``` sh
    cat <<EOF >${NEXT_MAJOR_VERSION}/changelog.yaml
    ---
    ancestor: ${CURRENT_MAJOR_VERSION}.0.0
    releases: {}
    EOF
    ```

6. Create a blank `validate-tags-ignores` file

    ``` sh
    touch "${NEXT_MAJOR_VERSION}/validate-tags-ignores"
    ```

7. Add the next major version to ansible-build-data's CI

    Open `.github/workflows/antsibull-build.yml` and the following block to the
    matrix:

    ``` yaml
    - name: Ansible ${NEXT_MAJOR_VERSION}
      ansible_version: ${NEXT_MAJOR_VERSION}.99.0
      ansible_major_version: ${NEXT_MAJOR_VERSION}
    ```

8. Commit the changes

    ``` sh
    git add "${NEXT_MAJOR_VERSION}" .github/workflows/antsibull-build.yml
    ```

9. Submit a PR against ansible-build-data


## Freeze release

<!--
TODO: Improve the release playbook to support this case without requiring extra steps.
-->

Beyond the regular [Ansible Release Process](release-process.md), X.Y.0
releases require special handling before running the release playbook.

1. Determine the previous and the current releases

    ``` sh
    MAJOR_VERSION=9
    VERSION=9.0.0
    PREVIOUS_VERSION=9.0.0rc1
    ```

2. Set up your Git clones and release venv as outlined in the [Ansible Release Process](release-process.md) document.

3. Copy over the previous release's deps and galaxy files.

    ``` sh
    cp "ansible-${PREVIOUS_VERSION}.yaml" "ansible-${VERSION}.yaml"
    cp "ansible-${PREVIOUS_VERSION}.deps" "ansible-${VERSION}.deps"
    ```

4. Edit the current ansible version in the deps file

    ``` sh
    sed -i "s|^_ansible_version:.*$|_ansible_version: ${VERSION}|" \
       "ansible-${VERSION}.deps"
    ```

5. Add a changelog entry for the new release

    Open `${MAJOR_VERSION}/changelog.yaml` and the following block to the
    releases table:

    ``` yaml
     ${VERSION}:
       changes:
         release_summary: 'Release Date: ${RELEASE_DATE}
           `Porting Guide <https://docs.ansible.com/ansible/devel/porting_guides.html>`_'
       release_date: '${RELEASE_DATE}'
    ```

    The release date should be formatted as `YYYY-MM-DD`.

6. Manually update specific collection versions if needed.

    In some cases, it may be necessary to update certain collections if, for
    example, a serious bug is found is one of the collections.
    In that case, open up the deps and galaxy files copied over in the step 2
    and change the versions for the collections in question.
    Make sure that the versions in both files are consistent.

7. Generate the tags data file

    ``` sh
    antsibull-build validate-tags \
        --data-dir . \
        --ignores-file validate-tags-ignores \
        --output "ansible-${VERSION}-tags.yaml" \
        "${VERSION}"
    ```

8. Run the the release playbook as outlined in [Ansible Release Process](release-process.md).
   Make sure to use pass `-e antsibull_data_reset=false` to preserve the
   ansible-build-data modifications.
