# PlayGround_FedeOriglia
PlayGround Intermedio

1 - Para crear/resetear tu base de datos vas a tener que hacer los siguientes pasos:
* - Borra el archivo SQLite en la raiz del directorio ejemplo
* - En el terminal de VSC coloca python manage.py migrate
* - Luego en la misma terminal haces python manage.py runserver (si ahora ves en tu
    web http://127.0.0.1:8000, va a mostrarte las listas vacias)

2 - Importar el seed_data haciendo lo siguiente en el shell:
* python manage.py shell
* import seed_data
de esta forma deberiamos contar con todos los datos (ver mensaje de correcta importacion de los mismos), para Familiares, Autos y Mascotas del presente modelo.

2 - En el browser se tiene el menú de opciones sobre los cuales podemos interactuar. Ejecutar uno a uno para su correcto uso! (por ej. http://127.0.0.1:8000/mi-familia/familia).

mi-familia/familia - "Muestra familiares presentes en la Base de Datos"
mi-familia/autos - "Muestra autos presentes en la Base de Datos"
mi-familia/mascotas - "Muestra mascotas presentes en la Base de Datos"
mi-familia/buscar_familiar - "Buscar un familiar por Nombre"
mi-familia/alta_familiar - "Alta de un familiar"
mi-familia/buscar_auto - "Buscar auto por Marca"
mi-familia/alta_auto - "Alta de Auto"
mi-familia/buscar_mascota - "Buscar Mascota por Especie"
mi-familia/alta_mascota - "Alta de Mascota"

Muchas gracias.
