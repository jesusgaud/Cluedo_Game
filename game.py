import random

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

        self.players = [
            Player("Human Player", self.characters[0]),
            Player("Computer Player 1", self.characters[1]),
            Player("Computer Player 2", self.characters[2])
        ]

        self.player = self.players[0]

        self.setup_cards()

    def setup_cards(self):
        character_cards = [c.name for c in self.characters]
        weapon_cards = [w.name for w in self.weapons]
        room_cards = self.mansion.get_rooms()

        deck = character_cards + weapon_cards + room_cards

        solution_cards = [
            self.solution.character.name,
            self.solution.weapon.name,
            self.solution.room
        ]

        for card in solution_cards:
            if card in deck:
                deck.remove(card)

        random.shuffle(deck)

        i = 0
        for card in deck:
            self.players[i].add_card(card)
            i = (i + 1) % len(self.players)

    def display_menu(self):
        print("\nChoose an action:")
        print("1. Move")
        print("2. Suggest")
        print("3. Accuse")
        print("4. View Cards")
        print("5. View Notes")
        print("6. Quit")

    def display_location(self):
        print(f"\nCurrent Room: {self.player.character.current_room}")

    def move_player(self):
        self.display_location()

        available = self.mansion.get_adjacent_rooms(
            self.player.character.current_room
        )

        print("Available rooms:")
        for r in available:
            print(f"- {r}")

        choice = input("Move to: ").strip()

        if self.player.move(self.mansion, choice):
            print(f"Moved to {choice}")
        else:
            print("Invalid move")

    def make_suggestion(self):
        print("\n--- Suggestion ---")

        character = input("Character: ").strip()
        weapon = input("Weapon: ").strip()
        room = self.player.character.current_room

        print(f"\nSuggestion: {character} with {weapon} in {room}")

        self.handle_refutation(character, weapon, room)

    def handle_refutation(self, character, weapon, room):
        suggested = [character, weapon, room]

        for player in self.players:
            if player == self.player:
                continue

            matching_cards = [
                card for card in player.cards if card in suggested
            ]

            if matching_cards:
                shown_card = random.choice(matching_cards)

                print(f"{player.name} shows you a card: {shown_card}")

                self.player.add_note(
                    f"{player.name} showed {shown_card}"
                )
                return

        print("No one could refute your suggestion.")
        self.player.add_note(
            f"No refute: {character}, {weapon}, {room}"
        )

    def make_accusation(self):
        print("\n--- Final Accusation ---")

        character = input("Character: ").strip()
        weapon = input("Weapon: ").strip()
        room = input("Room: ").strip()

        if self.solution.check_guess(character, weapon, room):
            print("✅ Correct! You win!")
        else:
            print("❌ Incorrect. You lose.")
            print(
                f"Solution was: {self.solution.character.name}, "
                f"{self.solution.weapon.name}, {self.solution.room}"
            )

        return True

    def show_cards(self):
        self.player.show_cards()

    def show_notes(self):
        self.player.show_notes()

    def start(self):
        print("=== CLUEDO GAME ===")
        print("You are Miss Scarlett")

        game_over = False

        while not game_over:
            self.display_location()
            self.display_menu()

            choice = input("Choice: ").strip()

            if choice == "1":
                self.move_player()
            elif choice == "2":
                self.make_suggestion()
            elif choice == "3":
                game_over = self.make_accusation()
            elif choice == "4":
                self.show_cards()
            elif choice == "5":
                self.show_notes()
            elif choice == "6":
                game_over = True
            else:
                print("Invalid option")

        print("Game ended.")
