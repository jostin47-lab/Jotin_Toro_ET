def mostrar_menu():
    print()
    print("========== GIMNASIO FITPASS ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("======================================")


def leer_opcion():
    opcion_valida = False
    opcion = 0

    while opcion_valida == False:
        try:
            opcion = int(input("Ingrese una opción del 1 al 6: "))

            if opcion >= 1 and opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")

        except ValueError:
            print("Debe seleccionar una opción válida")

    return opcion


def cupos_tipo(tipo, planes, inscripciones):
    total_cupos = 0

    for codigo in planes:
        if planes[codigo][1].lower() == tipo.lower():
            if codigo in inscripciones:
                total_cupos = total_cupos + inscripciones[codigo][1]

    print("El total de cupos disponibles es:", total_cupos)


def busqueda_precio(p_min, p_max, planes, inscripciones):
    resultados = []

    for codigo in inscripciones:
        precio = inscripciones[codigo][0]
        cupos = inscripciones[codigo][1]

        if precio >= p_min and precio <= p_max and cupos != 0:
            nombre = planes[codigo][0]
            resultado = nombre + "--" + codigo
            resultados.append(resultado)

    resultados.sort()

    if len(resultados) == 0:
        print("No hay planes en ese rango de precios.")
    else:
        print("Los planes encontrados son:", resultados)


def buscar_codigo(codigo, planes, inscripciones):
    codigo = codigo.upper()

    for codigo_guardado in planes:
        if codigo_guardado.upper() == codigo:
            return True

    for codigo_guardado in inscripciones:
        if codigo_guardado.upper() == codigo:
            return True

    return False


def actualizar_precio(codigo, nuevo_precio, planes, inscripciones):
    codigo = codigo.upper()

    if buscar_codigo(codigo, planes, inscripciones) == True:
        if codigo in inscripciones:
            inscripciones[codigo][0] = nuevo_precio
            return True

    return False


def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    else:
        return True


def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True


def validar_tipo(tipo):
    tipo = tipo.lower()

    if tipo == "mensual" or tipo == "trimestral" or tipo == "anual":
        return True
    else:
        return False


def validar_duracion(duracion):
    if duracion > 0:
        return True
    else:
        return False


def validar_acceso_piscina(acceso_piscina):
    acceso_piscina = acceso_piscina.lower()

    if acceso_piscina == "s" or acceso_piscina == "n":
        return True
    else:
        return False


def validar_incluye_clases(incluye_clases):
    incluye_clases = incluye_clases.lower()

    if incluye_clases == "s" or incluye_clases == "n":
        return True
    else:
        return False


def validar_horario(horario):
    if horario.strip() == "":
        return False
    else:
        return True


def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False


def validar_cupos(cupos):
    if cupos >= 0:
        return True
    else:
        return False


def agregar_plan(codigo, nombre, tipo, duracion,
                 acceso_piscina, incluye_clases,
                 horario, precio, cupos,
                 planes, inscripciones):

    codigo = codigo.upper()

    if buscar_codigo(codigo, planes, inscripciones) == True:
        return False

    if acceso_piscina.lower() == "s":
        piscina = True
    else:
        piscina = False

    if incluye_clases.lower() == "s":
        clases = True
    else:
        clases = False

    planes[codigo] = [
        nombre,
        tipo.lower(),
        duracion,
        piscina,
        clases,
        horario
    ]

    inscripciones[codigo] = [
        precio,
        cupos
    ]

    return True


def eliminar_plan(codigo, planes, inscripciones):
    codigo = codigo.upper()

    if buscar_codigo(codigo, planes, inscripciones) == True:
        if codigo in planes and codigo in inscripciones:
            del planes[codigo]
            del inscripciones[codigo]
            return True

    return False


planes = {
    "F001": ["Plan Básico", "mensual", 1, False, False, "libre"],
    "F002": ["Plan Full", "mensual", 1, True, True, "libre"],
    "F003": ["Plan Estudiante", "trimestral", 3, False, True, "tarde"],
    "F004": ["Plan Senior", "trimestral", 3, True, False, "mañana"],
    "F005": ["Plan Anual Pro", "anual", 12, True, True, "libre"],
    "F006": ["Plan Nocturno", "mensual", 1, False, True, "noche"]
}


inscripciones = {
    "F001": [14990, 30],
    "F002": [22990, 10],
    "F003": [39990, 0],
    "F004": [35990, 6],
    "F005": [159990, 2],
    "F006": [18990, 15]
}


opcion = 0

while opcion != 6:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:

        tipo = input(
            "Ingrese el tipo de plan (mensual/trimestral/anual): "
        ).lower()

        while validar_tipo(tipo) == False:
            print("Debe ingresar mensual, trimestral o anual")

            tipo = input(
                "Ingrese el tipo de plan (mensual/trimestral/anual): "
            ).lower()

        cupos_tipo(tipo, planes, inscripciones)

    elif opcion == 2:

        precios_validos = False

        while precios_validos == False:

            try:
                print("Los precios deben ser números enteros mayores o iguales a cero")

                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))

                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    precios_validos = True
                else:
                    print("El precio mínimo debe ser menor o igual al máximo")

            except ValueError:
                print("Debe ingresar valores enteros")

        busqueda_precio(
            p_min,
            p_max,
            planes,
            inscripciones
        )

    elif opcion == 3:

        continuar = "s"

        while continuar == "s":

            codigo = input(
                "Ingrese el código del plan, por ejemplo F001: "
            ).upper()

            precio_valido = False

            while precio_valido == False:

                try:
                    nuevo_precio = int(
                        input("Ingrese el nuevo precio, mayor que cero: ")
                    )

                    if validar_precio(nuevo_precio) == True:
                        precio_valido = True
                    else:
                        print("El precio debe ser mayor que cero")

                except ValueError:
                    print("Debe ingresar un precio entero")

            actualizado = actualizar_precio(
                codigo,
                nuevo_precio,
                planes,
                inscripciones
            )

            if actualizado == True:
                print("Precio actualizado")
            else:
                print("El código no existe")

            respuesta_valida = False

            while respuesta_valida == False:

                continuar = input(
                    "¿Desea actualizar otro precio? (s = sí / n = no): "
                ).lower()

                if continuar == "s" or continuar == "n":
                    respuesta_valida = True
                else:
                    print("Debe ingresar s o n")

    elif opcion == 4:

        codigo = input(
            "Ingrese código del plan, por ejemplo F010: "
        ).upper()

        nombre = input("Ingrese nombre del plan: ")

        tipo = input(
            "Ingrese tipo de plan (mensual/trimestral/anual): "
        ).lower()

        datos_enteros_validos = True

        try:
            duracion = int(
                input("Ingrese duración en meses, mayor que cero: ")
            )

            acceso_piscina = input(
                "¿Incluye acceso a piscina? (s = sí / n = no): "
            ).lower()

            incluye_clases = input(
                "¿Incluye clases grupales? (s = sí / n = no): "
            ).lower()

            horario = input(
                "Ingrese horario (mañana/tarde/noche/libre): "
            )

            precio = int(
                input("Ingrese precio, mayor que cero: ")
            )

            cupos = int(
                input("Ingrese cupos disponibles, mayor o igual a cero: ")
            )

        except ValueError:
            print("Duración, precio y cupos deben ser valores enteros")
            datos_enteros_validos = False

        if datos_enteros_validos == True:

            datos_validos = True

            if validar_codigo(codigo) == False:
                print("El código no puede estar vacío")
                datos_validos = False

            elif buscar_codigo(codigo, planes, inscripciones) == True:
                print("El código ya existe")
                datos_validos = False

            elif validar_nombre(nombre) == False:
                print("El nombre no puede estar vacío")
                datos_validos = False

            elif validar_tipo(tipo) == False:
                print("El tipo debe ser mensual, trimestral o anual")
                datos_validos = False

            elif validar_duracion(duracion) == False:
                print("La duración debe ser mayor que cero")
                datos_validos = False

            elif validar_acceso_piscina(acceso_piscina) == False:
                print("El acceso a piscina debe ser s o n")
                datos_validos = False

            elif validar_incluye_clases(incluye_clases) == False:
                print("La inclusión de clases debe ser s o n")
                datos_validos = False

            elif validar_horario(horario) == False:
                print("El horario no puede estar vacío")
                datos_validos = False

            elif validar_precio(precio) == False:
                print("El precio debe ser mayor que cero")
                datos_validos = False

            elif validar_cupos(cupos) == False:
                print("Los cupos deben ser mayores o iguales a cero")
                datos_validos = False

            if datos_validos == True:

                agregado = agregar_plan(
                    codigo,
                    nombre,
                    tipo,
                    duracion,
                    acceso_piscina,
                    incluye_clases,
                    horario,
                    precio,
                    cupos,
                    planes,
                    inscripciones
                )

                if agregado == True:
                    print("Plan agregado")
                else:
                    print("El código ya existe")

    elif opcion == 5:

        codigo = input(
            "Ingrese el código del plan que desea eliminar, por ejemplo F001: "
        ).upper()

        eliminado = eliminar_plan(
            codigo,
            planes,
            inscripciones
        )

        if eliminado == True:
            print("Plan eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")