from sqlalchemy import (Column, String, DateTime, TEXT)
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class LogData(Base):
    """
    Create a log data table
    """
    __tablename__ = 'log_data'

    id = Column(UUID(as_uuid=True), primary_key=True)
    timestamp = Column(DateTime)
    log_type = Column(String(50))
    action = Column(String(100))
    message = Column(TEXT)
