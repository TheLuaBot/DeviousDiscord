"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz, Astro

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

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

class EmbedMediaProxy(EmbedProxy):
    def __init__(self, layer: Dict[str, Any]):
        super().__init__(layer)
        self._flags = self.__dict__.pop('flags', 0)

    def __bool__(self) -> bool:
        # This is a nasty check to see if we only have the `_flags` attribute which is created regardless in init.
        # Had we had any of the other items, like image/video data this would be >1 and therefor
        # would not be "empty".
        return len(self.__dict__) > 1

    @property
    def flags(self) -> AttachmentFlags:
        return AttachmentFlags._from_value(self._flags or 0)


    if TYPE_CHECKING:
        from typing_extensions import Self

        from .types.embed import Embed as EmbedData, EmbedType

        T = TypeVar('T')

        class _EmbedFooterProxy(Protocol):
            text: Optional[str]
            icon_url: Optional[str]

        class _EmbedFieldProxy(Protocol):
            name: Optional[str]
            value: Optional[str]
            inline: bool

        class _EmbedMediaProxy(Protocol):
            url: Optional[str]
            proxy_url: Optional[str]
            height: Optional[int]
            width: Optional[int]
            flags: AttachmentFlags

        class _EmbedProviderProxy(Protocol):
            name: Optional[str]
            url: Optional[str]

        class _EmbedAuthorProxy(Protocol):
            name: Optional[str]
            url: Optional[str]
            icon_url: Optional[str]
            proxy_icon_url: Optional[str]
