document.querySelector("form").addEventListener("submit", function(event) {
    var username = document.getElementById("username").value;
    if (!username) {
        alert("Please enter your name!");
        event.preventDefault();
    }
    else{
        alert("Hello, " + username + "!");
    }
});
