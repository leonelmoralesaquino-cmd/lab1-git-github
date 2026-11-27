def saludar(nombre: str) -> str:
    return f"¡Hola, {nombre}! Bienvenido al proyecto colaborativo con Git y GitHub."

if __name__ == "__main__":
    usuario = input("Ingresa tu nombre: ")
    print(saludar(usuario))
