from django.db import models
from django.contrib.auth.models import User
from django import forms

class Complain(models.Model):

    address = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    description = models.TextField()
    ministry =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    approve = models.BooleanField(default=False)
    dateApprove = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.ministry

    def summary(self):
        return self.description[:50]

    def pub_date_up(self):
        return self.pub_date.strftime('%b %e %Y')