from pprint import pprint
from config.admin import Create_Service
from packages.toraja.command.duplicate.abstract import BaseCommand
from googlecalendar.models import MeetingSchedule, MeetingScheduleStatus


class Command(BaseCommand):

    def google_api(self):

        CLIENT_SECRET_FILE = "client_secret_853798205580-2tvs2gg4svrbe0aqtis37f1gmav1nou2.apps.googleusercontent.com.json"
        API_NAME = 'googlecalendar'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/calendar']

        # if MeetingSchedule.objects.filter('status') == New :

        meeting_schedules = MeetingSchedule.objects.filter(status=MeetingScheduleStatus.Confirmed)
        for meeting_schedule in meeting_schedules:
            print(f"Topik               : {meeting_schedule.topic}")
            print(f"Deskripsi           : {meeting_schedule.descriptions}")
            print(f"Status              : {meeting_schedule.status}")
            print(f"Lokasi              : {meeting_schedule.location}")
            print(f"Waktu Mulai         : {meeting_schedule.start_dates}")
            print(f"Waktu Selesai       : {meeting_schedule.end_dates}")


        # else:
        #     print("Meeting already set or passed")

            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

            request_body = {
                'summary': meeting_schedule.topic
            }
            # #
            # to create
            response = service.calendars().insert(body=request_body).execute()
            print(response)

            calendar_id_latihan = response['id']

            # to CRUD Google Calendar API
            colors = service.colors().get().execute()
            pprint(colors)

            recurrence = [
                'RRULE:FREQ=MONTHLY;COUNT=2'
            ]

            # hour_adjustment = -7

            event_request_body = {
                # 'start': {
                #     'dateTime': convert_to_RFC_datetime(2022, 8, 20, 11 + hour_adjustment, 30),
                #     'timezone': 'Asia/Jakarta'
                # },
                # 'end': {
                #     'dateTime': convert_to_RFC_datetime(2022, 8, 20, 12 + hour_adjustment, 30),
                #     'timezone': 'Asia/Jakarta'
                # },

                "start": {
                    "dateTime": meeting_schedule.start_dates.isoformat() + 'Z',
                    "timezone": 'Asia/Jakarta'
                },
                "end": {
                    "dateTime": meeting_schedule.end_dates.isoformat() + 'Z',
                    "timezone": 'Asia/Jakarta'
                },
                "summary": meeting_schedule.topic,
                "description": meeting_schedule.descriptions,
                'colorId': 5,
                'status': 'confirmed',
                'transparency': 'opaque',
                'visibility': 'private',
                "location": meeting_schedule.location,
                'attachment': [
                    {
                        'fileUrl': None,
                        'title': 'Meeting Merdeka'
                    }
                ],
                'attendees': [
                    {
                        'displayName': 'ADMIN',
                        'comment': 'Admin Meeting',
                        'email': 'izmo.software@gmail.com',
                        'optional': False,
                        'organizer': True,
                        'responseStatus': 'accepted'
                    }
                ],
                'reccurence': recurrence
            }

            maxAttendees = 15
            sendNotification = True
            sendUpdate = 'none'
            supportsAttachments = True
            events = service.events()
            # resp = calendar_list = service.calendarList().list(pageToken=None).execute()
            # print(1, resp)
            # resp = service.calendarList().get(calendarId=calendar_id_latihan).execute()
            # print(2, resp)
            response = events.insert(
                calendarId=calendar_id_latihan,
                maxAttendees=maxAttendees,
                sendNotifications=sendNotification,
                sendUpdates=sendUpdate,
                supportsAttachments=supportsAttachments,
                body=event_request_body,
            ).execute()
            pprint(response)

            meeting_schedule.status = MeetingScheduleStatus.Posted
            meeting_schedule.save()

            # MeetingSchedule.objects.filter(status=2)
            # MeetingSchedule.save(update_fields=["status"])

            # MeetingSchedule.objects.filter(pk=meeting_schedule.pk).update(active=True)

            # eventId = response['id']
            #
            # start_datetime = meeting_schedule['start_dates'].isoformat() + 'Z'
            # end_datetime = meeting_schedule['end+_dates'].isoformat() + 'Z'
            # response['start']['dateTime'] = start_datetime
            # response['end']['dateTime'] = end_datetime
            # response['summary'] = 'Lunch'
            # response['Description'] = 'Having Lunch Meeting'
            # service.events().update(
            #     calendarId=calendar_id_latihan,
            #     eventId=eventId,
            #     body=response
            # ).execute()

            # service.events().delete(calendarId=calendar_id_latihan, eventId=eventId).execute()
            #
            # print(dir(service))

    def handle(self, *args, **options):
        self.google_api()


