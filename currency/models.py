from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=50)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker
