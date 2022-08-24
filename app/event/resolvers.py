from turtle import st
from services import session
from pathlib import Path
import requests
import urllib.request
import os
from settings.config import API_ENDPOINT
import httpx
from resident.resolvers import transform_attribute as transform_resident

async def load_events(header):

    headers = {"authorization": header.get('authorization')}
    async with httpx.AsyncClient(base_url=API_ENDPOINT) as client:

        res = await client.get(url="/api/events?populate=*", headers=headers)

    # print("Res: ", res.json())

    json_obj = res.json()

    eventList = json_obj["data"]
    # print("EventList: ", eventList)

    event_iterator = map(transform_event, eventList)
    # print("EventList: ", list(event_iterator))
    return list(event_iterator)


def create_event(event, headers):
    res_obj = {'data': {'Title': event.Title,
                        'Description': event.Description, 'resident': event.resident}}

    try:

        resp = session.post('api/events', headers=headers, json=res_obj)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    json_obj = resp.json()
    result = json_obj["data"]
   
    event = transform_attribute(result["attributes"])
   
    event["id"] = result["id"]
    return event


def transform_attribute(attr):
    attributes = {}
    attributes['title'] = attr["Title"]
    attributes["description"] = attr.get("Description", None)
    attributes["updatedAt"] = attr["updatedAt"]
    attributes["createdAt"] = attr["createdAt"]
    attributes["photos"] = attr.get("Photos", None)
    attributes['resident'] = attr.get("resident", None)
    attributes["songs"] = attr.get("Songs", None)

    return attributes


def transform_event(event):
    trans_event = {}
    trans_event['id'] = event['id']
    attributes = transform_attribute(event["attributes"])
    trans_event['title'] = attributes['title']
    trans_event['description'] = attributes.get("description", '')
    trans_event['updatedAt'] = attributes["updatedAt"]
    trans_event["createdAt"] = attributes["createdAt"]

    photos = attributes['photos'].get("data", None)

    if photos is not None:
        iterator = map(transform_files, photos)
        trans_event["photos"] = list(iterator)
    
    resident = attributes["resident"].get("data", None)
    event_resident = None
    if resident is not None:
        event_resident = transform_resident(resident['attributes'])
        event_resident["id"] = resident["id"]
    
    trans_event["resident"] = event_resident
    return trans_event


def transform_files(event):
    trans_file = {}
    photo_id = event['id']
    trans_file['id'] = photo_id
    attributes = transform__file_attribute(event["attributes"])
    trans_file["name"] = attributes.get("name", None)
    endpont = attributes.get("url", None)
    url = "https://pandasvr.d.umn.edu" + endpont
    BASE_DIR = Path(__file__).resolve().parent
    filename = attributes.get("name", 'newfile.jpg')
    path = f'upload/{photo_id}'
    new_url = f'/upload/{photo_id}/{filename}'

    FILE_DIR = Path(BASE_DIR / path)
    FILE_DIR.mkdir(parents=True, exist_ok=True)

    filename = FILE_DIR.joinpath(filename)

    urllib.request.urlretrieve(url=url, filename=filename)
    trans_file["url"] = new_url
    trans_file["mime"] = attributes.get("mime", None)
    return trans_file


def transform__file_attribute(attr):
    attributes = {}
    attributes["name"] = attr["name"]
    attributes['url'] = attr['url']
    attributes['mime'] = attr['mime']
    return attributes
