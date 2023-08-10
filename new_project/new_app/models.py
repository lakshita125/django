from django.db import models


class Students(models.Model):
  name = models.TextField(max_length=255)
  email = models.EmailField()
  roll_no=models.IntegerField(primary_key=True)
  DOA=models.DateField(auto_now_add=True)

class classroom(models.Model):
  name_of_class=models.TextField()
  class_teacher=models.TextField(max_length=20)
  
class teachers(models.Model):
  name_teacher=models.TextField()
  sub_teacher=models.TextField()
  teacher_id=models.IntegerField(primary_key=True) 
  
class marks(models.Model):
  maths= models.IntegerField()
  science=models.IntegerField()
  english=models.IntegerField()  
  computer=models.IntegerField()  
  #def _str_(self):
   # return self.name
# Create your models here.

