from django.db import models
from django.utils import timezone

class Map(models.Model):
    coord_lats = models.FloatField()
    coord_lons = models.FloatField()

    def __str__(self):
        return self.title
