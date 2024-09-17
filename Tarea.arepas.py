# Solicitar al usuario los ingredientes para hacer arepas

# Pedir cantidad de harina (en gramos)
harina = input("Ingrese la cantidad de harina (en gramos): ")

# Pedir cantidad de agua (en mililitros)
agua = input("Ingrese la cantidad de agua (en mililitros): ")

# Pedir cantidad de sal (en gramos)
sal = input("Ingrese la cantidad de sal (en gramos): ")

# Convertir los valores de entrada a flotantes
harina = float(harina)
agua = float(agua)
sal = float(sal)

# Calcular la masa total resultante (simple suma de los ingredientes)
masa_total = harina + agua + sal

# Mostrar la cantidad de masa resultante
print("La cantidad total de masa para arepas es:", masa_total, "gramos.")