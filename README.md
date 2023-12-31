# Breddit

Breddit is a web application that allows users to post and interact with content in a Reddit-like fashion. It enables users to create posts, comment on them, and vote on their favorite content.
![Image 1](static/breddit/css/templates/images/posts.jpg)

## Features

- **User Authentication**: Users can sign up, log in, and log out. Authentication is required for posting, commenting, and voting.
![Image 1](static/breddit/css/templates/images/login.jpg)


- **Create Posts**: Authenticated users can create new posts with a title and content.
![Image 1](static/breddit/css/templates/images/makeapost.jpg)


- **Commenting**: Users can comment on posts, and discussions can happen within each post.
![Image 1](static/breddit/css/templates/images/comments.jpg)

- **Reply to Comments**: Users can reply to comments also reffered to as subcomments.
![Image 1](static/breddit/css/templates/images/reply.jpg)

**Find By ID**: Users can fetch a particular post by ID, implemented with a real time API.
![Image 1](static/breddit/css/templates/images/findbyid.jpg)

- **Voting System**: Users can upvote/like or downvote/unlike posts. The number of votes is displayed, and posts can be sorted by popularity.
![Image 1](static/breddit/css/templates/images/like.jpg)
- **Responsive Design**: The application is designed to work seamlessly on desktop and mobile devices.
 ![Image 1](static/breddit/css/templates/images/mobile.jpg)
- **Filtering**: Posts can be filtered by Fresh (latest), Hot (most liked), Trending (most comments).
![Image 1](static/breddit/css/templates/images/filters.jpg)

## Technologies Used

- **Python (Django Framework):** The core backend framework used to build and manage the application's server-side logic.

- **Django REST framework:** The Django REST framework was used to create APIs for serving and consuming data within the application. This technology stack allows Breddit to deliver a seamless user experience by providing real-time updates and interactions through the use of AJAX for making API calls.

- **HTML/CSS:** For creating the application's web pages and styling.

- **JavaScript** (AJAX for asynchronous operations): Used to implement asynchronous features such as making API calls without reloading the entire page, enabling dynamic updates.

- **Bootstrap for styling:** Bootstrap is used to provide a responsive and visually appealing user interface.

- **MySQL :** The database system used to store and manage data, including user accounts, posts, comments, and votes.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/andregrandon/Breddit.git

2. cd breddit
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt

3. python3 manage.py makemigrations
   python3 manage.py migrate

4. python3 manage.py createsuperuser

5. python3 manage.py runserver

6. Access the application in your web browser at http://localhost:8000/.


## Usage

Register a new user account or log in with the admin account created.
Create new posts, comment on existing posts, and interact with the content.