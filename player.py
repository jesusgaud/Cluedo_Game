class Player:
    def __init__(self, character):
        self.character = character

    def move(self, mansion, room):
        current_room = self.character.current_room
        valid_rooms = mansion.get_adjacent_rooms(current_room)

        if room in valid_rooms:
            self.character.move_to(room)
            return True

        return False
