# Generated by Django 2.2.4 on 2019-08-14 21:44

from django.db import migrations, transaction
from django.db.models import Prefetch

BATCH_SIZE = 5000

STATUS_ACTIVE = "A"
STATUS_WAITING = "W"
STATUS_COMPLETED = "C"
STATUS_INTERRUPTED = "I"
STATUS_EXPIRED = "X"
STATUS_FAILED = "F"

EXIT_TYPE_COMPLETED = "C"
EXIT_TYPE_INTERRUPTED = "I"
EXIT_TYPE_EXPIRED = "E"


def calculate_status(run):  # pragma: no cover
    if run.session and run.session.status == STATUS_FAILED:
        return STATUS_FAILED

    if run.exit_type == EXIT_TYPE_COMPLETED:
        return STATUS_COMPLETED
    if run.exit_type == EXIT_TYPE_INTERRUPTED:
        return STATUS_INTERRUPTED
    if run.exit_type == EXIT_TYPE_EXPIRED:
        return STATUS_EXPIRED

    if run.exit_type:  # just in case there's an unrecognized exit_type
        return STATUS_COMPLETED

    if run.session and run.session.status == STATUS_WAITING and run.session.current_flow_id == run.flow_id:
        return STATUS_WAITING

    if run.is_active:
        return STATUS_ACTIVE

    # if the run isn't active.. but doesn't have an exit type.. then let's say it was interrupted
    return STATUS_INTERRUPTED


def populate_run_status(apps, schema_editor):  # pragma: no cover
    FlowRun = apps.get_model("flows", "FlowRun")
    FlowSession = apps.get_model("flows", "FlowSession")

    num_updated = 0
    max_id = -1
    while True:
        batch = list(
            FlowRun.objects.filter(status=None, id__gt=max_id)
            .only("id", "exit_type", "is_active", "flow_id", "session")
            .prefetch_related(Prefetch("session", FlowSession.objects.only("id", "status", "current_flow_id")))
            .order_by("id")[:BATCH_SIZE]
        )
        if not batch:
            break

        with transaction.atomic():
            for run in batch:
                run.status = calculate_status(run)
                run.save(update_fields=("status",))

        num_updated += len(batch)
        print(f" > Updated {num_updated} flow runs with a status")

        max_id = batch[-1].id


def reverse(apps, schema_editor):  # pragma: no cover
    pass


def apply_manual():  # pragma: no cover
    from django.apps import apps

    populate_run_status(apps, None)


class Migration(migrations.Migration):

    dependencies = [("flows", "0213_flowrun_status")]

    operations = [migrations.RunPython(populate_run_status, reverse)]
