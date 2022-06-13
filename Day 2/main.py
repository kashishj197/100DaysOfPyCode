# # Lesson 1: Data types # #
# Integer
123_456_789

# Float
3.1479

# String
"Hello"[4]

# Boolean
True
False

# # Lesson 2: Type errors, Type checking and Type conversion # #
num_char = len(input("What is your name?\n"))
print(type(num_char))
# print("your name has " + num_char + " characters.") gives type_error
print("your name has " + str(num_char) + " characters.")

# Exercise
inp = input("Write two digit number: ")
first_digit = int(inp[0])
second_digit = int(inp[1])
rev_total = second_digit + first_digit
print(rev_total)

# # Lesson 3: Mathematical operations # #
# +, -, /, //, *, **
# PEMDAS (), **, * /, + -
print(3 * 3 + 3 * 3 / 3 - 3)

# Exercise
height = input("Height in Metres: ")
weight = input("Weight in Kg: ")

BMI = int(int(weight) / (float(height) ** 2))
print(BMI)

# # Lesson 4: F strings # #
name = "Kashish"
age = 23
print(f"your name is {name} and your age is {age}")

# Exercise
age = int(input("What is your age?\n"))

years_remaining = 65 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months")

