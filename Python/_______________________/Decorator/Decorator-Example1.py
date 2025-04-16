from time import time


def speed_test(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed : {end_time - start_time}")
        return result

    return wrapper


@speed_test
def sum_list():
    return sum([x for x in range(40000000)])


@speed_test
def sum_gen():
    return sum(x for x in range(40000000))


sum_gen()
sum_list()
