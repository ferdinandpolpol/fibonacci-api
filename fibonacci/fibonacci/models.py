
from django.db import models, Max


class FibonacciHistory(models.Model):
    index = models.IntegerField(help_text="Index of fibonacci")
    fibonacci_number = models.BigIntegerField(help_text="Actual fibonacci")


