from .models import HealthcheckResponse, HealthCheckStatus


async def respond_healthcheck() -> HealthcheckResponse:
    """Docker healthcheck response to validate if the app is up"""
    return HealthcheckResponse(status=HealthCheckStatus.OK)
