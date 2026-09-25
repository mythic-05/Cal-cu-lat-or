import streamlit as st
import time
import streamlit.components.v1 as components

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="Web Arcade", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "👾 Space Invaders", "🕹️ Tetris", "🦖 T-Rex Run"]
)

# -------------------------------------------------------------
# PAGE 1: REAL FUNCTIONAL CALCULATOR (Python-Native)
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
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly.")
            else:
                st.success(f"Result: {val1 + val2}")
        elif operation == "Subtraction (-)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly.")
            else:
                st.success(f"Result: {val1 - val2}")
        elif operation == "Multiplication (×)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly.")
            else:
                st.success(f"Result: {val1 * val2}")
        elif operation == "Division (÷)":
            if val2 == 0:
                countdown_box = st.empty()
                for seconds_left in range(5, 0, -1):
                    countdown_box.error(f"Why tf you divide by zero im cooked {seconds_left} SECONDS...")
                    time.sleep(1) 
                countdown_box.empty()
                st.write("# yes rico kabo-💥💥💥💥💥💥")
                st.error("The calculation logic has completely vaporized.")
            else:
                st.success(f"Result: {val1 / val2}")

# -------------------------------------------------------------
# BROWSER-NATIVE GAME ENGINE LOADER
# -------------------------------------------------------------
else:
    # Embedded high-performance client-side logic codes
    games = {
        "🐍 Snake": """
            <style>canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; } h1,p {color:white; text-align:center; font-family:sans-serif;}</style>
            <h1>🐍 Snake Game</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="400" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let grid = 20, snake = [{x:160,y:160},{x:140,y:160}], dx = grid, dy = 0, score = 0;
            let food = {x: 80, y: 80};
            function main() {
                if (gameOver()) return alert('Game Over! Score: ' + score);
                setTimeout(function() { clear(); drawFood(); move(); drawSnake(); main(); }, 100);
            }
            function clear() { ctx.fillStyle = '#111'; ctx.fillRect(0,0,canvas.width,canvas.height); }
            function drawSnake() { ctx.fillStyle = 'lime'; snake.forEach(s => ctx.fillRect(s.x, s.y, grid-2, grid-2)); }
            function move() {
                const head = {x: snake[0].x + dx, y: snake[0].y + dy};
                snake.unshift(head);
                if(head.x === food.x && head.y === food.y) {
                    score += 10; document.getElementById('score').innerText = 'Score: ' + score;
                    food = {x: Math.floor(Math.random()*20)*grid, y: Math.floor(Math.random()*20)*grid};
                } else snake.pop();
            }
            function drawFood() { ctx.fillStyle = 'red'; ctx.fillRect(food.x, food.y, grid-2, grid-2); }
            function gameOver() {
                const h = snake[0];
                return h.x<0||h.x>=canvas.width||h.y<0||h.y>=canvas.height||snake.slice(1).some(s=>s.x===h.x&&s.y===h.y);
            }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowUp'&&dy===0){dx=0;dy=-grid;} if(e.key==='ArrowDown'&&dy===0){dx=0;dy=grid;}
                if(e.key==='ArrowLeft'&&dx===0){dx=-grid;dy=0;} if(e.key==='ArrowRight'&&dx===0){dx=grid;dy=0;}
            });
            main();
            </script>
        """,
        "👾 Space Invaders": """
            <style>canvas { background: #000; display: block; margin: auto; border: 4px solid #fff; } h1,p {color:white; text-align:center; font-family:sans-serif;}</style>
            <h1>👾 Space Invaders</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="400" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let player = {x: 180, y: 360, w: 30, h: 20}, lasers = [], invaders = [], score = 0;
            for(let i=0; i<6; i++) for(let j=0; j<3; j++) invaders.push({x: 40+i*50, y: 30+j*30, w:25, h:20});
            function loop() {
                ctx.clearRect(0,0,400,400); ctx.fillStyle='blue'; ctx.fillRect(player.x, player.y, player.w, player.h);
                ctx.fillStyle='red'; invaders.forEach(inv => ctx.fillRect(inv.x, inv.y, inv.w, inv.h));
                ctx.fillStyle='yellow'; lasers.forEach((l,li) => { l.y-=5; ctx.fillRect(l.x, l.y, 4, 10); if(l.y<0) lasers.splice(li,1); });
                lasers.forEach((l,li) => { invaders.forEach((inv,ii) => {
                    if(l.x>inv.x && l.x<inv.x+inv.w && l.y>inv.y && l.y<inv.y+inv.h) { invaders.splice(ii,1); lasers.splice(li,1); score+=10; document.getElementById('score').innerText = 'Score: ' + score; }
                })});
                if(invaders.length === 0) return alert('You Win!');
                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowLeft' && player.x>0) player.x-=15;
                if(e.key==='ArrowRight' && player.x<370) player.x+=15;
                if(e.key===' ') lasers.push({x: player.x+13, y: player.y});
            });
            loop();
            </script>
        """,
        "🕹️ Tetris": """
            <style>canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; } h1 {color:white; text-align:center; font-family:sans-serif;}</style>
            <h1>🕹️ Client-Side Tetris</h1>
            <canvas id="game" width="240" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            ctx.scale(20, 20);
            const arena = Array(20).fill().map(() => Array(12).fill(0));
            const player = { pos: {x: 5, y: 0}, matrix: [[0,1,0],[1,1,1],[0,0,0]] };
            function draw() { ctx.fillStyle='#111'; ctx.fillRect(0,0,canvas.width,canvas.height); drawMatrix(arena, {x:0, y:0}); drawMatrix(player.matrix, player.pos); }
            function drawMatrix(m, o) { m.forEach((row, y) => row.forEach((val, x) => { if(val) { ctx.fillStyle='red'; ctx.fillRect(x + o.x, y + o.y, 1, 1); } })); }
            let dropCounter = 0; function update(time = 0) { dropCounter += 16; if(dropCounter > 1000) { player.pos.y++; dropCounter=0; } draw(); requestAnimationFrame(update); }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowLeft') player.pos.x--; if(e.key==='ArrowRight') player.pos.x++; if(e.key==='ArrowDown') player.pos.y++;
            });
            update();
            </script>
        """,
        "🦖 T-Rex Run": """
            <style>canvas { background: #f7f7f7; display: block; margin: auto; border: 2px solid #333; } h1,p {color:#333; text-align:center; font-family:sans-serif;}</style>
            <h1>🦖 T-Rex Run</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="600" height="150"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let dino = {y: 130, vy: 0, isJumping: false}, obstacles = [{x: 600}], score = 0;
            function loop() {
                ctx.clearRect(0,0,600,150); score++; document.getElementById('score').innerText = 'Score: ' + score;
                if(dino.isJumping) { dino.vy += 0.6; dino.y += dino.vy; if(dino.y >= 130) { dino.y = 130; dino.isJumping = false; } }
                ctx.fillStyle='#333'; ctx.fillRect(50, dino.y-20, 20, 20); // Dino
                obstacles.forEach((o, i) => { o.x -= 5; ctx.fillRect(o.x, 110, 15, 40); if(o.x < -15) obstacles[i] = {x: 600 + Math.random()*300}; 
                    if(o.x > 50 && o.x < 70 && dino.y >= 110) { alert('Game Over!'); score=0; o.x=600; }
                });
                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => { if((e.key===' ' || e.key==='ArrowUp') && !dino.isJumping) { dino.vy = -12; dino.isJumping = true; } });
            loop();
            </script>
        """
    }

    # Display game instantly inside native sandbox with absolutely no backend delays
    st.title(app_mode)
    components.html(games[app_mode], height=500)import streamlit as st
import time
import streamlit.components.v1 as components

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="Web Arcade", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "👾 Space Invaders", "🕹️ Tetris", "🦖 T-Rex Run"]
)

# -------------------------------------------------------------
# PAGE 1: REAL FUNCTIONAL CALCULATOR (Python-Native)
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
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly.")
            else:
                st.success(f"Result: {val1 + val2}")
        elif operation == "Subtraction (-)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly.")
            else:
                st.success(f"Result: {val1 - val2}")
        elif operation == "Multiplication (×)":
            if val1 == 67 and val2 == 67:
                st.error("Fuck you now theres a Tactical Nuke arriving to your location rapidly.")
            else:
                st.success(f"Result: {val1 * val2}")
        elif operation == "Division (÷)":
            if val2 == 0:
                countdown_box = st.empty()
                for seconds_left in range(5, 0, -1):
                    countdown_box.error(f"Why tf you divide by zero im cooked {seconds_left} SECONDS...")
                    time.sleep(1) 
                countdown_box.empty()
                st.write("# yes rico kabo-💥💥💥💥💥💥")
                st.error("The calculation logic has completely vaporized.")
            else:
                st.success(f"Result: {val1 / val2}")

# -------------------------------------------------------------
# BROWSER-NATIVE GAME ENGINE LOADER
# -------------------------------------------------------------
else:
    # Embedded high-performance client-side logic codes
    games = {
        "🐍 Snake": """
            <style>canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; } h1,p {color:white; text-align:center; font-family:sans-serif;}</style>
            <h1>🐍 Snake Game</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="400" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let grid = 20, snake = [{x:160,y:160},{x:140,y:160}], dx = grid, dy = 0, score = 0;
            let food = {x: 80, y: 80};
            function main() {
                if (gameOver()) return alert('Game Over! Score: ' + score);
                setTimeout(function() { clear(); drawFood(); move(); drawSnake(); main(); }, 100);
            }
            function clear() { ctx.fillStyle = '#111'; ctx.fillRect(0,0,canvas.width,canvas.height); }
            function drawSnake() { ctx.fillStyle = 'lime'; snake.forEach(s => ctx.fillRect(s.x, s.y, grid-2, grid-2)); }
            function move() {
                const head = {x: snake[0].x + dx, y: snake[0].y + dy};
                snake.unshift(head);
                if(head.x === food.x && head.y === food.y) {
                    score += 10; document.getElementById('score').innerText = 'Score: ' + score;
                    food = {x: Math.floor(Math.random()*20)*grid, y: Math.floor(Math.random()*20)*grid};
                } else snake.pop();
            }
            function drawFood() { ctx.fillStyle = 'red'; ctx.fillRect(food.x, food.y, grid-2, grid-2); }
            function gameOver() {
                const h = snake[0];
                return h.x<0||h.x>=canvas.width||h.y<0||h.y>=canvas.height||snake.slice(1).some(s=>s.x===h.x&&s.y===h.y);
            }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowUp'&&dy===0){dx=0;dy=-grid;} if(e.key==='ArrowDown'&&dy===0){dx=0;dy=grid;}
                if(e.key==='ArrowLeft'&&dx===0){dx=-grid;dy=0;} if(e.key==='ArrowRight'&&dx===0){dx=grid;dy=0;}
            });
            main();
            </script>
        """,
        "👾 Space Invaders": """
            <style>canvas { background: #000; display: block; margin: auto; border: 4px solid #fff; } h1,p {color:white; text-align:center; font-family:sans-serif;}</style>
            <h1>👾 Space Invaders</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="400" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let player = {x: 180, y: 360, w: 30, h: 20}, lasers = [], invaders = [], score = 0;
            for(let i=0; i<6; i++) for(let j=0; j<3; j++) invaders.push({x: 40+i*50, y: 30+j*30, w:25, h:20});
            function loop() {
                ctx.clearRect(0,0,400,400); ctx.fillStyle='blue'; ctx.fillRect(player.x, player.y, player.w, player.h);
                ctx.fillStyle='red'; invaders.forEach(inv => ctx.fillRect(inv.x, inv.y, inv.w, inv.h));
                ctx.fillStyle='yellow'; lasers.forEach((l,li) => { l.y-=5; ctx.fillRect(l.x, l.y, 4, 10); if(l.y<0) lasers.splice(li,1); });
                lasers.forEach((l,li) => { invaders.forEach((inv,ii) => {
                    if(l.x>inv.x && l.x<inv.x+inv.w && l.y>inv.y && l.y<inv.y+inv.h) { invaders.splice(ii,1); lasers.splice(li,1); score+=10; document.getElementById('score').innerText = 'Score: ' + score; }
                })});
                if(invaders.length === 0) return alert('You Win!');
                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowLeft' && player.x>0) player.x-=15;
                if(e.key==='ArrowRight' && player.x<370) player.x+=15;
                if(e.key===' ') lasers.push({x: player.x+13, y: player.y});
            });
            loop();
            </script>
        """,
        "🕹️ Tetris": """
            <style>canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; } h1 {color:white; text-align:center; font-family:sans-serif;}</style>
            <h1>🕹️ Client-Side Tetris</h1>
            <canvas id="game" width="240" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            ctx.scale(20, 20);
            const arena = Array(20).fill().map(() => Array(12).fill(0));
            const player = { pos: {x: 5, y: 0}, matrix: [[0,1,0],[1,1,1],[0,0,0]] };
            function draw() { ctx.fillStyle='#111'; ctx.fillRect(0,0,canvas.width,canvas.height); drawMatrix(arena, {x:0, y:0}); drawMatrix(player.matrix, player.pos); }
            function drawMatrix(m, o) { m.forEach((row, y) => row.forEach((val, x) => { if(val) { ctx.fillStyle='red'; ctx.fillRect(x + o.x, y + o.y, 1, 1); } })); }
            let dropCounter = 0; function update(time = 0) { dropCounter += 16; if(dropCounter > 1000) { player.pos.y++; dropCounter=0; } draw(); requestAnimationFrame(update); }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowLeft') player.pos.x--; if(e.key==='ArrowRight') player.pos.x++; if(e.key==='ArrowDown') player.pos.y++;
            });
            update();
            </script>
        """,
        "🦖 T-Rex Run": """
            <style>canvas { background: #f7f7f7; display: block; margin: auto; border: 2px solid #333; } h1,p {color:#333; text-align:center; font-family:sans-serif;}</style>
            <h1>🦖 T-Rex Run</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="600" height="150"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let dino = {y: 130, vy: 0, isJumping: false}, obstacles = [{x: 600}], score = 0;
            function loop() {
                ctx.clearRect(0,0,600,150); score++; document.getElementById('score').innerText = 'Score: ' + score;
                if(dino.isJumping) { dino.vy += 0.6; dino.y += dino.vy; if(dino.y >= 130) { dino.y = 130; dino.isJumping = false; } }
                ctx.fillStyle='#333'; ctx.fillRect(50, dino.y-20, 20, 20); // Dino
                obstacles.forEach((o, i) => { o.x -= 5; ctx.fillRect(o.x, 110, 15, 40); if(o.x < -15) obstacles[i] = {x: 600 + Math.random()*300}; 
                    if(o.x > 50 && o.x < 70 && dino.y >= 110) { alert('Game Over!'); score=0; o.x=600; }
                });
                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => { if((e.key===' ' || e.key==='ArrowUp') && !dino.isJumping) { dino.vy = -12; dino.isJumping = true; } });
            loop();
            </script>
        """
    }

    # Display game instantly inside native sandbox with absolutely no backend delays
    st.title(app_mode)
    components.html(games[app_mode], height=500)
