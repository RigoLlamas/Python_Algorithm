"""
1.-
Solicitar el RFC e imprimir su homoclave (Solo los ultimos 3 caracteres)

2.-
Solicictar una cadena de caracteres "texto" y una cadena de caracteres "consulta".
Si segunda cadena aparece exactamente dentro de la primera mostrar True y por otro lado False

3.-
Solicitar el nombre completo de una persona:
    Eliminar los espacios inecesarios del texto.
    Determinar si todas las letras ingresadas son minusculas
    Determinar si el nombre empieza con una vocal no acentuda.
    Determinar cuantas vocales no acentudas existen.
    Para determinar y mostrar en pantalla (True/False).
"""

opcion = 0
while opcion != "S":
    opcion = input("[1] Imprimir homoclave. \n[2] Encontrar textos en otros textos. \n[3] Curiosidades sobre mi nombre\n[S] Salir\n")
    if opcion == "1":
        print("Imprimir homoclave")
        RFC = input("Ingrese su RFC: ")
        print("Tu homocalve es: " + RFC[10:13:1])
    elif opcion == "2":
        print("Encontrar texto en otros textos")
        texto = input("Ingrese el texto base: ")
        consulta = input("Ingrese el fragmento de texto a buscar: ")
        print("¿Existe en el texto? :", consulta in texto)

    elif opcion == "3":
        print("Curiosidades sobre mi nombre")
        nombre = input("Ingrese su nombre: ").strip()
        print("¿Todas las letras son minusculas?", nombre.islower())
        print("¿Inicia con vocal acentuada?", nombre.startswith(("á", "é", "í", "ó", "ú")))

        cantidadVocales = nombre.count("a") + nombre.count("e") + nombre.count("i") + nombre.count("o") + nombre.count("u")
        cantidadVocalesAcentuadas = nombre.count("á") + nombre.count("é") + nombre.count("í") + nombre.count("ó") + nombre.count("ú")

        print("Total de vocales: ", cantidadVocales + cantidadVocalesAcentuadas)
        print("Vocales acentudas: ", cantidadVocalesAcentuadas)
        print("Vocales no acentudas: ", cantidadVocales )

    print("\n")