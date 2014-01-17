from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=(('L', 'LOW'), ('H', 'HIGH'),))
    last_date = models.DateField()
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
