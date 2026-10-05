'''#TODO author: Addie Hurst'''
# TODO:
# - Run all four sorting algorithms on every permutation. - STILL NEEDS HEAPSORT


'''Code Author: Erich M., Addie verified'''
import time
import csv
from permutations import *
from mergesort import *
from quicksort import *
from shakersort import *
from heapsort import *

SIZES = [4, 6, 8]
ALGORITHMS = {"mergesort": mergeSort, "quicksort": quicksort, "shakersort": shakerSort, "heapsort": heapsort}

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
