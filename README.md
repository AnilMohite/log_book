#Log Book
This repository contains a Flask application that allows users to create and manage multiple log books. The application is integrated with a MySQL database and uses HTML, CSS, JavaScript, and Bootstrap 5 for the frontend.

#Prerequisites
Before setting up the application, ensure that you have the following prerequisites installed:

Python 3.x
MySQL
#Installation and Setup
To set up the application, follow these steps:

Clone the repository:
git clone https://github.com/AnilMohite/log_book/
  
Change into the project directory:
cd log_book

Install the required Python packages:
(find in Build folder)

pip install -r requirements.txt

Configure the MySQL database: 
Create database "log_book" and import the log_book.sql script

#Flask Setup
Start the Flask development server:
python app.py
Open your web browser and navigate to http://localhost:5000 to access the application.

#Database Integration
The application uses a MySQL database to store log book data. The database integration is handled using Flask-SQLAlchemy.

#Workflow
Sign Up: Users can create a new account by providing their email address and password.

Sign In: Existing users can sign in using their email address and password.

Log Book Creation: Once signed in, users can create multiple log books based on different log book types. They can provide a name and select a log book type during the creation process.

Log Book Management: Users can view their existing log books on the dashboard. They can edit or delete log books as needed.

Entry Management: Within each log book, users can add, edit, and delete entries.

The application provides a user-friendly interface with HTML, CSS, JavaScript, and Bootstrap 5, making it easy to navigate and interact with log books and entries.

Feel free to explore and customize the application according to your requirements.
