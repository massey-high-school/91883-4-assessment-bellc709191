import random

# number checking function


def intcheck(question, low=None, high=None):

    # sets up error messages

    if low is not None and high is not None:
            error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
            "equal to {}".format(high)
    else:
        error = "please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


# Main routine

num_questions = intcheck("Questions: ", 1)

low = intcheck("Low Number: ")
high = intcheck("High Number: ", low + 1)

for item in range(1, num_questions + 1):
    number1 = random.randint(low, high)
    number2 = random.randint(low, high)

    question = "{} + {} = ".format(number1, number2)
    answer = number1 + number2

    user_ans = int(input(question))

    # Compares users answer with the correct answer

    if user_ans != answer:
        print()
        print("Sorry, that is the wrong answer. The correct answer was {}".format(answer))
        print()

    else:
        print()
        print("Well Done, You got it right!")
        print()

