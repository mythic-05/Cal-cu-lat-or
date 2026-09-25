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
    ["🔢 Calculator", "🐍 Snake", "🟓 Pong", "🕹️Tetris", "🦖 Blob Run", "🍕 Pac-Man"]
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
                body { margin: 0; padding: 0; font-family: sans-serif; background: #111; color: white; touch-action: manipulation; }
                canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; max-width: 100%; height: auto; } 
                h1, p { text-align: center; margin: 5px 0; }
                .game-container { position: relative; width: 400px; max-width: 100%; margin: auto; }
                .overlay { display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(0,0,0,0.85); color: #ff4b4b; padding: 20px; text-align: center; border-radius: 10px; border: 2px solid #ff4b4b; font-size: 1.5rem; font-weight: bold; width: 80%; z-index: 10; }
                .overlay p { font-size: 1rem; color: #fff; margin-top: 10px; font-weight: normal; }
                .mobile-controls { display: grid; grid-template-columns: repeat(3, 1fr); width: 200px; margin: 15px auto; gap: 10px; }
                .btn { background: #333; color: white; border: 2px solid #fff; padding: 15px; text-align: center; font-size: 1.2rem; border-radius: 8px; user-select: none; cursor: pointer; }
                .btn:active { background: #555; }
                .spacer { visibility: hidden; }
            </style>
            <h1>🐍 Snake Game</h1><p id='score'>Score: 0</p>
            <div class="game-container">
                <div id="overlay" class="overlay">try again?<p id="insult"></p></div>
                <canvas id="game" width="400" height="400"></canvas>
            </div>
            <div class="mobile-controls">
                <div class="spacer"></div><div class="btn" id="btn-up">▲</div><div class="spacer"></div>
                <div class="btn" id="btn-left">◀</div><div class="spacer"></div><div class="btn" id="btn-right">▶</div>
                <div class="spacer"></div><div class="btn" id="btn-down">▼</div><div class="spacer"></div>
            </div>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let grid = 20, score = 0, gameRunning = true;
            let snake = [{x: 160, y: 160}, {x: 140, y: 160}, {x: 120, y: 160}];
            let dx = grid, dy = 0;
            let food = {x: 80, y: 80};

            function main() {
                if (!gameRunning) return;
                let cause = gameOver();
                if (cause) {
                    gameRunning = false;
                    document.getElementById('overlay').style.display = 'block';
                    
                    let lines = ["Hey idiot, the apple's over there.", "Nice one!", "Imagine losing in a snake game lmfao"];
                    if (cause === 'edge') lines.push("Maybe pay attention next time?");
                    if (cause === 'self') {
                        lines.push("Maybe don't hit yourself");
                        lines.push("Stop hitting yourself stop hitting yourself");
                    }
                    document.getElementById('insult').innerText = lines[Math.floor(Math.random() * lines.length)];
                    
                    setTimeout(resetGame, 3000);
                    return;
                }
                setTimeout(function() { clear(); drawFood(); move(); drawSnake(); main(); }, 150);
            }
            function resetGame() {
                snake = [{x: 160, y: 160}, {x: 140, y: 160}, {x: 120, y: 160}];
                dx = grid; dy = 0; score = 0;
                document.getElementById('score').innerText = 'Score: ' + score;
                document.getElementById('overlay').style.display = 'none';
                food = {x: Math.floor(Math.random()*19)*grid, y: Math.floor(Math.random()*19)*grid};
                gameRunning = true;
                main();
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
            function gameOver() {
                const h = snake[0];
                if (h.x < 0 || h.x >= canvas.width || h.y < 0 || h.y >= canvas.height) return 'edge';
                for(let i = 1; i < snake.length; i++) {
                    if(snake[i].x === h.x && snake[i].y === h.y) return 'self';
                }
                return null;
            }
            function handleInput(dir) {
                if(dir === 'up' && dy === 0) { dx = 0; dy = -grid; }
                if(dir === 'down' && dy === 0) { dx = 0; dy = grid; }
                if(dir === 'left' && dx === 0) { dx = -grid; dy = 0; }
                if(dir === 'right' && dx === 0) { dx = grid; dy = 0; }
            }
            window.addEventListener('keydown', e => {
                const key = e.key.toLowerCase();
                if(['arrowup', 'arrowdown', 'arrowleft', 'arrowright', ' '].includes(e.key.toLowerCase())) e.preventDefault();
                if(e.key==='ArrowUp' || key==='w') handleInput('up');
                if(e.key==='ArrowDown' || key==='s') handleInput('down');
                if(e.key==='ArrowLeft' || key==='a') handleInput('left');
                if(e.key==='ArrowRight' || key==='d') handleInput('right');
            });
            document.getElementById('btn-up').addEventListener('touchstart', e => { e.preventDefault(); handleInput('up'); });
            document.getElementById('btn-down').addEventListener('touchstart', e => { e.preventDefault(); handleInput('down'); });
            document.getElementById('btn-left').addEventListener('touchstart', e => { e.preventDefault(); handleInput('left'); });
            document.getElementById('btn-right').addEventListener('touchstart', e => { e.preventDefault(); handleInput('right'); });
            main();
            </script>
        """,
        "🟓 Pong": """
            <style>
                body { margin: 0; padding: 0; font-family: sans-serif; background: #000; color: white; touch-action: none; }
                canvas { background: #000; display: block; margin: auto; border: 4px solid #fff; max-width: 100%; height: auto; } 
                h1, p { text-align: center; }
                .pong-layout { position: relative; display: flex; width: 600px; max-width: 100%; margin: auto; }
                .touch-zone { position: absolute; top: 0; bottom: 0; width: 50%; z-index: 5; }
                #left-zone { left: 0; }
                #right-zone { right: 0; }
            </style>
            <h1>🟓 Pong Match</h1>
            <p id="score-board">Left Player: 0 | Right Player: 0</p>
            <div class="pong-layout">
                <div id="left-zone" class="touch-zone"></div>
                <div id="right-zone" class="touch-zone"></div>
                <canvas id="game" width="600" height="400"></canvas>
            </div>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let leftPaddle = {x: 10, y: 150, w: 10, h: 80}, rightPaddle = {x: 580, y: 150, w: 10, h: 80};
            let ball = {x: 300, y: 200, r: 7, vx: 4, vy: 4};
            let leftScore = 0, rightScore = 0;
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

                if(ball.x < 0) { rightScore++; updateScoreBoard(); resetBall(); } 
                else if(ball.x > 600) { leftScore++; updateScoreBoard(); resetBall(); }

                ctx.fillStyle = 'white';
                ctx.fillRect(leftPaddle.x, leftPaddle.y, leftPaddle.w, leftPaddle.h);
                ctx.fillRect(rightPaddle.x, rightPaddle.y, rightPaddle.w, rightPaddle.h);
                ctx.beginPath(); ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI*2); ctx.fill();

                requestAnimationFrame(loop);
            }
            
            function updateScoreBoard() {
                document.getElementById('score-board').innerText = `Left Player: ${leftScore} | Right Player: ${rightScore}`;
            }
            
            function resetBall() {
                ball.x = 300; ball.y = 200; 
                ball.vx = ball.vx > 0 ? -4 : 4;
                ball.vy = Math.random() > 0.5 ? 4 : -4;
            }

            window.addEventListener('keydown', e => {
                if(['arrowup', 'arrowdown', 'w', 's'].includes(e.key.toLowerCase())) e.preventDefault();
                keys[e.key.toLowerCase()] = true;
            });
            window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);

            function handleTouch(e, zone) {
                e.preventDefault();
                let rect = canvas.getBoundingClientRect();
                for (let touch of e.touches) {
                    let clientX = touch.clientX - rect.left;
                    let clientY = touch.clientY - rect.top;
                    let canvasY = clientY * (400 / rect.height);
                    if(zone === 'left' && touch.clientX < window.innerWidth/2) leftPaddle.y = Math.min(320, Math.max(0, canvasY - 40));
                    if(zone === 'right' && touch.clientX >= window.innerWidth/2) rightPaddle.y = Math.min(320, Math.max(0, canvasY - 40));
                }
            }
            document.getElementById('left-zone').addEventListener('touchmove', e => handleTouch(e, 'left'));
            document.getElementById('left-zone').addEventListener('touchstart', e => handleTouch(e, 'left'));
            document.getElementById('right-zone').addEventListener('touchmove', e => handleTouch(e, 'right'));
            document.getElementById('right-zone').addEventListener('touchstart', e => handleTouch(e, 'right'));

            loop();
            </script>
        """,
        "🕹️Tetris": """
            <style>
                body { margin: 0; padding: 0; font-family: sans-serif; background: #111; color: white; touch-action: manipulation; }
                canvas { background: #111; display: block; margin: auto; border: 4px solid #fff; max-width: 100%; height: auto; } 
                h1, p { text-align: center; margin: 5px 0; }
                .game-container { position: relative; width: 240px; max-width: 100%; margin: auto; }
                .overlay { display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(0,0,0,0.85); color: #00d2ff; padding: 20px; text-align: center; border-radius: 10px; border: 2px solid #00d2ff; font-size: 1.5rem; font-weight: bold; width: 80%; z-index: 10; }
                .mobile-controls { display: grid; grid-template-columns: repeat(4, 1fr); width: 240px; margin: 15px auto; gap: 8px; }
                .btn { background: #333; color: white; border: 2px solid #fff; padding: 12px 5px; text-align: center; font-size: 1rem; border-radius: 8px; user-select: none; cursor: pointer; }
                .btn:active { background: #555; }
            </style>
            <h1>🕹️ Tetris</h1><p id='score'>Score: 0</p>
            <div class="game-container">
                <div id="overlay" class="overlay">try again?</div>
                <canvas id="game" width="240" height="400"></canvas>
            </div>
            <div class="mobile-controls">
                <div class="btn" id="btn-left">◀</div>
                <div class="btn" id="btn-rot">🔄</div>
                <div class="btn" id="btn-drop">▼</div>
                <div class="btn" id="btn-right">▶</div>
            </div>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            ctx.scale(20, 20);
            
            const arena = Array(20).fill().map(() => Array(12).fill(0));
            const COLORS = [null, '#FF0D72', '#0DC2FF', '#0DFF72', '#F538FF', '#FF8E0D', '#FFE138', '#3877FF'];
            const SHAPES = 'ILJOTSZ';

            let score = 0, gameRunning = true;
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
                let rowsCleared = 0;
                for (let y = arena.length - 1; y >= 0; --y) {
                    let full = true;
                    for (let x = 0; x < arena[y].length; ++x) {
                        if (arena[y][x] === 0) { full = false; break; }
                    }
                    if (full) {
                        arena.splice(y, 1);
                        arena.unshift(Array(12).fill(0));
                        y++; 
                        rowsCleared++;
                    }
                }
                if (rowsCleared > 0) {
                    score += rowsCleared * 100;
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
                if (collide(arena, player)) { 
                    gameRunning = false;
                    document.getElementById('overlay').style.display = 'block';
                    setTimeout(() => {
                        arena.forEach(row => row.fill(0)); 
                        score = 0; 
                        document.getElementById('score').innerText = 'Score: ' + score;
                        document.getElementById('overlay').style.display = 'none';
                        gameRunning = true;
                        playerReset();
                    }, 2500);
                }
            }

            function playerDrop() {
                if (!gameRunning) return;
                player.pos.y++;
                if (collide(arena, player)) {
                    player.pos.y--; 
                    merge(arena, player); 
                    arenaSweep();
                    playerReset(); 
                }
                dropCounter = 0;
            }

            function playerRotate() {
                if (!gameRunning) return;
                rotate(player.matrix);
                if (collide(arena, player)) {
                    rotate(player.matrix); rotate(player.matrix); rotate(player.matrix);
                }
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
                if(dropCounter > 400) { playerDrop(); } 
                draw(); requestAnimationFrame(update); 
            }

            function moveLeft() { if(gameRunning) { player.pos.x--; if(collide(arena, player)) player.pos.x++; } }
            function moveRight() { if(gameRunning) { player.pos.x++; if(collide(arena, player)) player.pos.x--; } }

            window.addEventListener('keydown', e => {
                if (!gameRunning) return;
                const key = e.key.toLowerCase();
                if(['arrowleft', 'arrowright', 'arrowdown', 'a', 'd', 's', ' '].includes(key)) e.preventDefault();
                if(key==='arrowleft' || key==='a') moveLeft();
                if(key==='arrowright' || key==='d') moveRight();
                if(key==='arrowdown' || key==='s') playerDrop();
                if(e.key===' ') playerRotate();
            });

            document.getElementById('btn-left').addEventListener('touchstart', e => { e.preventDefault(); moveLeft(); });
            document.getElementById('btn-right').addEventListener('touchstart', e => { e.preventDefault(); moveRight(); });
            document.getElementById('btn-drop').addEventListener('touchstart', e => { e.preventDefault(); playerDrop(); });
            document.getElementById('btn-rot').addEventListener('touchstart', e => { e.preventDefault(); playerRotate(); });

            playerReset(); update();
            </script>
        """,
        "🦖 Blob Run": """
            <style>
                body { margin: 0; padding: 0; font-family: sans-serif; background: #fff; color: #333; touch-action: manipulation; }
                canvas { background: #f7f7f7; display: block; margin: auto; border: 2px solid #333; max-width: 100%; height: auto; } 
                h1, p { text-align: center; margin: 5px 0; }
                .game-container { position: relative; width: 600px; max-width: 100%; margin: auto; }
                .overlay { display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(255,255,255,0.9); color: #333; padding: 20px; text-align: center; border-radius: 10px; border: 2px solid #333; font-size: 1.5rem; font-weight: bold; width: 60%; z-index: 10; }
                .mobile-controls { display: flex; justify-content: center; gap: 20px; width: 100%; margin: 15px auto; }
                .btn { background: #e0e0e0; color: #333; border: 2px solid #333; padding: 15px 30px; text-align: center; font-size: 1.2rem; border-radius: 8px; user-select: none; cursor: pointer; font-weight: bold; }
                .btn:active { background: #bbb; }
            </style>
            <h1>🦖 Blob Run</h1><p id='score'>Score: 0</p>
            <div class="game-container">
                <div id="overlay" class="overlay">try again?</div>
                <canvas id="game" width="600" height="150"></canvas>
            </div>
            <div class="mobile-controls">
                <div class="btn" id="btn-jump">JUMP (▲)</div>
                <div class="btn" id="btn-duck">DUCK (▼)</div>
            </div>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let dino = {y: 130, vy: 0, w: 18, h: 22, isJumping: false, isDucking: false}; 
            let obstacles = [], score = 0, gameRunning = true;
            
            function spawnObstacle() {
                let type = Math.random() < 0.4 ? 'bird' : 'cactus';
                let obsY = type === 'bird' ? 95 : 112; 
                let obsW = type === 'bird' ? 15 : 12;
                let obsH = type === 'bird' ? 12 : 26;
                obstacles.push({x: 650, type: type, y: obsY, w: obsW, h: obsH});
            }
            spawnObstacle();

            function loop() {
                if (!gameRunning) return;
                ctx.clearRect(0,0,600,150); score++; document.getElementById('score').innerText = 'Score: ' + score;
                
                if(dino.isJumping) { 
                    dino.vy += 0.55; dino.y += dino.vy; 
                    if(dino.y >= 130) { dino.y = 130; dino.isJumping = false; } 
                }
                
                ctx.fillStyle = '#333';
                if(dino.isDucking && !dino.isJumping) {
                    dino.w = 30; dino.h = 13;
                    ctx.fillRect(50, 130 - dino.h, dino.w, dino.h); 
                    ctx.fillRect(50 + dino.w, 130 - dino.h + 2, 8, 8); 
                } else {
                    dino.w = 18; dino.h = 24;
                    ctx.fillRect(50, dino.y-dino.h, dino.w, dino.h); 
                    ctx.fillRect(50 + dino.w, dino.y-dino.h, 6, 8); 
                    ctx.fillStyle = 'white'; ctx.fillRect(50 + dino.w + 2, dino.y-dino.h + 2, 2, 2); 
                    ctx.fillStyle = '#333'; ctx.fillRect(54, dino.y, 3, 5); ctx.fillRect(61, dino.y, 3, 5); 
                }

                if(Math.random() < 0.01 && (obstacles.length === 0 || obstacles[obstacles.length-1].x < 420)) spawnObstacle();

                obstacles.forEach((o, i) => { 
                    o.x -= 6.5; 
                    ctx.fillStyle = o.type === 'bird' ? 'blue' : 'green';
                    ctx.fillRect(o.x, o.y, o.w, o.h);
                    
                    if(o.x < -20) obstacles.splice(i, 1);
                    
                    let dinoTop = dino.isDucking && !dino.isJumping ? 130 - dino.h : dino.y - dino.h;
                    let dinoBottom = dino.isDucking && !dino.isJumping ? 130 : dino.y;
                    let dinoLeft = 50;
                    let dinoRight = 50 + (dino.isDucking && !dino.isJumping ? dino.w + 8 : dino.w);

                    if(o.x < dinoRight && o.x + o.w > dinoLeft && o.y < dinoBottom && o.y + o.h > dinoTop) {
                        gameRunning = false;
                        document.getElementById('overlay').style.display = 'block';
                        setTimeout(resetDinoGame, 2500);
                    }
                });
                requestAnimationFrame(loop);
            }

            function resetDinoGame() {
                score = 0; obstacles = []; spawnObstacle();
                dino.y = 130; dino.vy = 0; dino.isJumping = false; dino.isDucking = false;
                document.getElementById('overlay').style.display = 'none';
                gameRunning = true;
                loop();
            }

            function jump() {
                if(!dino.isJumping && !dino.isDucking) { dino.vy = -8.5; dino.isJumping = true; }
            }

            window.addEventListener('keydown', e => { 
                const key = e.key.toLowerCase();
                if([' ', 'arrowup', 'arrowdown', 'w', 's'].includes(key)) e.preventDefault();
                if((key===' ' || key==='arrowup' || key==='w')) jump();
                if((key==='arrowdown' || key==='s')) { dino.isDucking = true; }
            });
            window.addEventListener('keyup', e => {
                const key = e.key.toLowerCase();
                if(key==='arrowdown' || key==='s') { dino.isDucking = false; }
            });

            document.getElementById('btn-jump').addEventListener('touchstart', e => { e.preventDefault(); jump(); });
            document.getElementById('btn-duck').addEventListener('touchstart', e => { e.preventDefault(); dino.isDucking = true; });
            document.getElementById('btn-duck').addEventListener('touchend', e => { e.preventDefault(); dino.isDucking = false; });
            loop();
            </script>
        """,
        "🍕 Pac-Man": """
            <style>
                body { margin: 0; padding: 0; font-family: sans-serif; background: #000; color: white; touch-action: manipulation; }
                canvas { background: #000; display: block; margin: auto; border: 4px solid #fff; max-width: 100%; height: auto; } 
                h1, p { text-align: center; margin: 5px 0; }
                .game-container { position: relative; width: 380px; max-width: 100%; margin: auto; }
                .overlay { display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(0,0,0,0.85); color: #ffff00; padding: 20px; text-align: center; border-radius: 10px; border: 2px solid #ffff00; font-size: 1.5rem; font-weight: bold; width: 80%; z-index: 10; }
                .mobile-controls { display: grid; grid-template-columns: repeat(3, 1fr); width: 180px; margin: 15px auto; gap: 10px; }
                .btn { background: #333; color: white; border: 2px solid #fff; padding: 15px; text-align: center; font-size: 1.2rem; border-radius: 8px; user-select: none; cursor: pointer; }
                .btn:active { background: #555; }
                .spacer { visibility: hidden; }
            </style>
            <h1>🍕 Pac-Man Arcade</h1><p id='score'>Score: 0</p>
            <div class="game-container">
                <div id="overlay" class="overlay">try again?</div>
                <canvas id="game" width="380" height="380"></canvas>
            </div>
            <div class="mobile-controls">
                <div class="spacer"></div><div class="btn" id="btn-up">▲</div><div class="spacer"></div>
                <div class="btn" id="btn-left">◀</div><div class="spacer"></div><div class="btn" id="btn-right">▶</div>
                <div class="spacer"></div><div class="btn" id="btn-down">▼</div><div class="spacer"></div>
            </div>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            const tileSize = 20;
            let score = 0, gameRunning = true;

            let map = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
                [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
                [1,1,1,1,0,1,1,1,2,1,2,1,1,1,0,1,1,1,1],
                [2,2,2,1,0,1,2,2,2,2,2,2,2,1,0,1,2,2,2],
                [1,1,1,1,0,1,2,1,1,2,1,1,2,1,0,1,1,1,1],
                [2,2,2,2,0,2,2,1,2,2,2,1,2,2,0,2,2,2,2],
                [1,1,1,1,0,1,2,1,1,1,1,1,2,1,0,1,1,1,1],
                [2,2,2,1,0,1,2,2,2,2,2,2,2,1,0,1,2,2,2],
                [1,1,1,1,0,1,2,1,1,1,1,1,2,1,0,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
                [1,0,0,1,0,0,0,0,0,2,0,0,0,0,0,1,0,0,1],
                [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
                [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ];

            let pacman = { x: 9, y: 15, dx: 0, dy: 0, nextDx: 0, nextDy: 0 };
            let ghosts = [
                { x: 9, y: 7, dx: 1, dy: 0, color: 'red' },
                { x: 8, y: 9, dx: -1, dy: 0, color: 'pink' },
                { x: 10, y: 9, dx: 1, dy: 0, color: 'cyan' }
            ];

            function isWall(gridX, gridY) {
                if (gridX < 0 || gridX >= 19 || gridY < 0 || gridY >= 19) return false;
                return map[gridY][gridX] === 1;
            }

            function draw() {
                ctx.fillStyle = '#000';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                for (let r = 0; r < 19; r++) {
                    for (let c = 0; c < 19; c++) {
                        if (map[r][c] === 1) {
                            ctx.fillStyle = '#1111b3';
                            ctx.fillRect(c * tileSize, r * tileSize, tileSize, tileSize);
                        } else if (map[r][c] === 0) {
                            ctx.fillStyle = '#ffb8ae';
                            ctx.beginPath();
                            ctx.arc(c * tileSize + tileSize/2, r * tileSize + tileSize/2, 3, 0, Math.PI * 2);
                            ctx.fill();
                        }
                    }
                }

                let centerX = pacman.x * tileSize + tileSize / 2;
                let centerY = pacman.y * tileSize + tileSize / 2;
                let radius = tileSize / 2 - 1;

                let startAngle = 0.2;
                let endAngle = 1.8;

                if (pacman.dx === 1) { startAngle = 0.2; endAngle = 1.8; }
                else if (pacman.dx === -1) { startAngle = 1.2; endAngle = 0.8; }
                else if (pacman.dy === 1) { startAngle = 0.7; endAngle = 0.3; }
                else if (pacman.dy === -1) { startAngle = 1.7; endAngle = 1.3; }

                ctx.fillStyle = '#ffff00';
                ctx.beginPath();
                ctx.arc(centerX, centerY, radius, startAngle * Math.PI, endAngle * Math.PI);
                ctx.lineTo(centerX, centerY);
                ctx.closePath();
                ctx.fill();

                ghosts.forEach(g => {
                    ctx.fillStyle = g.color;
                    ctx.fillRect(g.x * tileSize + 2, g.y * tileSize + 2, tileSize - 4, tileSize - 4);
                });
            }

            function update() {
                if (!gameRunning) return;

                if (pacman.nextDx !== 0 || pacman.nextDy !== 0) {
                    if (!isWall(pacman.x + pacman.nextDx, pacman.y + pacman.nextDy)) {
                        pacman.dx = pacman.nextDx;
                        pacman.dy = pacman.nextDy;
                    }
                }

                if (!isWall(pacman.x + pacman.dx, pacman.y + pacman.dy)) {
                    pacman.x += pacman.dx;
                    pacman.y += pacman.dy;
                    if (pacman.x < 0) pacman.x = 18;
                    if (pacman.x > 18) pacman.x = 0;
                }

                if (map[pacman.y][pacman.x] === 0) {
                    map[pacman.y][pacman.x] = 2;
                    score += 10;
                    document.getElementById('score').innerText = 'Score: ' + score;
                }

                ghosts.forEach(g => {
                    let options = [];
                    let dirs = [{x:1,y:0},{x:-1,y:0},{x:0,y:1},{x:0,y:-1}];
                    dirs.forEach(d => {
                        if (!isWall(g.x + d.x, g.y + d.y) && !(d.x === -g.dx && d.y === -g.dy)) {
                            options.push(d);
                        }
                    });
                    if (options.length === 0) {
                        g.dx = -g.dx; g.dy = -g.dy;
                    } else {
                        let choice = options[Math.floor(Math.random() * options.length)];
                        g.dx = choice.x; g.dy = choice.y;
                    }

                    if (!isWall(g.x + g.dx, g.y + g.dy)) {
                        g.x += g.dx;
                        g.y += g.dy;
                        if (g.x < 0) g.x = 18;
                        if (g.x > 18) g.x = 0;
                    }

                    if (g.x === pacman.x && g.y === pacman.y) {
                        gameRunning = false;
                        document.getElementById('overlay').style.display = 'block';
                        setTimeout(resetPacman, 2500);
                    }
                });

                draw();
                setTimeout(update, 220);
            }

            function resetPacman() {
                score = 0;
                document.getElementById('score').innerText = 'Score: ' + score;
                document.getElementById('overlay').style.display = 'none';
                pacman = { x: 9, y: 15, dx: 0, dy: 0, nextDx: 0, nextDy: 0 };
                ghosts = [
                    { x: 9, y: 7, dx: 1, dy: 0, color: 'red' },
                    { x: 8, y: 9, dx: -1, dy: 0, color: 'pink' },
                    { x: 10, y: 9, dx: 1, dy: 0, color: 'cyan' }
                ];
                for (let r = 0; r < 19; r++) {
                    for (let c = 0; c < 19; c++) {
                        if (map[r][c] === 2 && (r !== 15 || c !== 9)) {
                            map[r][c] = 0;
                        }
                    }
                }
                gameRunning = true;
                draw();
            }

            function handleInput(dir) {
                if (dir === 'up') { pacman.nextDx = 0; pacman.nextDy = -1; }
                if (dir === 'down') { pacman.nextDx = 0; pacman.nextDy = 1; }
                if (dir === 'left') { pacman.nextDx = -1; pacman.nextDy = 0; }
                if (dir === 'right') { pacman.nextDx = 1; pacman.nextDy = 0; }
            }

            window.addEventListener('keydown', e => {
                const key = e.key.toLowerCase();
                if (['arrowup', 'arrowdown', 'arrowleft', 'arrowright', ' ', 'w', 's', 'a', 'd'].includes(key)) e.preventDefault();
                if (key === 'arrowup' || key === 'w') handleInput('up');
                if (key === 'arrowdown' || key === 's') handleInput('down');
                if (key === 'arrowleft' || key === 'a') handleInput('left');
                if (key === 'arrowright' || key === 'd') handleInput('right');
            });

            document.getElementById('btn-up').addEventListener('touchstart', e => { e.preventDefault(); handleInput('up'); });
            document.getElementById('btn-down').addEventListener('touchstart', e => { e.preventDefault(); handleInput('down'); });
            document.getElementById('btn-left').addEventListener('touchstart', e => { e.preventDefault(); handleInput('left'); });
            document.getElementById('btn-right').addEventListener('touchstart', e => { e.preventDefault(); handleInput('right'); });

            draw();
            update();
            </script>
        """
    }

    cleaned_mode = app_mode.strip()
    st.title(app_mode)
    components.html(games[cleaned_mode], height=650)
