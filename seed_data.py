from ejemplo.models import Familiar
Familiar(nombre="Marisa", dni=25345851, fecha_nac='1968-03-11', direccion="Av R. J. Carcano, 619 – Villa Carlos Paz - Cba").save()
Familiar(nombre="Federico", dni=17581634, fecha_nac='1966-08-23', direccion="Av R. J. Carcano, 619 – Villa Carlos Paz - Cba").save()
Familiar(nombre="Karla", dni=35841865, fecha_nac='1985-05-05', direccion="Pedro Goyena, 15 – Cordoba - Cba").save()
Familiar(nombre="Gisel", dni=37946634, fecha_nac='1990-02-22', direccion="Arturo Orgaz 515 – Cordoba - Cba").save()
print("Se cargo con éxito los usuarios de pruebas")

from ejemplo.models import Auto
Auto(marca="Ford", modelo="Ka", anio="2009").save()
Auto(marca="Citroen", modelo="C4", anio="2016").save()
Auto(marca="Fiat", modelo="Palio", anio="2007").save()
print("Se cargo con éxito los autos de pruebas")

from ejemplo.models import Mascota
Mascota(especie="Perro", nombre="Tefi", edad=4).save()
Mascota(especie="Perro", nombre="India", edad=18).save()
Mascota(especie="Gato", nombre="Blanch", edad=5).save()
print("Se cargo con éxito las mascotas de pruebas")