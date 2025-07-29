"""
Credit to https://github.com/efrenfuentes
Who created the original version
https://gist.github.com/efrenfuentes/3785655
"""

MONEDA_SINGULAR = "peso"
MONEDA_PLURAL = "pesos"

CENTAVOS_SINGULAR = "centavo"
CENTAVOS_PLURAL = "centavos"

MAX_NUMERO = 999999999999

MIL_MILLONES = 1000000000
UN_MILLON = 1000000
MIL = 1000
CIEN = 100
DIEZ = 10
UNO = 1
DOS = 2

UNIDADES = (
    "cero",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
)

DECENAS = (
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciséis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
)

DIEZ_DIEZ = (
    "cero",
    "diez",
    "veinte",
    "treinta",
    "cuarenta",
    "cincuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "noventa",
)

CIENTOS = (
    "_",
    "ciento",
    "doscientos",
    "trescientos",
    "cuatrocientos",
    "quinientos",
    "seiscientos",
    "setecientos",
    "ochocientos",
    "novecientos",
)


def numero_a_letras(numero: int) -> str:
    numero_entero = int(numero)
    if numero_entero > MAX_NUMERO:
        raise OverflowError("Número demasiado alto")
    if numero_entero < 0:
        negativo_letras = numero_a_letras(abs(numero))
        return f"menos {negativo_letras}"
    letras_decimal = ""
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * CIEN))
    if parte_decimal > DIEZ - UNO:
        letras_decimal = f"punto {numero_a_letras(parte_decimal)}"
    elif parte_decimal > 0:
        letras_decimal = f"punto cero {numero_a_letras(parte_decimal)}"
    if numero_entero <= CIEN - UNO:
        resultado = leer_decenas(numero_entero)
    elif numero_entero <= MIL - UNO:
        resultado = leer_centenas(numero_entero)
    elif numero_entero <= UN_MILLON - UNO:
        resultado = leer_miles(numero_entero)
    elif numero_entero <= MIL_MILLONES - UNO:
        resultado = leer_millones(numero_entero)
    else:
        resultado = leer_millardos(numero_entero)
    resultado = resultado.replace("uno mil", "un mil")
    resultado = resultado.strip()
    resultado = resultado.replace(" _ ", " ")
    resultado = resultado.replace("  ", " ")
    if parte_decimal > 0:
        resultado = f"{resultado} {letras_decimal}"
    return resultado


def numero_a_moneda(numero: int) -> str:
    numero_entero = int(numero)
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * CIEN))
    centimos = CENTAVOS_SINGULAR if parte_decimal == 1 else CENTAVOS_PLURAL
    moneda = MONEDA_SINGULAR if numero_entero == 1 else MONEDA_PLURAL
    letras = numero_a_letras(numero_entero)
    letras = letras.replace("uno", "un")
    aux_decimal = numero_a_letras(parte_decimal).replace("uno", "un")
    letras_decimal = f"con {aux_decimal} {centimos}"
    letras = f"{letras} {moneda} {letras_decimal} "
    return letras.strip()


def leer_decenas(numero: int) -> str:
    if numero < DIEZ:
        return UNIDADES[numero]
    decena, unidad = divmod(numero, DIEZ)
    if numero <= DIEZ + DIEZ - UNO:
        resultado = DECENAS[unidad]
    elif DIEZ + DIEZ + UNO <= numero <= DIEZ + DIEZ + DIEZ - UNO:
        resultado = f"veinti{UNIDADES[unidad]}"
    else:
        resultado = DIEZ_DIEZ[decena]
        if unidad > 0:
            resultado = f"{resultado} y {UNIDADES[unidad]}"
    return resultado


def leer_centenas(numero: int) -> str:
    centena, decena = divmod(numero, CIEN)
    if decena == 0 and centena == 1:
        resultado = "cien"
    else:
        resultado = CIENTOS[centena]
        if decena > 0:
            decena_letras = leer_decenas(decena)
            resultado = f"{resultado} {decena_letras}"
    return resultado


def leer_miles(numero: int) -> str:
    millar, centena = divmod(numero, MIL)
    resultado = ""
    if millar == UNO:
        resultado = ""
    if (millar >= DOS) and (millar <= DIEZ - UNO):
        resultado = UNIDADES[millar]
    elif (millar >= DIEZ) and (millar <= CIEN - UNO):
        resultado = leer_decenas(millar)
    elif (millar >= CIEN) and (millar <= MIL - UNO):
        resultado = leer_centenas(millar)
    resultado = f"{resultado} mil"
    if centena > 0:
        centena_letras = leer_centenas(centena)
        resultado = f"{resultado} {centena_letras}"
    return resultado.strip()


def leer_millones(numero: int) -> str:
    millon, millar = divmod(numero, UN_MILLON)
    resultado = ""
    if millon == UNO:
        resultado = " un millon "
    if (millon >= DOS) and (millon <= DIEZ - UNO):
        resultado = UNIDADES[millon]
    elif (millon >= DIEZ) and (millon <= CIEN - UNO):
        resultado = leer_decenas(millon)
    elif (millon >= CIEN) and (millon <= MIL - UNO):
        resultado = leer_centenas(millon)
    if millon > UNO:
        resultado = f"{resultado} millones"
    if (millar > 0) and (millar <= MIL - UNO):
        centena_letras = leer_centenas(millar)
        resultado = f"{resultado} {centena_letras}"
    elif (millar >= MIL) and (millar <= UN_MILLON - UNO):
        miles_letras = leer_miles(millar)
        resultado = f"{resultado} {miles_letras}"
    return resultado


def leer_millardos(numero: int) -> str:
    millardo, millon = divmod(numero, UN_MILLON)
    miles_letras = leer_miles(millardo)
    millones_letras = leer_millones(millon)
    return f"{miles_letras} millones {millones_letras}"
