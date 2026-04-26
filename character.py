class Character:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def move_to(self, room):
        self.current_room = room
