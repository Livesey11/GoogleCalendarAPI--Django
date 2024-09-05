from django.db.models import PositiveIntegerField, SET_NULL, CharField, DateTimeField, IntegerChoices
from packages.toraja.model.abstract import StandardAbstract
from user.models import User


class MeetingScheduleStatus(IntegerChoices):
    Draft = 1
    Confirmed = 2
    Posted = 3


class MeetingSchedule(StandardAbstract):
    topic = CharField(max_length=255, null=False, blank=False, editable=True)
    descriptions = CharField(max_length=255, null=False, blank=False, editable=True, default="")
    start_dates = DateTimeField(null=True, blank=True, editable=True)
    end_dates = DateTimeField(null=True, blank=True, editable=True)
    # name_user = OneToOneField(User, null=True, on_delete=SET_NULL, blank=False, editable=True)
    status = PositiveIntegerField(choices=MeetingScheduleStatus.choices, null=True, blank=True, editable=True, default=MeetingScheduleStatus.Draft)
    location = CharField(max_length=255, null=False, blank=False, editable=True, default="")

    key_fields = ['topic']
    displays = ['topic, user']