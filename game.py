from mansion import Mansion
from character import Character
from weapon import Weapon
from player import Player
from solution import Solution


class Game:
    def __init__(self):
        self.mansion = Mansion()

        self.characters = [
            Character("Miss Scarlett", "Hall"),
            Character("Colonel Mustard", "Dining Room"),
            Character("Mrs. Peacock", "Conservatory"),
            Character("Professor Plum", "Study"),
            Character("Mrs. White", "Kitchen"),
            Character("Mr. Green", "Ballroom")
        ]

        self.weapons = [
            Weapon("Candlestick"),
            Weapon("Revolver"),
            Weapon("Rope"),
            Weapon("Knife"),
            Weapon("Lead Pipe"),
            Weapon("Wrench")
        ]

        self.solution = Solution(
            self.characters,
            self.weapons,
            self.mansion.get_rooms()
        )

        self.player = Player(self.characters[0])

    def display_current_location(self):
        print(f"You are currently in: {self.player.character.current_room}")

    def display_available_moves(self):
        current_room = self.player.character.current_room
        available_rooms = self.mansion.get_adjacent_rooms(current_room)

        print("Available rooms:")
        for room in available_rooms:
            print(f"- {room}")

    def move_player(self):
        self.display_current_location()
        self.display_available_moves()

        selected_room = input("Enter the room you want to move to: ")

        if self.player.move(self.mansion, selected_room):
            print(f"Moved to {selected_room}.")
        else:
            print("Invalid move. You can only move to an adjacent room.")

    def make_suggestion(self):
        print("\nMake a suggestion.")

        character = input("Enter character name: ")
        weapon = input("Enter weapon name: ")
        room = self.player.character.current_room

        print(
            f"Suggestion: {character} committed the crime "
            f"with the {weapon} in the {room}."
        )

        if self.solution.check_guess(character, weapon, room):
            print("Correct suggestion! You solved the mystery.")
            return True

        print("Incorrect suggestion.")
        return False

    def start(self):
        print("Welcome to Cluedo!")
        print("You are playing as Miss Scarlett.")
        print()

        game_over = False

        while not game_over:
            self.move_player()

            make_guess = input("Would you like to make a suggestion? (yes/no): ")

            if make_guess.lower() == "yes":
                game_over = self.make_suggestion()

            continue_game = input("Continue playing? (yes/no): ")

            if continue_game.lower() != "yes":
                game_over = True

        print("Game ended.")
