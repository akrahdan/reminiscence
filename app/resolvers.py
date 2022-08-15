from services import StrapiSession
import json
session = StrapiSession(base_url="http://10.140.127.124:1337")
headers = { "Authorization": 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNjYwMjM3MDU2LCJleHAiOjE2NjI4MjkwNTZ9.1iL1VyHL1GUnkkplzRw6-qjoS6712e1alMljuLpwyAA'}

def load_events():
    resp =  session.get('api/events?populate=*', headers=headers)
    json_obj = resp.json()
    eventList = json_obj["data"]
    event_iterator = map(transform_event, eventList)
    return list(event_iterator)


def transform_attribute(attr):
    attributes = {}
    attributes['Title'] = attr["Title"]
    attributes["Description"] = attr["Description"]
    attributes["updatedAt"] = attr["updatedAt"]
    attributes["createdAt"] = attr["createdAt"]
    return attributes

def transform_event(event):
    trans_event = {}
    trans_event['id'] = event['id']
    attributes = transform_attribute(event["attributes"])
    trans_event["attributes"] = attributes
    return trans_event


    

    



def fetch_residents():
    resp = session.get('api/residents')

load_events()
  

