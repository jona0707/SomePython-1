#SomePython-1.4.2 ~ Jona
#-------------------#
#Permitirá enviar alertas de temperatura, humedad y presion con Sense HAT a un bot de Telegram (previamente programado).
#Para la creacion del bot y obtencion de credenciales, verificar el repositorio, especificamente: 
#https://github.com/jona0707/SomePython-1/tree/main/3.%20EnvioMSGBotTelegram

#Se enviaran datos de Temperatura, Presión y Humedad obtenidos por el emulador de SenseHat, si se desea 
#utilizar SenseHat en sí, solo hace falta cambiar la biblioteca (y obviamente el uso de la placa).


#Importo librerias: GET y sense HAT
import requests
from sense_emu import SenseHat
import time
#Recordar que esto es porque haremos en emulador, caso contrario importariamos la libreria tal que:
#from sense_hat import SenseHat

#Iniciamos variables:
#Colores para impresion en la placa LED del SenseHat:
R = (255,0,0)
G = (0,255,255)
B = (0,0,255)
#Contador:
cont = 0
#Definimos variable de muestreo en segundos:
muestreo = 10
#SenseHAT:
sense = SenseHat()
sense.clear()

#Datos 'normales' (si sobrepasa estos datos se envia la alerta).
tempIns = 27
humeIns = 30
presIns = 1000

#Defino la funcion para enviar el mensaje al bot de telegram:
def enviarMSG(msg):
    token = 'TOKEN'
    msgId = 'MESSAGEID'
    msg = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+msgId+'&parse_mode=Markdown&text='+msg
    
    #Envio el mensaje
    requests.get(msg)

#EMPIEZA EL MENSAJE CON LO SOLICITADO:
enviarMSG("☁Temperatura, humedad y presión utilizando Sense HAT ☁\n\n")
enviarMSG("Se enviará la información en caso de superarse los siguientes valores: ")
enviarMSG("TEMPERATURA: "+str(tempIns)+"🌡️ HUMEDAD: "+str(humeIns)+"💦 PRESIÓN: "+str(presIns)+"⏱️")

#Simulamos un Do-While para que el programa nos premita verificar los que los valores no sobrepasen (se verificaran 3 valores).
while cont<3:
  #Tomamos los valores con el sense:
  tempSH = sense.get_temperature()
  humeSH = sense.get_humidity()
  presSH = sense.get_pressure()

  #Y redondeamos sus valoreS:
  tempSH = round(tempSH,1)
  humeSH = round(humeSH,1)
  presSH = round(presSH,1)

  if (tempSH >= tempIns):
    enviarMSG("⚠️¡ALERTA TEMPERATURA!⚠️\nLa temperatura es de: "+str(tempSH)+"C°")
    sense.clear()
    #Para el RGB del Sense HAT:
    impLED = 'T(C): '+str(tempSH)
    sense.show_message(impLED, text_colour = R)

  if (humeSH >= humeIns):
    enviarMSG("⚠️¡ALERTA HUMEDAD!⚠️\nLa humedad es de: "+str(humeSH)+"%")
    sense.clear()
    #Para el RGB del Sense HAT:
    impLED = 'H(%): '+str(humeSH)
    sense.show_message(impLED, text_colour = R)

  if (presSH >= presIns):
    enviarMSG("⚠️¡ALERTA PRESIÓN!⚠️\nLa presión es de: "+str(presSH)+" [Ombar]")
    sense.clear()
    #Para el RGB del Sense HAT:
    impLED = 'P(%): '+str(presSH)
    sense.show_message(impLED, text_colour = R)
  
  cont+=1
  time.sleep(muestreo)

