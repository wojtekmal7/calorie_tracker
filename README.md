
# Calorie Tracker App

## Overview

This project is a Django-based web application for tracking daily calorie intake. Users can register, log in, add meals with nutritional information, and view their consumption history throughout the day.

## Author

Wojciech Malesiński

## Features

- **User Registration and Login**  
  Users can create accounts and log in using their email and password.

- **Meal Management**  
  Add meals with nutritional values (calories, proteins, carbohydrates, fats, etc.). Meals can consist of multiple ingredients.

- **Meal Search**  
  Search for previously added meals or ingredients in the database.

- **Consumption History**  
  View a list of meals consumed each day and the total daily calorie intake.

- **Calorie Summary**  
  Automatically calculates the total calories consumed in a given day.

## Technologies

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite

## Installation

1. Install Python 3.x  
2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install Django:
   ```bash
   pip install django
   ```

4. Clone or download the project files.  
5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000`

## Usage

- **Register**: Create an account with your email and password.  
- **Login**: Access the app using your credentials.  
- **Add Meals**: Use the form to add meal details.  
- **View History**: Browse your meal history and calorie summary per day.

## Notes

- All data used in this application is fictional and for demonstration only.
- PESEL (if used) must be 11 digits long and is validated internally.

## License

This project is intended for educational and demonstration purposes only.
