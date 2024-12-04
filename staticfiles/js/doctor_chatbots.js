async function sendMessageToBackend(doctorId, message) {
    try {
        const response = await fetch("/chatbot/chatbot/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                doctor_id: doctorId,
                message: message,
            }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data.message; // Backend only returns the message content
    } catch (err) {
        console.error("Fetch error:", err);
        return `Error: ${err.message}`; // Return error message
    }
}

function initializeChatbot(doctorId) {
    const chatbotForm = document.getElementById("chatbot-form");
    const chatbotInput = document.getElementById("chatbot-input");
    const chatbotMessages = document.getElementById("chatbot-messages");

    chatbotForm.onsubmit = async function (e) {
        e.preventDefault();

        const userMessage = chatbotInput.value.trim();
        if (!userMessage) return;

        // Call the backend to send the message
        const aiMessage = await sendMessageToBackend(doctorId, userMessage);

        // Handle display logic in HTML
        appendMessage("user", userMessage, null); // User messages have no avatar
        appendMessage(
            "doctor",
            aiMessage,
            doctorDetails[doctorId].image // Doctor avatar
        );

        // Clear the input box
        chatbotInput.value = "";
    };
}

// Function to add messages to the chat area
function appendMessage(sender, message, avatarUrl) {
    const chatbotMessages = document.getElementById("chatbot-messages");

    // Create the message container
    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container", `${sender}-message`);

    // If there is an avatar, add the avatar element
    if (avatarUrl) {
        const avatar = document.createElement("img");
        avatar.src = avatarUrl;
        avatar.alt = "avatar";
        avatar.classList.add("avatar");
        messageContainer.appendChild(avatar);
    } else if (sender === "user") {
        // If it's a user message and no avatar exists, generate a letter avatar
        const avatar = document.createElement("div");
        avatar.classList.add("avatar", "user-avatar");
        avatar.textContent = "U"; // Can be changed to the user's name initial
        messageContainer.appendChild(avatar);
    }

    // Add the message content
    const messageText = document.createElement("div");
    messageText.classList.add("message-text");
    messageText.textContent = message;
    messageContainer.appendChild(messageText);

    // Append to the chat message list
    chatbotMessages.appendChild(messageContainer);

    // Scroll to the bottom
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}
