# Django for Beginners 4.0 - Willian S. Vincent

## Chapter 1: Inital Setup
- `django-admin startproject django_project .` - to create a new Django project
- `python manage.py runserver` - to run the django project

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
    ├── db.sqlite3
    ├── manage.py
    └── .venv/
    ```
- Add *app* to `django_project/settings.py`
  - `INSTALLED_APPS` list - `app-name.apps.App-nameConfig`
- FBVs v/s CBVs v/s GCBVs
- CBVs means DRY rule, concise code due to abstraction, extendability using mixins
- Add *view function* to `app-name/urls.py`
  - `URL_PATTERNS` list - (*regex for url, reference for view function, view's name*)
- *Include* the `app-name.urls` to `django_project/urls.py`
  
## Chapter 3: Pages App
- Default Templates Folder Structure
    ```
    └── app-name
        ├── templates
            ├── app-name
                ├── template.html
    ```
- Using single project-level templates directory vs App-level templates directory
  - requires tweaking in `django_project/setting.py`
    - `TEMPLATES` list - `"DIRS": [BASE_DIR / "templates"]`
- Generic Class Based View : `django.views.generic`
  - *`TemplateView`*
- `as_view()` for CBVs
- Template-Inheritance using templating language `{% %}`
- `django.test`
  - test case classes: *`SimpleTestCase`*, *`TestCase`*, *`TransactionTestCase`* and *`LiveServerTestCase`*
- Deployement Checklist

## Chapter 4: Message Board App
- Activating models - after creating them
  - `python manage.py makemigrations app-name`
  - `python manage.py migrate`
- Admin User
  - `python manage.py createsuperuser`
- Model Registration
  - `app-name/admin.py`
  - `admin.site.register(model_name)`
- `__str__()` method
- *`ListView`*
- *`TestCase`*
  - `setUpTestData()` hook - to create a test data
  - `@classmethod` decorator
  - `cls` parameter -> `self`

## Chapter 5: Blog App
- ForeignKey : `auth.User`
  - on_delete option
- Static Files
  - `STATIC_URL` & `STATICFILES_DIRS` at `settings.py`
  - `{% load static %}`
  - `<link rel="stylesheet" href="{% static 'css/base.css' %}">`
- *`DetailView`*
  - `/post/pk/` url
  - `context_object_name`
- `pk`: auto-incementing primary key in DB
- Testing User Model
  - `get_user_model()`

## Chapter 6: Forms
- *`CreateView`*
  - `fields` attribute 
    - `__all__`
  - `post` form
    - `csrf_token`
- *`UpdateView`*
  - `/post/pk/edit` url
- *`DeleteView`*
  - `success_url` attribute
    - `reverse_lazy()` : won't redirect until the deleting is finished
    - doesn't needed in *`CreateView`* & *`UpdateView`* because of `get_absolute_url()` in `Post` model
- Testing
  - `302` status code for redirect
  
## Chapter 7: User Accounts
- `auth` app & `User` object
- *`LoginView`*
  - `templates/registration/` for `login.html` & `signup.html`
  - urls from `django.contrib.auth.urls`
  - `LOGIN_REDIRECT_URL` & `LOGOUT_REDIRECT_URL` in `settings.py`
  - `is_authenticated` attribute
  - Using ~~link~~ form(POST) for *Logout*
- `UserCreationForm` from `django.contrib.auth.forms` for signup form 
  - can override the `form_valid()` to automatically login the User

## Chapter 8: Custom User Model
- `AbstractUser` from `auth.models` to create a Customer User Model
- `null` v/s `blank` in model fields
  - empty string '' instead of `NULL` for string based fields
- updating `UserCreationForm` & `UserChangeForm` from `auth.forms` in `accounts/forms.py` for new Sign-up & edit 
- modifying `admin.py` to create `CustomUserAdmin` based on `UserAdmin` from `auth.admin`
  - `add_form`,`form`, `model`, `list_display`,`fieldsets`,`add_fieldsets`
- registering both `CustomUser` & `CustomUserAdmin` in `admin.py`

## Chapter 9: User Authentication
-  using `TemplateView` directly in `urls.py`
   -  `path("", TemplateView.as_view(template_name="home.html"), name="home")`
-  customizing the `fields` attribute in `Meta` class for including new fields in the signup form

## Chapter 10: Bootstrap
- Bootstrap Starter Template in `base.html`
  - `meta="viewport"` 
  - Bootstrap CDN for CSS & Js
- Available in all pages through template inheritance
- `django-crispy-forms` package
  - `{% load crispy_forms_tags %}`
  - `{{ form|crispy }}`

## Chapter 11: Password Change and Reset
- Views & Urls for Password Change are already provided by Django
- 2 templates are needed to be overriden for custom password change 
  - `templates/registration/password_change_form.html`
  - `templates/registration/password_change_done.html`
- `Console Backend`
  - `EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"` in `settings.py`
- 4 templates are needed to be overriden for custom password reset
  - `templates/registration/password_reset_form.html`
  - `templates/registration/password_reset_done.html`
  - `templates/registration/password_reset_confirm.html`
  - `templates/registration/password_reset_complete.html`



















## Chapter 12: Email
## Chapter 13: Newspaper App
## Chapter 14: Permissions and Authorization
## Chapter 15: Comments
## Chapter 16: Deployment
