# smart-steel-task
* smart steel task

## Prerequisites
* postgres database
* python3
    
## Quick Start
* Create new database in your postgres DB
    ```
    CREATE DATABASE smart_steel;
    ```
* clone git repo
    command line
    ```
    git clone repo https://github.com/jerin/smart-steel-task.git
    cd smart-steel-task    
    ```
* Create new .env file in root and add the environment variable by referring .env.template

* Initialize and activate a virtualenv
    ```
    pip install virtualenv
    virtualenv smartenv
    smartenv\Scripts\activate
    ```
* Install the dependencies
    ```
    pip install -r requirements.txt
    ```
* Database migration
    ```
    flask db upgrade
    ```
## Application 1 (Import task data from csv to db)
* Data migration
    ```
    python import-data/import_task_data.py
    ```
## Application 2 (Dispaly data on web browser)
* Web application
    ```
    flask run
    ```
* Open http://localhost:5000/taskdata
## Test cases
* Run unit tests
    ```
    python -m pytest
    ```