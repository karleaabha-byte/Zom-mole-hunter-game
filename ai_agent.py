"""
Adversarial Mole AI for Zom-Mole Hunter.

Zephyr acts as an adversarial player.

MINIMAX:
    Zephyr = MIN
    Detective = MAX

The AI evaluates possible future game states and chooses
the action that is most beneficial to Zephyr.
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
    # GAME STATE EXTRACTION
    # =========================================================

    def _state_value(self, game_state):

        """
        Evaluate the current state from Zephyr's perspective.

        Higher score = better for Zephyr.
        Lower score = better for detective.
        """

        if game_state is None:
            return 0

        score = 0


        # -----------------------------------------------------
        # SUSPICION
        # -----------------------------------------------------

        suspicion = getattr(
            game_state,
            "suspicion",
            10
        )

        # High suspicion means the detective is getting
        # closer to discovering Zephyr.

        score -= suspicion * 2


        # -----------------------------------------------------
        # VISITED ROOMS
        # -----------------------------------------------------

        visited_rooms = getattr(
            game_state,
            "visited_rooms",
            {}
        )

        # More investigated rooms generally means more
        # evidence for the detective.

        score -= len(visited_rooms) * 4


        # -----------------------------------------------------
        # CONTRADICTIONS
        # -----------------------------------------------------

        contradiction_flagged = getattr(
            game_state,
            "contradiction_flagged",
            False
        )

        if contradiction_flagged:
            score -= 20


        # -----------------------------------------------------
        # PIN
        # -----------------------------------------------------

        pin_cracked = getattr(
            game_state,
            "pin_cracked",
            False
        )

        if pin_cracked:
            # Detective has gained access to interrogation.
            score -= 15


        # -----------------------------------------------------
        # SECURITY CHALLENGE
        # -----------------------------------------------------

        security_active = getattr(
            game_state,
            "security_challenge_active",
            False
        )

        security_complete = getattr(
            game_state,
            "security_challenge_complete",
            False
        )

        wordle_failed = getattr(
            game_state,
            "wordle_failed",
            False
        )


        if security_active:

            # Very good for Zephyr.
            score += 30

        elif security_complete:

            # Detective defeated the obstacle.
            score -= 15

        elif wordle_failed:

            # Even better for Zephyr because interrogation
            # access is permanently blocked.
            score += 35


        # -----------------------------------------------------
        # WORDLE ATTEMPTS
        # -----------------------------------------------------

        wordle_attempts = getattr(
            game_state,
            "wordle_attempts",
            []
        )

        score += len(wordle_attempts) * 2


        # -----------------------------------------------------
        # QUESTIONS
        # -----------------------------------------------------

        asked = getattr(
            game_state,
            "asked",
            {}
        )

        # Every interrogation gives the detective information.

        score -= len(asked) * 5


        # -----------------------------------------------------
        # ACTIONS USED
        # -----------------------------------------------------

        actions_used = getattr(
            game_state,
            "actions_used",
            0
        )

        # More actions means the detective has had more
        # opportunities to gather evidence.

        score -= actions_used


        return score


    # =========================================================
    # SIMULATED STATE
    # =========================================================

    def _simulate_state(
        self,
        game_state,
        action,
        action_type
    ):

        """
        Create a lightweight simulated copy of the game state.

        We do NOT execute the real game methods because those
        methods would create actual evidence/log changes.

        Instead we simulate the important strategic effects.
        """

        if game_state is None:
            return None

        state = copy.deepcopy(game_state)


        # -----------------------------------------------------
        # STORAGE
        # -----------------------------------------------------

        if action_type == "room":

            room = action

            if room == "Storage":

                if action == "sabotage":

                    state.suspicion += 3

                    state.room_decisions[
                        "Storage"
                    ] = "riddle_sabotage"

                else:

                    state.room_decisions[
                        "Storage"
                    ] = "help"


        # -----------------------------------------------------
        # SECURITY
        # -----------------------------------------------------

        elif action_type == "security":

            if action == "sabotage":

                state.security_challenge_active = True

                state.security_challenge_complete = False

            else:

                state.security_challenge_active = False

                state.security_challenge_complete = True


        # -----------------------------------------------------
        # TRUTH / LIE
        # -----------------------------------------------------

        elif action_type == "statement":

            if action == "lie":

                state.suspicion += 8

            else:

                state.suspicion -= 2


        state.suspicion = max(
            0,
            min(
                100,
                state.suspicion
            )
        )

        return state


    # =========================================================
    # DETECTIVE RESPONSE SIMULATION
    # =========================================================

    def _detective_responses(
        self,
        state,
        action_type
    ):

        """
        Generate possible detective responses.

        The detective is MAX in the Minimax tree.
        """

        if state is None:
            return []


        # -----------------------------------------------------
        # ROOM RESPONSE
        # -----------------------------------------------------

        if action_type == "room":

            return [
                "investigate_more",
                "continue"
            ]


        # -----------------------------------------------------
        # SECURITY RESPONSE
        # -----------------------------------------------------

        if action_type == "security":

            return [
                "attempt_wordle",
                "continue"
            ]


        # -----------------------------------------------------
        # STATEMENT RESPONSE
        # -----------------------------------------------------

        if action_type == "statement":

            return [
                "trust_statement",
                "suspect_zephyr"
            ]


        return ["continue"]


    # =========================================================
    # DETECTIVE STATE SIMULATION
    # =========================================================

    def _simulate_detective_response(
        self,
        state,
        response,
        action_type
    ):

        if state is None:
            return None

        new_state = copy.deepcopy(state)


        # -----------------------------------------------------
        # DETECTIVE INVESTIGATES MORE
        # -----------------------------------------------------

        if response == "investigate_more":

            new_state.actions_used += 1


        # -----------------------------------------------------
        # DETECTIVE ATTEMPTS WORDLE
        # -----------------------------------------------------

        elif response == "attempt_wordle":

            new_state.actions_used += 1


        # -----------------------------------------------------
        # DETECTIVE SUSPECTS ZEPHYR
        # -----------------------------------------------------

        elif response == "suspect_zephyr":

            new_state.suspicion += 5


        # -----------------------------------------------------
        # DETECTIVE TRUSTS STATEMENT
        # -----------------------------------------------------

        elif response == "trust_statement":

            new_state.suspicion -= 2


        new_state.suspicion = max(
            0,
            min(
                100,
                new_state.suspicion
            )
        )

        return new_state


    # =========================================================
    # MINIMAX
    # =========================================================

    def _minimax(
        self,
        state,
        depth,
        maximizing
    ):

        """
        Minimax search.

        maximizing = True
            Detective tries to maximize its advantage.

        maximizing = False
            Zephyr tries to minimize detective advantage.

        Our evaluation is from Zephyr's perspective.
        Therefore:

            Zephyr MIN
            Detective MAX
        """

        if state is None:

            return 0


        if depth == 0:

            return self._state_value(state)


        # =====================================================
        # ZEHPYR / MIN
        # =====================================================

        if not maximizing:

            actions = [
                "sabotage",
                "help"
            ]

            best_value = float("inf")


            for action in actions:

                simulated = self._simulate_state(
                    state,
                    action,
                    "room"
                )

                # Detective gets a chance to respond.
                responses = self._detective_responses(
                    simulated,
                    "room"
                )

                if not responses:

                    value = self._minimax(
                        simulated,
                        depth - 1,
                        True
                    )

                else:

                    values = []

                    for response in responses:

                        response_state = (
                            self._simulate_detective_response(
                                simulated,
                                response,
                                "room"
                            )
                        )

                        values.append(
                            self._minimax(
                                response_state,
                                depth - 1,
                                False
                            )
                        )

                    # Detective chooses the outcome best
                    # for themselves.
                    value = max(values)


                best_value = min(
                    best_value,
                    value
                )


            return best_value


        # =====================================================
        # DETECTIVE / MAX
        # =====================================================

        responses = self._detective_responses(
            state,
            "room"
        )

        best_value = float("-inf")


        for response in responses:

            simulated = (
                self._simulate_detective_response(
                    state,
                    response,
                    "room"
                )
            )

            value = self._state_value(
                simulated
            )

            best_value = max(
                best_value,
                value
            )


        return best_value


    # =========================================================
    # CHOOSE BETWEEN HELP AND SABOTAGE
    # =========================================================

    def _choose_adversarial_action(
        self,
        game_state,
        action_type
    ):

        """
        Search the possible outcomes of each Zephyr action
        and select the action with the best Minimax value.
        """

        if game_state is None:

            return (
                "sabotage"
                if self.rng.random() < 0.5
                else "help"
            )


        actions = [
            "sabotage",
            "help"
        ]

        values = {}


        for action in actions:

            simulated = self._simulate_state(
                game_state,
                action,
                action_type
            )


            responses = self._detective_responses(
                simulated,
                action_type
            )


            if not responses:

                value = self._minimax(
                    simulated,
                    self.search_depth - 1,
                    True
                )

            else:

                response_values = []


                for response in responses:

                    response_state = (
                        self._simulate_detective_response(
                            simulated,
                            response,
                            action_type
                        )
                    )

                    response_values.append(
                        self._minimax(
                            response_state,
                            self.search_depth - 1,
                            False
                        )
                    )


                # Detective chooses their best response.
                value = max(response_values)


            values[action] = value


        # Zephyr chooses the MINIMUM value for the detective.

        best_action = min(
            values,
            key=values.get
        )


        self.decisions_log.append(
            f"Minimax evaluated {action_type}: "
            f"sabotage={values['sabotage']:.2f}, "
            f"help={values['help']:.2f}. "
            f"Zephyr chose {best_action.upper()}."
        )


        return best_action


    # =========================================================
    # ROOM ACTION
    # =========================================================

    def decide_help_or_sabotage(
        self,
        action_name,
        suspicion=None,
        actions_remaining=None,
        game_state=None
    ):

        """
        General adversarial decision.

        game_state is optional so the method remains compatible
        with older versions of the game.
        """

        decision = self._choose_adversarial_action(
            game_state,
            "room"
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

        decision = self._choose_adversarial_action(
            game_state,
            "security"
        )


        if decision == "sabotage":

            self.security_sabotage_count += 1

            self.sabotage_count += 1

            self.decisions_log.append(
                "Zephyr used Minimax to activate "
                "the secondary security challenge."
            )

            return True


        self.security_skip_count += 1

        self.help_count += 1

        self.decisions_log.append(
            "Zephyr used Minimax to leave "
            "interrogation access unlocked."
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
        Decide whether Zephyr should lie.

        The AI compares:

            LIE
            TRUTH

        using the current game state.
        """

        if game_state is None:

            # Compatibility fallback.
            tell_truth = (
                self.rng.random() < 0.5
            )

        else:

            truth_state = self._simulate_state(
                game_state,
                "truth",
                "statement"
            )

            lie_state = self._simulate_state(
                game_state,
                "lie",
                "statement"
            )


            truth_value = self._minimax(
                truth_state,
                self.search_depth - 1,
                True
            )

            lie_value = self._minimax(
                lie_state,
                self.search_depth - 1,
                True
            )


            # Zephyr chooses the action that produces the
            # lowest score for the detective.

            if lie_value < truth_value:

                tell_truth = False

            elif truth_value < lie_value:

                tell_truth = True

            else:

                tell_truth = (
                    self.rng.random() < 0.5
                )


            self.decisions_log.append(
                f"Minimax evaluated statement: "
                f"truth={truth_value:.2f}, "
                f"lie={lie_value:.2f}. "
                f"Zephyr chose "
                f"{'TRUTH' if tell_truth else 'LIE'}."
            )


        if tell_truth:

            self.truth_count += 1

        else:

            self.lie_count += 1


        return tell_truth


    # =========================================================
    # STATISTICS
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
