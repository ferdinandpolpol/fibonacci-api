from copy import copy
from celery import task

from django.db.models import Max

from .models import FibonacciHistory

@task()
def create_fibonacci(n):
    """
    Description:
        Calculates the nth fibonacci number and stores it in the database.
    Parameters:
        n (int): the ordinal of the fibonacci number to calculate
    Returns:
        None
    """
    # 0,1,1,2,3,5,8,13,etc
    n = int(n)
    fibs = FibonacciHistory.objects.all()
    index = 0

    max_num = fibs.aggregate(Max('index'))
    current_max = max_num['index__max'] or 0
    
    val1 = 0
    val2 = 1
    if current_max <= 0:
        pass
    else:
        second_max = current_max - 1
        val1 = int(fibs.get(index=current_max).fibonacci_number)
        val2 = int(fibs.get(index=second_max).fibonacci_number)
        index = current_max + 1

    while index <= n:
        # Edge case if there is no current fib sequence
        if index == 0:
            fib = 0
            val1 = 0
            val2 = 1
        else:
            fib = val1 + val2
            tmp = copy(val1)
            val1 = fib
            val2 = tmp

        FibonacciHistory.objects.create(
            index=index,
            fibonacci_number=fib
        )

        print(f"Created fib index {index} with value {fib}")
        
        index += 1