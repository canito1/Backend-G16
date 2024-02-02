from variables import conexion
from sqlalchemy import Column, types, ForeignKey

class DireccionModel (conexion.Model):
    __tablename__ = 'direcciones'
    id = Column(name='id',
                type_=types.Integer, 
                autoincrement = True,
                primary_key = True)
    calle = Column(type_= types.Text)
    numero = Column(type_= types.String(20))
    referencia = Column(type_= types.Text)
    predeterminada = Column(name='predeterminada', type_= types.Boolean, default=False)
    usuarioId = Column(ForeignKey(column='usuarios.id'),
                 nullable=False, name='usuarioId')