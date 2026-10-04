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
from quicksort import *

SIZES = [4, 6, 8]
TRIALS = 10
ALGORITHMS = {"mergesort": mergeSort, "quicksort": quicksort}

def benchmark(sort_algorithm, inputs, trials=TRIALS):
    trial_times = []
    for trial in range(trials):
        start = time.perf_counter()
        for arr in inputs:
            sort_algorithm(arr)
        end = time.perf_counter()
        trial_times.append(end - start)
    return trial_times

if __name__ == "__main__":
    rows = []
    print(f"{'algorithm':<10} {'size' :>4} {'arrays':>7} {'trial':>5} {'total (s)':>10} {'per sort (microseconds)':>14}")

    for name, sort_algorithm in ALGORITHMS.items():

        for size in SIZES:
            inputs = generatePermutations(list(range(1, size + 1)))
            count = len(inputs)
            trial_times = benchmark(sort_algorithm, inputs)

            for trial, total in enumerate(trial_times, start=1):
                per_sort_us = total / count * 1_000_000
                print(f"{name:<10} {size:>4} {count:>7} {trial:>5} {total:>10.4f} {per_sort_us:>14.2f}")
                rows.append([name, size, count, trial, total, per_sort_us])

            best = min(trial_times)
            print(f" -> {name}, size {size}: best total {best:.4f}s, "
              f"avg per sort {best / count * 1_000_000:.2f} microseconds\n")

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["algorithm", "sizes", "arrays_sorted", "trial", "total_seconds", "per_sort_microseconds"])
    writer.writerows(rows)
