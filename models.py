from sqlalchemy import Column, Integer, String
from db import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)
    email = Column(String(120), unique=True)
    # всегда делать repr для представления в читаемом виде
    def __repr__(self):
        return f'<User {self.name} {self.email}>'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    # создаст на сайте соответствующую табличку в ValentinaStudios 
    # (в левом верхнем углу нажать "обновить")