from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    hometown = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title