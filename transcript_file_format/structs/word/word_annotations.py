#!/usr/bin/env python

from __future__ import annotations

import msgspec

from ...custom_types import JSONCompatType

###############################################################################


class WordAnnotations(msgspec.Struct):
    meta: JSONCompatType | None = None
    custom: JSONCompatType | None = None
