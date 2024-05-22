# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel, UnionMetadata
from .chat_citation import ChatCitation
from .chat_document import ChatDocument
from .chat_search_query import ChatSearchQuery
from .chat_search_result import ChatSearchResult
from .chat_stream_end_event_finish_reason import ChatStreamEndEventFinishReason
from .non_streamed_chat_response import NonStreamedChatResponse
from .tool_call import ToolCall


class StreamedChatResponse_StreamStart(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    generation_id: str
    event_type: typing.Literal["stream-start"] = "stream-start"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class StreamedChatResponse_SearchQueriesGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    search_queries: typing.List[ChatSearchQuery]
    event_type: typing.Literal["search-queries-generation"] = "search-queries-generation"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class StreamedChatResponse_SearchResults(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    search_results: typing.Optional[typing.List[ChatSearchResult]] = None
    documents: typing.Optional[typing.List[ChatDocument]] = None
    event_type: typing.Literal["search-results"] = "search-results"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class StreamedChatResponse_TextGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    text: str
    event_type: typing.Literal["text-generation"] = "text-generation"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class StreamedChatResponse_CitationGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    citations: typing.List[ChatCitation]
    event_type: typing.Literal["citation-generation"] = "citation-generation"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class StreamedChatResponse_ToolCallsGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    tool_calls: typing.List[ToolCall]
    event_type: typing.Literal["tool-calls-generation"] = "tool-calls-generation"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class StreamedChatResponse_StreamEnd(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    finish_reason: ChatStreamEndEventFinishReason
    response: NonStreamedChatResponse
    event_type: typing.Literal["stream-end"] = "stream-end"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


StreamedChatResponse = typing_extensions.Annotated[
    typing.Union[
        StreamedChatResponse_StreamStart,
        StreamedChatResponse_SearchQueriesGeneration,
        StreamedChatResponse_SearchResults,
        StreamedChatResponse_TextGeneration,
        StreamedChatResponse_CitationGeneration,
        StreamedChatResponse_ToolCallsGeneration,
        StreamedChatResponse_StreamEnd,
    ],
    UnionMetadata(discriminant="event_type"),
]
