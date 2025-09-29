print("¡Bienvenido al convertidor de números!")

# Bucle principal del programa
while True:
    print("\nSelecciona el tipo de conversión:")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

    seleccion = input("Ingresa tu opción (1, 2 o 3): ")

    match seleccion:
        case "1":
            print("\n--- Conversión: Decimal a Binario ---")
            
            while True:
                numero_decimal_str = input("Ingresa un número decimal positivo: ")
            
                # Validación de entrada decimal
                if numero_decimal_str.isdigit():
                    numero_decimal = int(numero_decimal_str)

                    # Conversión de Decimal a Binario
                    binario = ""
                    numero = numero_decimal

                    if numero == 0:
                        binario = "0"
                    else:
                        while numero > 0:
                            resto = numero % 2       # Calcula el resto de dividir por 2
                            binario = str(resto) + binario  # Lo agrega al principio
                            numero = numero // 2     # División entera por 2

                    print(f"Equivalente en binario: {binario}")
                    break  # Salir del bucle de validación
                else:
                    print("Entrada inválida. Por favor, ingresa solo dígitos.")

        case "2":
            print("\n--- Conversión: Binario a Decimal ---")
            # Para binario a decimal: recorrer el número binario de derecha a izquierda, multiplicando cada dígito por 2^posición.

            while True:
                numero_binario_str = input("Ingresa un número binario (solo 0s y 1s): ")
            
                valido = True
                # Recorrido y validación del número binario

                if not numero_binario_str.isdigit():
                    valido = False
                    
                for digito in numero_binario_str:
                    if digito not in ("0", "1"):
                        valido = False
                        break

                # Conversión de numero Binario a Decimal
                if valido:
                    decimal = 0 # acumulador para el resultado en base 10
                    potencia = 0 # posición del digito (empezamos en la derecha)

                    for digito in numero_binario_str[::-1]: # Recorre los digitos del numero binario a la inversa
                        decimal += int(digito) * (2 ** potencia)
                        # convertimos el carácter ('0' o '1') a número entero
                        # multiplicamos por 2^potencia y lo sumamos al acumulador
                        potencia += 1 # Aumentamos la potencia de 2 para el siguiente digito
                    print("El decimal es:", decimal)
                    break
                else:
                    print("Error: El número ingresado no es binario válido.")

        case "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break # Salir del bucle principal
        case _:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")