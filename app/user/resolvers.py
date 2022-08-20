from services import session
import httpx
from settings.config import API_ENDPOINT

def user_login(login, headers):
    json_obj = {'identifier': login.identifier, "password": login.password}
    print("JSON: ", json_obj, "Type: ", type(json_obj))
    print("Headers: ", headers)
    res = session.post("/api/auth/local", json= json_obj)
    result = res.json()
    print("Result: ", result)
    user = result.get("user", {})
    user["jwt"] = result.get("jwt", None)
    return user


async def get_currrent_user(headers):
    headers = {"authorization" : headers.get('authorization', None)}
    async with httpx.AsyncClient(base_url=API_ENDPOINT) as client:
        
        res = await client.get(url="/api/users/me", headers=headers)

    print("Res: ", res.json())
    return res.json()



