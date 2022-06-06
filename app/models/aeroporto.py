from sqlalchemy import Column, Integer, String, Numeric
from app import ma, db

class Aeroporto(db.Model):

    __tablename__ = 'aeroportos'

    id_aeroporto = Column(Integer, primary_key=True)
    nome_aeroporto = Column(String(120), nullable=False)
    codigo_iata = Column(String(3), nullable=False)
    cidade = Column(String(120), nullable=False)
    pais = Column(String(120), nullable=False)
    latitude = Column(Numeric(10, 6), nullable=False)
    longitude = Column(Numeric(10, 6), nullable=False)
    altitude = Column(Numeric(10, 6), nullable=False)

    def __init__(self, nome_aeroporto, codigo_iata, cidade, pais, latitude, longitude, altitude) -> None:
        self.nome_aeroporto = nome_aeroporto
        self.codigo_iata = codigo_iata
        self.cidade = cidade
        self.pais = pais
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Aeroportos: {self.name}'

class AeroportoSchema(ma.Schema):
    class Meta:
        model = Aeroporto
        sql_session = db.session
        load_instance = True

    id_aeroporto = ma.auto_field()
    nome_aeroporto = ma.auto_field()
    codigo_iata = ma.auto_field()
    cidade = ma.auto_field()
    pais = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    altitude = ma.auto_field()