
import random

low = 1
high = 20

# generate two random numbers and make them into a question (hint: use .format)
for item in range(1,5):
    number1 = random.randint(low, high)
    number2 = random.randint(low, high)

    question = "{} + {} = ".format(number1, number2)
    answer = number1 + number2

    # generate question
    print(question, answer)

