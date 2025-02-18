# StudentService

A list of all methods in the `StudentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                                                         | Description |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- |
| [add_student_student_new_post](#add_student_student_new_post)                                                                                                                   |             |
| [add_students_student_new_many_post](#add_students_student_new_many_post)                                                                                                       |             |
| [get_by_id_student_id_id_get](#get_by_id_student_id_id_get)                                                                                                                     |             |
| [get_all_students_student_all_get](#get_all_students_student_all_get)                                                                                                           |             |
| [get_by_tg_id_student_tg_tg_id_get](#get_by_tg_id_student_tg_tg_id_get)                                                                                                         |             |
| [get_student_courses_by_id_student_id_id_courses_get](#get_student_courses_by_id_student_id_id_courses_get)                                                                     |             |
| [get_student_courses_by_tg_student_tg_tg_id_courses_get](#get_student_courses_by_tg_student_tg_tg_id_courses_get)                                                               |             |
| [get_student_assingments_by_tg_student_tg_tg_id_assignments_get](#get_student_assingments_by_tg_student_tg_tg_id_assignments_get)                                               |             |
| [get_student_assignments_by_course_student_tg_tg_id_course_course_id_assignments_get](#get_student_assignments_by_course_student_tg_tg_id_course_course_id_assignments_get)     |             |
| [get_student_week_assignments_by_tg_student_tg_tg_id_week_assignments_get](#get_student_week_assignments_by_tg_student_tg_tg_id_week_assignments_get)                           |             |
| [get_student_lessons_by_tg_student_tg_tg_id_lessons_get](#get_student_lessons_by_tg_student_tg_tg_id_lessons_get)                                                               |             |
| [get_student_lessons_by_tg_student_tg_tg_id_schedule_get](#get_student_lessons_by_tg_student_tg_tg_id_schedule_get)                                                             |             |
| [change_assignment_status_student_tg_student_tg_assignments_assignment_id_status_patch](#change_assignment_status_student_tg_student_tg_assignments_assignment_id_status_patch) |             |

## add_student_student_new_post

- HTTP Method: `POST`
- Endpoint: `/student/new`

**Parameters**

| Name         | Type                            | Required | Description       |
| :----------- | :------------------------------ | :------- | :---------------- |
| request_body | [Student](../models/Student.md) | ✅       | The request body. |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram
from edugram.models import Student

sdk = Edugram(
    timeout=10000
)

request_body = Student(
    _id="_id",
    tg_id="tg_id",
    name="name",
    email="email",
    role="student",
    grade="grade",
    courses=[
        "courses"
    ],
    assignments=[
        "assignments"
    ]
)

result = sdk.student.add_student_student_new_post(request_body=request_body)

print(result)
```

## add_students_student_new_many_post

- HTTP Method: `POST`
- Endpoint: `/student/new_many`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [List[Student]](../models/Student.md) | ✅       | The request body. |

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
        "tg_id": "tg_id",
        "name": "name",
        "email": "email",
        "role": "student",
        "grade": "grade",
        "courses": [
            "courses"
        ],
        "assignments": [
            "assignments"
        ]
    }
]

result = sdk.student.add_students_student_new_many_post(request_body=request_body)

print(result)
```

## get_by_id_student_id_id_get

- HTTP Method: `GET`
- Endpoint: `/student/id/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`Student`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_by_id_student_id_id_get(id_="id")

print(result)
```

## get_all_students_student_all_get

- HTTP Method: `GET`
- Endpoint: `/student/all`

**Return Type**

`List[StudentShortSchemaOut]`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_all_students_student_all_get()

print(result)
```

## get_by_tg_id_student_tg_tg_id_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| tg_id | str  | ✅       |             |

**Return Type**

`Student`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_by_tg_id_student_tg_tg_id_get(tg_id="tg_id")

print(result)
```

## get_student_courses_by_id_student_id_id_courses_get

- HTTP Method: `GET`
- Endpoint: `/student/id/{id}/courses`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`StudentCoursesList`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_courses_by_id_student_id_id_courses_get(id_="id")

print(result)
```

## get_student_courses_by_tg_student_tg_tg_id_courses_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}/courses`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| tg_id | str  | ✅       |             |

**Return Type**

`StudentCoursesList`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_courses_by_tg_student_tg_tg_id_courses_get(tg_id="tg_id")

print(result)
```

## get_student_assingments_by_tg_student_tg_tg_id_assignments_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}/assignments`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| tg_id | str  | ✅       |             |

**Return Type**

`StudentAssignmentSchemaOutList`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_assingments_by_tg_student_tg_tg_id_assignments_get(tg_id="tg_id")

print(result)
```

## get_student_assignments_by_course_student_tg_tg_id_course_course_id_assignments_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}/course/{course_id}/assignments`

**Parameters**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| tg_id     | str  | ✅       |             |
| course_id | str  | ✅       |             |

**Return Type**

`List[StudentAssignmentShortSchemaOut]`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_assignments_by_course_student_tg_tg_id_course_course_id_assignments_get(
    tg_id="tg_id",
    course_id="course_id"
)

print(result)
```

## get_student_week_assignments_by_tg_student_tg_tg_id_week_assignments_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}/week_assignments`

**Parameters**

| Name         | Type | Required | Description      |
| :----------- | :--- | :------- | :--------------- |
| tg_id        | str  | ✅       |                  |
| date_of_week | str  | ❌       | date of the week |

**Return Type**

`List[StudentAssignmentShortSchemaOut]`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_week_assignments_by_tg_student_tg_tg_id_week_assignments_get(
    tg_id="tg_id",
    date_of_week="2025-02-18"
)

print(result)
```

## get_student_lessons_by_tg_student_tg_tg_id_lessons_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}/lessons`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| tg_id | str  | ✅       |             |

**Return Type**

`List[StudentLessonSchemaOut]`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_lessons_by_tg_student_tg_tg_id_lessons_get(tg_id="tg_id")

print(result)
```

## get_student_lessons_by_tg_student_tg_tg_id_schedule_get

- HTTP Method: `GET`
- Endpoint: `/student/tg/{tg_id}/schedule`

**Parameters**

| Name         | Type                        | Required | Description                                                              |
| :----------- | :-------------------------- | :------- | :----------------------------------------------------------------------- |
| tg_id        | str                         | ✅       |                                                                          |
| date_of_week | str                         | ❌       | date of the week                                                         |
| step         | int                         | ❌       | Step for pagination: 0 - current week, 1 - next week, -1 - previous week |
| order        | [Order](../models/Order.md) | ❌       | Sort order: asc or desc                                                  |

**Return Type**

`List[StudentWeekdayLessonsSchemaOut]`

**Example Usage Code Snippet**

```python
from edugram import Edugram
from edugram.models import Order

sdk = Edugram(
    timeout=10000
)

result = sdk.student.get_student_lessons_by_tg_student_tg_tg_id_schedule_get(
    tg_id="tg_id",
    date_of_week="2025-02-18",
    step=8,
    order="ask"
)

print(result)
```

## change_assignment_status_student_tg_student_tg_assignments_assignment_id_status_patch

- HTTP Method: `PATCH`
- Endpoint: `/student/tg/{student_tg}/assignments/{assignment_id}/status`

**Parameters**

| Name          | Type                          | Required | Description |
| :------------ | :---------------------------- | :------- | :---------- |
| student_tg    | str                           | ✅       |             |
| assignment_id | str                           | ✅       |             |
| status        | [Status](../models/Status.md) | ✅       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram
from edugram.models import Status

sdk = Edugram(
    timeout=10000
)

result = sdk.student.change_assignment_status_student_tg_student_tg_assignments_assignment_id_status_patch(
    student_tg="student_tg",
    assignment_id="assignment_id",
    status="ready"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
