# DeepSolv_InstaClone

## Overview
This is a clone of instagram backend services, with features such as Sign up, Login, creating post etc.
User Registration
User Login
Create Posts with following details:
Caption
Post Image/Video URL
Background Music URL (Optional)
Post Category like (Tech, Entertainment, Business etc.)
Datetime Posted
Publisher User ID
Any other attribute you find helpful
(Note: Make sure that you implement a mechanism for validating the user before processing the create request)
View a user profile. (Profile should reflect all the information we usually see on Instagram when we visit a user profile)
Follow other users.
Get contents posted by the logged in user.
Get contents posted by other users on the platform.
Get details of a specific post (Actual post, post by user, likes count, comments count, and other relevant details)
Like a post.
Get all users who liked a particular post
Comment on a post.
Get all users and their comments on a particular post.
Implement user feed, where a user can get a list of posts based on the users they follow, in a reverse chronological order (Latest post on top). This should be paginated.

## Features
- **Login and Sign up**: Users can register and again login.
- **Post creation**: User can create new post, with all features such a Caption, background music etc. 
- **View and follow other users**: Users can search other users and receive required data such as posts made by a particular user.
- **Interaction with posts**: User can like, and comment on a post, and view other comments.

## Technologies Used
- **Backend**: FastAPI

## Getting Started

### Prerequisites

### Installation
1. Create a folder

2. Clone the repository:
   ```bash
   git clone https://github.com/streetcodec/DeepSolv_InstaClone.git
   ```

3. Install dependencies:
   ```bash
   pip install "fastapi[standard]"
   
   ```

4. Start the development server:
   ```bash
    fastapi dev main.py
   ```

4. Open the application in your browser:
   ```
   (http://127.0.0.1:8000/items/5?q=somequery.)
   ```

## Folder Structure
```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
└── src
    ├── activity
    │   ├── __init__.py
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── models.cpython-310.pyc
    │   │   ├── service.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── schemas.py
    │   ├── service.py
    │   └── views.py
    ├── api.py
    ├── auth
    │   ├── enums.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── enums.cpython-310.pyc
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── models.cpython-310.pyc
    │   │   ├── schemas.cpython-310.pyc
    │   │   ├── service.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── schemas.py
    │   ├── service.py
    │   └── views.py
    ├── database.py
    ├── db.sql
    ├── .DS_Store
    ├── __init__.py
    ├── main.py
    ├── post
    │   ├── __init__.py
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── models.cpython-310.pyc
    │   │   ├── schemas.cpython-310.pyc
    │   │   ├── service.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── schemas.py
    │   ├── service.py
    │   └── views.py
    ├── profile
    │   ├── __init__.py
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── schemas.cpython-310.pyc
    │   │   ├── service.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── schemas.py
    │   ├── service.py
    │   └── views.py
    └── __pycache__
        ├── api.cpython-310.pyc
        ├── database.cpython-310.pyc
        ├── __init__.cpython-310.pyc
        └── main.cpython-310.pyc
```


## Contributing
Feel free to open issues and submit pull requests to improve the project. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

---
