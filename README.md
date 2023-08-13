# Culinary Recipes - Restaurant Menu Management System

This guide outlines the steps to set up your individual project for managing culinary recipes using a Python web framework. The project involves cloning a GitHub repository, configuring a virtual environment, setting up a database, and creating a superuser.

## Cloning the Repository
1. Clone the GitHub repository for your Python web framework project using the command:

    git clone https://github.com/Andon-ov/Culinary-Recipes.git


## Navigating to Project Folder
2. Change the directory to the project folder using the command:

    cd Culinary-Recipes


## Setting up Virtual Environment
3. Set up a virtual environment for your project using the command:

    python -m venv venv


## Activating Virtual Environment
4. Activate the virtual environment using the command:
- On Linux/Mac:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

## Installing Dependencies
5. Install the required dependencies for your project using the command:

    pip install -r requirements.txt


## Updating pip
6. Update pip to ensure it's up to date by using the command:

    pip install --upgrade pip


## Running the Development Server
7. Start the development server for your project using the command:

    python manage.py runserver


## Launching Postgres Container
8. Launch a Postgres container for your database using the command:

    docker run -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1123QwER -d -v my-postgres-data:/var/lib/postgresql/data --name postgres postgres:latest


## Adding Database to PyCharm
9. Add the database to your PyCharm project with the following credentials:
- Username: postgres
- Password: 1123QwER
- Database: recipes_db

## Applying Migrations
10. Apply the migrations for your database using the command:
 ```
 python manage.py migrate
 ```

## Creating a Superuser
11. Create a superuser for your project using the command:
 ```
 python manage.py createsuperuser
 ```

## Granting Permissions
12. Log in to the database and give all necessary permissions to the superuser.

This series of steps will help you set up your Python web framework project for managing culinary recipes. If you have any further questions or need additional assistance, feel free to ask!


