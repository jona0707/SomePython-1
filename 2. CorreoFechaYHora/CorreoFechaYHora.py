#SomePython-1.2 ~ Jona
#-------------------#
#Permite enviar un correo electrónico indicando la fecha y hora de 8 países de diferentes zonas horarias. 
#Para ello se debera tener un correo electronico con la autenticacion de 2 pasos (simplemente activada), 
#luego se crea una contraseña de aplicación y una vez se haya hecho esto, se tendrá la API correspondiente para usar en el Script.

#Incluyo las librerias
import smtplib
import pytz
from datetime import datetime

#Variables de utilidad:
correoSMTP = 'INCLUIR CORREO DE ORIGEN (SMTP)'
claveAPI = 'INCLUIR API'

#Importante (Poner el correo de destino):
correoDestino = 'INCLUIR CORREO DE DESTINO'

#En primer lugar conectaremos el correo con el protocolo SMTP, con el smtp y el puerto
cnx = smtplib.SMTP(host='smtp.gmail.com',port=587)
cnx.ehlo()
cnx.starttls()
cnx.login(correoSMTP,claveAPI)

#Ahora, escogeremos los paises de 8 zonas horarias diferentes, donde se incluira Ecuador, tendremos tuplas para cada pais este con su zona horaria:
paises = [('Ecuador','America/Guayaquil'),('China', 'Asia/Shanghai'),('Francia', 'Europe/Paris'),('India', 'Asia/Kolkata'),('Mexico', 'America/Mexico_City'),('Canada','America/Toronto'),('Indonesia', 'Asia/Jakarta'),('Sudafrica', 'Africa/Johannesburg')]

#Agregamos un Asunto porque de lo contrario NO ENVIARÁ
cuerpo = "Subject: Hora y Fecha en distintos paises. De: Jonathan Puente.\n\n"

#Primero recorro con zh (zona horaria) y pais las tuplas, encontrando el pais y la zona horaria, esta ultima
#se enviara como parametro para la funcion pytz que devuelve datos de zonas horarias distintas. Luego simplemente ingreso
#esta informacion en el metodo now de datetime para obtener el tiempo actual en aquellas zonas.
#Aprovecho el for para la construccion del mensaje, donde simplemente concateno dos cadenas de texto con el f-strings que me
#ayuda a incluir variables dentro del texto, en este caso pais y FyH:

for pais, zh in paises:
  
  FyH = datetime.now(pytz.timezone(zh))

  cuerpo +=  f"{pais}: {FyH}\n"

print(cuerpo)
mensaje = cuerpo
#Finalmente enviamos el mensaje:
cnx.sendmail(correoSMTP,correoDestino,mensaje)
#Y cierro la conexion:
cnx.quit()
