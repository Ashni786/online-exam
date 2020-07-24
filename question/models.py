from django.contrib.auth.models import User
from django.db import models

class Questions(models.Model):
    CAT_CHOICES = (
    ('ComputerScience', 'Computer Science'),
    ('Histroy', 'Histroy'),
    ('Science', 'Science'),
    ('ArtandLiterature', 'Art and Literature'),
    ('Geography','Geography'),
    ('Music','Music '),
    ('movies','Movies'),
    ('maths','Maths'),
    ('generalknowledge','GeneralKnowledge')
    )
    catagory = models.CharField(max_length=25, choices=CAT_CHOICES)
    question = models.TextField(max_length=500)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    choose = (('A', 'optiona'), ('B', 'optionb'), ('C', 'optionc'), ('D', 'optiond'))
    answer = models.CharField(max_length=1, choices=choose)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question


class Feedback(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return 'Feedback from' + ' ' + self.name


