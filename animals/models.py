from django.db import models
import datetime
import uuid

class animal(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  name = models.CharField(max_length=64)
  age = models.IntegerField()
  image = models.ImageField(upload_to='images/%Y/%m/%d/')
  
  def __str__(self):
    return self.name