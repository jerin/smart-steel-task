from database.database import Base, db_session
from models import LogData
from datetime import datetime
import uuid

class Log:
    def insert_log(log_type, action, message=""):
        try:
            data = LogData(id = uuid.uuid1(), timestamp = datetime.now(), log_type= log_type,action = action,message= message)                   
            db_session.add(data)   
            db_session.commit()
        except Exception as Err:
            raise Err
    def get_log():
        try:
            data = LogData.query.all()
            return data                  
        except Exception as Err:
            raise Err
