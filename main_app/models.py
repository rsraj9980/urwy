from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(1-5)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    endDate = models.DateField()
    createDate = models.DateField() #should be provided by the browser no?
    bid = models.IntegerField()
    budget = models.IntegerField()
    category = models.ManyToManyField(Category)
    # add more properties here! :D 
    
    def __str__(self):
        return self.title


