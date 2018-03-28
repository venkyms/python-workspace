def nearest_square(limit):
    answer = 1
    while (answer + 1) ** 2 < limit:
        answer += 1
    return answer ** 2


squares = set()
# index = 1
# while index <= 2000:
for index in range(2000):
    squares.add(nearest_square(index))


print("square:{}".format(squares))
print("square:length:{}".format(len(squares)))
# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers

for sq in squares:
    print(sq)


# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
# def nearest_square(limit):
#     answer = 0
#     while (answer + 1) ** 2 < limit:
#         answer += 1
#     return answer ** 2
