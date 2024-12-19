document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("liver-disease-form");
    form.addEventListener("submit", async function(event) {
        event.preventDefault();  // Prevent default form submission

        // Collect the input values from the form
        const data = {
            age: document.getElementById("age").value,
            gender: document.getElementById("gender").value,
            tot_bilirubin: document.getElementById("tot_bilirubin").value,
            direct_bilirubin: document.getElementById("direct_bilirubin").value,
            tot_proteins: document.getElementById("tot_proteins").value,
            albumin: document.getElementById("albumin").value,
            ag_ratio: document.getElementById("ag_ratio").value,
            sgpt: document.getElementById("sgpt").value,
            sgot: document.getElementById("sgot").value,
            alkphos: document.getElementById("alkphos").value
        };

        try {
            // Send the data to the Flask backend with correct headers
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Correct Content-Type for JSON
                },
                body: JSON.stringify(data),  // Send the data as JSON string
            });

            // Wait for the response and handle it
            const result = await response.json();

            // If the response contains an error, alert it
            if (result.error) {
                alert(`Error: ${result.error}`);
            } else {
                // Redirect to result page with prediction value
                window.location.href = `/result?prediction=${result.prediction}`;
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while communicating with the server.');
        }
    });
});
