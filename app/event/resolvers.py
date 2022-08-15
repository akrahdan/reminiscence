from services import StrapiSession
import json
session = StrapiSession(base_url="http://10.140.127.124:1337")
# headers = { "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNjYwMjM3MDU2LCJleHAiOjE2NjI4MjkwNTZ9.1iL1VyHL1GUnkkplzRw6-qjoS6712e1alMljuLpwyAA'}

def load_events(headers):
   
    resp =  session.get('api/events?populate=*', headers=headers)
    json_obj = resp.json()
   
    eventList = json_obj["data"]
    event_iterator = map(transform_event, eventList)
    
    return list(event_iterator)

def create_event(event, headers):
    res_obj = {'data': {'Title': event.Title,
                        'Description': event.Description, 'resident': event.resident}}

    resp = session.post('api/events', headers=headers, json=res_obj)
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


    