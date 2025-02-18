# This file was generated by liblab | https://liblab.com/

from typing import Union
from .net.environment import Environment
from .sdk import Edugram
from .services.async_.index import IndexServiceAsync
from .services.async_.sentry_debug import SentryDebugServiceAsync
from .services.async_.student import StudentServiceAsync
from .services.async_.courses import CoursesServiceAsync
from .services.async_.teacher import TeacherServiceAsync
from .services.async_.assignments import AssignmentsServiceAsync
from .services.async_.lessons import LessonsServiceAsync
from .services.async_.auth import AuthServiceAsync


class EdugramAsync(Edugram):
    """
    EdugramAsync is the asynchronous version of the Edugram SDK Client.
    """

    def __init__(
        self,
        base_url: Union[Environment, str] = Environment.DEFAULT,
        timeout: int = 60000,
    ):
        super().__init__(base_url=base_url, timeout=timeout)

        self.index = IndexServiceAsync(base_url=self._base_url)
        self.sentry_debug = SentryDebugServiceAsync(base_url=self._base_url)
        self.student = StudentServiceAsync(base_url=self._base_url)
        self.courses = CoursesServiceAsync(base_url=self._base_url)
        self.teacher = TeacherServiceAsync(base_url=self._base_url)
        self.assignments = AssignmentsServiceAsync(base_url=self._base_url)
        self.lessons = LessonsServiceAsync(base_url=self._base_url)
        self.auth = AuthServiceAsync(base_url=self._base_url)
