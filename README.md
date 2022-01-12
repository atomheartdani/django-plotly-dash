Django application to centralize management of Plotly Dash applications

Example Dash apps are included in the project and are found under `django_dashboard/home/dash_apps`

# Prerequisites
You should have a postgres database and a redis service. If you don't have them, you can easily have them with docker and a couple of commands:

`docker run -d --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password postgres`\
`docker run -d --name redis -p 6379:6379 redis:4`

Unless you are running a test, you should definitely change that default "password"


# First time install
1) Create a `.env` file in `$project_repository/django_dashboard` using the `.env_template` file provided and edit all the fields in accordance to you environment
2) Open a cli in $project_repository

### Running with docker
3) Choose a fancy name for your image and container (ie "django") and run the following commands:\
`docker build -t django -f ./docker/Dockerfile .`\
`docker run -d --name django -p:8000:8000 django`

### Running without docker
3) Create and activate a virtual environment (optional):\
`python -m venv venv`\
`venv/Scripts/activate` (on Windows)\
`source venv/bin/activate` (on Unix/MacOS)
4) Run the following commands:\
`python -m pip install -r requirements.txt`\
`python manage.py collectstatic`\
`python manage.py migrate`
5) Create a superuser with the command:\
`python manage.py createsuperuser`
6) Run the Django app with:\
`python manage.py runserver`
