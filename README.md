# SomePython-1
Algunos scripts útiles escritos en Python, útiles para empezar (comentados en español):
  1. MateriasNotas:
     Se utilizan listas, ciclos y funciones para realizar un script que verifique estado de notas.
       Aprueba: Mayor o igual que 18. Supletorio: entre 18 y 28 - 18 incluido, 28 sin incluir. Reprueba: menor a 18.
       
  2. CorreoFechaYHora:
     Permite enviar un correo electrónico indicando la fecha y hora de 8 países de diferentes zonas horarias.
     Para ello se debera tener un correo electronico con la autenticacion de 2 pasos (simplemente activada), luego
     se crea una contraseña de aplicación y una vez se haya hecho esto, se tendrá la API correspondiente para usar
     en el Script.
     
     Se uso listas y las librerías SMTPLIB, DATATIME y PYTZ.
     
  3. EnvioMSGBotTelegram:
     Permitirá enviar un mensaje a través de un bot de Telegram, utilizando el Token, el Message Id.
       El token se obtiene llamando al BotFather usando (secuencialmente): /start, /newbot, nombre Bot, nombre User.
       Se inicia el Bot con /star utilizando la URL entregada en el BotFather.
       El message Id se obtiene introduciendo https://api.telegram.org/bot<yourtoken>/getUpdates
     
<-------------------------------------->
Some useful scripts written in Python, useful to get started (commented in Spanish):
   1. MateriasNotas:
      Lists, loops and functions are used to create a script that checks the status of notes.
        Approves: Greater than or equal to 18. Supplementary: between 18 and 28 - 18 included, 28 not included. Fail: under 18.
       
   2. CorreoFechaYHora:
      It allows sending an email indicating the date and time of 8 countries in different time zones.
      To do this, you must have an email with 2-step authentication (simply activated), then
      an application password is created and once this is done, you will have the corresponding API to use
      in the Script.
     
      Lists and the SMTPLIB, DATATIME and PYTZ libraries were used.
     
   3. EnvioMSGBotTelegram:
      It will allow sending a message through a Telegram bot, using the Token, the Message Id.
        The token is obtained by calling BotFather using (sequentially): /start, /newbot, Bot name, User name.
        The Bot is started with /star using the URL given in the BotFather.
        The message Id is obtained by entering https://api.telegram.org/bot<yourtoken>/getUpdates
