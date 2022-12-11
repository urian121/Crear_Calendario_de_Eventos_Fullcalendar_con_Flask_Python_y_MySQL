from flask import Flask, request, render_template, jsonify, json
from datetime import datetime
from confiDB import * #Importando conexion BD


app = Flask(__name__) 

#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
    mycursor         = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM eventoscalendar")
    mycursor.execute(querySQL)
    mycursor.fetchall() #fetchall () Obtener todos los registros
    
    mycursor.close() #cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return render_template('public/index.html', miData = API())


@app.route('/form', methods=['GET', 'POST'])
def registrarEvento():
    msg =''
    if request.method == 'POST':
        evento            = request.form['evento']
        f_inicio          = request.form['fecha_inicio']; 
        f_fin             = request.form['fecha_fin']
        color_evento      = request.form['color_evento']
        print(f_inicio, f_fin)
        
        '''
        Nota: Ambas fechas llegan en formato dia-mes-año,
        hay que pasarlas año, mes y dia
        '''
        fecha_inicio = datetime.strptime(f_inicio, '%m-%d-%Y').date()
        fecha_fin    = datetime.strptime(f_fin, '%m-%d-%Y').date()
        print(fecha_inicio, fecha_fin)
         
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO eventoscalendar(evento, fecha_inicio, fecha_fin, color_evento) VALUES (%s, %s, %s, %s)")
        valores     = (evento, fecha_inicio, fecha_fin, color_evento)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
    
        return render_template('public/index.html', msg='Formulario enviado')

@app.route('/eventos', methods=['GET','POST'])
def ejemplo(): 
    input = '2021/05/25'
    # format
    format = '%Y/%m/%d'
    datetime = datetime.datetime.strptime(input, format)
    print(datetime.date())
    return 'ok'

#Creando mi Decorador para el Home
#@app.route('/api-eventos', methods=['GET','POST'])
def API():
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
        mycursor         = conexion_MySQLdb.cursor(dictionary=True)
        #Obteniendo todos los eventos desde BD
        querySQL  = ("SELECT * FROM eventoscalendar ORDER BY id")
        mycursor.execute(querySQL)
        dataEventos = mycursor.fetchall() #fetchall () Obtener todos los registros
        print(dataEventos)
        print(jsonify(dataR = [dataEventos, 1]))
        
        mycursor.close() #cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        return dataEventos
     
if __name__ == '__main__': 
    app.run(debug=True, port=5000) 