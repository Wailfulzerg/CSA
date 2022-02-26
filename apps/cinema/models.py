from django.db import models
from django.db.models import Count


class Cinema(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField(null=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    afisha_id = models.IntegerField(unique=True)

    @property
    def available_dates(self):
        result = (Event.objects
                  .values('date')
                  .annotate(dcount=Count('date'))
                  .order_by()
                  )
        return [str(i['date']) for i in result]


class Hall(models.Model):
    name = models.CharField(max_length=128)
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, related_name='halls')


class Event(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, related_name='events')
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, related_name='events')
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='events')
    date = models.DateField()
    time = models.TimeField()
