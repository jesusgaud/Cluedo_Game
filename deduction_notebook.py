class DeductionNotebook:
    """
    Tracks known and eliminated possibilities for a player.

    Phase 2 behavior:
    - Stores all possible suspects, weapons, and rooms.
    - Eliminates cards the player owns.
    - Eliminates cards shown to the player.
    - Tracks unresolved no-refutation suggestions.
    - Identifies when only one suspect, weapon, and room remain.
    """

    def __init__(self, character_names, weapon_names, room_names):
        self.possible_suspects = set(character_names)
        self.possible_weapons = set(weapon_names)
        self.possible_rooms = set(room_names)

        self.eliminated_cards = set()
        self.known_cards = set()
        self.unrefuted_suggestions = []

    def eliminate_card(self, card):
        self.eliminated_cards.add(card)
        self.known_cards.add(card)

        self.possible_suspects.discard(card)
        self.possible_weapons.discard(card)
        self.possible_rooms.discard(card)

    def record_owned_cards(self, cards):
        for card in cards:
            self.eliminate_card(card)

    def record_shown_card(self, card):
        self.eliminate_card(card)

    def record_unrefuted_suggestion(self, character, weapon, room):
        self.unrefuted_suggestions.append((character, weapon, room))

    def get_unknown_suspects(self):
        return list(self.possible_suspects)

    def get_unknown_weapons(self):
        return list(self.possible_weapons)

    def get_unknown_rooms(self):
        return list(self.possible_rooms)

    def is_ready_to_accuse(self):
        return (
            len(self.possible_suspects) == 1
            and len(self.possible_weapons) == 1
            and len(self.possible_rooms) == 1
        )

    def get_accusation(self):
        if not self.is_ready_to_accuse():
            return None

        return (
            next(iter(self.possible_suspects)),
            next(iter(self.possible_weapons)),
            next(iter(self.possible_rooms))
        )
