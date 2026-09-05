import streamlit as st

from game import GameState, ROOMS
import case


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Zom-Mole Hunter",
    page_icon="🕵️",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b0f0d;
        color: #e8f5e9;
    }

    .main-title {
        font-size: 52px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 30px;
    }

    .danger {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #8b0000;
        background-color: #210909;
    }

    .success {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #176b35;
        background-color: #092313;
    }

    .evidence-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #555;
        background-color: #151917;
        margin-bottom: 10px;
    }

    .suspect-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #444;
        background-color: #111513;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "game" not in st.session_state:

    st.session_state.game = GameState()


game = st.session_state.game


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def rerun():
    st.rerun()


def show_message(success, message):

    if success:
        st.success(message)

    else:
        st.error(message)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🧟 ZOM-MOLE HUNTER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    "A suspicious employee. A contaminated facility. "
    "One mole. Find them before you run out of time."
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📊 CASE STATUS")

    st.metric(
        "ACTIONS REMAINING",
        game.actions_remaining
    )

    st.metric(
        "SUSPICION",
        game.suspicion
    )

    st.divider()

    st.subheader("🔐 SECURITY")

    if game.pin_cracked:

        st.success("PIN CRACKED")

    else:

        st.warning("PIN LOCKED")


    if game.security_challenge_active:

        st.warning("SECONDARY LOCK ACTIVE")

    elif game.security_challenge_complete:

        st.success("SECONDARY LOCK CLEARED")

    elif game.wordle_failed:

        st.error("SECURITY FAILED")


    st.divider()

    st.subheader("🏢 ROOMS")

    for room in ROOMS:

        if room in game.visited_rooms:

            st.write(
                f"✅ {room}"
            )

        else:

            st.write(
                f"⬜ {room}"
            )


    st.divider()

    if st.button(
        "🔄 RESTART CASE",
        use_container_width=True
    ):

        st.session_state.game = GameState()

        st.rerun()


# ============================================================
# GAME OVER
# ============================================================

if game.game_over:

    st.divider()

    if game.result == "win":

        st.markdown(
            """
            <div class="success">
            <h2>🎉 CASE SOLVED</h2>
            <p>
            You correctly identified the mole.
            The facility is safe... for now.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="danger">
            <h2>💀 WRONG ACCUSATION</h2>
            <p>
            You accused the wrong employee.
            The real mole got away.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Final Case Report")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Accused",
            game.accused
        )

    with col2:

        st.metric(
            "Suspicion",
            game.suspicion
        )

    with col3:

        st.metric(
            "Actions Used",
            game.actions_used
        )


    st.divider()

    st.subheader("📝 Investigation Log")

    for entry in game.log:

        st.write(
            f"• {entry}"
        )


    st.stop()


# ============================================================
# MAIN TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🔎 INVESTIGATE",
        "🔐 SECURITY",
        "💬 INTERROGATE",
        "📋 EVIDENCE",
        "⚖️ ACCUSE"
    ]
)


# ============================================================
# TAB 1 — INVESTIGATION
# ============================================================

with tab1:

    st.header("🔎 Investigate the Facility")

    st.write(
        "Search the rooms for clues. "
        "Every important Zephyr action has an independent 50/50 "
        "chance of HELP or SABOTAGE."
    )


    # --------------------------------------------------------
    # ROOM BUTTONS
    # --------------------------------------------------------

    cols = st.columns(3)


    for index, room in enumerate(ROOMS):

        with cols[index]:

            st.subheader(room)

            if room in game.visited_rooms:

                st.success(
                    "Already investigated"
                )

                clue = game.visited_rooms[room]

                st.write(clue)


            else:

                if st.button(
                    f"Investigate {room}",
                    key=f"visit_{room}",
                    disabled=not game.can_act(),
                    use_container_width=True
                ):

                    success, result = game.visit_room(
                        room
                    )

                    if success:

                        st.success(
                            f"You investigated the {room}."
                        )

                        st.write(result)

                    else:

                        st.error(result)

                    st.rerun()


    # --------------------------------------------------------
    # SHOW VISITED CLUES
    # --------------------------------------------------------

    st.divider()

    st.subheader("🗂️ Recovered Clues")

    if not game.visited_rooms:

        st.info(
            "No clues recovered yet."
        )

    else:

        for room, clue in game.visited_rooms.items():

            with st.expander(
                f"📁 {room}"
            ):

                st.write(clue)


# ============================================================
# TAB 2 — SECURITY
# ============================================================

with tab2:

    st.header("🔐 Security System")


    # ========================================================
    # PIN SECTION
    # ========================================================

    st.subheader("Cafeteria Security PIN")

    if game.pin_cracked:

        st.success(
            "🔓 PIN 4619 CRACKED"
        )

        st.write(
            "Restricted employee records are now accessible."
        )

    else:

        st.write(
            "The Cafeteria clue contains a hidden "
            "4-digit security PIN."
        )

        pin_guess = st.text_input(
            "Enter 4-digit PIN",
            max_chars=4,
            key="pin_input"
        )


        if st.button(
            "CRACK PIN",
            disabled=not game.can_act(),
            use_container_width=True
        ):

            if not pin_guess:

                st.warning(
                    "Enter a PIN first."
                )

            else:

                correct = game.attempt_pin(
                    pin_guess
                )

                if correct:

                    st.success(
                        "🔓 PIN CRACKED!"
                    )

                else:

                    st.error(
                        "❌ Incorrect PIN."
                    )

                st.rerun()


    # ========================================================
    # WORDLE SECURITY CHALLENGE
    # ========================================================

    if game.security_challenge_active:

        st.divider()

        st.header("🚨 SECONDARY SECURITY LOCK")

        st.warning(
            "Zephyr triggered an additional security challenge."
        )

        st.write(
            "Solve the 5-letter Wordle-style challenge "
            "to unlock interrogation."
        )

        st.info(
            "🟩 Correct letter and position\n\n"
            "🟨 Correct letter, wrong position\n\n"
            "⬛ Letter is not in the answer"
        )


        # ----------------------------------------------------
        # ATTEMPTS
        # ----------------------------------------------------

        attempts_left = (
            game.wordle_max_attempts
            - len(game.wordle_attempts)
        )


        st.metric(
            "ATTEMPTS REMAINING",
            attempts_left
        )


        # ----------------------------------------------------
        # PREVIOUS ATTEMPTS
        # ----------------------------------------------------

        if game.wordle_attempts:

            st.subheader(
                "Previous Attempts"
            )

            for attempt in game.wordle_attempts:

                feedback = []

                for i, letter in enumerate(attempt):

                    if (
                        i < len(game.wordle_answer)
                        and letter == game.wordle_answer[i]
                    ):

                        feedback.append("🟩")

                    elif (
                        letter in game.wordle_answer
                    ):

                        feedback.append("🟨")

                    else:

                        feedback.append("⬛")


                st.write(
                    f"`{attempt}`  "
                    + " ".join(feedback)
                )


        # ----------------------------------------------------
        # WORDLE INPUT
        # ----------------------------------------------------

        wordle_guess = st.text_input(
            "Enter a 5-letter word",
            max_chars=5,
            key="wordle_input"
        )


        if st.button(
            "SUBMIT WORD",
            use_container_width=True
        ):

            success, result = game.submit_wordle(
                wordle_guess
            )


            # ------------------------------------------------
            # INVALID INPUT
            # ------------------------------------------------

            if not success:

                if result == "ATTEMPTS_EXHAUSTED":

                    st.error(
                        "🔐 Security challenge failed."
                    )

                elif isinstance(result, dict):

                    if result["status"] == "FAILED":

                        st.error(
                            "🔐 Security challenge failed."
                        )

                    else:

                        st.error(
                            "Invalid attempt."
                        )

                else:

                    st.error(
                        result
                    )


            # ------------------------------------------------
            # VALID RESULT
            # ------------------------------------------------

            elif isinstance(result, dict):

                status = result.get(
                    "status"
                )


                if status == "CORRECT":

                    st.success(
                        "🔓 SECURITY LOCK DEFEATED!"
                    )

                    st.write(
                        "Interrogation access unlocked."
                    )


                elif status == "CONTINUE":

                    st.info(
                        "Not quite. Keep investigating."
                    )


                elif status == "FAILED":

                    st.error(
                        "🔐 SECURITY CHALLENGE FAILED."
                    )


            elif result == "ALREADY_COMPLETE":

                st.success(
                    "Security challenge already completed."
                )


            st.rerun()


    # ========================================================
    # SECURITY COMPLETE
    # ========================================================

    elif game.security_challenge_complete:

        st.divider()

        st.success(
            "🔓 ALL SECURITY LOCKS CLEARED"
        )

        st.write(
            "You can now interrogate the suspects."
        )


    # ========================================================
    # SECURITY FAILED
    # ========================================================

    elif game.wordle_failed:

        st.divider()

        st.error(
            "🔒 SECURITY SYSTEM LOCKED YOU OUT"
        )

        st.write(
            "The secondary security challenge was not completed."
        )


# ============================================================
# TAB 3 — INTERROGATION
# ============================================================

with tab3:

    st.header("💬 Interrogation Room")


    # --------------------------------------------------------
    # ACCESS CHECK
    # --------------------------------------------------------

    if not game.pin_cracked:

        st.warning(
            "🔒 Crack the Cafeteria PIN before interrogating "
            "employees."
        )

    elif game.security_challenge_active:

        st.warning(
            "🔐 Complete the secondary security challenge "
            "before interrogating employees."
        )

    elif game.wordle_failed:

        st.error(
            "🔒 Interrogation access is blocked."
        )

    else:

        st.write(
            "Ask each suspect one question."
        )

        st.info(
            "Zephyr independently decides 50/50 whether "
            "to tell the truth or lie."
        )


        # ----------------------------------------------------
        # SUSPECTS
        # ----------------------------------------------------

        for character in case.CHARACTERS:

            st.markdown(
                f'<div class="suspect-card">'
                f"<h3>🧑 {character}</h3>"
                f"</div>",
                unsafe_allow_html=True
            )


            if character in game.asked:

                previous = game.asked[
                    character
                ]

                st.success(
                    "Already questioned."
                )

                st.write(
                    f"**Question:** "
                    f"{previous['question']}"
                )

                st.write(
                    f"**Answer:** "
                    f"{previous['answer']}"
                )

                continue


            question_options = list(
                case.QUESTION_BANK.keys()
            )


            selected_question = st.selectbox(
                "Choose a question",
                question_options,
                key=f"question_{character}"
            )


            if st.button(
                f"Question {character}",
                key=f"ask_{character}",
                disabled=not game.can_act(),
                use_container_width=True
            ):

                success, answer = game.ask_question(
                    character,
                    selected_question
                )


                if success:

                    st.success(
                        f"{character}: {answer}"
                    )

                else:

                    st.error(
                        answer
                    )

                st.rerun()


# ============================================================
# TAB 4 — EVIDENCE
# ============================================================

with tab4:

    st.header("📋 Evidence Board")


    # --------------------------------------------------------
    # ROOM EVIDENCE
    # --------------------------------------------------------

    st.subheader("🔎 Physical Evidence")

    if not game.visited_rooms:

        st.info(
            "Investigate rooms to collect evidence."
        )

    else:

        for room, clue in game.visited_rooms.items():

            st.markdown(
                f"""
                <div class="evidence-box">

                <h4>📍 {room}</h4>

                <p>{clue}</p>

                </div>
                """,
                unsafe_allow_html=True
            )


    # --------------------------------------------------------
    # INTERROGATION EVIDENCE
    # --------------------------------------------------------

    st.subheader("💬 Statements")

    if not game.asked:

        st.info(
            "No suspect statements recorded."
        )

    else:

        for character, statement in game.asked.items():

            st.markdown(
                f"""
                <div class="evidence-box">

                <h4>🧑 {character}</h4>

                <p>
                <b>Question:</b>
                {statement['question']}
                </p>

                <p>
                <b>Answer:</b>
                {statement['answer']}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    # --------------------------------------------------------
    # CONTRADICTIONS
    # --------------------------------------------------------

    st.subheader("🚨 Contradictions")

    if game.contradiction_flagged:

        st.error(
            game.last_contradiction
            or "A contradiction was detected."
        )

    else:

        st.info(
            "No confirmed contradictions yet."
        )


    # --------------------------------------------------------
    # AI DECISIONS
    # --------------------------------------------------------

    st.subheader("🤖 Zephyr Activity")

    ai_stats = game.mole_ai.stats()


    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Help",
            ai_stats["help_count"]
        )

    with col2:

        st.metric(
            "Sabotage",
            ai_stats["sabotage_count"]
        )

    with col3:

        st.metric(
            "Truth",
            ai_stats["truth_count"]
        )

    with col4:

        st.metric(
            "Lies",
            ai_stats["lie_count"]
        )


    if ai_stats["decisions_log"]:

        with st.expander(
            "View Zephyr Decision Log"
        ):

            for decision in ai_stats[
                "decisions_log"
            ]:

                st.write(
                    f"• {decision}"
                )


# ============================================================
# TAB 5 — ACCUSATION
# ============================================================

with tab5:

    st.header("⚖️ Final Accusation")

    st.write(
        "When you are confident, accuse the person "
        "you believe is the mole."
    )


    # --------------------------------------------------------
    # CURRENT STATUS
    # --------------------------------------------------------

    if game.accused:

        st.warning(
            f"You accused {game.accused}."
        )


    # --------------------------------------------------------
    # CHARACTER BUTTONS
    # --------------------------------------------------------

    st.subheader(
        "Who is the mole?"
    )


    cols = st.columns(
        len(case.CHARACTERS)
    )


    for index, character in enumerate(
        case.CHARACTERS
    ):

        with cols[index]:

            if st.button(
                f"⚖️ Accuse {character}",
                key=f"accuse_{character}",
                use_container_width=True
            ):

                success, result = game.make_accusation(
                    character
                )


                if success:

                    st.rerun()

                else:

                    st.error(
                        result
                    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🧟 Zom-Mole Hunter • "
    "Investigate carefully. Trust nobody. "
    "Every Zephyr decision is a 50/50 gamble."
)
