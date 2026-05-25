// ================= PROTOCOL MAPPING =================
const layerProtocols = {
    "Application": ["HTTP", "DNS"],
    "Presentation": ["TLS"],
    "Session": ["RPC"],
    "Transport": ["TCP", "UDP"],
    "Network": ["IP"],
    "Data Link": ["ETHERNET"],
    "Physical": ["FIBER"]
};


// ================= NAVIGATION =================
function go(protocol){

    let form = document.createElement("form");
    form.method = "POST";
    form.action = "/analyze";

    let input = document.createElement("input");
    input.type = "hidden";
    input.name = "protocol";
    input.value = protocol;

    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
}


// ================= SHOW PROTOCOL OPTIONS =================
function showProtocols(layer){

    let container = document.getElementById("protocolList");

    if (!container) return;

    container.innerHTML = "";

    let protocols = layerProtocols[layer];

    if (!protocols) return;

    protocols.forEach(p => {

        let btn = document.createElement("button");
        btn.innerText = p;

        btn.onclick = () => go(p);

        container.appendChild(btn);
    });
}


// ================= HOVER TOOLTIP =================
function showHint(text){

    let hint = document.getElementById("hintBox");

    if (!hint) return;

    hint.innerText = text;
    hint.style.display = "block";
}

function hideHint(){
    let hint = document.getElementById("hintBox");
    if (hint) hint.style.display = "none";
}


// ================= PACKET FLOW TRIGGER =================
function startFlowAnimation(){

    let canvas = document.getElementById("packetCanvas");
    if (!canvas) return;

    let ctx = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = 200;

    let x = 0;

    function draw(){

        ctx.clearRect(0,0,canvas.width,canvas.height);

        ctx.fillStyle = "cyan";
        ctx.font = "14px monospace";

        const layers = [
            "Application",
            "Presentation",
            "Session",
            "Transport",
            "Network",
            "Data Link",
            "Physical"
        ];

        layers.forEach((layer, i) => {
            ctx.fillText(layer, 50 + i * 150, 50);
        });

        // packet
        ctx.fillStyle = "red";
        ctx.beginPath();
        ctx.arc(x, 100, 6, 0, Math.PI * 2);
        ctx.fill();

        x += 3;
        if (x > canvas.width) x = 0;

        requestAnimationFrame(draw);
    }

    draw();
}


// ================= AUTO INIT =================
window.onload = function(){
    startFlowAnimation();
};