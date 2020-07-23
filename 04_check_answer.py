
import random

low = 1
high = 20

# generate two random numbers and make them into a question (hint: use .format)
for item in range(1, 5):
    number1 = random.randint(low, high)
    number2 = random.randint(low, high)

    question = "{} + {} = ".format(number1, number2)
    answer = number1 + number2

    user_ans = int(input(question))

    if user_ans != answer:
        print()
        print("Sorry, that is the wrong answer. The correct answer was {}".format(answer))
        print()

    else:
        print()
        print("Well Done, You got it right!")
        print()
