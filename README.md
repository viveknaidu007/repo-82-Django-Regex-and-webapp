# repo-82-Django-Regex-and-webapp
here im building apis for my requirement

# create a python venv in the vscode or use conda environemt
activate ur environemnt
pip install django

# Create a Django project
django-admin startproject myproject

# cd myproject
django-admin startapp admin_panel
django-admin startapp user_panel

# define models
define ur model in admin_panel/user_panel

# define serializers
define ur serializers in admin_panel

# Define Views and API Endpoints:
define views in admin_panel

# url configuratoin
define urls in myproject

define urls in admin_panel

# Authentication
You can use Django's built-in authentication or integrate third-party libraries like Django Rest Framework JWT for token-based authentication.

# Fronteend
create the steps for ur templates

# for running the code
python manage.py runserver

# PROJECT STEPS
1. add templates , static , media folders

1. update ur settings.py and urls.py 
* give your app paths in urls.py in myproejct
* update the names in settings.py in my project

2. update the admin_panel
* add urls.py
* update the admin panel : models , views

3. update the user_panel
* add urls.py in user_panel folder
* update the user_panel : models , views

## error u will face by runnin gthe python manage.py runserver , without applying migartion:
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.  

# so applying migrations
python manage.py migrate

# now run the project
python manage.py runserver


# check online reference and docuemnetaion for html  , css , js templates , 
## my main aim to develop a djnago webapp