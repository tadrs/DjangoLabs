from django.db import models
from course.models import Course
# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='trainees/')
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)



