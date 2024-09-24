# My Web App

This is a simple web application built using Django. It features a basic HTML/CSS web page with dynamic content, form handling, and data persistence. The app stores user submissions in a database and ensures no duplicate email entries are saved.

## Features

1. **Basic Web Page**: 
   - Includes a header, navigation menu, main content, and footer.
   - Styled with basic CSS for a clean and simple layout.

2. **Dynamic Content**: 
   - Displays random quotes and the current date in the main content area.

3. **Form Handling**: 
   - Collects user information (name and email) via a form.
   - Form validation prevents duplicate email submissions.

4. **Data Persistence**: 
   - Submissions are saved to a database and displayed on a separate page.
   - Prevents duplicate email addresses using form validation.

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/kksain/My_Web_Page.git
cd webapp

### 2. Set Up Virtual Environment
- python3 -m venv venv
- source venv/bin/activate  # For Linux/macOS
# or
- venv\Scripts\activate     # For Windows

### 3. Install Dependencies
- pip install -r requirements.txt

### 4. Set Up the Database
- python manage.py makemigrations
- python manage.py migrate

### 5. Run the Development Server
- python manage.py runserver
- Visit http://127.0.0.1:8000/ to view the app.

### Usage
# 1.Submit Form:

Navigate to the homepage.
Fill out the form with your name and email.
If the email is new, it will be saved and a success message will be displayed.
If the email already exists, you will be notified of the duplicate.
# 2.View Submissions:

Go to the /submissions/ URL to view all stored submissions.



