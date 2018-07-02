import random

print("START")
answer = random.randint(1,100)
temp = input("Please guess!\n")
guess = int(temp)

while guess != answer:
    assert guess < 100
    if guess < answer:
        print("N\nToo small")
    elif guess > answer:
        print("N\nToo big")
    temp = input("Please guess again!\n")
    guess = int(temp)

print("Y")
print("Good!\n")

