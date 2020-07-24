from django.contrib.auth.models import User
from django.db import models

class Questions(models.Model):
    CAT_CHOICES = (
    ('ComputerScience', 'Computer Science'),
    ('Histroy', 'Histroy'),
    ('Science', 'Science'),
    ('ArtandLiterature', 'Art and Literature'),
    ('Geography', 'Geography'),
    ('Music', 'Music '),
    ('movies', 'Movies'),
    ('maths', 'Maths'),
    ('generalknowledge', 'GeneralKnowledge'),
    )
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question


class result(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=10)
    maxscore = models.CharField(max_length=10)




