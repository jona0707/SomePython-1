#SomePython-1.3 ~ Jona
#-------------------#
#Permitirá enviar un mensaje a través de un bot de Telegram, utilizando el Token, el Message Id. El token se obtiene llamando al BotFather usando 
#(secuencialmente): /start, /newbot, nombre Bot, nombre User. Se inicia el Bot con /star utilizando la URL entregada en el BotFather. 
#El message Id se obtiene introduciendo https://api.telegram.org/bot/getUpdates

#Librerias:
#Para GET
import requests

#Creo una funcion para usarla cada que se ejecute y se ingrese un mensaje:

def enviarMSG(msg):
    token = 'TOKEN'
    msgId = 'MSGID'
    msg = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+msgId+'&parse_mode=Markdown&text='+msg
    
    #Envio el mensaje
    requests.get(msg)
    
    #Para solicitar información de lo enviado y demás, en formato JSON para que sea legible:
    #response = requests.get(msg)
    #return response.json()


#Creo el main:
m = input("Escriba su mensaje: ")
enviarMSG(m)

#En caso de haber solicitado el json:
#msgE = enviarMSG(m)
#print('\nArchivo JSON como respuesta: \n')
#print(msgE)
