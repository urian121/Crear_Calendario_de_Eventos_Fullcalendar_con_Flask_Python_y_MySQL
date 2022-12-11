<em> # Su título aquí </em>

<em> PASO 1, Crear mi entorno virtual </em>
virtualenv -p python3 env o python3 -m venv env

<em> PASO 2, Activar el entorno virtual ejecutando</em>
 . env/Scripts/activate  
 
<em> PASO 3, Ya dentro del entorno virtual instalar flask</em>
  pip install flask

<em> PASO 4, Instalar Python MySQL Connector, es una bibliote (Driver) para </em>
<em> conectar Python con MySQL</em>
pip install mysql-connector-python


<h1 align="center"> Crear/Actualizar el fichero requirements.txt:</h1>
pip freeze > requirements.txt

# IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo
# requirements.txt con el comando pip install -r requirements.txt en el 
# mismo se encuentran todas las dependecias del proyecto.

# Para desactivar nuestro entono virtual (env) $ deactivate   
 
Comando para actualizar pip: python -m pip install --upgrade pip




INSTALACION
- - - - - - -

git clone https://github.com/urian121/Crear_Calendario_de_Eventos_Fullcalendar_con_Flask_Python_y_MySQL.git

cd Crear_Calendario_de_Eventos_Fullcalendar_con_Flask_Python_y_MySQL.git

pip install -r requirements.txt

python app/main.py


