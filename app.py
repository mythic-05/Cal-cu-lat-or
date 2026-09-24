import streamlit as st
import time

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["Calc which is short for Calculator I'm just using slang", "Calculator", "🐍 Snake"]
)

# -------------------------------------------------------------
# PAGE 1: YOUR ORIGINAL JOKE CALCULATOR
# -------------------------------------------------------------
if app_mode == "Calc which is short for Calculator I'm just using slang":
    st.title("Calc is short for Calculator")
    st.caption("Enter numbers to check database sync status or activate payload triggers.")

    # 1st Number Input
    num1 = st.number_input("1st Number:", value=0.0, step=1.0, key="joke_num1")

    # Custom text triggers for the 1st number
    if num1 == 67:
        st.error("unfunny")
    elif num1 != 0:
        st.info("Number added to database")

    # 2nd Number Input
    num2 = st.number_input("2nd Number:", value=0.0, step=1.0, key="joke_num2")

    # Custom text triggers for the 2nd number
    if num2 == 67:
        st.error("67 in the big 26 🥀")
    elif num2 != 0:
        st.info("Adding...")

    # Action Button
    if st.button("Calculate Result", key="joke_btn"):
        st.subheader("---Result---")
        result = num1 + num2

        # Secret Easter Egg Conditions
        if num1 == 67 and num2 == 67:
            st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly. Its traveling to you there because the missle knows where it is by knowing where it isn't")
        elif num1 == 9 and num2 == 10:
            st.success("🗣️ 21 YOU STUPID")
        else:
            st.success(f"Answer: {result}")


# -------------------------------------------------------------
# PAGE 2: REAL FUNCTIONAL CALCULATOR (SOMETHING USEFUL)
# -------------------------------------------------------------
elif app_mode == "Calculator":
    st.title("🔢 Calculator")
    st.caption("A clean, functional calculator for standard arithmetic and utility math.")

    val1 = st.number_input("First Number (x):", value=0.0, step=0.1, key="pro_val1")
    val2 = st.number_input("Second Number (y):", value=0.0, step=0.1, key="pro_val2")
    
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
            st.success(f"Result: {val1 + val2}")
        elif operation == "Subtraction (-)":
            st.success(f"Result: {val1 - val2}")
        elif operation == "Multiplication (×)":
            st.success(f"Result: {val1 * val2}")
        elif operation == "Power (x^y)":
            st.success(f"Result: {val1 ** val2}")
        elif operation == "Remainder (%)":
            if val2 == 0:
                st.error("Error: Cannot calculate remainder with a divisor of zero.")
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
            else:
                st.success(f"Result: {val1 / val2}")



# -------------------------------------------------------------
# PAGE 3: PLAYABLE SNAKE GAME (INSTANT TURN-BASED REWRITE)
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

    def reset_game():
        st.session_state.snake = [(5, 5), (5, 6), (5, 7)]
        st.session_state.food = (3, 3)
        st.session_state.score = 0
        st.session_state.game_over = False

    # Centralized physics step execution function
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

        # Collision detection checks
        if (head_x < 0 or head_x >= GRID_SIZE or 
            head_y < 0 or head_y >= GRID_SIZE or 
            new_head in st.session_state.snake):
            st.session_state.game_over = True
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
        if st.button("Play Again"):
            reset_game()
            st.rarun = True # Triggers UI refresh safely
            st.rerun()
    else:
        # Visual Arcade Controller Interface
        st.write("--- Controls ---")
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button("🔼 Up"):
                move_snake("UP")
                st.rerun()
        
        col4, col5, col6 = st.columns(3)
        with col4:
            if st.button("◀️ Left"):
                move_snake("LEFT")
                st.rerun()
        with col5:
            st.write("🕹️ D-Pad")
        with col6:
            if st.button("▶️ Right"):
                move_snake("RIGHT")
                st.rerun()
                
            col7, col8, col9 = st.columns(3)
        with col8:
            if st.button("🔽 Down"):
                move_snake("DOWN")
                st.rerun()

