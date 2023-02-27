from django.db import models
from django.utils import timezone
# from twilio.rest import Client
# import os

CHOICES = (
    ("YES", "YES"),
    ("NO", "NO"),
)


class MyModel(models.Model):
    date = timezone.now()
    fullname = models.CharField(max_length=200, blank=True)
    mobile_number = models.IntegerField(blank=True)
    eaten = models.CharField(max_length=10, choices=CHOICES, default='NO', blank=True)
    eaten_report = models.CharField(max_length=200, default="none", blank=True)
    slept = models.CharField(max_length=10, choices=CHOICES, default='NO',blank=True)
    slept_report = models.CharField(max_length=200, default="none", blank=True)
    active = models.CharField(max_length=10, choices=CHOICES, default="NO", blank=True)
    kid_fight = models.CharField(max_length=10, choices=CHOICES, default="NO", blank=True)
    fight_report = models.CharField(max_length=200, default="none", blank=True)
    health_problem = models.CharField(max_length=10, choices=CHOICES, default="NO", blank=True)
    health_problem_report = models.CharField(max_length=200, default="none", blank=True)
    toilet = models.CharField(max_length=10, choices=CHOICES, default="NO", blank=True)
    toilet_report = models.CharField(max_length=200, default="none", blank=True)
    class_participation = models.CharField(max_length=10, choices=CHOICES, default="NO", blank=True)
    class_participation_report = models.CharField(max_length=200, default="none", blank=True)
    kid_attitude = models.CharField(max_length=200, default="NONE", blank=True)
    academic_performance = models.CharField(max_length=200, default="NONE", blank=True)
    kid_interest = models.CharField(max_length=200, default="NONE", blank=True)
    teacher_name = models.CharField(max_length=30, default="NONE", blank=True)
    general_comment = models.CharField(max_length=300, default="NONE", blank=True)
    

    def __str__(self):
        return self.fullname + " - " + str(self.date)

    # def save(self, *args, **kwargs):
    #     if self.fullname:
    #         account_sid = os.environ['AC2e802620fbd1776456e14fc4bd568d2e']
    #         auth_token = os.environ['9e1a32852676186c612607a654b845a0']
    #         client = Client(account_sid, auth_token)

    #         message = client.messages \
    #                         .create(
    #                             body="A form has been created successfully for - {self.fullname}.",
    #                             from_='+16822376264',
    #                             to='+233546873228'
    #                         )

    #         print(message.sid)
    #     return super().save(*args, **kwargs)