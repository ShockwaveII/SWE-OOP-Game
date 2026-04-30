import random
class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    def describe(self):
        print(
            "The [" + self.name + "] is here - " + self.description
        )

class Weapon(Item):
    def __init__(self, item_name):
        super().__init__(item_name)
        self.item_dmg_type = None
        self.item_lowest_dmg_value = 0
        self.item_highest_dmg_value = 0

    #damage values
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

