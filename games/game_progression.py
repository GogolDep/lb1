import random

def generate_question():
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    length = 10
    progression = [start * (ratio ** i) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct = progression[hidden_index]
    progression[hidden_index] = '..'
    question = " ".join(map(str, progression))
    return question, correct
