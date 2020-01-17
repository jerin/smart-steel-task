#!/usr/bin/env python
from flask import Flask, request, render_template
from flask_migrate import Migrate
from config import Config
from database.database import Base, db_session
from logs import Log
from task import TaskData as TaskDataOP


app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': Config.SQLALCHEMY_DATABASE_URI
})  

migrate = Migrate(app, Base)

from models import LogData, TaskData

@app.route('/')
def welcome():
    return "welcome to python application"
    
@app.route('/taskdata')
def task_data():
    Log.insert_log("info","task data requested","task data requested")
    data = TaskDataOP.get_task_data()
    return render_template('task_data.html',
                           data=data,
                           title="Show Data")    

@app.errorhandler(404)
def page_not_found(e):
    Log.insert_log("error","invalid url",request.path)
    app.logger.error('Page not found: %s', (request.path))
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    Log.insert_log("error","internal server error",str(error))
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html',error=error), 500

@app.teardown_appcontext
def shutdown_session(exception=None):    
    db_session.remove()

if __name__ == '__main__':
    app.run(threaded=True)