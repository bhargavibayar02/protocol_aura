// ================= PACKET FLOW SIMULATION =================

const canvas = document.getElementById("packetCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = 350;

// OSI Layers
const layers = [
    "Application",
    "Presentation",
    "Session",
    "Transport",
    "Network",
    "Data Link",
    "Physical"
];

// Encapsulation labels
const encapsulation = [
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
let direction = "down"; // down = encapsulation, up = decapsulation

let packet = {
    x: 400,
    y: 0,
    size: 10
};

// ================= INIT =================
function initFlow() {

    yPos = [];
    let gap = canvas.height / (layers.length + 1);

    for (let i = 0; i < layers.length; i++) {
        yPos.push(gap * (i + 1));
    }

    packet.y = yPos[0];
}

// ================= DRAW LAYERS =================
function drawLayers() {

    ctx.font = "15px monospace";

    layers.forEach((layer, i) => {

        let y = yPos[i];

        // Box
        ctx.strokeStyle = "cyan";
        ctx.strokeRect(100, y - 15, 250, 30);

        // Text
        ctx.fillStyle = "cyan";
        ctx.fillText(layer, 110, y + 5);

        // Highlight active layer
        if (i === currentLayer) {
            ctx.fillStyle = "rgba(0,255,255,0.2)";
            ctx.fillRect(100, y - 15, 250, 30);
        }
    });
}

// ================= DRAW PACKET =================
function drawPacket() {

    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.arc(packet.x, packet.y, packet.size, 0, Math.PI * 2);
    ctx.fill();

    // Label
    ctx.fillStyle = "white";
    ctx.fillText(encapsulation[currentLayer], packet.x + 15, packet.y + 5);
}

// ================= ANIMATION =================
function animateFlow() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawLayers();
    drawPacket();

    let targetY = yPos[currentLayer];

    // Smooth move
    packet.y += (targetY - packet.y) * 0.1;

    // Move layer logic
    if (Math.abs(packet.y - targetY) < 1) {

        setTimeout(() => {

            if (direction === "down") {
                currentLayer++;

                // Reached Physical → reverse
                if (currentLayer >= layers.length - 1) {
                    direction = "up";
                }

            } else {
                currentLayer--;

                // Back to Application → reverse again
                if (currentLayer <= 0) {
                    direction = "down";
                }
            }

        }, 400);
    }

    requestAnimationFrame(animateFlow);
}

// ================= INIT =================
window.addEventListener("load", () => {
    initFlow();
    animateFlow();
});

// ================= RESPONSIVE =================
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = 350;
    initFlow();
});