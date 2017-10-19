To Do app in Python
===================

This app is a sample To Do app developed for a Meetup at Nelkinda
on the topic testing an untested Flask application.

In addition to that this repository is designed to serve as a template
for developing additional Flask applications with a proper setup of
running all the scripts and for running the complete test suite.

Description of the application
------------------------------
This application is split into two sub modules
1. *User* deals with handling the user's login and registration activity
2. *Todo* deals with the handling of all the todo lists and items

The tests are split into four levels of tests:
1. Unit tests
2. Database tests
3. Api tests
4. Acceptance tests


Steps to setup the application
------------------------------
```bash
# Set up a virtual environment
mkvirtualenv --python=`which python3` todo_app

# Activate the environment
workon todo_app

# Deactivate the environment
deactivate

# Install the requirements for dev (automatically install prod requirements)
pip install -r requirements_dev.txt

# Run the server
manage serve

# Run the complete test suite
manage test
```

Database setup (You need to have postgres installed for this)
--------------
```bash
# For Debian based linux
sudo apt install postgresql

# Create the dev and test database in postgres 
sudo -u postgres psql -c "CREATE ROLE todo_app"
sudo -u postgres psql -c "CREATE ROLE todo_app_test"
sudo -u postgres psql -c "CREATE DATABASE todo_app OWNER todo_app"
sudo -u postgres psql -c "CREATE DATABASE todo_app_test OWNER todo_app_test"

# Reverse the creation of the databases
sudo -u postgres psql -c "DROP DATABASE todo_app"
sudo -u postgres psql -c "DROP DATABASE todo_app_test"
sudo -u postgres psql -c "DROP ROLE todo_app"
sudo -u postgres psql -c "DROP ROLE todo_app_test"
```
