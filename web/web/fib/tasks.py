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

    existing_max_index = fibs.aggregate(Max('index'))
    current_max_index = existing_max_index['index__max'] or 0
    fib_count = fibs.count()

    val1 = 0
    val2 = 1

    if current_max_index > 1:
        # Only start getting values from DB if there are 2 or more indexes stored
        second_to_max_index = current_max_index - 1
        val1 = int(fibs.get(index=current_max_index).fibonacci_number)
        val2 = int(fibs.get(index=second_to_max_index).fibonacci_number)

    index = current_max_index
    while index <= n:
        if index > 0 and index == current_max_index:
            index += 1
            continue

        if index == 0 and fib_count <= 0:
            # Case 1: When there is no existing data in db yet
            # Assume at 0 index which has 0 value
            fib = 0
            index = 0
        elif index == 0 and fib_count == 1:
            # Case 2: When there is existing data but only at index 0
            # Assume that we are at index 1 with value 1
            fib = 1
            index = 1
        else:
            fib = val1 + val2
            val2 = copy(val1)
            val1 = fib

        FibonacciHistory.objects.create(
            index=index,
            fibonacci_number=fib
        )

        print(f"Created fib index {index} with value {fib}")
        
        index += 1