import random


class Solution:
    def __init__(self, characters, weapons, rooms):
        self.character = random.choice(characters)
        self.weapon = random.choice(weapons)
        self.room = random.choice(rooms)

    def check_guess(self, character, weapon, room):
        return (
            self.character.name == character
            and self.weapon.name == weapon
            and self.room == room
        )
