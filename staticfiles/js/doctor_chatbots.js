document.addEventListener("DOMContentLoaded", function () {
    const chatbotForm = document.getElementById("chatbot-form");
    const chatbotInput = document.getElementById("chatbot-input");
    const chatbotMessages = document.getElementById("chatbot-messages");
    const doctorIdField = document.getElementById("doctor-id");

    chatbotForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const userMessage = chatbotInput.value.trim();
        if (!userMessage) return;

        // Display the user's message
        chatbotMessages.innerHTML += `<div class="user-message">You: ${userMessage}</div>`;
        chatbotInput.value = ""; // Clear the input field

        const doctorId = doctorIdField ? doctorIdField.value : null;

        try {
            const response = await fetch("/chatbot/chatbot/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: userMessage, doctor_id: doctorId }),
            });

            const data = await response.json();
            if (data.message) {
                chatbotMessages.innerHTML += `<div class="ai-message">AI: ${data.message}</div>`;
            } else {
                chatbotMessages.innerHTML += `<div class="error-message">Error: ${data.error || "Unknown error"}</div>`;
            }
        } catch (err) {
            chatbotMessages.innerHTML += `<div class="error-message">Error: ${err.message}</div>`;
        }
    });
});

function startDoctorChat(doctorId) {
    const doctorIdField = document.getElementById("doctor-id");
    if (doctorIdField) {
        doctorIdField.value = doctorId;
    }
    document.getElementById("chatbot-container").style.display = "block";
}
