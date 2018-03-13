def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    if len(input_list) > 3:
        sorted_list = sorted(input_list, reverse=True)
        return sorted_list[0:3]
    else:
        return sorted(input_list, reverse=True)


print(top_three([2,3,5,6,8,4,2,1]))
print(top_three([2,3,5]))
print(top_three([2,3]))

