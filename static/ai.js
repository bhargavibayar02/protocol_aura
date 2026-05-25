// ================= AI ASK FUNCTION =================
async function askAI(protocol) {

    let question = prompt("Ask any question about " + protocol + " (e.g., attacks, working, timing):");

    // If user cancels
    if (question === null) return;

    // Empty question fallback
    if (question.trim() === "") {
        question = "Explain in detail";
    }

    let aiBox = document.getElementById("aiBox");

    // Typing animation (loading)
    aiBox.innerHTML = " Thinking...";

    try {
        let response = await fetch('/ai_chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `protocol=${protocol}&question=${encodeURIComponent(question)}`
        });

        let data = await response.json();

        typeEffect(aiBox, data.response);

    } catch (error) {
        aiBox.innerHTML = "Error connecting to AI engine.";
    }
}


// ================= TYPING EFFECT =================
function typeEffect(element, text) {

    element.innerHTML = "";
    let i = 0;

    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, 15);
        }
    }

    typing();
}


// ================= OPTIONAL QUICK QUESTIONS =================
function quickAsk(protocol, type) {

    let questions = {
        "working": "Explain working in detail",
        "attack": "Explain attacks and mitigation",
        "timing": "Explain timing and performance",
        "realworld": "Explain real-world usage"
    };

    let aiBox = document.getElementById("aiBox");
    aiBox.innerHTML = " Thinking...";

    fetch('/ai_chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `protocol=${protocol}&question=${questions[type]}`
    })
    .then(res => res.json())
    .then(data => {
        typeEffect(aiBox, data.response);
    });
}