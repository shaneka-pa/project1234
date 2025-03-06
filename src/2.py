def get_random_code(length=8):
    import random
    code = ''.join([str(random.randint(0, 9)) for i in range(length)])
    return code

get_random_code()
