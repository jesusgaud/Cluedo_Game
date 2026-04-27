import tkinter as tk
from tkinter import messagebox
from game import Game
from computer_player_ai import ComputerPlayerAI
import time


class CluedoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cluedo Game - Final Version")
        self.root.geometry("1000x780")

        self.game = Game()
        self.computer_ai = ComputerPlayerAI()
        self.current_player_index = 0
        self.game_over = False
        self.ai_turn_in_progress = False

        self.tracker = {
            "Suspects": {character.name: "?" for character in self.game.characters},
            "Weapons": {weapon.name: "?" for weapon in self.game.weapons},
            "Rooms": {room: "?" for room in self.game.mansion.get_rooms()}
        }

        self.room_positions = {
            "Study": (50, 50),
            "Hall": (250, 50),
            "Lounge": (450, 50),
            "Library": (50, 250),
            "Dining Room": (450, 250),
            "Billiard Room": (50, 400),
            "Conservatory": (50, 550),
            "Ballroom": (250, 550),
            "Kitchen": (450, 550),
        }

        self.highlighted_rooms = []
        self.player_colors = ["red", "blue", "green"]

        self.build_ui()
        self.refresh_ui()
        self.refresh_tracker()

        self.log_message("Welcome to Cluedo!")
        self.log_message("Click a highlighted room to move.")
        self.log_message("After each move, the player may make a suggestion.")
        self.log_message("Use the accusation button when ready to solve the mystery.")

    def build_ui(self):
        tk.Label(
            self.root,
            text="CLUEDO",
            font=("Arial", 26, "bold")
        ).pack()

        self.info_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12)
        )
        self.info_label.pack()

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(fill="both", expand=True)

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(fill="both", expand=True)

        # Quadrant 1: Live Board
        board_frame = tk.Frame(top_frame)
        board_frame.pack(side="left", fill="both", expand=True, padx=(40, 0))

        self.canvas = tk.Canvas(
            board_frame,
            width=600,
            height=650,
            bg="#88bfa7"
        )
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.on_canvas_click)

        button_frame = tk.Frame(board_frame)
        button_frame.pack(pady=5)

        tk.Button(
            button_frame,
            text="Make Accusation",
            width=18,
            bg="darkred",
            fg="white",
            command=self.make_accusation
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Show Current Player Cards",
            width=22,
            command=self.show_current_player_cards
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Quit",
            width=12,
            command=self.root.quit
        ).grid(row=0, column=2, padx=5)

        # Quadrant 2: Detective's Notepad
        notepad_frame = tk.Frame(top_frame)
        notepad_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        tk.Label(
            notepad_frame,
            text="Detective's Notepad",
            font=("Arial", 12, "bold"),
            fg="darkred"
        ).pack(pady=(0, 4))

        self.tracker_box = tk.Text(
            notepad_frame,
            height=25,
            width=60,
            font=("Consolas", 9),
            bg="#fffaf0",
            fg="#24140e",
            relief="ridge",
            bd=2
        )
        self.tracker_box.pack(fill="both", expand=True)

        # Quadrant 3: Feedback Console / Game Log with scrollbar
        log_frame = tk.Frame(bottom_frame)
        log_frame.pack(side="left", fill="both", expand=True, padx=(40, 0))

        tk.Label(
            log_frame,
            text="Feedback Console / Game Log",
            font=("Arial", 11, "bold")
        ).pack(anchor="w")

        log_text_frame = tk.Frame(log_frame)
        log_text_frame.pack(fill="both", expand=True)

        self.log = tk.Text(
            log_text_frame,
            height=9,
            width=90,
            font=("Consolas", 9)
        )
        self.log.pack(side="left", fill="both", expand=True)

        self.log_scrollbar = tk.Scrollbar(
            log_text_frame,
            orient="vertical",
            command=self.log.yview
        )
        self.log_scrollbar.pack(side="right", fill="y")

        self.log.config(yscrollcommand=self.log_scrollbar.set)

        # Quadrant 4: How to Play Instructions
        instructions_frame = tk.Frame(bottom_frame)
        instructions_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        instructions_text = (
            "How to Play\n\n"
            "1. Click a highlighted room to move.\n"
            "2. After moving, make a suggestion.\n"
            "3. A suggestion includes a character, weapon, and current room.\n"
            "4. Other players may refute by showing a matching card.\n"
            "5. Use card information, the game log, and the Detective's Notepad.\n"
            "6. Make a final accusation when you think you know the answer.\n\n"
            "Goal:\n"
            "Identify the correct suspect, weapon, and room."
        )

        self.instructions_box = tk.Label(
            instructions_frame,
            text=instructions_text,
            font=("Arial", 10),
            justify="left",
            bg="#f4ead2",
            fg="#24140e",
            padx=12,
            pady=10,
            relief="ridge",
            bd=2,
            anchor="nw",
            width=60
        )
        self.instructions_box.pack(fill="both", expand=True)

    def refresh_tracker(self):
        self.tracker_box.config(state="normal")
        self.tracker_box.delete("1.0", tk.END)

        self.tracker_box.insert(tk.END, "Legend: ? = Unknown | ✓ = Correct | ✗ = Eliminated\n\n")

        for category, items in self.tracker.items():
            self.tracker_box.insert(tk.END, f"{category}\n")
            self.tracker_box.insert(tk.END, "-" * len(category) + "\n")

            for name, status in items.items():
                self.tracker_box.insert(tk.END, f"{status} {name}\n")

            self.tracker_box.insert(tk.END, "\n")

        self.tracker_box.config(state="disabled")

    def update_tracker(self, character, weapon, room):
        solution = self.game.solution

        if character in self.tracker["Suspects"]:
            self.tracker["Suspects"][character] = (
                "✓" if character == solution.character.name else "✗"
            )

        if weapon in self.tracker["Weapons"]:
            self.tracker["Weapons"][weapon] = (
                "✓" if weapon == solution.weapon.name else "✗"
            )

        if room in self.tracker["Rooms"]:
            self.tracker["Rooms"][room] = (
                "✓" if room == solution.room else "✗"
            )

        self.refresh_tracker()

    def draw_board_background(self):
        # Outer green board
        self.canvas.create_rectangle(
            5, 5, 595, 645,
            fill="#8fc7ad",
            outline="#1f3d2b",
            width=5
        )

        # Yellow hallway grid
        for x in range(20, 581, 30):
            for y in range(20, 631, 30):
                self.canvas.create_rectangle(
                    x, y, x + 30, y + 30,
                    fill="#f0d66f",
                    outline="#9c8a3a",
                    width=1
                )

        # Central decorative area, intentionally no "Clue" text
        self.canvas.create_rectangle(
            235, 285, 365, 385,
            fill="#24364d",
            outline="#8b0000",
            width=4
        )

        self.canvas.create_rectangle(
            255, 305, 345, 365,
            fill="#d7d0c0",
            outline="#5a2a1f",
            width=2
        )

        self.canvas.create_line(255, 335, 345, 335, fill="#5a2a1f", width=2)
        self.canvas.create_line(300, 305, 300, 365, fill="#5a2a1f", width=2)

        # Decorative wall paths
        self.canvas.create_line(20, 20, 580, 20, fill="#b00020", width=5)
        self.canvas.create_line(20, 20, 20, 630, fill="#b00020", width=5)
        self.canvas.create_line(580, 20, 580, 630, fill="#b00020", width=5)
        self.canvas.create_line(20, 630, 580, 630, fill="#b00020", width=5)

    def draw_room_details(self, room, x, y):
        if room == "Study":
            self.canvas.create_rectangle(x + 15, y + 20, x + 100, y + 35, fill="#8b5a2b")
            self.canvas.create_rectangle(x + 20, y + 55, x + 95, y + 70, fill="#c4a484")

        elif room == "Hall":
            self.canvas.create_rectangle(x + 30, y + 20, x + 90, y + 70, fill="#d8c3a5")
            self.canvas.create_line(x + 35, y + 30, x + 85, y + 30, fill="#6b4f3f", width=2)
            self.canvas.create_line(x + 35, y + 60, x + 85, y + 60, fill="#6b4f3f", width=2)

        elif room == "Lounge":
            self.canvas.create_rectangle(x + 18, y + 25, x + 105, y + 65, fill="#b98b82")
            self.canvas.create_oval(x + 35, y + 35, x + 88, y + 58, fill="#f4d1c1")

        elif room == "Library":
            self.canvas.create_rectangle(x + 15, y + 15, x + 30, y + 85, fill="#7b3f00")
            self.canvas.create_rectangle(x + 90, y + 15, x + 105, y + 85, fill="#7b3f00")
            self.canvas.create_oval(x + 45, y + 35, x + 80, y + 65, fill="#d8c3a5")

        elif room == "Dining Room":
            self.canvas.create_rectangle(x + 25, y + 25, x + 95, y + 65, fill="#a0522d")
            self.canvas.create_oval(x + 30, y + 30, x + 90, y + 60, fill="#d8b384")

        elif room == "Billiard Room":
            self.canvas.create_rectangle(x + 25, y + 30, x + 95, y + 65, fill="#2f6b4f")
            self.canvas.create_oval(x + 35, y + 40, x + 45, y + 50, fill="#ffffff")
            self.canvas.create_oval(x + 75, y + 40, x + 85, y + 50, fill="#ffffff")

        elif room == "Conservatory":
            self.canvas.create_rectangle(x + 20, y + 25, x + 100, y + 75, fill="#bfe3c0")
            self.canvas.create_line(x + 20, y + 25, x + 100, y + 75, fill="#3c7a3c", width=2)
            self.canvas.create_line(x + 100, y + 25, x + 20, y + 75, fill="#3c7a3c", width=2)

        elif room == "Ballroom":
            self.canvas.create_rectangle(x + 20, y + 20, x + 100, y + 75, fill="#e5d3b3")
            self.canvas.create_oval(x + 35, y + 30, x + 85, y + 65, fill="#f7e6b5")

        elif room == "Kitchen":
            self.canvas.create_rectangle(x + 20, y + 20, x + 100, y + 40, fill="#c0c0c0")
            self.canvas.create_rectangle(x + 30, y + 55, x + 90, y + 75, fill="#ffffff")
            self.canvas.create_oval(x + 45, y + 58, x + 55, y + 68, fill="#808080")
            self.canvas.create_oval(x + 65, y + 58, x + 75, y + 68, fill="#808080")

    def draw_board(self):
        self.canvas.delete("all")
        self.room_boxes = {}

        self.draw_board_background()

        for room, (x, y) in self.room_positions.items():
            color = "#d3d3d3"

            if room in self.highlighted_rooms:
                color = "#a8e6cf"

            current_player = self.game.players[self.current_player_index]
            if room == current_player.character.current_room:
                color = "#ffd1d1"

            rect = self.canvas.create_rectangle(
                x, y, x + 120, y + 100,
                fill=color,
                outline="darkred",
                width=3
            )

            self.draw_room_details(room, x, y)

            text = self.canvas.create_text(
                x + 60, y + 50,
                text=room,
                font=("Arial", 9, "bold")
            )

            self.room_boxes[rect] = room
            self.room_boxes[text] = room

        self.draw_players()

    def draw_players(self):
        for i, player in enumerate(self.game.players):
            room = player.character.current_room

            if room in self.room_positions:
                x, y = self.room_positions[room]

                self.canvas.create_oval(
                    x + 20 + (i * 18),
                    y + 20 + (i * 18),
                    x + 50 + (i * 18),
                    y + 50 + (i * 18),
                    fill=self.player_colors[i],
                    outline="black",
                    width=2
                )

                self.canvas.create_text(
                    x + 35 + (i * 18),
                    y + 35 + (i * 18),
                    text=str(i + 1),
                    fill="white",
                    font=("Arial", 9, "bold")
                )

    def on_canvas_click(self, event):
        if self.game_over:
            messagebox.showinfo("Game Over", "The game has already ended.")
            return

        current_player = self.game.players[self.current_player_index]

        if self.is_computer_player(current_player):
            messagebox.showinfo("Computer Turn", "Please wait. The computer player is taking its turn.")
            return

        clicked_room = self.get_room_from_click(event.x, event.y)

        if not clicked_room:
            return

        current_room = current_player.character.current_room

        valid_moves = self.game.mansion.get_adjacent_rooms(current_room)

        if clicked_room in valid_moves:
            self.animate_move(current_player, clicked_room)
            self.log_message(f"{current_player.name} moved from {current_room} to {clicked_room}.")

            self.prompt_suggestion(current_player)
        else:
            messagebox.showwarning(
                "Invalid Move",
                f"{current_player.name} cannot move directly from {current_room} to {clicked_room}."
            )

    def get_room_from_click(self, x, y):
        for item, room in self.room_boxes.items():
            coords = self.canvas.coords(item)

            if len(coords) == 4:
                if coords[0] <= x <= coords[2] and coords[1] <= y <= coords[3]:
                    return room

            if len(coords) == 2:
                text_x, text_y = coords
                room_x, room_y = self.room_positions[room]
                if room_x <= x <= room_x + 120 and room_y <= y <= room_y + 100:
                    return room

        return None

    def animate_move(self, player, new_room):
        player.character.move_to(new_room)

        for _ in range(3):
            self.draw_board()
            self.root.update()
            time.sleep(0.1)

    def prompt_suggestion(self, player):
        popup = tk.Toplevel(self.root)
        popup.title("Make Suggestion")
        popup.geometry("320x260")

        tk.Label(
            popup,
            text=f"{player.name}, make a suggestion",
            font=("Arial", 12, "bold")
        ).pack(pady=8)

        tk.Label(popup, text=f"Current Room: {player.character.current_room}").pack(pady=4)

        tk.Label(popup, text="Character").pack()
        character_var = tk.StringVar(value=self.game.characters[0].name)
        tk.OptionMenu(
            popup,
            character_var,
            *[character.name for character in self.game.characters]
        ).pack()

        tk.Label(popup, text="Weapon").pack()
        weapon_var = tk.StringVar(value=self.game.weapons[0].name)
        tk.OptionMenu(
            popup,
            weapon_var,
            *[weapon.name for weapon in self.game.weapons]
        ).pack()

        def submit_suggestion():
            character = character_var.get()
            weapon = weapon_var.get()
            room = player.character.current_room

            self.log_message(
                f"{player.name} suggests: {character} with the {weapon} in the {room}."
            )

            self.update_tracker(character, weapon, room)

            result = self.refute_suggestion(player, character, weapon, room)
            self.log_message(result)

            popup.destroy()
            self.next_turn()

        def skip_suggestion():
            self.log_message(f"{player.name} skipped making a suggestion.")
            popup.destroy()
            self.next_turn()

        tk.Button(
            popup,
            text="Submit Suggestion",
            command=submit_suggestion
        ).pack(pady=8)

        tk.Button(
            popup,
            text="Skip Suggestion",
            command=skip_suggestion
        ).pack()

    def refute_suggestion(self, suggesting_player, character, weapon, room):
        suggested_items = [character, weapon, room]

        for player in self.game.players:
            if player == suggesting_player:
                continue

            matching_cards = [
                card for card in player.cards
                if card in suggested_items
            ]

            if matching_cards:
                shown_card = matching_cards[0]

                if suggesting_player == self.game.player:
                    suggesting_player.add_note(f"{player.name} showed {shown_card}")

                return f"{player.name} refuted the suggestion by showing: {shown_card}."

        if suggesting_player == self.game.player:
            suggesting_player.add_note(f"No refutation: {character}, {weapon}, {room}")

        return "No player could refute the suggestion."

    def make_accusation(self):
        if self.game_over:
            messagebox.showinfo("Game Over", "The game has already ended.")
            return

        current_player = self.game.players[self.current_player_index]

        popup = tk.Toplevel(self.root)
        popup.title("Final Accusation")
        popup.geometry("320x300")

        tk.Label(
            popup,
            text=f"{current_player.name}, make a final accusation",
            font=("Arial", 12, "bold")
        ).pack(pady=8)

        tk.Label(popup, text="Character").pack()
        character_var = tk.StringVar(value=self.game.characters[0].name)
        tk.OptionMenu(
            popup,
            character_var,
            *[character.name for character in self.game.characters]
        ).pack()

        tk.Label(popup, text="Weapon").pack()
        weapon_var = tk.StringVar(value=self.game.weapons[0].name)
        tk.OptionMenu(
            popup,
            weapon_var,
            *[weapon.name for weapon in self.game.weapons]
        ).pack()

        tk.Label(popup, text="Room").pack()
        room_var = tk.StringVar(value=self.game.mansion.get_rooms()[0])
        tk.OptionMenu(
            popup,
            room_var,
            *self.game.mansion.get_rooms()
        ).pack()

        def submit_accusation():
            character = character_var.get()
            weapon = weapon_var.get()
            room = room_var.get()

            self.log_message(
                f"{current_player.name} accuses: {character} with the {weapon} in the {room}."
            )

            self.update_tracker(character, weapon, room)

            if self.game.solution.check_guess(character, weapon, room):
                messagebox.showinfo("Game Over", f"{current_player.name} wins! Correct accusation.")
                self.log_message(f"GAME OVER: {current_player.name} solved the mystery.")
            else:
                solution = (
                    f"{self.game.solution.character.name}, "
                    f"{self.game.solution.weapon.name}, "
                    f"{self.game.solution.room}"
                )
                messagebox.showinfo(
                    "Game Over",
                    f"Incorrect accusation.\nCorrect solution: {solution}"
                )
                self.log_message(f"GAME OVER: Incorrect accusation. Correct solution: {solution}")

            self.game_over = True
            self.canvas.unbind("<Button-1>")
            popup.destroy()
            self.refresh_ui()

        tk.Button(
            popup,
            text="Submit Accusation",
            bg="darkred",
            fg="white",
            command=submit_accusation
        ).pack(pady=12)

    def show_current_player_cards(self):
        current_player = self.game.players[self.current_player_index]

        if not current_player.cards:
            messagebox.showinfo("Cards", f"{current_player.name} has no cards.")
            return

        messagebox.showinfo(
            f"{current_player.name}'s Cards",
            "\n".join(current_player.cards)
        )

    def is_computer_player(self, player):
        return player.name.startswith("Computer Player")

    def run_computer_turn_if_needed(self):
        if self.game_over or self.ai_turn_in_progress:
            return

        current_player = self.game.players[self.current_player_index]

        if not self.is_computer_player(current_player):
            return

        self.ai_turn_in_progress = True
        self.root.after(750, self.run_computer_turn)

    def run_computer_turn(self):
        if self.game_over:
            self.ai_turn_in_progress = False
            return

        current_player = self.game.players[self.current_player_index]

        if not self.is_computer_player(current_player):
            self.ai_turn_in_progress = False
            return

        current_room = current_player.character.current_room
        selected_room = self.computer_ai.choose_room(current_player, self.game.mansion)

        if selected_room is None:
            self.log_message(f"{current_player.name} has no valid moves and skips movement.")
        else:
            self.animate_move(current_player, selected_room)
            self.log_message(f"{current_player.name} moved from {current_room} to {selected_room}.")

        character, weapon, room = self.computer_ai.choose_suggestion(current_player, self.game)

        self.log_message(
            f"{current_player.name} suggests: {character} with the {weapon} in the {room}."
        )

        self.update_tracker(character, weapon, room)

        result = self.refute_suggestion(current_player, character, weapon, room)
        self.log_message(result)

        self.ai_turn_in_progress = False
        self.root.after(750, self.next_turn)

    def next_turn(self):
        if self.game_over:
            return

        self.current_player_index = (
            self.current_player_index + 1
        ) % len(self.game.players)

        self.refresh_ui()
        self.run_computer_turn_if_needed()

    def refresh_ui(self):
        current_player = self.game.players[self.current_player_index]

        if self.game_over:
            self.info_label.config(
                text=f"Game Over | Last Player: {current_player.name}"
            )
            self.highlighted_rooms = []
        else:
            self.info_label.config(
                text=f"Turn: {current_player.name} | Room: {current_player.character.current_room}"
            )

            if self.is_computer_player(current_player):
                self.highlighted_rooms = []
            else:
                self.highlighted_rooms = self.game.mansion.get_adjacent_rooms(
                    current_player.character.current_room
                )

        self.draw_board()

    def log_message(self, msg):
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CluedoUI(root)
    root.mainloop()
