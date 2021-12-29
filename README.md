Django application to centralize management of Plotly Dash applications

Example Dash apps are included in the project and are found under `django_dashboard/home/dash_apps`

# Prerequisites
You should have a postgres database and a redis service. If you don't have them, you can easily have them with docker and a couple of commands:

`docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password postgres`\
`docker run -d --name redis -p 6379:6379 redis:4`

Unless you are running a test, you should definitely change that default "password"

If you already have postgres or redis, be sure to setup their location in the `django_dashboard/django_dashboard/settings.py` file


# First time install
1) Create a `.env` file in `$project_repository/django_dashboard` and put a django secret key inside it like this:\
`SECRET_KEY = 'this-is-my-awesome-django-secret-key'`
2) Open a cli in $project_repository
3) Create and activate a virtual environment (optional):\
`python -m venv venv`\
`venv/Scripts/activate`
4) Run the following commands:\
`python -m pip install -r requirements.txt`\
`python manage.py collectstatic`\
`python manage.py migrate`
5) Create a superuser with the command:\
`python manage.py createsuperuser`
6) Run the Django app with:\
`python manage.py runserver`
