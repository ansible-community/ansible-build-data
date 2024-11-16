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

1. Determine the current major version and next major version:

    ``` sh
    CURRENT_MAJOR_VERSION=11
    NEXT_MAJOR_VERSION=12
    ```

2. Create the major version directory:

    ``` sh
    mkdir "${NEXT_MAJOR_VERSION}/"
    ```

3. Copy over the `ansible.in` and `collection-meta.yaml` files:

    ``` sh
    cp "${CURRENT_MAJOR_VERSION}/ansible.in" "${CURRENT_MAJOR_VERSION}/collection-meta.yaml" \
       "${NEXT_MAJOR_VERSION}/"
    ```

4. Symlink `${CURRENT_MAJOR_VERSION}.0.0`'s deps file to
   `${NEXT_MAJOR_VERSION}/ancestor.deps`:

    ``` sh
    ln -sr "${CURRENT_MAJOR_VERSION}/ansible-${CURRENT_MAJOR_VERSION}.0.0.deps" \
       "${NEXT_MAJOR_VERSION}/ancestor.deps"
    ```

5. Create a stub `changelog.yaml` file:

    ``` sh
    cat <<EOF >${NEXT_MAJOR_VERSION}/changelog.yaml
    ---
    ancestor: ${CURRENT_MAJOR_VERSION}.0.0
    releases: {}
    EOF
    ```

6. Create a blank `validate-tags-ignores` file:

    ``` sh
    touch "${NEXT_MAJOR_VERSION}/validate-tags-ignores"
    ```

7. Create a blank `ansible-${NEXT_MAJOR_VERSION}.constraints` file:

    ``` sh
    touch "${NEXT_MAJOR_VERSION}/ansible-${NEXT_MAJOR_VERSION}.constraints"
    ```

    You might need to fill this with some initial data.

8. Add the next major version to ansible-build-data's CI:

    Open `.github/workflows/antsibull-build.yml` and the following block to the
    matrix:

    ``` yaml
    - name: Ansible ${NEXT_MAJOR_VERSION}
      ansible_version: ${NEXT_MAJOR_VERSION}.99.0
      ansible_major_version: ${NEXT_MAJOR_VERSION}
    ```

9. Update `collection-meta.yaml` and `ansible.in`:

    1. Find all collection entries from `collections` in `collections-meta.yaml`
       that have a `removal` entry with `major_version` equal to `${NEXT_MAJOR_VERSION}`.

        - If the `removal` entry has an `updates` and the last entry is about keeping them (`readded_version` or `cancelled_version`),
          remove the `removal` entry completely.

        - Otherwise, cut out the collection's entry and paste it into a temporary buffer / file.

    2. For every cut out metadata entry,
       remove the corresponding entry in `ansible.in`.

    3. For every cut out metadata entry,
       find the correct place in `removed_collections` in `collections-meta.yaml`
       to insert the removed part from `collections-meta.yaml` and paste the entry there.
       Modify the entry as follows:

        - Replace `major_version: ${NEXT_MAJOR_VERSION}` by `version: ${NEXT_MAJOR_VERSION}.0.0a1`.

        - Remove `announce_version` if present.

        - Remove `updates` if present.

10. Validate build data:

    ```sh
    antsibull-build lint-build-data --data-dir "${NEXT_MAJOR_VERSION}" "${NEXT_MAJOR_VERSION}"
    ```

11. Commit the changes:

    ``` sh
    git add "${NEXT_MAJOR_VERSION}" .github/workflows/antsibull-build.yml
    ```

12. Submit a PR against [the ansible-build-data repository](https://github.com/ansible-community/ansible-build-data/).
