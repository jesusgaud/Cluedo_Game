# 🎯 Cluedo Game

---

## 📌 Overview

This project implements a **full digital version of the classic Cluedo (Clue) board game** using Python.

The application models a mansion environment where multiple players (**human and AI-controlled**) move between rooms, make suggestions, track deductions, and attempt to solve the mystery by identifying the correct:

- 🕵️ **Suspect (Character)**
- 🗡️ **Weapon**
- 🏠 **Room**

The system supports both:
- 🖥️ Terminal-based gameplay
- 🎮 Advanced graphical user interface (GUI) built with **Tkinter**

This project evolved across multiple phases, culminating in an **AI-driven, interactive gameplay experience with real-time deduction tracking**.

---

## 🎮 Core Features

### 🕹️ Game Mechanics
- Mansion layout with connected rooms
- Character and weapon definitions
- Randomized solution generation
- Player movement restricted to adjacent rooms
- Suggestion system with refutation logic
- Accusation system with win/loss conditions
- Card distribution across players

### 🖥️ User Experience
- Fully interactive **Tkinter-based GUI**
- Live game board with player movement visualization
- Click-based navigation for movement
- Real-time feedback console (game log)
- 📖 "How to Play" instructional panel
- 🧾 Detective’s Notepad (live deduction tracker)

---

## 🧠 AI Implementation (Phases 1–3)

### 🤖 Phase 1 – Basic AI
- Computer players take turns automatically
- Movement is randomly selected from valid adjacent rooms
- Suggestions are randomly generated

### 🧩 Phase 2 – Deduction-Based AI
- Each AI player maintains a **Deduction Notebook**
- AI tracks:
  - Known cards (owned or revealed)
  - Eliminated possibilities
  - Unknown possibilities
- AI avoids suggesting known or eliminated cards
- AI prioritizes unknown suspects, weapons, and rooms

### 🎯 Phase 3 – Accusation AI
- AI makes an accusation **ONLY when logically confident**
- Conditions:
  - Exactly one suspect remains
  - Exactly one weapon remains
  - Exactly one room remains
- Accusations are based on **logical elimination (not randomness)**

---

## 🧾 Detective’s Notepad (Key Feature)

The GUI includes a real-time deduction tracker called:

### **"Detective’s Notepad"**

Tracks:
- Suspects
- Weapons
- Rooms

### Legend:
- ❓ Unknown
- ✔️ Confirmed solution
- ❌ Eliminated

💡 This mimics the original Clue game’s deduction sheet for strategic gameplay.

---

## 🖼️ Graphical User Interface Layout

The UI is designed using a **quadrant-based layout**:

| Quadrant | Component |
|--------|----------|
| 🔲 Top Left | 🎲 Live Game Board |
| 🔲 Top Right | 🧾 Detective’s Notepad |
| 🔲 Bottom Left | 📜 Feedback Console / Game Log (Scrollable) |
| 🔲 Bottom Right | 📖 How-To-Play Instructions |

### Additional UI Features:
- Player tokens rendered dynamically on the board
- Highlighted valid movement rooms
- Animated movement transitions
- Popup dialogs for:
  - Suggestions
  - Accusations

---

## ▶️ How to Run

### 🖥️ Terminal Version

```bash
cd JesusGaud_Project2_SourceCode
python main.py

cd JesusGaud_Project2_SourceCode
python ui.py

---

## 🎯 Gameplay Instructions
Click a highlighted room to move
After moving, make a suggestion
A suggestion includes:
Character
Weapon
Current room
Other players attempt to refute your suggestion
Use:
📜 Game Log
🧾 Detective’s Notepad
to track deductions
Make a final accusation when confident
🏆 Winning Condition
✔️ Correct accusation → Player wins
❌ Incorrect accusation → Game ends and solution is revealed

---

## 🏗️ Project Structure
Core Modules
main.py → Terminal entry point
ui.py → Graphical user interface
game.py → Core game orchestration
player.py → Player state and behavior
character.py → Character definitions
weapon.py → Weapon definitions
mansion.py → Room layout and adjacency
solution.py → Mystery solution logic
card.py → Card abstraction
AI Modules
computer_player_ai.py → AI decision logic
deduction_notebook.py → Deduction tracking system

---

## ⚙️ Requirements
Python 3.x
Tkinter (included with standard Python)

✅ No external libraries required

## 🌐 GitHub Repository

Clone the repository:
git clone https://github.com/jesusgaud/Cluedo_Game.git
cd Cluedo_Game
python ui.py

---

## 🧱 Development Practices

This project follows strong software engineering principles:

Object-Oriented Programming (OOP)
Separation of Concerns
Modular architecture
Scalable design for future AI enhancements
Version control with Git and GitHub
🌿 Branching Strategy
main → Final submission
ai_phase1 → Basic AI implementation
ai_phase2 → Deduction-based AI

---

## 🧪 Testing and Validation

✔️ Manual gameplay testing completed

Verified:
Movement rules
Suggestion/refutation logic
AI turn automation
Deduction updates
Game termination conditions

✅ No runtime errors or crashes observed

---

## 🏁 Conclusion

This project demonstrates the integration of:

🎮 Game design
🧱 Object-Oriented Programming
🧠 Artificial Intelligence (rule-based + deduction-based)
🖥️ GUI development

The final system delivers a complete, interactive Cluedo experience with intelligent computer players and a professional user interface.
