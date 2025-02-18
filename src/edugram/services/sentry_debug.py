# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class SentryDebugService(BaseService):

    @cast_models
    def trigger_error_sentry_debug_get(self) -> any:
        """trigger_error_sentry_debug_get

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        serialized_request = (
            Serializer(f"{self.base_url}/sentry-debug", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
