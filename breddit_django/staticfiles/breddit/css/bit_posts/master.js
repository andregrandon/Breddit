//FIND_BY_ID.HTML SCRIPT//

        document.addEventListener("DOMContentLoaded", function () {
            const findPostButton = document.getElementById("find-post-button");
            const postContainer = document.getElementById("post-container");
    
            findPostButton.addEventListener("click", function () {
                const postId = document.getElementById("post-id").value;
                const apiUrl = document.getElementById("find-post-form").getAttribute("data-url");  // Get the API URL
    
                // Make a POST request to the API endpoint
                fetch(apiUrl, {  // Use the retrieved API URL
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken"), // Include CSRF token
                    },
                    body: JSON.stringify({ post_id: postId }),
                })
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.error) {
                            postContainer.innerHTML = `<p>${data.error}</p>`;
                        } else {
                            // Display the retrieved post in the container
                            postContainer.innerHTML = `
                                <div class="post">
                                    <h2 class="post-title">${data.title}</h2>
                                    <p class="post-content">${data.content}</p>
                                    <p class="post-author">Author: ${data.user.username}</p>
                                </div>
                            `;
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                        postContainer.innerHTML = `<p>Error fetching post data.</p>`;
                    });
            });
    
            // Function to get the CSRF token from cookies
            function getCookie(name) {
                const value = `; ${document.cookie}`;
                const parts = value.split(`; ${name}=`);
                if (parts.length === 2) return parts.pop().split(";").shift();
            }
        });


        
//POST.HTML SCRIPT//
        document.addEventListener("DOMContentLoaded", function () {
            const postForm = document.getElementById("post-form");
            const postFormMessages = document.getElementById("post-form-messages");
            const postListContainer = document.getElementById("post-list-container"); 
         
            const formData = new FormData(postForm);
      
            postForm.addEventListener("submit", function (e) {
                e.preventDefault();
           
                const formData = new FormData(postForm);
    
                fetch(postForm.getAttribute("action"), {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken"), 
                    },
                })
                    .then((response) => response.json())
                    .then((data) => {
                        console.log(data);
    
                        postFormMessages.innerHTML = "<div class='alert alert-success'>Post created successfully.</div>";
    
                        const newPost = document.createElement("div");
                        newPost.classList.add("post");
                        newPost.innerHTML = `
                            <h2 class="post-title">${data.title}</h2>
                            <p class="post-content">${data.content}</p>
                            <p class="post-author">Author: ${data.user.username}</p>
                            <button class="like-button" data-post-id="${data.id}">
                                <i class="fas fa-thumbs-up"></i> Like
                            </button>
                            <span class="likes-count">0</span> likes
                        `;
                        postListContainer.prepend(newPost); 
    
                        postForm.reset();
                    })
                    .catch((error) => {
                        console.error("Error:", error);
    
                        postFormMessages.innerHTML = "<div class='alert alert-danger'>An error occurred while creating the post.</div>";
                    });
            });
    
            function getCookie(name) {
                
            }
        });        



    
//CREATE_COMMENT.HTML SCRIPT//
        document.addEventListener("DOMContentLoaded", function () {
            // Function to toggle the visibility of replies for a comment
            function toggleReplies(comment) {
                const repliesContainer = comment.querySelector(".replies");
                const openCloseButton = comment.querySelector(".open-close-replies-button");
                const replyCount = repliesContainer.querySelectorAll(".reply").length; // Count the replies
    
                if (repliesContainer.style.display === "none" || repliesContainer.style.display === "") {
                    repliesContainer.style.display = "block";
                    openCloseButton.textContent = `Close Replies (${replyCount})`;
                } else {
                    repliesContainer.style.display = "none";
                    openCloseButton.textContent = `Open Replies (${replyCount})`;
                }
            }
    
            // Initialize the reply count for all comment sections
            const commentSections = document.querySelectorAll(".comment");
            commentSections.forEach(function (comment) {
                const openCloseButton = comment.querySelector(".open-close-replies-button");
                const repliesContainer = comment.querySelector(".replies");
                const replyCount = repliesContainer.querySelectorAll(".reply").length; // Count the replies
                openCloseButton.textContent = `Open Replies (${replyCount})`;
            });
    
            // Attach click event listeners to all open/close buttons
            const openCloseButtons = document.querySelectorAll(".open-close-replies-button");
            openCloseButtons.forEach(function (openCloseButton) {
                openCloseButton.addEventListener("click", function (event) {
                    event.preventDefault();
                    const comment = openCloseButton.closest(".comment");
                    toggleReplies(comment);
                });
            });
    
            // Attach click event listeners to the like buttons
            const likeButtons = document.querySelectorAll(".like-button");
            likeButtons.forEach(function (likeButton) {
                likeButton.addEventListener("click", function (event) {
                    event.preventDefault();
                    const postId = likeButton.getAttribute("data-post-id");
                });
            });
        });