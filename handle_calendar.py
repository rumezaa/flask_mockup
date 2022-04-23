import requests
from pprint import*
import google
from backend.Google import Create_Service,convert_to_RFC_datetime


class HandleRequests:
    def __init__(self):
        client_id = "925812010640-1dfpm334hia22bcsgki6hi4dlab5lgij.apps.googleusercontent.com"
        client_secret = "backend/client_secret.json"
        scopes = ['https://www.googleapis.com/auth/calendar']


        s = Create_Service(client_secret,"calendar api","v3",scopes)
        pass
