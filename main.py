from time import perf_counter
import csv
import sys


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


def main():
    num = 3000
    write_file = open("paljon.csv", "w")
    writer = csv.writer(write_file, delimiter=",", lineterminator="\n")
    writer.writerow(["factorial", "with memo", "n"])

    sys.setrecursionlimit(3000)
    for i in range(0, num, 10):
        time_normal = calc_time(i, factorial)
        time_memo = calc_time(i, fact_memo)
        writer.writerow([time_normal, time_memo, i])
    
    write_file.close() 
    print("Done")
    input("Lopeta (0): ")

if __name__ == "__main__":
    main()
