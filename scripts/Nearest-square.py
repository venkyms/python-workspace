def nearest_square(param):
    """
    Find the nearest square value less than param
    :param param: input param in int
    :return: nearest square value
    """
    square_value, square_value_temp, index = 1, 1, 1
    while index <= param / 2:
        square_value_temp = index ** 2
        if square_value_temp > param:
            return square_value
        else:
            square_value = square_value_temp
        index += 1
        print("square_value:{}".format(square_value))


def nearest_square1(limit):
    answer = 0
    while (answer + 1) ** 2 < limit:
        answer += 1
    return answer ** 2


test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

test2 = nearest_square(50)
print("expected result: 49, actual result: {}".format(test2))
