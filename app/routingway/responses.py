from pydantic import BaseModel, computed_field, Field
from datetime import datetime


class BasicResponse(BaseModel):
    success: bool = Field(default=True, description="Whether the request was successful")
    data: dict = Field(default={}, description="Additional data")
    status: str | None = Field(
        default=None,
        description="Information about the status of the request if it is not normal")

    @computed_field(description="The time the server responded to the request. WILL BE REMOVED IN THE FUTURE")
    @property
    def servertime(self) -> str:  # TODO probably uselses, maybe add software version or something
        return datetime.now().isoformat()


class LogResponse(BasicResponse):
    log: list[str] = Field(description="Output of the executed operation")
