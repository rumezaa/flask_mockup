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
            timezone = data['time_zone'][i]
            location = data['location'][i]
            end = data['end-time'][i]


            start = start.split("-")
            end = end.split("-")


            start_year = int(start[0])
            print(start_year)
            start_month = int(start[1])
            temp = start[2].split("T")
            start_day = int(temp[0])
            temp1 = temp[1].split(":")

            start_hour = int(temp1[0])
            start_minute = int(temp1[1])
            print(start_minute)

            end_year = int(end[0])
            end_month = int(end[1])
            tem = end[2].split("T")
            end_day = int(tem[0])
            te = tem[1].split(":")
            end_hour = int(te[0])
            end_minute = int(te[1])

            default_temp = {
                'summary': f'{summary}',
                'location': f'{location}',
                'description': f'{description}',
                'start': {
                    'dateTime': convert_to_RFC_datetime(start_year, start_month, start_day, start_hour, start_minute),
                    'timeZone': f'{timezone}',
                },
                'end': {
                    'dateTime': convert_to_RFC_datetime(end_year, end_month, end_day, end_hour, end_minute),
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

