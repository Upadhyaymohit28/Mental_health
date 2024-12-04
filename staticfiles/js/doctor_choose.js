document.addEventListener("DOMContentLoaded", function () {
    const chatbotForm = document.getElementById("chatbot-form");
    const chatbotMessages = document.getElementById("chatbot-messages");
    const chatHeader = document.getElementById("chat-header");

    // Doctor chat initialization logic
    window.startDoctorChat = function (doctorId) {
        const selectedDoctor = doctorDetails[doctorId];

        // Update chat header with doctor's avatar, name, and description
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

        // Display the input box and clear the message area
        chatbotForm.style.display = "flex";
        chatbotMessages.classList.remove("empty");
        chatbotMessages.innerHTML = "";

        // Update selected state for the doctor card
        document.querySelectorAll('.doctor-item').forEach(item => item.classList.remove('selected'));
        document.querySelector(`.doctor-item:nth-child(${doctorId + 1})`).classList.add('selected');

        // Call the initialization logic from doctor_chatbots.js
        initializeChatbot(doctorId);
    };

    // Get doctor ID parameter from the URL
    const urlParams = new URLSearchParams(window.location.search);
    const doctorId = urlParams.get('doctor_id');

    if (doctorId) {
        // Automatically initialize chat for the selected doctor
        startDoctorChat(Number(doctorId));
    }
});
