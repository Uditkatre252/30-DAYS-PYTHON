import random

random_number = random.randint(1, 100)


while True:
    your_choice = int(input("Enter your choice: "))
    if random_number > your_choice:
        print("too low")
    elif random_number < your_choice:
        print("too high")
    elif your_choice == random_number:
        print("you guessed right")
        break

