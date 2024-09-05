# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .chat_content_start_event_delta_message import ChatContentStartEventDeltaMessage
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ChatContentStartEventDelta(UncheckedBaseModel):
    message: typing.Optional[ChatContentStartEventDeltaMessage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
