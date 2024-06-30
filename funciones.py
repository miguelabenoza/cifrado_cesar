def cifrar(mensaje: str, d: int):
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    longitud_alfabeto = len(alfabeto)
    str_cifrado = ""

    for caracter in mensaje.upper():     
        if caracter in alfabeto:
            indice_actual_caracter = alfabeto.index(caracter)
            indice_desplazado = (indice_actual_caracter + d) % longitud_alfabeto
            str_cifrado += alfabeto[indice_desplazado]

    return str_cifrado

