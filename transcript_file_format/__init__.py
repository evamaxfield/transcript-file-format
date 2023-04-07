"""Top-level package for transcript_file_format."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("transcript-file-format")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Eva Maxfield Brown"
__email__ = "evamaxfieldbrown@gmail.com"


import msgspec

from .custom_types import PathLike
from .structs.sentence.sentence import Sentence  # noqa: F401
from .structs.transcript.transcript import Transcript  # noqa: F401
from .structs.word.word import Word  # noqa: F401


def from_json(path: PathLike) -> Transcript:
    with open(path, "rb") as open_f:
        return msgspec.json.decode(open_f.read(), type=Transcript)
    

def to_json(transcript: Transcript, path: PathLike) -> None:
    with open(path, "wb") as open_f:
        open_f.write(msgspec.json.encode(transcript))