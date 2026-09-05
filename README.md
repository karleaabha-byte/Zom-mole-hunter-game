# Zom-Mole Hunter — 50/50 Zephyr Edition

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Zephyr's decision rules

- Storage investigation: 50% HELP / 50% SABOTAGE.
  - Help -> normal riddle.
  - Sabotage -> corrupted/harder riddle.
- Cafeteria investigation: 50% HELP / 50% SABOTAGE.
  - Help -> normal receipt.
  - Sabotage -> tampered receipt; the `??19` PIN fragment survives.
- Correct PIN: 50% HELP / 50% SABOTAGE.
  - Help -> interrogation opens immediately.
  - Sabotage -> Wordle security challenge appears.
- Zephyr interrogation: 50% TRUTH / 50% LIE.
  - The selected answer is actually different for truth vs lie.

## Streamlit reruns

The AI decision is made inside `GameState` only when a player performs an
actual game action. A normal Streamlit rerun only redraws the UI and does not
roll the 50/50 again. This prevents a single click from changing outcomes
because Streamlit reran the script.
