async function sendMessage() {

    const userInput = document.getElementById("prompt").value;

    const response = await fetch("http://localhost:5000/api/chat", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            prompt: userInput
        })
    });

    const data = await response.json();

    document.getElementById("response").innerText = data.reply;
}
