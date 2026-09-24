import streamlit as st
import time
import random

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "👾 Space Invaders"]
)

# -------------------------------------------------------------
# PAGE 1: REAL FUNCTIONAL CALCULATOR 
# -------------------------------------------------------------
if app_mode == "🔢 Calculator":
    st.title("🔢 Calculator")
    st.caption("For those who just joined the stream calc is short for Calculator i'm just using slang")

    val1 = st.number_input("First Number (x):", value=0.0, step=0.1, key="pro_val1")
    if val1 == 67:
        st.error("unfunny")

    val2 = st.number_input("Second Number (y):", value=0.0, step=0.1, key="pro_val2")
    if val2 == 67:
        st.error("67 in the big 26 🥀")
    
    operation = st.selectbox(
        "Select Operation:",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (x^y)", "Remainder (%)", "Absolute Value |x|"]
    )

    if st.button("Compute Result", key="pro_btn"):
        st.write("---")
        if operation == "Addition (+)":
            if (val1 == 9 and val2 == 10) or (val1 == 10 and val2 == 9):
                st.success("🗣️ 21 YOU STUPID")
            elif val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
            else:
                st.success(f"Result: {val1 + val2}")
        elif operation == "Subtraction (-)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
            else:
                st.success(f"Result: {val1 - val2}")
        elif operation == "Multiplication (×)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
            else:
                st.success(f"Result: {val1 * val2}")
        elif operation == "Power (x^y)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
            else:
                st.success(f"Result: {val1 ** val2}")
        elif operation == "Remainder (%)":
            if val2 == 0:
                st.error("Error: Cannot calculate remainder with a divisor of zero.")
            elif val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
            else:
                st.success(f"Result: {val1 % val2}")
        elif operation == "Absolute Value |x|":
            st.success(f"Result: {abs(val1)} (Note: This operation ignores the second number)")
        elif operation == "Division (÷)":
            if val2 == 0:
                countdown_box = st.empty()
                for seconds_left in range(5, 0, -1):
                    countdown_box.error(f"Why tf you divide by zero im cooked {seconds_left} SECONDS...")
                    time.sleep(1) 
                countdown_box.empty()
                st.write("# yes rico kabo-💥💥💥💥💥💥")
                st.error("The calculation logic has completely vaporized. Application unusable.")
                blast_grid = " ".join(["💥" if i % 2 == 0 else "🔥" for i in range(120)])
                st.text(blast_grid)
            elif val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
            else:
                st.success(f"Result: {val1 / val2}")



# -------------------------------------------------------------
# PAGE 2: PLAYABLE SNAKE GAME 
# -------------------------------------------------------------
elif app_mode == "🐍 Snake":
    st.title("🐍 Web Arcade: Snake")
    st.caption("Click a direction button below. The snake will instantly move one step in that direction!")

    if 'snake' not in st.session_state:
        st.session_state.snake = [(5, 5), (5, 6), (5, 7)]
        st.session_state.food = (2, 2)
        st.session_state.score = 0
        st.session_state.game_over = False
    if 'current_hint' not in st.session_state:
        st.session_state.current_hint = ""

    def reset_game():
        st.session_state.snake = [(5, 5), (5, 6), (5, 7)]
        st.session_state.food = (3, 3)
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.current_hint = ""

    def move_snake(next_dir):
        if st.session_state.game_over:
            return
        head_x, head_y = st.session_state.snake[0]
        if next_dir == "UP": head_y -= 1
        elif next_dir == "DOWN": head_y += 1
        elif next_dir == "LEFT": head_x -= 1
        elif next_dir == "RIGHT": head_x += 1

        new_head = (head_x, head_y)
        GRID_SIZE = 10

        if (head_x < 0 or head_x >= GRID_SIZE or head_y < 0 or head_y >= GRID_SIZE or new_head in st.session_state.snake):
            st.session_state.game_over = True
            hints = ["Maybe pay attention next time?", "Hey idiot the apples over there", "Maybe don't spam?", "Nice one!", "imagine losing in snake lmfao"]
            st.session_state.current_hint = random.choice(hints)
        else:
            st.session_state.snake.insert(0, new_head)
            if new_head == st.session_state.food:
                st.session_state.score += 1
                st.session_state.food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
            else:
                st.session_state.snake.pop()

    GRID_SIZE = 10
    grid = [["⬜" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    if not st.session_state.game_over:
        fx, fy = st.session_state.food
        grid[fy][fx] = "🍎"
        for i, (sx, sy) in enumerate(st.session_state.snake):
            grid[sy][sx] = "🟩" if i > 0 else "🐲"

    st.text("\n".join([" ".join(row) for row in grid]))
    st.write(f"🏆 Current Score: **{st.session_state.score}**")

    if st.session_state.game_over:
        st.error("Game Over!")
        st.warning(st.session_state.current_hint)
        if st.button("Play Again"):
            reset_game()
            st.rerun()
    else:
        st.write("--- Controls ---")
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("🔼 Up"):
                move_snake("UP"); st.rerun()
        col4, col5, col6 = st.columns(3)
        with col4:
            if st.button("◀️ Left"):
                move_snake("LEFT"); st.rerun()
        with col5:
            st.write("D-Pad")
        with col6:
            if st.button("▶️ Right"):
                move_snake("RIGHT"); st.rerun()
        col7, col8, col9 = st.columns(3)
        with col8:
            if st.button("🔽 Down"):
                move_snake("DOWN"); st.rerun()
# -------------------------------------------------------------
# PAGE 3: PLAYABLE SPACE INVADERS (TURN-BASED FIX)
# -------------------------------------------------------------
elif app_mode == "👾 Space Invaders":
    st.title("👾 Space Invaders")
    st.caption("Move your ship and fire lasers to clear the descending alien fleet!")

    # Initialize state variables safely
    if 'player_x' not in st.session_state:
        st.session_state.player_x = 4
        st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]
        st.session_state.si_score = 0
        st.session_state.active_laser = None  # Persistent coordinate: (x, y)
        st.session_state.si_game_over = False

    def draw_and_render_grid():
        """Draws the current layout of objects on our board grid"""
        si_grid = [["⬛" for _ in range(10)] for _ in range(10)]
        if not st.session_state.si_game_over:
            for ix, iy in st.session_state.invaders:
                si_grid[iy][ix] = "🛸"
            if st.session_state.active_laser:
                lx, ly = st.session_state.active_laser
                si_grid[ly][lx] = "⚡"
            si_grid[st.session_state.player_x] = "🚀"
        return "\n".join([" ".join(row) for row in si_grid])

    def run_si_turn(action):
        if st.session_state.si_game_over:
            return

        # 1. Advance an existing active laser first, regardless of the action taken
        if st.session_state.active_laser:
            lx, ly = st.session_state.active_laser
            ly -= 2  # Moves 2 squares per turn to keep the speed fast and snappy
            
            # Impact Check during flight progression
            if (lx, ly) in st.session_state.invaders or (lx, ly + 1) in st.session_state.invaders:
                target = (lx, ly) if (lx, ly) in st.session_state.invaders else (lx, ly + 1)
                st.session_state.invaders.remove(target)
                st.session_state.si_score += 10
                st.session_state.active_laser = None
            elif ly <= 0:
                st.session_state.active_laser = None  # Clears safely if it goes off-screen
            else:
                st.session_state.active_laser = (lx, ly)

        # 2. Process the player's core input action
        if action == "LEFT" and st.session_state.player_x > 0:
            st.session_state.player_x -= 1
        elif action == "RIGHT" and st.session_state.player_x < 9:
            st.session_state.player_x += 1
        elif action == "FIRE":
            # Spawn a fresh laser tracking slot if empty
            if st.session_state.active_laser is None:
                st.session_state.active_laser = (st.session_state.player_x, 8)

        # 3. Handle Alien Fleet Descent step pacing logic
        if random.random() < 0.30 and len(st.session_state.invaders) > 0:
            new_invaders = []
            for ix, iy in st.session_state.invaders:
                if iy + 1 >= 9:
                    st.session_state.si_game_over = True
                new_invaders.append((ix, iy + 1))
            st.session_state.invaders = new_invaders

        # Wave Respawn Condition Check
        if len(st.session_state.invaders) == 0:
            st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]

    # Render visuals layout frame
    st.text(draw_and_render_grid())
    st.write(f"🏆 Score: **{st.session_state.si_score}**")

    # Controller UI Layout Panel
    if st.session_state.si_game_over:
        st.error("Your ship was overrun!")
        if st.button("Respawn Fleet"):
            del st.session_state.player_x
            st.rerun()
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("◀️ Move Left"):
                run_si_turn("LEFT")
                st.rerun()
        with col2:
            if st.button("🔥 Fire Laser"):
                run_si_turn("FIRE")
                st.rerun()
        with col3:
            if st.button("Move Right ▶️"):
                run_si_turn("RIGHT")
                st.rerun()


           
