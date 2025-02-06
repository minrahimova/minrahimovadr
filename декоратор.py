import time


def log_function_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__}  with args:{args} , kwargs:{kwargs}")
        print(f"{func.__name__} returned: {result}")
        print(f"Result: {result}")
        return result
    return wrapper


@log_function_calls
def multiply_numbers(x, y):
    return x * y





def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function calculate_multiply took {time.time() - start} seconds to execute")
        return result

    return wrapper

@measure_execution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
    return tot




class CacheResult:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args, **kwargs):

        if self.cache.get(str((args,kwargs))):
            print("Retrieving result from cache...")
        else:
            self.cache[str((args, kwargs))] = self.func(*args, **kwargs)
        return self.cache.get(str((args,kwargs)))
@CacheResult
def calculate_multiply(x, y):
    print("Calculating the product of two numbers...")
    return x * y


class RateLimiter:
    def __init__(self, max_calls, period):
            self.max_calls = max_calls
            self.period = period
            self.calls = []
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            i= 1
            t = time.time()
            while i < self.max_calls:
                if i > len(self.calls) or t -self.calls[-i] >  self.period:
                    self.calls.append(t)
                    return func(*args, **kwargs)
                i+=1
            raise Exception("Rate limit exceeded. Please try again later.")

        return wrapper
@RateLimiter(max_calls=4, period=3)
def api_call():
    time.sleep(0.1)
    print("API call executed successfully...")
    # Выполнить вызовы API

# multiply_numbers(10, 5)

# print(calculate_multiply([1, 2, 3, 4, 5]))

# print(calculate_multiply(4, 5))  # Вычисление выполняется
# print(calculate_multiply(4, 5))  # Результат извлекается из кэша
# print(calculate_multiply(5, 7))  # Вычисление выполняется
# print(calculate_multiply(5, 7))  # Результат извлекается из кэша
# print(calculate_multiply(-3, 7)) # Вычисление выполняется
# print(calculate_multiply(-3, 7))

# for _ in range(8):
#     try:
#         api_call()
#     except Exception as e:
#         print(f"Error occurred: {e}")
# time.sleep(10)
# api_call()