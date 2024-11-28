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
        return data.message; // 后端仅返回消息内容
    } catch (err) {
        console.error("Fetch error:", err);
        return `Error: ${err.message}`; // 返回错误消息
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

        // 调用后端发送消息
        const aiMessage = await sendMessageToBackend(doctorId, userMessage);

        // 在 HTML 中处理展示逻辑
        appendMessage("user", userMessage, null); // 用户消息无头像
        appendMessage(
            "doctor",
            aiMessage,
            doctorDetails[doctorId].image // 医生头像
        );

        // 清空输入框
        chatbotInput.value = "";
    };
}

// 用于向消息区域添加消息的函数
function appendMessage(sender, message, avatarUrl) {
    const chatbotMessages = document.getElementById("chatbot-messages");

    // 创建消息容器
    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container", `${sender}-message`);

    // 如果有头像，添加头像元素
    if (avatarUrl) {
        const avatar = document.createElement("img");
        avatar.src = avatarUrl;
        avatar.alt = "avatar";
        avatar.classList.add("avatar");
        messageContainer.appendChild(avatar);
    } else if (sender === "user") {
        // 如果是用户消息且没有头像，生成字母头像
        const avatar = document.createElement("div");
        avatar.classList.add("avatar", "user-avatar");
        avatar.textContent = "U"; // 可改为用户的名字首字母
        messageContainer.appendChild(avatar);
    }

    // 添加消息内容
    const messageText = document.createElement("div");
    messageText.classList.add("message-text");
    messageText.textContent = message;
    messageContainer.appendChild(messageText);

    // 添加到消息列表
    chatbotMessages.appendChild(messageContainer);

    // 滚动到底部
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}
