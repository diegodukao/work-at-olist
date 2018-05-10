from django.db import models


class Call(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=11, null=True)
    destination = models.CharField(max_length=11, null=True)


class CallRecord(models.Model):
    CALL_START = 1
    CALL_END = 2
    RECORD_TYPES = [
        (CALL_START, 'start'),
        (CALL_END, 'end'),
    ]
    original_id = models.IntegerField(null=True)
    record_type = models.SmallIntegerField(choices=RECORD_TYPES)
    call = models.ForeignKey('calls.Call', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
