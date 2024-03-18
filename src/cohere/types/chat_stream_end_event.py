# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .chat_stream_end_event_finish_reason import ChatStreamEndEventFinishReason
from .chat_stream_event import ChatStreamEvent
from .non_streamed_chat_response import NonStreamedChatResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ChatStreamEndEvent(ChatStreamEvent):
    finish_reason: ChatStreamEndEventFinishReason = pydantic.Field()
    """
    - `COMPLETE` - the model sent back a finished reply
    - `ERROR_LIMIT` - the reply was cut off because the model reached the maximum number of tokens for its context length
    - `MAX_TOKENS` - the reply was cut off because the model reached the maximum number of tokens specified by the max_tokens parameter
    - `ERROR` - something went wrong when generating the reply
    - `ERROR_TOXIC` - the model generated a reply that was deemed toxic
    """

    response: NonStreamedChatResponse = pydantic.Field()
    """
    The consolidated response from the model. Contains the generated reply and all the other information streamed back in the previous events.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
