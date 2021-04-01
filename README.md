## Requisitos
* django
* postgresql
* django rest framework

## Ejecucion
* Crear la base de datos rest_api_db en postgreSQL
* Asegurarse que en el archivo de api_rest/setting.py la configuracion de DATABASE sea la correcta.
* Ejecutar los siguientes comandos para migrar los modelos a la base de datos:
    - python manage.py makemigration enterpriseapi
    - python manage.py migrate
* Ejecutar 'python manage.py runserver' y todo listo.
* Hacer peticiones a la api desde la herramienta que desees.