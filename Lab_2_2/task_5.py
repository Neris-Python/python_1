def cache(func):
    cache_dict = {}
    def wrapper(*args):
        key = ()
        for a in args:
            key += (a,)
        if key in cache_dict:
            return cache_dict[key]
        else:
            result = func(*args)
            cache_dict[key] = result
            return result
    return wrapper
import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        print("Время выполнения функции", func.__name__, elapsed_ms,  "мс")
        return result
    return wrapper

@timing
@cache
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
print("fib(5):", fib(5))
print("\n Второй вызов fib(5) (должен из кэша) ")
print("fib(5) снова:", fib(5))
print("\n Вызов fib(3) (новый, но частично из кэша от fib(5)) ")
print("fib(3):", fib(3))
