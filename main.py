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
armoury.set_key("Armoury Key Card")

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

#rooms ACT II 
main_road = Cave("Main Road")
main_road.set_description("[main road description placeholder]")

#characters ACT I
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_health(100)
harry.set_lowest_dmg_value(0)
harry.set_highest_dmg_value(40)

automaton_seeker = Enemy("Automoton Seeker", "A vile automoton who's come to finish the job")
automaton_seeker.set_conversation("You die here, human! With the rest of your crew!")
automaton_seeker.set_health(100)
automaton_seeker.set_lowest_dmg_value(0)
automaton_seeker.set_highest_dmg_value(40)

terminal = Character("Terminal", "A computer terminal whose dim glow illuminates the room - [talk] to access terminal")
terminal.set_conversation("\nB-B0rEali5 sTa-a-atUs rEp0Rt:\n\nEng1nes: oFfline\nSHie1d SystEm5: offlinE\nFiRe SupRess1on SysTem: off1ine\nHuLl 1ntegriTy: hEav1ly c0mpRom1sed\nClimaTe Contr0l SySteM: offliNe\n\n-- m0vEmeNt deTectEd 1n caRgo bAy --")
hallway.set_character(terminal)

cpt_levi = Character("Captain Levi's cryo-cell", "A large, frozen-over glass tube. The cryo-gas is leaking! - [talk] to open cryo-cell")
cpt_levi.set_conversation("...nothing... Captain Levi's eyes are rolled back. His body limp and lifeless\nIt's too late...")
cryo_respository.set_character(cpt_levi)

#items
vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")

armoury_key = Item("Armoury Key Card")
armoury_key.set_description("This looks useful")
cargo_bay.set_item(armoury_key)

mech_suit = Item("Mk3 Mech Suit")
mech_suit.set_description("A powerful Mechanised Exo Suit, looks good at clearing debris")
armoury.set_item(mech_suit)

#weapons
gun = Weapon("Gun")
gun.set_description("a gun")
gun.set_lowest_dmg_value(0)
gun.set_highest_dmg_value(50)

power_punch = Weapon("Power Punch!")
power_punch.set_lowest_dmg_value(0)
power_punch.set_highest_dmg_value(50)

explosive_shell = Weapon("Explosive Shell")
explosive_shell.set_lowest_dmg_value(20)
explosive_shell.set_highest_dmg_value(40)

kill = Weapon("kill")
kill.set_lowest_dmg_value(1000)
kill.set_highest_dmg_value(1000)





#gameplay loop

bag = {
    "kill" : kill
}


event_act1_1_mech_suit = False
event_act1_2_seeker = False
act = 1
player_health = 100
current_cave = cryo_respository
dead = False
fighting = False
player_turn = False
enemy_turn = True
print("-----------------------------------------------------------------------------")
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
        if inhabitant is Enemy:
            inhabitant.display_health()
        print("\n")
    command = input(">")
    print("-----------------------------------------------------------------------------")

    #navigation
    if command in ["north", "south", "east", "west"]:
            current_cave = current_cave.move(command, bag)

    # Talk to the inhabitant
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

    # Fight with the inhabitant
    elif command == "fight":
        fighting = True
        player_turn = True
        enemy_turn = False
        while fighting == True:
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                while player_turn == True:
                    if player_health > 0:
                        if inhabitant.health > 0:
                            print("-------------------------")
                            print("What will you fight with?")
                            print("-------------------------")
                            weapon_name = input()
                            if weapon_name in bag:
                                dmg_done = bag[weapon_name].get_dmg_value()
                                inhabitant.health = inhabitant.health - dmg_done
                                print(str(dmg_done) + " damage done")
                                player_turn = False
                                enemy_turn = True

                            else:
                                print("You don't have a " + weapon_name)
                                enemy_turn = False
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
                print("----------------------------------")
                print("There is no one here to fight with")
                print("----------------------------------")

    #pat the inhabitabt
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("---------------------------------")
                print("I wouldn’t do that if I were you…")
                print("---------------------------------")
            else:
                inhabitant.pat()
        else:
            print("------------------------------")
            print("There is no one here to pat :(")
            print("------------------------------")

    #take item
    elif command == "take":
        if item is not None:
            print("------------------------" + ("-" * len(item.get_name())))
            print("You put the " + item.get_name() + " in your bag")
            print("------------------------" + ("-" * len(item.get_name())))
            bag.update({(item.get_name()) : item})
            current_cave.set_item(None)



    if act == 1:
        if "Mk3 Mech Suit" in bag and event_act1_1_mech_suit == False:
            bag.update({"Power Punch!" : power_punch})
            bag.update({"Explosive Shell" : explosive_shell})
            cargo_bay.set_character(automaton_seeker)
            event_act1_1_mech_suit = True

        if cargo_bay.get_character() == None and event_act1_1_mech_suit == True and event_act1_2_seeker == False and current_cave == cargo_bay: 
            cargo_bay.set_description("[Cargo Bay description placeholder]\n----------------------------------------------------\n[Use Mech Suit] to clear debris and escape the ship!\n----------------------------------------------------")
            if command == "Use Mech Suit":
                print("\n")
                print("Using the Mech Suit, you clear the fallen debris. \nThe sound of metal scaping against the ships hull fills the room. \nYou manage to escape the escape the Borealis!")
                print("\n")
                print("Act I Complete")
                event_act1_2_seeker = True
                current_cave = main_road
                act = 2
    else:
        print("---------------------")
        print("You can't go that way")
        print("---------------------")






print("\n")
print("Game Over")