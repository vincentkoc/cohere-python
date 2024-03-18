# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .embed_by_type_response import EmbedByTypeResponse
from .embed_floats_response import EmbedFloatsResponse


class EmbedResponse_EmbeddingsFloats(EmbedFloatsResponse):
    response_type: typing.Literal["embeddings_floats"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class EmbedResponse_EmbeddingsByType(EmbedByTypeResponse):
    response_type: typing.Literal["embeddings_by_type"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


EmbedResponse = typing.Union[EmbedResponse_EmbeddingsFloats, EmbedResponse_EmbeddingsByType]
