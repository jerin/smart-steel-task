from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy_searchable import make_searchable
from sqlalchemy.orm import configure_mappers
from sqlalchemy.pool import NullPool
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, poolclass=NullPool)

configure_mappers()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
make_searchable(Base.metadata)
Base.query = db_session.query_property()