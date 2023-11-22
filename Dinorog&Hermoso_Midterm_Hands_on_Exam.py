def get_student_input(prompt):
    while True:
        try:
            student_input = int(input(prompt))
            if 1 <= student_input <= 99:
                return student_input
            else:
                print("Invalid Input."
                      "\n<The correct answer is between [1-99]>")

        except ValueError:
            print("Error 404"
                  "\n<Please enter valid integers>")


def get_new_answer(prompt):
    while True:
        new_answer = input(prompt)
        if new_answer in ['yes', 'no']:
            return new_answer
        else:
            print("Invalid Input."
                  "\nPlease enter 'yes' or 'no'")


while True:
    print("\nGRADE SCHOOL STUDENT!"
          "\nSEAT WORK: BASIC OPERATIONS")
    print("Answer the following questions:")

    question1 = get_student_input("\n1.) What is 53 + 5? ")
    if question1 == 58:
        print("Your answer is CORRECT!")

    elif question1 != 58:
        print("Your answer is INCORRECT!")

    question2 = get_student_input("\n2.) What is 52 - 10? ")
    if question2 == 42:
        print("Your answer is CORRECT!")

    elif question2 != 42:
        print("Your answer is INCORRECT!")

    question3 = get_student_input("\n3.) What is 3 x 10? ")
    if question3 == 30:
        print("Your answer is CORRECT!")

    elif question3 != 30:
        print("Your answer is INCORRECT!")

    question4 = get_student_input("\n4.) what is 15 / 5? ")
    if question4 == 3:
        print("Your answer is CORRECT!")

    elif question4 != 3:
        print("Your answer is INCORRECT!")

    another_student = get_new_answer("\nDo you want to answer again [yes | no]: ")
    if another_student != 'yes':
        break
