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

# list to hold quiz history
quiz_history = []
questions_asked = 0
num_right = 0
num_wrong = 0


questions_left = num_questions

for item in range(1, num_questions + 1):
    number1 = random.randint(low, high)
    number2 = random.randint(low, high)

    question = "{} + {} = ".format(number1, number2)
    answer = number1 + number2

    user_ans = int(input(question))
    questions_asked += 1

    # Compares users answer with the correct answer

    if user_ans != answer:
        num_wrong += 1
        print()
        print("Sorry, that is the wrong answer. The correct answer was {}".format(answer))
        print()
        quiz_history.append("Question {}: You got it wrong".format(questions_asked))

    else:
        num_right += 1
        print()
        print("Well Done, You got it right!")
        print()
        quiz_history.append("Question {}: You got it right".format(questions_asked))

print()
print("**** Game History ******")
for item in quiz_history:
    print(item)

print()
print("You got {} out of {} Correct".format(num_right, num_questions))
print()
print("Thanks for playing")

