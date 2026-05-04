from cave import Cave 
from character import Character
from character import Enemy, Friend
from item import Weapon, Item
import random

#weapons
pistol = Weapon("Pistol")
pistol.set_description("An abandoned pistol, half-buried in the snow")
pistol.set_lowest_dmg_value(10)
pistol.set_highest_dmg_value(30)

combat_knife = Weapon("Combat Knife")
combat_knife.set_description("A gunmetal grey combat knife, someone must have lost it")
combat_knife.set_lowest_dmg_value(0)
combat_knife.set_highest_dmg_value(50)

power_punch = Weapon("Power Punch!")
power_punch.set_lowest_dmg_value(0)
power_punch.set_highest_dmg_value(50)

explosive_shell = Weapon("Explosive Shell")
explosive_shell.set_lowest_dmg_value(20)
explosive_shell.set_highest_dmg_value(40)

kill = Weapon("kill")
kill.set_lowest_dmg_value(1000)
kill.set_highest_dmg_value(1000)

#items ACT I
armoury_key = Item("Armoury Key Card")
armoury_key.set_description("This looks useful")

mech_suit = Item("Mk3 Mech Suit")
mech_suit.set_description("A powerful Mechanised Exo Suit, looks good at clearing debris")

#items ACT II
red_key_card = Item("Red Keycard")
green_key_card = Item("Green Keycard")
blue_key_card = Item("Blue Keycard")
factory_gate_key = Item("Factory Gate Key")
power_cell = Item("Power-cell")





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
armoury.add_item(mech_suit)

cargo_bay = Cave("Cargo Bay")
cargo_bay.set_description("[Cargo Bay description placeholder]")
cargo_bay.set_locked(False)
cargo_bay.add_item(armoury_key)

#Room links ACT I
cryo_respository.link_cave(hallway, "south")
hallway.link_cave(cargo_bay, "west")
hallway.link_cave(cryo_respository, "north")
hallway.link_cave(armoury, "east")
cargo_bay.link_cave(hallway, "east")
armoury.link_cave(hallway, "west")

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
hallway.add_character(terminal)

cpt_levi = Character("Captain Levi's cryo-cell", "A large, frozen-over glass tube. The cryo-gas is leaking! - [talk] to open cryo-cell")
cpt_levi.set_conversation("...nothing... Captain Levi's eyes are rolled back. His body limp and lifeless\nIt's too late...")
cryo_respository.add_character(cpt_levi)

#rooms ACT II 
main_road = Cave("Main Road")
main_road.set_description("[main road description placeholder]")
main_road.set_locked(False)
main_road.add_item(pistol)
main_road.add_character(harry)
main_road.add_character(automaton_seeker)

plaza = Cave("Plaza")
plaza.set_description("[Plaza description placeholder]")
plaza.set_locked(False)

crash_site = Cave("Borealis Crash Site")
crash_site.set_description("[Borealis Crash Site description placeholder]")
crash_site.set_locked(False)

factory_gate = Cave("Factory Gate")
factory_gate.set_description("[description placeholder]")
factory_gate.set_locked(False)
factory_gate.add_item(combat_knife)

factory_floor = Cave("Factory Floor")
factory_floor.set_description("[description placeholder]")
factory_floor.set_locked(True)
factory_floor.set_key("Factory Gate Key")

security_room = Cave("Security Room")
security_room.set_description("[description placeholder]")
security_room.set_locked(False)


#room links ACT II
plaza.link_cave(main_road, "east")
main_road.link_cave(plaza, "west")
main_road.link_cave(crash_site, "south")
main_road.link_cave(factory_gate, "east")
factory_gate.link_cave(main_road, "west")
factory_gate.link_cave(factory_floor, "east")
factory_gate.link_cave(security_room, "south")
factory_floor.link_cave(factory_gate, "west")
crash_site.link_cave(main_road, "north")
crash_site.link_cave(security_room, "east")
security_room.link_cave(factory_gate, "north")
security_room.link_cave(crash_site, "west")

#characters ACTII
automaton_sentry_1 = Enemy("Automaton Sentry", "An armed Automaton Guard on lookout")
automaton_sentry_1.set_conversation("Hey! You're not supposed to be here!")
automaton_sentry_1.set_health(100)
automaton_sentry_1.set_lowest_dmg_value(0)
automaton_sentry_1.set_highest_dmg_value(30)
factory_gate.add_character(automaton_sentry_1)

automaton_sentry_2 = Enemy("Automaton Sentry", "An armed Automaton Guard, looks like he's looking for someone")
automaton_sentry_2.set_conversation("Sentry 02 reporting!I found the intruder, over!")
automaton_sentry_2.set_health(100)
automaton_sentry_2.set_lowest_dmg_value(0)
automaton_sentry_2.set_highest_dmg_value(30)

automaton_sentry_3 = Enemy("Automaton Sentry", "An armed Automaton Guard, looks like he's on high alert")
automaton_sentry_3.set_conversation("This is sentry 03! He's here! The intruder's here, over!")
automaton_sentry_3.set_health(100)
automaton_sentry_3.set_lowest_dmg_value(0)
automaton_sentry_3.set_highest_dmg_value(30)

automaton_factory_keeper = Enemy("Automaton Factory Keeper", "A large and intimidating automaton with mech upgrades.\nIt looks like his upgrades are powered by a power-cell!")
automaton_factory_keeper.set_conversation("You dare set foot in my factory?!")
automaton_factory_keeper.set_health(150)
automaton_factory_keeper.set_lowest_dmg_value(0)
automaton_factory_keeper.set_highest_dmg_value(50)
factory_floor.add_character(automaton_factory_keeper)

#Story functions
def randomise_room_act2():
    random_room = random.choice([plaza, main_road, crash_site, security_room])
    return random_room

#gameplay loop

bag = {
    "kill" : kill
}

#starting location/ACT
act = 2
current_cave = main_road

event_act1_1_mech_suit = False
event_act1_2_seeker = False

automaton_sentry_2_location = randomise_room_act2()
automaton_sentry_3_location = randomise_room_act2()
event_act2_1_start = False
event_act2_2_sentry1 = False
event_act2_3_sentry2 = False
event_act2_4_sentry3 = False
event_act2_5_keys = False
event_act2_6_keeper = False
event_act2_7_powercell = False

player_health = 100
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

    items = current_cave.get_item()
    if items:
        print("-- Items --")
        for item in items:
            item.describe()
        print("\n")
    

    inhabitant = current_cave.get_character()
    if inhabitant:
        print("-- Characters --")
        for character in inhabitant:
            character.describe()

    print("\n")
    command = input(">")
    print("-----------------------------------------------------------------------------")

    #navigation
    if command in ["north", "south", "east", "west"]:
            current_cave = current_cave.move(command, bag)

    # Talk to the inhabitant
    elif command == "talk":
        if inhabitant is not None:
            if inhabitant:
                print("Who do you want to talk to?")
                for char in inhabitant:
                    print("- " + char.name)

            choice = input()

            for char in inhabitant:
                if char.name == choice:
                    inhabitant = char
                    break
            inhabitant.talk()

    # Fight with the inhabitant
    elif command == "fight":
        fighting = True
        player_turn = True
        enemy_turn = False
        if inhabitant:
            print("Who do you want to fight?")
            for char in inhabitant:
                print("- " + char.name)

        choice = input()

        for char in inhabitant:
            if char.name == choice:
                inhabitant = char
                break

        while fighting == True:
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                while player_turn == True:
                    if player_health > 0:
                        if inhabitant.health > 0:
                            print("-------------------------")
                            print("Available weapons:")
                            for weapon in bag:
                                print("- " + weapon)
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
                            current_cave.remove_character(inhabitant)
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
        if inhabitant:
            print("Who do you want to pat?")
            for char in inhabitant:
                print("- " + char.name)

            choice = input()

            for char in inhabitant:
                if char.name == choice:
                    inhabitant = char
                    break
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
        if items:
            print("What do you want to take?")
            for item in items:
                print("- " + item.name)

        choice = input()

        for item in items:
            if item.get_name() == choice:
                print("------------------------" + ("-" * len(item.get_name())))
                print("You put the " + item.get_name() + " in your bag")
                print("------------------------" + ("-" * len(item.get_name())))
                bag.update({(item.get_name()) : item})
                items.remove(item)
                break

    else:
        print("---------------------")
        print("You can't go that way")
        print("---------------------")

    #events
    if act == 1:
        if "Mk3 Mech Suit" in bag and event_act1_1_mech_suit == False:
            bag.update({"Power Punch!" : power_punch})
            bag.update({"Explosive Shell" : explosive_shell})
            cargo_bay.add_character(automaton_seeker)
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

    elif act == 2:
        if event_act2_1_start == False:
            #remove for testing bag.pop("Mk3 Mech Suit")
            #remove for testingbag.pop("Power Punch!")
            #remove for testingbag.pop("Explosive Shell")
            print("\n")
            print("--- ACT II ---")
            print("\n")
            print("As you make your way north from the Borealis crash site,\nits not long until the mech suit begins to make a strange noise.\nIts motors jitter and each movement is weaker than the last.\nThen suddenly, the mech suit stops...dead in its tracks.\nAs you inspect the suit, you find it, the power cell\nit's damaged from you earlier battle with the seeker.\nWithout the suit, you'll never make it to the room\n\n-- Maybe there's a power cell around here somewhere? --")
            print("\n")
            event_act2_1_start = True

        if current_cave == factory_gate and current_cave.get_character() is None and event_act2_2_sentry1 == False:
            bag.update({"Red Keycard" : red_key_card})
            print("\n")
            print("It looks like your fight drew some attention. You hear other automatons arriving in the distance")
            print("\n")
            print("----------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Red Keycard] and you put it in your bag. Maybe this is for the gate?")
            print("----------------------------------------------------------------------------------------------------")
            print("\n")
            automaton_sentry_2_location.add_character(automaton_sentry_2)
            automaton_sentry_3_location.add_character(automaton_sentry_3)
            event_act2_2_sentry1 = True

        if current_cave == automaton_sentry_2_location and current_cave.get_character() is None and event_act2_2_sentry1 == True and event_act2_3_sentry2 == False:
            bag.update({"Green Keycard" : green_key_card})
            print("\n")
            print("------------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Green Keycard] and you put it in your bag. Maybe this is for the gate?")
            print("------------------------------------------------------------------------------------------------------")
            print("\n")
            event_act2_3_sentry2 = True

        if current_cave == automaton_sentry_3_location and current_cave.get_character() is None and event_act2_2_sentry1 == True and event_act2_4_sentry3 == False:
            bag.update({"Blue Keycard" : blue_key_card})
            print("\n")
            print("-----------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Blue Keycard] and you put it in your bag. Maybe this is for the gate?")
            print("-----------------------------------------------------------------------------------------------------")
            print("\n")
            event_act2_4_sentry3 = True

        if current_cave == factory_gate and event_act2_3_sentry2 == True and event_act2_4_sentry3 == True and event_act2_5_keys == False:
            bag.update({"Factory Gate Key" : factory_gate_key})
            print("\n")
            print("---------------------------------------------------------------")
            print("Looks like you have all 3 keys, maybe you can open the gate now")
            print("---------------------------------------------------------------")
            print("\n")
            event_act2_5_keys = True

        if current_cave == factory_floor and current_cave.get_character() is None and event_act2_6_keeper == False:
            bag.update({"Power-cell" : power_cell})
            print("\n")
            print("---------------------------------------------------------------------------------------------------------------------")
            print("The automaton factory keeper dropped a [Power-cell] and you put it in your bag. You can finally power your mech suit!")
            print("---------------------------------------------------------------------------------------------------------------------")
            print("\n")
            event_act2_6_keeper = True

        if current_cave == main_road and event_act2_6_keeper == True and event_act2_7_powercell == False:
            main_road.set_description("Placeholder description\n----------------------------------------------------\n[Power Mech Suit] to clear debris and escape the ship!\n----------------------------------------------------")
            if command == "Power Mech Suit":
                print("\n")
                print("You put the powercell in the mech suit and its engines humm to life")
                print("\n")
                print("Act II Complete")
                event_act2_7_powercell = True
                act = 3




print("\n")
print("Game Over")