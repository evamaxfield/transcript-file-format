#!/usr/bin/env python

from __future__ import annotations

from pathlib import Path

###############################################################################

JSONCompatType = dict[str, str | int | float | bool | dict | list | None]
PathLike = str | Path