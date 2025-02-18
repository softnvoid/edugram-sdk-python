# AuthService

A list of all methods in the `AuthService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                 | Description |
| :-------------------------------------------------------------------------------------- | :---------- |
| [get_user_status_auth_check_user_tg_id_get](#get_user_status_auth_check_user_tg_id_get) |             |

## get_user_status_auth_check_user_tg_id_get

- HTTP Method: `GET`
- Endpoint: `/auth/check_user/{tg_id}`

**Parameters**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| tg_id | str  | ✅       |             |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from edugram import Edugram

sdk = Edugram(
    timeout=10000
)

result = sdk.auth.get_user_status_auth_check_user_tg_id_get(tg_id="tg_id")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
