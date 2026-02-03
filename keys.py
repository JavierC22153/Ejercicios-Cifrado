import random
import string

# 1. Generar llave dinámica (ASCII)
def generar_llave_dinamica(longitud):
    caracteres_seguros = string.ascii_letters + string.digits + string.punctuation + ' '
    llave = ''.join(random.choice(caracteres_seguros) for _ in range(longitud))
    return llave

# 2. Cifrado ASCII con llave de tamaño fijo
def cifrar_ascii_llave_fija(texto, llave):
    resultado = []
    k_len = len(llave)

    for i, char in enumerate(texto):
        valor_texto = ord(char)
        valor_llave = ord(llave[i % k_len])
        cifrado = (valor_texto + valor_llave) % 256
        resultado.append(chr(cifrado))

    return ''.join(resultado)

# Función de descifrado para llave fija
def descifrar_ascii_llave_fija(texto_cifrado, llave):
    resultado = []
    k_len = len(llave)

    for i, char in enumerate(texto_cifrado):
        valor_cifrado = ord(char)
        valor_llave = ord(llave[i % k_len])
        descifrado = (valor_cifrado - valor_llave) % 256
        resultado.append(chr(descifrado))

    return ''.join(resultado)

# 3. Cifrado ASCII con llave de tamaño dinámico
def cifrar_ascii_llave_dinamica(texto):
    llave_dinamica = generar_llave_dinamica(len(texto))
    resultado = []

    for i in range(len(texto)):
        valor_texto = ord(texto[i])
        valor_llave = ord(llave_dinamica[i])
        cifrado = (valor_texto + valor_llave) % 256
        resultado.append(chr(cifrado))

    return ''.join(resultado), llave_dinamica

# Función de descifrado para llave dinámica
def descifrar_ascii_llave_dinamica(texto_cifrado, llave):
    resultado = []

    for i in range(len(texto_cifrado)):
        valor_cifrado = ord(texto_cifrado[i])
        valor_llave = ord(llave[i])
        descifrado = (valor_cifrado - valor_llave) % 256
        resultado.append(chr(descifrado))

    return ''.join(resultado)

# Ejemplo de uso
if __name__ == "__main__":
    mensaje = "Javier"
    print("Mensaje original:", mensaje)
    print()

    # 1. Llave dinámica
    llave = generar_llave_dinamica(5)
    print("1. Llave dinámica generada:", repr(llave))
    print()

    # 2. Cifrado con llave fija
    cifrado_fijo = cifrar_ascii_llave_fija(mensaje, llave)
    print("2. Cifrado con llave fija:", repr(cifrado_fijo))
    descifrado_fijo = descifrar_ascii_llave_fija(cifrado_fijo, llave)
    print("   Descifrado:", descifrado_fijo)
    print()

    # 3. Cifrado con llave dinámica
    cifrado_dinamico, llave_auto = cifrar_ascii_llave_dinamica(mensaje)
    print("3. Cifrado con llave dinámica:", repr(cifrado_dinamico))
    print("   Llave autogenerada:", repr(llave_auto))
    descifrado_dinamico = descifrar_ascii_llave_dinamica(cifrado_dinamico, llave_auto)
    print("   Descifrado:", descifrado_dinamico)