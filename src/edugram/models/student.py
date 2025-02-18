# This file was generated by liblab | https://liblab.com/

from typing import List
from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Student(BaseModel):
    """Student

    :param _id: _id, defaults to None
    :type _id: str, optional
    :param tg_id: tg_id
    :type tg_id: str
    :param name: name
    :type name: str
    :param email: email
    :type email: str
    :param role: role, defaults to None
    :type role: str, optional
    :param grade: grade
    :type grade: str
    :param courses: courses
    :type courses: List[str]
    :param assignments: assignments
    :type assignments: List[str]
    """

    def __init__(
        self,
        tg_id: str,
        name: str,
        email: str,
        grade: str,
        courses: List[str],
        assignments: List[str],
        _id: Union[str, None] = SENTINEL,
        role: str = SENTINEL,
        **kwargs
    ):
        """Student

        :param _id: _id, defaults to None
        :type _id: str, optional
        :param tg_id: tg_id
        :type tg_id: str
        :param name: name
        :type name: str
        :param email: email
        :type email: str
        :param role: role, defaults to None
        :type role: str, optional
        :param grade: grade
        :type grade: str
        :param courses: courses
        :type courses: List[str]
        :param assignments: assignments
        :type assignments: List[str]
        """
        if _id is not SENTINEL:
            self._id = self._define_str("_id", _id, nullable=True)
        self.tg_id = tg_id
        self.name = name
        self.email = email
        if role is not SENTINEL:
            self.role = role
        self.grade = grade
        self.courses = courses
        self.assignments = assignments
        self._kwargs = kwargs
