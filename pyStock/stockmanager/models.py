from django.db import models


# Create your models here.
class Stock(models.Model):
    name_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_text
