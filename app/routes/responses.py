from pydantic import BaseModel, computed_field, Field
from datetime import datetime


class BasicResponse(BaseModel):
    success: bool = Field(default=True, description="Whether the request was successful")
    report: dict | list = Field(default={}, description="If available, a report about the request")
    status: str | None = Field(
        default=None,
        description="Information about the status of the request if it is not normal")

    @computed_field(description="The time the server responded to the request. WILL BE REMOVED IN THE FUTURE")
    @property
    def servertime(self) -> str:  # TODO probably uselses, maybe add software version or something
        return datetime.now().isoformat()


class LogResponse(BasicResponse):
    log: list[str] = Field(description="Output of the executed operation")


class RawDataResponse(BasicResponse):
    results: list[dict] = Field(description="Raw datasets directly from the database")
    results_returned: int = Field(description="Number of datasets returned")
    results_total: int = Field(description="Total number of datasets available")
