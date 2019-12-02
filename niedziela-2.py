import random

bird = "duck"
while bird != "pigeon":
    print("waiting...")
    x = random.randrange(0, 101)
    print(x)
    if x < 30:
        bird = "pigeon"

print("Hurray, I'm a pigeon!")
