from django.db import models


# Create your models here.
# The model name 'Topic' will be the name of the table in the databse.
# model (1)
class Topic(models.Model):

    topic_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.topic_name


# model (2)
class Webpage(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


# model (3)
class AccessRecord(models.Model):

    topic = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


# model (4)
class FormData(models.Model):

    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    text = models.CharField(max_length=512)

    def __str__(self):
        return self.name
