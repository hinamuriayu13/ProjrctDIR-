from django.db import models

# Create your models here.
class Currency(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    currency_name = models.CharField(max_length=50)

    def __str__(self):
        return self.currency_name
    
class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, related_name='base_currency', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_currency', on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.base_currency} to {self.target_currency}: {self.rate}"
