def convert_to_numeric(score):
    """
    Convert input score to int type
    :param score: could be of any type for eg. String, int, float
    :return: float
    """
    return float(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Sum of three scores excluding highest and lowest score
    :param score1: float
    :param score2: float
    :param score3: float
    :param score4: float
    :param score5: float
    :return: sum of three scores excluding highest and lowest score in float
    """
    sum_of_three_middle_scores = (score1 + score2 + score3 + score4 + score5) - min(score1, score2, score3, score4, score5) - max(score1, score2, score3, score4, score5)
    return sum_of_three_middle_scores


def score_to_rating_string(average_score):
    """
    Convert average score to rating
    0 <= average_score < 1	Terrible
    1 <= average_score < 2	Bad
    2 <= average_score < 3	OK
    3 <= average_score < 4	Good
    4 <= average_score <= 5	Excellent
    :param average_score: average score in float
    :return: rating in string
    """

    if 0 <= average_score < 1:
        return "Terrible"
    elif 1 <= average_score < 2:
        return "Bad"
    elif 2 <= average_score < 3:
        return "OK"
    elif 3 <= average_score < 4:
        return "Good"
    elif 4 <= average_score <= 5:
        return "Excellent"


def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


print(scores_to_rating(1, 2, 3, 4, 5))
print(scores_to_rating("1", 2, 3.0, 4, "5"))
print(scores_to_rating("1", 2, "3.0", 4, "5"))
