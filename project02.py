from sqlalchemy import (
    Column, Integer, String, ForeignKey,select)
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
Session = sessionmaker(bind=engine)

with Session() as session:
    user01 = User(name ="Ali",email = "ali@gmail.com")
    user01.tasks = [
        Task(title ="Kitob o'qish", status ="kutilmoqda"),
        Task(title ="Darsga borish", status ="kutilmoqda"),
        Task(title ="Yugurish", status ="kutilmoqda"),
    ]

    user02 = User(name ="Vali",email = "vali@gmail.com" )
    user02.tasks = [
        Task(title ="Najot Ta'limga borish", status ="tugalangan"),
        Task(title ="Uy vazifasini bajarish", status ="kutilmoqda"),
        Task(title ="Kitob o'qish", status ="kutilmoqda"),
    ]

    user03 = User(name ="John",email = "John4@gmail.com" )
    user03.tasks = [
        Task(title ="Darsga borish", status ="bajarilgan"),
        Task(title ="Ovqatlans", status ="kutilmoqda"),
        Task(title ="Mini Proekt yaratsh", status ="kutilmoqda"),
    ]
    
    session.add(user01)
    session.add(user02)
    session.add(user03)
  
    session.commit()

    session.add_all([user01,user02,user03])

# 3 - task
stmt = select(Task)
rows = session.execute(stmt).fetchall()

for row in rows:
    task = row[0] 
    print(task.title, task.status)


# 4-task

users = session.query(User).all()

for user in users:
    for task in user.tasks:
        print(f" {user.name} -> [{task.title}, {task.status}]")

# 5 - task

stmt = select(Task).where(Task.status == "done")
result = session.execute(stmt).scalars()

for task in result:
    print(task.title, task.status)

