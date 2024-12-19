document.getElementById("heart-disease-form").addEventListener("submit", function(event) {
    // Prevent default form submission so that we can validate before submission
    event.preventDefault();

    // Collect input values from the form
    let age = document.getElementById("age").value;
    let sex = document.getElementById("sex").value;
    let chestPain = document.getElementById("chestPain").value;
    let trestbps = document.getElementById("trestbps").value;
    let cholesterol = document.getElementById("cholesterol").value;
    let fbsOver120 = document.getElementById("fbsOver120").value;
    let ekg = document.getElementById("ekg").value;
    let maxHr = document.getElementById("maxHr").value;
    let exerciseAngina = document.getElementById("exerciseAngina").value;
    let stDepression = document.getElementById("stDepression").value;
    let slope = document.getElementById("slope").value;
    let ca = document.getElementById("ca").value;
    let thal = document.getElementById("thal").value;

    // If validation passes, allow form submission
    document.getElementById("heart-disease-form").submit();
});
