import random
import math


def get_lcm_of_three(a, b, c):
    lcm_ab = a * b // math.gcd(a, b)
    lcm_abc = lcm_ab * c // math.gcd(lcm_ab, c)
    return lcm_abc


print("Welcome to the Brain Games!")
name = input("May I have your name? ")
print(f"Hello, {name}!")
print("Find the smallest common multiple of given numbers.")

while True:
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    num3 = random.randint(1, 15)
    numbers = [num1, num2, num3]
    correct_answer = get_lcm_of_three(num1, num2, num3)

    print(f"Question: {' '.join(map(str, numbers))}")
    user_answer = input("Your answer: ")

    if user_answer == 'q':
        break

    if int(user_answer) == correct_answer:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


print(f"Congratulations, {name}!")
