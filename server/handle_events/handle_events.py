import eventbrite
from eventbrite import Eventbrite

class Events:
    def __init__(self):
        self.events = Eventbrite(oauth_token="HMDILKOOYVHWM4HOFU7J")

    def get_events(self,*id):
        client_id = self.events.get_user()['id']
        events = self.events.get_user_events(client_id)
        return events
