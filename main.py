from cave import Cave 
from character import Character
from character import Enemy, Friend
from item import Weapon, Item


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
harry.set_health(100)
cryo_respository.set_character(harry)


#items
vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")

#weapons
gun = Weapon("Gun")
gun.set_description("a gun")
gun.set_dmg_value(10)
cryo_respository.set_item(gun)




#gameplay loop
bag = []
current_cave = cryo_respository
dead = False
fighting = False
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
        inhabitant.display_health()
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
        fighting = True
        while fighting == True:
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                print("What will you fight with?")
                weapon = input()
                if weapon in bag:
                    dmg_done = weapon.get_dmg_value()
                    print(dmg_done + "damage done")

                else:
                    print("You don't have a " + weapon)
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