#!/usr/bin/env python

from __future__ import annotations

import msgspec

###############################################################################


class SectionAnnotation(msgspec.Struct):
    """
    A section or portion of the dialogue, meeting.

    I.e. in a meeting of a council or board a "section" of the meeting
    might be the "Call to Order" section.
    """
    name: str
    start_sentence_index: int
    stop_sentence_index: int
    generator: str
    description: str | None = None