from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
DIFFICULTY = (
  ('E', 'Easy'),
  ('I', 'Intermediate'),
  ('H', 'Hard')
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(
        'difficulty selection',
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[0][0]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks_create')
        # kwargs={'pk': self.id}

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField('Description', max_length=250)
    createDate = models.DateField('Created Date', default= timezone.now) #should be provided by the browser no?
    endDate = models.DateField('End Date')
    budget = models.IntegerField()
    categories = models.ManyToManyField(Category) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # add more properties here! :D 
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'task_id': self.id})


class Bid(models.Model):
    amount = models.IntegerField()
    date = models.DateField('Date', default= timezone.now)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount}"