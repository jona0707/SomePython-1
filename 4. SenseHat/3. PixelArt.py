#SomePython-1.4.3 ~ Jona
#-------------------#
#Imágenes o pixel arts generadas en el Sense HAT:
#Importo librerías:
from sense_emu import SenseHat
from time import sleep

#Inicio la variable
sense=SenseHat()

#Al ser pixel arts con colores especificos, puedo obtener su codigo rgb utilizando herramientas en web:
#Negro
n = (0,0,0) 
#Blanco
b = (255,255,255)

#EJEMPLO NO ESTILIZADO (se recomienda definir los rgb con la misma cantidad de caracteres, en este caso falla 'naO').
#PIKACHU
am = (255,241,0)
na = (255,152,0)
ca = (199,109,0)
naO = (255,150,0)
gr = (66,66,66)
ro = (255,33,4) 

pikachu = [
  b,gr,gr,b,b,b,b,gr,
  b,b,am,na,b,b,b,na,
  b,b,b,am,am,am,am,na,
  naO,naO,b,am,n,am,am,n,
  naO,naO,b,ro,am,am,am,na,
  b,ca,b,am,na,na,na,b,
  b,ca,am,naO,am,na,am,b,
  b,b,am,naO,ca,ca,naO,b
]

#DUENDE
az = (67,126,202)
ve = (62,167,15)
ka = (139,49,49)
to = (255,151,0)
pi = (221,154,67)
vo = (5,89,4)

duende = [
  az,ve,ve,ve,ve,ve,ve,az,
  to,ka,ka,ka,ka,ka,ka,to,
  to,to,n,to,to,n,to,to,
  to,to,n,to,to,n,to,to,
  az,to,to,to,to,to,to,az,
  az,ve,ve,ve,ve,ve,ve,az,
  ve,az,ve,ve,ve,ve,az,ve,
  az,pi,vo,gr,gr,vo,pi,az
]

#KIRBY
ci = (66,165,245)
rs = (248,187,208)
dr = (244,143,177)
mo = (26,35,126)
br = (240,98,146)
vi = (173,20,87)
pe = (194,24,91)
vd = (76,175,80)

kirby = [
  ci,ci,ci,ci,ci,ci,ci,ci,
  ci,ci,rs,rs,rs,rs,ci,ci,
  ci,rs,rs,rs,rs,rs,rs,ci,
  ci,dr,rs,n,rs,n,rs,ci,
  dr,rs,rs,mo,rs,mo,rs,dr,
  dr,dr,br,rs,rs,rs,br,dr,
  ci,vi,dr,dr,rs,rs,vi,ci,
  vd,vi,pe,pe,vd,vi,pe,vd
]


sense.set_pixels()

while True:
  sleep(100)

