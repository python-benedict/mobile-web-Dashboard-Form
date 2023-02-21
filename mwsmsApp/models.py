from django.db import models
# from twilio.rest import Client
# import os

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname

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