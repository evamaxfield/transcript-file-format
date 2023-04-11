#!/usr/bin/env python

from __future__ import annotations

import msgspec

from ..word.word import Word
from .sentence_annotations import SentenceAnnotations

###############################################################################


class Sentence(msgspec.Struct):
    start_time: float
    end_time: float
    text: str
    words: list[Word] | None = None
    annotations: SentenceAnnotations | None = None
