from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateField('events time')
    create_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Guest(models.Model):
    event_id = models.ForeignKey(Event)
    guest_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateField(auto_now=True)

class Meta:
    unique_together = ('event', 'phone')

def __str__(self):
    return self.guest_name

