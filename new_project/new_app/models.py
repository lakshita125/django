from django.db import models


class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def _str_(self):
    return self.name
# Create your models here.
