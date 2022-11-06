import random
userpick = input("What number from 0 to 100 I am thinking about? ")
picked = int(random.randrange(0 , 100))
print(f"userpick: {userpick}")
print(f"picked: {picked}")
number_of_tries = 1
while userpick != picked:
    picked = int(random.randrange(0 , 100))
    userpick = input("Not this one. Try another one ")
    print(f"userpick: {userpick}")
    print(f"picked: {picked}")
    number_of_tries += 1
else:
    name = str(input("You made it! Let`s save your score. Give me your nick: "))
    print(f"You tried {number_of_tries} times")
