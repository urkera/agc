from django.db import models


class Currency(models.Model):
    label = models.CharField(max_length=50, unique=True)
    ticker = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.ticker

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class Price(models.Model):
    currency = models.ForeignKey('Currency', on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField(auto_now=True)
    oopen = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    close = models.FloatField()
    average = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.currency.label

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
