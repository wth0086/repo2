from django.db import models
from django.utils import timezone


class Complain(models.Model):
    customer_ID = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    complain_type = models.CharField(max_length=100)
    room_number = models.IntegerField(default=0)
    employee_ID = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)
    complain_message = models.CharField(max_length=100)
    solved_message = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_ID


class types_of_complain(models.Model):
    code = models.CharField(max_length=100)
    explanation = models.CharField(max_length=100)

    def __str__(self):
        return self.code