import random
random1 = random.randint(1, 99)
random2 = random.randint(1, 99)

addition = eval("random1 + random2")
subtraction = eval("random1 - random2")
multiplication = eval("random1 * random2")
division = eval("random1 / random2")


print(f"Question 1\n{random1} + {random2}?")
first_answer = eval(input("Answer: "))
if first_answer == addition:
    print("You are Correct")

else:
    print("Wrong")

print(f"Question 2\n{random1} - {random2}?")
second_answer = eval(input("Answer: "))
if first_answer == subtraction:
    print("You are Correct")

else:
    print("Wrong")

print(f"Question 3\n{random1} * {random2}?")
third_answer = eval(input("Answer: "))
if first_answer == multiplication:
    print("You are Correct")

else:
    print("Wrong")

print(f"Question 4\n{random1} / {random2}?")
fourth_answer = eval(input("Answer: "))
if first_answer == division:
    print("You are Correct")

else:
    print("Wrong")

