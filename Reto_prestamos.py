https://replit.com/@Lenia-Palestina/P2Reto?s=app

print("Hola!, estoy aquí para ayudarte a analizar el prestamo")
cantidad=int(input("Inserta la cantidad del préstamo:"))
tasa=int(input("Inserta la tasa de interes anual:"))
plazo=int(input("Inserta el plazo del prestamo (En años):"))

if tasa<=5 and plazo<=5: 
  print("Préstamo de bajo riesgo")
elif tasa>5 or plazo>5:
  print("Préstamo de medio riesgo")
else: 
  print("Préstamo de alto riesgo")
