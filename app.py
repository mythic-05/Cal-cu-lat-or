import streamlit as st
import time
import streamlit.components.v1 as components

# --- APP CONFIGURATION & NAVIGATION ---
st.set_page_config(page_title="Web Arcade", layout="centered")

st.sidebar.title(" Applications ")
app_mode = st.sidebar.radio(
    "Choose a tool to load:",
    ["🔢 Calculator", "🐍 Snake", "👾 Space Invaders", "🕹️Tetris", "🦖 T-Rex Run"]
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
# BROWSER-NATIVE GAME INTERFACES (Zero-Delay JavaScript)
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
                // FIXED: Increased timeout from 90 to 150 to make the snake noticeably slower
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
                if((e.key==='ArrowUp' || e.key==='w' || e.key==='W') && dy===0){dx=0;dy=-grid;}
                if((e.key==='ArrowDown' || e.key==='s' || e.key==='S') && dy===0){dx=0;dy=grid;}
                if((e.key==='ArrowLeft' || e.key==='a' || e.key==='A') && dx===0){dx=-grid;dy=0;}
                if((e.key==='ArrowRight' || e.key==='d' || e.key==='D') && dx===0){dx=grid;dy=0;}
            });
            main();
            </script>
        """,
        "👾 Space Invaders": """
            <style>
                canvas { background: #000; display: block; margin: auto; border: 4px solid #fff; } 
                h1, p { color: white; text-align: center; font-family: sans-serif; }
            </style>
            <h1>👾 Space Invaders</h1><p id='score'>Score: 0</p>
            <canvas id="game" width="400" height="400"></canvas>
            <script>
            const canvas = document.getElementById('game'), ctx = canvas.getContext('2d');
            let player = {x: 180, y: 360, w: 30, h: 20}, lasers = [], invaders = [], score = 0;
            let lastShotTime = 0; // FIXED: For shooting delay rate-limiting
            let invaderDirection = 1; // 1 = right, -1 = left
            let invaderMoveCounter = 0;

            function initInvaders() {
                invaders = [];
                for(let i=0; i<6; i++) for(let j=0; j<3; j++) invaders.push({x: 40+i*50, y: 30+j*30, w:25, h:20});
            }
            initInvaders();

            function loop() {
                ctx.clearRect(0,0,400,400); 
                ctx.fillStyle='blue'; ctx.fillRect(player.x, player.y, player.w, player.h);
                ctx.fillStyle='red'; invaders.forEach(inv => ctx.fillRect(inv.x, inv.y, inv.w, inv.h));
                ctx.fillStyle='yellow'; 
                
                // FIXED: Make fleet dynamically step sideways and march down closer over time
                invaderMoveCounter++;
                if (invaderMoveCounter % 40 === 0) {
                    let shiftDown = false;
                    invaders.forEach(inv => {
                        inv.x += invaderDirection * 10;
                        if (inv.x > 360 || inv.x < 10) { shiftDown = true; }
                    });
                    if (shiftDown) {
                        invaderDirection *= -1;
                        invaders.forEach(inv => { inv.y += 15; });
                    }
                }

                // Game Over if invaders breach defense perimeter
                invaders.forEach(inv => {
                    if (inv.y + inv.h >= player.y) {
                        alert('Game Over! Your base was overrun.');
                        initInvaders();
                        score = 0;
                    }
                });
                
                lasers.forEach((l,li) => { 
                    l.y-=7; 
                    ctx.fillRect(l.x, l.y, 4, 10); 
                    if(l.y<0) lasers.splice(li,1); 
                });
                
                lasers.forEach((l,li) => { 
                    invaders.forEach((inv,ii) => {
                        if(l.x>inv.x && l.x<inv.x+inv.w && l.y>inv.y && l.y<inv.y+inv.h) { 
                            invaders.splice(ii,1); 
                            lasers.splice(li,1); 
                            score+=10; 
                            document.getElementById('score').innerText = 'Score: ' + score; 
                        }
                    })
                });
                
                if(invaders.length === 0) {
                    alert('You Win! Initializing next fleet...');
                    initInvaders();
                }
                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => {
                if((e.key==='ArrowLeft' || e.key==='a' || e.key==='A') && player.x>0) player.x-=20;
                if((e.key==='ArrowRight' || e.key==='d' || e.key==='D') && player.x<370) player.x+=20;
                if(e.key===' ') {
                    let now = Date.now();
                    // FIXED: Enforce a 400ms weapons-cooldown shooting delay
                    if (now - lastShotTime > 400) {
                        lasers.push({x: player.x+13, y: player.y});
                        lastShotTime = now;
                    }
                }
            });
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
            
            // Standard tetromino blocks
            const SHAPES = [
                [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]], // I
                [[2,2],[2,2]], // O
                [[0,3,0],[3,3,3],[0,0,0]], // T
                [[4,0,0],[4,4,4],[0,0,0]]  // L
            ];

            function createPiece() {
                const shape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
                return { pos: {x: 4, y: 0}, matrix: shape };
            }

            let player = createPiece();
            let score = 0;

            function draw() { 
                ctx.fillStyle='#111'; ctx.fillRect(0,0,canvas.width,canvas.height); 
                drawMatrix(arena, {x:0, y:0}, 'cyan'); 
                drawMatrix(player.matrix, player.pos, 'red'); 
            }
            function drawMatrix(m, o, color) { 
                m.forEach((row, y) => row.forEach((val, x) => { 
                    if(val !== 0) { ctx.fillStyle=color; ctx.fillRect(x + o.x, y + o.y, 1, 1); } 
                })); 
            }
            function merge(arena, player) {
                player.matrix.forEach((row, y) => {
                    row.forEach((value, x) => {
                        if (value) { arena[y + player.pos.y][x + player.pos.x] = value; }
                    });
                });
            }
            function collide(arena, player) {
                const [m, o] = [player.matrix, player.pos];
                for (let y = 0; y < m.length; ++y) {
                    for (let x = 0; x < m[y].length; ++x) {
                        if (m[y][x] !== 0 && (arena[y + o.y] === undefined || arena[y + o.y][x + o.x] === undefined || arena[y + o.y][x + o.x] !== 0)) { return true; }
                    }
                }
                return false;
            }
            
            // FIXED: Clear rows properly instead of resetting whole board back to top when a single block hits floor!
            function arenaSweep() {
                let rowCount = 1;
                outer: for (let y = arena.length - 1; y > 0; --y) {
                    for (let x = 0; x < arena[y].length; ++x) {
                        if (arena[y][x] === 0) { continue outer; }
                    }
                    const row = arena.splice(y, 1)[0].fill(0);
                    arena.unshift(row);
                    ++y;
                    score += rowCount * 100;
                    document.getElementById('score').innerText = 'Score: ' + score;
                }
            }

            function playerDrop() {
                player.pos.y++;
                if (collide(arena, player)) {
                    player.pos.y--;
                    merge(arena, player);
                    arenaSweep(); // Check for completed lines
                    player = createPiece(); // Spawn new piece at top
                    if (collide(arena, player)) {
                        // Real game over clear
                        arena.forEach(row => row.fill(0));
                        score = 0;
                        document.getElementById('score').innerText = 'Score: ' + score;
                    }
                }
                dropCounter = 0;
            }

            let dropCounter = 0; 
            let lastTime = 0;
            function update(time = 0) { 
                const deltaTime = time - lastTime;
                lastTime = time;
                dropCounter += deltaTime; 
                // FIXED: Adjusted threshold counter drop speed from 1000ms down to 400ms for faster drops
                if(dropCounter > 400) { playerDrop(); } 
                draw(); 
                requestAnimationFrame(update); 
            }
            window.addEventListener('keydown', e => {
                if(e.key==='ArrowLeft' || e.key==='a') { player.pos.x--; if(collide(arena, player)) player.pos.x++; }
                if(e.key==='ArrowRight' || e.key==='d') { player.pos.x++; if(collide(arena, player)) player.pos.x--; }
                if(e.key==='ArrowDown' || e.key==='s') { playerDrop(); }
            });
            update();
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
            // FIXED: Toned down velocity gravity jump heights so the dino isn't soaring off-screen
            let dino = {y: 130, vy: 0, isJumping: false}, obstacles = [{x: 600}], score = 0;
            
            function loop() {
                ctx.clearRect(0,0,600,150); 
                score++; 
                document.getElementById('score').innerText = 'Score: ' + score;
                
                if(dino.isJumping) { 
                    dino.vy += 0.7; // Increased gravity drop down speed
                    dino.y += dino.vy; 
                    if(dino.y >= 130) { dino.y = 130; dino.isJumping = false; } 
                }
                
                // FIXED: Render actual geometric visual elements for a simple green T-Rex dinosaur layout profile instead of a flat generic cube structure box
                ctx.fillStyle='green';
                ctx.fillRect(50, dino.y - 25, 20, 25); // Body
                ctx.fillRect(60, dino.y - 33, 14, 12); // Head snout layout
                ctx.fillStyle='black';
                ctx.fillRect(63, dino.y - 30, 2, 2);   // Eye tracking pixel
                ctx.fillStyle='green';
                ctx.fillRect(46, dino.y - 12, 5, 8);   // Back leg extension
                ctx.fillRect(56, dino.y - 12, 5, 8);   // Front leg extension
                
                obstacles.forEach((o, i) => { 
                    o.x -= 6; 
                    ctx.fillStyle='brown';
                    ctx.fillRect(o.x, 115, 12, 35); // Cactus obstacle structure
                    if(o.x < -15) o.x = 600 + Math.random()*300; 
                    
                    if(o.x > 35 && o.x < 70 && dino.y >= 115) { 
                        alert('Game Over! Your high score was: ' + score); 
                        score = 0; 
                        o.x = 600; 
                    }
                });
                requestAnimationFrame(loop);
            }
            window.addEventListener('keydown', e => { 
                // FIXED: Adjusted standard lift jump vector from -12 down to -8.5 for normal trajectory arcs
                if((e.key===' ' || e.key==='ArrowUp' || e.key==='w' || e.key==='W') && !dino.isJumping) { 
                    dino.vy = -8.5; 
                    dino.isJumping = true; 
                } 
            });
            loop();
            </script>
        """
    }

    # Normalize name keys to bypass string layout space mismatch options
    cleaned_mode = app_mode.replace("🕹️Tetris", "🕹️Tetris").strip()
    
    st.title(app_mode)
    components.html(games[cleaned_mode], height=520)
