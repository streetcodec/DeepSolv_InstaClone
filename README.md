# DeepSolv_InstaClone

## Overview
This is a clone of instagram backend services, with features such as Sign up, Login, creating post etc.

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
