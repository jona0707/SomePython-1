#SomePython-1.4.1 ~ Jona
#-------------------#
#Se llenarán los datos en una BDD utilizando el siguiente script, teniendo en cuenta la creación previa de
#un servidor LAMP cuya BDD está gestionada por MySQL utilizando PHPMyAdmin, la BDD tiene (para este caso en
#particular: 
#Nombre: Variables_Meteorologicas
#Tabla: Registrador
#Columnas: 'id' INT (Primary Key), 'fecha' DATE, 'hora' TIME, 'temperatura' FLOAT, 'presion' FLOAT, 'humedad' FLOAT.

#Se enviaran datos de Temperatura, Presión y Humedad obtenidos por el emulador de SenseHat, si se desea 
#utilizar SenseHat en sí, solo hace falta cambiar la biblioteca (y obviamente el uso de la placa).
#*----------------------------------*
#  Librerías previas a instalar!!! 
#       pip install pymysql
#*----------------------------------*

#Se accederá a estos datos a través del simulador sense_emu
from sense_emu import SenseHat
from time import sleep
import datetime
#Conexión a la base de datos
import pymysql.cursors 
import numpy as np

#Recordar que se deberá instalar con:
#pip install PyMySQL 
#en debian.

sense = SenseHat()
sense.clear()
#Se verifica la creación correcta de la base de datos:
chekDB = 2

#Recogemos los datos:

while True:
    tempT=0 
    presT=0 
    humT=0 
    for r in range(1,4):
        fecha=(datetime.datetime.now().strftime("%Y/%m/%d")) 
        hora=(datetime.datetime.now().strftime("%H:%M:%S")) 
        temp=sense.get_temperature() 
        pres=sense.get_pressure() 
        hum=sense.get_humidity() 
        
        #Se debe siempre inicializar la variable
        tempT+=temp
        presT+=pres
        humT+=hum
        sleep(5) #Delay de 20 seg por medicion
    
    #Promedio de tres mediciones cada 20 segundos:
    tempT=round(tempT/3,2) #Temperatura
    presT=round(presT/3,2) #Presión
    humT=round(humT/3,2)#Humedad
    break


#Se inicia la conexion (Teniendo en cuenta que uso 'localhost', si deseo, podria colocar la ip del servidor.
connectionDB=pymysql.connect(host='localhost',user='root',password='PASSWORD',db='Registrador')

with connectionDB:
        with connectionDB.cursor() as cursor:
            #Si no existe tabla se crea
            if chekDB==1:
                tabla="CREATE TABLE `Registrador`.`Variables_Meteorologicas` ( `id` INT(4) NOT NULL AUTO_INCREMENT , `fecha` DATE NOT NULL , `hora` TIME(6) NOT NULL , `temperatura` FLOAT(20) NOT NULL , `presion` FLOAT(20) NOT NULL , `humedad` FLOAT(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"
                cursor.execute(tabla)
                chekDB=2
            #Y sino se ingresan los valores
            sql = "INSERT INTO Variables_Meteorologicas (Fecha, Hora, Temperatura, Presion, Humedad)" "VALUES (%s,%s ,%s,%s,%s);"
            cursor.execute(sql, (fecha,hora,tempT,presT,humT))
        #Actualizacion de la base de datos
        connectionDB.commit()
        print('terminado')

