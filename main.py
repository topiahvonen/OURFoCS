import csv
import sys
import tracemalloc

import functions as f


def main():
    num = 3000
    write_file = open("results.csv", "w")
    writer = csv.writer(write_file, delimiter=",", lineterminator="\n")
    writer.writerow(
        [
            "n",
            "factorial t/s",
            "factorial mem/kB",
            "fact_memo t/s",
            "fact_memo mem/kB",
            "iteration t/s",
            "iteration mem/kB",
        ]
    )

    sys.setrecursionlimit(3000)
    for i in range(0, num, 10):
        tracemalloc.start()
        time_normal = f.calc_time(i, f.factorial)
        mem_normal = tracemalloc.get_traced_memory()[1] / (1024)
        tracemalloc.stop()
        tracemalloc.start()
        time_memo = f.calc_time(i, f.fact_memo)
        mem_memo = tracemalloc.get_traced_memory()[1] / (1024)
        tracemalloc.stop()
        tracemalloc.start()
        time_iter = f.calc_time(i, f.fact_iter)
        mem_iter = tracemalloc.get_traced_memory()[1] / (1024)
        tracemalloc.stop()

        writer.writerow(
            [i, time_normal, mem_normal, time_memo, mem_memo, time_iter, mem_iter]
        )

    write_file.close()
    print("Done")


if __name__ == "__main__":
    main()
