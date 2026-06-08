
def verificar_tipo(valor):
    print(f"Valor recibido: {valor} (tipo: {type(valor).__name__})")
    match valor:
        case 1:
            return "Es un número entero"
        case "texto":
            return "Es una cadena de texto"
        case 3.14:
            return "Es un número decimal"
        case _:
            return "Es un tipo de dato no reconocido"

resultado = verificar_tipo(5)
print(resultado)