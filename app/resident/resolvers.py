from services import session
from starlette.responses import StreamingResponse
from starlette.background import BackgroundTask
import requests
import httpx

from settings.config import API_ENDPOINT




async def load_residents(headers):

    headers = {"authorization" : headers.get('authorization')}
    async with httpx.AsyncClient(base_url=API_ENDPOINT) as client:
        
        res = await client.get(url="/api/residents", headers=headers)

    print("Res: ", res.json())
   
    json_obj = res.json()
   

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
    # print("RESP: ", resp.status_code)
    json_obj = resp.json()
    result = json_obj["data"]
   
    resident = transform_attribute(result["attributes"])
    
    resident["id"] = result.get("id")
    return resident


def transform_attribute(attr):
    attributes = {}
    attributes['residentId'] = attr.get("ResidentId", '')
    attributes["roomNo"] = attr.get("RoomNo", '')
    attributes["updatedAt"] = attr.get("updatedAt", '')
    attributes["createdAt"] = attr.get("createdAt", '')
    return attributes


def transform_resident(resident):
    trans_resident = {}
    trans_resident['id'] = resident.get('id', '')
    attributes = transform_attribute(resident.get("attributes"))
    trans_resident['residentId'] = attributes.get('residentId', None)
    trans_resident['roomNo'] = attributes.get("roomNo", None)
    trans_resident['updatedAt'] = attributes.get("updatedAt", None)
    trans_resident["createdAt"] = attributes.get("createdAt", None)
    return trans_resident
