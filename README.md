# Transup [![Build Status](https://travis-ci.com/otseobande/transup.svg?branch=develop)](https://travis-ci.com/otseobande/transup) [![codecov](https://codecov.io/gh/otseobande/transup/branch/develop/graph/badge.svg)](https://codecov.io/gh/otseobande/transup)

An application that help manage transportation suppliers.


## Setup

- Install virtualenv

```bash
pip install virtualenv
```

- Create the application's virtual environment

```bash
virtualenv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Setup environment variables

  Create a `.env` file, copy the content of the `.env.example` file into it and fill the necessary credentials

- Install dependencies

```bash
pip install -r requirements.txt
```

- Start the development server

```bash
python manage.py runserver
```

### Documentation

- [Swagger Documentation](http://ec2-13-58-177-108.us-east-2.compute.amazonaws.com/api/v1/docs/)

### Testing

Run `python manage.py test` to run tests

## Technologies Used

- [Django](https://www.djangoproject.com/)
- [Postgres](https://www.postgresql.org/)


## Project Management

[Pivotal Tracker](https://www.pivotaltracker.com) is used for this project. You can find the management board [here](https://www.pivotaltracker.com/n/projects/2376016).
