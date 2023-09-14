document.addEventListener("DOMContentLoaded", function () {
    const postForm = document.getElementById("post-form");
    const postFormMessages = document.getElementById("post-form-messages");

    postForm.addEventListener("submit", function (e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(postForm);

        // Make an AJAX POST request to the form's action attribute
        fetch(postForm.getAttribute("action"), {  // Use the form's action attribute
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": getCookie("csrftoken"), // Include CSRF token for security
            },
        })
            .then((response) => response.json())
            .then((data) => {
                // Handle the response data as needed
                console.log(data);

                // Display a success message or perform other actions
                postFormMessages.innerHTML = "<div class='alert alert-success'>Post created successfully.</div>";
            })
            .catch((error) => {
                console.error("Error:", error);

                // Display an error message or perform error handling
                postFormMessages.innerHTML = "<div class='alert alert-danger'>An error occurred while creating the post.</div>";
            });
    });

    // Function to get the CSRF token from cookies (you may need this)
    function getCookie(name) {
        // ...
    }
});
