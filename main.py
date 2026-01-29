import csv
import sys

from functions import *


def main():
    num = 3000
    write_file = open("results.csv", "w")
    writer = csv.writer(write_file, delimiter=",", lineterminator="\n")
    writer.writerow(["n", "factorial", "with memo", "iteration"])

    sys.setrecursionlimit(3000)
    for i in range(0, num, 10):
        time_normal = calc_time(i, factorial)
        time_memo = calc_time(i, fact_memo)
        time_iter = calc_time(i, fact_iter)
        writer.writerow([i, time_normal, time_memo, time_iter])
    
    write_file.close() 
    print("Done")


if __name__ == "__main__":
    main()
