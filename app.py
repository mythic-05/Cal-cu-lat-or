import streamlit as st
import time
import streamlit.components.v1 as components

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="Web Arcade", layout="centered")

# Sidebar navigation menu
st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "🟓 Pong", "🕹️Tetris", "🦖 T-Rex Run"]
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
# BROWSER-NATIVE GAME ENGINE LOADER (Zero-Delay JavaScript Canvas)
# -------------------------------------------------------------
else:
    games = {
        "🐍 Snake": """
            <style>
                canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; } 
                h1, p { color: white; text-align: center; font-family: sans-serif; }
            </style>
            <h1>🐍 Snake Game</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="400" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let grid = 20, score = 0;
            let snake = [{x: 160, y: 160}, {x: 140, y: 160}, {x: 120, y: 160}];
            let dx = grid, dy = 0;
            let food = {x: 80, y: 80};

            function main() {
                if (gameOver()) {
                    alert('Game Over! Score: ' + score);
                    resetGame();
                }
                setTimeout(function() { clear(); drawFood(); move(); drawSnake(); main(); }, 150);
            }
            function resetGame() {
                snake = [{x: 160, y: 160}, {x: 140, y: 160}, {x: 120, y: 160}];
                dx = grid; dy = 0; score = 0;
                document.getElementById('score').innerText = 'Score: ' + score;
                food = {x: 80, y: 80};
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
                const wallCollision = h.x < 0 || h.x >= canvas.width || h.y < 0 || h.y >= canvas.height;
                let selfCollision = false;
                for(let i = 1; i < snake.length; i++) {
                    if(snake[i].x === h.x && snake[i].y === h.y) selfCollision = true;
                }
                return wallCollision || selfCollision;
            }
            window.addEventListener('keydown', e => {
                const key = e.key.toLowerCase();
                if((e.key==='ArrowUp' || key==='w') && dy===0){dx=0;dy=-grid;}
                if((e.key==='ArrowDown' || key==='s') && dy===0){dx=0;dy=grid;}
                if((e.key==='ArrowLeft' || key==='a') && dx===0){dx=-grid;dy=0;}
                if((e.key==='ArrowRight' || key==='d') && dx===0){dx=grid;dy=0;}
            });
            main();
            </script>
        """,
        "🟓 Pong": """
            <style>
                canvas { background: #000; display: block; margin: auto; border: 4px solid #fff; } 
                h1, p { color: white; text-align: center; font-family: sans-serif; }
            </style>
            <h1>🟓 Pong Match</h1><p>Left (W/S) | Right (Up/Down)</p>
            <canvas id="game" width="600" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let leftPaddle = {x: 10, y: 150, w: 10, h: 80}, rightPaddle = {x: 580, y: 150, w: 10, h: 80};
            let ball = {x: 300, y: 200, r: 7, vx: 4, vy: 4};
            let keys = {};

            function loop() {
                ctx.clearRect(0, 0, 600, 400);
                
                if (keys['w']) leftPaddle.y = Math.max(0, leftPaddle.y - 6);
                if (keys['s']) leftPaddle.y = Math.min(320, leftPaddle.y + 6);
                if (keys['arrowup']) rightPaddle.y = Math.max(0, rightPaddle.y - 6);
                if (keys['arrowdown']) rightPaddle.y = Math.min(320, rightPaddle.y + 6);

                ball.x += ball.vx; ball.y += ball.vy;
                if(ball.y <= 0 || ball.y >= 400) ball.vy *= -1;

                if(ball.x <= leftPaddle.x + leftPaddle.w && ball.y >= leftPaddle.y && ball.y <= leftPaddle.y + leftPaddle.h) { ball.vx = Math.abs(ball.vx) + 0.2; }
                if(ball.x >= rightPaddle.x - ball.r && ball.y >= rightPaddle.y && ball.y <= rightPaddle.y + rightPaddle.h) { ball.vx = -Math.abs(ball.vx) - 0.2; }

                if(ball.x < 0 || ball.x > 600) { ball.x = 300; ball.y = 200; ball.vx = ball.vx > 0 ? -4 : 4; }

                ctx.fillStyle = 'white';
                ctx.fillRect(leftPaddle.x, leftPaddle.y, leftPaddle.w, leftPaddle.h);
                ctx.fillRect(rightPaddle.x, rightPaddle.y, rightPaddle.w, rightPaddle.h);
                ctx.beginPath(); ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI*2); ctx.fill();

                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => keys[e.key.toLowerCase()] = true);
            window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);
            loop();
            </script>
        """,
        "🕹️Tetris": """
            <style>
                canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; } 
                h1, p { color: white; text-align: center; font-family: sans-serif; }
            </style>
            <h1>🕹️ Tetris</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="240" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            ctx.scale(20, 20);
            
            const arena = Array(20).fill().map(() => Array(12).fill(0));
            const COLORS = [null, '#FF0D72', '#0DC2FF', '#0DFF72', '#F538FF', '#FF8E0D', '#FFE138', '#3877FF'];
            const SHAPES = 'ILJOTSZ';

            let score = 0;
            let player = { pos: {x: 0, y: 0}, matrix: null, colorId: 1 };

            function createPiece(type) {
                if (type === 'T') return [[0,1,0],[1,1,1],[0,0,0]];
                if (type === 'O') return [[1,1],[1,1]];
                if (type === 'I') return [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]];
                if (type === 'L') return [[0,1,0],[0,1,0],[0,1,1]];
                if (type === 'J') return [[0,1,0],[0,1,0],[1,1,0]];
                if (type === 'S') return [[0,1,1],[1,1,0],[0,0,0]];
                if (type === 'Z') return [[1,1,0],[0,1,1],[0,0,0]];
            }

            function draw() { 
                ctx.fillStyle='#111'; ctx.fillRect(0,0,canvas.width,canvas.height); 
                drawMatrix(arena, {x:0, y:0}); 
                drawMatrix(player.matrix, player.pos); 
            }

            function drawMatrix(m, o) { 
                m.forEach((row, y) => row.forEach((val, x) => { 
                    if(val) { ctx.fillStyle = COLORS[val]; ctx.fillRect(x + o.x, y + o.y, 1, 1); } 
                })); 
            }

            function merge(arena, player) {
                player.matrix.forEach((row, y) => {
                    row.forEach((value, x) => {
                        if (value) { arena[y + player.pos.y][x + player.pos.x] = player.colorId; }
                    });
                });
            }

            function collide(arena, player) {
                const [m, o] = [player.matrix, player.pos];
                for (let y = 0; y < m.length; ++y) {
                    for (let x = 0; x < m[y].length; ++x) {
                        if (m[y][x] !== 0 && (arena[y + o.y] && arena[y + o.y][x + o.x]) !== 0) { return true; }
                    }
                }
                return false;
            }

            function arenaSweep() {
                outer: for (let y = arena.length - 1; y >= 0; --y) {
                    for (let x = 0; x < arena[y].length; ++x) {
                        if (arena[y][x] === 0) continue outer;
                    }
                    const row = arena.splice(y, 1).fill(0);
                    arena.unshift(row);
                    ++y; score += 100;
                    document.getElementById('score').innerText = 'Score: ' + score;
                }
            }

            function playerReset() {
                const pieces = SHAPES;
                const char = pieces[pieces.length * Math.random() | 0];
                player.matrix = createPiece(char);
                player.colorId = SHAPES.indexOf(char) + 1;
                player.pos.y = 0;
                player.pos.x = (arena[0].length / 2 | 0) - (player.matrix[0].length / 2 | 0);
                if (collide(arena, player)) { arena.forEach(row => row.fill(0)); score = 0; }
            }

            function playerDrop() {
                player.pos.y++;
                if (collide(arena, player)) {
                    player.pos.y--; merge(arena, player); playerReset(); arenaSweep();
                }
                dropCounter = 0;
            }

            function rotate(matrix) {
                for (let y = 0; y < matrix.length; ++y) {
                    for (let x = 0; x < y; ++x) { [matrix[x][y], matrix[y][x]] = [matrix[y][x], matrix[x][y]]; }
                }
                matrix.forEach(row => row.reverse());
            }

            let dropCounter = 0, lastTime = 0;
            function update(time = 0) { 
                const deltaTime = time - lastTime; lastTime = time; dropCounter += deltaTime; 
                if(dropCounter > 200) { playerDrop(); } 
                draw(); requestAnimationFrame(update); 
            }

            window.addEventListener('keydown', e => {
                const key = e.key.toLowerCase();
                if(key==='arrowleft' || key==='a') { player.pos.x--; if(collide(arena, player)) player.pos.x++; }
                if(key==='arrowright' || key==='d') { player.pos.x++; if(collide(arena, player)) player.pos.x--; }
                if(key==='arrowdown' || key==='s') { playerDrop(); }
                if(e.key===' ') { 
                    rotate(player.matrix); 
                    if(collide(arena, player)) { rotate(player.matrix); rotate(player.matrix); rotate(player.matrix); }
                }
            });
            playerReset(); update();
            </script>
        """,
        "🦖 T-Rex Run": """
            <style>
                canvas { background: #f7f7f7; display: block; margin: auto; border: 2px solid #333; } 
                h1, p { color: #333; text-align: center; font-family: sans-serif; }
            </style>
            <h1>🦖 T-Rex Run</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="600" height="150"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let dino = {y: 130, vy: 0, isJumping: false, isDucking: false}, obstacles = [], score = 0;
            
            function spawnObstacle() {
                let type = Math.random() < 0.4 ? 'bird' : 'cactus';
                let obsY = type === 'bird' ? 95 : 110; 
                obstacles.push({x: 650, type: type, y: obsY, w: 15, h: type==='bird'?15:35});
            }
            spawnObstacle();

            function loop() {
                ctx.clearRect(0,0,600,150); score++; document.getElementById('score').innerText = 'Score: ' + score;
                
                if(dino.isJumping) { 
                    dino.vy += 0.55; dino.y += dino.vy; 
                    if(dino.y >= 130) { dino.y = 130; dino.isJumping = false; } 
                }
                
                ctx.fillStyle = '#333';
                if(dino.isDucking && !dino.isJumping) {
                    ctx.fillRect(50, 120, 32, 15); 
                    ctx.fillRect(72, 115, 12, 10); 
                } else {
                    ctx.fillRect(50, dino.y-25, 20, 20); 
                    ctx.fillRect(62, dino.y-35, 14, 14); 
                    ctx.fillStyle = 'white'; ctx.fillRect(70, dino.y-32, 2, 2); 
                    ctx.fillStyle = '#333'; ctx.fillRect(54, dino.y-5, 4, 6); ctx.fillRect(62, dino.y-5, 4, 6); 
                }

                if(Math.random() < 0.01 && (obstacles.length === 0 || obstacles[obstacles.length-1].x < 420)) spawnObstacle();

                obstacles.forEach((o, i) => { 
                    o.x -= 6.5; 
                    ctx.fillStyle = o.type === 'bird' ? 'blue' : 'green';
                    ctx.fillRect(o.x, o.y, o.w, o.h);
                    
                    if(o.x < -20) obstacles.splice(i, 1);
                    
                    let dinoTop = dino.isDucking && !dino.isJumping ? 120 : dino.y - 25;
                    let dinoBottom = 135;
                    let dinoLeft = 50;
                    let dinoRight = dino.isDucking && !dino.isJumping ? 82 : 70;

                    if(o.x < dinoRight && o.x + o.w > dinoLeft && o.y < dinoBottom && o.y + o.h > dinoTop) {
                        alert('Game Over! Restarting...'); score = 0; obstacles = []; spawnObstacle();
                    }
                });
                requestAnimationFrame(loop);
            }

            window.addEventListener('keydown', e => { 
                const key = e.key.toLowerCase();
                if((key===' ' || key==='arrowup' || key==='w') && !dino.isJumping && !dino.isDucking) { 
                    dino.vy = -8.5; dino.isJumping = true; 
                } 
                if((key==='arrowdown' || key==='s')) { dino.isDucking = true; }
            });
            window.addEventListener('keyup', e => {
                const key = e.key.toLowerCase();
                if(key==='arrowdown' || key==='s') { dino.isDucking = false; }
            });
            loop();
            </script>
        """
    }

    cleaned_mode = app_mode.replace("🕹️Tetris", "🕹️Tetris").strip()
    st.title(app_mode)
    components.html(games[cleaned_mode], height=520)
