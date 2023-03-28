#SomePython-1.1 ~ Jona
#-------------------#
#Se utilizan listas, ciclos y funciones para realizar un script que verifique estado de notas. 
#Aprueba: Mayor o igual que 18. Supletorio: entre 18 y 28 - 18 incluido, 28 sin incluir. Reprueba: menor a 18.

#Se implementaran arrays (listas) donde incluir las materias.
suple = []
notaSMin = []
auxNotas = []
materias = []
notasTotales = []
op = 0
numMat = 0


def verifNota(nota):
  if (nota < 0) or (nota > 20):
    return 1
  else:
    return 0

def impArray(array):
  for iArray in array:
    print(iArray)

def impMatNot(mat, nota):
  print('\nMATERIA: NOTA FINAL')
  for i in range(len(mat)):
    conc = mat[i] + ': ' + str(nota[i])
    print(conc)

def impAprob(mat, nota):
  print('\nMATERIAS APROBADAS: ')
  for i in range(len(mat)):
    if(nota[i]>=28):
      print(mat[i])


def impReprob(mat, nota):
  print('\nMATERIAS REPROBADAS (A REPETIR): ')
  for i in range(len(mat)):
    if(nota[i]<18):
      print(mat[i])

def impSuple(mat,nota):
  for i in range(len(mat)):
    if((nota[i]>=18) and (nota[i]<28)):
      notaSM = 48 - nota[i]
      if notaSM>=24:
        notaSMin.append(notaSM)
        suple.append(materias[i])
      else:
        notaSMin.append(24)
        suple.append(materias[i])


  print('\nMATERIA: NOTA MÍNIMA EXAMEN FINAL')
  for i in range(len(suple)):
    conc = suple[i] + ': ' + str(notaSMin[i])
    print(conc)

print("Sistema de calificaciones:")
while op != '6':
  print('1. Ingresar materias de su curso.')
  print('2. Ingresar notas de materias.')
  print('3. Materias aprobadas.')
  print('4. Materias reprobadas.')
  print('5. Materias a dar examen final y el minimo para aprobar.')
  print('6. Salir.')
  op = input('Ingrese la opcion que guste (Recorriendo el programa en orden): ')

  if op == '1':
    numMat = input('Ingrese el número de materias a ingresar: ')
    for i in range(1,int(numMat)+1,1):
      notaTotal = 0
      materiai = input('Ingrese el nombre de la materia ' +str(i)+ ' por favor: ')
      materias.append(materiai)
    print("\nSUS MATERIAS SON: ")
    impArray(materias)
    print('\n')
  elif op == '2':
    for materia in materias:
      print('Materia: '+materia)
      while True:
        nota1B = input('Ingrese la calificación de su primer bimestre (1BIM): ')
        try:
          if verifNota(float(nota1B))== 0:
            break
          else:
            print('Ingrese un número dentro del rango (0-20)')
        except:
          print('El valor ingresado NO es un número.')

      while True:
        nota2B = input('Ingrese la calificación de su segundo bimestre (2BIM): ')
        try:
          if verifNota(float(nota2B))== 0:
            break
          else:
            print('Ingrese un número dentro del rango (0-20)')
        except:
          print('El valor ingresado NO es un número.')
      notaTotal = float(nota1B) + float(nota2B)
      notasTotales.append(notaTotal)
    impMatNot(materias, notasTotales)
    print('\n')

  elif op == '3':
    impAprob(materias, notasTotales)
    print('\n')

  elif op == '4':
    impReprob(materias, notasTotales)
    print('\n')

  elif op == '5':
    impSuple(materias, notasTotales)
    print('\n')

