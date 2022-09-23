from services import session
import httpx
from settings.config import API_ENDPOINT

def user_login(login, headers):
    json_obj = {'identifier': login.identifier, "password": login.password}
    
    res = session.post("/api/auth/local", json= json_obj)
    result = res.json()
    
    user = result.get("user", {})
    user["jwt"] = result.get("jwt", None)
    return user


async def get_currrent_user(headers):
    headers = {"authorization" : headers.get('authorization', None)}
    async with httpx.AsyncClient(base_url=API_ENDPOINT) as client:
        
        res = await client.get(url="/api/users/me", headers=headers)

    return res.json()



