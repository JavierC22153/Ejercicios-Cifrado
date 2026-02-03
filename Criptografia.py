import base64

# ---------- ASCII → BINARIO ----------
def ascii_a_binario(texto):
    binarios = []
    for caracter in texto:
        codigo_ascii = ord(caracter)                        # ej: 'A' → 65
        bits = format(codigo_ascii, '08b')                  # ej: 65 → '01000001'
        binarios.append(bits)
    return ' '.join(binarios)

# ---------- BINARIO → ASCII ----------
def binario_a_ascii(binario):
    grupos = binario.replace(' ', '')                       # elimina espacios
    if len(grupos) % 8 != 0:
        return "Error: el binario debe tener un múltiplo de 8 bits."
    texto = ''
    for i in range(0, len(grupos), 8):
        byte = grupos[i:i+8]                                # ej: '01000001'
        numero = int(byte, 2)                               # ej: 65
        texto += chr(numero)                                # ej: 'A'
    return texto

# ---------- ASCII → BASE64 ----------
def ascii_a_base64(texto):
    return base64.b64encode(texto.encode('utf-8')).decode('utf-8')


# ---------- BASE64 → ASCII ----------
def base64_a_ascii(texto_base64):
    try:
        binario = base64_a_binario(texto_base64)            # BASE64 → BINARIO
        ascii_final = binario_a_ascii(binario)              # BINARIO → ASCII
        return ascii_final
    except Exception as e:
        return f"Error: {e}"


# ---------- TEXT ASCII → BASE64 (pasando por BINARIO) ----------
def ascii_a_base64_por_binario(texto):
    binario = ascii_a_binario(texto)                       
    base64_resultado = binario_a_base64(binario)            
    return base64_resultado


# ---------- BASE64 → BINARIO ----------
def base64_a_binario(texto_base64):
    bytes_decodificados = base64.b64decode(texto_base64)
    binarios = [format(byte, '08b') for byte in bytes_decodificados]
    return ' '.join(binarios)


# ---------- BINARIO → BASE64 ----------
def binario_a_base64(binario):
    grupos = binario.replace(' ', '')
    if len(grupos) % 8 != 0:
        return "Error: el binario debe tener un múltiplo de 8 bits."
    bytes_lista = []
    for i in range(0, len(grupos), 8):
        byte = int(grupos[i:i+8], 2)
        bytes_lista.append(byte)
    return base64.b64encode(bytes(bytes_lista)).decode('utf-8')


# ---------- XOR sobre BINARIO ----------
def xor_binario(binario1, binario2):
    b1 = binario1.replace(' ', '')
    b2 = binario2.replace(' ', '')

    if len(b1) == 0 or len(b2) == 0:
        return "Error: ambas cadenas deben tener al menos 1 bit."

    # Repetir b2 (clave) para que cubra toda la longitud de b1
    clave_repetida = (b2 * (len(b1) // len(b2) + 1))[:len(b1)]

    resultado = ''
    for bit_a, bit_b in zip(b1, clave_repetida):
        resultado += str(int(bit_a) ^ int(bit_b))

    # Insertar espacios cada 8 bits para leer mejor
    resultado_formateado = ' '.join(resultado[i:i+8] for i in range(0, len(resultado), 8))
    return resultado_formateado



def mostrar_menu():
    print("\n" + "=" * 55)
    print("  Ejercicio de Criptografía")
    print("=" * 55)
    print("  1) ASCII  →  BINARIO")
    print("  2) BASE64 →  BINARIO")
    print("  3) BINARIO → BASE64")
    print("  4) BINARIO → ASCII")
    print("  5) BASE64 →  ASCII  (pasa por binario)")
    print("  6) XOR    aplicado a BINARIO")
    print("  0) Salir")
    print("-" * 55)
    return input("  Selecciona una opción: ").strip()


def main():
    while True:
        opcion = mostrar_menu()

        # 1) ASCII → BINARIO
        if opcion == '1':
            texto = input("\n  Ingresa el texto ASCII: ")
            resultado = ascii_a_binario(texto)
            print(f"\n   Binario:\n    {resultado}")

        # 2) BASE64 → BINARIO
        elif opcion == '2':
            texto = input("\n  Ingresa el texto BASE64: ")
            resultado = base64_a_binario(texto)
            print(f"\n   Binario:\n    {resultado}")

        # 3) BINARIO → BASE64 
        elif opcion == '3':
            texto = input("\n  Ingresa el binario (bits separados por espacio): ")
            resultado = binario_a_base64(texto)
            print(f"\n   BASE64:\n    {resultado}")

        # 4) BINARIO → ASCII 
        elif opcion == '4':
            texto = input("\n  Ingresa el binario (bits separados por espacio): ")
            resultado = binario_a_ascii(texto)
            print(f"\n   ASCII:\n    {resultado}")

        # 5) BASE64 → ASCII (por binario)
        elif opcion == '5':
            texto = input("\n  Ingresa el texto BASE64: ")
            paso1 = base64_a_binario(texto)
            paso2 = binario_a_ascii(paso1)
            print(f"\n  → Paso 1 (BASE64 → Binario):\n    {paso1}")
            print(f"  → Paso 2 (Binario  → ASCII):\n    {paso2}")

        # 6) XOR sobre BINARIO
        elif opcion == '6':
            bin1 = input("\n  Ingresa el primer binario  (mensaje): ")
            bin2 = input("  Ingresa el segundo binario (clave)  : ")
            resultado = xor_binario(bin1, bin2)
            print(f"\n  Resultado XOR:\n    {resultado}")

        # 0) Salir
        elif opcion == '0':
            print("\n  ¡Hasta luego!\n")
            break

        else:
            print("\n   Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()