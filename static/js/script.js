document.addEventListener('DOMContentLoaded', function () {
    // Attach a submit event listener to the form
    document.getElementById('routeForm').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Fetch form data
        const formData = new FormData(event.target);

        // Send a POST request to the server
        fetch('/search_route', {
            method: 'POST',
            body: formData,
        })
