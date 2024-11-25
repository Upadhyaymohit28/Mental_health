document.addEventListener("DOMContentLoaded", function () {
    const chatbotForm = document.getElementById("chatbot-form");
    const chatbotInput = document.getElementById("chatbot-input");
    const chatbotMessages = document.getElementById("chatbot-messages");

    chatbotForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const userMessage = chatbotInput.value.trim();
        if (!userMessage) return;

        // Display user's message
        chatbotMessages.innerHTML += `<div class="user-message">You: ${userMessage}</div>`;

        // Clear input
        chatbotInput.value = "";

        // Send message to backend
        
        try {
            const response = await fetch("/chatbot/chatbot/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: "Hello, chatbot!" }),
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
        
            const data = await response.json();
            chatbotMessages.innerHTML += `<div class="ai-message">AI: ${data.message}</div>`;
        } catch (err) {
            chatbotMessages.innerHTML += `<div class="error-message">Error: ${err.message}</div>`;
            console.error("Fetch error:", err);
        }
        
        
    });
});
