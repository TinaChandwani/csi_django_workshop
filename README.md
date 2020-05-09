# csi_django_workshop





### STEPS 
1) pip install virtualenvwrapper-win (for windows)
mkvirtualenv (any_name)

NOW YOU ARE IN VIRTUAL ENVIRONMENT

pip install django

django-admin startproject (name of the project)

cd (name of the project)

code . (To open VS CODE)

python manage.py runserver

python manage.py migrate 

python manage.py createsuperuser

python manage.py startapp (name of the app) 
Settings.py of project :  add the below line:
            “posts.apps.PostsConfig”

TO KNOW ALL THE COMMANDS IN DJANGO:
“python manage.py help”
