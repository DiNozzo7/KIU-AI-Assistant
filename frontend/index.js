let userQuestion;

document.getElementById("submit_question").onclick = function () {
    userQuestion = document.getElementById("question").value;

    fetch("http://127.0.0.1:8000/ask", {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            question: userQuestion
        })
    })
    .then(response => response.json())
    .then(data => document.getElementById("answer").textContent = data.answer);
};