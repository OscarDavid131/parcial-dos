# Definir la función a y b
def calcular_bonificacion(salario_base, cargo, desempeño):
    cargo = cargo.lower()
    desempeño = desempeño.lower()

    bonificacion = 0

    if cargo == "directivo":
        if desempeño == "alto":
            bonificacion = salario_base * 0.20
        elif desempeño == "medio":
            bonificacion = salario_base * 0.10
    elif cargo == "operativo":
        if desempeño == "alto":
            bonificacion = salario_base * 0.15
        elif desempeño == "medio":
            bonificacion = salario_base * 0.05

    return bonificacion

# Solicitar datos
salario_base = float(input("Salario base mensual: "))
cargo = input("Cargo del empleado: ").strip()
desempeño = input("Nivel de desempeño: ").strip()

# Calcular la bonificación con los datos ingresados
bonificacion = calcular_bonificacion(salario_base, cargo, desempeño)

# Calcular el total a recibir
total = salario_base + bonificacion

# Imprimir el resumen del pago
print(f"\n-----Resumen del Pago-----")
print(f"Cargo: {cargo.capitalize()}")
print(f"Nivel de Desempeño: {desempeño.capitalize()}")
print(f"Salario Base: ${salario_base:,.2f}")
print(f"Bonificación: ${bonificacion:,.2f}")
print(f"Total a Recibir: ${total:,.2f}")
print(f"------------------------------------\n")

