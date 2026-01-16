# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2023 Maxwell G <maxwell@gtmx.me

from __future__ import annotations

import nox


@nox.session
def mkdocs(session: nox.Session):
    session.install("-r", "docs-requirements.txt")
    session.run("mkdocs", *(session.posargs or ["build"]))


@nox.session
def lint(session: nox.Session):
    session.install("yamllint")
    session.run("yamllint", ".")


@nox.session
def zizmor(session: nox.Session):
    args: list[str] = list(session.posargs)
    if not any(a.startswith("--persona") for a in args):
        args.append("--persona=regular")

    session.install("zizmor")
    session.run("zizmor", *args, ".github/workflows")
