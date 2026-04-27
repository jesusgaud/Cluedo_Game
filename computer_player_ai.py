import random


class ComputerPlayerAI:
    """
    Handles basic automated behavior for computer-controlled players.

    Phase 1 behavior:
    - Move to a random adjacent room.
    - Make a random suggestion using:
        1. A random character
        2. A random weapon
        3. The computer player's current room
    - Does not make automatic accusations yet.
    """

    def choose_room(self, player, mansion):
        """
        Select a valid adjacent room for the computer player.

        Args:
            player: The computer-controlled Player object.
            mansion: The Mansion object containing room connections.

        Returns:
            str or None: The selected room name, or None if no moves are available.
        """
        current_room = player.character.current_room
        available_rooms = mansion.get_adjacent_rooms(current_room)

        if not available_rooms:
            return None

        return random.choice(available_rooms)

    def choose_suggestion(self, player, game):
        """
        Select a basic suggestion for the computer player.

        Args:
            player: The computer-controlled Player object.
            game: The Game object containing characters, weapons, and room data.

        Returns:
            tuple: (character_name, weapon_name, room_name)
        """
        character = random.choice(game.characters).name
        weapon = random.choice(game.weapons).name
        room = player.character.current_room

        return character, weapon, room

    def should_accuse(self, player):
        """
        Decide whether the computer player should make a final accusation.

        Phase 1 intentionally disables automatic accusations to avoid ending
        the game unexpectedly during early AI implementation.

        Args:
            player: The computer-controlled Player object.

        Returns:
            bool: Always False in Phase 1.
        """
        return False

    def choose_accusation(self, player, game):
        """
        Placeholder for future accusation logic.

        Phase 2 or Phase 3 can use deduction notes, known cards, and remaining
        possibilities to make a smarter accusation.

        Args:
            player: The computer-controlled Player object.
            game: The Game object.

        Returns:
            tuple: (character_name, weapon_name, room_name)
        """
        character = random.choice(game.characters).name
        weapon = random.choice(game.weapons).name
        room = random.choice(game.mansion.get_rooms())

        return character, weapon, room
