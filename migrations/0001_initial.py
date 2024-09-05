# Generated by Django 3.2 on 2022-08-23 15:38

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='MeetingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('sync_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('topic', models.CharField(max_length=255)),
                ('descriptions', models.CharField(default='', max_length=255)),
                ('start_dates', models.DateTimeField(blank=True, null=True)),
                ('end_dates', models.DateTimeField(blank=True, null=True)),
                ('status', models.PositiveIntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Confirmed'), (3, 'Posted')], default=1, null=True)),
                ('location', models.CharField(default='', max_length=255)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_googlecalendar_meetingschedules', to='user.user')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by_googlecalendar_meetingschedules', to='user.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalMeetingSchedule',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('modified_at', models.DateTimeField(blank=True, editable=False)),
                ('sync_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('topic', models.CharField(max_length=255)),
                ('descriptions', models.CharField(default='', max_length=255)),
                ('start_dates', models.DateTimeField(blank=True, null=True)),
                ('end_dates', models.DateTimeField(blank=True, null=True)),
                ('status', models.PositiveIntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Confirmed'), (3, 'Posted')], default=1, null=True)),
                ('location', models.CharField(default='', max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.user')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='user.user')),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.user')),
            ],
            options={
                'verbose_name': 'historical meeting schedule',
                'verbose_name_plural': 'historical meeting schedules',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
