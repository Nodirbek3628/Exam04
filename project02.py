from sqlalchemy import (
    Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship, sessionmaker
from database import Base, engine,Session


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    email = Column(String(64), unique=True, nullable=False)

    tasks = relationship("Task", back_populates="user")
  
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(160), nullable=False)
    status = Column(String(160), default="pending")
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

# 2-task
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

with Session() as session:
    user01 = User(id = 1,name ="Ali",email = "ali@gmail.com")
    user02 = User(id = 2,name ="Vali",email = "vali@gmail.com" )
    user03 = User(id = 3,name ="John",email = "John4@gmail.com" )
    
    session.add(user01)
    session.add(user02)
    session.add(user03)
  
    session.commit()

    session.add_all([user01,user02,user03])




