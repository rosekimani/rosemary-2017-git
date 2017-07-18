from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    trainer = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.title
