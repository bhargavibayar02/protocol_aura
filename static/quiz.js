// ================= QUIZ STATE =================
let currentQ = 0;
let score = 0;
let answered = false;


// ================= START QUIZ =================
function startQuiz(){

    if (!quizData || quizData.length === 0){
        document.getElementById("quizBox").innerHTML = "No quiz available";
        return;
    }

    currentQ = 0;
    score = 0;

    showQuestion();
}


// ================= SHOW QUESTION =================
function showQuestion(){

    answered = false;

    let q = quizData[currentQ];

    let box = document.getElementById("quizBox");

    let html = `
        <div class="card">
            <h3>Question ${currentQ + 1} / ${quizData.length}</h3>
            <p>${q.q}</p>
    `;

    q.options.forEach(option => {
        html += `<button class="optionBtn" onclick="selectAnswer('${option}')">${option}</button>`;
    });

    html += `
        <div id="feedback"></div>
        <br>
        <button onclick="nextQuestion()" id="nextBtn" disabled>Next</button>
        </div>
    `;

    box.innerHTML = html;
}


// ================= SELECT ANSWER =================
function selectAnswer(selected){

    if (answered) return;

    answered = true;

    let correct = quizData[currentQ].answer;

    let buttons = document.getElementsByClassName("optionBtn");

    for (let btn of buttons){

        if (btn.innerText === correct){
            btn.style.background = "green";
            btn.style.color = "black";
        }

        if (btn.innerText === selected && selected !== correct){
            btn.style.background = "red";
            btn.style.color = "white";
        }

        btn.disabled = true;
    }

    let feedback = document.getElementById("feedback");

    if (selected === correct){
        score++;
        feedback.innerHTML = "<p style='color:lime;'>✔ Correct!</p>";
    } else {
        feedback.innerHTML = `<p style='color:red;'>✖ Wrong! Correct: ${correct}</p>`;
    }

    document.getElementById("nextBtn").disabled = false;
}


// ================= NEXT QUESTION =================
function nextQuestion(){

    currentQ++;

    if (currentQ >= quizData.length){
        showResult();
    } else {
        showQuestion();
    }
}


// ================= SHOW RESULT =================
function showResult(){

    let box = document.getElementById("quizBox");

    let percent = Math.round((score / quizData.length) * 100);

    let grade = "";

    if (percent >= 80) grade = "Excellent ";
    else if (percent >= 60) grade = "Good ";
    else grade = "Needs Improvement ⚠";

    box.innerHTML = `
        <div class="card">
            <h2>Quiz Completed</h2>
            <p><b>Score:</b> ${score} / ${quizData.length}</p>
            <p><b>Percentage:</b> ${percent}%</p>
            <p><b>Performance:</b> ${grade}</p>

            <br>
            <button onclick="startQuiz()"> Retake Quiz</button>
        </div>
    `;
}