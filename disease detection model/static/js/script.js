function showForm(type) {
    // Hide all forms initially
    document.querySelectorAll('.form-container').forEach(form => {
        form.style.display = 'none';
    });

    // Show the selected form
    if (type === 'heart') {
        document.querySelector('.heart-form').style.display = 'block';
    } else if (type === 'kidney') {
        document.querySelector('.kidney-form').style.display = 'block';
    } else if (type === 'tb') {
        document.querySelector('.tb-form').style.display = 'block';
    } else if (type === 'liver') {
        document.querySelector('.liver-form').style.display = 'block'; // Show Liver form
    } else if (type === 'more') {
        document.querySelector('.more-form').style.display = 'block';
    }
}

// Prevent default form submission
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent the form from submitting
        // You can handle form data here, e.g., display a message or process the input
        alert('Form submitted successfully!');
    });
});
