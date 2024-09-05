# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EmbedByTypeResponseEmbeddings(UncheckedBaseModel):
    """
    An object with different embedding types. The length of each embedding type array will be the same as the length of the original `texts` array.
    """

    float_: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[float]]], FieldMetadata(alias="float")
    ] = pydantic.Field(default=None)
    """
    An array of float embeddings.
    """

    int8: typing.Optional[typing.List[typing.List[int]]] = pydantic.Field(default=None)
    """
    An array of signed int8 embeddings. Each value is between -128 and 127.
    """

    uint8: typing.Optional[typing.List[typing.List[int]]] = pydantic.Field(default=None)
    """
    An array of unsigned int8 embeddings. Each value is between 0 and 255.
    """

    binary: typing.Optional[typing.List[typing.List[int]]] = pydantic.Field(default=None)
    """
    An array of packed signed binary embeddings. The length of each binary embedding is 1/8 the length of the float embeddings of the provided model. Each value is between -128 and 127.
    """

    ubinary: typing.Optional[typing.List[typing.List[int]]] = pydantic.Field(default=None)
    """
    An array of packed unsigned binary embeddings. The length of each binary embedding is 1/8 the length of the float embeddings of the provided model. Each value is between 0 and 255.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
