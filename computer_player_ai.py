import random


class ComputerPlayerAI:
    """
    Handles automated behavior for computer-controlled players.

    Phase 2 behavior:
    - Prefer moving toward rooms that are still possible solution rooms.
    - Prefer suggestions using unknown suspects and weapons.
    - Use the current room as the suggested room.
    - Make an accusation only when the notebook has narrowed the solution.
    """

    def choose_room(self, player, mansion):
        current_room = player.character.current_room
        available_rooms = mansion.get_adjacent_rooms(current_room)

        if not available_rooms:
            return None

        if player.notebook is None:
            return random.choice(available_rooms)

        unknown_rooms = player.notebook.get_unknown_rooms()
        preferred_rooms = [
            room for room in available_rooms
            if room in unknown_rooms
        ]

        if preferred_rooms:
            return random.choice(preferred_rooms)

        return random.choice(available_rooms)

    def choose_suggestion(self, player, game):
        if player.notebook is None:
            character = random.choice(game.characters).name
            weapon = random.choice(game.weapons).name
            room = player.character.current_room
            return character, weapon, room

        unknown_suspects = player.notebook.get_unknown_suspects()
        unknown_weapons = player.notebook.get_unknown_weapons()

        if unknown_suspects:
            character = random.choice(unknown_suspects)
        else:
            character = random.choice(game.characters).name

        if unknown_weapons:
            weapon = random.choice(unknown_weapons)
        else:
            weapon = random.choice(game.weapons).name

        room = player.character.current_room

        return character, weapon, room

    def should_accuse(self, player):
        if player.notebook is None:
            return False

        return player.notebook.is_ready_to_accuse()

    def choose_accusation(self, player, game):
        if player.notebook is not None:
            accusation = player.notebook.get_accusation()

            if accusation is not None:
                return accusation

        character = random.choice(game.characters).name
        weapon = random.choice(game.weapons).name
        room = random.choice(game.mansion.get_rooms())

        return character, weapon, room
