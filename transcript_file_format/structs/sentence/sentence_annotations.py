#!/usr/bin/env python

from __future__ import annotations

import msgspec

from ...custom_types import JSONCompatType
from .speaker_annotation import SpeakerAnnotation

###############################################################################


class SentenceAnnotations(msgspec.Struct):
    speaker: SpeakerAnnotation | None = None
    meta: JSONCompatType | None = None
    custom: JSONCompatType | None = None
