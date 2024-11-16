# New Ansible Releases

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
    ln -sr "${CURRENT_MAJOR_VERSION}/ansible-${CURRENT_MAJOR_VERSION}.0.0.deps" \
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

7. Create a blank `ansible-${NEXT_MAJOR_VERSION}.constraints` file

    ``` sh
    touch "${NEXT_MAJOR_VERSION}/ansible-${NEXT_MAJOR_VERSION}.constraints"
    ```

    You might need to fill this with some initial data.

8. Add the next major version to ansible-build-data's CI

    Open `.github/workflows/antsibull-build.yml` and the following block to the
    matrix:

    ``` yaml
    - name: Ansible ${NEXT_MAJOR_VERSION}
      ansible_version: ${NEXT_MAJOR_VERSION}.99.0
      ansible_major_version: ${NEXT_MAJOR_VERSION}
    ```

9. Commit the changes

    ``` sh
    git add "${NEXT_MAJOR_VERSION}" .github/workflows/antsibull-build.yml
    ```

10. Submit a PR against ansible-build-data
