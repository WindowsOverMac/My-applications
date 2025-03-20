# Traducido al español
import random
print("¿Lanzar los dados?")  

userinput = input()

if userinput in ["sí", "claro", "sip", "si", "ye", "y"]:
    random_int = random.randint(1, 60)
    print(random_int)
else:
    print("No se lanzaron. O denegado o sintaxis inválida.") 
  
  




























