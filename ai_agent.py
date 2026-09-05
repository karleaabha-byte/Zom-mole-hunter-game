"""
Adversarial Mole AI for Zom-Mole Hunter.

Zephyr is an adversarial agent.

MINIMAX:
    Detective = MAX
    Zephyr    = MIN

The AI evaluates possible future states and chooses
the action that is most favorable to Zephyr.
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
    # STATE EVALUATION
    # =========================================================

    def _evaluate(self, state):

        """
        Evaluate a game state from Zephyr's perspective.

        Higher score = better for Zephyr.
        Lower score = better for the detective.
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

        visited = getattr(
            state,
            "visited_rooms",
            {}
        )

        score -= len(visited) * 3


        # -----------------------------------------------------
        # QUESTIONS
        # -----------------------------------------------------

        asked = getattr(
            state,
            "asked",
            {}
        )

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

            # Detective now has interrogation access.

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

            # This is VERY good for Zephyr because
            # interrogation is currently blocked.

            score += 50


        elif wordle_failed:

            # Permanent interrogation lock.

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

            # Every remaining attempt means the detective
            # still has to spend effort defeating the lock.

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
        # ACTION COUNT
        # -----------------------------------------------------

        actions = getattr(
            state,
            "actions_used",
            0
        )

        score -= actions


        return score


    # =========================================================
    # STATE SIMULATION
    # =========================================================

    def _simulate(
        self,
        state,
        action,
        action_type
    ):

        """
        Create a simulated future state.

        The actual GameState is never modified.
        """

        if state is None:
            return None


        new_state = copy.deepcopy(state)


        # =====================================================
        # STORAGE
        # =====================================================

        if action_type == "storage":

            if action == "sabotage":

                new_state.suspicion += 3

                new_state.room_decisions[
                    "Storage"
                ] = "riddle_sabotage"

            else:

                new_state.room_decisions[
                    "Storage"
                ] = "help"


        # =====================================================
        # SECURITY
        # =====================================================

        elif action_type == "security":

            if action == "sabotage":

                new_state.security_challenge_active = True

                new_state.security_challenge_complete = False

                new_state.wordle_failed = False

                # Give Zephyr an immediate advantage.

                new_state.suspicion = max(
                    0,
                    new_state.suspicion - 2
                )


            elif action == "help":

                new_state.security_challenge_active = False

                new_state.security_challenge_complete = True

                new_state.wordle_failed = False

                # Detective gets immediate interrogation access.

                new_state.suspicion = min(
                    100,
                    new_state.suspicion + 3
                )


        # =====================================================
        # STATEMENT
        # =====================================================

        elif action_type == "statement":

            if action == "lie":

                new_state.suspicion += 8

            else:

                new_state.suspicion -= 2


        # =====================================================
        # DETECTIVE RESPONSE
        # =====================================================

        elif action_type == "detective":

            if action == "question":

                new_state.actions_used += 1

                new_state.suspicion -= 1


            elif action == "suspect":

                new_state.actions_used += 1

                new_state.suspicion += 5


            elif action == "solve_wordle":

                new_state.actions_used += 1

                # A successful future Wordle solution would
                # remove Zephyr's security advantage.

                new_state.security_challenge_active = False

                new_state.security_challenge_complete = True


        # -----------------------------------------------------
        # CLAMP
        # -----------------------------------------------------

        new_state.suspicion = max(
            0,
            min(
                100,
                new_state.suspicion
            )
        )


        return new_state


    # =========================================================
    # DETECTIVE RESPONSES
    # =========================================================

    def _detective_actions(
        self,
        state,
        action_type
    ):

        """
        Possible responses by the detective.

        Detective is MAX.
        """

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
                "continue"
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
            "continue"
        ]


    # =========================================================
    # MINIMAX
    # =========================================================

    def _minimax(
        self,
        state,
        depth,
        maximizing,
        action_type
    ):

        """
        Minimax search.

        Detective = MAX
        Zephyr = MIN
        """

        if state is None:

            return 0


        if depth <= 0:

            return self._evaluate(state)


        # =====================================================
        # DETECTIVE / MAX
        # =====================================================

        if maximizing:

            responses = self._detective_actions(
                state,
                action_type
            )


            if not responses:

                return self._evaluate(state)


            best_value = float("-inf")


            for response in responses:

                next_state = self._simulate(
                    state,
                    response,
                    "detective"
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
        # ZEPHYR / MIN
        # =====================================================

        actions = [
            "sabotage",
            "help"
        ]


        best_value = float("inf")


        for action in actions:

            next_state = self._simulate(
                state,
                action,
                action_type
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
    # SECURITY MINIMAX
    # =========================================================

    def _choose_security_action(
        self,
        game_state
    ):

        """
        Decide whether Zephyr should activate the Wordle
        security challenge.

        This is a dedicated Minimax search because the
        security decision has a completely different effect
        from the Storage decision.
        """

        if game_state is None:

            return (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )


        # -----------------------------------------------------
        # SIMULATE WORDLE
        # -----------------------------------------------------

        sabotage_state = self._simulate(
            game_state,
            "sabotage",
            "security"
        )


        # -----------------------------------------------------
        # SIMULATE NO WORDLE
        # -----------------------------------------------------

        help_state = self._simulate(
            game_state,
            "help",
            "security"
        )


        # -----------------------------------------------------
        # MINIMAX VALUES
        # -----------------------------------------------------

        sabotage_value = self._minimax(
            sabotage_state,
            self.search_depth - 1,
            True,
            "security"
        )


        help_value = self._minimax(
            help_state,
            self.search_depth - 1,
            True,
            "security"
        )


        # -----------------------------------------------------
        # ZEHPYR CHOOSES THE LOWER VALUE
        # -----------------------------------------------------

        if sabotage_value < help_value:

            decision = "sabotage"

        elif help_value < sabotage_value:

            decision = "help"

        else:

            # Equal positions.
            # Use a random tie-break rather than always
            # choosing the same action.

            decision = (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )


        self.decisions_log.append(
            "MINIMAX SECURITY DECISION: "
            f"Wordle={sabotage_value:.2f}, "
            f"No Wordle={help_value:.2f}. "
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

        """
        General Zephyr decision.

        Uses Minimax when GameState is available.
        """

        if game_state is None:

            decision = (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )

        else:

            # Storage is the primary room where Zephyr
            # actually has a sabotage choice.

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
    # ROOM MINIMAX
    # =========================================================

    def _choose_room_action(
        self,
        game_state
    ):

        sabotage_state = self._simulate(
            game_state,
            "sabotage",
            "storage"
        )


        help_state = self._simulate(
            game_state,
            "help",
            "storage"
        )


        sabotage_value = self._minimax(
            sabotage_state,
            self.search_depth - 1,
            True,
            "storage"
        )


        help_value = self._minimax(
            help_state,
            self.search_depth - 1,
            True,
            "storage"
        )


        if sabotage_value < help_value:

            decision = "sabotage"

        elif help_value < sabotage_value:

            decision = "help"

        else:

            decision = (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )


        self.decisions_log.append(
            "MINIMAX ROOM DECISION: "
            f"Sabotage={sabotage_value:.2f}, "
            f"Help={help_value:.2f}. "
            f"Zephyr chose {decision.upper()}."
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
    # SECURITY / WORDLE
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
                "🚨 Zephyr chose to activate "
                "the SECONDARY WORDLE SECURITY CHALLENGE."
            )

            return True


        self.security_skip_count += 1

        self.help_count += 1

        self.decisions_log.append(
            "🔓 Zephyr chose to leave "
            "interrogation unlocked."
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
    # TRUTH / LIE
    # =========================================================

    def decide_truth_or_lie(
        self,
        suspicion=None,
        game_state=None
    ):

        """
        Minimax decision between telling the truth
        and lying.
        """

        if game_state is None:

            tell_truth = (
                self.rng.random() < 0.5
            )

        else:

            truth_state = self._simulate(
                game_state,
                "truth",
                "statement"
            )


            lie_state = self._simulate(
                game_state,
                "lie",
                "statement"
            )


            truth_value = self._minimax(
                truth_state,
                self.search_depth - 1,
                True,
                "statement"
            )


            lie_value = self._minimax(
                lie_state,
                self.search_depth - 1,
                True,
                "statement"
            )


            if lie_value < truth_value:

                tell_truth = False

            elif truth_value < lie_value:

                tell_truth = True

            else:

                tell_truth = (
                    self.rng.random() < 0.5
                )


            self.decisions_log.append(
                "MINIMAX STATEMENT DECISION: "
                f"Truth={truth_value:.2f}, "
                f"Lie={lie_value:.2f}. "
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
