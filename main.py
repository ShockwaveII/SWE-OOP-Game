from cave import Cave 
from character import Character
from character import Enemy, Friend
from item import Weapon, Item
import tkinter as tk
from tkinter import scrolledtext
import random
import pygame

#pygame.mixer.init()
act_1_audio = "Act_1_audio.mp3"
act_2_3_audio = "Act_2_3_audio.mp3"

#weapons
pistol = Weapon("Pistol")
pistol.set_dmg_range(" - 10-30 ranged damage")
pistol.set_description("An abandoned pistol, half-buried in the snow - 10-30 ranged damage")
pistol.set_lowest_dmg_value(10)
pistol.set_highest_dmg_value(30)
pistol.set_dmg_type("ranged")

combat_knife = Weapon("Combat Knife")
combat_knife.set_dmg_range(" - 0-40 melee damage")
combat_knife.set_description("A gunmetal grey combat knife, someone must have lost it - 0-40 melee damage")
combat_knife.set_lowest_dmg_value(0)
combat_knife.set_highest_dmg_value(40)
combat_knife.set_dmg_type("melee")

power_punch = Weapon("Power Punch")
power_punch.set_dmg_range(" - 0-50 melee damage")
power_punch.set_lowest_dmg_value(0)
power_punch.set_highest_dmg_value(50)
power_punch.set_dmg_type("melee")

explosive_shell = Weapon("Explosive Shell")
explosive_shell.set_dmg_range(" - 20-40 ranged damage")
explosive_shell.set_lowest_dmg_value(20)
explosive_shell.set_highest_dmg_value(40)
explosive_shell.set_dmg_type("ranged")

kill = Weapon("kill")
kill.set_dmg_range(" 1000 ranged dmg")
kill.set_lowest_dmg_value(1000)
kill.set_highest_dmg_value(1000)
kill.set_dmg_type("ranged")

nothing = Weapon("nothing")
nothing.set_dmg_range(" 0 melee damage")
nothing.set_lowest_dmg_value(0)
nothing.set_highest_dmg_value(0)
nothing.set_dmg_type("melee")

#items ACT I
armoury_key = Item("Armoury Key Card")
armoury_key.set_description("This looks useful")

mech_suit = Item("Mk3 Mech Suit")
mech_suit.set_description("A powerful Mechanised Exo Suit, looks good at clearing debris")

#items ACT II
red_key_card = Item("red Keycard")
green_key_card = Item("green Keycard")
blue_key_card = Item("blue Keycard")
factory_gate_key = Item("factory Gate Key")
power_cell = Item("power-cell")





#rooms ACT I
cryo_respository = Cave("Cryo Repository")
cryo_respository.set_description("A cold and sterile room, illuminated by the faint and\nrefracted glow of the rows upon rows of damaged cyro-cells.")
cryo_respository.set_locked(False)

hallway = Cave ("Hallway")
hallway.set_description("A dimly lit metallic hallway where stray sparks spring from the abundnace of exposed wiring.\nEvery other steel plate which lines the hall is either deformed, burnt or fallen to the floor.")
hallway.set_locked(False)

armoury = Cave("Armoury")
armoury.set_description("A sturdy and reinforced section of the ship which has largely survived the crash.\nInside lays racks of special weapons, tools and equipment\n-- The centrepiece is a large yellow mech exosuit --")
armoury.set_locked(True)
armoury.set_key("Armoury Key Card")
armoury.add_item(mech_suit)

cargo_bay = Cave("Cargo Bay")
cargo_bay.set_description("A hevily damaged section of the ship, half crushed by\na mountain of debris and what was formerlly considered 'cargo'.\nA lone beam of natural sunlight from outside the ship penetrates through!\n\n-- Maybe some heavy machinery from the armoury could clear this debris? --")
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
main_road.set_description("A wide asphalt road that spans as far as the eye can see a deep layer\nof snow covers the surrounding area which reflects the moonlight\nThe mech suit is inconspicuously hidden under a torn fabric tarpn\n\n-- There's a bright artificial light emanating from the east --")
main_road.set_locked(False)
main_road.add_item(pistol)

plaza = Cave("Plaza")
plaza.set_description("A quiet and spacious environment that looks designed for leasure\nA lone vending machine in pristine conditions stands out, yet\nseems entirely unimportant. Its almost calming...")
plaza.set_locked(False)

crash_site = Cave("Borealis Crash Site View")
crash_site.set_description("The Borealis dominates the landscape despite lacking its front third.\nThe fires still flicker and dance as its situation deteriorates\n\n-- The automatons will pay for this! --")
crash_site.set_locked(False)

factory_gate = Cave("Factory Gate")
factory_gate.set_description("A tall concrete wall stretches endlessly in two directions. Its\nentrance is a thick steel gate that looks capable of stopping\nanything in its tracks")
factory_gate.set_locked(False)
factory_gate.add_item(combat_knife)

factory_floor = Cave("Factory Floor")
factory_floor.set_description("An expansive platform littered with heavy industrial machinery. An\nominous red light engulfs the facility instilling a sense of terror\n")
factory_floor.set_locked(True)
factory_floor.set_key("factory gate key")

security_room = Cave("Security Room")
security_room.set_description("A small and quiet room which stands out in the snow. The flurescent\nlight illuminates its surroundings, prime of which is a lone tree\nstump with a knife jabbed in it")
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
automaton_sentry_1.set_lowest_dmg_value(10)
automaton_sentry_1.set_highest_dmg_value(40)
factory_gate.add_character(automaton_sentry_1)

automaton_sentry_2 = Enemy("Automaton Sentry", "An armed Automaton Guard, looks like he's looking for someone")
automaton_sentry_2.set_conversation("Sentry 02 reporting!I found the intruder, over!")
automaton_sentry_2.set_health(100)
automaton_sentry_2.set_lowest_dmg_value(10)
automaton_sentry_2.set_highest_dmg_value(40)

automaton_sentry_3 = Enemy("Automaton Sentry", "An armed Automaton Guard, looks like he's on high alert")
automaton_sentry_3.set_conversation("This is sentry 03! He's here! The intruder's here, over!")
automaton_sentry_3.set_health(100)
automaton_sentry_3.set_lowest_dmg_value(10)
automaton_sentry_3.set_highest_dmg_value(40)

automaton_factory_keeper = Enemy("Automaton Factory Keeper", "A large and intimidating automaton with mech upgrades.\nIt looks like his upgrades are powered by a power-cell!")
automaton_factory_keeper.set_conversation("You dare set foot in my factory?!")
automaton_factory_keeper.set_health(120)
automaton_factory_keeper.set_lowest_dmg_value(15)
automaton_factory_keeper.set_highest_dmg_value(45)
factory_floor.add_character(automaton_factory_keeper)

gate_terminal = Character("Gate Control Terminal", "A digital terminal that controls the factory gate - [talk] to access terminal")
gate_terminal.set_conversation("Gate locking: Engaged\n-- looks like there are 3 key slots --")
factory_gate.add_character(gate_terminal)

mech_suit_unpowered = Character("Mk3 Mech Suit", "A powerful Mechanised Exo Suit - [talk] to access diagnostics")
mech_suit_unpowered.set_conversation("Mk3 Mech Suit - Diagnostics:\nPowercell status: Damaged\n-- Warning insufficient power! --")
main_road.add_character(mech_suit_unpowered)

vending_machine = Character("Vending machine", "A lone, dimly lit vending machine - [talk] to use")
vending_machine.set_conversation("Beep! Boop!... ~-!$@&&# ... Ding! One can of motor oil. (This is useless)")
plaza.add_character(vending_machine)

sleepy = Character("Sleepy Automaton ", "A security automaton asleep in the security office. talk?")
sleepy.set_conversation("zzz... (Do automatons dream of electric sheep?)")
security_room.add_character(sleepy)

#rooms ACT III
control_facility_gate = Cave("Control Facility Gate")
control_facility_gate.set_description("The tall and domineering entrance to the control facility which\ngoverns all megafactories on the planet. A robust and mechanical\nfigure stands expectingly in the doorway, a cold sneer on his\nrobotic face.")
control_facility_gate.set_locked(False)

boss_arena_1 = Cave("1st Floor - The Lobby")
boss_arena_1.set_description("The ground lobby of the control facility. Its a large ornate room\nwith plentiful space to fight. The elevator is at the very end.")
boss_arena_1.set_locked(False)

boss_arena_2 = Cave("2nd Floor - The Observation platform")
boss_arena_2.set_description("The floor is dominated by a large window that offers a stunning\nview of the megafactory. Its industrial might a symbol of automaton power\nIt will soon be reduced to rubble.")
boss_arena_2.set_locked(False)

boss_arena_3 = Cave("3rd Floor - The Inner Sanctum")
boss_arena_3.set_description("The inner most chamber of the control facility. The control room itself is\nwithin sight, the automaton's guardian and commander is the only obstacle left.")
boss_arena_3.set_locked(False)
upgrade_room_1 = Cave("Elevator - Floor 1")
upgrade_room_1.set_description("An industrial elevator with multiple cargo crates. Some of them\nmay be useful.\n\n--- You can only take one ---")
upgrade_room_1.set_locked(True)
upgrade_room_1.set_key("boss phase 1")

upgrade_room_2 = Cave("Elevator - Floor 2")
upgrade_room_2.set_description("An industrial elevator with multiple cargo crates. Some of them\nmay be useful.\n\n--- You can only take one ---")
upgrade_room_2.set_locked(True)
upgrade_room_2.set_key("boss phase 2")

control_room = Cave("Control Room")
control_room.set_description("A small chamber littered with a plethora of screens and blinking\nlights. The centrepeice is a large red button that reads Detonate.\n\n---------------------------------------------------------------\nType [Self Destruct] to destroy all megafactories on Cyberstan!\n---------------------------------------------------------------")
control_room.set_locked(True)
control_room.set_key("boss phase 3")

Rocket_room = Cave("Emergency Escape Rocket")
Rocket_room.set_description("A small rocket designed to transport a select few off-world in the\nevent of an emergency. The controls are relatively simple.\n\n------------------------------------\nType [Liftoff] to launch the rocket!\n------------------------------------")
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
boss_phase_1 = Enemy("Automaton Viceroy", "The proud mechanical ruler of Cyberstan come put you in the ground")
boss_phase_1.set_conversation("Stand ready, human. You shall be reuinted with your fallen comrades very soon...")
boss_phase_1.set_health(100)
boss_phase_1.set_lowest_dmg_value(10)
boss_phase_1.set_highest_dmg_value(45)
boss_arena_1.add_character(boss_phase_1)

boss_phase_2 = Enemy("Automaton Viceroy - 2nd form", "The despotic viceroy, now upgraded with an arsenal of heat-seeking rockets")
boss_phase_2.set_conversation("You think this is over? No. Be ready to greet your foul brethren in hell!")
boss_phase_2.set_health(150)
boss_phase_2.set_lowest_dmg_value(15)
boss_phase_2.set_highest_dmg_value(50)
boss_arena_2.add_character(boss_phase_2)

boss_phase_3 = Enemy("Automaton Viceroy - 3rd form", "What stands before you is a hulking steel monster. His tall frame filled out with a bulk of guns and thick metal armour")
boss_phase_3.set_conversation("YOU DIE HERE, MEATBAG!!!")
boss_phase_3.set_health(250)
boss_phase_3.set_lowest_dmg_value(15)
boss_phase_3.set_highest_dmg_value(55)
boss_arena_3.add_character(boss_phase_3)

control_console = Character("Control Console", "A large assortment of buttons and switches with a large detonation button in the centre")
control_console.set_conversation("Self destruct system on standby, awaiting input")
control_room.add_character(control_console)

rocket_control_terminal = Character("Rocket Control Terminal","input [talk] to access ship diagnostics")
rocket_control_terminal.set_conversation("Emergency Escape Rocket Status Report:\nEngines: Online\nSheilds: Online\nFire Supression System: Online\nHull Integrity: Intact\nClimate Control System: Online\n\n--- Ready for liftoff ---")
Rocket_room.add_character(rocket_control_terminal)

#items ACT III
boss_phase_1_key = Item("boss phase 1")
boss_phase_2_key = Item("boss phase 2")
boss_phase_3_key = Item("boss phase 3")

#rewards 1
rocket_launcher = Weapon("Rocket launcher")
rocket_launcher.set_dmg_range(" - 20-65 ranged damage")
rocket_launcher.set_description("A VERY powerful ranged weapon! reliable but damage is limited - 20-65 ranged damage")
rocket_launcher.set_lowest_dmg_value(20)
rocket_launcher.set_highest_dmg_value(60)
rocket_launcher.set_dmg_type("ranged")
upgrade_room_1.add_item(rocket_launcher)

rocket_hammer = Weapon("Rocket Hammer")
rocket_hammer.set_dmg_range(" - 0-85 melee damage")
rocket_hammer.set_description("A VERY powerful melee weapon! can do alot of damage is also very dodgeable - 0-85 melee damage")
rocket_hammer.set_lowest_dmg_value(0)
rocket_hammer.set_highest_dmg_value(75)
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
    print("------------------------------" + ("-" * len(item.get_name())))
    print("You put the " + item.get_name() + " in your inventory")
    print("------------------------------" + ("-" * len(item.get_name())))
    bag.update({item.get_name().lower(): item})
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

def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)

#gameplay loop

bag = {
    "kill" : kill,
    "nothing" : nothing
}

#starting location/ACT
act = 3
current_cave = control_facility_gate

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



print("-------------------------------------------------------------------------------------------------")
print("You are the ‘Sole Survivor’, an Imperial marine aboard the ISV Borealis which has crashed\non the Forgeworld of ‘Cyberstan’, occupied by the treacherous Automoton Legion. The legion\nof mechanical monstrosities has launched its brutal war of aggression against the Imperium\nof Terra, sending the galaxy into turmoil. Now alone and behind enemy lines, you have no choice\nbut to take down the Forgeworld and ensure it cannot fuel the automaton war machine.")
print("-------------------------------------------------------------------------------------------------")
print("\n")
print("--- ACT I ---")
print("\n")
print("You wake up to the cold embrace of your cryo-cell as it opens...")
#play_music(act_1_audio)
while dead == False:
    #descriptions
    
    print("\n")
    current_cave.get_details()
    print("\n")

    items = current_cave.get_item()
    if items:
        print("-- Items - Type [take] to put weapon in inventory --")
        for item in items:
            item.describe()
        print("\n")
    

    inhabitant = current_cave.get_character()
    if inhabitant:
        print("-- Characters - Type [talk] to interact --")
        for character in inhabitant:
            character.describe()

    print("\n")
    command = input(">")
    command = command.lower()
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
            choice = choice.lower()

            for char in inhabitant:
                if char.name.lower() == choice:
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
            choice = choice.lower()

            enemy = None
            for char in enemies:
                if char.name.lower() == choice:
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
                print("Available weapons - Type the name of the weapon to use it:")
                for item in bag.values():
                    if isinstance(item, Weapon):
                        print("* " + item.get_name() +item.get_dmg_range())

                weapon_name = input("What will you fight with?\n")
                weapon_name = weapon_name.lower()

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
            item = items[0]
            take_item(item, items)

        else:
            print("What do you want to take?")
            for item in items:
                print("- " + item.name)

            choice = input()
            choice = choice.lower()

            for item in items:
                if item.get_name().lower() == choice:
                    take_item(item, items)
                    break

    #events
    if act == 1:
        if "mk3 mech suit" in bag and event_act1_1_mech_suit == False:
            bag.update({"power punch" : power_punch})
            bag.update({"explosive shell" : explosive_shell})
            cargo_bay.add_character(automaton_seeker)
            event_act1_1_mech_suit = True

        if automaton_seeker not in cargo_bay.get_character() and event_act1_1_mech_suit == True and event_act1_2_seeker == False and current_cave == cargo_bay: 
            cargo_bay.set_description("A heavily damaged section of the ship, half crushed by\na mountain of debris and what was formally considered 'cargo'.\nA lone beam of natural sunlight from outside the ship penetrates through!\n\n---------------------------------------------------------\nType [Use Mech Suit] to clear debris and escape the ship!\n---------------------------------------------------------")
            if command == "use mech suit":
                print("\n")
                print("Using the Mech Suit, you clear the fallen debris.\nThe sound of metal scraping against the ships hull fills the room.\nYou manage to escape the escape the Borealis!")
                print("\n")
                print("Act I Complete")
                event_act1_2_seeker = True
                current_cave = main_road
                act = 2
                bag.pop("mk3 mech suit")
                bag.pop("power punch")
                bag.pop("explosive shell")
                print("\n")
                print("--- ACT II ---")
                print("\n")
                print("As you make your way north from the Borealis crash site,\nits not long until the mech suit begins to make a strange noise.\nIts motors jitter and each movement is weaker than the last.\nThen suddenly, the mech suit stops...dead in its tracks.\nAs you inspect the suit, you find it, the power cell\nit's damaged from you earlier battle with the seeker.\nWithout the suit, you'll never make it to the room\n\n-- Maybe there's a power cell around here somewhere? --")
                print("\n")
                pygame.mixer.music.stop()
                #play_music(act_2_3_audio)

    elif act == 2:
        if current_cave == factory_gate and automaton_sentry_1 not in current_cave.get_character() and event_act2_2_sentry1 == False:
            bag.update({"red Keycard" : red_key_card})
            print("\n")
            print("It looks like your fight drew some attention. You hear other automatons arriving in the distance")
            print("\n")
            print("----------------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Red Keycard] and you put it in your inventory. Maybe this is for the gate?")
            print("----------------------------------------------------------------------------------------------------------")
            print("\n")
            automaton_sentry_2_location.add_character(automaton_sentry_2)
            automaton_sentry_3_location.add_character(automaton_sentry_3)
            event_act2_2_sentry1 = True

        if current_cave == automaton_sentry_2_location and automaton_sentry_2 not in current_cave.get_character() and event_act2_2_sentry1 == True and event_act2_3_sentry2 == False:
            bag.update({"green Keycard" : green_key_card})
            print("\n")
            print("------------------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Green Keycard] and you put it in your inventory. Maybe this is for the gate?")
            print("------------------------------------------------------------------------------------------------------------")
            print("\n")
            event_act2_3_sentry2 = True

        if current_cave == automaton_sentry_3_location and automaton_sentry_3 not in current_cave.get_character() and event_act2_2_sentry1 == True and event_act2_4_sentry3 == False:
            bag.update({"blue Keycard" : blue_key_card})
            print("\n")
            print("-----------------------------------------------------------------------------------------------------------")
            print("The automaton sentry dropped a [Blue Keycard] and you put it in your inventory. Maybe this is for the gate?")
            print("-----------------------------------------------------------------------------------------------------------")
            print("\n")
            event_act2_4_sentry3 = True

        if current_cave == factory_gate and event_act2_3_sentry2 == True and event_act2_4_sentry3 == True and event_act2_5_keys == False:
            bag.update({"factory gate key" : factory_gate_key})
            print("\n")
            print("-------------------------------------------------------------------")
            print("Looks like you have all 3 keys, maybe you can enter the factory now")
            print("-------------------------------------------------------------------")
            print("\n")
            event_act2_5_keys = True

        if current_cave == factory_floor and automaton_factory_keeper not in current_cave.get_character() and event_act2_6_keeper == False:
            bag.update({"power-cell" : power_cell})
            print("\n")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("The automaton factory keeper dropped a [Power-cell] and you put it in your inventory. You can finally power your mech suit!")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("\n")
            gate_terminal.set_conversation("Gate locking: Disengaged")
            event_act2_6_keeper = True

        if current_cave == main_road and event_act2_6_keeper == True and event_act2_7_powercell == False:
            main_road.set_description("Placeholder description\n-------------------------------------------\nType [Power Mech Suit] to insert power-cell\n-------------------------------------------")
            if command == "power mech suit":
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
                bag.update({"power punch" : power_punch})
                bag.update({"explosive shell" : explosive_shell})
                
    elif act == 3:
        if current_cave == boss_arena_1 and boss_phase_1 not in current_cave.get_character() and event_act3_1_boss_1 == False:
            bag.update({"boss phase 1" : boss_phase_1_key})
            print("\n")
            print("The Automaton viceroy stumbles back momenteray in a breif moment of weakness.\n'This isn't over...' he says before blasting his way to the next floor\n-- The elevator should be accessable now --")
            print("\n")
            event_act3_1_boss_1 = True

        if current_cave == boss_arena_2 and boss_phase_2 not in current_cave.get_character() and event_act3_2_boss_2 == False:
            bag.update({"boss phase 2" : boss_phase_2_key})
            print("\n")
            print("The Automaton viceroy recoils at your blow, his once composed\ndemenor now consumed by rage. 'LETS FINSIH THIS!!' he roars\nblasting his way to the next floor again\n-- The elevator should be accessable now --")
            print("\n")
            event_act3_2_boss_2 = True

        if current_cave == boss_arena_3 and boss_phase_3 not in current_cave.get_character() and event_act3_3_boss_3 == False:
            bag.update({"boss phase 3" : boss_phase_3_key})
            print("\n")
            print("The Automaton viceroy collapses, clearly too damaged to get\nback up again. 'Curse you human!' he managed to utter out\nbefore his systems go offline.")
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
            if command == "self destruct":
                current_cave.set_description("A small chamber littered with a plethora of screens and blinking\nlights. The centrepeice is a large red button that reads Detonate.\n\n--- Hurry to the escape rocket! ---")
                print("As you press the button, you feel the ground start to shake. Your\neyes are drawn to the screens that now flash with a red 'warning' sign\nAll megafactories all arounf the planet have begun the self destruct\nsequence, including the one you're in right now!")
                event_act3_8_BOMBSAWAY = True

        if current_cave == Rocket_room and event_act3_8_BOMBSAWAY == True:
            if command == "liftoff":
                print("You activate the rocket's ignition and it begins to violently rattle.\nThe engines roar to life and soon the rocket is thrust into the stars.\nBefore long, you feel the weightlessness of zero gravity as you\nfloat from your seat towards the window. Outside you see the\nplanet, Cyberstan. The many megafactories that litter its surface igniting like fireworks.\nYour comrades are avenged and the automatons crippled.\n\n--- Congratulations, you beat the game! ---")
                dead = True
