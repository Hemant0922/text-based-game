import random

def display_inventory(player):
    if player["inventory"]:
        print("\nYour Inventory:")
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("\nYour inventory is empty.")

def main():
    print("Welcome to the Enhanced Treasure Hunter Adventure!")
    print("Embark on a journey to find ancient treasures, uncover secrets, and overcome challenges.")
    player = create_character()
    story_intro(player)

def create_character():
    print("\n--- Character Creation ---")
    name = input("Enter your character's name: ")
    profession = choose_profession()
    return {
        "name": name,
        "profession": profession,
        "inventory": [],
        "treasure": 0,
        "health": 100,
        "skills": [],
        "quests": []
    }

def choose_profession():
    print("\nChoose your profession:")
    print("1. Archaeologist")
    print("2. Treasure Hunter")
    print("3. Explorer")

    profession_options = {"1": "Archaeologist", "2": "Treasure Hunter", "3": "Explorer"}
    while True:
        choice = input("Enter the number corresponding to your profession: ")
        if choice in profession_options:
            return profession_options[choice]
        print("Invalid choice. Please try again.")

def story_intro(player):
    print(f"\nWelcome, {player['name']} the {player['profession']}!")
    print("Your journey begins in a remote jungle, rumored to hold a legendary treasure.")
    print("You must uncover clues, make wise decisions, and face challenges to claim the treasure!")

    npc_encounter(player)

def npc_encounter(player):
    print("\n--- NPC Encounter ---")
    print("You encounter an old guide who offers you assistance.")
    print("He offers two things:")
    print("1. A map of the area that reveals hidden locations.")
    print("2. A rope to help with climbing.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("You received a hidden map! It will help you uncover more treasure locations.")
        player["inventory"].append("Hidden Map")
    elif choice == "2":
        print("You received a rope! It will help you scale dangerous cliffs.")
        player["inventory"].append("Rope")
    else:
        print("The guide leaves you with nothing, but you press on.")
    
    first_decision(player)

def first_decision(player):
    print("\n--- The Jungle Entrance ---")
    print("You arrive at the entrance of a dense jungle. Do you:")
    print("1. Enter cautiously, preparing for obstacles.")
    print("2. Rush in eagerly, eager to uncover secrets.")
    print("3. Speak with the guide for advice.")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        cautious_approach(player)
    elif choice == "2":
        adventurous_approach(player)
    elif choice == "3":
        npc_advice(player)
    else:
        print("Invalid choice. Try again.")
        first_decision(player)

def npc_advice(player):
    print("\nThe guide shares valuable advice:")
    print("He tells you that the jungle is full of dangers and you should tread carefully.")
    print("With this newfound wisdom, you feel more confident.")
    first_decision(player)

def cautious_approach(player):
    print("\nYou enter the jungle cautiously, scanning the area.")
    if random.choice([True, False]):
        print("You discover an ancient stone tablet with a clue leading to the treasure.")
        player["treasure"] += 10
        player["inventory"].append("Stone Tablet")
    else:
        print("The jungle seems quiet, but you miss an important clue.")
    next_step(player)

def adventurous_approach(player):
    print("\nYou rush into the jungle, eager to uncover the treasure.")
    if random.choice([True, False]):
        print("Your boldness leads you to a hidden cave filled with ancient artifacts.")
        player["treasure"] += 20
        player["inventory"].append("Ancient Artifacts")
    else:
        print("You encounter a wild animal!")
        combat(player)
    next_step(player)

def combat(player):
    print("\n--- Combat Encounter ---")
    print("A wild animal attacks! You must defend yourself.")
    print("1. Use the rope to trap it.")
    print("2. Fight the animal using your skills.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1" and "Rope" in player["inventory"]:
        print("You successfully trap the animal with the rope!")
        player["health"] -= 10
        print("You lost 10 health points.")
    elif choice == "2":
        print("You fight the animal bravely!")
        if random.choice([True, False]):
            print("You defeat the animal but lose some health.")
            player["health"] -= 20
        else:
            print("You are injured but escape.")
            player["health"] -= 30
    else:
        print("You freeze in fear and the animal escapes.")
    print(f"Remaining Health: {player['health']}")
    next_step(player)

def next_step(player):
    print("\n--- The Puzzle of the Cave ---")
    display_inventory(player)
    print("Inside the cave, you find a mysterious locked chest. The inscription on it reads:")
    print('"To unlock the chest, answer the riddle correctly."')
    print("Riddle: I have keys but open no locks. What am I?")

    answer = input("Enter your answer: ").strip().lower()
    if answer == "piano":
        print("Correct! The chest opens, revealing a treasure map.")
        player["treasure"] += 30
        player["inventory"].append("Treasure Map")
    else:
        print("Incorrect! The chest remains locked.")
    final_decision(player)

def final_decision(player):
    print("\n--- Final Decision ---")
    display_inventory(player)
    print("The map leads to two possible locations:")
    print("1. A mountain pass with a dangerous climb.")
    print("2. A river with fast-moving waters.")
    print("3. A hidden temple.")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        mountain_pass(player)
    elif choice == "2":
        river_adventure(player)
    elif choice == "3":
        hidden_temple(player)
    else:
        print("Invalid choice. Try again.")
        final_decision(player)

def hidden_temple(player):
    print("\nYou venture into the hidden temple.")
    print("The temple is filled with traps and puzzles.")
    if "Hidden Map" in player["inventory"]:
        print("The map leads you to a secret room with a treasure chest.")
        player["treasure"] += 50
        player["inventory"].append("Ancient Relic")
    else:
        print("You get lost and end up at a dead end.")
    end_game(player)

def mountain_pass(player):
    print("\nYou choose the mountain pass.")
    if random.choice([True, False]):
        print("You successfully navigate the climb and discover the legendary treasure hidden in a cave.")
        player["treasure"] += 50
        player["inventory"].append("Legendary Treasure")
    else:
        print("The climb is difficult, and you don't make it to the treasure this time.")
    end_game(player)

def river_adventure(player):
    print("\nYou choose to navigate the river.")
    if random.choice([True, False]):
        print("You successfully cross the river and find the treasure buried under a tree.")
        player["treasure"] += 40
        player["inventory"].append("Hidden Treasure")
    else:
        print("The river is too dangerous, and you are swept downstream.")
    end_game(player)

def end_game(player):
    print("\n--- End of Game ---")
    print(f"Thank you for playing, {player['name']}!")
    print(f"Final Profession: {player['profession']}")
    print(f"Total Treasure: {player['treasure']}")
    display_inventory(player)
    print(f"Remaining Health: {player['health']}")
    print("Good luck on your next treasure hunt!")

if __name__ == "__main__":
    main()
