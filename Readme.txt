Cluedo Game - Project 2 (Final Submission)

---

Description:

This project implements a full digital version of the classic Cluedo (Clue) board game using Python.

The application models a mansion environment where multiple players (human and AI-controlled) move between rooms, make suggestions, track deductions, and attempt to solve the mystery by identifying the correct:

* Suspect (Character)
* Weapon
* Room

The system supports both a terminal-based version and an advanced graphical user interface (GUI) built with Tkinter.

This project evolved across multiple phases, culminating in an AI-driven, interactive gameplay experience with real-time deduction tracking.

---

Core Features:

Game Mechanics:

* Mansion layout with connected rooms
* Character and weapon definitions
* Randomized solution generation
* Player movement restricted to adjacent rooms
* Suggestion system with refutation logic
* Accusation system with win/loss conditions
* Card distribution across players

User Experience:

* Fully interactive Tkinter-based GUI
* Live game board with player movement visualization
* Click-based navigation for movement
* Real-time feedback console (game log)
* "How to Play" instructional panel
* Detective’s Notepad (live deduction tracker)

---

AI Implementation (Phases 1–3):

Phase 1 – Basic AI:

* Computer players take turns automatically
* Movement is randomly selected from valid adjacent rooms
* Suggestions are randomly generated

Phase 2 – Deduction-Based AI:

* Each AI player maintains a Deduction Notebook
* AI tracks:

  * Known cards (owned or revealed)
  * Eliminated possibilities
  * Unknown possibilities
* AI avoids suggesting known or eliminated cards
* AI prioritizes unknown suspects, weapons, and rooms

Phase 3 – Accusation AI:

* AI makes an accusation ONLY when:

  * Exactly one suspect remains
  * Exactly one weapon remains
  * Exactly one room remains
* Accusations are based on logical elimination (not randomness)

---

Detective’s Notepad (Key Feature):

The GUI includes a real-time deduction tracker called:

"Detective’s Notepad"

It displays:

* Suspects
* Weapons
* Rooms

Each item is marked as:

* ? → Unknown
* ✓ → Confirmed solution
* ✗ → Eliminated

This provides a visual deduction system similar to the original board game.

---

Graphical User Interface Layout:

The UI is designed as a quadrant-based system:

Quadrant 1:

* Live Game Board (interactive and animated)

Quadrant 2:

* Detective’s Notepad (AI + player deduction tracking)

Quadrant 3:

* Feedback Console / Game Log (scrollable)

Quadrant 4:

* "How to Play" instructions

Additional UI Features:

* Player tokens rendered on the board
* Highlighted valid movement rooms
* Animated movement transitions
* Popup dialogs for suggestions and accusations

---

How to Run (Terminal Version):

1. Open a terminal

2. Navigate to the project directory:

   cd JesusGaud_Project2_SourceCode

3. Run:

   python main.py

---

How to Run (Graphical UI Version):

1. Open a terminal

2. Navigate to the project directory:

   cd JesusGaud_Project2_SourceCode

3. Run:

   python ui.py

---

Gameplay Instructions:

1. Click a highlighted room to move
2. After moving, make a suggestion
3. A suggestion includes:

   * Character
   * Weapon
   * Current room
4. Other players attempt to refute your suggestion
5. Use:

   * Game Log
   * Detective’s Notepad
     to track deductions
6. Make a final accusation when confident

Winning Condition:

* Correct accusation → Player wins
* Incorrect accusation → Game ends, solution revealed

---

Project Structure:

Core Modules:

* main.py → Terminal entry point
* ui.py → Graphical user interface
* game.py → Core game orchestration
* player.py → Player state and behavior
* character.py → Character definitions
* weapon.py → Weapon definitions
* mansion.py → Room layout and adjacency
* solution.py → Mystery solution logic
* card.py → Card abstraction

AI Modules:

* computer_player_ai.py → AI decision logic
* deduction_notebook.py → Deduction tracking system

---

Requirements:

* Python 3.x
* Tkinter (included with standard Python)

No external libraries are required.

---

GitHub Repository:

Clone the repository:

git clone https://github.com/jesusgaud/Cluedo_Game.git

Navigate to project:

cd Cluedo_Game

Run:

python ui.py

---

Development Practices:

* Object-Oriented Programming (OOP)
* Separation of Concerns
* Modular architecture
* Scalable design for future AI enhancements
* Version control with Git and GitHub

Branching Strategy:

* main → final submission
* ai_phase1 → basic AI implementation
* ai_phase2 → deduction-based AI

---

Testing and Validation:

* Manual gameplay testing completed
* Verified:

  * Movement rules
  * Suggestion/refutation logic
  * AI turn automation
  * Deduction updates
  * Game termination conditions
* No runtime errors or crashes observed

---

Conclusion:

This project demonstrates the integration of:

* Game design
* Object-oriented programming
* Artificial intelligence (rule-based and deduction-based)
* GUI development

The final system provides a complete, interactive Cluedo experience with intelligent computer players and a professional user interface.
