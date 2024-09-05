# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .api_meta import ApiMeta
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TokenizeResponse(UncheckedBaseModel):
    tokens: typing.List[int] = pydantic.Field()
    """
    An array of tokens, where each token is an integer.
    """

    token_strings: typing.List[str]
    meta: typing.Optional[ApiMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
