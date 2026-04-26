class Mansion:
    def __init__(self):
        self.rooms = {
            "Kitchen": ["Ballroom", "Dining Room"],
            "Ballroom": ["Kitchen", "Conservatory", "Hall"],
            "Conservatory": ["Ballroom", "Library"],
            "Dining Room": ["Kitchen", "Lounge"],
            "Lounge": ["Dining Room", "Hall"],
            "Hall": ["Lounge", "Ballroom", "Study"],
            "Study": ["Hall", "Library"],
            "Library": ["Study", "Conservatory", "Billiard Room"],
            "Billiard Room": ["Library"]
        }

    def get_rooms(self):
        return list(self.rooms.keys())

    def get_adjacent_rooms(self, room):
        return self.rooms.get(room, [])
