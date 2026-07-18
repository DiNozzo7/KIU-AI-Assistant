document.getElementById("submit_question").onclick = function () {
    const answerBox = document.getElementById("answer");
    const userQuestion = document.getElementById("question").value;

    answerBox.textContent = "Thinking...";

    fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: userQuestion
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.top_score < 0.5) {
            answerBox.textContent = "I do not have information about that.";
        } else {
            answerBox.textContent = data.answer;
        }
    })
};