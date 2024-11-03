# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .chat_message_start_event_delta import ChatMessageStartEventDelta
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .chat_content_start_event_delta import ChatContentStartEventDelta
from .chat_content_delta_event_delta import ChatContentDeltaEventDelta
from .chat_tool_plan_delta_event_delta import ChatToolPlanDeltaEventDelta
from .chat_tool_call_start_event_delta import ChatToolCallStartEventDelta
from .chat_tool_call_delta_event_delta import ChatToolCallDeltaEventDelta
from .citation_start_event_delta import CitationStartEventDelta
from .chat_message_end_event_delta import ChatMessageEndEventDelta
import typing_extensions
from ..core.unchecked_base_model import UnionMetadata


class MessageStartStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["message-start"] = "message-start"
    id: typing.Optional[str] = None
    delta: typing.Optional[ChatMessageStartEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ContentStartStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["content-start"] = "content-start"
    index: typing.Optional[int] = None
    delta: typing.Optional[ChatContentStartEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ContentDeltaStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["content-delta"] = "content-delta"
    index: typing.Optional[int] = None
    delta: typing.Optional[ChatContentDeltaEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ContentEndStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["content-end"] = "content-end"
    index: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ToolPlanDeltaStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["tool-plan-delta"] = "tool-plan-delta"
    delta: typing.Optional[ChatToolPlanDeltaEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ToolCallStartStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["tool-call-start"] = "tool-call-start"
    index: typing.Optional[int] = None
    delta: typing.Optional[ChatToolCallStartEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ToolCallDeltaStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["tool-call-delta"] = "tool-call-delta"
    index: typing.Optional[int] = None
    delta: typing.Optional[ChatToolCallDeltaEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class ToolCallEndStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["tool-call-end"] = "tool-call-end"
    index: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class CitationStartStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["citation-start"] = "citation-start"
    index: typing.Optional[int] = None
    delta: typing.Optional[CitationStartEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class CitationEndStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["citation-end"] = "citation-end"
    index: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


class MessageEndStreamedChatResponseV2(UncheckedBaseModel):
    """
    StreamedChatResponse is returned in streaming mode (specified with `stream=True` in the request).
    """

    type: typing.Literal["message-end"] = "message-end"
    id: typing.Optional[str] = None
    delta: typing.Optional[ChatMessageEndEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


StreamedChatResponseV2 = typing_extensions.Annotated[
    typing.Union[
        MessageStartStreamedChatResponseV2,
        ContentStartStreamedChatResponseV2,
        ContentDeltaStreamedChatResponseV2,
        ContentEndStreamedChatResponseV2,
        ToolPlanDeltaStreamedChatResponseV2,
        ToolCallStartStreamedChatResponseV2,
        ToolCallDeltaStreamedChatResponseV2,
        ToolCallEndStreamedChatResponseV2,
        CitationStartStreamedChatResponseV2,
        CitationEndStreamedChatResponseV2,
        MessageEndStreamedChatResponseV2,
    ],
    UnionMetadata(discriminant="type"),
]