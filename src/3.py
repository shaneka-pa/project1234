import random

def get_random_number(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    return random.choice(numbers)