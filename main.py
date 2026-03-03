import csv
import sys

import functions as f


def main():
    num = 3000
    write_file = open("results.csv", "w")
    writer = csv.writer(write_file, delimiter=",", lineterminator="\n")
    writer.writerow(["n", "factorial", "with memo", "iteration"])

    sys.setrecursionlimit(3000)
    for i in range(0, num, 10):
        time_normal = f.average_time(i, f.factorial)
        time_memo = f.average_mem_time(i, f.fact_memo)
        time_iter = f.average_time(i, f.fact_iter)
        writer.writerow([i, time_normal, time_memo, time_iter])

    write_file.close()
    print("Done")


if __name__ == "__main__":
    main()
