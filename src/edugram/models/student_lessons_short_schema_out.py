# This file was generated by liblab | https://liblab.com/

from typing import Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"date_": "date"})
class StudentLessonsShortSchemaOut(BaseModel):
    """StudentLessonsShortSchemaOut

    :param _id: _id, defaults to None
    :type _id: str, optional
    :param title: title
    :type title: str
    :param date_: date_
    :type date_: str
    :param course_title: course_title
    :type course_title: str
    """

    def __init__(
        self,
        title: str,
        date_: str,
        course_title: Union[str, None],
        _id: str = SENTINEL,
        **kwargs
    ):
        """StudentLessonsShortSchemaOut

        :param _id: _id, defaults to None
        :type _id: str, optional
        :param title: title
        :type title: str
        :param date_: date_
        :type date_: str
        :param course_title: course_title
        :type course_title: str
        """
        if _id is not SENTINEL:
            self._id = _id
        self.title = title
        self.date_ = date_
        self.course_title = self._define_str(
            "course_title", course_title, nullable=True
        )
        self._kwargs = kwargs
