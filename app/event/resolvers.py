from services import session
from pathlib import Path
import requests
import urllib.request
import httpx
# session = StrapiSession(base_url="http://10.140.127.124:1337")
# session = StrapiSession(base_url="https://pandasvr.d.umn.edu")
# headers = { "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNjYwMjM3MDU2LCJleHAiOjE2NjI4MjkwNTZ9.1iL1VyHL1GUnkkplzRw6-qjoS6712e1alMljuLpwyAA'}


def load_events(headers):
    print("Headers: ", headers)
    try:
        resp = session.get('api/events?populate=*', headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    json_obj = resp.json()

    eventList = json_obj["data"]
    # print("EventList: ", eventList)
    # urllib.request.urlretrieve(url="", )
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
    attributes["description"] = attr["Description"]
    attributes["updatedAt"] = attr["updatedAt"]
    attributes["createdAt"] = attr["createdAt"]
    attributes["photos"] = attr["Photos"]

    attributes["songs"] = attr["Songs"]

    return attributes


def transform_event(event):
    trans_event = {}
    trans_event['id'] = event['id']
    attributes = transform_attribute(event["attributes"])
    trans_event['title'] = attributes['title']
    trans_event['description'] = attributes["description"]
    trans_event['updatedAt'] = attributes["updatedAt"]
    trans_event["createdAt"] = attributes["createdAt"]
    photos = attributes['photos'].get("data", None)
    if photos is not None:
        iterator = map(transform_files, photos)
        trans_event["photos"] = list(iterator)
    return trans_event


def transform_files(event):
    trans_file = {}
    trans_file['id'] = event['id']
    attributes = transform__file_attribute(event["attributes"])
    trans_file["name"] = attributes.get("name", None)
    endpont = attributes.get("url", None)
    url = "https://pandasvr.d.umn.edu" + endpont
    BASE_DIR = Path(__file__).resolve().parent
    
    filename = BASE_DIR / "images.jpg" 
    urllib.request.urlretrieve(url=url, filename=filename)
    trans_file["url"] = attributes.get("url", None)
    trans_file["mime"] = attributes.get("mime", None)
    return trans_file


def transform__file_attribute(attr):
    attributes = {}
    attributes["name"] = attr["name"]
    attributes['url'] = attr['formats']['thumbnail']['url']
    attributes['mime'] = attr['formats']['thumbnail']['mime']
    return attributes
