# transcript-file-format

[![Build Status](https://github.com/CouncilDataProject/transcript-file-format/workflows/CI/badge.svg)](https://github.com/CouncilDataProject/transcript-file-format/actions)
[![Documentation](https://github.com/CouncilDataProject/transcript-file-format/workflows/Documentation/badge.svg)](https://CouncilDataProject.github.io/transcript-file-format)

A generalized transcript file format and utilities for parsing.

---

## Installation

**Stable Release:** `pip install transcript-file-format`<br>
**Development Head:** `pip install git+https://github.com/CouncilDataProject/transcript-file-format.git`

## Quickstart

```python
from transcript_file_format import Transcript, Sentence, to_json, from_json

# Create a transcript with metadata
t = Transcript(
    sentences=[
        Sentence(
            index=0,
            start_time=0.1,
            end_time=1.2,
            text="hello world",
        ),
        Sentence(
            index=1,
            start_time=1.4,
            end_time=2.6,
            text="my name is eva",
        ),
    ],
    generator="Hand Written by Eva",
    session_datetime="2023-04-05",
    created_datetime="2023-04-06",
)

# Store to JSON
to_json(t, "example.json")

# Read from JSON back to object
t = from_json("example.json")
# Transcript(sentences=[...] (n=2), generator='Hand Written by Eva', confidence=None, session_datetime='2023-04-05', created_datetime='2023-04-06', annotations=None)
```

## Documentation

For full package documentation please visit [CouncilDataProject.github.io/transcript-file-format](https://CouncilDataProject.github.io/transcript-file-format).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**MIT License**
