from sqlalchemy import (Column, String, DateTime, Float, Integer)
from database import Base


class TaskData(Base):
    """
    Create a task data table
    """
    __tablename__ = 'task_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    temperature = Column(Float)
    duration = Column(String(100))
    batch_id = Column(DateTime, primary_key=True)
