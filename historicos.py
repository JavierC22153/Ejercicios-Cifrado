# Cifrado César
def cesar_cifrar(mensaje, desplazamiento):
    resultado = ""

    for caracter in mensaje:
        codigo = ord(caracter)

        if 65 <= codigo <= 90:
            nuevo = ((codigo - 65 + desplazamiento) % 26) + 65
            resultado += chr(nuevo)

        elif 97 <= codigo <= 122:
            nuevo = ((codigo - 97 + desplazamiento) % 26) + 97
            resultado += chr(nuevo)

        else:
            resultado += caracter

    return resultado

def cesar_descifrar(mensaje, desplazamiento):
    return cesar_cifrar(mensaje, -desplazamiento)

# ROT13 (reutiliza César)
def rot13(mensaje):
    return cesar_cifrar(mensaje, 13)

# Cifrado Vigenère
def vigenere_cifrar(mensaje, clave):
    resultado = ""
    indice_clave = 0
    clave = clave.lower()

    for caracter in mensaje:
        codigo = ord(caracter)

        if caracter.isalpha():
            k = ord(clave[indice_clave % len(clave)]) - 97
            indice_clave += 1

            if 65 <= codigo <= 90:
                nuevo = ((codigo - 65 + k) % 26) + 65
            else:
                nuevo = ((codigo - 97 + k) % 26) + 97

            resultado += chr(nuevo)
        else:
            resultado += caracter

    return resultado

def vigenere_descifrar(mensaje, clave):
    resultado = ""
    indice_clave = 0
    clave = clave.lower()

    for caracter in mensaje:
        codigo = ord(caracter)

        if caracter.isalpha():
            k = ord(clave[indice_clave % len(clave)]) - 97
            indice_clave += 1

            if 65 <= codigo <= 90:
                nuevo = ((codigo - 65 - k) % 26) + 65
            else:
                nuevo = ((codigo - 97 - k) % 26) + 97

            resultado += chr(nuevo)
        else:
            resultado += caracter

    return resultado

# Análisis de Frecuencia
def analisis_frecuencia(mensaje):
    frecuencia = {}

    for caracter in mensaje.lower():
        if caracter.isalpha():
            if caracter in frecuencia:
                frecuencia[caracter] += 1
            else:
                frecuencia[caracter] = 1

    total = sum(frecuencia.values())
    
    if total == 0:
        print("No hay letras para analizar.")
        return frecuencia

    print("\n" + "="*50)
    print("ANÁLISIS DE FRECUENCIA DE CARACTERES")
    print("="*50)
    print(f"{'Carácter':<12} | {'Frecuencia':<12} | {'Porcentaje':<12}")
    print("-" * 50)

    for letra in sorted(frecuencia.keys(), key=lambda x: frecuencia[x], reverse=True):
        conteo = frecuencia[letra]
        porcentaje = (conteo / total) * 100
        barra = "█" * int(porcentaje / 2)
        print(f"    {letra:<8} | {conteo:^12} | {porcentaje:>6.2f}%  {barra}")
    
    print("-" * 50)
    print(f"Total de letras analizadas: {total}")
    print("="*50 + "\n")

    return frecuencia

# MENÚ INTERACTIVO
def mostrar_menu():
    print("\n" + "="*60)
    print(" SISTEMA DE CIFRADO CLÁSICO")
    print("="*60)
    print("1. Cifrado César")
    print("2. ROT13")
    print("3. Cifrado Vigenère")
    print("4. Análisis de Frecuencia")
    print("5. Salir")
    print("="*60)

def menu_cesar():
    print("\n--- CIFRADO CÉSAR ---")
    mensaje = input("Ingrese el mensaje: ")
    
    while True:
        try:
            desplazamiento = int(input("Ingrese el desplazamiento (número entero): "))
            break
        except ValueError:
            print(" Error: Debe ingresar un número entero.")
    
    cifrado = cesar_cifrar(mensaje, desplazamiento)
    descifrado = cesar_descifrar(cifrado, desplazamiento)
    
    print("\n" + "="*60)
    print(" MENSAJE ORIGINAL:")
    print(f"   {mensaje}")
    print("\n MENSAJE CIFRADO:")
    print(f"   {cifrado}")
    print(f"   (con desplazamiento: {desplazamiento})")
    print("\n MENSAJE DESCIFRADO:")
    print(f"   {descifrado}")
    print("="*60)

def menu_rot13():
    print("\n--- ROT13 ---")
    mensaje = input("Ingrese el mensaje: ")
    
    cifrado = rot13(mensaje)
    descifrado = rot13(cifrado)
    
    print("\n" + "="*60)
    print(" MENSAJE ORIGINAL:")
    print(f"   {mensaje}")
    print("\n MENSAJE CON ROT13:")
    print(f"   {cifrado}")
    print("\n APLICANDO ROT13 NUEVAMENTE (descifrado):")
    print(f"   {descifrado}")
    print("="*60)

def menu_vigenere():
    print("\n--- CIFRADO VIGENÈRE ---")
    mensaje = input("Ingrese el mensaje: ")
    clave = input("Ingrese la clave (palabra alfabética): ")
    
    if not clave or not clave.replace(" ", "").isalpha():
        print(" Error: La clave debe contener solo letras.")
        return
    
    cifrado = vigenere_cifrar(mensaje, clave)
    descifrado = vigenere_descifrar(cifrado, clave)
    
    print("\n" + "="*60)
    print(" MENSAJE ORIGINAL:")
    print(f"   {mensaje}")
    print("\n CLAVE:")
    print(f"   {clave}")
    print("\n MENSAJE CIFRADO:")
    print(f"   {cifrado}")
    print("\n MENSAJE DESCIFRADO:")
    print(f"   {descifrado}")
    print("="*60)

def menu_analisis():
    print("\n--- ANÁLISIS DE FRECUENCIA ---")
    print("Ingrese el texto a analizar (puede ser varias líneas).")
    print("Presione Enter dos veces para finalizar:\n")
    
    lineas = []
    while True:
        linea = input()
        if linea == "":
            break
        lineas.append(linea)
    
    texto = " ".join(lineas)
    
    if not texto.strip():
        print(" Error: No se ingresó ningún texto.")
        return
    
    print(f"\n Texto a analizar: '{texto}'")
    analisis_frecuencia(texto)

def main():
    while True:
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            menu_cesar()
        
        elif opcion == "2":
            menu_rot13()
        
        elif opcion == "3":
            menu_vigenere()
        
        elif opcion == "4":
            menu_analisis()
        
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\n Opción no válida. Por favor, elija una opción del 1 al 5.")
        
        input("\nPresione Enter para continuar")

if __name__ == "__main__":
    main()