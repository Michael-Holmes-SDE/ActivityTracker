from django.db import models
from django.utils import timezone

class Activity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def time_spent(self):
        delta = timezone.timedelta()
        for timelog in self.timelog_set.all():
            delta += (timelog.end_time - timelog.start_time)
        return delta

class TimeLog(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.TextField()

    def __str__(self):
        return f"Time Log for {self.activity} ({self.start_time} - {self.end_time} - {self.duration})"
     