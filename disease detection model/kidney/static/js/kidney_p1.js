document.getElementById('kidney-disease-form').addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData.entries()); // Convert to JSON format

        try {
            // Send the data as JSON to the server
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            // Parse and handle the server's response
            const result = await response.json();
            if (response.ok) {
                window.location.href = `/result?prediction=${encodeURIComponent(result.prediction)}`;
            } else {
                alert(`Error: ${result.error}`);
            }
        } catch (error) {
            alert(`Failed to send data: ${error.message}`);
        }
});
