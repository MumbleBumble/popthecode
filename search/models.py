from django.db import models

class Browser(models.Model):
    name = models.CharField(max_length = 2)
    mozilla = models.CharField(max_length = 20)
    render = models.CharField(max_length = 75)
    after = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length = 2)
    paren = models.CharField(max_length = 75)
    mobile = models.CharField(max_length = 15)

    def __unicode__(self):
        return self.name
