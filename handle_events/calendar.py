from backend.google_apis import create_service, convert_to_RFC_datetime


# handles calendar events -- can integarte auth tech later

class HandleCalendar:
    def __init__(self, calendar_id="jvt5hhmrfbnkjivfmsfjomse04@group.calendar.google.com"):
        # creating api service
        client_id = "488996747074-hbluscucl9ulbihc6g8ek8hs4gqgjk6b.apps.googleusercontent.com"
        client_secret = "client_secret.json"
        scopes = ['https://www.googleapis.com/auth/calendar']
        self.calendar_id = calendar_id
        self.service = create_service(client_secret, "calendar", "v3", scopes)

    # adds events to calendar, edit teh default temp w event data
    def add_events(self, data):
        for i in range(len(data['summary'])):

            summary = data['summary'][i]
            description = data['description'][i]
            start = data['start_time'][i]
            timezone = data['timezone'][i]
            location = data['location'][i]



            start = start.split("-")

            end = data['end-time'][i]
            end = end.split("-")


            year = start[0]
            month = start[1]
            temp = start[2]
            temp = temp.split("T")
            day = temp[0]
            temp1 = temp[1].split(":")
            hour = temp1[0]
            minute = temp[1]

            eyear = end[0]
            emonth = end[1]
            temp = end[2]
            temp = temp.split("t")
            eday = temp[0]
            temp1 = temp[1].split(":")
            ehour = temp1[0]
            eminute = temp[1]

            default_temp = {
                'summary': f'{summary}',
                'location': f'{location}',
                'description': f'{description}',
                'start': {
                    'dateTime': convert_to_RFC_datetime(year, month, day, hour, minute),
                    'timeZone': f'{timezone}',
                },
                'end': {
                    'dateTime': convert_to_RFC_datetime(eyear, emonth, eday, ehour, eminute),
                    'timeZone': f'{timezone}',
                },
                'recurrence': [
                    'RRULE:FREQ=DAILY;COUNT=2'
                ],
                'attendees': [

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

