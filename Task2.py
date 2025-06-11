import random


def generate_geometric_progression():
    length = random.randint(7, 10)  
    start = random.randint(1, 10) 
    ratio = random.randint(2, 5) 

    progression = []
    for i in range(length):
        progression.append(start * (ratio ** i))

    return progression


print("Welcome to the Brain Games!")
name = input("May I have your name? ")
print(f"Hello, {name}!")
print("What number is missing in the progression?")

while True:
    progression = generate_geometric_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]

    progression_str = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_str.append("..")
        else:
            progression_str.append(str(num))
    question = " ".join(progression_str)

    print(f"Question: {question}")
    user_answer = input("Your answer: ").strip()

    if user_answer == 'q':
        break

    if int(user_answer) == correct_answer:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")

print(f"Congratulations, {name}!")
