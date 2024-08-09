# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel


class DocumentContent(UncheckedBaseModel):
    """
    Content block of the message that contains information about documents.
    """

    id: str
    document: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow