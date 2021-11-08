from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Boolean,BLOB,Date

db=SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'Categorias'
    idCategoria=Column(Integer,primary_key=True)
    nombre=Column(String(60),unique=True)
    estatus=Column(Boolean, default=True)
    foto=Column(BLOB,nullable=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaIndividual(self,id):
        return self.query.get(id)

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self,id):
        objeto=self.consultaIndividual(id)
        db.session.delete(objeto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()
