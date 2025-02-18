# This file was generated by liblab | https://liblab.com/

from typing import Awaitable, List
from .utils.to_async import to_async
from ..student import StudentService
from ...models.utils.sentinel import SENTINEL
from ...models import (
    Student,
    StudentShortSchemaOut,
    StudentCoursesList,
    StudentAssignmentSchemaOutList,
    StudentAssignmentShortSchemaOut,
    StudentLessonSchemaOut,
    StudentWeekdayLessonsSchemaOut,
    Order,
    Status,
)


class StudentServiceAsync(StudentService):
    """
    Async Wrapper for StudentServiceAsync
    """

    def add_student_student_new_post(self, request_body: Student) -> Awaitable[any]:
        return to_async(super().add_student_student_new_post)(request_body)

    def add_students_student_new_many_post(
        self, request_body: List[Student]
    ) -> Awaitable[any]:
        return to_async(super().add_students_student_new_many_post)(request_body)

    def get_by_id_student_id_id_get(self, id_: str) -> Awaitable[Student]:
        return to_async(super().get_by_id_student_id_id_get)(id_)

    def get_all_students_student_all_get(
        self,
    ) -> Awaitable[List[StudentShortSchemaOut]]:
        return to_async(super().get_all_students_student_all_get)()

    def get_by_tg_id_student_tg_tg_id_get(self, tg_id: str) -> Awaitable[Student]:
        return to_async(super().get_by_tg_id_student_tg_tg_id_get)(tg_id)

    def get_student_courses_by_id_student_id_id_courses_get(
        self, id_: str
    ) -> Awaitable[StudentCoursesList]:
        return to_async(super().get_student_courses_by_id_student_id_id_courses_get)(
            id_
        )

    def get_student_courses_by_tg_student_tg_tg_id_courses_get(
        self, tg_id: str
    ) -> Awaitable[StudentCoursesList]:
        return to_async(super().get_student_courses_by_tg_student_tg_tg_id_courses_get)(
            tg_id
        )

    def get_student_assingments_by_tg_student_tg_tg_id_assignments_get(
        self, tg_id: str
    ) -> Awaitable[StudentAssignmentSchemaOutList]:
        return to_async(
            super().get_student_assingments_by_tg_student_tg_tg_id_assignments_get
        )(tg_id)

    def get_student_assignments_by_course_student_tg_tg_id_course_course_id_assignments_get(
        self, tg_id: str, course_id: str
    ) -> Awaitable[List[StudentAssignmentShortSchemaOut]]:
        return to_async(
            super().get_student_assignments_by_course_student_tg_tg_id_course_course_id_assignments_get
        )(tg_id, course_id)

    def get_student_week_assignments_by_tg_student_tg_tg_id_week_assignments_get(
        self, tg_id: str, date_of_week: str = SENTINEL
    ) -> Awaitable[List[StudentAssignmentShortSchemaOut]]:
        return to_async(
            super().get_student_week_assignments_by_tg_student_tg_tg_id_week_assignments_get
        )(tg_id, date_of_week)

    def get_student_lessons_by_tg_student_tg_tg_id_lessons_get(
        self, tg_id: str
    ) -> Awaitable[List[StudentLessonSchemaOut]]:
        return to_async(super().get_student_lessons_by_tg_student_tg_tg_id_lessons_get)(
            tg_id
        )

    def get_student_lessons_by_tg_student_tg_tg_id_schedule_get(
        self,
        tg_id: str,
        date_of_week: str = SENTINEL,
        step: int = SENTINEL,
        order: Order = SENTINEL,
    ) -> Awaitable[List[StudentWeekdayLessonsSchemaOut]]:
        return to_async(
            super().get_student_lessons_by_tg_student_tg_tg_id_schedule_get
        )(tg_id, date_of_week, step, order)

    def change_assignment_status_student_tg_student_tg_assignments_assignment_id_status_patch(
        self, student_tg: str, assignment_id: str, status: Status
    ) -> Awaitable[any]:
        return to_async(
            super().change_assignment_status_student_tg_student_tg_assignments_assignment_id_status_patch
        )(student_tg, assignment_id, status)
