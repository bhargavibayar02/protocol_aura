// ================= OSI ANIMATION (NO SHAKE FINAL) =================

const canvas = document.getElementById("packetCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = 320;

const layers = [
    "Application (7)",
    "Presentation (6)",
    "Session (5)",
    "Transport (4)",
    "Network (3)",
    "Data Link (2)",
    "Physical (1)"
];

const labels = [
    "Data",
    "Data",
    "Data",
    "TCP Segment",
    "IP Packet",
    "Frame",
    "Bits"
];

let yPos = [];
let currentLayer = 0;
let direction = 1; // 1 = down, -1 = up
let moving = true;

let packet = {
    x: 350,
    y: 0,
    speed: 3
};


// ================= INIT =================
function initOSI(){

    yPos = [];

    let gap = canvas.height / (layers.length + 1);

    for (let i = 0; i < layers.length; i++) {
        yPos.push(gap * (i + 1));
    }

    packet.y = yPos[0];
}


// ================= DRAW =================
function drawLayers(){

    ctx.font = "15px monospace";

    layers.forEach((layer, i) => {

        let y = yPos[i];

        ctx.strokeStyle = "cyan";
        ctx.strokeRect(80, y - 15, 260, 30);

        if (i === currentLayer){
            ctx.fillStyle = "rgba(0,255,255,0.2)";
            ctx.fillRect(80, y - 15, 260, 30);
        }

        ctx.fillStyle = "cyan";
        ctx.fillText(layer, 90, y + 5);
    });
}

function drawPacket(){

    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.arc(packet.x, packet.y, 8, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "white";
    ctx.fillText(labels[currentLayer], packet.x + 15, packet.y + 5);
}


// ================= ANIMATION =================
function animateOSI(){

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawLayers();
    drawPacket();

    let targetY = yPos[currentLayer];

    if (moving){

        let distance = targetY - packet.y;

        // MOVE WITHOUT OVERSHOOT
        if (Math.abs(distance) > packet.speed){
            packet.y += Math.sign(distance) * packet.speed;
        } 
        else {
            // SNAP EXACTLY (NO SHAKE)
            packet.y = targetY;
            moving = false;

            // PAUSE BEFORE NEXT MOVE
            setTimeout(() => {

                currentLayer += direction;

                if (currentLayer === layers.length - 1 || currentLayer === 0){
                    direction *= -1;
                }

                moving = true;

            }, 600);
        }
    }

    requestAnimationFrame(animateOSI);
}


// ================= INIT =================
window.onload = function(){
    initOSI();
    animateOSI();
};


// ================= RESPONSIVE =================
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = 320;
    initOSI();
});