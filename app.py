import streamlit as st
import time
import random
import streamlit.components.v1 as components

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="Web Arcade", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "👾 Space Invaders", "🕹️Tetris", "🍕 Pac-Man"]
)


# -------------------------------------------------------------
# BROWSER KEYBOARD ENGINE
# -------------------------------------------------------------
def inject_keyboard_engine(key_mapping):
    """
    Injects an isolated browser-level listener. Maps keystrokes safely 
    to specific uniquely-keyed buttons on the active page.
    """
    js_code = f"""
    <script>
    const doc = window.parent.document;
    doc.onkeydown = function(e) {{
        let keyMap = {key_mapping};
        if (e.key in keyMap) {{
            let buttons = Array.from(doc.querySelectorAll('button'));
            let targetBtn = buttons.find(el => el.innerText.trim().includes(keyMap[e.key]));
            if (targetBtn) {{
                e.preventDefault();
                targetBtn.click();
            }}
        }}
    }};
    </script>
    """
    components.html(js_code, height=0, width=0)


# -------------------------------------------------------------
# PAGE 1: REAL FUNCTIONAL CALCULATOR 
# -------------------------------------------------------------
if app_mode == "🔢 Calculator":
    st.title("🔢 Calculator")
    st.caption("For those who just joined the stream calc is short for Calculator i'm just using slang")

    val1 = st.number_input("First Number (x):", value=0.0, step=0.1, key="calc_val1")
    if val1 == 67:
        st.error("unfunny")

    val2 = st.number_input("Second Number (y):", value=0.0, step=0.1, key="calc_val2")
    if val2 == 67:
        st.error("67 in the big 26 🥀")
    
    operation = st.selectbox(
        "Select Operation:",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (x^y)", "Remainder (%)", "Absolute Value |x|"],
        key="calc_operation"
    )

    if st.button("Compute Result", key="calc_btn_compute"):
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
    st.title("🐍 Snake")
    st.caption("Eat the apples and get fat.")

    inject_keyboard_engine({
        "ArrowUp": "Up", "w": "Up", "W": "Up",
        "ArrowDown": "Down", "s": "Down", "S": "Down",
        "ArrowLeft": "Left", "a": "Left", "A": "Left",
        "ArrowRight": "Right", "d": "Right", "D": "Right"
    })

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

    snake_controls = st.container()
    if st.session_state.game_over:
        st.error("Game Over!")
        st.warning(st.session_state.current_hint)
        if st.button("Play Again", key="snake_btn_retry"):
            reset_game()
            st.rerun()
    else:
        with snake_controls:
            st.write("--- Controls ---")
            s_col1, s_col2, s_col3 = st.columns(3)
            with s_col2:
                if st.button("🔼 Up", key="snake_b_up"):
                    move_snake("UP"); st.rerun()
            s_col4, s_col5, s_col6 = st.columns(3)
            with s_col4:
                if st.button("◀️ Left", key="snake_b_left"):
                    move_snake("LEFT"); st.rerun()
            with s_col5:
                st.write("D-Pad")
            with s_col6:
                if st.button("▶️ Right", key="snake_b_right"):
                    move_snake("RIGHT"); st.rerun()
            s_col7, s_col8, s_col9 = st.columns(3)
            with s_col8:
                if st.button("🔽 Down", key="snake_b_down"):
                    move_snake("DOWN"); st.rerun()


# -------------------------------------------------------------
# PAGE 3: PLAYABLE SPACE INVADERS
# -------------------------------------------------------------
elif app_mode == "👾 Space Invaders":
    st.title("👾 Space Invaders")
    st.caption("Arrow Left/Right to slide, Spacebar to shoot!")

    inject_keyboard_engine({
        "ArrowLeft": "Move Left", "a": "Move Left", "A": "Move Left",
        "ArrowRight": "Move Right", "d": "Move Right", "D": "Move Right",
        " ": "Fire Laser"
    })

    if 'player_x' not in st.session_state:
        st.session_state.player_x = 4
        st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]
        st.session_state.si_score = 0
        st.session_state.active_laser = None  
        st.session_state.si_game_over = False

    def draw_and_render_grid():
        si_grid = [["⬛" for _ in range(10)] for _ in range(10)]
        if not st.session_state.si_game_over:
            for ix, iy in st.session_state.invaders:
                si_grid[iy][ix] = "🛸"
            if st.session_state.active_laser:
                lx, ly = st.session_state.active_laser
                si_grid[ly][lx] = "⚡"
            si_grid[9][st.session_state.player_x] = "🚀"
        return "\n".join([" ".join(row) for row in si_grid])

    grid_placeholder = st.empty()
    score_placeholder = st.empty()

    def run_si_turn(action):
        if st.session_state.si_game_over:
            return

        if action == "LEFT" and st.session_state.player_x > 0:
            st.session_state.player_x -= 1
        elif action == "RIGHT" and st.session_state.player_x < 9:
            st.session_state.player_x += 1
        elif action == "FIRE":
            if st.session_state.active_laser is None:
                lx = st.session_state.player_x
                ly = 9
                while ly > 0:
                    ly -= 1
                    st.session_state.active_laser = (lx, ly)
                    if (lx, ly) in st.session_state.invaders:
                        st.session_state.invaders.remove((lx, ly))
                        st.session_state.si_score += 10
                        st.session_state.active_laser = None
                        break
                    grid_placeholder.text(draw_and_render_grid())
                    score_placeholder.write(f"🏆 Score: **{st.session_state.si_score}**")
                    time.sleep(0.008)
                st.session_state.active_laser = None

        if random.random() < 0.35 and len(st.session_state.invaders) > 0:
            new_invaders = []
            for ix, iy in st.session_state.invaders:
                if iy + 1 >= 9:
                    st.session_state.si_game_over = True
                new_invaders.append((ix, iy + 1))
            st.session_state.invaders = new_invaders

        if len(st.session_state.invaders) == 0:
            st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]

    grid_placeholder.text(draw_and_render_grid())
    score_placeholder.write(f"🏆 Score: **{st.session_state.si_score}**")

    si_controls = st.container()
    if st.session_state.si_game_over:
        st.error("Your ship was overrun!")
        if st.button("Respawn Fleet", key="si_btn_retry"):
            del st.session_state.player_x
            st.rerun()
    else:
        with si_controls:
            si_col1, si_col2, si_col3 = st.columns(3)
            with si_col1:
                if st.button("◀️ Move Left", key="si_b_left"):
                    run_si_turn("LEFT")
                    st.rerun()
            with si_col2:
                if st.button("🔥 Fire Laser", key="si_b_fire"):
                    run_si_turn("FIRE")
                    st.rerun()
            with si_col3:
                if st.button("Move Right ▶️", key="si_b_right"):
                    run_si_turn("RIGHT")
                    st.rerun()


# -------------------------------------------------------------
# PAGE 4: PLAYABLE TETRIS
# -------------------------------------------------------------
elif app_mode == "🕹️Tetris":
    st.title("🕹️Tetris")
    st.caption("Arrow Left/Right to slide, Arrow Up or W to Rotate!")

    inject_keyboard_engine({
        "ArrowLeft": "Left", "a": "Left", "A": "Left",
        "ArrowRight": "Right", "d": "Right", "D": "Right",
        "ArrowUp": "Rotate", "w": "Rotate", "W": "Rotate"
    })

    T_ROWS, T_COLS = 12, 8
    
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

    def check_collision(piece, offset_x=0, offset_y=0, test_matrix=None):
        matrix = test_matrix if test_matrix is not None else piece["matrix"]
        for r_idx, row in enumerate(matrix):
            for c_idx, val in enumerate(row):
                if val:
                    new_x = piece["x"] + c_idx + offset_x
                    new_y = piece["y"] + r_idx + offset_y
                    if new_x < 0 or new_x >= T_COLS or new_y >= T_ROWS:
                        return True
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

        new_board = [row for row in st.session_state.tetris_board if "⬛" in row]
        cleared_rows = T_ROWS - len(new_board)
        
        if cleared_rows > 0:
            st.session_state.t_score += cleared_rows * 100
            for _ in range(cleared_rows):
                new_board.insert(0, ["⬛" for _ in range(T_COLS)])
            st.session_state.tetris_board = new_board

        st.session_state.current_piece = get_random_piece()
        if check_collision(st.session_state.current_piece):
            st.session_state.t_game_over = True

    def rotate_matrix(matrix):
        return [list(x) for x in zip(*matrix[::-1])]

    def run_tetris_step(action):
        if st.session_state.t_game_over:
            return
        piece = st.session_state.current_piece
        if action == "LEFT" and not check_collision(piece, offset_x=-1):
            piece["x"] -= 1
        elif action == "RIGHT" and not check_collision(piece, offset_x=1):
            piece["x"] += 1
        elif action == "ROTATE":
            rotated = rotate_matrix(piece["matrix"])
            if not check_collision(piece, offset_x=0, offset_y=0, test_matrix=rotated):
                piece["matrix"] = rotated
        elif action == "DROP":
            if not check_collision(piece, offset_y=1):
                piece["y"] += 1
            else:
                lock_piece(piece)

    grid_placeholder = st.empty()
    score_placeholder = st.empty()
    tetris_controls = st.container()

    if st.session_state.t_game_over:
        grid_placeholder.empty()
        score_placeholder.write(f"🏆 Final Score: **{st.session_state.t_score}**")
        with tetris_controls:
            st.error("Game Over!")
            if st.button("Play Again", key="tetris_btn_retry"):
                reset_tetris()
                st.rerun()
    else:
        display_board = [row[:] for row in st.session_state.tetris_board]
        p = st.session_state.current_piece
        for r_idx, row in enumerate(p["matrix"]):
            for c_idx, val in enumerate(row):
                if val:
                    y_pos = p["y"] + r_idx
                    x_pos = p["x"] + c_idx
                    if 0 <= y_pos < T_ROWS and 0 <= x_pos < T_COLS:
                        display_board[y_pos][x_pos] = p["color"]

        grid_string = "\n".join([" ".join(row) for row in display_board])
        grid_placeholder.text(grid_string)
        score_placeholder.write(f"🏆 Score: **{st.session_state.t_score}**")

        with tetris_controls:
            st.write("--- Controls ---")
            t_col1, t_col2, t_col3 = st.columns(3)
            with t_col1:
                if st.button("◀️ Left", key="t_b_left"):
                    run_tetris_step("LEFT")
                    st.rerun()
            with t_col2:
                if st.button("🔄 Rotate", key="t_b_rotate"):
                    run_tetris_step("ROTATE")
                    st.rerun()
            with t_col3:
                if st.button("Right ▶️", key="t_b_right"):
                    run_tetris_step("RIGHT")
                    st.rerun()

        time.sleep(0.300)
        run_tetris_step("DROP")
        st.rerun()



# -------------------------------------------------------------
# PAGE 5: PLAYABLE PAC-MAN (FOUR CIRCLE GHOSTS)
# -------------------------------------------------------------
elif app_mode == "🍕 Pac-Man":
    st.title("🍕 Pac-Man")
    st.caption("Escape all 4 ghosts and eat pellets!")

    inject_keyboard_engine({
        "ArrowUp": "Up", "w": "Up", "W": "Up",
        "ArrowDown": "Down", "s": "Down", "S": "Down",
        "ArrowLeft": "Left", "a": "Left", "A": "Left",
        "ArrowRight": "Right", "d": "Right", "D": "Right"
    })

    # Fixed 9x9 Maze Layout Grid (1 = Wall, 0 = Open Path with Dot)
    PAC_MAZE = [,
 ,
 ,
 ,
 ,
 ,
 ,
 ,
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    M_ROWS, M_COLS = 9, 9

    # Game State Session Engine Initializer
    if 'pac_x' not in st.session_state:
        st.session_state.pac_x = 1
        st.session_state.pac_y = 1
        st.session_state.pac_face = "😮"  # Dynamic tracking face
        st.session_state.ghosts = [
            {"x": 7, "y": 7, "icon": "🔴", "type": "blinky"},  # Blinky: Red Circle
            {"x": 1, "y": 7, "icon": "🌸", "type": "pinky"},   # Pinky: Pink Circle/Flower
            {"x": 7, "y": 1, "icon": "🔵", "type": "inky"},    # Inky: Blue Circle
            {"x": 3, "y": 3, "icon": "🟠", "type": "clyde"}    # Clyde: Orange Circle
        ]
        st.session_state.dots = [(r, c) for r in range(M_ROWS) for c in range(M_COLS) if PAC_MAZE[r][c] == 0]
        st.session_state.pac_score = 0
        st.session_state.pac_game_over = False
        st.session_state.pac_victory = False

    def reset_pacman():
        st.session_state.pac_x = 1
        st.session_state.pac_y = 1
        st.session_state.pac_face = "😮"
        st.session_state.ghosts = [
            {"x": 7, "y": 7, "icon": "🔴", "type": "blinky"},
            {"x": 1, "y": 7, "icon": "🌸", "type": "pinky"},
            {"x": 7, "y": 1, "icon": "🔵", "type": "inky"},
            {"x": 3, "y": 3, "icon": "🟠", "type": "clyde"}
        ]
        st.session_state.dots = [(r, c) for r in range(M_ROWS) for c in range(M_COLS) if PAC_MAZE[r][c] == 0]
        st.session_state.pac_score = 0
        st.session_state.pac_game_over = False
        st.session_state.pac_victory = False

    def run_pacman_turn(direction):
        if st.session_state.pac_game_over or st.session_state.pac_victory:
            return

        # 1. Animate Pac-Man's Face based on movement direction
        if direction in ["UP", "DOWN"]:
            st.session_state.pac_face = "😲" if st.session_state.pac_face == "😮" else "😮"
        elif direction in ["LEFT", "RIGHT"]:
            st.session_state.pac_face = "😋" if st.session_state.pac_face == "😮" else "😮"

        # 2. Process Pac-Man Movement
        next_x, next_y = st.session_state.pac_x, st.session_state.pac_y
        if direction == "UP": next_y -= 1
        elif direction == "DOWN": next_y += 1
        elif direction == "LEFT": next_x -= 1
        elif direction == "RIGHT": next_x += 1

        # Move if destination path is open
        if 0 <= next_y < M_ROWS and 0 <= next_x < M_COLS:
            if PAC_MAZE[next_y][next_x] != 1:
                st.session_state.pac_x = next_x
                st.session_state.pac_y = next_y

        # Score pellet ingestion mapping
        current_loc = (st.session_state.pac_y, st.session_state.pac_x)
        if current_loc in st.session_state.dots:
            st.session_state.dots.remove(current_loc)
            st.session_state.pac_score += 10

        # Victory check
        if len(st.session_state.dots) == 0:
            st.session_state.pac_victory = True
            return

        # 3. Process Ghost Personalities AI Engine
        px, py = st.session_state.pac_x, st.session_state.pac_y
        for ghost in st.session_state.ghosts:
            gx, gy = ghost["x"], ghost["y"]
            possible_moves = []

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = gx + dx, gy + dy
                if 0 <= ny < M_ROWS and 0 <= nx < M_COLS and PAC_MAZE[ny][nx] != 1:
                    possible_moves.append((nx, ny))

            if possible_moves:
                if ghost["type"] == "blinky":
                    # Directly chases Pac-Man position
                    best_move = min(possible_moves, key=lambda m: abs(m[0]-px) + abs(m[1]-py))
                elif ghost["type"] == "pinky":
                    # Tries to ambush 2 steps ahead of Pac-Man direction
                    target_x = px + 2 if direction == "RIGHT" else (px - 2 if direction == "LEFT" else px)
                    target_y = py + 2 if direction == "DOWN" else (py - 2 if direction == "UP" else py)
                    best_move = min(possible_moves, key=lambda m: abs(m[0]-target_x) + abs(m[1]-target_y))
                elif ghost["type"] == "clyde":
                    # Chases if far away, runs to bottom-left corner if closer than 4 spaces
                    dist = abs(gx-px) + abs(gy-py)
                    if dist > 4:
                        best_move = min(possible_moves, key=lambda m: abs(m[0]-px) + abs(m[1]-py))
                    else:
                        best_move = min(possible_moves, key=lambda m: abs(m[0]-1) + abs(m[1]-7))
                else:
                    # Inky: Random selection
                    best_move = random.choice(possible_moves)

                ghost["x"], ghost["y"] = best_move[0], best_move[1]

        # Post-movement game over impact collision check
        for ghost in st.session_state.ghosts:
            if ghost["x"] == st.session_state.pac_x and ghost["y"] == st.session_state.pac_y:
                st.session_state.pac_game_over = True

    # Render Visual Layer Blocks
    grid_placeholder = st.empty()
    score_placeholder = st.empty()
    controls_placeholder = st.empty()

    if st.session_state.pac_game_over:
        grid_placeholder.empty()
        score_placeholder.write(f"🏆 Final Score: **{st.session_state.pac_score}**")
        with controls_placeholder:
            st.error("Waka Waka... Caught by a Ghost! Game Over.")
            if st.button("Play Again", key="pac_retry_lost"):
                reset_pacman(); st.rerun()
    elif st.session_state.pac_victory:
        grid_placeholder.empty()
        score_placeholder.write(f"🏆 High Score: **{st.session_state.pac_score}**")
        with controls_placeholder:
            st.success("🎉 Victory! You cleared the maze and beat the ghosts!")
            if st.button("Play Again", key="pac_retry_win"):
                reset_pacman(); st.rerun()
    else:
        # Construct current frame layer grid
        display_grid = [["🟦" if cell == 1 else "🔸" for cell in row] for row in PAC_MAZE]
        
        # Erase dots from map layer if consumed
        for r in range(M_ROWS):
            for c in range(M_COLS):
                if PAC_MAZE[r][c] == 0 and (r, c) not in st.session_state.dots:
                    display_grid[r][c] = "⬛"

        # Overlay active target sprites safely
        for ghost in st.session_state.ghosts:
            display_grid[ghost["y"]][ghost["x"]] = ghost["icon"]
            
        # Draw Pac-Man on top layer
        display_grid[st.session_state.pac_y][st.session_state.pac_x] = st.session_state.pac_face

        grid_placeholder.text("\n".join([" ".join(row) for row in display_grid]))
        score_placeholder.write(f"🏆 Score: **{st.session_state.pac_score}** | 🔸 Remaining Pellets: **{len(st.session_state.dots)}**")

        # Static D-Pad Control Dashboard
        with controls_placeholder:
            st.write("--- Controls ---")
            p_col1, p_col2, p_col3 = st.columns(3)
            with p_col2:
                if st.button("🔼 Up", key="pac_b_up"):
                    run_pacman_turn("UP"); st.rerun()
            p_col4, p_col5, p_col6 = st.columns(3)
            with p_col4:
                if st.button("◀️ Left", key="pac_b_left"):
                    run_pacman_turn("LEFT"); st.rerun()
            with p_col5:
                st.write("D-Pad")
            with p_col6:
                if st.button("▶️ Right", key="pac_b_right"):
                    run_pacman_turn("RIGHT"); st.rerun()
            p_col7, p_col8, p_col9 = st.columns(3)
            with p_col8:
                if st.button("🔽 Down", key="pac_b_down"):
                    run_pacman_turn("DOWN"); st.rerun()
