from django.db import models

# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.color_name
    

class Person(models.Model):
    color = models.ForeignKey(Color, null = True, blank = True, related_name = ("color"), on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
        