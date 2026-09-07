def calcular_total (precio, cantidad):
    total = precio * cantidad
    return total

if __name__ == "__main__":
    precio = 10
    cantidad = 3
    resultado = calcular_total (precio, cantidad)
    print("Total de la compra: $" + str(resultado))