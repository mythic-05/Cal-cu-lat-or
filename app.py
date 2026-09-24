import streamlit as st
import time

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢Calculator", "🐍 Snake", "👾Space Invaders"]
)

# -------------------------------------------------------------
# PAGE 1: REAL FUNCTIONAL CALCULATOR 
# -------------------------------------------------------------
if app_mode == "Calculator":
    st.title("🔢 Calculator")
    st.caption("For those who just joined the stream calc is short for Calculator i'm just using slang")

    val1 = st.number_input("First Number (x):", value=0.0, step=0.1, key="pro_val1")
    
    # Text trigger for the first input number
    if val1 == 67:
        st.error("unfunny")

    val2 = st.number_input("Second Number (y):", value=0.0, step=0.1, key="pro_val2")
    
    # Text trigger for the second input number
    if val2 == 67:
        st.error("67 in the big 26 🥀")
    
    operation = st.selectbox(
        "Select Operation:",
        [
            "Addition (+)", 
            "Subtraction (-)", 
            "Multiplication (×)", 
            "Division (÷)", 
            "Power (x^y)",
            "Remainder (%)",       
            "Absolute Value |x|"   
        ]
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
                # 1. Create a dynamic placeholder for the countdown clock
                countdown_box = st.empty()
                
                # 2. Run the 5-second ticking countdown loop
                for seconds_left in range(5, 0, -1):
                    countdown_box.error(f"Why tf you divide by zero im cooked {seconds_left} SECONDS...")
                    time.sleep(1) # Pause the app for exactly 1 second per tick
                
                # 3. Clear out the countdown box text
                countdown_box.empty()
                
                # 4. Fill the main page layout with a massive wall of explosion emojis
                st.write("# yes rico kabo-💥💥💥💥💥💥")
                st.error("The calculation logic has completely vaporized. Application unusable.")
                
                # Generate a huge wall grid of fire and smoke emoji blocks
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

    # Initialize session state variables
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

    # Centralized physics step execution function
    def move_snake(next_dir):
        if st.session_state.game_over:
            return
            
        head_x, head_y = st.session_state.snake
        if next_dir == "UP": head_y -= 1
        elif next_dir == "DOWN": head_y += 1
        elif next_dir == "LEFT": head_x -= 1
        elif next_dir == "RIGHT": head_x += 1

        new_head = (head_x, head_y)
        GRID_SIZE = 10

        # Collision detection checks
        if (head_x < 0 or head_x >= GRID_SIZE or 
            head_y < 0 or head_y >= GRID_SIZE or 
            new_head in st.session_state.snake):
            st.session_state.game_over = True
            
            # Select the random insult once right at death
            import random
            hints = [
                "Maybe pay attention next time?",
                "Hey idiot the apples over there",
                "Maybe don't spam?",
                "Nice one!",
                "imagine losing in snake lmfao"
            ]
            st.session_state.current_hint = random.choice(hints)
        else:
            st.session_state.snake.insert(0, new_head)
            if new_head == st.session_state.food:
                st.session_state.score += 1
                import random
                st.session_state.food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
            else:
                st.session_state.snake.pop()

    # Render the text-based grid layout screen
    GRID_SIZE = 10
    grid = [["⬜" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    if not st.session_state.game_over:
        fx, fy = st.session_state.food
        grid[fy][fx] = "🍎"
        for i, (sx, sy) in enumerate(st.session_state.snake):
            grid[sy][sx] = "🟩" if i > 0 else "🐲"

    grid_string = "\n".join([" ".join(row) for row in grid])
    st.text(grid_string)
    st.write(f"🏆 Current Score: **{st.session_state.score}**")

    if st.session_state.game_over:
        st.error("Game Over!")
        st.warning(st.session_state.current_hint)
        
        if st.button("Play Again"):
            reset_game()
            st.rerun()
    else:
        # Visual Arcade Controller Interface
        st.write("--- Controls ---")
        
        # Row 1: Up Button
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("🔼 Up"):
                move_snake("UP")
                st.rerun()
        
        # Row 2: Left, D-Pad, Right Buttons
        col4, col5, col6 = st.columns(3)
        with col4:
            if st.button("◀️ Left"):
                move_snake("LEFT")
                st.rerun()
        with col5:
            st.write("D-Pad")
        with col6:
            if st.button("▶️ Right"):
                move_snake("RIGHT")
                st.rerun()
                
        # Row 3: Down Button
        col7, col8, col9 = st.columns(3)
        with col8:
            if st.button("🔽 Down"):
                move_snake("DOWN")
                st.rerun()


st.title("👾 Space Invaders")
st.caption("Move your ship and fire lasers to clear the descending alien fleet!")

# Initialize state variables
if 'player_x' not in st.session_state:
    st.session_state.player_x = 4
    st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]
    st.session_state.lasers = []
    st.session_state.si_score = 0
    st.session_state.si_game_over = False

def run_si_turn(action):
    if st.session_state.si_game_over:
        return

    # 1. Player Action
    if action == "LEFT" and st.session_state.player_x > 0:
        st.session_state.player_x -= 1
    elif action == "RIGHT" and st.session_state.player_x < 9:
        st.session_state.player_x += 1
    elif action == "FIRE":
        st.session_state.lasers.append((st.session_state.player_x, 8))

    # 2. Move Lasers Upward
    new_lasers = []
    for lx, ly in st.session_state.lasers:
        if ly > 0:
            new_lasers.append((lx, ly - 1))
    st.session_state.lasers = new_lasers

    # 3. Collision Logic (Laser hits Invader)
    remaining_invaders = []
    for ix, iy in st.session_state.invaders:
        hit = False
        for lx, ly in st.session_state.lasers:
            if lx == ix and ly == iy:
                hit = True
                st.session_state.lasers.remove((lx, ly))
                st.session_state.si_score += 10
                break
        if not hit:
            remaining_invaders.append((ix, iy))
    st.session_state.invaders = remaining_invaders

    # 4. Automate Invader Descent (Random chance each step)
    import random
    if random.random() < 0.35 and len(st.session_state.invaders) > 0:
        new_invaders = []
        for ix, iy in st.session_state.invaders:
            if iy + 1 >= 9:
                st.session_state.si_game_over = True
            new_invaders.append((ix, iy + 1))
        st.session_state.invaders = new_invaders

    # Victory check
    if len(st.session_state.invaders) == 0:
        # Spawn fresh tougher wave
        st.session_state.invaders = [(1, 1), (3, 1), (5, 1), (7, 1), (2, 2), (4, 2), (6, 2)]

# Draw Grid Screen
si_grid = [["⬛" for _ in range(10)] for _ in range(10)]
if not st.session_state.si_game_over:
    for ix, iy in st.session_state.invaders:
        si_grid[iy][ix] = "🛸"
    for lx, ly in st.session_state.lasers:
        si_grid[ly][lx] = "⚡"
    si_grid[9][st.session_state.player_x] = "🚀"

st.text("\n".join([" ".join(row) for row in si_grid]))
st.write(f"🏆 Score: **{st.session_state.si_score}**")

if st.session_state.si_game_over:
    st.error("Your ship was overrun!")
    if st.button("Respawn Fleet"):
        del st.session_state.player_x
        st.rerun()
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("◀️ Move Left"):
            run_si_turn("LEFT"); st.rerun()
    with col2:
        if st.button("🔥 Fire Laser"):
            run_si_turn("FIRE"); st.rerun()
    with col3:
        if st.button("Move Right ▶️"):
            run_si_turn("RIGHT"); st.rerun()


