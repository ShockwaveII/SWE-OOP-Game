
import random
class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.health = 0
        self.dmg = 0
        self.starting_health = 0

    def set_weakness(self, weakness):
        self.weakness = weakness

    #health system
    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health
    
    def set_starting_health(self, starting_health_input):
        self.starting_health = starting_health_input

    def get_starting_health(self):
        return self.starting_health
    
    
    def display_health(self):
        print(self.name + ' has ' + str(self.health) + ' health')

    #Stealing System   
    def steal(self):
        print("You steal from " + self.name)

    #combat system
    def set_lowest_dmg_value(self, item_lowest_dmg_value):
        self.item_lowest_dmg_value = item_lowest_dmg_value

    def get_lowest_dmg_value(self):
        return self.item_lowest_dmg_value
    
    def set_highest_dmg_value(self, item_highest_dmg_value):
        self.item_highest_dmg_value = item_highest_dmg_value

    def get_highest_dmg_value(self):
        return self.item_highest_dmg_value
    
    def get_dmg_value(self):
        dmg = random.randint(self.item_lowest_dmg_value, self.item_highest_dmg_value)
        return dmg

    #health system
    def set_health(self, health):
        self.health = health

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back")
        # What other methods could your Friend class have?




