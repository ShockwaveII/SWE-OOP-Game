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
pistol.set_dmg_type("ranged")

combat_knife = Weapon("Combat Knife")
combat_knife.set_description("A gunmetal grey combat knife, someone must have lost it")
combat_knife.set_lowest_dmg_value(0)
combat_knife.set_highest_dmg_value(50)
combat_knife.set_dmg_type("melee")

power_punch = Weapon("Power Punch!")
power_punch.set_lowest_dmg_value(0)
power_punch.set_highest_dmg_value(50)
power_punch.set_dmg_type("melee")

explosive_shell = Weapon("Explosive Shell")
explosive_shell.set_lowest_dmg_value(20)
explosive_shell.set_highest_dmg_value(40)
explosive_shell.set_dmg_type("ranged")

kill = Weapon("kill")
kill.set_lowest_dmg_value(1000)
kill.set_highest_dmg_value(1000)
kill.set_dmg_type("ranged")

nothing = Weapon("nothing")
nothing.set_lowest_dmg_value(0)
nothing.set_highest_dmg_value(0)
nothing.set_dmg_type("melee")

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
cargo_bay.set_description("There's debris that needs heavy machinery to clear, like a mech suit")
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

gate_terminal = Character("Gate Control Terminal", "A digital terminal that controls the factory gate - [talk] to access terminal")
gate_terminal.set_conversation("Gate locking: Engaged\n-- looks like there are 3 key slots --")
factory_gate.add_character(gate_terminal)

mech_suit_unpowered = Character("Mk3 Mech Suit", "A powerful Mechanised Exo Suit - [talk] to access diagnostics")
mech_suit_unpowered.set_conversation("Mk3 Mech Suit - Diagnostics:\nPowercell status: Damaged\n-- Warning insufficient power! --")
main_road.add_character(mech_suit_unpowered)

vending_machine = Character("Vending machine", "A lone, dimly lit vending machine - [talk] to use")
vending_machine.set_conversation("Beep! Boop! ... ~-!$@&&# ... Ding! One can of motor oil ")
plaza.add_character(vending_machine)

sleepy = Character("Sleepy Automaton ", "A security automaton asleep in the security office. talk?")
sleepy.set_conversation("zzz... (Do automatons dream of electric sheep?)")
security_room.add_character(sleepy)

#rooms ACT III
control_facility_gate = Cave("Control Facility Gate")
control_facility_gate.set_description("placeholder")
control_facility_gate.set_locked(False)

boss_arena_1 = Cave("Boss Arena 1")
boss_arena_1.set_description("placeholder")
boss_arena_1.set_locked(False)

boss_arena_2 = Cave("Boss Arena 2")
boss_arena_2.set_description("placeholder")
boss_arena_2.set_locked(False)

boss_arena_3 = Cave("Boss Arena 3")
boss_arena_3.set_description("placeholder")
boss_arena_3.set_locked(False)

upgrade_room_1 = Cave("Upgrade Room 1")
upgrade_room_1.set_description("placeholder")
upgrade_room_1.set_locked(True)
upgrade_room_1.set_key("Boss Phase 1")

upgrade_room_2 = Cave("Upgrade Room 2")
upgrade_room_2.set_description("placeholder")
upgrade_room_2.set_locked(True)
upgrade_room_2.set_key("Boss Phase 2")

control_room = Cave("Control Room")
control_room.set_description("placeholder")
control_room.set_locked(True)
control_room.set_key("Boss Phase 3")

Rocket_room = Cave("Emergency Escape Rocket")
Rocket_room.set_description("placeholder")
Rocket_room.set_locked(False)

#room links ACT III
control_facility_gate.link_cave(boss_arena_1, "north")
boss_arena_1.link_cave(upgrade_room_1, "north")
boss_arena_1.link_cave(control_facility_gate, "south")
upgrade_room_1.link_cave(boss_arena_1, "south")
upgrade_room_1.link_cave(boss_arena_2, "north")
boss_arena_2.link_cave(upgrade_room_1, "south")
boss_arena_2.link_cave(upgrade_room_2, "north")
upgrade_room_2.link_cave(boss_arena_2, "south")
upgrade_room_2.link_cave(boss_arena_3, "north")
boss_arena_3.link_cave(upgrade_room_2, "south")
boss_arena_3.link_cave(control_room, "north")
control_room.link_cave(boss_arena_3, "south")
control_room.link_cave(Rocket_room, "east")
Rocket_room.link_cave(control_room, "west")

#characters ACT III
boss_phase_1 = Enemy("Boss fight phase 1", "placeholder")
boss_phase_1.set_conversation("placeholder")
boss_phase_1.set_health(150)
boss_phase_1.set_lowest_dmg_value(0)
boss_phase_1.set_highest_dmg_value(50)
boss_arena_1.add_character(boss_phase_1)

boss_phase_2 = Enemy("Boss fight phase 2", "placeholder")
boss_phase_2.set_conversation("placeholder")
boss_phase_2.set_health(150)
boss_phase_2.set_lowest_dmg_value(0)
boss_phase_2.set_highest_dmg_value(50)
boss_arena_2.add_character(boss_phase_2)

boss_phase_3 = Enemy("Boss fight phase 3", "placeholder")
boss_phase_3.set_conversation("placeholder")
boss_phase_3.set_health(150)
boss_phase_3.set_lowest_dmg_value(0)
boss_phase_3.set_highest_dmg_value(50)
boss_arena_3.add_character(boss_phase_3)

#items ACT III
boss_phase_1_key = Item("Boss Phase 1")
boss_phase_2_key = Item("Boss Phase 2")
boss_phase_3_key = Item("Boss Phase 3")

#rewards 1
rocket_launcher = Weapon("Rocket launcher")
rocket_launcher.set_description("A VERY powerful ranged weapon! reliable but damage is limited")
rocket_launcher.set_lowest_dmg_value(20)
rocket_launcher.set_highest_dmg_value(65)
rocket_launcher.set_dmg_type("ranged")
upgrade_room_1.add_item(rocket_launcher)

rocket_hammer = Weapon("Rocket Hammer")
rocket_hammer.set_description("A VERY powerful melee weapon! can do alot of damage is also very dodgeable")
rocket_hammer.set_lowest_dmg_value(0)
rocket_hammer.set_highest_dmg_value(85)
rocket_hammer.set_dmg_type("melee")
upgrade_room_1.add_item(rocket_hammer)

#rewards 2
laser_sights = Item("Laser sights")
laser_sights.set_description("-- +25% increased ranged damage --")
upgrade_room_2.add_item(laser_sights)

mech_suit_overclock = Item("Mech Suit Overclocking")
mech_suit_overclock.set_description("-- +25% increased melee damage --")
upgrade_room_2.add_item(mech_suit_overclock)

#Story functions
def randomise_room_act2():
    random_room = random.choice([plaza, main_road, crash_site, security_room])
    return random_room

def take_item(item, items):
    print("------------------------" + ("-" * len(item.get_name())))
    print("You put the " + item.get_name() + " in your bag")
    print("------------------------" + ("-" * len(item.get_name())))
    bag.update({item.get_name(): item})
    items.remove(item)

def respawn(act):
    global current_cave, player_health, dead

    print("\n--- You feel consciousness returning... ---\n")

    player_health = 100
    dead = False

    if act == 1:
        current_cave = cryo_respository
        print("You awaken back in the Cryo Repository...")
    
    elif act == 2:
        current_cave = main_road
        print("You awaken near the Borealis crash site...")
    
    elif act == 3:
        current_cave = control_facility_gate
        print("You awaken at the Control Facility Gate...")

    print("Try again.\n")

#gameplay loop

bag = {
    "kill" : kill,
    "nothing" : nothing
}

#starting location/ACT
act = 1
current_cave = cryo_respository

#act 1 events
event_act1_1_mech_suit = False
event_act1_2_seeker = False

#act 2 events
automaton_sentry_2_location = randomise_room_act2()
automaton_sentry_3_location = randomise_room_act2()
event_act2_1_start = False
event_act2_2_sentry1 = False
event_act2_3_sentry2 = False
event_act2_4_sentry3 = False
event_act2_5_keys = False
event_act2_6_keeper = False
event_act2_7_powercell = False

#act 3 events
event_act3_1_boss_1 = False
event_act3_2_boss_2 = False
event_act3_3_boss_3 = False
event_act3_4_rocket_hammer = False
event_act3_5_rocket_launcher = False
event_act3_6_sights = False
event_act3_7_overclock = False
event_act3_8_BOMBSAWAY = False



player_health = 100
dead = False
fighting = False
player_turn = False
enemy_turn = True
ranged_dmg_done_modifier = 1
melee_dmg_done_modifier = 1
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
    #command = command.lower()
    print("-----------------------------------------------------------------------------")

    #navigation
    if command in ["north", "south", "east", "west"]:
            current_cave = current_cave.move(command, bag)

    # Talk to the inhabitant
    elif command == "talk":
        if not inhabitant:
            print("There's no one here to talk to")

        elif len(inhabitant) == 1:
            char = inhabitant[0]
            print("You talk to " + char.name)
            char.talk()

        else:
            print("Who do you want to talk to?")
            for char in inhabitant:
                print("- " + char.name)

            choice = input()

            for char in inhabitant:
                if char.name == choice:
                    char.talk()
                    break

    # Fight with the inhabitant
    elif command == "fight":
        fighting = True
        player_turn = True
        enemy_turn = False

        if not inhabitant:
            print("There is no one here to fight with")
            continue

        # filter only enemies
        enemies = [char for char in inhabitant if isinstance(char, Enemy)]

        if not enemies:
            print("There is no one here to fight with")
            continue

        elif len(enemies) == 1:
            enemy = enemies[0]
            print("You engage " + enemy.name)

        else:
            print("Who do you want to fight?")
            for char in enemies:
                print("- " + char.name)

            choice = input()

            enemy = None
            for char in enemies:
                if char.name == choice:
                    enemy = char
                    break

            if not enemy:
                print("Invalid choice")
                continue

        while fighting:
            if player_turn:
                if player_health <= 0:
                    print("you were defeated by " + enemy.name)
                    fighting = False
                    respawn(act)
                    break

                if enemy.health <= 0:
                    print("You defeated " + enemy.name)
                    current_cave.remove_character(enemy)
                    player_health = 100
                    fighting = False
                    break

                print("-------------------------")
                print("Available weapons:")
                for item in bag.values():
                    if isinstance(item, Weapon):
                        print("* " + item.get_name())

                weapon_name = input("What will you fight with?\n")

                if weapon_name in bag:
                    if bag[weapon_name].item_dmg_type == "ranged":
                        dmg_done = bag[weapon_name].get_dmg_value()
                        enemy.health = enemy.health - (dmg_done * ranged_dmg_done_modifier)
                        print(str(dmg_done * ranged_dmg_done_modifier) + " damage done")
                        print("ranged dmg")
                        player_turn = False
                        enemy_turn = True
                    elif bag[weapon_name].item_dmg_type == "melee":
                        dmg_done = bag[weapon_name].get_dmg_value()
                        enemy.health = enemy.health - (dmg_done * melee_dmg_done_modifier)
                        print(str(dmg_done * melee_dmg_done_modifier) + " damage done")
                        print("melee dmg")
                        player_turn = False
                        enemy_turn = True
                else:
                    print("You don't have a " + weapon_name)

            elif enemy_turn:
                print("\n" + enemy.name + " attacks!")
                dmg = enemy.get_dmg_value()
                player_health = player_health - dmg
                print(str(dmg) + " damage taken")

                print("----------------")
                print("Player Health: " + str(player_health))
                print("Enemy Health: " + str(enemy.health))
                print("----------------\n")

                enemy_turn = False
                player_turn = True

    elif command == "take":
        if not items:
            print("There is nothing here to take")

        elif len(items) == 1:
            # AUTO TAKE
            item = items[0]
            take_item(item, items)

        else:
            print("What do you want to take?")
            for item in items:
                print("- " + item.name)

            choice = input()

            for item in items:
                if item.get_name() == choice:
                    take_item(item, items)
                    break

    #events
    if act == 1:
        if "Mk3 Mech Suit" in bag and event_act1_1_mech_suit == False:
            bag.update({"Power Punch!" : power_punch})
            bag.update({"Explosive Shell" : explosive_shell})
            cargo_bay.add_character(automaton_seeker)
            event_act1_1_mech_suit = True

        if automaton_seeker not in cargo_bay.get_character() and event_act1_1_mech_suit == True and event_act1_2_seeker == False and current_cave == cargo_bay: 
            cargo_bay.set_description("[Cargo Bay description placeholder]\n----------------------------------------------------\n[Use Mech Suit] to clear debris and escape the ship!\n----------------------------------------------------")
            if command == "Use Mech Suit":
                print("\n")
                print("Using the Mech Suit, you clear the fallen debris. \nThe sound of metal scaping against the ships hull fills the room. \nYou manage to escape the escape the Borealis!")
                print("\n")
                print("Act I Complete")
                event_act1_2_seeker = True
                current_cave = main_road
                act = 2
                bag.pop("Mk3 Mech Suit")
                bag.pop("Power Punch!")
                bag.pop("Explosive Shell")
                print("\n")
                print("--- ACT II ---")
                print("\n")
                print("As you make your way north from the Borealis crash site,\nits not long until the mech suit begins to make a strange noise.\nIts motors jitter and each movement is weaker than the last.\nThen suddenly, the mech suit stops...dead in its tracks.\nAs you inspect the suit, you find it, the power cell\nit's damaged from you earlier battle with the seeker.\nWithout the suit, you'll never make it to the room\n\n-- Maybe there's a power cell around here somewhere? --")
                print("\n")

    elif act == 2:
        if current_cave == factory_gate and automaton_sentry_1 not in current_cave.get_character() and event_act2_2_sentry1 == False:
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

        if current_cave == automaton_sentry_2_location and automaton_sentry_2 not in current_cave.get_character() and event_act2_2_sentry1 == True and event_act2_3_sentry2 == False:
            bag.update({"Green Keycard" : green_key_card})
            print("\n")
            print("------------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Green Keycard] and you put it in your bag. Maybe this is for the gate?")
            print("------------------------------------------------------------------------------------------------------")
            print("\n")
            event_act2_3_sentry2 = True

        if current_cave == automaton_sentry_3_location and automaton_sentry_3 not in current_cave.get_character() and event_act2_2_sentry1 == True and event_act2_4_sentry3 == False:
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

        if current_cave == factory_floor and automaton_factory_keeper not in current_cave.get_character() and event_act2_6_keeper == False:
            bag.update({"Power-cell" : power_cell})
            print("\n")
            print("---------------------------------------------------------------------------------------------------------------------")
            print("The automaton factory keeper dropped a [Power-cell] and you put it in your bag. You can finally power your mech suit!")
            print("---------------------------------------------------------------------------------------------------------------------")
            print("\n")
            gate_terminal.set_conversation("Gate locking: Disengaged")
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
                current_cave = control_facility_gate
                print("\n")
                print("--- ACT III ---")
                print("\n")
                print("You make your way to the foot of the steely spire which dominates the skyline,\nThe Megafactory Control Facility\nAs you step foot through the gate, you see the visage of a tall and menacing machine\n-- looks like there's going to be one last fight... --")
                print("\n")
                
    elif act == 3:
        if current_cave == boss_arena_1 and boss_phase_1 not in current_cave.get_character() and event_act3_1_boss_1 == False:
            bag.update({"Boss Phase 1" : boss_phase_1_key})
            print("\n")
            print("Congratulatulations message 1")
            print("\n")
            event_act3_1_boss_1 = True

        if current_cave == boss_arena_2 and boss_phase_2 not in current_cave.get_character() and event_act3_2_boss_2 == False:
            bag.update({"Boss Phase 2" : boss_phase_2_key})
            print("\n")
            print("Congratulatulations message 2")
            print("\n")
            event_act3_2_boss_2 = True

        if current_cave == boss_arena_3 and boss_phase_3 not in current_cave.get_character() and event_act3_3_boss_3 == False:
            bag.update({"Boss Phase 3" : boss_phase_3_key})
            print("\n")
            print("Congratulatulations message 3")
            print("\n")
            event_act3_3_boss_3 = True

        if current_cave == upgrade_room_1 and rocket_hammer not in current_cave.get_item() and event_act3_4_rocket_hammer == False:
            current_cave.remove_item(rocket_launcher)
            event_act3_4_rocket_hammer = True

        if current_cave == upgrade_room_1 and rocket_launcher not in current_cave.get_item() and event_act3_5_rocket_launcher == False:
            current_cave.remove_item(rocket_hammer)
            event_act3_5_rocket_launcher = True

        if current_cave == upgrade_room_2 and laser_sights not in current_cave.get_item() and event_act3_6_sights == False:
            current_cave.remove_item(mech_suit_overclock)
            ranged_dmg_done_modifier = ranged_dmg_done_modifier + 0.25
            event_act3_6_sights = True

        if current_cave == upgrade_room_2 and mech_suit_overclock not in current_cave.get_item() and event_act3_7_overclock == False:
            current_cave.remove_item(laser_sights)
            melee_dmg_done_modifier = melee_dmg_done_modifier + 0.25
            event_act3_7_overclock = True

        if current_cave == control_room and event_act3_8_BOMBSAWAY == False:
            if command == "Activate Self-destruct Sequence":
                print("Megafacories go Boom!")
                Rocket_room.set_description("time to get outa here")
                event_act3_8_BOMBSAWAY = True

        if current_cave == Rocket_room and event_act3_8_BOMBSAWAY == True:
            if command == "Activate Launch Sequence":
                print("You won the game")



print("\n")
print("Game Over")