// ================= MATRIX BACKGROUND =================

// Get canvas
const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

// Fullscreen canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Characters (binary + symbols for better effect)
const chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const fontSize = 14;
const columns = Math.floor(canvas.width / fontSize);

// Create drops array
const drops = [];
for (let i = 0; i < columns; i++) {
    drops[i] = Math.random() * canvas.height;
}

// ================= DRAW FUNCTION =================
function drawMatrix() {

    // Dark transparent overlay (trail effect)
    ctx.fillStyle = "rgba(0, 0, 0, 0.08)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Green text
    ctx.fillStyle = "#00ff00";
    ctx.font = fontSize + "px monospace";

    // Loop columns
    for (let i = 0; i < drops.length; i++) {

        const text = chars.charAt(Math.floor(Math.random() * chars.length));

        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        // Reset drop randomly
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.97) {
            drops[i] = 0;
        }

        drops[i]++;
    }
}

// ================= LOOP =================
setInterval(drawMatrix, 35);


// ================= RESPONSIVE =================
window.addEventListener("resize", () => {

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

});