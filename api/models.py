from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    make  = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year  = models.IntegerField()
    owner = models.ForeignKey(User,
                related_name='cars', related_query_name='car')

    def __unicode__(self):
        return '{}'.format(self.id)
