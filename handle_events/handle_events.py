
import requests
class Events:
    def __init__(self,token):
        self.token = token

    #will return a json copy of all the events
    def get_events(self):
        id = requests.get(url=f"https://www.eventbriteapi.com/v3/users/me/organizations/",
                          headers={"Authorization": f'Bearer {self.token}'}).json()

        id = id["organizations"][0]["id"]

        events = requests.get(url=f"https://www.eventbriteapi.com/v3/organizations/{id}/events/",
                              headers={"Authorization": f'Bearer {self.token}'}).json()
        return events.json()
#
#
#
# # from eventbrite import Eventbrite
eventbrite = Eventbrite("ENIBW4MQNTNKBZEOBGU3")
#
#
# Get my own User ID
print(eventbrite.get_user())



