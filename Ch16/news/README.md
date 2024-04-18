Since [Heroku](https://www.heroku.com/pricing) doesn't offer a free tier anymore, I used an alternate service called [FL0](https://www.fl0.com).

I followed this [YT video](https://youtu.be/dftvQCUauTE) for reference.
The steps are almost the same as mentioned in the book.

Here is the summarized version of the deployment steps for FL0:
1. Sign up for an account in [FL0](https://www.fl0.com) using GitHub(recommended) or Google or Email.
   1. Add your name & create a workspace.
   2. Add a project
2. Create a Postgres database in FL0.
   1. Give the database a name 
   2. Set the region nearest to your location
   3. Copy the DB url from the **Connection Info** tab and store it somewhere for later use.
3. Install the following python packages in your virtual environment
   1. `pip install django-environ`
   2. `pip install psycopg2-binary`
   3. `pip install dj-database-url`
4. To enable `environ`, Add the following code in `settings.py`
```py
import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent # this line will already be in the file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
```
5. Create a `.env` file in the root directory, and initalize the variables: `DEBUG`, `SECRET_KEY`, `DATABASE_URL`
   1. Set `DEBUG=True` for local developement
   2. Create a secret key using Python's built-in `secrets` module as mentioned in the book.
   3. Use that generated value for `SECRET_KEY`
   4. Set `DATABASE_URL=use-the-url-from-the-postgres-db` temporarily to set up the postgres DB and to create an admin user using the local server.
6. To use these environment variables, make the following code changes in `settings.py`
```py
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']
#CSRF_TRUSTED_ORIGINS = ['*']
```
7. To configure the database settings, modify the following code in the `settings.py`
```py
import dj_database_url

DATABASES = { 
    'default': dj_database_url(env('DATABASE_URL'))
} # This will be located after some code below the initializaton of ALLOWED_HOSTS
```
8. Run `python manage.py migrate` in your terminal to setup the postgres DB in FL0
9. Run `python manage.py createsuperuser` and create an admin user for that DB
10. Now you can set `DATABASE_URL=sqlite:///db.sqlite3` for local development
11. Handling static files with [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) (refer this for up-to-date guide)
    1. Create a `static` folder with subfolders `css` & `js`
    2. Create `base.css` inside `static/css` and `base.js` inside `static.js`
    3. Install the python package: `pip install whitenoise`
    4. In the `settings.py` file
        1. Add its Middleware above `CommonMiddleware`
        2. Define `STATICFILES_STORAGE` & `STATIC_ROOT` 
    5. Run the collectstatic command: `python manage.py collectstatic`
    6. Add `{% load static %}` tag at the top of `base.html`
12. Important deployment configurations
   1. Install the python package: `pip install gunicorn`
   2. Create `requirements.txt` using `pip freeze` in the base directory
   3. Create a `Procfile` in the root directory and add the following code
       1. Add `release: python manage.py migrate` to set up the Postgres DB in FL0
       2. Add `web: gunicorn django_project.wsgi --log-file -`
13. Push your code to GitHub
    1.  Create a new repository (if required)
    2.  Create `.gitignore` in your project folder & add the exceptions to exclude `.env` & `db.sqlite3`
    3.  Push your code to the repository
14. Deploying to FL0
    1.  In your FL0 project dashboard, Add a New Web application service
    2.  Connect your GitHub repo & authorize FL0 (skip if already done)
    3.  Give the web application a name 
    4.  Set the region nearest to your location
    5.  Add the environment variables
        1.  `SECRET_KEY=same-as-local-env`
        2.  `DATABASE_URL=use-the-url-from-the-postgres-db`
        3.  Since `DEBUG` has a default value of `False`, no need the define it here
    6.  Deploy
15. After Deployment, update the `ALLOWED_HOSTS` & `CSRF_TRUSTED_ORIGINS` in the `settings.py`
```py
ALLOWED_HOSTS = ['your-fl0-url']
CSRF_TRUSTED_ORIGINS = ['https://your-fl0-url']
```
1.   Finally push the updated code to re-deploy the app.

---
> To Create a Admin User in the Postgres DB
1. Replace the sqlite3 url in the local .env file with the postgres DB's url
2. Run `python manage.py createsuperuser` in the terminal and create the admin user as usual.
3. Run the project in the local server connected to the FL0's postgres DB
4. Visit the admin url in the browser and test the login
5. Since this DB is also connected to the deployed project in the FL0 platform, same admin credentials can be used to login at `your-project-url-from-fl0/admin`.