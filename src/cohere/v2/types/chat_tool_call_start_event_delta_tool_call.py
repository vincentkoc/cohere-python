# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .chat_tool_call_start_event_delta_tool_call_function import ChatToolCallStartEventDeltaToolCallFunction
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ChatToolCallStartEventDeltaToolCall(UncheckedBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[typing.Literal["function"]] = None
    function: typing.Optional[ChatToolCallStartEventDeltaToolCallFunction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
