from __future__ import annotations

import datetime
from typing import Any, Dict, List, Mapping, Optional, Protocol, TYPE_CHECKING, TypeVar, Union

from . import utils
from .colour import Colour
from .flags import AttachmentFlags, EmbedFlags

# fmt: off
__all__ = (
    'Embed',
)

class QuickEmbed():

    text: Optional[str]
    image_url: Optional[str]

    description: str
    icon_url: Optional[str]
    

class EmbedProxy:
    def __init__(self, layer: Dict[str, Any]):
        self.__dict__.update(layer)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        inner = ', '.join((f'{k}={getattr(self, k)!r}' for k in dir(self) if not k.startswith('_')))
        return f'EmbedProxy({inner})'

    def __getattr__(self, attr: str) -> None:
        return None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, EmbedProxy) and self.__dict__ == other.__dict__
