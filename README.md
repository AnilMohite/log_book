# Log Book
This repository contains a Flask application that allows users to create and manage multiple log books. The application is integrated with a MySQL database and uses HTML, CSS, JavaScript, and Bootstrap 5 for the frontend.

## Prerequisites
Before setting up the application, ensure that you have the following prerequisites installed:
- Python 3.x
- MySQL

## Installation and Setup
To set up the application, follow these steps:

1. Clone the repository:
```shell
git clone https://github.com/AnilMohite/log_book.git
```

2. Change into the project directory:
```shell
cd log_book
```

3. Install the required Python packages (find in Build folder):
```shell
pip install -r requirements.txt
```

4. Configure the MySQL database (find in Build folder): 
Create database "log_book" and import the log_book.sql script

## Flask Setup
1. Start the Flask development server:
```shell
    python app.py
```
2. Open your web browser and navigate to http://127.0.0.1:5000 to access the application.

## Database Integration
The application uses a MySQL database to store log book data. The database integration is handled using Flask-SQLAlchemy.

## Workflow
- Sign Up: Users can create a new account by providing their email address and password.
![Application Screenshot](https://github.com/AnilMohite/log_book/blob/main/Build/screenshots/signup-screen.png)
- Sign In: Existing users can sign in using their email address and password.
![Application Screenshot](https://github.com/AnilMohite/log_book/blob/main/Build/screenshots/signin-screen.png)
- Log Book Creation: Once signed in, users can create multiple log books based on different log book types. They can provide a name and select a log book type during the creation process.
![Application Screenshot](https://github.com/AnilMohite/log_book/blob/main/Build/screenshots/logbook-create-screen.png)
- Log Book Management: Users can view their existing log books on the dashboard. They can edit or delete log books as needed.
![Application Screenshot](https://github.com/AnilMohite/log_book/blob/main/Build/screenshots/home-screen.png)
- Entry Management: Within each log book, users can add, edit, and delete entries.
![Application Screenshot](https://github.com/AnilMohite/log_book/blob/main/Build/screenshots/logbook-entries-add-view-screen.png)

The application provides a user-friendly interface with HTML, CSS, JavaScript, and Bootstrap 5, making it easy to navigate and interact with log books and entries.

Feel free to explore and customize the application according to your requirements.
