// Attaching an event listener to the element with id 'copyButton'. 
// This will trigger when the button is clicked
document.getElementById("copyButton").addEventListener("click", function() {
    
    // Get the email text from the element with id 'emailToCopy'
    let email = document.getElementById('emailToCopy').innerText;
  
    // Use the Clipboard API's writeText method to copy the text
    navigator.clipboard.writeText(email).then(function() {
      
        // Success! Email is on clipboard, now notify the user
        alert("Email copied to clipboard!");
      
    }).catch(function() {
      
        // Something went wrong, handle the error
        alert("Failed to copy email :(");
      
    });
});