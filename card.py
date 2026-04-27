class Card:
    def __init__(self, name, card_type):
        self.name = name
        self.card_type = card_type

    def __str__(self):
        return f"{self.name} ({self.card_type})"
