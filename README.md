# ProyectoDjango

# Para levantar el proyecto ejecutar el siguiente comando en la terminal:

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver 

# El proyecto dispone de una app llamada User dodnde se encuentra las siguientes rutas:

GET /: inicio muestra la pagina principal de la app.
GET /galeria/: muestra la pagina galeria de la app.
GET /blog/: muestra la pagina blog de la app donde tiene un listado de usuarios y un buscador de los mismos ademas de un formulario de registro para nuevos usuarios.
POST /blog/: crea un nuevo usuario con los datos enviados por POST.