# # Lesson 1: Love Calculator # #
combined_name = input("What is your name?\n") + input("What is your crush name?\n")
per_one = 0
per_two = 0

for n in combined_name.lower():
    if n in "true":
        per_one += 1
    elif n in "love":
        per_two += 1

total_love = int(str(per_one) + str(per_two))
if total_love <= 10 or total_love >= 90:
    print(f"Your score is {total_love}%, you go together like coke and mentos")
elif 40 <= total_love <= 50:
    print(f"Your score is {total_love}%, you are alright together")
else:
    print(f"Your score is {total_love}%")
