import sys

projects = [
    ["https://editor.p5js.org/fanningo24/full/86awrM6mr", "Just press load"],
    ["https://editor.p5js.org/L0MP/full/-TLcGhmlo", "Use arrow keys to move"],
    ["https://editor.p5js.org/alfandrej23/full/erlS2Cubq", "Tic tac toe"],
    ["https://editor.p5js.org/adam7/full/rb87IYaXw", "Move mouse and click"],
    [
        "https://editor.p5js.org/goldman-wetzlerj24/full/94Cm43WAB",
        "adjust sliders to see how objects of different masses and velocities will collide",
    ],
    ["https://editor.p5js.org/VLP_0608/full/sG2s8J7H2", "student eating pretzel"],
    [
        "https://editor.p5js.org/novakovicn24/full/8qrkeZNru",
        "press load, art of astroid colliding",
    ],
    ["https://editor.p5js.org/swagtime/full/NbcUP6MR5y", "rope/spring system"],
    ["https://editor.p5js.org/justanotherstrange/full/ZKw2nMeSP", "blackjack game"],
    ["https://editor.p5js.org/goldman-wetzlerj24/full/ctiRi3cSy", "wave rider"],
    ["https://editor.p5js.org/swagtime/full/l53WOnM6a", "art: rainbow star"],
    # [
    #     "https://editor.p5js.org/swagtime/full/n812WCCtU",
    #     "cool audio stuff, move your mouse",
    # ],
    ["https://editor.p5js.org/adam7/full/CR2T6HARN", "use wasd to move the box"],
    [
        "https://editor.p5js.org/fanningo24/full/6rMYfJAqQ",
        "use wasd to move the circle",
    ],
    ["https://editor.p5js.org/goldman-wetzlerj24/full/oFP1CpW4V", "swinging rope"],
    [
        "https://editor.p5js.org/swagtime/full/L5u1htJgK",
        "snake game, use arrow keys to play",
    ],
    [
        "https://editor.p5js.org/JazzyJasperZ/full/92xmPQh44",
        "wordle clone, guess the word",
    ],
    [
        "https://editor.p5js.org/goldman-wetzlerj24/full/73dxhVGGQ",
        "semi-realistic planetary orbit, adjust the slider to adjust gravity",
    ],
    ["https://editor.p5js.org/novakovicn24/full/eaLLPJClI", "merry christmas art!"],
    ["https://editor.p5js.org/JazzyJasperZ/full/uY3HYwH6N", "frantic teapot"],
    [
        "https://editor.p5js.org/L0MP/full/GiZMNz-88",
        "2d pong, use arrow keys and wasd to move",
    ],
    ["https://editor.p5js.org/swagtime/full/a3bvdik28", "bees swarm the mouse"],
    [
        "https://editor.p5js.org/fanningo24/full/VZPF2QknO",
        "type a color in the box",
    ],
    ["https://editor.p5js.org/JazzyJasperZ/full/4OwzVY8Ro", "bouncing ball"],
    ["https://editor.p5js.org/muenchl24/full/zhKBxwxM2", "pong!"],
    [
        "https://editor.p5js.org/swagtime/full/eVcUy-nEU",
        "play pong against an ai with your mouse!",
    ],
    [
        "https://editor.p5js.org/Milesc25/full/IIzTPI0sC",
        "move in 3d with your arrow keys",
    ],
    ["https://editor.p5js.org/Pomatoes/full/q2vJCWs7F", "ball bouncing"],
    ["https://editor.p5js.org/levant25/full/GX-vZoB9y", "cool triangle bouncing"],
    ["https://editor.p5js.org/fanningo24/full/5uv8IQERA", "McDonalds art"],
    ["https://editor.p5js.org/swagtime/full/T6hvXSs45", "ball bouncing around"],
    ["https://editor.p5js.org/swagtime/full/N4d9Zc397", "arrows follow your mouse"],
    [
        "https://editor.p5js.org/L0MP/full/O_QHrtJFY",
        "space gun, arrow keys to move, space bar to shoot",
    ],
    [
        "https://editor.p5js.org/Milesc25/full/ovpQLyIJt",
        "walk through a tunnel with the up arrow",
    ],
    ["https://editor.p5js.org/adam7/full/78PvpTU0q", "a cool flag"],
    [
        "https://editor.p5js.org/depreistsullivanh24/full/frgILk-6A",
        "another cool flag",
    ],
    ["https://editor.p5js.org/muenchl24/full/_UpfXg7TI", "moving flag"],
    ["https://editor.p5js.org/muenchl24/full/OoT1nC9MT", "another awesome flag"],
    [
        "https://editor.p5js.org/L0MP/full/hgwwtssJO",
        "move the arrow keys to get the gold",
    ],
    [
        "https://editor.p5js.org/swagtime/full/CfA6ixz0s",
        "use left and right arrowkeys to animate this flag",
    ],
    ["https://editor.p5js.org/swagtime/full/7XmVtb2cb", "3D lorenz attractor!"],
    [
        "https://editor.p5js.org/goldman-wetzlerj24/full/AzaxXYjNI",
        "2D lorenz attractor",
    ],
    [
        "https://editor.p5js.org/goldman-wetzlerj24/full/8hBQKBdoj",
        "rope simulation (move the mouse)",
    ],
    [
        "https://editor.p5js.org/goldman-wetzlerj24/full/GcbeZN78t",
        "dynamical flow simulation",
    ],
]


def render_proj(project):
    print("<div class='proj-div'>")
    print(f"<p>{project[1]}</p>")
    print(
        f"<iframe width=600 height=600 src='about:blank' id={hash(project[0])}>{project[1]}</iframe><BR/>"
    )
    print(
        f"<button onclick=\"document.getElementById('{hash(project[0])}').contentWindow.location.replace('{project[0]}'); this.innerHTML = 'Reload demo'; document.getElementById('c{hash(project[0])}').hidden = false; document.getElementById('{hash(project[0])}').focus();\">Load demo</button>"
    )
    print(
        f"<button hidden id='c{hash(project[0])}' onclick=\"document.getElementById('{hash(project[0])}').contentWindow.location.replace('about:blank')\">Close Demo</button>"
    )
    print("</div>")


sys.stdout = open("index.html", "w")
print("<!DOCTYPE html>")
print(
    """
    <head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,600;1,300&display=swap" rel="stylesheet">
    <title>programming club projects</title>
    <style>
    body {
    	background: #1C1C1D;
    	color: #FFFFFF;
        font-family: Sans-Serif;
        font-family: 'JetBrains Mono', monospace;
        text-align: center;
    }
    .proj-div {
    	border-radius: 25px;
    	margin: auto;
    }
      h1 {
        font-size: 40px;
        color: #4EE37E
      }
    p {
        font-size: 30px;
        margin-top:25px;
        margin-left: 10%;
        margin-right:10%;
    }
    .items-center {
        text-align: center;
    }
    hr {
        border: none;
        margin-top: 30px;
        border-top: 3px dotted #fff;
        height: 3px;
        width: 60%;
    }
    button {
        background-color: #4EE37E;
        color: #1C1C1D;
        display: inline-block;
        padding: 15px 32px;
        border: none;
        font-family: 'JetBrains Mono', monospace;
        font-size:15px;
        border-radius: 12px;
        transition-duration: 500ms;
        transition: visibility 0s, opacity 0.5s linear;
        cursor: pointer;
    }
    [hidden] { display: none !important; }

    </style>
</head>
    """
)
print("<body>")
print(
    """
<h1>Projects Developed By Programming Club Members:</h1>
Press the <img src="code.png"/> button to see the code for any project here!
<BR>
Enjoy!
<HR/>
"""
)
print("<div class='items-center'>")
import random

random.shuffle(projects)
for proj in projects:
    render_proj(proj)
    print("<BR/>")
print("</div>")
print(
    """
<script>
window.addEventListener("keydown", function(e) {
    // space and arrow keys
    if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
        e.preventDefault();
    }
}, false);
</script>

"""
)
print("</body>")


sys.stdout.close()
