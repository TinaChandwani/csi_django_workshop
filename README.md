# csi_django_workshop


### STEPS 
1) pip install virtualenvwrapper-win (for windows)
2) mkvirtualenv (any_name)

**NOW YOU ARE IN VIRTUAL ENVIRONMENT**

3) pip install django 
4) django-admin startproject (name of the project)

5) cd (name of the project)

6) code . (To open VS CODE)

7) python manage.py runserver (command to run the server)

8) python manage.py migrate (command to migrate into your database)

9) python manage.py createsuperuser (command used to create admin user)

10) python manage.py startapp (name of the app) 

Settings.py of project :  add the below line:
            “posts.apps.PostsConfig”

**TO KNOW ALL THE COMMANDS IN DJANGO:**
*“python manage.py help”
