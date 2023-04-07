#!/usr/bin/env python

from __future__ import annotations

from typing import Self

import msgspec

from ..sentence.sentence import Sentence
from .transcript_annotations import TranscriptAnnotations

###############################################################################

class Transcript(msgspec.Struct):
    """
    A transcript object.

    Contains list of Sentence objects along with additional metadata.
    """

    sentences: list[Sentence]
    generator: str | None = None
    confidence: float | None = None
    session_datetime: str | None = None
    created_datetime: str | None = None
    annotations: TranscriptAnnotations | None = None

    def __repr__(self: Self) -> str:
        """Print shortform version of transcript."""
        output = "Transcript("

        # Use vars to maintain subclassing
        for attr in self.__struct_fields__:
            val = getattr(self, attr)

            # Truncate sentences
            if attr == "sentences":
                output += f"{attr}=[...] (n={len(val)}), "

            # Add quotes for strings
            elif type(val) == str:
                output += f"{attr}='{val}', "

            else:
                output += f"{attr}={val}, "

        # Remove last comma and space and close parentheses
        return (output[:-2] + ")").strip()
    
    