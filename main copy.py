from cave import Cave 
from character import Character
from character import Enemy, Friend
from item import Item


#rooms ACT I
cryo_respository = Cave(" Cryo Repository")
cryo_respository.set_description("[cryo description placeholder]")

hallway = Cave ("Hallway")
hallway.set_description("[Hallway description placeholder]")

armoury = Cave("Armoury")
armoury.set_description("[Armoury description placeholder]")

cargo_bay = Cave("Cargo Bay")
cargo_bay.set_description("[Cargo Bay description placeholder]")

#Room links ACT I
cryo_respository.link_cave(hallway, "south")
hallway.link_cave(cargo_bay, "west")
hallway.link_cave(cryo_respository, "north")
hallway.link_cave(armoury, "east")
cargo_bay.link_cave(hallway, "east")
armoury.link_cave(hallway, "west")

#characters
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")


#items
vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")



#gameplay loop
bag = []
current_cave = cryo_respository
dead = False
while dead == False:
    #descriptions
    print("\n")
    item = current_cave.get_item()
    if item is not None:
        item.describe()
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">")

    #navigation
    if command in ["north", "south", "east", "west"]:
            current_cave = current_cave.move(command)

    # Talk to the inhabitant
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    # Fight with the inhabitant
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True
                    print("Bravo,hero you won the fight!")
                    current_cave.set_character(None)
                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")

    #pat the inhabitabt
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn’t do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

    #take item
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)