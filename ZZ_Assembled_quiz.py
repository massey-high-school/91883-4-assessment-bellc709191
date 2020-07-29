import random


def dec_statement(statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))
    return ""

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

print("Welcome to my addition math quiz!")
print()

num_questions = intcheck("How many questions would you like?: ", 1)
print()
low = intcheck("Please enter a Low Number: ")
print()
high = intcheck("Please enter a High Number: ", low + 1)
print()

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

    print("Question {}".format(questions_asked + 1))
    user_ans = int(input(question))
    questions_asked += 1

    # Compares users answer with the correct answer

    if user_ans != answer:
        num_wrong += 1
        print()
        feedback = dec_statement("Sorry, that is the wrong answer. The correct answer was {}".format(answer), "#")
        print()
        quiz_history.append("Question {}: You got it wrong".format(questions_asked))

    else:
        num_right += 1
        print()
        feedback = dec_statement("Well Done, You got it right!", "*")
        print()
        quiz_history.append("Question {}: You got it right".format(questions_asked))

# shows the user a list of their quiz

print()
print("**** Quiz History ******")
for item in quiz_history:
    print(item)

print()
print("You got {} out of {} Correct".format(num_right, num_questions))
print()
print("Thanks for playing")
