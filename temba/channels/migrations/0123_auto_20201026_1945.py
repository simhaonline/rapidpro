# Generated by Django 2.2.10 on 2020-10-26 19:45

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import temba.channels.models
import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0122_populate_allow_international"),
    ]

    operations = [
        migrations.AlterField(model_name="channel", name="bod", field=models.TextField(null=True),),
        migrations.AlterField(model_name="channel", name="channel_type", field=models.CharField(max_length=3),),
        migrations.AlterField(
            model_name="channel", name="config", field=temba.utils.models.JSONAsTextField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="org",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="channels", to="orgs.Org"
            ),
        ),
        migrations.AlterField(
            model_name="channel",
            name="parent",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="channels.Channel"),
        ),
        migrations.AlterField(model_name="channel", name="role", field=models.CharField(default="SR", max_length=4),),
        migrations.AlterField(
            model_name="channel",
            name="schemes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=16),
                default=temba.channels.models._get_default_channel_scheme,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="channelevent",
            name="channel",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="channels.Channel"),
        ),
        migrations.AlterField(
            model_name="channelevent",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="channel_events", to="contacts.Contact"
            ),
        ),
        migrations.AlterField(
            model_name="channelevent",
            name="contact_urn",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_events",
                to="contacts.ContactURN",
            ),
        ),
        migrations.AlterField(
            model_name="channelevent",
            name="created_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="channelevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("unknown", "Unknown Call Type"),
                    ("mt_call", "Outgoing Call"),
                    ("mt_miss", "Missed Outgoing Call"),
                    ("mo_call", "Incoming Call"),
                    ("mo_miss", "Missed Incoming Call"),
                    ("stop_contact", "Stop Contact"),
                    ("new_conversation", "New Conversation"),
                    ("referral", "Referral"),
                    ("welcome_message", "Welcome Message"),
                ],
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="channelevent", name="extra", field=temba.utils.models.JSONAsTextField(default=dict, null=True),
        ),
        migrations.AlterField(model_name="channelevent", name="occurred_on", field=models.DateTimeField(),),
        migrations.AlterField(
            model_name="channelevent",
            name="org",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="orgs.Org"),
        ),
        migrations.AlterField(
            model_name="channellog",
            name="channel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="logs", to="channels.Channel"
            ),
        ),
        migrations.AlterField(
            model_name="channellog",
            name="connection",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="channel_logs",
                to="channels.ChannelConnection",
            ),
        ),
        migrations.AlterField(
            model_name="channellog", name="created_on", field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(model_name="channellog", name="description", field=models.CharField(max_length=255),),
        migrations.AlterField(model_name="channellog", name="is_error", field=models.BooleanField(default=False),),
        migrations.AlterField(
            model_name="channellog", name="method", field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name="channellog",
            name="msg",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="channel_logs", to="msgs.Msg"
            ),
        ),
        migrations.AlterField(model_name="channellog", name="request", field=models.TextField(null=True),),
        migrations.AlterField(model_name="channellog", name="request_time", field=models.IntegerField(null=True),),
        migrations.AlterField(model_name="channellog", name="response", field=models.TextField(null=True),),
        migrations.AlterField(model_name="channellog", name="response_status", field=models.IntegerField(null=True),),
        migrations.AlterField(model_name="channellog", name="url", field=models.TextField(null=True),),
        migrations.AlterField(
            model_name="syncevent",
            name="channel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="sync_events", to="channels.Channel"
            ),
        ),
        migrations.AlterField(
            model_name="syncevent", name="incoming_command_count", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="syncevent", name="lifetime", field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(model_name="syncevent", name="network_type", field=models.CharField(max_length=128),),
        migrations.AlterField(
            model_name="syncevent", name="outgoing_command_count", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="syncevent", name="pending_message_count", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(model_name="syncevent", name="power_level", field=models.IntegerField(),),
        migrations.AlterField(
            model_name="syncevent",
            name="power_source",
            field=models.CharField(
                choices=[("AC", "A/C"), ("USB", "USB"), ("WIR", "Wireless"), ("BAT", "Battery")], max_length=64
            ),
        ),
        migrations.AlterField(
            model_name="syncevent",
            name="power_status",
            field=models.CharField(
                choices=[
                    ("UNK", "Unknown"),
                    ("CHA", "Charging"),
                    ("DIS", "Discharging"),
                    ("NOT", "Not Charging"),
                    ("FUL", "FUL"),
                ],
                default="UNK",
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name="syncevent", name="retry_message_count", field=models.IntegerField(default=0),
        ),
    ]