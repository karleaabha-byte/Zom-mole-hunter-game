Pasted text.txt
Document
soo pls help me make this in such a way that                  START 
                   │ 
                   ▼ 
             Investigate rooms 
                   │ 
          ┌────────┴────────┐ 
          ▼                 ▼ 
     Storage             Cafeteria 
          │                 │ 
       50/50             Find ??19 
          │                 │ 
     ┌────┴────┐            ▼ 
     │         │        Try PIN 4619 
     ▼         ▼            │ 
   NORMAL    HARD            ▼ 
   RIDDLE    RIDDLE       PIN CRACKED 
                             │ 
                         ┌───┴───┐ 
                         │       │ 
                       50/50    50/50 
                         │       │ 
                         ▼       ▼ 
                    CHALLENGE   NO CHALLENGE 
                         │       │ 
                         ▼       │ 
                      WORDLE     │ 
                         │       │ 
                         ▼       │ 
                       SOLVE     │ 
                         │       │ 
                         └───┬───┘ 
                             ▼ 
                       INTERROGATIONS 
                             │ 
                             ▼ 
                    Zephyr answers 
                       50/50 truth/lie 
                             │ 
                             ▼ 
                         ACCUSATION every time streamlit is reloaded, the agent should have 50-50 choice on actions that it makes whether to help or sabotage

Absolutely 😭 remove the timer entirely. The Wordle/security challenge should just be limited by attempts, not time.

Here’s a copy-pastable README:

# 🧟‍♂️ Zom-Mole Hunter

## Noir Detective Edition

Zom-Mole Hunter is an interactive detective mystery game built with Python and Streamlit.

The player takes the role of a detective investigating a suspicious incident inside a research facility. Evidence has been tampered with, security systems have been compromised, suspects have conflicting alibis, and one member of the team is secretly working against everyone else.

The objective is to investigate the facility, collect evidence, solve puzzles, interrogate suspects, and correctly identify the mole.

---

# 🕵️ The Mystery

At 12:18 AM, a serious incident occurs inside a research facility.

Several suspicious events happen at approximately the same time:

- Six experimental filter cartridges are missing from Storage.
- A laboratory centrifuge has been interrupted.
- A vial has been broken.
- The corridor cameras have lost several minutes of footage.
- The facility's security system has been accessed.
- Someone inside the facility appears to have deliberately interfered with the investigation.

Five employees were still inside the facility:

| Character | Role | Primary Area |
|-----------|------|--------------|
| Raven | Head Chemist | Laboratory |
| Zephyr | Supply Coordinator | Storage |
| Luca | Security Officer | Corridors |
| Marinette | Medic | Medical Bay |
| Adrien | Engineer | Generator Room |

One of them is the hidden mole.

The detective must determine who is responsible.

---

# 🎯 Main Objective

The main objective is to correctly identify the mole.

The mole is:

**Zephyr**

However, the player is not simply told this.

The player must build a case using:

- Physical evidence
- Room clues
- Riddles
- The hidden PIN
- Security information
- Suspect alibis
- Interrogations
- Contradictions
- Zephyr's possible lies
- Detective reasoning

The final accusation determines whether the investigation succeeds or fails.

---

# 🎮 Gameplay Flow

The main gameplay flow is:

```text
START
  │
  ▼
INVESTIGATE ROOMS
  │
  ├───────────────────┐
  ▼                   ▼
STORAGE            CAFETERIA
  │                   │
  │ 50/50             │ 50/50
  │                   │
  ├────────┐          ├────────┐
  ▼        ▼          ▼        ▼
 HELP   SABOTAGE    HELP    SABOTAGE
  │        │          │        │
  ▼        ▼          ▼        ▼
NORMAL    HARD      NORMAL   TAMPERED
RIDDLE    RIDDLE    RECEIPT  RECEIPT
  │        │          │        │
  └────────┴──────────┴────────┘
                   │
                   ▼
              FIND PIN CLUES
                   │
                   ▼
                PIN 4619
                   │
                   ▼
              PIN CRACKED
                   │
                50/50 AI
              ┌────┴────┐
              ▼         ▼
            HELP     SABOTAGE
              │         │
              │       WORDLE
              │         │
              │       SOLVE
              │         │
              └────┬────┘
                   ▼
             INTERROGATIONS
                   │
                   ▼
            QUESTION SUSPECTS
                   │
                   ▼
          ZEPHYR: 50/50 TRUTH/LIE
                   │
                   ▼
              BUILD CASE
                   │
                   ▼
              ACCUSATION
                   │
             ┌─────┴─────┐
             ▼           ▼
          CORRECT       WRONG
             │           │
             ▼           ▼
            WIN         LOSE
🔎 Investigation

The detective can investigate different areas of the facility.

The main investigation areas include:

Laboratory
Storage
Cafeteria

Each area provides information that can be used to reconstruct what happened.

🧪 Laboratory

The Laboratory contains important physical evidence related to the incident.

The Laboratory establishes part of the timeline and provides information that can later be combined with evidence from other rooms.

The Laboratory clue is always available and is not affected by Zephyr's sabotage decision.

The laboratory also contributes to the PIN.

The relevant laboratory number is:

4
📦 Storage

Storage contains the main riddle.

When the player investigates Storage, Zephyr's AI makes an independent 50/50 decision.

The result is either:

HELP

or:

SABOTAGE
If Zephyr helps

The player receives the normal Storage riddle.

The answer is:

BREEZE
If Zephyr sabotages

The player receives a harder/corrupted version of the Storage riddle.

The harder version is designed to make the investigation more difficult without making the entire case impossible.

The answer still relates to the same underlying clue.

The important information is that:

BREEZE

contains six letters.

Therefore:

STORAGE NUMBER = 6
🥤 Cafeteria

The Cafeteria contains a supply/restocking log.

Zephyr also gets an independent 50/50 decision here.

50%
 ├── HELP
 │
 └── SABOTAGE

If Zephyr helps, the normal receipt is available.

If Zephyr sabotages, the receipt is partially tampered with.

The important PIN fragment remains visible:

??19

This is intentional.

Sabotage makes the investigation harder, but it does not completely destroy the information needed to solve the case.

🔐 PIN System

The player must discover a four-digit PIN.

The PIN is constructed from information found during the investigation.

The relevant pieces are:

Laboratory number = 4

Storage answer = BREEZE

Length of BREEZE = 6

Cafeteria suffix = 19

Therefore:

4 + 6 + 19

produces:

4619

The correct PIN is:

4619

Entering the correct PIN unlocks the next stage of the investigation.

🛡️ Security Challenge

After the player successfully cracks the PIN, Zephyr makes another independent 50/50 decision.

There are two possible outcomes.

HELP

Zephyr does not interfere with the security system.

The player proceeds directly to interrogations.

PIN CRACKED
     ↓
HELP
     ↓
INTERROGATIONS
SABOTAGE

Zephyr interferes with the security system.

The player must complete a Wordle-style security challenge before interrogation access is restored.

PIN CRACKED
     ↓
SABOTAGE
     ↓
WORDLE
     ↓
SOLVE
     ↓
INTERROGATIONS
🟩 Wordle Challenge

The security challenge is a five-letter Wordle-style puzzle.

The current answer is:

VENTS

The player has a maximum of:

6 attempts

There is no timer.

The challenge is based only on the number of attempts.

The player receives feedback about each letter and must determine the correct word.

The challenge is successfully completed when the player enters:

VENTS

Once solved, interrogation access is restored.

💬 Interrogation System

After the security stage, the detective can question suspects.

The suspects include:

Raven
Zephyr
Luca
Marinette
Adrien

The player can use the interrogation system to compare suspect statements against the physical evidence collected during the investigation.

One of the important questions concerns the suspects' whereabouts at approximately:

11:50 PM

The player should compare each alibi with the evidence found in the facility.

🤖 Zephyr's AI

Zephyr is controlled by the MoleAI system.

The AI is designed to behave as an adversarial hidden mole.

Instead of always sabotaging the player, Zephyr makes independent 50/50 decisions.

This means Zephyr can sometimes help the detective and sometimes interfere with the investigation.

This makes the game less predictable and gives different playthroughs different investigation conditions.

🎲 50/50 Help/Sabotage System

The AI can make several independent decisions.

Storage
50% → HELP
50% → SABOTAGE
Cafeteria
50% → HELP
50% → SABOTAGE
Security
50% → HELP
50% → SABOTAGE

These are independent decisions.

For example, one playthrough could be:

Storage      → HELP
Cafeteria    → SABOTAGE
Security     → HELP

Another playthrough could be:

Storage      → SABOTAGE
Cafeteria    → HELP
Security     → SABOTAGE

The underlying mystery remains the same, but the difficulty and route can change.

⚠️ Streamlit and AI Decisions

The AI decisions are designed specifically to work correctly with Streamlit.

Streamlit reruns the application after many user interactions.

The game therefore does NOT make a new random decision every time the interface refreshes.

Instead, the process is:

PLAYER ACTION
     ↓
GAMESTATE
     ↓
MOLE AI MAKES DECISION
     ↓
DECISION IS STORED
     ↓
STREAMLIT RERUNS
     ↓
UI DISPLAYS STORED RESULT

Therefore:

A Streamlit rerun does not create a new AI decision.

A new 50/50 decision only occurs when the player performs a new game action that actually requires one.

This prevents outcomes from changing unexpectedly when the page reruns.

🕵️ Zephyr's Truth/Lie System

Zephyr is also capable of lying during interrogations.

Whenever Zephyr is questioned, the AI makes another independent 50/50 decision:

50% → TRUTH
50% → LIE

If Zephyr tells the truth, the player receives his true alibi.

If Zephyr lies, the player receives a different false answer.

The player must therefore determine whether Zephyr's statement is consistent with the evidence.

The important point is that the lie is not simply a hidden variable.

The actual answer displayed to the player changes depending on the AI decision.

🧠 Evidence-Based Deduction

The game is designed around deduction rather than simply guessing the mole.

The player should combine information from:

Laboratory
    +
Storage
    +
Cafeteria
    +
PIN
    +
Security challenge
    +
Interrogations
    +
Suspect alibis
    +
Contradictions

The evidence board helps the detective keep track of information discovered during the investigation.

📋 Evidence Board

evidence.py contains the EvidenceBoard class.

The evidence board stores information collected during the game.

It can contain:

Physical clues

Examples:

Laboratory evidence
Storage evidence
Cafeteria evidence
PIN clues
Suspect statements

The board records information from interrogations, including:

suspect
question
answer
truth/lie information
Detective notes

The player can also record notes to help organize their deductions.

PIN progress

The evidence system also tracks whether the required PIN has been discovered/cracked.

The evidence board is intended to support the investigation without automatically revealing the answer.

⏳ Action System

The game uses an action budget to create strategic pressure.

The detective has:

12 actions

available.

Actions can include:

Investigating rooms
Attempting the PIN
Questioning suspects
Other investigation actions

The game tracks:

actions_used
actions_remaining

The player therefore needs to decide which actions are most useful.

There is intentionally no real-time countdown timer.

The pressure comes from the limited number of actions rather than real-world time.

👁️ Suspicion System

The game also maintains a suspicion score.

The starting suspicion level is:

10

Suspicion can change throughout the investigation.

For example:

Suspicious sabotage can increase suspicion.
Contradictory statements can increase suspicion.
Evidence supporting a suspect's innocence can reduce suspicion.
Certain interrogation outcomes can change suspicion.

The suspicion score is limited to:

0–100

Suspicion provides feedback about the investigation but does not automatically reveal the mole.

⚖️ Final Accusation

Once the detective believes they have enough evidence, they can make a final accusation.

The player selects:

The suspect they believe is the mole.
Supporting evidence.
Their reasoning/closing statement.

The accusation is then submitted.

The player should ideally be able to explain why the evidence points toward their chosen suspect.

🏆 Win Condition

The correct mole is:

Zephyr

The player wins if they accuse Zephyr.

The game records:

result = "win"

and displays the successful case outcome.

💀 Lose Condition

The player loses if they accuse someone other than Zephyr.

For example:

Accuse Raven → LOSS
Accuse Luca → LOSS
Accuse Marinette → LOSS
Accuse Adrien → LOSS
Accuse Zephyr → WIN

The purpose of the investigation is therefore to gather enough evidence to confidently identify Zephyr.

🏅 Performance Grading

The game also evaluates how efficiently the detective solved the case.

The performance system uses the number of actions taken.

A successful investigation can receive different grades depending on efficiency.

Example grading:

Grade	Description
S	Exceptional / near-optimal investigation
A	Excellent investigation
B	Good investigation
C	Correct but inefficient
F	Case not solved correctly

The reference solution is contained in:

optimal_path.py
🧪 Solvability Testing

The project includes a development-time solvability check.

The purpose is to ensure that the AI's sabotage mechanics do not accidentally make the mystery impossible.

The game intentionally allows sabotage to make clues harder while retaining enough information to solve the case.

Run:

python optimal_path.py

to perform the solvability check.

The test verifies that the case remains solvable even when sabotaged clue versions are used.

📁 Project Structure
zom_mole_hunter/
│
├── app.py
├── ai_agent.py
├── case.py
├── evidence.py
├── game.py
├── optimal_path.py
├── sounds.py
├── requirements.txt
└── README.md
📄 File Descriptions
app.py

The main Streamlit application.

It is responsible for the user interface, including:

Start screen
Case briefing
Room investigation
Clue display
PIN interface
Wordle security challenge
Interrogations
Evidence board
Accusation screen
Results
Performance information
Streamlit session state

This is the file used to launch the game.

game.py

The main game engine.

It contains the GameState class and controls the rules of the game.

Responsibilities include:

Action tracking
Suspicion tracking
Room investigation
AI decisions
Evidence collection
PIN attempts
Security challenge
Interrogations
Suspect statements
Accusation handling
Win/lose conditions
Game statistics

The UI calls the game engine instead of implementing the core game rules itself.

ai_agent.py

Contains the MoleAI class.

Responsibilities include:

50/50 Help/Sabotage decisions
Storage sabotage
Cafeteria sabotage
Security sabotage
Truth/Lie decisions
AI decision logging
AI statistics

The AI uses independent random decisions for each relevant game event.

case.py

Contains the case's static data.

This includes:

Story
Background
Characters
Suspect profiles
Rooms
Timeline
Questions
Suspect answers
Laboratory clues
Storage clues
Sabotaged Storage clues
Cafeteria clues
Sabotaged Cafeteria clues
PIN information

Keeping case content separate from game logic makes the mystery easier to modify.

evidence.py

Contains the EvidenceBoard class.

It handles evidence collected by the detective.

This keeps evidence management separate from the main game engine.

optimal_path.py

Contains:

Reference solution
Hint system
Performance scoring
Solvability verification

It can also be run directly as a development/testing script.

sounds.py

Contains optional sound-effect functionality.

The project can generate simple sounds for events such as:

Typewriter effects
Suspicion changes
Alerts
Success
Victory

The sound system is designed to fail gracefully if audio dependencies are unavailable.

requirements.txt

Contains the Python packages required to run the project.

The main dependencies include:

streamlit
numpy
scipy

The project also uses Python's standard library.

🛠️ Technology Stack

The project uses:

Python

Main programming language.

Streamlit

Used to build the interactive web application.

NumPy

Used by the audio utilities.

SciPy

Used for WAV/audio generation.

Python Standard Library

The project also uses standard modules such as:

random
time
html
io
🚀 Installation
1. Download the project

Download or clone the project repository.

Open a terminal inside the project folder.

cd zom_mole_hunter
2. Create a Virtual Environment
Windows
python -m venv venv

Activate it:

venv\Scripts\activate
macOS/Linux
python3 -m venv venv

Activate it:

source venv/bin/activate
3. Install Dependencies

Run:

pip install -r requirements.txt

If necessary:

python -m pip install -r requirements.txt
▶️ Running the Game

Start the Streamlit application:

streamlit run app.py

Streamlit will provide a local address.

Open the address in your browser.

🧪 Running the Solvability Test

To test the case:

python optimal_path.py

This verifies that the investigation remains solvable even with sabotaged clues.

🔄 Resetting the Game

The application supports starting a fresh investigation.

A reset creates a new game state and clears:

Visited rooms
Collected evidence
PIN progress
Wordle attempts
Interrogation results
Suspicion changes
Action count
AI decisions
Accusation state

A new investigation therefore starts independently from the previous one.

🧩 Customizing the Game

The project is modular, so different parts of the game can be modified independently.

Change the story

Edit:

case.py

Modify the case introduction and background information.

Change suspects

Edit the character definitions and suspect profiles in:

case.py

You can change:

Names
Roles
Locations
Alibis
Personality
Interrogation answers
Change rooms

Modify the room definitions in:

case.py

and the corresponding game logic in:

game.py
Change the PIN

Modify the relevant case variables in:

case.py

The PIN can be redesigned around different clue combinations.

Change the Wordle challenge

The security challenge can be modified in:

game.py

You can change:

Answer
Number of attempts
Word length
Feedback behavior

There is deliberately no time limit.

Change AI behavior

Modify:

ai_agent.py

This is the main location for changing the mole's decision-making behavior.

For example, the 50/50 probability could later be changed to something such as:

70% HELP
30% SABOTAGE

or:

30% HELP
70% SABOTAGE

if a different difficulty level is desired.

🏗️ Architecture

The project separates the user interface, game logic, AI, evidence, case content, and utilities.

                  ┌─────────────────┐
                  │     app.py      │
                  │  Streamlit UI   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     game.py     │
                  │    GameState    │
                  │   Rules/State   │
                  └───────┬─┬───────┘
                          │ │
              ┌───────────┘ └───────────┐
              ▼                         ▼
       ┌──────────────┐          ┌──────────────┐
       │  ai_agent.py │          │ evidence.py  │
       │    MoleAI    │          │ EvidenceBoard│
       └──────┬───────┘          └──────────────┘
              │
              ▼
       ┌──────────────┐
       │   case.py    │
       │  Case Data   │
       └──────────────┘

       ┌─────────────────┐
       │ optimal_path.py │
       │ Testing / Hints │
       └─────────────────┘

       ┌─────────────────┐
       │    sounds.py    │
       │  Audio Utility  │
       └─────────────────┘
🔁 Game State Architecture

The central GameState object stores the current state of the investigation.

It keeps track of information such as:

Actions
Suspicion
Visited rooms
Collected evidence
Room decisions
PIN attempts
PIN status
Security challenge status
Wordle attempts
Interrogation results
Accusation
Game result

This state is stored in Streamlit's session state so that it survives normal application reruns.

🎲 Replayability

The 50/50 AI system creates different possible investigation paths.

For example:

Playthrough 1
Storage → HELP
Cafeteria → HELP
Security → HELP
Zephyr → TRUTH
Playthrough 2
Storage → SABOTAGE
Cafeteria → HELP
Security → SABOTAGE
Zephyr → LIE
Playthrough 3
Storage → SABOTAGE
Cafeteria → SABOTAGE
Security → HELP
Zephyr → LIE

The player therefore cannot assume that every investigation will play out identically.

🎭 Design Philosophy

The game is built around three main principles.

1. The mole should interfere

Zephyr should make the detective's job harder.

However, sabotage should not automatically end the investigation.

2. The player should solve the mystery

The game provides clues rather than simply announcing the answer.

The detective is expected to:

Observe
Compare
Question
Remember
Deduce
3. Randomness should affect difficulty, not solvability

The AI's 50/50 decisions create replayability.

However, the essential evidence remains available.

The goal is:

Different route
      ≠
Impossible case
🧠 Example Playthrough

A possible investigation might look like:

START
  ↓
Investigate Laboratory
  ↓
Investigate Storage
  ↓
AI chooses HELP
  ↓
Solve normal Storage riddle
  ↓
Investigate Cafeteria
  ↓
AI chooses SABOTAGE
  ↓
Inspect tampered receipt
  ↓
Discover ??19
  ↓
Combine evidence
  ↓
PIN = 4619
  ↓
Enter PIN
  ↓
AI chooses SABOTAGE
  ↓
WORDLE
  ↓
Solve VENTS
  ↓
Interrogations
  ↓
Question Raven
  ↓
Question Luca
  ↓
Question Zephyr
  ↓
AI chooses LIE
  ↓
Compare Zephyr's answer with evidence
  ↓
Build accusation
  ↓
Accuse Zephyr
  ↓
CASE CLOSED

Another playthrough may skip the Wordle challenge entirely if Zephyr chooses to help after the PIN is cracked.

📌 Important Game Rules
Zephyr is the mole.
Storage has an independent 50/50 Help/Sabotage decision.
Cafeteria has an independent 50/50 Help/Sabotage decision.
After the PIN is cracked, security has another independent 50/50 decision.
If security is sabotaged, the player must solve the Wordle challenge.
The Wordle challenge has six attempts.
There is no timer.
Zephyr has an independent 50/50 Truth/Lie decision during interrogation.
Streamlit reruns do not create new AI decisions.
The player has a limited action budget.
The final accusation determines whether the case is solved.
The evidence is designed to keep the case solvable even when sabotage occurs.
📜 Project Summary

Zom-Mole Hunter is a modular interactive detective game combining:

Detective investigation
Evidence collection
Puzzle solving
Riddles
PIN cracking
Wordle-style security
Suspect interrogation
Truth/Lie mechanics
Adversarial AI
Randomized gameplay
Action management
Suspicion tracking
Final deduction
Performance evaluation
Optional audio

The project demonstrates how a stateful interactive game can be built using Python and Streamlit while keeping the UI, game rules, case data, evidence management, and AI behavior separated into different modules.

🔍 Quick Start

Once Python is installed:

cd zom_mole_hunter
pip install -r requirements.txt
streamlit run app.py

For the solvability test:

python optimal_path.py

Then open the Streamlit application and begin the investigation.

🧟 CASE FILE: ACTIVE

Someone inside the facility is sabotaging the investigation.

The clues are incomplete.

The suspects are lying.

The security system has been compromised.

And one of them is the mole.

Can you identify Zephyr before you run out of actions?

Good luck, detective.

not in readme bro.. in code remove timer for wordle

OH 😭 yes, I misunderstood you. You mean remove the Wordle timer from the actual code, not the README.

Please upload the current project/code (ideally the whole project ZIP, or at least game.py and app.py) so I can remove all timer-related Wordle logic cleanly without accidentally breaking the rest of your game.

I’ll make it:

WORDLE
↓
6 attempts
↓
No countdown
↓
No time remaining
↓
No timeout
↓
Solve VENTS → continue

And I’ll remove the timer from both the backend/game logic and the Streamlit UI, not just hide it.

Pasted text(2).txt
Document


import time
import case

from ai_agent import MoleAI
from evidence import EvidenceBoard


# ============================================================
# GAME CONSTANTS
# ============================================================

ROOMS = [
    "Laboratory",
    "Storage",
    "Cafeteria"
]

TOTAL_BUDGET = 12

WORDLE_ANSWER = "VENTS"
WORDLE_MAX_ATTEMPTS = 6
WORDLE_TIME_LIMIT = 45


# ============================================================
# GAME STATE
# ============================================================

class GameState:

    def __init__(self, seed=None):

        # ----------------------------------------------------
        # AI
        # ----------------------------------------------------

        self.mole_ai = MoleAI(seed)

        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        self.evidence = EvidenceBoard()

        # ----------------------------------------------------
        # ACTION / GAME STATE
        # ----------------------------------------------------

        self.actions_used = 0

        self.suspicion = 10

        self.visited_rooms = {}

        self.room_decisions = {}

        self.asked = {}

        self.log = []

        self.game_over = False

        self.result = None

        self.accused = None

        # ----------------------------------------------------
        # CONTRADICTIONS
        # ----------------------------------------------------

        self.contradiction_flagged = False

        self.last_contradiction = None

        # ----------------------------------------------------
        # CAFETERIA PIN
        # ----------------------------------------------------

        self.pin_cracked = False

        self.pin_attempts = 0

        # ----------------------------------------------------
        # SECURITY CHALLENGE
        # ----------------------------------------------------

        self.security_challenge_active = False

        self.security_challenge_complete = False

        self.wordle_answer = WORDLE_ANSWER

        self.wordle_attempts = []

        self.wordle_max_attempts = WORDLE_MAX_ATTEMPTS

        self.wordle_time_limit = WORDLE_TIME_LIMIT

        self.wordle_started_at = None

        self.wordle_failed = False


    # ========================================================
    # ACTIONS
    # ========================================================

    @property
    def actions_remaining(self):

        return TOTAL_BUDGET - self.actions_used


    def can_act(self):

        return (
            not self.game_over
            and self.actions_remaining > 0
        )


    def _log(self, text):

        self.log.append(text)


    def _clamp_suspicion(self):

        self.suspicion = max(
            0,
            min(
                100,
                self.suspicion
            )
        )


    # ========================================================
    # ROOM INVESTIGATION
    # ========================================================

    def visit_room(self, room):

        if not self.can_act():

            return (
                False,
                "No actions remaining."
            )

        if room in self.visited_rooms:

            return (
                False,
                f"You've already investigated the {room}."
            )

        if room not in ROOMS:

            return (
                False,
                "Unknown room."
            )


        # ====================================================
        # LABORATORY
        # ====================================================

        if room == "Laboratory":

            clue = case.get_lab_clue()

            self.evidence.add_clue(
                "lab_acrostic"
            )

            self.room_decisions[room] = "neutral"


        # ====================================================
        # STORAGE
        # ====================================================

        elif room == "Storage":

            # ------------------------------------------------
            # ZEPHYR MAKES ONE INDEPENDENT 50/50 DECISION.
            # ------------------------------------------------

            decision = self.mole_ai.decide_room_action(
                self.suspicion,
                self.actions_remaining
            )

            if decision == "sabotage":

                clue = case.get_storage_clue("sabotage")

                self.room_decisions[room] = "sabotage"

                self._log(
                    "⚠️ Zephyr sabotaged the Storage clue. "
                    "The harder riddle was left behind."
                )

                self.suspicion += 3

            else:

                clue = case.get_storage_clue("help")

                self.room_decisions[room] = "help"

                self._log(
                    "📦 Zephyr helped. The normal Storage riddle "
                    "was left intact."
                )

            self.evidence.add_clue("storage_riddle")


        # ====================================================
        # CAFETERIA
        # ====================================================

        else:

            # ------------------------------------------------
            # ZEPHYR MAKES ANOTHER INDEPENDENT 50/50 DECISION.
            # ------------------------------------------------

            decision = self.mole_ai.decide_cafeteria_action(
                self.suspicion,
                self.actions_remaining
            )

            clue = case.get_cafeteria_clue(decision)
            self.room_decisions[room] = decision

            if decision == "sabotage":
                self._log(
                    "⚠️ Zephyr sabotaged the Cafeteria receipt, "
                    "but the useful PIN fragment survived."
                )
                self.suspicion += 3
            else:
                self._log(
                    "🥤 Zephyr helped. The Cafeteria receipt "
                    "was left intact."
                )

            self.evidence.add_clue("cafeteria_pin")


        # ----------------------------------------------------
        # CLAMP SUSPICION
        # ----------------------------------------------------

        self._clamp_suspicion()


        # ----------------------------------------------------
        # SAVE INVESTIGATION
        # ----------------------------------------------------

        self.visited_rooms[room] = clue

        self.actions_used += 1

        self._log(
            f"🔎 Investigated the {room}."
        )

        return (
            True,
            clue
        )


    # ========================================================
    # PIN
    # ========================================================

    def attempt_pin(self, guess):

        if self.pin_cracked:

            return True

        if not self.can_act():

            return False

        # ----------------------------------------------------
        # EVERY ATTEMPT COSTS ONE ACTION
        # ----------------------------------------------------

        self.actions_used += 1

        self.pin_attempts += 1

        digits = "".join(
            character
            for character in str(guess)
            if character.isdigit()
        )

        correct = (
            digits == case.CORRECT_PIN
        )


        # ====================================================
        # CORRECT PIN
        # ====================================================

        if correct:

            self.pin_cracked = True

            self.evidence.set_pin_cracked()

            self._log(
                "🔓 PIN CRACKED. "
                "Restricted employee access unlocked."
            )


            # ------------------------------------------------
            # ZEPHYR GETS A CHANCE TO SABOTAGE INTERROGATION
            # ------------------------------------------------

            activate_challenge = (
                self.mole_ai.decide_extra_challenge(
                    self.suspicion,
                    self.actions_remaining
                )
            )


            if activate_challenge:

                self.security_challenge_active = True

                self.security_challenge_complete = False

                self.wordle_started_at = time.time()

                self._log(
                    "🚨 SECONDARY SECURITY LOCK ACTIVATED."
                )

            else:

                self.security_challenge_active = False

                self.security_challenge_complete = True

                self._log(
                    "🔓 INTERROGATION SYSTEM UNLOCKED."
                )

            return True


        # ====================================================
        # INCORRECT PIN
        # ====================================================

        self._log(
            f"🔐 Incorrect PIN attempt "
            f"#{self.pin_attempts}."
        )

        return False


    # ========================================================
    # WORDLE / SECURITY CHALLENGE
    # ========================================================

    def submit_wordle(self, guess):

        # ----------------------------------------------------
        # CHALLENGE ACTIVE?
        # ----------------------------------------------------

        if not self.security_challenge_active:

            if self.security_challenge_complete:

                return (
                    True,
                    "ALREADY_COMPLETE"
                )

            return (
                False,
                "No security challenge is active."
            )


        # ----------------------------------------------------
        # TIME CHECK
        # ----------------------------------------------------

        elapsed = (
            time.time()
            - self.wordle_started_at
        )

        if elapsed >= self.wordle_time_limit:

            self.security_challenge_active = False

            self.wordle_failed = True

            self._log(
                "⏰ SECURITY CHALLENGE FAILED: "
                "Time expired."
            )

            return (
                False,
                "TIME_EXPIRED"
            )


        # ----------------------------------------------------
        # NORMALIZE GUESS
        # ----------------------------------------------------

        guess = str(guess).strip().upper()


        # ----------------------------------------------------
        # LENGTH CHECK
        # ----------------------------------------------------

        if len(guess) != 5:

            return (
                False,
                "Enter a 5-letter word."
            )


        # ----------------------------------------------------
        # LETTER CHECK
        # ----------------------------------------------------

        if not guess.isalpha():

            return (
                False,
                "Letters only."
            )


        # ----------------------------------------------------
        # ATTEMPT LIMIT
        # ----------------------------------------------------

        if (
            len(self.wordle_attempts)
            >= self.wordle_max_attempts
        ):

            self.security_challenge_active = False

            self.wordle_failed = True

            self._log(
                "🔐 SECURITY CHALLENGE FAILED: "
                "Maximum attempts reached."
            )

            return (
                False,
                "ATTEMPTS_EXHAUSTED"
            )


        # ----------------------------------------------------
        # SAVE ATTEMPT
        # ----------------------------------------------------

        self.wordle_attempts.append(
            guess
        )


        answer = self.wordle_answer

        result = []


        # ----------------------------------------------------
        # WORDLE RESULT
        # ----------------------------------------------------

        for index, letter in enumerate(guess):

            if letter == answer[index]:

                result.append("🟩")

            elif letter in answer:

                result.append("🟨")

            else:

                result.append("⬛")


        # ====================================================
        # CORRECT
        # ====================================================

        if guess == answer:

            self.security_challenge_complete = True

            self.security_challenge_active = False

            self._log(
                "🔓 SECONDARY SECURITY LOCK DEFEATED."
            )

            return (
                True,
                {
                    "status": "CORRECT",
                    "result": result,
                    "attempts_remaining": (
                        self.wordle_max_attempts
                        - len(self.wordle_attempts)
                    )
                }
            )


        # ====================================================
        # OUT OF ATTEMPTS
        # ====================================================

        if (
            len(self.wordle_attempts)
            >= self.wordle_max_attempts
        ):

            self.security_challenge_active = False

            self.wordle_failed = True

            self._log(
                "🔐 SECURITY CHALLENGE FAILED."
            )

            return (
                False,
                {
                    "status": "FAILED",
                    "result": result,
                    "attempts_remaining": 0
                }
            )


        # ====================================================
        # INCORRECT BUT CONTINUE
        # ====================================================

        return (
            True,
            {
                "status": "CONTINUE",
                "result": result,
                "attempts_remaining": (
                    self.wordle_max_attempts
                    - len(self.wordle_attempts)
                )
            }
        )


    # ========================================================
    # TIME REMAINING FOR WORDLE
    # ========================================================

    def get_wordle_time_remaining(self):

        if not self.security_challenge_active:

            return 0

        if self.wordle_started_at is None:

            return self.wordle_time_limit

        elapsed = (
            time.time()
            - self.wordle_started_at
        )

        remaining = (
            self.wordle_time_limit
            - elapsed
        )

        return max(
            0,
            int(remaining)
        )


    # ========================================================
    # INTERROGATION
    # ========================================================

    def ask_question(
        self,
        character,
        question_key
    ):

        # ----------------------------------------------------
        # PIN LOCK
        # ----------------------------------------------------

        if not self.pin_cracked:

            return (
                False,
                "🔒 The interrogation system is locked. "
                "Crack the Cafeteria PIN first."
            )


        # ----------------------------------------------------
        # SECURITY CHALLENGE LOCK
        # ----------------------------------------------------

        if self.security_challenge_active:

            return (
                False,
                "🔐 Interrogation is locked. "
                "Complete the secondary security challenge."
            )


        # ----------------------------------------------------
        # FAILED SECURITY CHALLENGE
        # ----------------------------------------------------

        if self.wordle_failed:

            return (
                False,
                "🔐 Interrogation access was blocked "
                "by the security system."
            )


        # ----------------------------------------------------
        # ACTION CHECK
        # ----------------------------------------------------

        if not self.can_act():

            return (
                False,
                "No actions remaining."
            )


        # ----------------------------------------------------
        # ONE QUESTION PER SUSPECT
        # ----------------------------------------------------

        if character in self.asked:

            return (
                False,
                f"You've already questioned {character}."
            )


        # ----------------------------------------------------
        # VALID CHARACTER
        # ----------------------------------------------------

        if character not in case.CHARACTERS:

            return (
                False,
                "Unknown character."
            )


        # ----------------------------------------------------
        # VALID QUESTION
        # ----------------------------------------------------

        if question_key not in case.QUESTION_BANK:

            return (
                False,
                "Unknown question."
            )


        # ====================================================
        # MOLE AI DECIDES TRUTH / LIE
        # ====================================================

        if character == case.MOLE:

            tell_truth = self.mole_ai.decide_truth_or_lie(
                self.suspicion
            )

            answer_data = case.get_question(
                character,
                question_key
            )

            if tell_truth:
                answer = answer_data.get(
                    "truth_answer",
                    answer_data["answer"]
                )
                lied = False
            else:
                answer = answer_data.get(
                    "lie_answer",
                    answer_data["answer"]
                )
                lied = True

        else:

            answer_data = case.get_question(
                character,
                question_key
            )

            answer = answer_data["answer"]

            lied = False


        # ----------------------------------------------------
        # SAVE STATEMENT
        # ----------------------------------------------------

        self.asked[character] = {

            "question": question_key,

            "answer": answer,

            "lied": lied
        }


        # ----------------------------------------------------
        # SAVE TO EVIDENCE BOARD
        # ----------------------------------------------------

        self.evidence.log_answer(
            character,
            question_key,
            answer,

            # EvidenceBoard stores whether statement
            # is true.
            not lied
        )


        # ====================================================
        # SUSPICION
        # ====================================================

        if character == case.MOLE:

            if lied:

                self.suspicion += 8

                self._log(
                    "⚠️ Zephyr's answer feels rehearsed."
                )

            else:

                self.suspicion -= 2

                self._log(
                    "🔎 Zephyr gave a surprisingly "
                    "straightforward answer."
                )

        else:

            self.suspicion -= 1


        self._clamp_suspicion()


        # ----------------------------------------------------
        # CONSUME ACTION
        # ----------------------------------------------------

        self.actions_used += 1


        # ----------------------------------------------------
        # LOG
        # ----------------------------------------------------

        self._log(
            f"💬 Questioned {character}."
        )


        # ====================================================
        # CONTRADICTION DETECTION
        # ====================================================

        try:

            new_contradictions = (
                self.evidence.detect_contradictions()
            )

        except AttributeError:

            new_contradictions = []


        for contradiction in new_contradictions:

            self.contradiction_flagged = True

            self.last_contradiction = (
                contradiction["detail"]
            )

            self._log(
                f"🚨 {contradiction['detail']}"
            )


        return (
            True,
            answer
        )


    # ========================================================
    # FINAL ACCUSATION
    # ========================================================

    def make_accusation(
        self,
        character
    ):

        if self.game_over:

            return (
                False,
                "The case is already closed."
            )


        if character not in case.CHARACTERS:

            return (
                False,
                "Unknown character."
            )


        self.accused = character

        self.actions_used = TOTAL_BUDGET

        self.game_over = True


        if character == case.MOLE:

            self.result = "win"

        else:

            self.result = "lose"


        self._log(
            f"⚖️ Final accusation: "
            f"{character}."
        )


        return (
            True,
            self.result
        )


    # ========================================================
    # STATS
    # ========================================================

    def get_stats(self):

        return {

            "actions_used":
                self.actions_used,

            "actions_remaining":
                self.actions_remaining,

            "suspicion":
                self.suspicion,

            "result":
                self.result,

            "accused":
                self.accused,

            "contradiction_flagged":
                self.contradiction_flagged,

            "guilt_scores":
                getattr(
                    self.evidence,
                    "guilt_scores",
                    {}
                ),

            "last_contradiction":
                self.last_contradiction,

            "pin_cracked":
                self.pin_cracked,

            "pin_attempts":
                self.pin_attempts,

            "security_challenge_active":
                self.security_challenge_active,

            "security_challenge_complete":
                self.security_challenge_complete,

            "wordle_attempts":
                self.wordle_attempts,

            "wordle_time_remaining":
                self.get_wordle_time_remaining(),

            "wordle_failed":
                self.wordle_failed,

            "mole_ai":
                self.mole_ai.stats()
        }


YES. In this file, you can remove all timer functionality. You don't need time at all.

Make these exact changes:

1. Remove:

import time

2. Remove:

WORDLE_TIME_LIMIT = 45

3. In __init__, remove:

self.wordle_time_limit = WORDLE_TIME_LIMIT

self.wordle_started_at = None

4. In attempt_pin(), remove:

self.wordle_started_at = time.time()

5. Replace your entire submit_wordle() function with this:

# ========================================================
# WORDLE / SECURITY CHALLENGE
# ========================================================

def submit_wordle(self, guess):

    # ----------------------------------------------------
    # CHALLENGE ACTIVE?
    # ----------------------------------------------------

    if not self.security_challenge_active:

        if self.security_challenge_complete:

            return (
                True,
                "ALREADY_COMPLETE"
            )

        return (
            False,
            "No security challenge is active."
        )


    # ----------------------------------------------------
    # NORMALIZE GUESS
    # ----------------------------------------------------

    guess = str(guess).strip().upper()


    # ----------------------------------------------------
    # LENGTH CHECK
    # ----------------------------------------------------

    if len(guess) != 5:

        return (
            False,
            "Enter a 5-letter word."
        )


    # ----------------------------------------------------
    # LETTER CHECK
    # ----------------------------------------------------

    if not guess.isalpha():

        return (
            False,
            "Letters only."
        )


    # ----------------------------------------------------
    # ATTEMPT LIMIT
    # ----------------------------------------------------

    if (
        len(self.wordle_attempts)
        >= self.wordle_max_attempts
    ):

        self.security_challenge_active = False

        self.wordle_failed = True

        self._log(
            "🔐 SECURITY CHALLENGE FAILED: "
            "Maximum attempts reached."
        )

        return (
            False,
            "ATTEMPTS_EXHAUSTED"
        )


    # ----------------------------------------------------
    # SAVE ATTEMPT
    # ----------------------------------------------------

    self.wordle_attempts.append(
        guess
    )


    answer = self.wordle_answer

    result = []


    # ----------------------------------------------------
    # WORDLE RESULT
    # ----------------------------------------------------

    for index, letter in enumerate(guess):

        if letter == answer[index]:

            result.append("🟩")

        elif letter in answer:

            result.append("🟨")

        else:

            result.append("⬛")


    # ====================================================
    # CORRECT
    # ====================================================

    if guess == answer:

        self.security_challenge_complete = True

        self.security_challenge_active = False

        self._log(
            "🔓 SECONDARY SECURITY LOCK DEFEATED."
        )

        return (
            True,
            {
                "status": "CORRECT",
                "result": result,
                "attempts_remaining": (
                    self.wordle_max_attempts
                    - len(self.wordle_attempts)
                )
            }
        )


    # ====================================================
    # OUT OF ATTEMPTS
    # ====================================================

    if (
        len(self.wordle_attempts)
        >= self.wordle_max_attempts
    ):

        self.security_challenge_active = False

        self.wordle_failed = True

        self._log(
            "🔐 SECURITY CHALLENGE FAILED."
        )

        return (
            False,
            {
                "status": "FAILED",
                "result": result,
                "attempts_remaining": 0
            }
        )


    # ====================================================
    # INCORRECT BUT CONTINUE
    # ====================================================

    return (
        True,
        {
            "status": "CONTINUE",
            "result": result,
            "attempts_remaining": (
                self.wordle_max_attempts
                - len(self.wordle_attempts)
            )
        }
    )

6. Delete this entire function:

def get_wordle_time_remaining(self):
    ...

7. In get_stats(), remove:

"wordle_time_remaining":
    self.get_wordle_time_remaining(),

That's it for game.py.

Your Wordle now works purely as:

WORDLE
  ↓
Enter 5-letter guess
  ↓
🟩 🟨 ⬛ feedback
  ↓
Maximum 6 attempts
  ↓
VENTS = success
  ↓
6 wrong guesses = failure

No timer, no time import, no timestamps, no timeout.

One important thing: if your app.py currently displays "Time Remaining", "45 seconds", a countdown, or uses get_wordle_time_remaining(), that needs to be removed there too. Send me your app.py and I'll point out the exact lines to delete/change.

give full pls

YESS 😭 Here is the FULL game.py, with the timer completely removed. You can copy-paste this whole thing directly over your current file.

import case

from ai_agent import MoleAI
from evidence import EvidenceBoard


# ============================================================
# GAME CONSTANTS
# ============================================================

ROOMS = [
    "Laboratory",
    "Storage",
    "Cafeteria"
]

TOTAL_BUDGET = 12

WORDLE_ANSWER = "VENTS"
WORDLE_MAX_ATTEMPTS = 6


# ============================================================
# GAME STATE
# ============================================================

class GameState:

    def __init__(self, seed=None):

        # ----------------------------------------------------
        # AI
        # ----------------------------------------------------

        self.mole_ai = MoleAI(seed)

        # ----------------------------------------------------
        # EVIDENCE
        # ----------------------------------------------------

        self.evidence = EvidenceBoard()

        # ----------------------------------------------------
        # ACTION / GAME STATE
        # ----------------------------------------------------

        self.actions_used = 0

        self.suspicion = 10

        self.visited_rooms = {}

        self.room_decisions = {}

        self.asked = {}

        self.log = []

        self.game_over = False

        self.result = None

        self.accused = None

        # ----------------------------------------------------
        # CONTRADICTIONS
        # ----------------------------------------------------

        self.contradiction_flagged = False

        self.last_contradiction = None

        # ----------------------------------------------------
        # CAFETERIA PIN
        # ----------------------------------------------------

        self.pin_cracked = False

        self.pin_attempts = 0

        # ----------------------------------------------------
        # SECURITY CHALLENGE
        # ----------------------------------------------------

        self.security_challenge_active = False

        self.security_challenge_complete = False

        self.wordle_answer = WORDLE_ANSWER

        self.wordle_attempts = []

        self.wordle_max_attempts = WORDLE_MAX_ATTEMPTS

        self.wordle_failed = False


    # ========================================================
    # ACTIONS
    # ========================================================

    @property
    def actions_remaining(self):

        return TOTAL_BUDGET - self.actions_used


    def can_act(self):

        return (
            not self.game_over
            and self.actions_remaining > 0
        )


    def _log(self, text):

        self.log.append(text)


    def _clamp_suspicion(self):

        self.suspicion = max(
            0,
            min(
                100,
                self.suspicion
            )
        )


    # ========================================================
    # ROOM INVESTIGATION
    # ========================================================

    def visit_room(self, room):

        if not self.can_act():

            return (
                False,
                "No actions remaining."
            )

        if room in self.visited_rooms:

            return (
                False,
                f"You've already investigated the {room}."
            )

        if room not in ROOMS:

            return (
                False,
                "Unknown room."
            )


        # ====================================================
        # LABORATORY
        # ====================================================

        if room == "Laboratory":

            clue = case.get_lab_clue()

            self.evidence.add_clue(
                "lab_acrostic"
            )

            self.room_decisions[room] = "neutral"


        # ====================================================
        # STORAGE
        # ====================================================

        elif room == "Storage":

            # ------------------------------------------------
            # ZEPHYR MAKES ONE INDEPENDENT 50/50 DECISION.
            # ------------------------------------------------

            decision = self.mole_ai.decide_room_action(
                self.suspicion,
                self.actions_remaining
            )

            if decision == "sabotage":

                clue = case.get_storage_clue("sabotage")

                self.room_decisions[room] = "sabotage"

                self._log(
                    "⚠️ Zephyr sabotaged the Storage clue. "
                    "The harder riddle was left behind."
                )

                self.suspicion += 3

            else:

                clue = case.get_storage_clue("help")

                self.room_decisions[room] = "help"

                self._log(
                    "📦 Zephyr helped. The normal Storage riddle "
                    "was left intact."
                )

            self.evidence.add_clue(
                "storage_riddle"
            )


        # ====================================================
        # CAFETERIA
        # ====================================================

        else:

            # ------------------------------------------------
            # ZEPHYR MAKES ANOTHER INDEPENDENT 50/50 DECISION.
            # ------------------------------------------------

            decision = self.mole_ai.decide_cafeteria_action(
                self.suspicion,
                self.actions_remaining
            )

            clue = case.get_cafeteria_clue(
                decision
            )

            self.room_decisions[room] = decision

            if decision == "sabotage":

                self._log(
                    "⚠️ Zephyr sabotaged the Cafeteria receipt, "
                    "but the useful PIN fragment survived."
                )

                self.suspicion += 3

            else:

                self._log(
                    "🥤 Zephyr helped. The Cafeteria receipt "
                    "was left intact."
                )

            self.evidence.add_clue(
                "cafeteria_pin"
            )


        # ----------------------------------------------------
        # CLAMP SUSPICION
        # ----------------------------------------------------

        self._clamp_suspicion()


        # ----------------------------------------------------
        # SAVE INVESTIGATION
        # ----------------------------------------------------

        self.visited_rooms[room] = clue

        self.actions_used += 1

        self._log(
            f"🔎 Investigated the {room}."
        )

        return (
            True,
            clue
        )


    # ========================================================
    # PIN
    # ========================================================

    def attempt_pin(self, guess):

        if self.pin_cracked:

            return True

        if not self.can_act():

            return False

        # ----------------------------------------------------
        # EVERY ATTEMPT COSTS ONE ACTION
        # ----------------------------------------------------

        self.actions_used += 1

        self.pin_attempts += 1

        digits = "".join(
            character
            for character in str(guess)
            if character.isdigit()
        )

        correct = (
            digits == case.CORRECT_PIN
        )


        # ====================================================
        # CORRECT PIN
        # ====================================================

        if correct:

            self.pin_cracked = True

            self.evidence.set_pin_cracked()

            self._log(
                "🔓 PIN CRACKED. "
                "Restricted employee access unlocked."
            )


            # ------------------------------------------------
            # ZEPHYR GETS A CHANCE TO SABOTAGE INTERROGATION
            # ------------------------------------------------

            activate_challenge = (
                self.mole_ai.decide_extra_challenge(
                    self.suspicion,
                    self.actions_remaining
                )
            )


            if activate_challenge:

                self.security_challenge_active = True

                self.security_challenge_complete = False

                self._log(
                    "🚨 SECONDARY SECURITY LOCK ACTIVATED."
                )

            else:

                self.security_challenge_active = False

                self.security_challenge_complete = True

                self._log(
                    "🔓 INTERROGATION SYSTEM UNLOCKED."
                )

            return True


        # ====================================================
        # INCORRECT PIN
        # ====================================================

        self._log(
            f"🔐 Incorrect PIN attempt "
            f"#{self.pin_attempts}."
        )

        return False


    # ========================================================
    # WORDLE / SECURITY CHALLENGE
    # ========================================================

    def submit_wordle(self, guess):

        # ----------------------------------------------------
        # CHALLENGE ACTIVE?
        # ----------------------------------------------------

        if not self.security_challenge_active:

            if self.security_challenge_complete:

                return (
                    True,
                    "ALREADY_COMPLETE"
                )

            return (
                False,
                "No security challenge is active."
            )


        # ----------------------------------------------------
        # NORMALIZE GUESS
        # ----------------------------------------------------

        guess = str(guess).strip().upper()


        # ----------------------------------------------------
        # LENGTH CHECK
        # ----------------------------------------------------

        if len(guess) != 5:

            return (
                False,
                "Enter a 5-letter word."
            )


        # ----------------------------------------------------
        # LETTER CHECK
        # ----------------------------------------------------

        if not guess.isalpha():

            return (
                False,
                "Letters only."
            )


        # ----------------------------------------------------
        # ATTEMPT LIMIT
        # ----------------------------------------------------

        if (
            len(self.wordle_attempts)
            >= self.wordle_max_attempts
        ):

            self.security_challenge_active = False

            self.wordle_failed = True

            self._log(
                "🔐 SECURITY CHALLENGE FAILED: "
                "Maximum attempts reached."
            )

            return (
                False,
                "ATTEMPTS_EXHAUSTED"
            )


        # ----------------------------------------------------
        # SAVE ATTEMPT
        # ----------------------------------------------------

        self.wordle_attempts.append(
            guess
        )


        answer = self.wordle_answer

        result = []


        # ----------------------------------------------------
        # WORDLE RESULT
        # ----------------------------------------------------

        for index, letter in enumerate(guess):

            if letter == answer[index]:

                result.append("🟩")

            elif letter in answer:

                result.append("🟨")

            else:

                result.append("⬛")


        # ====================================================
        # CORRECT
        # ====================================================

        if guess == answer:

            self.security_challenge_complete = True

            self.security_challenge_active = False

            self._log(
                "🔓 SECONDARY SECURITY LOCK DEFEATED."
            )

            return (
                True,
                {
                    "status": "CORRECT",

                    "result": result,

                    "attempts_remaining": (
                        self.wordle_max_attempts
                        - len(self.wordle_attempts)
                    )
                }
            )


        # ====================================================
        # OUT OF ATTEMPTS
        # ====================================================

        if (
            len(self.wordle_attempts)
            >= self.wordle_max_attempts
        ):

            self.security_challenge_active = False

            self.wordle_failed = True

            self._log(
                "🔐 SECURITY CHALLENGE FAILED."
            )

            return (
                False,
                {
                    "status": "FAILED",

                    "result": result,

                    "attempts_remaining": 0
                }
            )


        # ====================================================
        # INCORRECT BUT CONTINUE
        # ====================================================

        return (
            True,
            {
                "status": "CONTINUE",

                "result": result,

                "attempts_remaining": (
                    self.wordle_max_attempts
                    - len(self.wordle_attempts)
                )
            }
        )


    # ========================================================
    # INTERROGATION
    # ========================================================

    def ask_question(
        self,
        character,
        question_key
    ):

        # ----------------------------------------------------
        # PIN LOCK
        # ----------------------------------------------------

        if not self.pin_cracked:

            return (
                False,
                "🔒 The interrogation system is locked. "
                "Crack the Cafeteria PIN first."
            )


        # ----------------------------------------------------
        # SECURITY CHALLENGE LOCK
        # ----------------------------------------------------

        if self.security_challenge_active:

            return (
                False,
                "🔐 Interrogation is locked. "
                "Complete the secondary security challenge."
            )


        # ----------------------------------------------------
        # FAILED SECURITY CHALLENGE
        # ----------------------------------------------------

        if self.wordle_failed:

            return (
                False,
                "🔐 Interrogation access was blocked "
                "by the security system."
            )


        # ----------------------------------------------------
        # ACTION CHECK
        # ----------------------------------------------------

        if not self.can_act():

            return (
                False,
                "No actions remaining."
            )


        # ----------------------------------------------------
        # ONE QUESTION PER SUSPECT
        # ----------------------------------------------------

        if character in self.asked:

            return (
                False,
                f"You've already questioned {character}."
            )


        # ----------------------------------------------------
        # VALID CHARACTER
        # ----------------------------------------------------

        if character not in case.CHARACTERS:

            return (
                False,
                "Unknown character."
            )


        # ----------------------------------------------------
        # VALID QUESTION
        # ----------------------------------------------------

        if question_key not in case.QUESTION_BANK:

            return (
                False,
                "Unknown question."
            )


        # ====================================================
        # MOLE AI DECIDES TRUTH / LIE
        # ====================================================

        if character == case.MOLE:

            tell_truth = (
                self.mole_ai.decide_truth_or_lie(
                    self.suspicion
                )
            )

            answer_data = case.get_question(
                character,
                question_key
            )

            if tell_truth:

                answer = answer_data.get(
                    "truth_answer",
                    answer_data["answer"]
                )

                lied = False

            else:

                answer = answer_data.get(
                    "lie_answer",
                    answer_data["answer"]
                )

                lied = True

        else:

            answer_data = case.get_question(
                character,
                question_key
            )

            answer = answer_data["answer"]

            lied = False


        # ----------------------------------------------------
        # SAVE STATEMENT
        # ----------------------------------------------------

        self.asked[character] = {

            "question": question_key,

            "answer": answer,

            "lied": lied
        }


        # ----------------------------------------------------
        # SAVE TO EVIDENCE BOARD
        # ----------------------------------------------------

        self.evidence.log_answer(
            character,
            question_key,
            answer,

            # EvidenceBoard stores whether statement
            # is true.
            not lied
        )


        # ====================================================
        # SUSPICION
        # ====================================================

        if character == case.MOLE:

            if lied:

                self.suspicion += 8

                self._log(
                    "⚠️ Zephyr's answer feels rehearsed."
                )

            else:

                self.suspicion -= 2

                self._log(
                    "🔎 Zephyr gave a surprisingly "
                    "straightforward answer."
                )

        else:

            self.suspicion -= 1


        self._clamp_suspicion()


        # ----------------------------------------------------
        # CONSUME ACTION
        # ----------------------------------------------------

        self.actions_used += 1


        # ----------------------------------------------------
        # LOG
        # ----------------------------------------------------

        self._log(
            f"💬 Questioned {character}."
        )


        # ====================================================
        # CONTRADICTION DETECTION
        # ====================================================

        try:

            new_contradictions = (
                self.evidence.detect_contradictions()
            )

        except AttributeError:

            new_contradictions = []


        for contradiction in new_contradictions:

            self.contradiction_flagged = True

            self.last_contradiction = (
                contradiction["detail"]
            )

            self._log(
                f"🚨 {contradiction['detail']}"
            )


        return (
            True,
            answer
        )


    # ========================================================
    # FINAL ACCUSATION
    # ========================================================

    def make_accusation(
        self,
        character
    ):

        if self.game_over:

            return (
                False,
                "The case is already closed."
            )


        if character not in case.CHARACTERS:

            return (
                False,
                "Unknown character."
            )


        self.accused = character

        self.actions_used = TOTAL_BUDGET

        self.game_over = True


        if character == case.MOLE:

            self.result = "win"

        else:

            self.result = "lose"


        self._log(
            f"⚖️ Final accusation: "
            f"{character}."
        )


        return (
            True,
            self.result
        )


    # ========================================================
    # STATS
    # ========================================================

    def get_stats(self):

        return {

            "actions_used":
                self.actions_used,

            "actions_remaining":
                self.actions_remaining,

            "suspicion":
                self.suspicion,

            "result":
                self.result,

            "accused":
                self.accused,

            "contradiction_flagged":
                self.contradiction_flagged,

            "guilt_scores":
                getattr(
                    self.evidence,
                    "guilt_scores",
                    {}
                ),

            "last_contradiction":
                self.last_contradiction,

            "pin_cracked":
                self.pin_cracked,

            "pin_attempts":
                self.pin_attempts,

            "security_challenge_active":
                self.security_challenge_active,

            "security_challenge_complete":
                self.security_challenge_complete,

            "wordle_attempts":
                self.wordle_attempts,

            "wordle_failed":
                self.wordle_failed,

            "mole_ai":
                self.mole_ai.stats()
        }
What changed

I removed every Wordle timer component:

❌ import time
❌ WORDLE_TIME_LIMIT = 45
❌ wordle_time_limit
❌ wordle_started_at
❌ time.time()
❌ elapsed-time calculation
❌ TIME_EXPIRED
❌ get_wordle_time_remaining()
❌ wordle_time_remaining from stats

Everything else in your game.py stays the same. Wordle is now 6 attempts only.




import html
import streamlit as st
import case

from game import GameState, TOTAL_BUDGET, ROOMS

============================================================
PAGE CONFIG
============================================================

st.set_page_config(
page_title="Zom-Mole Hunter",
page_icon="🧟",
layout="wide",
initial_sidebar_state="expanded",
)

============================================================
NOIR AESTHETIC
============================================================

st.markdown(
"""
<style>

.stApp {
    background:
        linear-gradient(
            135deg,
            #1a0f2e 0%,
            #2d1b4e 50%,
            #1f1135 100%
        );
    color: #e0d5d5;
}

body {
    font-family: Georgia, serif;
}

h1 {
    color: #d4af37;
    font-family: monospace;
    font-size: 2.5rem;
    text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
    letter-spacing: 3px;
}

h2,
h3 {
    color: #f39c12;
    font-family: monospace;
    text-shadow: 0 0 8px rgba(243, 156, 18, 0.4);
}

/* ========================================================
   TABS
   ======================================================== */

.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
}

.stTabs [data-baseweb="tab"] {
    background-color: #3d2860;
    border-radius: 8px 8px 0 0;
    padding: 10px 18px;
    color: #c9a961;
    font-family: monospace;
    border: 1px solid #5a3d8a;
}

.stTabs [aria-selected="true"] {
    background-color: #5a3d8a !important;
    color: #d4af37 !important;
    border: 1px solid #d4af37;
}

/* ========================================================
   EXPANDERS
   ======================================================== */

div[data-testid="stExpander"] {
    border: 1px solid #5a3d8a;
    border-radius: 10px;
    background-color: #2d1f42;
}

/* ========================================================
   METRICS
   ======================================================== */

div[data-testid="stMetricValue"] {
    color: #f39c12;
    font-size: 1.8rem;
    font-family: monospace;
}

/* ========================================================
   BUTTONS
   ======================================================== */

.stButton > button {
    background-color: #5a3d8a;
    color: #d4af37;
    border-radius: 8px;
    border: 1.5px solid #d4af37;
    font-family: monospace;
    font-weight: bold;
    box-shadow: 0 0 8px rgba(212, 175, 55, 0.3);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #d4af37;
    color: #1a0f2e;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.8);
}

/* ========================================================
   CASE FILE
   ======================================================== */

.case-file {
    background: rgba(45, 31, 66, 0.85);
    border: 1px solid #5a3d8a;
    border-left: 4px solid #d4af37;
    border-radius: 8px;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 5px 25px rgba(0, 0, 0, 0.35);
}

/* ========================================================
   BACKGROUND
   ======================================================== */

.background-section {
    background: #2d1f42;
    border: 1px solid #5a3d8a;
    border-radius: 8px;
    padding: 16px;
    margin: 12px 0;
    font-family: monospace;
}

.background-title {
    color: #d4af37;
    font-weight: bold;
    margin-bottom: 12px;
    font-size: 1rem;
    letter-spacing: 1px;
}

.background-entry {
    color: #c9a961;
    padding: 8px 0;
    border-bottom: 1px dotted #5a3d8a;
    line-height: 1.5;
}

/* ========================================================
   START SCREEN
   ======================================================== */

.game-title-main {
    color: #d4af37;
    font-family: monospace;
    font-size: 3.2rem;
    font-weight: bold;
    letter-spacing: 6px;
    text-align: center;
    text-shadow:
        0 0 10px rgba(212, 175, 55, 0.5),
        0 0 25px rgba(212, 175, 55, 0.2);
    padding-top: 35px;
}

.game-title-sub {
    color: #c9a961;
    font-family: monospace;
    font-size: 1rem;
    letter-spacing: 3px;
    text-align: center;
    margin-top: 8px;
    margin-bottom: 25px;
}

.opening-story {
    background: rgba(26, 16, 36, 0.92);
    border: 1px solid #5a3d8a;
    border-left: 4px solid #d4af37;
    border-radius: 8px;
    padding: 30px;
    margin: 20px 0;
    line-height: 1.8;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
}

.opening-label {
    color: #d4af37;
    font-family: monospace;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 15px;
}

.opening-warning {
    color: #f39c12;
    font-family: monospace;
    font-weight: bold;
    border-top: 1px solid #5a3d8a;
    border-bottom: 1px solid #5a3d8a;
    padding: 15px 0;
    margin: 18px 0;
    text-align: center;
    letter-spacing: 1px;
}

/* ========================================================
   UNLOCKED ACCESS
   ======================================================== */

.unlock-box {
    background: #21152d;
    border: 2px solid #d4af37;
    border-radius: 8px;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.15);
}

.unlock-title {
    color: #d4af37;
    font-family: monospace;
    font-weight: bold;
    font-size: 1.1rem;
    letter-spacing: 1px;
}

/* ========================================================
   LOCKED INTERROGATION
   ======================================================== */

.locked-box {
    background: #21152d;
    border: 1px solid #705d7d;
    border-left: 4px solid #725b7b;
    border-radius: 8px;
    padding: 25px;
    margin: 20px 0;
    text-align: center;
}

.locked-title {
    color: #c9a961;
    font-family: monospace;
    font-weight: bold;
    font-size: 1.2rem;
    letter-spacing: 1px;
}

/* ========================================================
   SECURITY CHALLENGE
   ======================================================== */

.security-box {
    background: #21152d;
    border: 2px solid #d4af37;
    border-left: 5px solid #f39c12;
    border-radius: 8px;
    padding: 28px;
    margin: 20px 0;
    text-align: center;
    box-shadow:
        0 0 20px rgba(212, 175, 55, 0.12),
        0 5px 25px rgba(0, 0, 0, 0.35);
}

.security-title {
    color: #d4af37;
    font-family: monospace;
    font-size: 1.35rem;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.security-warning {
    color: #f39c12;
    font-family: monospace;
    font-weight: bold;
    letter-spacing: 1px;
    margin: 12px 0;
}

.security-word {
    color: #d4af37;
    font-family: monospace;
    font-size: 1.8rem;
    font-weight: bold;
    letter-spacing: 7px;
    margin: 20px 0;
}

.security-attempt {
    color: #c9a961;
    font-family: monospace;
    font-size: 0.9rem;
    margin-top: 10px;
}

/* ========================================================
   LAB NOTE
   ======================================================== */

.note-card {
    background: #f4ecd8;
    color: #3a3226;
    font-family: Georgia, serif;
    padding: 25px;
    border-radius: 2px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
    transform: rotate(-1deg);
    margin: 14px 4px;
    line-height: 1.9;
    font-size: 1.05rem;
}

.note-line {
    margin: 7px 0;
}

/* ========================================================
   STORAGE RIDDLE
   ======================================================== */

.riddle-board {
    background-color: #10151f;
    background-image:
        linear-gradient(
            #1c2434 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            #1c2434 1px,
            transparent 1px
        );
    background-size: 22px 22px;
    color: #e5e7eb;
    font-family: Georgia, serif;
    font-size: 1.1rem;
    padding: 24px;
    border-radius: 8px;
    border: 2px solid #334155;
    line-height: 1.8;
    margin: 14px 4px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
}

.riddle-line {
    margin: 5px 0;
}

.riddle-question {
    color: #f1f5f9;
    font-style: italic;
    margin-top: 14px;
}

/* ========================================================
   RECEIPT
   ======================================================== */

.receipt {
    background: #fdfdfd;
    color: #111;
    font-family: "Courier New", monospace;
    padding: 20px;
    border: 1px dashed #777;
    max-width: 340px;
    margin: 14px auto;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
}

.receipt-title {
    text-align: center;
    font-weight: bold;
    margin-bottom: 12px;
    border-bottom: 1px dashed #777;
    padding-bottom: 8px;
}

.pin-display {
    margin-top: 12px;
    font-size: 1.2rem;
    font-weight: bold;
}

.pin-digit {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 30px;
    height: 34px;
    margin: 0 3px;
    border-bottom: 2px solid #333;
    font-weight: bold;
    font-size: 1.2rem;
}

.pin-redacted {
    color: #999;
}

/* ========================================================
   STATEMENTS
   ======================================================== */

.statement-card {
    background: #241936;
    border-left: 4px solid #d4af37;
    border-radius: 6px;
    padding: 16px;
    margin: 12px 0;
}

.statement-character {
    color: #d4af37;
    font-family: monospace;
    font-weight: bold;
    font-size: 1rem;
}

.statement-question {
    color: #9d8ca8;
    font-size: 0.85rem;
    margin-top: 8px;
}

.statement-answer {
    color: #f0e7d8;
    font-family: Georgia, serif;
    font-size: 1.15rem;
    line-height: 1.5;
    margin-top: 8px;
}

/* ========================================================
   SUSPECT
   ======================================================== */

.suspect-card {
    background: #3d2860;
    border-left: 4px solid #f39c12;
    padding: 15px;
    margin: 8px 0;
    border-radius: 4px;
}

/* ========================================================
   QUOTE
   ======================================================== */

.quote-box {
    background: #1a1024;
    border-left: 3px solid #d4af37;
    padding: 18px;
    margin: 12px 0;
    font-family: Georgia, serif;
    font-size: 1.2rem;
    line-height: 1.5;
    color: #f0e7d8;
}

/* ========================================================
   LOG
   ======================================================== */

.log-entry {
    font-family: monospace;
    font-size: 0.85rem;
    color: #c9a961;
    padding: 5px 0;
    border-bottom: 1px dotted #5a3d8a;
}

/* ========================================================
   CLUE CHIP
   ======================================================== */

.clue-chip {
    display: inline-block;
    padding: 7px 12px;
    margin: 4px;
    border: 1px solid #725b7b;
    color: #d8c9dc;
    background: #201825;
    font-size: 0.75rem;
    border-radius: 4px;
}

/* ========================================================
   FINAL REPORT
   ======================================================== */

.verdict-box {
    background: #21152d;
    border: 2px solid #d4af37;
    border-radius: 8px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.2);
}

</style>
""",
unsafe_allow_html=True,

)

============================================================
SESSION STATE
============================================================

if "game" not in st.session_state:
st.session_state.game = GameState()

if "detective_name" not in st.session_state:
st.session_state.detective_name = ""

if "case_started" not in st.session_state:
st.session_state.case_started = False

if "final_evidence_saved" not in st.session_state:
st.session_state.final_evidence_saved = []

if "final_reasoning_saved" not in st.session_state:
st.session_state.final_reasoning_saved = ""

game = st.session_state.game

============================================================
HELPER FUNCTIONS
============================================================

def safe_html(value):
return html.escape(str(value))

def get_profile(character):

profiles = getattr(case, "PROFILES", {})

if isinstance(profiles, dict):
    return profiles.get(character, {})

return {}

def get_question_text(question_key):

questions = getattr(case, "QUESTION_BANK", {})

if isinstance(questions, dict):
    return questions.get(
        question_key,
        question_key
    )

return str(question_key)

def get_statement_data(character):

statements = getattr(
    game.evidence,
    "suspect_statements",
    {}
)

if not isinstance(statements, dict):
    return {}

value = statements.get(
    character,
    {}
)

if isinstance(value, dict):
    return value

return {}

def statement_count():

total = 0

statements = getattr(
    game.evidence,
    "suspect_statements",
    {}
)

if not isinstance(statements, dict):
    return 0

for value in statements.values():

    if isinstance(value, dict):
        total += len(value)

    elif value:
        total += 1

return total
============================================================
LAB RENDERER
============================================================

def render_lab_note(lines):

html_output = '<div class="note-card">'

for item in lines:

    if isinstance(item, str):

        text = item

    elif (
        isinstance(item, (list, tuple))
        and len(item) >= 2
    ):

        text = f"{item[0]}{item[1]}"

    elif isinstance(item, dict):

        text = item.get(
            "text",
            item.get("content", "")
        )

        if item.get("letter"):
            text = (
                f'{item["letter"]}'
                f'{text}'
            )

    else:

        text = str(item)

    html_output += (
        '<div class="note-line">'
        f'{safe_html(text)}'
        '</div>'
    )

html_output += "</div>"

st.html(html_output)
============================================================
STORAGE RIDDLE
============================================================

def render_storage_riddle(riddle):

html_output = '<div class="riddle-board">'

for index, line in enumerate(riddle):

    if index == len(riddle) - 1:

        html_output += (
            '<div class="riddle-question">'
            f'{safe_html(line)}'
            '</div>'
        )

    else:

        html_output += (
            '<div class="riddle-line">'
            f'{safe_html(line)}'
            '</div>'
        )

html_output += "</div>"

st.html(html_output)
============================================================
CAFETERIA RECEIPT
============================================================

def render_receipt(
job,
pin_digits,
redacted
):

if isinstance(
    pin_digits,
    (list, tuple)
):

    digits = list(pin_digits)

else:

    digits = list(
        str(pin_digits)
    )


if isinstance(
    redacted,
    str
):

    redacted_values = [
        char in ("?", "x", "X", "*")
        for char in redacted
    ]

elif isinstance(
    redacted,
    (list, tuple)
):

    redacted_values = list(
        redacted
    )

else:

    redacted_values = []


html_output = (
    '<div class="receipt">'
)

html_output += (
    '<div class="receipt-title">'
    'RESTOCKING LOG — MACHINE #3'
    '</div>'
)

html_output += (
    '<div>'
    'Restocked by: '
    f'<b>{safe_html(job)}</b>'
    '</div>'
)

html_output += (
    '<div class="pin-display">'
    'Employee PIN: '
)


for index, digit in enumerate(
    digits
):

    is_redacted = (
        index < len(redacted_values)
        and bool(
            redacted_values[index]
        )
    )

    if is_redacted:

        html_output += (
            '<span class="pin-digit '
            'pin-redacted">'
            '?'
            '</span>'
        )

    else:

        html_output += (
            '<span class="pin-digit">'
            f'{safe_html(digit)}'
            '</span>'
        )


html_output += "</div>"
html_output += "</div>"

st.html(html_output)
============================================================
GENERIC CLUE RENDERER
============================================================

def render_clue(
room,
clue
):

if not isinstance(clue, dict):

    st.write(clue)

    return


# ========================================================
# LABORATORY
# ========================================================

if room == "Laboratory":

    if clue.get("title"):

        st.markdown(
            f"### "
            f"{safe_html(clue['title'])}"
        )

    if clue.get("lines"):

        render_lab_note(
            clue["lines"]
        )

    if clue.get("note"):

        st.info(
            clue["note"]
        )

    if clue.get("description"):

        st.write(
            clue["description"]
        )


# ========================================================
# STORAGE
# ========================================================

elif room == "Storage":

    if clue.get("title"):

        st.markdown(
            f"### "
            f"{safe_html(clue['title'])}"
        )

    # ----------------------------------------------------
    # SABOTAGE WARNING
    # ----------------------------------------------------

    if "CORRUPTED" in str(
        clue.get("title", "")
    ).upper():

        st.warning(
            "⚠️ The Storage terminal has been "
            "tampered with. The original riddle "
            "appears to have been replaced."
        )

    if clue.get("riddle"):

        render_storage_riddle(
            clue["riddle"]
        )

    if clue.get("note"):

        st.info(
            clue["note"]
        )

    if clue.get("description"):

        st.write(
            clue["description"]
        )


# ========================================================
# CAFETERIA
# ========================================================

elif room == "Cafeteria":

    if clue.get("title"):

        st.markdown(
            f"### "
            f"{safe_html(clue['title'])}"
        )

    if all(
        key in clue
        for key in (
            "job",
            "pin_digits",
            "redacted"
        )
    ):

        render_receipt(
            clue["job"],
            clue["pin_digits"],
            clue["redacted"]
        )

    if clue.get("note"):

        st.info(
            clue["note"]
        )

    if clue.get("description"):

        st.write(
            clue["description"]
        )
============================================================
RESET CASE
============================================================

def reset_case():

st.session_state.game = GameState()

st.session_state.detective_name = ""

st.session_state.case_started = False

st.session_state.final_evidence_saved = []

st.session_state.final_reasoning_saved = ""

keys_to_remove = [
    "final_reasoning",
    "final_suspect",
    "final_evidence",
    "pin_guess",
    "start_detective_name",
    "wordle_guess",
]

for key in keys_to_remove:

    if key in st.session_state:

        del st.session_state[key]
============================================================
OPENING SCREEN
============================================================

if not st.session_state.case_started:

st.html(
    """
    <div class="game-title-main">
        🧟 ZOM-MOLE HUNTER
    </div>

    <div class="game-title-sub">
        A NOIR DETECTIVE INVESTIGATION
    </div>
    """
)


st.html(
    """
    <div class="opening-story">

        <div class="opening-label">
            📁 CASE FILE
        </div>

        <div class="opening-label">
            CLASSIFIED — NIGHT SHIFT INVESTIGATION
        </div>

        <h2>
            THE NIGHT SHIFT INCIDENT
        </h2>

        <p>
            <b>12:18 AM.</b>
        </p>

        <p>
            The research facility should have been asleep.
        </p>

        <p>
            Instead, emergency lights are flashing,
            a laboratory alarm is screaming through the
            corridors, and six experimental filter
            cartridges have disappeared from Storage.
        </p>

        <p>
            At first, security believed it was an
            equipment failure.
        </p>

        <p>
            Then they found the broken vial.
        </p>

        <p>
            Then the ventilation panel.
        </p>

        <p>
            Then someone noticed that three minutes of
            corridor camera footage had vanished.
        </p>

        <div class="opening-warning">
            FIVE PEOPLE WERE STILL INSIDE THE FACILITY.
        </div>

        <p>
            One of them is lying.
        </p>

        <p>
            Possibly more than one.
        </p>

        <p>
            But finding a liar is not enough.
            You need to determine which lie actually
            connects to the missing materials.
        </p>

        <p>
            You have <b>12 actions</b> before the
            investigation window closes.
        </p>

        <p>
            Search the rooms. Examine the evidence.
            Crack the restricted access PIN.
            Interrogate the employees.
            Then decide who is the Mole.
        </p>

    </div>
    """
)


st.write("")


st.html(
    """
    <div
        style="
            color:#d4af37;
            font-family:monospace;
            font-weight:bold;
            font-size:1.15rem;
            letter-spacing:2px;
            margin-top:25px;
            margin-bottom:12px;
        "
    >
        🕵️ IDENTIFY YOURSELF
    </div>
    """
)


detective_name = st.text_input(
    "Enter your detective name",
    placeholder="e.g. Detective Morgan",
    key="start_detective_name",
)


st.write("")


if st.button(
    "🔎 ENTER THE CASE",
    use_container_width=True,
):

    if not detective_name.strip():

        st.warning(
            "Enter your detective name before beginning."
        )

    else:

        st.session_state.detective_name = (
            detective_name.strip()
        )

        st.session_state.case_started = True

        st.rerun()


st.stop()
============================================================
GAME TITLE
============================================================

st.title(
"🧟 ZOM-MOLE HUNTER"
)

st.caption(
f"Detective Case File: "
f"{st.session_state.detective_name} | "
f"{game.actions_remaining} Actions Remaining"
)

============================================================
SIDEBAR
============================================================

with st.sidebar:

st.header(
    "CASE DOSSIER"
)

st.write(
    f"**Detective:** "
    f"{st.session_state.detective_name}"
)

st.divider()

st.subheader(
    "Actions Remaining"
)

st.metric(
    "",
    game.actions_remaining
)

progress = (
    game.actions_used / TOTAL_BUDGET
    if TOTAL_BUDGET > 0
    else 0
)

progress = max(
    0.0,
    min(1.0, progress)
)

st.progress(
    progress
)

st.caption(
    f"{game.actions_used} of "
    f"{TOTAL_BUDGET} actions used"
)

st.divider()

st.subheader(
    "Investigation"
)

st.write(
    f"🏚️ Scenes searched: "
    f"**{len(game.visited_rooms)}/{len(ROOMS)}**"
)

st.write(
    f"🗣️ Statements collected: "
    f"**{statement_count()}**"
)

st.write(
    f"🔎 Physical clues: "
    f"**{len(game.evidence.clues_found)}**"
)


# ========================================================
# SECURITY STATUS
# ========================================================

if not game.pin_cracked:

    st.warning(
        "🔒 Interrogations locked"
    )

elif game.security_challenge_active:

    st.error(
        "🔐 Security challenge active"
    )

elif game.wordle_failed:

    st.error(
        "🔐 Interrogation access blocked"
    )

else:

    st.success(
        "🔓 Interrogations unlocked"
    )


st.divider()


# ========================================================
# CASE LOG
# ========================================================

with st.expander(
    "📋 CASE LOG"
):

    if game.log:

        for entry in reversed(
            game.log[-10:]
        ):

            st.html(
                '<div class="log-entry">'
                f'• {safe_html(entry)}'
                '</div>'
            )

    else:

        st.write(
            "*No entries yet.*"
        )


st.divider()


if st.button(
    "🔄 START NEW CASE",
    use_container_width=True
):

    reset_case()

    st.rerun()
============================================================
CASE INTRO
============================================================

st.markdown(
'<div class="case-file">',
unsafe_allow_html=True
)

case_intro = getattr(
case,
"CASE_INTRO",
"A mysterious incident has occurred."
)

st.markdown(
case_intro
)

st.markdown(
"</div>",
unsafe_allow_html=True
)

============================================================
END OF GAME
============================================================

if game.game_over:

st.divider()

if game.result == "win":

    st.html(
        """
        <div class="verdict-box">

            <h1>CASE SOLVED</h1>

            <h2>
                THE MOLE HAS BEEN IDENTIFIED
            </h2>

            <p>
                Your accusation was correct.
                The evidence led you to the right suspect.
            </p>

        </div>
        """
    )

else:

    st.html(
        """
        <div class="verdict-box">

            <h1>CASE FAILED</h1>

            <h2>
                THE MOLE GOT AWAY
            </h2>

            <p>
                Your accusation did not identify the Mole.
            </p>

        </div>
        """
    )

    st.warning(
        f"The real Mole was **{case.MOLE}**."
    )


st.divider()

st.subheader(
    "INVESTIGATION REPORT"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Actions Used",
        f"{game.actions_used}/{TOTAL_BUDGET}"
    )

with col2:

    st.metric(
        "Scenes Searched",
        len(game.visited_rooms)
    )

with col3:

    st.metric(
        "Statements",
        statement_count()
    )


st.divider()

st.subheader(
    "Your Accusation"
)

st.write(
    f"**Suspect:** {game.accused}"
)


if game.result == "win":

    st.success(
        "Correct accusation."
    )

else:

    st.error(
        "Incorrect accusation."
    )


if st.session_state.final_evidence_saved:

    st.divider()

    st.subheader(
        "Evidence You Selected"
    )

    for evidence in (
        st.session_state.final_evidence_saved
    ):

        st.html(
            '<span class="clue-chip">'
            f'✓ {safe_html(evidence)}'
            '</span>'
        )


if st.session_state.final_reasoning_saved:

    st.divider()

    st.subheader(
        "Your Reasoning"
    )

    st.html(
        '<div class="quote-box">'
        f'{safe_html(st.session_state.final_reasoning_saved)}'
        '</div>'
    )


st.stop()
============================================================
MAIN GAME TABS
============================================================

(
tab_background,
tab_rooms,
tab_people,
tab_accuse,
) = st.tabs(
[
"📋 BACKGROUND",
"🏚️ CRIME SCENES",
"🗣️ INTERROGATIONS",
"⚖️ ACCUSATION",
]
)

============================================================
BACKGROUND TAB
============================================================

with tab_background:

st.subheader(
    "THE NIGHT SHIFT INCIDENT"
)

st.write(
    "These are the established facts of the case. "
    "Pay attention to times, locations and who had "
    "access to what."
)

background = getattr(
    case,
    "BACKGROUND",
    {}
)


if isinstance(
    background,
    dict
):

    for section, section_data in background.items():

        html_output = (
            '<div class="background-section">'
            '<div class="background-title">'
            f'{safe_html(section)}'
            '</div>'
        )


        if isinstance(
            section_data,
            dict
        ):

            if "entries" in section_data:

                for entry in section_data["entries"]:

                    if (
                        isinstance(
                            entry,
                            (list, tuple)
                        )
                        and len(entry) >= 2
                    ):

                        label = entry[0]
                        text = entry[1]

                        html_output += (
                            '<div class="background-entry">'
                            f'<strong>{safe_html(label)}</strong>'
                            '&nbsp; '
                            f'{safe_html(text)}'
                            '</div>'
                        )

                    else:

                        html_output += (
                            '<div class="background-entry">'
                            f'{safe_html(entry)}'
                            '</div>'
                        )


            if "notes" in section_data:

                for note_text in section_data["notes"]:

                    html_output += (
                        '<div class="background-entry">'
                        f'• {safe_html(note_text)}'
                        '</div>'
                    )


        else:

            html_output += (
                '<div class="background-entry">'
                f'{safe_html(section_data)}'
                '</div>'
            )


        html_output += "</div>"

        st.html(
            html_output
        )


else:

    st.write(
        background
    )
============================================================
CRIME SCENES
============================================================

with tab_rooms:

st.subheader(
    "🏚️ Crime Scenes"
)

st.write(
    f"You have **{game.actions_remaining} actions** remaining."
)


room_descriptions = {

    "Laboratory":
        "The centrifuge room where the incident began.",

    "Storage":
        "Shelves, the ventilation system and a strange riddle.",

    "Cafeteria":
        "A vending machine, a restocking cart "
        "and one suspicious receipt.",
}


cols = st.columns(
    len(ROOMS)
)


for col, room in zip(
    cols,
    ROOMS
):

    with col:

        st.markdown(
            f"### {room}"
        )

        st.caption(
            room_descriptions.get(
                room,
                "A location inside the facility."
            )
        )


        # =================================================
        # INVESTIGATED
        # =================================================

        if room in game.visited_rooms:

            st.success(
                "✓ Location investigated"
            )

            clue = game.visited_rooms[room]

            render_clue(
                room,
                clue
            )


            # =================================================
            # CAFETERIA PIN
            # =================================================

            if room == "Cafeteria":

                st.divider()

                st.markdown(
                    "**🔐 Crack the Employee PIN**"
                )


                if game.pin_cracked:

                    st.success(
                        "🔓 PIN CRACKED"
                    )


                    # ----------------------------------------
                    # SECURITY CHALLENGE ACTIVE
                    # ----------------------------------------

                    if game.security_challenge_active:

                        st.html(
                            """
                            <div class="security-box">

                                <div class="security-title">
                                    🔐 SECONDARY SECURITY LOCK
                                </div>

                                <div class="security-warning">
                                    ADDITIONAL VERIFICATION REQUIRED
                                </div>

                                <p>
                                    Restricted employee access has
                                    triggered a secondary security
                                    protocol.
                                </p>

                                <p>
                                    <b>
                                        Interrogation access remains locked.
                                    </b>
                                </p>

                            </div>
                            """
                        )


                    else:

                        st.html(
                            """
                            <div class="unlock-box">

                                <div class="unlock-title">
                                    🔓 RESTRICTED ACCESS GRANTED
                                </div>

                                <p>
                                    The employee record linked to
                                    the restocking log has been
                                    unlocked.
                                </p>

                                <p>
                                    <b>ACCESS RECORD:</b>
                                    The restocking cycle was initiated
                                    using an authorized employee
                                    credential.
                                </p>

                                <p>
                                    The system confirms that the
                                    credential belonged to an employee
                                    scheduled for the night shift.
                                </p>

                                <p>
                                    <b>
                                        INTERROGATION SYSTEM: ONLINE
                                    </b>
                                </p>

                            </div>
                            """
                        )


                else:

                    pin_guess = st.text_input(
                        "Enter four digits",
                        max_chars=4,
                        key="pin_guess",
                        disabled=not game.can_act(),
                    )


                    if st.button(
                        "🔓 VERIFY PIN",
                        key="verify_pin",
                        use_container_width=True,
                        disabled=not game.can_act(),
                    ):

                        pin_correct = game.attempt_pin(
                            pin_guess
                        )


                        if pin_correct:

                            st.success(
                                "🔓 PIN CRACKED. "
                                "Restricted access unlocked."
                            )

                        else:

                            st.error(
                                "❌ Incorrect PIN. "
                                "1 action used."
                            )

                        st.rerun()


                    st.caption(
                        f"Every PIN attempt costs 1 action. "
                        f"{game.actions_remaining} actions remaining."
                    )


        # =================================================
        # NOT INVESTIGATED
        # =================================================

        else:

            if st.button(
                f"🔎 Investigate {room}",
                key=f"visit_{room}",
                disabled=not game.can_act(),
                use_container_width=True,
            ):

                success, payload = (
                    game.visit_room(room)
                )

                if success:

                    st.rerun()

                else:

                    st.warning(
                        str(payload)
                    )
============================================================
INTERROGATIONS
============================================================

with tab_people:

st.subheader(
    "🗣️ Interrogation Room"
)


# ========================================================
# PIN NOT CRACKED
# ========================================================

if not game.pin_cracked:

    st.html(
        """
        <div class="locked-box">

            <div class="locked-title">
                🔒 INTERROGATION SYSTEM LOCKED
            </div>

            <p>
                Employee interrogation records are protected
                behind restricted access.
            </p>

            <p>
                You must crack the Cafeteria employee PIN
                before you can question anyone.
            </p>

            <p>
                <b>
                    Locate the Cafeteria and recover the
                    missing digits.
                </b>
            </p>

        </div>
        """
    )


# ========================================================
# ZEPHYR SECURITY SABOTAGE
# ========================================================

elif game.security_challenge_active:

    remaining_time = (
        game.get_wordle_time_remaining()
    )

    attempts_used = len(
        game.wordle_attempts
    )

    attempts_remaining = (
        game.wordle_max_attempts
        - attempts_used
    )


    st.html(
        f"""
        <div class="security-box">

            <div class="security-title">
                🔐 SECONDARY SECURITY LOCK
            </div>

            <div class="security-warning">
                INTERROGATION ACCESS DENIED
            </div>

            <p>
                The restricted employee system has detected
                an additional authentication requirement.
            </p>

            <p>
                Someone has modified the security protocol.
            </p>

            <p>
                Complete the emergency verification challenge
                to continue.
            </p>

            <div class="security-word">
                _ _ _ _ _
            </div>

            <p>
                <b>
                    FIVE-LETTER SECURITY WORD
                </b>
            </p>

        </div>
        """
    )


    # ====================================================
    # CHALLENGE STATUS
    # ====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "TIME REMAINING",
            f"{remaining_time}s"
        )

    with col2:

        st.metric(
            "ATTEMPTS REMAINING",
            attempts_remaining
        )


    # ====================================================
    # PREVIOUS ATTEMPTS
    # ====================================================

    if game.wordle_attempts:

        st.markdown(
            "### Previous Attempts"
        )

        for attempt in game.wordle_attempts:

            display = ""

            for index, letter in enumerate(
                attempt
            ):

                if (
                    index < len(
                        game.wordle_answer
                    )
                    and letter
                    == game.wordle_answer[index]
                ):

                    display += "🟩"

                elif (
                    letter
                    in game.wordle_answer
                ):

                    display += "🟨"

                else:

                    display += "⬛"

            st.write(
                f"`{attempt}`  {display}"
            )


    # ====================================================
    # WORDLE INPUT
    # ====================================================

    guess = st.text_input(
        "Enter a 5-letter word",
        max_chars=5,
        key="wordle_guess",
        placeholder="_____",
    )


    if st.button(
        "🔓 SUBMIT SECURITY WORD",
        key="submit_wordle",
        use_container_width=True,
    ):

        success, result = (
            game.submit_wordle(
                guess
            )
        )


        # -----------------------------------------------
        # CORRECT
        # -----------------------------------------------

        if (
            isinstance(result, dict)
            and result.get("status")
            == "CORRECT"
        ):

            st.success(
                "🔓 SECURITY LOCK DEFEATED."
            )

            st.balloons()

            st.rerun()


        # -----------------------------------------------
        # CONTINUE
        # -----------------------------------------------

        elif (
            isinstance(result, dict)
            and result.get("status")
            == "CONTINUE"
        ):

            st.rerun()


        # -----------------------------------------------
        # FAILED
        # -----------------------------------------------

        elif (
            isinstance(result, dict)
            and result.get("status")
            == "FAILED"
        ):

            st.error(
                "🔐 SECURITY LOCK FAILED. "
                "Interrogation access has been blocked."
            )

            st.rerun()


        # -----------------------------------------------
        # TIME EXPIRED
        # -----------------------------------------------

        elif result == "TIME_EXPIRED":

            st.error(
                "⏰ TIME EXPIRED. "
                "The security system locked you out."
            )

            st.rerun()


        else:

            st.warning(
                str(result)
            )


    st.caption(
        "The security timer is enforced by the game engine. "
        "A successful solution is required to unlock interrogation."
    )


# ========================================================
# FAILED SECURITY CHALLENGE
# ========================================================

elif game.wordle_failed:

    st.html(
        """
        <div class="locked-box">

            <div class="locked-title">
                🔐 INTERROGATION ACCESS BLOCKED
            </div>

            <p>
                The secondary security protocol could not
                be defeated.
            </p>

            <p>
                The employee interrogation system remains
                inaccessible.
            </p>

            <p>
                <b>
                    You must rely on the physical evidence,
                    timeline and case records.
                </b>
            </p>

        </div>
        """
    )


    st.divider()

    st.info(
        "The case is still solvable. "
        "The security sabotage does not remove "
        "any physical evidence."
    )


# ========================================================
# FULLY UNLOCKED
# ========================================================

else:

    st.write(
        "The interrogation system is online. "
        "Everyone has something to say. "
        "The trick is figuring out whether it matters."
    )


    question_bank = getattr(
        case,
        "QUESTION_BANK",
        {}
    )


    for character in case.CHARACTERS:

        profile = get_profile(
            character
        )


        with st.expander(
            f"🧑 {character} — "
            f"{profile.get('role', 'Unknown role')}"
        ):


            st.html(
                '<div class="suspect-card">'
                f'<strong>{safe_html(character)}</strong>'
                '<br>'
                '<span style="color:#c9a961;font-size:.8rem;">'
                f'{safe_html(profile.get("role", "Unknown role"))}'
                ' • '
                f'{safe_html(profile.get("location", "Unknown"))}'
                '</span>'
                '<br><br>'
                f'{safe_html(profile.get("description", ""))}'
                '<br><br>'
                f'<i>{safe_html(profile.get("personality", ""))}</i>'
                '</div>'
            )


            asked_data = game.asked.get(
                character
            )


            # =================================================
            # ALREADY QUESTIONED
            # =================================================

            if asked_data:

                question_key = asked_data.get(
                    "question"
                )

                answer = asked_data.get(
                    "answer",
                    ""
                )


                st.markdown(
                    "**Statement collected:**"
                )


                st.html(
                    '<div class="statement-card">'
                    '<div class="statement-question">'
                    f'Q: {safe_html(get_question_text(question_key))}'
                    '</div>'
                    '<div class="statement-answer">'
                    f'“{safe_html(answer)}”'
                    '</div>'
                    '</div>'
                )


                # ------------------------------------------------
                # Do NOT tell player whether Zephyr lied.
                # They must deduce this themselves.
                # ------------------------------------------------

                st.info(
                    "You have already questioned this person. "
                    "Study their statement against the evidence."
                )


            # =================================================
            # NOT QUESTIONED
            # =================================================

            else:

                if (
                    isinstance(
                        question_bank,
                        dict
                    )
                    and question_bank
                ):

                    question_keys = list(
                        question_bank.keys()
                    )


                    q_key = st.selectbox(
                        "Question",
                        options=question_keys,
                        format_func=get_question_text,
                        key=f"question_{character}",
                    )


                    if st.button(
                        f"💬 Ask {character}",
                        key=f"ask_{character}",
                        disabled=not game.can_act(),
                        use_container_width=True,
                    ):

                        success, answer = (
                            game.ask_question(
                                character,
                                q_key
                            )
                        )


                        if success:

                            st.rerun()

                        else:

                            st.warning(
                                str(answer)
                            )


                else:

                    st.warning(
                        "No questions are configured."
                    )
============================================================
ACCUSATION
============================================================

with tab_accuse:

st.subheader(
    "⚖️ Final Accusation"
)

st.warning(
    "Once you submit an accusation, "
    "the investigation ends."
)

st.write(
    "Don't accuse someone simply because they lied. "
    "Accuse the person whose statements and actions "
    "connect to the actual incident."
)


suspect = st.selectbox(
    "Who is the Mole?",
    case.CHARACTERS,
    key="final_suspect",
)


st.divider()


st.subheader(
    "What convinced you?"
)


evidence_options = []


clue_labels = {

    "lab_acrostic":
        "🧪 Laboratory note",

    "storage_riddle":
        "📦 Storage riddle",

    "cafeteria_pin":
        "🥤 Cafeteria restocking receipt",
}


# ========================================================
# PHYSICAL CLUES
# ========================================================

for clue in getattr(
    game.evidence,
    "clues_found",
    []
):

    label = clue_labels.get(
        clue,
        str(clue)
    )

    if label not in evidence_options:

        evidence_options.append(
            label
        )


# ========================================================
# STATEMENTS
# ========================================================

for character in case.CHARACTERS:

    statements = get_statement_data(
        character
    )


    for question_key in statements:

        label = (
            f"🗣️ {character}: "
            f"{get_question_text(question_key)}"
        )


        if label not in evidence_options:

            evidence_options.append(
                label
            )


if evidence_options:

    selected_evidence = st.multiselect(
        "Select the clues/statements "
        "that support your accusation",
        evidence_options,
        key="final_evidence",
    )

else:

    selected_evidence = []

    st.info(
        "You haven't collected any evidence yet."
    )


st.divider()


st.subheader(
    "Your Reasoning"
)


reasoning = st.text_area(
    "Build your case",
    placeholder=(
        "Explain why the evidence points to this person..."
    ),
    height=180,
    key="final_reasoning",
)


st.divider()


if st.button(
    "🔨 SUBMIT FINAL ACCUSATION",
    type="primary",
    use_container_width=True,
    disabled=not game.can_act(),
):

    if not selected_evidence:

        st.error(
            "A detective needs evidence. "
            "Select at least one piece of evidence."
        )

    elif not reasoning.strip():

        st.error(
            "Explain your reasoning before "
            "closing the case."
        )

    else:

        st.session_state.final_evidence_saved = (
            selected_evidence.copy()
        )

        st.session_state.final_reasoning_saved = (
            reasoning.strip()
        )


        success, result = (
            game.make_accusation(
                suspect
            )
        )


        if success:

            st.rerun()

        else:

            st.error(
                str(result)
            )
============================================================
OUT OF ACTIONS
============================================================

if (
game.actions_remaining == 0
and not game.game_over
):

st.error(
    "⏰ You have used all 12 actions. "
    "The facility is running out of time. "
    "Make your final accusation."
)
Close
