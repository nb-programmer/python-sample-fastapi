import logging
from collections.abc import Mapping


class HealthCheckFilter(logging.Filter):
    """Filter out healthcheck access logs from uvicorn.access module"""

    HEALTHCHECK_ROUTE = "/health/healthcheck"

    def filter(self, record: logging.LogRecord) -> bool:
        # Check if the log message arguments contain our healthcheck route
        if isinstance(record.args, tuple):
            return self.HEALTHCHECK_ROUTE not in record.args
        elif isinstance(record.args, Mapping):
            return self.HEALTHCHECK_ROUTE not in record.args.values()

        return True
