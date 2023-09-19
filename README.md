# Breddit

Breddit is a web application that allows users to post and interact with content in a Reddit-like fashion. It enables users to create posts, comment on them, and vote on their favorite content.

## Features

- **User Authentication**: Users can sign up, log in, and log out. Authentication is required for posting, commenting, and voting.

- **Create Posts**: Authenticated users can create new posts with a title and content.

- **Commenting**: Users can comment on posts, and discussions can happen within each post.

- **Reply to Comments**: Users can reply to comments also reffered to as subcomments.

- **Voting System**: Users can upvote/like or downvote/unlike posts. The number of votes is displayed, and posts can be sorted by popularity.

- **Responsive Design**: The application is designed to work seamlessly on desktop and mobile devices.

- **Filtering**: Posts can be filtered by Fresh (latest), Hot (most liked), Trending (most comments).

## Technologies Used

- Python (Django Framework): The core backend framework used to build and manage the application's server-side logic.

- Django REST framework: The Django REST framework was used to create APIs for serving and consuming data within the application. This technology stack allows Breddit to deliver a seamless user experience by providing real-time updates and interactions through the use of AJAX for making API calls.

- HTML/CSS: For creating the application's web pages and styling.

- JavaScript (AJAX for asynchronous operations): Used to implement asynchronous features such as making API calls without reloading the entire page, enabling dynamic updates.

- Bootstrap for styling: Bootstrap is used to provide a responsive and visually appealing user interface.

- mySQL (or your preferred database)**: The database system used to store and manage data, including user accounts, posts, comments, and votes.

- Deployment Platform : The chosen platform for hosting and deploying the application to make it accessible online.


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