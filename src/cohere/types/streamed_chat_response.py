# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .chat_search_query import ChatSearchQuery
from .chat_search_result import ChatSearchResult
from .chat_document import ChatDocument
from .chat_citation import ChatCitation
from .tool_call import ToolCall
from .chat_stream_end_event_finish_reason import ChatStreamEndEventFinishReason
from .non_streamed_chat_response import NonStreamedChatResponse
from .tool_call_delta import ToolCallDelta
import typing_extensions
from ..core.unchecked_base_model import UnionMetadata


class StreamedChatResponse_StreamStart(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["stream-start"] = "stream-start"
    generation_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_SearchQueriesGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["search-queries-generation"] = "search-queries-generation"
    search_queries: typing.List[ChatSearchQuery]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_SearchResults(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["search-results"] = "search-results"
    search_results: typing.Optional[typing.List[ChatSearchResult]] = None
    documents: typing.Optional[typing.List[ChatDocument]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_TextGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["text-generation"] = "text-generation"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_CitationGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["citation-generation"] = "citation-generation"
    citations: typing.List[ChatCitation]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_ToolCallsGeneration(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["tool-calls-generation"] = "tool-calls-generation"
    text: typing.Optional[str] = None
    tool_calls: typing.List[ToolCall]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_StreamEnd(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["stream-end"] = "stream-end"
    finish_reason: ChatStreamEndEventFinishReason
    response: NonStreamedChatResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamedChatResponse_ToolCallsChunk(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    event_type: typing.Literal["tool-calls-chunk"] = "tool-calls-chunk"
    tool_call_delta: ToolCallDelta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamedChatResponse = typing_extensions.Annotated[
    typing.Union[
        StreamedChatResponse_StreamStart,
        StreamedChatResponse_SearchQueriesGeneration,
        StreamedChatResponse_SearchResults,
        StreamedChatResponse_TextGeneration,
        StreamedChatResponse_CitationGeneration,
        StreamedChatResponse_ToolCallsGeneration,
        StreamedChatResponse_StreamEnd,
        StreamedChatResponse_ToolCallsChunk,
    ],
    UnionMetadata(discriminant="event_type"),
]
