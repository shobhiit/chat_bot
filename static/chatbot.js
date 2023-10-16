
function sendMessage() {
    // Get user input and clear the input field
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value;
    userInput.value = '';

    // Append user message to chat logs
    appendMessage('user-message', 'User: ' + userMessage);

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
        // Append chatbot message to chat logs
        appendMessage('chatbot-message', 'Chatbot: ' + data.chatbot_response);
    });
}

function appendMessage(className, text) {
    // Create a new message element
    const messageContainer = document.getElementById('chat-log');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    // Create and append the user or chatbot message
    const messageParagraph = document.createElement('p');
    messageParagraph.classList.add(className);
    messageParagraph.innerHTML = text;  // Use innerHTML to handle HTML content
    messageElement.appendChild(messageParagraph);

    // Append the message element to the chat logs
    messageContainer.appendChild(messageElement);
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


function handleKeyDown(event) {
    // Check if the pressed key is Enter (key code 13)
    if (event.keyCode === 13) {
        sendMessage();
    }
}
