class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = []
        self.item = []
        self.locked = False
        self.key = None

    def get_description(self):
        return self.description
    def set_description(self, cave_description):
        self.description = cave_description

    def describe (self):
        print(self.description)

    def set_name (self, cave_name):
        self.name = cave_name
    def get_name (self):
        return self.name
    
    def add_character(self, new_character):
        self.character.append(new_character)

    def get_character(self):
        return self.character

    def remove_character(self, character):
        if character in self.character:
            self.character.remove(character)
    
    def add_item(self, new_item):
        self.item.append(new_item)

    def get_item(self):
        return self.item

    def remove_item(self, item):
        if item in self.item:
            self.item.remove(item)
    
    #Locked Room system:
    def get_locked(self):
        return self.locked
    def set_locked(self, room_locked):
        self.locked = room_locked

    def get_key(self):
        return self.key
    def set_key(self, room_key):
        self.key = room_key

       
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        print("-- Location: ["+ self.name +"] --")
        print(self.description)
        print("\n")
        print("-- Connected Locations --")
        for direction in self .linked_caves:
            cave = self.linked_caves[direction]
            print("The " + cave.get_name() + " is " + direction)
            
    def move(self, direction, bag):
        if direction in self.linked_caves:
            next_room = self.linked_caves[direction]
            if next_room.get_locked():
                if next_room.get_key().lower() in bag:
                    print("\n")
                    print("------------------------------------")
                    print("You use the key to unlock the room.")
                    print("------------------------------------")
                    next_room.set_locked(False)
                    return next_room
                else:
                    print("\n")
                    print("----------------------------------------------------------")
                    print("This room is locked. Maybe there's a key around somewhere?")
                    print("----------------------------------------------------------")
                    return self
            else:
                return next_room
                
        else:
            return self
        
