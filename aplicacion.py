from finanzas import Finanzas

while True:
    print(
        "Porfavor, seleccione una de las opciones que se le presentan a continuacion: "
    )
    print("1. Iniciar cuenta, saldo: $0.00")
    print("2. Registrar un ingreso o salida.")
    print("3. Registro de ingresos.")
    print("4. Registro de salidas.")
    print("5. Registro de transacciones.")
    print("6. Total en cuenta.")
    print("7. Salir.")
    opcion = input("Numero: ")

    if opcion == "7":
        break
    elif opcion == "1":
        id = input("Porfavor, ingrese el Id de su cuenta: ")
        name = input("Su nombre: ")
        amount = 0.00
        finanzas = Finanzas(id, name, amount)
        print("Se ha iniciado la cuenta a $0.00")
    elif opcion == "2":
        op1 = input(
            "1. Registrar ingreso. 2. Registrar salida. Porfavor, Ingrese una opción: "
        )
        if op1 == "1":
            id = input("Ingrese el id del ingreso: ")
            amount = float(input("Ingrese el monto del ingreso: "))
            finanzas.regIngreso(id, amount)
        elif op1 == "2":
            id = input("Ingrese el id de la salida: ")
            amount = float(input("Ingrese el monto de la salida: "))
            finanzas.regSalida(id, amount)
    elif opcion == "3":
        print("Registro de ingresos: ")
        finanzas.regIngreso()
    elif opcion == "4":
        print("Registro de salidas: ")
        finanzas.regSalida()
    elif opcion == "5":
        print("Registro de transacciones: ")
        print("Registro de ingresos: ")
        finanzas.regIngreso()
        print("Registro de salidas: ")
        finanzas.regSalida()
    elif opcion == "6":
        name = finanzas.recuperarName()
        id = finanzas.recuperarId()
        amountF = finanzas.fAmount()
        print("El monto actual de la cuenta con Id {id} de {name} es: ${amountF}")
