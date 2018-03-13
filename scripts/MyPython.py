def which_prize(points):
    """Function to decide the prize based on points"""
    if 0 <= points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif 51 <= points <= 150:
        return "Oh dear, no prize this time."
    elif 151 <= points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"

    elif 181 <= points <= 200:
        return "Congratulations! You have won a penguin!"
    else:
        return "Oh dear, no prize this time."


print(which_prize(0))
print(which_prize(0))
