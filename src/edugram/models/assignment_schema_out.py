# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class AssignmentSchemaOut(BaseModel):
    """AssignmentSchemaOut

    :param student_name: student_name
    :type student_name: str
    :param student_tg_id: student_tg_id
    :type student_tg_id: str
    :param assignment_title: assignment_title
    :type assignment_title: str
    :param assignment_id: assignment_id
    :type assignment_id: str
    :param status: status
    :type status: str
    """

    def __init__(
        self,
        student_name: str,
        student_tg_id: str,
        assignment_title: str,
        assignment_id: str,
        status: str,
        **kwargs
    ):
        """AssignmentSchemaOut

        :param student_name: student_name
        :type student_name: str
        :param student_tg_id: student_tg_id
        :type student_tg_id: str
        :param assignment_title: assignment_title
        :type assignment_title: str
        :param assignment_id: assignment_id
        :type assignment_id: str
        :param status: status
        :type status: str
        """
        self.student_name = student_name
        self.student_tg_id = student_tg_id
        self.assignment_title = assignment_title
        self.assignment_id = assignment_id
        self.status = status
        self._kwargs = kwargs
