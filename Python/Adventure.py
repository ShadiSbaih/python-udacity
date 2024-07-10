import time
import random
items = []

def print_pause(message):
    print(message)
    time.sleep(1.5)

def show_items():
    if not items:
        print_pause("You have no items or coins.")
    else:
        print_pause("You have:")
        for item in items:
            print_pause(item)

def check_items(item, area):
    if item not in items:
        print_pause(f"You took the {item}.")
        items.append(item)
    else:
        print_pause(f"You already took the {item}.")
    print_pause(f"Let's go back to the {area}.")

def intro():
    print_pause("Welcome, brave hero!")
    print_pause("A great challenge awaits you in the kingdom of Eldoria.")
    print_pause("Legends speak of a fearsome beast that terrorizes our lands.")
    print_pause("Your quest begins in the Enchanted Forest, shrouded in mist and mystery.")
    print_pause("As you step under the canopy of towering trees, you encounter a mystical crossroad.")
    print_pause("Three ancient paths lie before you, each veiled in swirling fog and echoing with the whispers of old.")
    print_pause("Choose your path wisely, for each step will bring you closer to your destiny.")

def forest():
    while True:
        print_pause("1-Go to The Left Path (Old House)\n2-Go to The Right Path (Cave)\n3-Go to Ahead Path (The bridge)")
        path = input("Where are you going? ")
        if path == "1":
            house()
        elif path == "2":
            cave()
        elif path == "3":
            bridge()
        else:
            print_pause("Sorry i dont't understand...")

def house():
    print_pause("You found an old house and there is some wood inside , you can take them.")
    if input("Take them? (yes/no) ").lower() == "yes":
        check_items("wood", "forest")
    forest()

def cave():
    print_pause("You found ropes inside a backpack left by previous adventurers.")
    if input("Take them? (yes/no) ").lower() == "yes":
        check_items("ropes", "forest")
    forest()

def bridge():
    print_pause("Oh Look, there is a bridge and it seems broken.")
    print_pause("You need wood and ropes to fix it.")
    if "ropes" in items and "wood" in items:
        print_pause("Well Done!You fixed the bridge.")
        print_pause("You can go ahead now.")
        print_pause("Again, there is a crossroad in the town with three different paths.")
        town()
    else:
        print_pause("You have missing items!")
        show_items()
        forest()

def town():
    while True:
        print_pause("1-Go to The Left Path (Monster Nest)\n2-Go to The Right Path (Treasure )\n3-Go to Ahead Path (The Blacksmith)")
        path = input("Where are you going? ")
        if path == "1":
            monster_nest(Monster)
        elif path == "2":
            treasure()
        elif path == "3":
            blacksmith()
        else:
            print("sorry i didn't understand")

def treasure():
    print_pause("Oh look! There is a treasure! chest full of coins nearby the town.")
    if input("Take it? (yes/no) ").lower() == "yes":
        check_items("coins", "town")

def blacksmith():
    print_pause("Oh, there is a blacksmith in the town.")
    if input("Go to him? (yes/no) ").lower() == "yes":
        if "coins" in items:
            check_items("sword", "town")
        else:
            show_items()
            print_pause("You have arrived at the town.")
            town()

def monster_nest(Monster):
    print_pause(f"Oh Look! You arrived at the {Monster}'s nest!")
    if input("Go to him? (yes/no) ").lower() == "yes":
        if "sword" in items:
         print_pause(f"You defeated the {Monster}!")
         print_pause("Finally, we can live in peace!")
         play_again()
        else:
            print_pause("You don't have a sword.")
            print_pause("You have arrived at the town.")
            town()

def play_again():
    if input("Would you like to play again? (yes/no) ").lower() == "yes":
        print_pause("Great! Restarting the game...")
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")

def play_game():
    global items 
    global monsters
    global Monster
    monsters=["Hydra", "Minotaur","Golem","Goblen"]
    Monster = random.choice(monsters)
    items = []
    intro()
    forest()

play_game()
