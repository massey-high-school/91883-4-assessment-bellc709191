# Component 1 - Ask user for number of questions

def check_questions():
    while True:
        response = input("How many questions would you like: ")

        round_error = "Please enter an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


