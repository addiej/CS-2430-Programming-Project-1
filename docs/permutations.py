#Team 3
#Team members Addie Hurst, Erich Mundt
#CS 2430 - 502
#Programming Project 1 – Fall 2026
#Primary Author: Erich M., Addie made minor edits

#permutations.py

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
