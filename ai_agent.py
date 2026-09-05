"""
Adversarial Mole AI for Zom-Mole Hunter.

Zephyr is the MAX player.
The Detective is the MIN player.

The AI uses depth-limited Minimax to choose actions
that maximize Zephyr's chances of avoiding detection.
"""

import random
import copy


class MoleAI:

    def __init__(self, seed=None, search_depth=3):

        self.rng = random.Random(seed)

        self.search_depth = search_depth

        self.sabotage_count = 0
        self.help_count = 0

        self.lie_count = 0
        self.truth_count = 0

        self.security_sabotage_count = 0
        self.security_skip_count = 0

        self.decisions_log = []


    # =========================================================
    # EVALUATION FUNCTION
    # =========================================================

    def _evaluate(self, state):

        """
        Evaluate a state from Zephyr's perspective.

        HIGHER SCORE = BETTER FOR ZEPHYR
        LOWER SCORE  = BETTER FOR DETECTIVE
        """

        if state is None:
            return 0


        score = 0


        # -----------------------------------------------------
        # SUSPICION
        # -----------------------------------------------------

        suspicion = getattr(
            state,
            "suspicion",
            10
        )

        # High suspicion is dangerous for Zephyr.

        score -= suspicion * 2


        # -----------------------------------------------------
        # VISITED ROOMS
        # -----------------------------------------------------

        visited_rooms = getattr(
            state,
            "visited_rooms",
            {}
        )

        # More investigation = more information for detective.

        score -= len(visited_rooms) * 3


        # -----------------------------------------------------
        # QUESTIONS
        # -----------------------------------------------------

        asked = getattr(
            state,
            "asked",
            {}
        )

        # More interrogations = more information.

        score -= len(asked) * 6


        # -----------------------------------------------------
        # CONTRADICTIONS
        # -----------------------------------------------------

        if getattr(
            state,
            "contradiction_flagged",
            False
        ):

            score -= 30


        # -----------------------------------------------------
        # PIN
        # -----------------------------------------------------

        if getattr(
            state,
            "pin_cracked",
            False
        ):

            # Detective has reached interrogation.

            score -= 10


        # -----------------------------------------------------
        # SECURITY CHALLENGE
        # -----------------------------------------------------

        security_active = getattr(
            state,
            "security_challenge_active",
            False
        )

        security_complete = getattr(
            state,
            "security_challenge_complete",
            False
        )

        wordle_failed = getattr(
            state,
            "wordle_failed",
            False
        )


        if security_active:

            # HUGE advantage for Zephyr.

            score += 50


        elif wordle_failed:

            # Interrogation is permanently blocked.

            score += 70


        elif security_complete:

            # Detective defeated the security obstacle.

            score -= 20


        # -----------------------------------------------------
        # WORDLE ATTEMPTS
        # -----------------------------------------------------

        wordle_attempts = getattr(
            state,
            "wordle_attempts",
            []
        )

        if security_active:

            remaining = (
                getattr(
                    state,
                    "wordle_max_attempts",
                    6
                )
                - len(wordle_attempts)
            )

            score += remaining * 3


        # -----------------------------------------------------
        # ACTIONS
        # -----------------------------------------------------

        actions_used = getattr(
            state,
            "actions_used",
            0
        )

        score -= actions_used


        return score


    # =========================================================
    # SIMULATE ZEHPYR ACTION
    # =========================================================

    def _simulate_zephyr_action(
        self,
        game_state,
        action,
        action_type
    ):

        """
        Simulate a Zephyr action without changing
        the real GameState.
        """

        if game_state is None:
            return None


        state = copy.deepcopy(
            game_state
        )


        # =====================================================
        # STORAGE
        # =====================================================

        if action_type == "storage":

            if action == "sabotage":

                state.suspicion += 3

                state.room_decisions[
                    "Storage"
                ] = "riddle_sabotage"

            else:

                state.room_decisions[
                    "Storage"
                ] = "help"


        # =====================================================
        # SECURITY / WORDLE
        # =====================================================

        elif action_type == "security":

            if action == "sabotage":

                # Zephyr activates Wordle.

                state.security_challenge_active = True

                state.security_challenge_complete = False

                state.wordle_failed = False


            else:

                # Zephyr allows interrogation.

                state.security_challenge_active = False

                state.security_challenge_complete = True

                state.wordle_failed = False


        # =====================================================
        # STATEMENT
        # =====================================================

        elif action_type == "statement":

            if action == "lie":

                state.suspicion += 8

            else:

                state.suspicion -= 2


        # -----------------------------------------------------
        # CLAMP
        # -----------------------------------------------------

        state.suspicion = max(
            0,
            min(
                100,
                state.suspicion
            )
        )


        return state


    # =========================================================
    # SIMULATE DETECTIVE ACTION
    # =========================================================

    def _simulate_detective_action(
        self,
        state,
        action,
        action_type
    ):

        """
        Simulate a Detective response.

        Detective is MIN.
        """

        if state is None:
            return None


        new_state = copy.deepcopy(
            state
        )


        # -----------------------------------------------------
        # WORDLE
        # -----------------------------------------------------

        if action == "solve_wordle":

            new_state.actions_used += 1

            # Assume the detective can eventually defeat
            # the security challenge.

            new_state.security_challenge_active = False

            new_state.security_challenge_complete = True


        # -----------------------------------------------------
        # WAIT
        # -----------------------------------------------------

        elif action == "wait":

            new_state.actions_used += 1


        # -----------------------------------------------------
        # SUSPECT ZEPHYR
        # -----------------------------------------------------

        elif action == "suspect":

            new_state.actions_used += 1

            new_state.suspicion += 5


        # -----------------------------------------------------
        # QUESTION
        # -----------------------------------------------------

        elif action == "question":

            new_state.actions_used += 1

            new_state.suspicion -= 1


        new_state.suspicion = max(
            0,
            min(
                100,
                new_state.suspicion
            )
        )


        return new_state


    # =========================================================
    # DETECTIVE ACTIONS
    # =========================================================

    def _get_detective_actions(
        self,
        state,
        action_type
    ):

        if state is None:
            return []


        if action_type == "security":

            if getattr(
                state,
                "security_challenge_active",
                False
            ):

                return [
                    "solve_wordle",
                    "wait"
                ]

            return [
                "question",
                "suspect"
            ]


        if action_type == "storage":

            return [
                "question",
                "suspect"
            ]


        if action_type == "statement":

            return [
                "question",
                "suspect"
            ]


        return [
            "question",
            "suspect"
        ]


    # =========================================================
    # MINIMAX
    # =========================================================

    def _minimax(
        self,
        state,
        depth,
        maximizing_player,
        action_type
    ):

        """
        Minimax search.

        MAX = Zephyr
        MIN = Detective
        """

        if state is None:

            return 0


        if depth <= 0:

            return self._evaluate(
                state
            )


        # =====================================================
        # ZEHPYR = MAX
        # =====================================================

        if maximizing_player:

            actions = [
                "sabotage",
                "help"
            ]

            best_value = float(
                "-inf"
            )


            for action in actions:

                next_state = (
                    self._simulate_zephyr_action(
                        state,
                        action,
                        action_type
                    )
                )


                value = self._minimax(
                    next_state,
                    depth - 1,
                    False,
                    action_type
                )


                best_value = max(
                    best_value,
                    value
                )


            return best_value


        # =====================================================
        # DETECTIVE = MIN
        # =====================================================

        else:

            actions = (
                self._get_detective_actions(
                    state,
                    action_type
                )
            )


            if not actions:

                return self._evaluate(
                    state
                )


            best_value = float(
                "inf"
            )


            for action in actions:

                next_state = (
                    self._simulate_detective_action(
                        state,
                        action,
                        action_type
                    )
                )


                value = self._minimax(
                    next_state,
                    depth - 1,
                    True,
                    action_type
                )


                best_value = min(
                    best_value,
                    value
                )


            return best_value


    # =========================================================
    # SECURITY DECISION
    # =========================================================

    def _choose_security_action(
        self,
        game_state
    ):

        """
        Decide whether Zephyr should activate Wordle.

        Zephyr is MAX.

        Therefore the action with the HIGHER
        Minimax value is selected.
        """

        if game_state is None:

            return "sabotage"


        # -----------------------------------------------------
        # OPTION 1: ACTIVATE WORDLE
        # -----------------------------------------------------

        sabotage_state = (
            self._simulate_zephyr_action(
                game_state,
                "sabotage",
                "security"
            )
        )


        # -----------------------------------------------------
        # OPTION 2: DO NOT ACTIVATE WORDLE
        # -----------------------------------------------------

        help_state = (
            self._simulate_zephyr_action(
                game_state,
                "help",
                "security"
            )
        )


        # -----------------------------------------------------
        # MINIMAX
        # -----------------------------------------------------

        sabotage_value = self._minimax(
            sabotage_state,
            self.search_depth - 1,
            False,
            "security"
        )


        help_value = self._minimax(
            help_state,
            self.search_depth - 1,
            False,
            "security"
        )


        # -----------------------------------------------------
        # ZEHPYR = MAX
        # -----------------------------------------------------

        if sabotage_value > help_value:

            decision = "sabotage"

        elif help_value > sabotage_value:

            decision = "help"

        else:

            # Tie breaker.

            decision = (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )


        self.decisions_log.append(
            "MINIMAX SECURITY DECISION: "
            f"ACTIVATE WORDLE={sabotage_value:.2f}, "
            f"NO WORDLE={help_value:.2f}. "
            f"Zephyr chose {decision.upper()}."
        )


        return decision


    # =========================================================
    # GENERAL ROOM DECISION
    # =========================================================

    def _choose_room_action(
        self,
        game_state
    ):

        sabotage_state = (
            self._simulate_zephyr_action(
                game_state,
                "sabotage",
                "storage"
            )
        )


        help_state = (
            self._simulate_zephyr_action(
                game_state,
                "help",
                "storage"
            )
        )


        sabotage_value = self._minimax(
            sabotage_state,
            self.search_depth - 1,
            False,
            "storage"
        )


        help_value = self._minimax(
            help_state,
            self.search_depth - 1,
            False,
            "storage"
        )


        # Zephyr = MAX.

        if sabotage_value > help_value:

            decision = "sabotage"

        elif help_value > sabotage_value:

            decision = "help"

        else:

            decision = (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )


        self.decisions_log.append(
            "MINIMAX ROOM DECISION: "
            f"SABOTAGE={sabotage_value:.2f}, "
            f"HELP={help_value:.2f}. "
            f"Zephyr chose {decision.upper()}."
        )


        return decision


    # =========================================================
    # GENERAL HELP / SABOTAGE
    # =========================================================

    def decide_help_or_sabotage(
        self,
        action_name,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        if game_state is None:

            decision = "sabotage"

        else:

            decision = self._choose_room_action(
                game_state
            )


        if decision == "sabotage":

            self.sabotage_count += 1

        else:

            self.help_count += 1


        self.decisions_log.append(
            f"Zephyr chose to {decision.upper()} "
            f"during {action_name}."
        )


        return decision


    # =========================================================
    # ROOM ACTION
    # =========================================================

    def decide_room_action(
        self,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        return self.decide_help_or_sabotage(
            "room investigation",
            suspicion,
            actions_remaining,
            game_state
        )


    # =========================================================
    # STORAGE RIDDLE
    # =========================================================

    def decide_riddle_sabotage(
        self,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        decision = self.decide_help_or_sabotage(
            "Storage riddle",
            suspicion,
            actions_remaining,
            game_state
        )


        return decision == "sabotage"


    # =========================================================
    # CAFETERIA
    # =========================================================

    def decide_cafeteria_action(
        self,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        return self.decide_help_or_sabotage(
            "Cafeteria clue",
            suspicion,
            actions_remaining,
            game_state
        )


    # =========================================================
    # SECURITY SABOTAGE
    # =========================================================

    def decide_security_sabotage(
        self,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        decision = self._choose_security_action(
            game_state
        )


        if decision == "sabotage":

            self.security_sabotage_count += 1

            self.sabotage_count += 1

            self.decisions_log.append(
                "🚨 Zephyr activated the "
                "SECONDARY WORDLE SECURITY CHALLENGE."
            )

            return True


        self.security_skip_count += 1

        self.help_count += 1

        self.decisions_log.append(
            "🔓 Zephyr allowed interrogation "
            "access without the Wordle challenge."
        )

        return False


    # =========================================================
    # COMPATIBILITY
    # =========================================================

    def decide_extra_challenge(
        self,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        return self.decide_security_sabotage(
            suspicion,
            actions_remaining,
            game_state
        )


    # =========================================================
    # TRUTH OR LIE
    # =========================================================

    def decide_truth_or_lie(
        self,
        suspicion=None,
        game_state=None
    ):

        """
        Decide whether Zephyr should tell the truth
        or lie.

        Zephyr = MAX.
        """

        if game_state is None:

            tell_truth = True

        else:

            truth_state = (
                self._simulate_zephyr_action(
                    game_state,
                    "truth",
                    "statement"
                )
            )


            lie_state = (
                self._simulate_zephyr_action(
                    game_state,
                    "lie",
                    "statement"
                )
            )


            truth_value = self._minimax(
                truth_state,
                self.search_depth - 1,
                False,
                "statement"
            )


            lie_value = self._minimax(
                lie_state,
                self.search_depth - 1,
                False,
                "statement"
            )


            # Zephyr = MAX.

            if lie_value > truth_value:

                tell_truth = False

            elif truth_value > lie_value:

                tell_truth = True

            else:

                tell_truth = (
                    self.rng.random() < 0.5
                )


            self.decisions_log.append(
                "MINIMAX STATEMENT DECISION: "
                f"TRUTH={truth_value:.2f}, "
                f"LIE={lie_value:.2f}. "
                f"Zephyr chose "
                f"{'TRUTH' if tell_truth else 'LIE'}."
            )


        if tell_truth:

            self.truth_count += 1

        else:

            self.lie_count += 1


        return tell_truth


    # =========================================================
    # STATS
    # =========================================================

    def stats(self):

        return {

            "sabotage_count":
                self.sabotage_count,

            "help_count":
                self.help_count,

            "lie_count":
                self.lie_count,

            "truth_count":
                self.truth_count,

            "security_sabotage_count":
                self.security_sabotage_count,

            "security_skip_count":
                self.security_skip_count,

            "search_depth":
                self.search_depth,

            "decisions_log":
                list(self.decisions_log)
        }
