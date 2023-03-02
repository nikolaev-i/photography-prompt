import random


with open('prompts.txt') as f:
    contents = f.read()
    prompt = contents.split("\n")
rand_number = random.randrange(0, len(prompt))

print(prompt[rand_number])


