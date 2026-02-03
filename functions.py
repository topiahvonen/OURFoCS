from time import perf_counter


def fact_iter(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return factorial(n - 1) * n


memory: dict = {0: 1}    # Base case
def fact_memo(n: int) -> int:
    if n in memory:
        return memory[n]
    memory[n] = fact_memo(n - 1) * n
    return memory[n]


def calc_time(n: int, f: function) -> float:
    start = perf_counter()
    f(n)
    end = perf_counter()
    return end - start

def average_time(n: int, f: function) -> float:
    time_sum: float = 0
    for _ in range(10):
        start = perf_counter()
        f(n)
        end = perf_counter()
        time_sum += (end - start)
    return time_sum / 10
