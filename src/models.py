from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    personajes_favoritos: Mapped[list['PersonajesFavoritos']] = relationship(back_populates='usuarios')

class Personajes(db.Model):
    __tablename__ = 'personajes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    estatura: Mapped[int] = mapped_column(Integer, nullable=True)
    PlanetaID: Mapped[int] = mapped_column(ForeignKey('planetas.id'))
    planet: Mapped['Planeta'] = relationship(back_populates='personajes')
    favoritos_por: Mapped[list['User']] = relationship(back_populates='personajes')

class Planeta(db.Model):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    clima: Mapped[str] = mapped_column(String(20), nullable=True)
    personajes: Mapped[list['Personajes']] = relationship(back_populates='planet')

class PersonajesFavoritos(db.Model):
    __tablename__ = 'personajes_favoritos'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuarioID: Mapped[int] = mapped_column(ForeignKey('user.id'))
    personajeID: Mapped[int] = mapped_column(ForeignKey('personajes.id'))
    usuarios: Mapped[list['User']] = relationship(back_populates='personajes_favoritos')
    personajes: Mapped['Personajes'] = relationship(back_populates='favoritos_por')

def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
