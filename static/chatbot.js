
function sendMessage() {
    const userMessage = document.getElementById('user-input').value;

    // Send user message to Django backend
    fetch('/get_chatbot_response/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken'),  // Ensure you have CSRF token
        },
        body: 'user_message=' + encodeURIComponent(userMessage),
    })
    .then(response => response.json())
    .then(data => {
        const chatLog = document.getElementById('chat-log');
        chatLog.innerHTML += '<p>User: ' + userMessage + '</p>';
        chatLog.innerHTML += '<p>Chatbot: ' + data.chatbot_response + '</p>';
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
