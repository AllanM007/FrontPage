from django.db import models

class Headline(models.Model):
  title = models.CharField(max_length=200, null=True)
  image = models.URLField(null=True, blank=True)
  url = models.TextField(null=True)
  
  def __str__(self):
    return self.title