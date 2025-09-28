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


                # Aquí irá el código para la conversión de Decimal a Binario



                    print(f"Número decimal ingresado: {numero_decimal}")
                # Código de conversión...
                    break # Salir del bucle de validación
                else:
                    print("Entrada inválida. Por favor, ingresa solo dígitos.")

        case "2":
            print("\n--- Conversión: Binario a Decimal ---")
        
            while True:
                numero_binario_str = input("Ingresa un número binario (solo 0s y 1s): ")
            
            # Validación de entrada binaria
                es_valido = True
                for digito in numero_binario_str:
                    if digito not in ('0', '1'):
                        es_valido = False
                        break
                if es_valido:



                    # Aquí irá el código para la conversión de Binario a Decimal





                    print(f"Número binario ingresado: {numero_binario_str}")
                # Código de conversión...
                    break # Salir del bucle de validación
                else:
                    print("Entrada inválida. Por favor, ingresa solo 0s y 1s.")

        case "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break # Salir del bucle principal
        case _:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")