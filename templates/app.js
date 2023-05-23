// JavaScript code for power consumption measurement application

document.getElementById("powerForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var pid = document.getElementById("pidInput").value;
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/power_consumption");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        if (xhr.status === 200) {
            var powerInfo = JSON.parse(xhr.responseText);
            document.getElementById("powerInfo").innerHTML = JSON.stringify(powerInfo, null, 2);
        } else {
            console.log("Error:", xhr.responseText);
        }
    };
    xhr.send("pid=" + pid);
});
