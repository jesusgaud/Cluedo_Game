Cluedo Game - Project 2

Description:
This project implements a simplified digital version of the classic Cluedo (Clue) board game using Python.
The game models a mansion environment where players move between rooms, make suggestions, and attempt to
solve the mystery by identifying the correct character, weapon, and room.

The application supports both a terminal-based version and a graphical user interface (GUI) version.

----------------------------------------

Features:

- Mansion layout with connected rooms
- Character and weapon definitions
- Random solution generation (character, weapon, room)
- Player movement between adjacent rooms
- Suggestion system with refutation logic
- Accusation system to determine the winner
- Card distribution among players
- Deduction notes tracking
- Graphical User Interface (Tkinter-based)

----------------------------------------

How to Run (Terminal Version):

1. Open a terminal
2. Navigate to the project directory:
   cd JesusGaud_Project2_SourceCode
3. Run the game:
   python main.py

----------------------------------------

How to Run (Graphical UI Version):

1. Open a terminal
2. Navigate to the project directory:
   cd JesusGaud_Project2_SourceCode
3. Run:
   python ui.py

----------------------------------------

Gameplay Instructions:

- Move between adjacent rooms using available options
- Make a suggestion once inside a room
- Other players will attempt to refute your suggestion
- Track information using deduction notes
- Make a final accusation at any time
- If correct → you win
- If incorrect → game ends and solution is revealed

----------------------------------------

Project Structure:

- main.py → Entry point (terminal version)
- ui.py → Graphical user interface
- game.py → Core game logic
- player.py → Player logic and state tracking
- character.py → Character definitions
- weapon.py → Weapon definitions
- mansion.py → Room layout and navigation
- solution.py → Mystery solution logic

----------------------------------------

Requirements:

- Python 3.x
- Tkinter (included with standard Python installation)

No external libraries are required.

----------------------------------------

(Optional - GitHub):

1. Clone the repository:
   git clone https://github.com/jesusgaud/Cluedo_Game.git

2. Navigate to the folder:
   cd Cluedo_Game

3. Run:
   python main.py
   OR
   python ui.py

----------------------------------------

Notes:

- Code follows object-oriented design principles
- Game logic separates responsibilities across modules
- Designed for scalability and future feature expansion
