from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///abcall.db')
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)

class Incident(Base):
    __tablename__ = 'incident'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    state = Column(String)
    priority = Column(Integer)
    client = Column(String)
    agent = Column(String)
    creation_date = Column(String)
    update_date = Column(String)

Base.metadata.create_all(engine)
