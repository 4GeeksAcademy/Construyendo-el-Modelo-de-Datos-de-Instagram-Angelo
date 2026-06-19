from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer  
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  
    nombre: Mapped[str] = mapped_column(String(50),nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False) 
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

class Personajes(db.Model):
    __tablename__='personajes'
    id : Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    estatura: Mapped[int] = mapped_column(Integer, nullable=True)

class Planetas(db.Model):
     __tablename__ = 'planetas'
     id: Mapped[int] = mapped_column(primary_Key=True)
     nombre: Mapped[str] = mapped_column(String (50), nullable=False)
     clima: Mapped[str] = mapped_column(String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
