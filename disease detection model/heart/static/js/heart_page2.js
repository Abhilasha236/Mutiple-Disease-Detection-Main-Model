window.onload = function() {
    // Get stored values
    let age = localStorage.getItem("age");
    let sex = localStorage.getItem("sex");
    let chestPain = localStorage.getItem("chestPain");
    let cholesterol = localStorage.getItem("cholesterol");
    let fbsOver120 = localStorage.getItem("fbsOver120");
    let ekg = localStorage.getItem("ekg");
    let maxHr = localStorage.getItem("maxHr");
    let exerciseAngina = localStorage.getItem("exerciseAngina");

    // // Simplified heart disease calculation logic
    // let resultText = "Heart Disease Absent";
    // if (chestPain === "yes" || fbsOver120 === "yes" || exerciseAngina === "yes" || cholesterol > 200) {
    //     resultText = "Heart Disease Present";
    // }

    // // Display the result
    // document.getElementById("result").innerHTML = `
    //     <h2>${resultText}</h2>
    //     <p>Based on your inputs, the result shows: <strong>${resultText}</strong>.</p>
    // `;
};

function goBack() {
    window.location.href = "heart_page1.html";
}
