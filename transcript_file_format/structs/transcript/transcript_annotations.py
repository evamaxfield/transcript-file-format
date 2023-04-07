#!/usr/bin/env python

from __future__ import annotations

import msgspec

from ...custom_types import JSONCompatType
from .section_annotation import SectionAnnotation

###############################################################################


class TranscriptAnnotations(msgspec.Struct):
    """Annotations that affect the whole transcript."""

    sections: list[SectionAnnotation] | None = None
    meta: JSONCompatType | None = None
    custom: JSONCompatType | None = None
