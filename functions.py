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


memory = {}
def fact_memo(n: int) -> int:
    if n == 0:
        return 1
    elif n in memory:
        return memory[n]
    memory[n] = fact_memo(n - 1) * n
    return memory[n]


def calc_time(n: int, f) -> float:
    start = perf_counter()
    f(n)
    end = perf_counter()
    return end - start