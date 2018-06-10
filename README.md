# Installation Guide:

Step 1: Create database with name users_database
Step 2: Open settings.py from project/settings.py and change the database details, ex:. database name,username and password
Step 3: Go to the project, open terminal and type command : source env_project/bin/activate
Step 4: Type : pip install -r requirements.txt (To install all the dependencies)
Step 5: Type : python manage.py makemigrations
Step 6: Type : python manage.py migrate
