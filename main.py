import random

def comparing_selection(choosed: int, random: int):
    if choosed > random:
        print ("Try smaller one")
        return False
    elif choosed < random:
        print("I am thinking about bigger one")
        return False
    else:
        return True
    
def write_to_file(name: str, number_of_tries: int):
    with open('scoreboard.txt', 'a') as sb:
        output = f"{name} guessed in {number_of_tries} tries "
        sb.write(output)
       
def main():
    userpick = input("What number from 0 to 100 I am thinking about? ")
    picked = random.randrange(0 , 100)
    print(picked)
    number_of_tries = 1
    while True:
        if comparing_selection(int(userpick), picked):
            break
        userpick = input("Try again: ")
        number_of_tries += 1
        
    name = input("You made it! Let`s save your score. Give me your nick: ")
    print(f"You tried {number_of_tries} times")

    write_to_file(name, number_of_tries)

    
if __name__ == "__main__":
    main()
