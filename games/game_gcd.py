import random
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def generate_question():
    nums = [random.randint(1, 20) for _ in range(3)]
    question = " ".join(map(str, nums))
    correct = lcm_multiple(nums)
    return question, correct
