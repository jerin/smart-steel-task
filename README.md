# smart-steel-task
* smart steel task

## Prerequisites
* postgres database
* python3
    
## Quick Start
* Create new database in your postgres DB
    sql command
    ```
    CREATE DATABASE smart_steel;
    ```
* clone git repo
    windows command line
    ```
    git clone repo https://github.com/jerin/smart-steel-task.git
    cd smart-steel-task    
    ```
* Create new .env file in root and add the environment variable by referring .env.template

* Initialize and activate a virtualenv
    windows command line
    ```
    pip install virtualenv
    virtualenv smartenv
    smartenv\Scripts\activate
    ```
* Install the dependencies
    windows command line
    ```
    pip install -r requirements.txt
    ```
* Database migration
    windows command line
    ```
    flask db upgrade
    ```
## Application 1 (Import task data from csv to db)
* Data migration
    windows command line
    ```
    python import-data/import_task_data.py
    ```
## Application 2 (Dispaly data on web browser)
* Web application
    windows command line
    ```
    flask run
    ```
* Open http://localhost:5000/taskdata
## Test cases
* Run unit tests
    windows command line
    ```
    python -m pytest
    ```