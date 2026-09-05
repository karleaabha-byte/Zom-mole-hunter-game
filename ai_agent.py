"""Adversarial Mole AI for Zom-Mole Hunter.

Every Zephyr decision that can affect the investigation is independently
50/50. Decisions are made only when the game engine explicitly asks for one.
Streamlit reruns do not make a second decision for the same action.
"""

import random


class MoleAI:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

        self.sabotage_count = 0
        self.help_count = 0
        self.lie_count = 0
        self.truth_count = 0
        self.security_sabotage_count = 0
        self.security_skip_count = 0
        self.decisions_log = []

    # ========================================================
    # GENERIC 50/50 DECISION
    # ========================================================

    def decide_help_or_sabotage(
        self,
        action_name,
        suspicion=None,
        actions_remaining=None,
    ):
        """Return 'help' or 'sabotage' with independent 50/50 odds."""
        decision = "sabotage" if self.rng.random() < 0.5 else "help"

        if decision == "sabotage":
            self.sabotage_count += 1
        else:
            self.help_count += 1

        self.decisions_log.append(
            f"Zephyr chose to {decision.upper()} during {action_name}."
        )

        return decision

    # ========================================================
    # ROOM INVESTIGATION
    # ========================================================

    def decide_room_action(self, suspicion=None, actions_remaining=None):
        return self.decide_help_or_sabotage(
            "room investigation",
            suspicion,
            actions_remaining,
        )

    # ========================================================
    # STORAGE RIDDLE
    # ========================================================

    def decide_riddle_sabotage(self, suspicion=None, actions_remaining=None):
        """Compatibility helper: True means give the hard riddle."""
        return (
            self.decide_help_or_sabotage(
                "Storage riddle",
                suspicion,
                actions_remaining,
            )
            == "sabotage"
        )

    # ========================================================
    # CAFETERIA CLUE
    # ========================================================

    def decide_cafeteria_action(self, suspicion=None, actions_remaining=None):
        return self.decide_help_or_sabotage(
            "Cafeteria clue",
            suspicion,
            actions_remaining,
        )

    # ========================================================
    # PIN -> WORDLE / NO WORDLE
    # ========================================================

    def decide_security_sabotage(self, suspicion=None, actions_remaining=None):
        """Return True for sabotage (Wordle), False for help (no Wordle)."""
        decision = self.decide_help_or_sabotage(
            "interrogation access",
            suspicion,
            actions_remaining,
        )

        if decision == "sabotage":
            self.security_sabotage_count += 1
            return True

        self.security_skip_count += 1
        return False

    def decide_extra_challenge(self, suspicion=None, actions_remaining=None):
        """Backward-compatible name used by the game engine."""
        return self.decide_security_sabotage(
            suspicion,
            actions_remaining,
        )

    # ========================================================
    # ZEPHYR TRUTH / LIE
    # ========================================================

    def decide_truth_or_lie(self, suspicion=None):
        """Return True for truth and False for lie with 50/50 odds."""
        tell_truth = self.rng.random() < 0.5

        if tell_truth:
            self.truth_count += 1
        else:
            self.lie_count += 1

        self.decisions_log.append(
            "Zephyr chose to "
            f"{'TELL THE TRUTH' if tell_truth else 'LIE'}."
        )

        return tell_truth

    # ========================================================
    # STATS
    # ========================================================

    def stats(self):
        return {
            "sabotage_count": self.sabotage_count,
            "help_count": self.help_count,
            "lie_count": self.lie_count,
            "truth_count": self.truth_count,
            "security_sabotage_count": self.security_sabotage_count,
            "security_skip_count": self.security_skip_count,
            "decisions_log": list(self.decisions_log),
        }
