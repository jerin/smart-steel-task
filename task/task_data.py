from database.database import db_session
from models import TaskData as TaskDataModel
from datetime import datetime


class TaskData:
    def get_task_data():
        try:
            data = TaskDataModel.query.all()
            return data
        except Exception as Err:
            raise Err

    def insert_task_data(id, temperature, duration, batch_id):
        try:
            data = TaskDataModel(id=id, timestamp=datetime.now(), temperature=temperature, duration=duration, batch_id=batch_id)
            db_session.add(data)
            db_session.commit()
        except Exception as Err:
            raise Err
