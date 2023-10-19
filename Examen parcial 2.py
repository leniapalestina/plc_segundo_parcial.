#Gestión de tareas diarias 

Día=int(input("Inserta el día de la semana (1-7):"))
Hora=int(input("Inserta la hora actual (en formato de 24 horas):"))
if Hora >1<=5:
  print("Debes estar dormido")
elif Hora >5<=14:
  print("Debes estar en clase")
elif Hora >14<=22:
  print("Puedes hacer tareas")


Estudios=(input("Inserta si la tarea es estudio, descanso o trabajo:"))
if Hora <18>=22 and Estudios=="descanso":
  print("Además de tomar una siesta puedes comenzar a realizar tus tareas")
  
if Hora <18>=22 and Día==6 and 7:
  print("Puedes ver una película")
elif Hora <14>=20 and Día== 1 and 3 and 5:
  print("Puedes ir al gimnasio")
elif Hora <13>=15 and Día== 2 and 4:
  print("Esperto estés comiendo algo muy nutritivo")
