#!/usr/bin/env python

from __future__ import annotations

import msgspec

from .word_annotations import WordAnnotations

###############################################################################


class Word(msgspec.Struct):
    start_time: float
    end_time: float
    text: str
    annotations: WordAnnotations | None = None
