from services import session


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


def get_currrent_user(headers):
    res = session.get("/api/users/me", headers=headers)
    return res.json()



