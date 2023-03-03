from modules import *

column = 'Unnamed: 0'


class Event:
    @staticmethod
    def find_row_index(df, name):
        row_index = df[df[column] == name].index[0]
        return row_index

    @staticmethod
    def extractor(xlsx_path: str, name: str):
        df = pd.read_excel(
            xlsx_path,
            sheet_name=0)

        values = {}

        for i, column in enumerate(df.columns):
            value1 = column
            value2 = df.iloc[Event.find_row_index(df, name), i]

            if pd.notnull(value2):
                values[value1] = value2

        return values

    @staticmethod
    def create_event(values):
        creds = None

        SCOPES = ['https://www.googleapis.com/auth/calendar']

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        for date, shift_time in values.items():
            if '-' in shift_time:
                start, end = shift_time.split("-")
                event_date = date.strftime("2023-%m-%d")
                event_start = f"{event_date}T{start}:00"
                event_end = f"{event_date}T{end}:00"

                event = {
                    'summary': 'Jobb',
                    'start': {
                        'dateTime': event_start,
                        'timeZone': 'Europe/Stockholm',
                    },
                    'end': {
                        'dateTime': event_end,
                        'timeZone': 'Europe/Stockholm',
                    },
                }

                event = service.events().insert(
                    calendarId='primary',
                    body=event).execute()
                link_to_event = (event.get('htmlLink'))
                print(f"✅ Event created: {link_to_event}")
