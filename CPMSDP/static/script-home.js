// script.js

// Example: Validate form inputs
function validateForm() {
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');

    if (nameInput.value === '' || emailInput.value === '') {
        alert('Please fill in all fields.');
        return false;
    }
    return true;
}

// Example: Display a welcome message
function showWelcomeMessage() {
    const userName = prompt('Enter your name:');
    alert(`Welcome, ${userName}!`);
}

// Example: Fetch data from an API
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call your functions as needed
validateForm();
showWelcomeMessage();
fetchData();
