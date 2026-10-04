#permutations.py
'''Code AUTHOR: ERICH M., with some edits by Addie Hurst for verification'''
#test n = 4; 0 through n-1 tested
numbers = [0, 1, 2, 3]
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
generatePermutations(numbers)
