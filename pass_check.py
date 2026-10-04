# Pedimos al usuario que ingrese la contraseña
password = input("Introduce la contraseña que deseas evaluar: ")

# Creamos variables para registrar si cumple con los requisitos
largo_correcto = len(password) >= 8
tiene_numero = False
tiene_mayuscula = False

# Revisamos cada carácter de la contraseña uno por uno
for caracter in password:
    if caracter.isdigit():    # ¿Es un número?
        tiene_numero = True
    if caracter.isupper():    # ¿Es una letra mayúscula?
        tiene_mayuscula = True

# Verificamos si cumple absolutamente todos los requisitos
if largo_correcto and tiene_numero and tiene_mayuscula:
    print("✅ ¡Contraseña segura y válida!")
else:
    print("❌ Contraseña insegura. Debe cumplir los siguientes requisitos:")
    
    # Le mostramos al usuario exactamente qué le faltó
    if not largo_correcto:
        print("  - Debe tener al menos 8 caracteres.")
    if not tiene_numero:
        print("  - Debe incluir al menos un número.")
    if not tiene_mayuscula:
        print("  - Debe incluir al menos una letra mayúscula.")

input("Presiona Enter para salir...")