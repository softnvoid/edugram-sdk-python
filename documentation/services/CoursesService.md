# CoursesService

A list of all methods in the `CoursesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                     | Description |
| :---------------------------------------------------------------------------------------------------------- | :---------- |
| [add_course_courses_new_post](#add_course_courses_new_post)                                                 |             |
| [add_courses_courses_new_many_post](#add_courses_courses_new_many_post)                                     |             |
| [get_by_id_courses_id_get](#get_by_id_courses_id_get)                                                       |             |
| [get_students_data_courses_course_id_students_get](#get_students_data_courses_course_id_students_get)       |             |
| [get_students_data_courses_course_id_assignments_get](#get_students_data_courses_course_id_assignments_get) |             |
| [add_student_update_data_courses_student_post](#add_student_update_data_courses_student_post)               |             |
| [add_assignment_courses_assignment_post](#add_assignment_courses_assignment_post)                           |             |
| [add_lesson_courses_lesson_post](#add_lesson_courses_lesson_post)                                           |             |

## add_course_courses_new_post

- HTTP Method: `POST`
- Endpoint: `/courses/new`

**Parameters**

| Name         | Type                          | Required | Description       |
| :----------- | :---------------------------- | :------- | :---------------- |
| request_body | [Course](../models/Course.md) | ✅       | The request body. |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram
from edugram.models import Course

sdk = Edugram(
    timeout=10000
)

request_body = Course(
    _id="_id",
    title="title",
    description="description",
    materials=[
        "materials"
    ],
    teacher_id="teacher_id",
    assignments=[
        "assignments"
    ],
    lessons=[
        "lessons"
    ],
    students=[
        "students"
    ]
)

result = sdk.courses.add_course_courses_new_post(request_body=request_body)

print(result)
```

## add_courses_courses_new_many_post

- HTTP Method: `POST`
- Endpoint: `/courses/new_many`

**Parameters**

| Name         | Type                                | Required | Description       |
| :----------- | :---------------------------------- | :------- | :---------------- |
| request_body | [List[Course]](../models/Course.md) | ✅       | The request body. |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

request_body = [
    {
        "_id": "_id",
        "title": "title",
        "description": "description",
        "materials": [
            "materials"
        ],
        "teacher_id": "teacher_id",
        "assignments": [
            "assignments"
        ],
        "lessons": [
            "lessons"
        ],
        "students": [
            "students"
        ]
    }
]

result = sdk.courses.add_courses_courses_new_many_post(request_body=request_body)

print(result)
```

## get_by_id_courses_id_get

- HTTP Method: `GET`
- Endpoint: `/courses/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`Course`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.courses.get_by_id_courses_id_get(id_="id")

print(result)
```

## get_students_data_courses_course_id_students_get

- HTTP Method: `GET`
- Endpoint: `/courses/{course_id}/students`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| course_id | str  | ✅       |             |

**Return Type**

`List[StudentDataOUt]`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.courses.get_students_data_courses_course_id_students_get(course_id="course_id")

print(result)
```

## get_students_data_courses_course_id_assignments_get

- HTTP Method: `GET`
- Endpoint: `/courses/{course_id}/assignments`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| course_id | str  | ✅       |             |

**Return Type**

`List[AssignmentDataOUt]`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.courses.get_students_data_courses_course_id_assignments_get(course_id="course_id")

print(result)
```

## add_student_update_data_courses_student_post

- HTTP Method: `POST`
- Endpoint: `/courses/student`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| course_id  | str  | ✅       |             |
| student_id | str  | ✅       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.courses.add_student_update_data_courses_student_post(
    course_id="course_id",
    student_id="student_id"
)

print(result)
```

## add_assignment_courses_assignment_post

- HTTP Method: `POST`
- Endpoint: `/courses/assignment`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| course_id     | str  | ✅       |             |
| assignment_id | str  | ✅       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.courses.add_assignment_courses_assignment_post(
    course_id="course_id",
    assignment_id="assignment_id"
)

print(result)
```

## add_lesson_courses_lesson_post

- HTTP Method: `POST`
- Endpoint: `/courses/lesson`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| course_id | str  | ✅       |             |
| lesson_id | str  | ✅       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.courses.add_lesson_courses_lesson_post(
    course_id="course_id",
    lesson_id="lesson_id"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
