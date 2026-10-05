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
from shakersort import *

SIZES = [4, 6, 8]
ALGORITHMS = {"mergesort": mergeSort, "quicksort": quicksort, "shakersort": shakerSort}

def countComparisons(sort_algorithm, inputs):
    #Pass a copy so the original permutation can never be changed
    result, comparisons = sort_algorithm(list(inputs))

    #Sanity check that the algorithm actually sorted correctly
    assert result == sorted(inputs), \
        f"{sort_algorithm.__name__} failed on {inputs}!"
    return comparisons

if __name__ == "__main__":
    records = []

    for size in SIZES:

        permutations = generatePermutations(list(range(size)))

        print("=" * 60)
        print(f"RESULTS FOR n = {size}")
        print("=" * 60)

        for name, sort_algorithm in ALGORITHMS.items():
            group = []
            for permutation in permutations:
                comparisons = countComparisons(sort_algorithm, permutation)
                group.append((name, size, tuple(permutation), comparisons))
            records.extend(group)

            average = sum(r[3] for r in group) / len(group)
            best10 = sorted(group, key=lambda r: r[3])[:10]
            worst10 = sorted(group, key=lambda r: r[3], reverse=True)[:10]

            print(f"\n--- {name}, n = {size} ---")
            print(f"Average comparisons: {average:.2f}")

            print("Best 10 cases (fewest comparisons):")
            for r in best10:
                print(f"  {list(r[2])}  ->  {r[3]} comparisons")

            print("Worst 10 cases (most comparisons):")
            for r in worst10:
                print(f"  {list(r[2])}  ->  {r[3]} comparisons")

        print()




with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["algorithm", "n", "original_array", "comparisons"])
    for algorithm, size, original, comparisons in records:
        writer.writerow([algorithm, size, list(original), comparisons])
