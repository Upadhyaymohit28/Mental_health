function startDoctorChat(doctorId) {
    console.log(`Starting chat with doctor ID: ${doctorId}`);
    const doctorIdField = document.getElementById("doctor-id");
    if (doctorIdField) {
        doctorIdField.value = doctorId;
    }
    document.getElementById("chatbot-container").style.display = "block";

    const chatbotMessages = document.getElementById("chatbot-messages");
    chatbotMessages.innerHTML += `<div class="info-message">You are now chatting with ${getDoctorName(doctorId)}.</div>`;
}

function getDoctorName(doctorId) {
    const doctorProfiles = {
        1: "Dr. Jane Smith",
        2: "Dr. John Doe",
        3: "Dr. Emily White",
    };
    return doctorProfiles[doctorId] || "Unknown Doctor";
}
