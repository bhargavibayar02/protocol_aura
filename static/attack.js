// ================= LOAD ATTACK DATA =================
function loadAttack(layer){

    fetch('/get_attack', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'layer=' + layer
    })
    .then(response => response.json())
    .then(data => {

        let container = document.getElementById("attackInfo");
        container.innerHTML = "";

        if (!data || data.length === 0) {
            container.innerHTML = "<p>No attack data available</p>";
            return;
        }

        data.forEach((attack, index) => {

            let html = `
                <div class="card">
                    <h3>${attack.name}</h3>

                    <p><b>Attack Flow:</b></p>
                    <ul>
            `;

            attack.flow.forEach(step => {
                html += `<li>${step}</li>`;
            });

            html += `
                    </ul>

                    <p><b>Impact:</b> ${attack.impact}</p>
                    <p><b>Detection:</b> ${attack.detection}</p>
                    <p><b>Mitigation:</b> ${attack.mitigation}</p>
                </div>
            `;

            container.innerHTML += html;
        });

        startAttackAnimation(layer);
    });
}


// ================= PACKET ANIMATION =================
function startAttackAnimation(layer){

    const canvas = document.getElementById("attackCanvas");
    const ctx = canvas.getContext("2d");

    canvas.width = 800;
    canvas.height = 300;

    let packets = [];

    // create packets
    for (let i = 0; i < 40; i++) {
        packets.push({
            x: 50,
            y: Math.random() * 250,
            speed: 2 + Math.random() * 3
        });
    }

    function draw(){

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Labels
        ctx.fillStyle = "cyan";
        ctx.font = "16px monospace";
        ctx.fillText("Attacker", 50, 20);
        ctx.fillText("Target Server", 650, 20);

        // Draw attacker + server boxes
        ctx.strokeStyle = "cyan";
        ctx.strokeRect(20, 50, 100, 100);
        ctx.strokeRect(650, 50, 100, 100);

        // Packets
        packets.forEach(p => {

            ctx.fillStyle = "red";
            ctx.fillRect(p.x, p.y, 5, 5);

            p.x += p.speed;

            // reset packet
            if (p.x > 650) {
                p.x = 50;
                p.y = Math.random() * 250;
            }
        });

        requestAnimationFrame(draw);
    }

    draw();
}