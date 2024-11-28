document.addEventListener("DOMContentLoaded", function () {
    const chatbotForm = document.getElementById("chatbot-form");
    const chatbotMessages = document.getElementById("chatbot-messages");
    const chatHeader = document.getElementById("chat-header");

    // 医生聊天初始化逻辑
    window.startDoctorChat = function (doctorId) {
        const selectedDoctor = doctorDetails[doctorId];

        // 更新聊天头部为医生头像、名字和简介
        chatHeader.innerHTML = `
           <div class="doctor-chat-info">
               <img src="${selectedDoctor.image}" class="doctor-avatar" alt="${selectedDoctor.name}">
               <div class="doctor-info">
                   <div class="doctor-name-specialty">
                       <span class="doctor-chat-name">${selectedDoctor.name}</span>
                       <span class="doctor-chat-specialty">${selectedDoctor.specialty}</span>
                   </div>
                   <span class="doctor-description">${selectedDoctor.description}</span>
               </div>
           </div>
        `;

        // 显示输入框并清空消息区域
        chatbotForm.style.display = "flex";
        chatbotMessages.classList.remove("empty");
        chatbotMessages.innerHTML = "";

        // 更新医生卡片选中状态
        document.querySelectorAll('.doctor-item').forEach(item => item.classList.remove('selected'));
        document.querySelector(`.doctor-item:nth-child(${doctorId + 1})`).classList.add('selected');

        // 调用 doctor_chatbots.js 中的初始化逻辑
        initializeChatbot(doctorId);
    };

    // 从 URL 获取医生 ID 参数
    const urlParams = new URLSearchParams(window.location.search);
    const doctorId = urlParams.get('doctor_id');

    if (doctorId) {
        // 自动初始化选中的医生聊天
        startDoctorChat(Number(doctorId));
    }
});
