from services import session
import requests
# session = StrapiSession(base_url="http://10.140.127.124:1337")
# headers = { "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNjYwMjM3MDU2LCJleHAiOjE2NjI4MjkwNTZ9.1iL1VyHL1GUnkkplzRw6-qjoS6712e1alMljuLpwyAA'}


def load_residents(headers):
    try:

       resp = session.get('api/residents', headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    json_obj = resp.json()

    residents = json_obj["data"]
    iterator = map(transform_resident, residents)

    return list(iterator)


def create_resident(resident, headers):
    res_obj = {'data': {'ResidentId': resident.ResidentId,
                        'RoomNo': resident.RoomNo}}
    
    print("CREATE: ", res_obj)
    try: 
        resp = session.post('api/residents', headers=headers, json=res_obj)
    
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print("RESP: ", resp.status_code)
    json_obj = resp.json()
    result = json_obj["data"]
    print("Headers: ", headers)
    resident = transform_attribute(result["attributes"])
    
    resident["id"] = result["id"]
    return resident


def transform_attribute(attr):
    attributes = {}
    attributes['residentId'] = attr["ResidentId"]
    attributes["roomNo"] = attr["RoomNo"]
    attributes["updatedAt"] = attr["updatedAt"]
    attributes["createdAt"] = attr["createdAt"]
    return attributes


def transform_resident(resident):
    trans_resident = {}
    trans_resident['id'] = resident['id']
    attributes = transform_attribute(resident["attributes"])
    trans_resident['residentId'] = attributes['residentId']
    trans_resident['roomNo'] = attributes["roomNo"]
    trans_resident['updatedAt'] = attributes["updatedAt"]
    trans_resident["createdAt"] = attributes["createdAt"]
    return trans_resident
