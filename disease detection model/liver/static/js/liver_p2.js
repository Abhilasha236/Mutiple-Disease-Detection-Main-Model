window.onload = function() {
    // Display the result
    document.getElementById("result").innerHTML = `
        <h2>${resultText}</h2>
        <p>Based on your inputs, the result shows: <strong>${resultText}</strong>.</p>
    `;
};

function goBack() {
    window.location.href = "liver_p1.html";
}

function consultDoc(){
    window.location.href = "doctor_details.html"
}
