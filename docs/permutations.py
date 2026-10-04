'''AUTHOR: ERICH M.'''
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
