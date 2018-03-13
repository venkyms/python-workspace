def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    middle_index = int(len(numbers)/2)
    if len(numbers) % 2 == 0:
        return (numbers[middle_index] + numbers[middle_index - 1]) / 2
    else:
        return numbers[middle_index]


test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

test4 = median([53, 12, 65, 7, 420, 317])
print("expected result: 65, actual result: {}".format(test4))
