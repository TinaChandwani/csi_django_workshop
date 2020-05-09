# csi_django_workshop

## [Django](https://docs.djangoproject.com/en/3.0/)

Django is a web application framework written in Python programming language. It is based on MVT (Model View Template) design pattern. The Django is very demanding due to its rapid development feature. It takes less time to build application after collecting client requirement.
## Why Django
A web framework is a collection of modular tools that abstracts away much of the difficulty–and repetition–inherent in web development. For example, most websites need the same basic functionality: the ability to connect to a database, set URL routes, display content on a page, handle security properly, and so on. Rather than recreate all of this from scratch, programmers over the years have created web frameworks in all the major programming languages: Django and Flask in Python, Rails in Ruby, and Express in JavaScript among many, many others.

Django inherited Python’s “batteries-included” approach and includes out-of-the box support for common tasks in web development:
- user authentication
- templates, routes, and views
- admin interface
- robust security
- support for multiple database backends and much much more
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
