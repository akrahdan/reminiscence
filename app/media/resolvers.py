from services import session
from requests_toolbelt.multipart import MultipartEncoder
import json


def upload_media(media, headers):
    res_obj = {'ref': media.ref,
               'refId': media.refId, 'field': media.field}
    
    files = []

    for file in media.files:
        files.append(file.file)

   
    resp = session.post('api/upload', headers=headers, data=res_obj, files=files)
    # print("Res: ", resp)
    json_obj = resp.json()
    result = json_obj["data"]

    media = transform_attribute(result["attributes"])
    media["id"] = result["id"]
    return media


def upload_files(multi_data, files, headers):
   
    
    resp = session.post('api/upload', headers=headers, data=multi_data, files=files)
    print("Res: ", resp)
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
    trans_event['updatedAt'] = attributes["updatedAt"]
    trans_event["createdAt"] = attributes["createdAt"]
    return trans_event
