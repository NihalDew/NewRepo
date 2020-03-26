from django.db import models

# Create your models here.
class Mark(models.Model):
    name = models.CharField(max_length=20)
    Roll = models.CharField(max_length=40)
    sub_1 = models.IntegerField()
    sub_2 = models.IntegerField()
    sub_3 = models.IntegerField()
    percent = models.IntegerField(default=0)

    def __str__(self):
        return self.name
