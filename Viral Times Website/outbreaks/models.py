from django.db import models

# Create your models here.
class Outbreak(models.Model):
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=200, default='', blank=True)
    disease = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100)
    death_toll_low = models.IntegerField()
    death_toll_high = models.IntegerField()
    transmission_type = models.CharField(max_length=100)
    regions_affected = models.TextField()
    symptoms = models.TextField()
    impact = models.TextField()

    def __str__(self):
        return self.name

class Report(models.Model):
    outbreak = models.ForeignKey(Outbreak, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    published = models.DateField()
    link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.title} ({self.outbreak.name})"
