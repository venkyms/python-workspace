def result_for_question(user_answer, expected_answer):
    """
    Check if the user_answer and expected_answer matches
    :param user_answer: user provided answer
    :param expected_answer: answer expected
    :return: Boolean value
    """
    return user_answer == expected_answer


def check_answers(user_answers, expected_answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    :param user_answers: The answers which user has provided
    :param expected_answers: Expected answers, this hold the correct answers for each question
    :return: Message to be displayed to the user
    """
    results = []
    for index in range(len(user_answers)):     # check each user_answer with expected_answer
        results.append(result_for_question(user_answers[index], expected_answers[index]))

    total_question = len(expected_answers)    # find total questions based on expected_answers
    count_correct = sum(results)  # get correct answer count
    count_incorrect = total_question - count_correct  # get incorrect answer count

    if count_correct / total_question > 0.7:
        return "Congratulations, you passed the test! You scored {} out of {}.".format(str(count_correct), total_question)
    elif count_incorrect / total_question >= 0.3:
        return "Unfortunately, you did not pass. You scored {} out of {}.".format(str(count_correct), total_question)


my_answers1 = [1, 2, 3, 4, 5]
my_answers2 = [2, 2, 4, 4, 5]
answers1 = [1, 2, 3, 4, 5]
print(check_answers(my_answers1, answers1))
print(check_answers(my_answers2, answers1))

my_answers3 = [1, 2, 3, 4, 5, 6]
my_answers4 = [2, 2, 4, 4, 5, 6]
answers2 = [1, 2, 3, 4, 5, 6]
print(check_answers(my_answers3, answers2))
print(check_answers(my_answers4, answers2))
