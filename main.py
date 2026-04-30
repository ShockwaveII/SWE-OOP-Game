from cave import Cave 
from character import Character
from character import Enemy, Friend
from item import Weapon, Item


#rooms ACT I
cryo_respository = Cave("Cryo Repository")
cryo_respository.set_description("[cryo description placeholder]")
cryo_respository.set_locked(False)

hallway = Cave ("Hallway")
hallway.set_description("[Hallway description placeholder]")
hallway.set_locked(False)

armoury = Cave("Armoury")
armoury.set_description("[Armoury description placeholder]")
armoury.set_locked(True)

cargo_bay = Cave("Cargo Bay")
cargo_bay.set_description("[Cargo Bay description placeholder]")
cargo_bay.set_locked(False)

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
harry.set_lowest_dmg_value(0)
harry.set_highest_dmg_value(40)
cryo_respository.set_character(harry)


#items
vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")

armoury_key = Item("Armoury Key Card")
armoury_key.set_description("This looks useful")

#weapons
gun = Weapon("Gun")
gun.set_description("a gun")
gun.set_lowest_dmg_value(0)
gun.set_highest_dmg_value(50)
cryo_respository.set_item(gun)




#gameplay loop

bag = {
}

player_health = 100
current_cave = cryo_respository
dead = False
fighting = False
player_turn = False
enemy_turn = True
while dead == False:
    #descriptions
    print("\n")
    current_cave.get_details()
    print("\n")

    item = current_cave.get_item()
    if item is not None:
        print("-- Items --")
        item.describe()
        print("\n")
    

    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        print("-- characters --")
        inhabitant.describe()
        inhabitant.display_health()
        print("\n")
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
        player_turn = True
        while fighting == True:
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                while player_turn == True:
                    if player_health > 0:
                        if inhabitant.health > 0:
                            print("What will you fight with?")
                            weapon_name = input()
                            if weapon_name in bag:
                                dmg_done = bag[weapon_name].get_dmg_value()
                                inhabitant.health = inhabitant.health - dmg_done
                                print(str(dmg_done) + " damage done")
                                player_turn = False
                                enemy_turn = True

                            else:
                                print("You don't have a " + weapon_name)
                        else:
                            print("You defeated "+ inhabitant.name)
                            current_cave.set_character(None)
                            player_turn = False
                            fighting = False
                    else:
                        print("you were defeated by " + inhabitant.name)
                        player_turn = False
                        fighting = False
                        dead = True

                    while enemy_turn == True:
                        print("\n")
                        print(inhabitant.name + " uses [Insert Attack]")
                        player_health = player_health - inhabitant.get_dmg_value()
                        print(str(inhabitant.get_dmg_value()) + " damage taken")
                        print("\n")
                        print("----------------")
                        print("Player Health: " + str(player_health))
                        print("Enemy Health: " + str(inhabitant.health)) 
                        print("----------------")
                        print("\n")
                        enemy_turn = False
                        player_turn = True

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
            bag.update({(item.get_name()) : item})
            current_cave.set_item(None)

    #unlock room:


print("\n")
print("Game Over")