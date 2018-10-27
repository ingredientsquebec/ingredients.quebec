import pymodm
from pymodm import fields


class Compagnie(pymodm.MongoModel):
    description = fields.CharField()
    logo = fields.CharField()
    name = fields.CharField(primary_key=True)
    URL = fields.CharField()


class Houblonniere(Compagnie):
    pass


class Levurier(Compagnie):
    pass


class Malterie(Compagnie):
    pass
