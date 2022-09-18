import time
from functools import lru_cache

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} with args: {args} took {str((end - start) * 1000)} mil sec")
        return result
    return wrapper

@time_it
@lru_cache
def recursive_fibonaci(num):
    if num <= 1:
        return num
    return recursive_fibonaci(num - 1) + recursive_fibonaci(num - 2)

@time_it
def fibonaci_dynamic(num):
    if num <= 1:
        return num
    mem = [0] * (num + 1)
    mem[1] = 1
    for i in range(2, num+1): #Plus 1 is due to the range not inclusive of end
        mem[i] = mem[i - 1] + mem[i - 2]

    return mem[num]

if __name__ == "__main__":

    fibo = recursive_fibonaci(100)
    print(fibo)