# def which_prize(points):
#     """Calculation prize based on the points"""
#     if 0 <= points <= 50:
#         return 'Congratulations! You have won a wooden rabbit!'
#     elif 51 <= points <= 150:
#         return 'Oh dear, no prize this time.'
#     elif 151 <= points <= 180:
#         return 'Congratulations! You have won a wafer-thin mint!'
#     elif 181 <= points <= 200:
#         return 'Congratulations! You have won a penguin!'
#     else:
#         return 'Oh dear, no prize this time.'


def which_prize(points):
    """Calculation prize based on the points"""
    prize = None
    if 0 <= points <= 50:
        prize = 'wooden rabbit'
    elif 51 <= points <= 150:
        prize = None
    elif 151 <= points <= 180:
        prize = 'wafer-thin mint'
    elif 181 <= points <= 200:
        prize = 'penguin'
    else:
        prize = None

    if prize:
        return 'Congratulations! You have won a {}!'.format(prize)
    else:
        return 'Oh dear, no prize this time.'



# edge cases
print(which_prize(0))
print(which_prize(20))
print(which_prize(50))

print(which_prize(51))
print(which_prize(70))
print(which_prize(150))

print(which_prize(151))
print(which_prize(170))
print(which_prize(180))

print(which_prize(181))
print(which_prize(190))
print(which_prize(200))


print(which_prize(210))
print(which_prize(-1))
