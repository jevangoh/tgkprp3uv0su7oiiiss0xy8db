from __future__ import annotations
import logging

from typing import Any
from structlog import BoundLogger


class tgkprp3uv0su7oiiiss0xy8db(BoundLogger):
    def record(self, event: str, **kwargs: Any) -> Any:
        return self._proxy_to_logger("record", event, **kwargs)

    def inform(self, event: str, **kwargs: Any) -> Any:
        return self._proxy_to_logger("inform", event, **kwargs)

    def notify(self, event: str, **kwargs: Any) -> Any:
        return self._proxy_to_logger("notify", event, **kwargs)

    def alert(self, event: str, **kwargs: Any) -> Any:
        return self._proxy_to_logger("alert", event, **kwargs)

    def warn(self, event: str, **kwargs: Any) -> Any:
        return self._proxy_to_logger("warn", event, **kwargs)

    def add_handler(self, handler: logging.Handler) -> tgkprp3uv0su7oiiiss0xy8db:
        logging.getLogger().addHandler(handler)
        return self
