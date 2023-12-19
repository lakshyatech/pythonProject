// script.js

document.addEventListener("DOMContentLoaded", function() {
    // Add an event listener to the form submission
    document.querySelector("form").addEventListener("submit", function(event) {
        // Check if the "Agree to Terms and Conditions" checkbox is checked
        if (!document.getElementById("agreeTAndC").checked) {
            // If not checked, prevent the form submission and show an alert
            alert("Please agree to the Terms and Conditions.");
            event.preventDefault();
        }
    });
});
