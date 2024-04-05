# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1
from ....core.unchecked_base_model import UncheckedBaseModel
from .event import Event


class ListEventsResponse(UncheckedBaseModel):
    """
    Response to a request to list events of a fine-tuned model.
    """

    events: typing.Optional[typing.List[Event]] = pydantic_v1.Field(default=None)
    """
    List of events for the fine-tuned model.
    """

    next_page_token: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Pagination token to retrieve the next page of results. If the value is "",
    it means no further results for the request.
    """

    total_size: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Total count of results.
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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
