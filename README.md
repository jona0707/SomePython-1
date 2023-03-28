# SomePython-1
Algunos scripts útiles escritos en Python, útiles para empezar (comentados en español):
  1. MateriasNotas:
  
     Se utilizan listas, ciclos y funciones para realizar un script que verifique estado de notas.
       Aprueba: Mayor o igual que 18. Supletorio: entre 18 y 28 - 18 incluido, 28 sin incluir. Reprueba: menor a 18.
       
  2. CorreoFechaYHora:
  
     Permite enviar un correo electrónico indicando la fecha y hora de 8 países de diferentes zonas horarias.     
     Se uso listas y las librerías SMTPLIB, DATATIME y PYTZ.
     
  3. EnvioMSGBotTelegram:
 
     Permitirá enviar un mensaje a través de un bot de Telegram, utilizando el Token, el Message Id.
       
  4. SenseHat:
     Scripts que utilicen la placa SenseHat o en su defecto, el emulador. (Aplicación en Raspberry).
     
     1. AlertaTemporalTelegram:
     
        Permitirá enviar alertas de temperatura, humedad y presion con Sense HAT a un bot de Telegram (previamente programado).
        
     2. RellenoMySQL:
     
        Se llenarán los datos en una BDD utilizando el siguiente script, teniendo en cuenta la creación previa de
        un servidor LAMP cuya BDD está gestionada por MySQL utilizando PHPMyAdmin.
        
     3. PixelArt:
     
        Imágenes o pixel arts generadas en el Sense HAT.
     
<------->

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
        
   4. SenseHat:
      Scripts that use the SenseHat board or, failing that, the emulator. (Application in Raspberry).
     
      1. AlertaTemporalTelegram:
     
         It will allow sending temperature, humidity and pressure alerts with Sense HAT to a Telegram bot (previously programmed).
        
      2. RellenoMySQL:
     
         The data will be filled in a BDD using the following script, taking into account the previous creation of
         a LAMP server whose DB is managed by MySQL using PHPMyAdmin.
        
      3. PixelArt:
     
         Images or pixel arts generated in the Sense HAT.
