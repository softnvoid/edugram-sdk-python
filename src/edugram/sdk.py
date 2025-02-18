# This file was generated by liblab | https://liblab.com/

from typing import Union
from .services.index import IndexService
from .services.sentry_debug import SentryDebugService
from .services.student import StudentService
from .services.courses import CoursesService
from .services.teacher import TeacherService
from .services.assignments import AssignmentsService
from .services.lessons import LessonsService
from .services.auth import AuthService
from .net.environment import Environment


class Edugram:
    def __init__(
        self,
        base_url: Union[Environment, str] = Environment.DEFAULT,
        timeout: int = 60000,
    ):
        """
        Initializes Edugram the SDK class.
        """

        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self.index = IndexService(base_url=self._base_url)
        self.sentry_debug = SentryDebugService(base_url=self._base_url)
        self.student = StudentService(base_url=self._base_url)
        self.courses = CoursesService(base_url=self._base_url)
        self.teacher = TeacherService(base_url=self._base_url)
        self.assignments = AssignmentsService(base_url=self._base_url)
        self.lessons = LessonsService(base_url=self._base_url)
        self.auth = AuthService(base_url=self._base_url)
        self.set_timeout(timeout)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )

        self.index.set_base_url(self._base_url)
        self.sentry_debug.set_base_url(self._base_url)
        self.student.set_base_url(self._base_url)
        self.courses.set_base_url(self._base_url)
        self.teacher.set_base_url(self._base_url)
        self.assignments.set_base_url(self._base_url)
        self.lessons.set_base_url(self._base_url)
        self.auth.set_base_url(self._base_url)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.index.set_timeout(timeout)
        self.sentry_debug.set_timeout(timeout)
        self.student.set_timeout(timeout)
        self.courses.set_timeout(timeout)
        self.teacher.set_timeout(timeout)
        self.assignments.set_timeout(timeout)
        self.lessons.set_timeout(timeout)
        self.auth.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
