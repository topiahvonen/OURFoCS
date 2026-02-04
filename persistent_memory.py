import sys
import pickle
import time
from functions import factorial, fact_memo
import csv


class Memory:
    memory: dict = {}
    filename: str = "memory.pkl"

    def __init__(self, filename):
        self.filename = filename
        self.memory = self.read_file()

    def read_file(self) -> dict:
        try:
            file = open(self.filename, "rb")
            memory = pickle.load(file)
            file.close()
        except OSError as e:
            print("Avaus ei onnistunut:")
            print(e)
            sys.exit(0)
        return memory

    def write_file(self):
        try:
            file = open(self.filename, "wb")
            pickle.dump(self.memory, file)
            file.close()
        except OSError as e:
            print("Kirjoitus ei onnistunu:")
            print(e)
            sys.exit(0)
        return None

    def fact_with_memory(self: Memory, n: int) -> int:
        if n == 0:
            return 1
        elif n in self.memory:
            return self.memory[n]
        self.memory[n] = self.fact_with_memory(n - 1) * n
        return self.memory[n]


def time_func(f: function, n: int):
    start = time.perf_counter()
    for i in range(1, n, 10):
        f(i)
    end = time.perf_counter()
    return end - start


def time_memory(n: int):
    start = time.perf_counter()
    mem = Memory("memory.pkl")
    for i in range(1, n, 10):
        mem.fact_with_memory(i)
    mem.write_file()
    end = time.perf_counter()
    return end - start


def main():
    sys.setrecursionlimit(1030)
    write_file = open("memory_results.csv", "w")
    writer = csv.writer(write_file, delimiter=",", lineterminator="\n")
    writer.writerow(["factorial", "fact_memo", "persistent"])

    for _ in range(100):
        time_factorial = time_func(factorial, 1000)
        time_fact_memo = time_func(fact_memo, 1000)
        time_persistent = time_memory(1000)
        writer.writerow([time_factorial, time_fact_memo, time_persistent])

    write_file.close()


if __name__ == "__main__":
    main()
