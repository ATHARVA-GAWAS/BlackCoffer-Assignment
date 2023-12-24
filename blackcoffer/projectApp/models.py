from django.db import models

# Create your models here.
class Data(models.Model):
    end_year=models.CharField(max_length=100)
    intensity=models.IntegerField(null=True,blank=True)
    sector=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    insight=models.CharField(max_length=100)
    url=models.URLField(max_length=100)
    region=models.CharField(max_length=100)
    start_year=models.CharField(max_length=100)
    impact=models.CharField(max_length=100)
    added=models.CharField(max_length=100)
    published=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    relevance=models.IntegerField(null=True,blank=True)
    pestle=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    likelihood=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.title