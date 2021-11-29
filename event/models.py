from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.category}"


class Event(models.Model):
    title  = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    location  = models.CharField(max_length=64)
    startDate = models.DateField()
    endDate = models.DateField()
    image   = models.ImageField(upload_to="eventimg")
    published = models.BooleanField()
    paid = models.BooleanField()
    categories = models.ManyToManyField(Category, blank=True, related_name="events")
    


