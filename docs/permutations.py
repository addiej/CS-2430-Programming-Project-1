#permutations.py
'''TODO author: Addie Hurst
# TODO:
# - Fix indentation so remainingNumbers is completely built before generating subPermutations.
# - Verify the generator produces exactly n! permutations.
# - Verify there are no duplicate permutations.
# - Verify every permutation contains all values from 0 through n - 1.
# - Test n = 4, 6, and 8.'''

'''Code AUTHOR: ERICH M., with some edits by Addie Hurst for verification'''
#test n = 6; 0 through n-1 tested
numbers = [0, 1, 2, 3, 4, 5]
def generatePermutations(numbers):

    if len(numbers) == 1:
        return [numbers]

    permutations = []

    for number in numbers:

        remainingNumbers = []
        for currentNumber in numbers:
            if currentNumber != number:
                remainingNumbers.append(currentNumber)

        subPermutations = generatePermutations(remainingNumbers)

        for permutation in subPermutations:
            permutations.append([number] + permutation)

    return permutations
#return count of permutations instead of returning each possible permutation (FIXED previous commit)
permutations = generatePermutations(numbers)
print("Total permutations:", len(permutations))
