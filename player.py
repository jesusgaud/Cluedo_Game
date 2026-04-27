class Player:
    def __init__(self, name, character):
        self.name = name
        self.character = character
        self.cards = []
        self.notes = []

    def move(self, mansion, room):
        current_room = self.character.current_room
        valid_rooms = mansion.get_adjacent_rooms(current_room)

        if room in valid_rooms:
            self.character.move_to(room)
            return True

        return False

    def add_card(self, card):
        self.cards.append(card)

    def add_note(self, note):
        self.notes.append(note)

    def show_cards(self):
        print(f"\n{self.name}'s cards:")
        if not self.cards:
            print("No cards assigned.")
        else:
            for card in self.cards:
                print(f"- {card}")

    def show_notes(self):
        print(f"\n{self.name}'s deduction notes:")
        if not self.notes:
            print("No notes yet.")
        else:
            for note in self.notes:
                print(f"- {note}")
