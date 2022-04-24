from backend.google_apis import create_service,convert_to_RFC_datetime
from pprint import pprint
#handles calendar events -- can integarte auth tech later
class HandleCalendar:
    def __init__(self, calendar_id="jvt5hhmrfbnkjivfmsfjomse04@group.calendar.google.com"):
        client_id = "925812010640-1dfpm334hia22bcsgki6hi4dlab5lgij.apps.googleusercontent.com"
        client_secret = "/home/rumeza/mockup/client_secret.json"
        scopes = ['https://www.googleapis.com/auth/calendar']
        self.calendar_id = calendar_id
        self.service = create_service(client_secret,"calendar","v3",scopes)
    def add_events(self):
        default_temp ={
    'summary': 'Google I/O 2015',
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'A chance to hear more about Google\'s developer products.',
    'start': {
        'dateTime': convert_to_RFC_datetime(2022,4,30,12,20),
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': convert_to_RFC_datetime(2022,5,2,12,20),
        'timeZone': 'America/Los_Angeles',
    },
    'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=2'
    ],
    'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

        self.service.events().insert(calendarId=self.calendar_id, body=default_temp).execute()
