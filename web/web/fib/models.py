
from django.db import models


class FibonacciHistory(models.Model):
    index = models.IntegerField(unique=True,help_text="Index of fibonacci")

    # Use text field so no int limit
    fibonacci_number = models.TextField(help_text="Actual fibonacci")


