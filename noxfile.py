from __future__ import annotations

import nox


@nox.session
def mkdocs(session: nox.Session):
    session.install("-r", "docs-requirements.txt")
    session.run("mkdocs", *(session.posargs or ["build"]))
