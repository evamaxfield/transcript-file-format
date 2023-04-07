#!/usr/bin/env python

from __future__ import annotations

import msgspec

from ...custom_types import JSONCompatType

###############################################################################


class SpeakerAnnotation(msgspec.Struct):
    name: str
    meta: JSONCompatType | None = None
