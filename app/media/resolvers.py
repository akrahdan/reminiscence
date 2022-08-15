from services import StrapiSession
import json
session = StrapiSession(base_url="http://10.140.127.124:1337")


def upload_media(media, headers):
    res_obj = {'ref': media.ref,
                        'refId': media.refId, 'field': media.field}

    resp = session.post('api/upload', headers=headers, data=res_obj, files= media.files)
    json_obj = resp.json()
    result = json_obj["data"]

    media = transform_attribute(result["attributes"])
    media["id"] = result["id"]
    return media


def transform_attribute(attr):
    attributes = {}
    attributes['name'] = attr["name"]
    attributes["url"] = attr["url"]
    attributes["mime"] = attr["mime"]
    attributes["width"] = attr["width"]
    attributes["height"] = attr["height"]

    return attributes

def transform_event(event):
    trans_event = {}
    trans_event['id'] = event['id']
    attributes = transform_attribute(event["attributes"])
    trans_event['title'] = attributes['title']
    trans_event['description'] = attributes["description"]
    trans_event['updatedAt']  = attributes["updatedAt"]
    trans_event["createdAt"] = attributes["createdAt"]
    return trans_event


    