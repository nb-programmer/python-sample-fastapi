from enum import Enum

from pydantic import BaseModel


class HealthCheckStatus(str, Enum):
    OK = "ok"


class HealthcheckResponse(BaseModel):
    status: HealthCheckStatus = HealthCheckStatus.OK
