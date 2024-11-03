# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
from .tool_message_v2content import ToolMessageV2Content
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ToolMessageV2(UncheckedBaseModel):
    """
    A message with Tool outputs.
    """

    tool_call_id: str = pydantic.Field()
    """
    The id of the associated tool call that has provided the given content
    """

    content: ToolMessageV2Content = pydantic.Field()
    """
    Outputs from a tool. The content should formatted as a JSON object string, or a list of tool content blocks
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow