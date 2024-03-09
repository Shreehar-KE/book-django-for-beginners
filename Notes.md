# Django for Beginners 4.0 - Willian S. Vincent

## Chapter 1: Inital Setup
- `django-admin startproject django_project .` - to create a new Django project

## Chapter 2: Hello World App
- `python manage.py migrate`
- Project's Folder Structure
    ```
    ├── django_project
    │   ├── __init__.py
    |   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3 # After migration
    ├── manage.py
    └── .venv/
    ```
- HTTP Request -> URL -> Django combines database, logic, styling -> HTTP Response
- MVC v/s MVT
  - MVT -> MVTU
  - HTTP Request -> URL -> View -> Model and Template -> HTTP Response
- Django Project - Group of Apps
- `python manage.py startapp app-name`
- App's Folder Structure
    ```
    ├── django_project
    ├── app-name
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── db.sqlite3 # After migration
    ├── manage.py
    └── .venv/
    ```
- Add *app* to `django_project/settings.py`
  - `INSTALLED_APPS` list - `app-name.apps.app-nameConfig`
- FBVs v/s CBVs v/s GCBVs
- CBVs means DRY rule, concise code due to abstraction, extendability using mixins
- Add *view function* to `app-name/urls.py`
  - `URL_PATTERNS` list - (regex for url, reference for view function, view's name)
- *Include* the `app-name.urls` to `django_project/urls.py`
  
## Chapter 3: Pages App
- 




## Chapter 4: Message Board App
## Chapter 5: Blog App
## Chapter 6: Forms
## Chapter 7: User Accounts
## Chapter 8: Custom User Model
## Chapter 9: User Authentication
## Chapter 10: Bootstrap
## Chapter 11: Password Change and Reset
## Chapter 12: Email
## Chapter 13: Newspaper App
## Chapter 14: Permissions and Authorization
## Chapter 15: Comments
## Chapter 16: Deployment
