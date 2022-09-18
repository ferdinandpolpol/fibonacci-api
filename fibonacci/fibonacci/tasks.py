from celery import task

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
    
    fibs = FibonacciHistory.objects.all()

    current_max = fibs.aggregate(Max('index'))
    second_max = current_max - 1
    
    val1 = 0
    val2 = 1
    if current_max <= 0:
        pass
    else:
        val1 = fibs.filter(index=current_max).fibonacci_number
        val2 = fibs.filter(index=second_max).fibonacci_number


    current_max 

    while current_max <= n:
        fib = val1 + val2

        FibonacciHistory.objects.create(
            index=current_max,
            fibonacci_number=fib
        )
        tmp = copy(val1)
        val1 = fib
        val2 = tml
        current_max += 1
