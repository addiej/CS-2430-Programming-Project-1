'''#TODO author: Addie Hurst'''
# TODO:
# - Generate values from 0 through n - 1.
# - Replace timing measurements with comparison counts.
# - Run all four sorting algorithms on every permutation.
# - Record algorithm name, original array, and comparison count.
# - Find the best 10 and worst 10 cases for each algorithm and n.
# - Calculate average comparisons for each algorithm and n.
# - Make sure sorting does not destroy the original unsorted permutation.
# - Output clearly labeled results for n = 4, 6, and 8.

'''Code Author: Erich M.'''
import time
import csv
from permutations import *
from mergesort import *

SIZES = [4, 6, 8]
TRIALS = 10

def benchmark(size, trials=TRIALS):

    inputs = generatePermutations(list(range(1, size + 1)))

    trial_times = []
    for trial in range(trials):
        start = time.perf_counter()
        for arr in inputs:
            mergeSort(arr)
        end = time.perf_counter()
        trial_times.append(end - start)
    return len(inputs), trial_times

if __name__ == "__main__":
    rows = []
    print(f"{'size' :>4} {'arrays':>7} {'trial':>5} {'total (s)':>10} {'per sort (microseconds)':>14}")

    for size in SIZES:
        count, trial_times = benchmark(size)
        for trial, total in enumerate(trial_times, start=1):
            per_sort_us = total / count * 1_000_000
            print(f"{size:>4} {count:>7} {trial:>5} {total:>10.4f} {per_sort_us:>14.2f}")
            rows.append([size, count, trial, total, per_sort_us])

        best = min(trial_times)
        print(f" -> size {size}: best total {best:.4f}s, "
              f"avg per sort {best / count * 1_000_000:.2f} microseconds\n")

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sizes", "arrays_sorted", "trial", "total_seconds", "per_sort_microseconds"])
    writer.writerows(rows)
