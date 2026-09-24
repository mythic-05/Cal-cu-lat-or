import streamlit as st
import time
import random

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "👾 Space Invaders", "🕹️Tetris"]
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
# PAGE 3: PLAYABLE SPACE INVADERS (PERSISTENT FASTER LASER
# -------------------------------------------------------------
elif app_mode == "👾 Space Invaders":
    st.title("👾 Space Invaders")
    st.caption("Move your ship and fire lasers to clear the descending alien fleet!")

    # Initialize state variables safely
    if 'player_x' not in st.session_state:
        st.session_state.player_x = 4
        st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]
        st.session_state.si_score = 0
        st.session_state.active_laser = None  # Tracks a persistent tuple: (laser_x, laser_y)
        st.session_state.si_game_over = False

    def draw_and_render_grid():
        """Helper function to draw the current frame to the screen"""
        si_grid = [["⬛" for _ in range(10)] for _ in range(10)]
        if not st.session_state.si_game_over:
            for ix, iy in st.session_state.invaders:
                si_grid[iy][ix] = "🛸"
            if st.session_state.active_laser:
                lx, ly = st.session_state.active_laser
                si_grid[ly][lx] = "⚡"
            si_grid[9][st.session_state.player_x] = "🚀"
        return "\n".join([" ".join(row) for row in si_grid])

    # Screen visual containers
    grid_placeholder = st.empty()
    score_placeholder = st.empty()

    def run_si_turn(action):
        if st.session_state.si_game_over:
            return

        # 1. Handle Ship Movements without wiping out the existing active laser coordinate
        if action == "LEFT" and st.session_state.player_x > 0:
            st.session_state.player_x -= 1
        elif action == "RIGHT" and st.session_state.player_x < 9:
            st.session_state.player_x += 1

        # 2. Handle Snappy, Fast Laser Fire Animation Loop
        elif action == "FIRE":
            # Only fire if there isn't a laser already clearing empty space on screen
            if st.session_state.active_laser is None:
                lx = st.session_state.player_x
                ly = 9
                
                while ly > 0:
                    ly -= 1
                    st.session_state.active_laser = (lx, ly)
                    
                    # Real-time impact detection
                    if (lx, ly) in st.session_state.invaders:
                        st.session_state.invaders.remove((lx, ly))
                        st.session_state.si_score += 10
                        st.session_state.active_laser = None
                        break
                        
                    # Update graphics frame layout rapidly with 0.08s speed step
                    grid_placeholder.text(draw_and_render_grid())
                    score_placeholder.write(f"🏆 Score: **{st.session_state.si_score}**")
                    time.sleep(0.008)
                
                # Clear laser reference path once it harmlessly exits the top ceiling grid row
                st.session_state.active_laser = None

        # 3. Handle Alien Fleet Descent step pacing logic
        if random.random() < 0.35 and len(st.session_state.invaders) > 0:
            new_invaders = []
            for ix, iy in st.session_state.invaders:
                if iy + 1 >= 9:
                    st.session_state.si_game_over = True
                new_invaders.append((ix, iy + 1))
            st.session_state.invaders = new_invaders

        # Tougher Wave Respawn Condition Check
        if len(st.session_state.invaders) == 0:
            st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]

    # Final visual refresh step
    grid_placeholder.text(draw_and_render_grid())
    score_placeholder.write(f"🏆 Score: **{st.session_state.si_score}**")

    # Controller UI Panel 
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

           
import streamlit as None
import time
import random

# -------------------------------------------------------------
# PAGE 4: PLAYABLE TETRIS 
# -------------------------------------------------------------
elif app_mode == "🕹️Tetris":
    st.title("🕹️Tetris")
    st.caption("Align horizontal rows! Blocks fall automatically every second.")

    T_ROWS, T_COLS = 12, 8

    # Classic Tetris Tetromino Shapes & Colors
    SHAPES = {
        "I": {"matrix": [[1, 1, 1, 1]], "color": "🟪"},
        "O": {"matrix": [[1, 1], [1, 1]], "color": "🟨"},
        "T": {"matrix": [[0, 1, 0], [1, 1, 1]], "color": "🟥"},
        "L": {"matrix": [[1, 0], [1, 0], [1, 1]], "color": "🟧"},
        "J": {"matrix": [[0, 1], [0, 1], [1, 1]], "color": "🟦"},
        "S": {"matrix": [[0, 1, 1], [1, 1, 0]], "color": "🟩"}
    }

    def get_random_piece():
        name = random.choice(list(SHAPES.keys()))
        return {
            "matrix": SHAPES[name]["matrix"],
            "color": SHAPES[name]["color"],
            "x": T_COLS // 2 - len(SHAPES[name]["matrix"][0]) // 2,
            "y": 0
        }

    # Initialize Tetris session state tracking
    if 'tetris_board' not in st.session_state:
        st.session_state.tetris_board = [["⬛" for _ in range(T_COLS)] for _ in range(T_ROWS)]
        st.session_state.current_piece = get_random_piece()
        st.session_state.t_score = 0
        st.session_state.t_game_over = False

    def reset_tetris():
        st.session_state.tetris_board = [["⬛" for _ in range(T_COLS)] for _ in range(T_ROWS)]
        st.session_state.current_piece = get_random_piece()
        st.session_state.t_score = 0
        st.session_state.t_game_over = False

    def check_collision(piece, offset_x=0, offset_y=0):
        """Returns True if the piece collides with walls or locked blocks."""
        matrix = piece["matrix"]
        for r_idx, row in enumerate(matrix):
            for c_idx, val in enumerate(row):
                if val:
                    new_x = piece["x"] + c_idx + offset_x
                    new_y = piece["y"] + r_idx + offset_y
                    # Check boundary limits
                    if new_x < 0 or new_x >= T_COLS or new_y >= T_ROWS:
                        return True
                    # Check background static grid blocks
                    if new_y >= 0 and st.session_state.tetris_board[new_y][new_x] != "⬛":
                        return True
        return False

    def lock_piece(piece):
        matrix = piece["matrix"]
        color = piece["color"]
        for r_idx, row in enumerate(matrix):
            for c_idx, val in enumerate(row):
                if val:
                    y = piece["y"] + r_idx
                    x = piece["x"] + c_idx
                    if y >= 0:
                        st.session_state.tetris_board[y][x] = color

        # Check and clear completed rows
        new_board = [row for row in st.session_state.tetris_board if "⬛" in row]
        cleared_rows = T_ROWS - len(new_board)
        
        if cleared_rows > 0:
            st.session_state.t_score += cleared_rows * 100
            for _ in range(cleared_rows):
                new_board.insert(0, ["⬛" for _ in range(T_COLS)])
            st.session_state.tetris_board = new_board

        # Spawn next shape piece
        st.session_state.current_piece = get_random_piece()
        if check_collision(st.session_state.current_piece):
            st.session_state.t_game_over = True

    def run_tetris_step(action):
        if st.session_state.t_game_over:
            return

        piece = st.session_state.current_piece

        if action == "LEFT" and not check_collision(piece, offset_x=-1):
            piece["x"] -= 1
        elif action == "RIGHT" and not check_collision(piece, offset_x=1):
            piece["x"] += 1
        elif action == "DROP":
            if not check_collision(piece, offset_y=1):
                piece["y"] += 1
            else:
                lock_piece(piece)

    # 1. UI Rendering Container
    game_container = st.empty()

    with game_container.container():
        # Compile Display Frame Framework Layer
        display_board = [row[:] for row in st.session_state.tetris_board]
        if not st.session_state.t_game_over:
            p = st.session_state.current_piece
            for r_idx, row in enumerate(p["matrix"]):
                for c_idx, val in enumerate(row):
                    if val:
                        y_pos = p["y"] + r_idx
                        x_pos = p["x"] + c_idx
                        if 0 <= y_pos < T_ROWS and 0 <= x_pos < T_COLS:
                            display_board[y_pos][x_pos] = p["color"]

        # Draw matrix grid board and score panel
        grid_string = "\n".join([" ".join(row) for row in display_board])
        st.text(grid_string)
        st.write(f"🏆 Score: **{st.session_state.t_score}**")

    # 2. Game Loops Controls Dashboard & Navigation Panel
    if st.session_state.t_game_over:
        st.error("Game Over!")
        if st.button("Play Again", key="reset_tetris_btn"):
            reset_tetris()
            st.rerun()
    else:
        st.write("--- Controls ---")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("◀️ Left", key="t_left"):
                run_tetris_step("LEFT")
                st.rerun()
        with col2:
            if st.button("🔽 Drop Step", key="t_down"):
                run_tetris_step("DROP")
                st.rerun()
        with col3:
            if st.button("Right ▶️", key="t_right"):
                run_tetris_step("RIGHT")
                st.rerun()

        # 3. Automatic Gravity Heartbeat ticker loop 
        # Delays script execution for 1 second, runs a drop frame, then forces a script redraw
        time.sleep(1.0)
        run_tetris_step("DROP")
        st.rerun()
