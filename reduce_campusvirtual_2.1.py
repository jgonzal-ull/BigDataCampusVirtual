#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import collections

# Map básico que ya clasifica las líneas en franjas horarias y procedencia interna y externa de la ULL
def reduce():
    lines = 0
    valores = dict()
    tipos = dict()

    lugar = {"monitorizar": 0,"redirigir": 1, "interno": 2, "externo": 3}
    tipo = {"externo": 0, "Cableada": 1, "Wifi": 2}

    for line in sys.stdin:
        lines += 1
        campos = line.split(";")
        anio = campos[0]
        mes = campos[1]
        dia = campos[2]
        hora = campos[3]
        externo = campos[4]
        tipoorigen =campos[5]
        valor = campos[6]
        clave = anio+mes+dia+hora
        if clave in valores:
            valores[clave][lugar[externo]] += int(valor)
            tipos[clave][tipo[tipoorigen]] += int(valor)
        else:
            valores[clave]=[0,0,0,0]
            tipos[clave]=[0,0,0]
            valores[clave][lugar[externo]] += int(valor)
            tipos[clave][tipo[tipoorigen]] += int(valor)
    print("Anio;Mes;Dia;Hora;Monitorizar;Redirigir;Interno;Externo;Externo;Cableada;Wifi")
    itemssalida = collections.OrderedDict(sorted(valores.items()))
    for indice in itemssalida:
        print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10}".format(anio, indice[4:6], indice[6:8], indice[8:10], valores[indice][0], valores[indice][1], valores[indice][2], valores[indice][3],tipos[indice][0], tipos[indice][1], tipos[indice][2]))
    return lines


def main():
    val = reduce()
    if str(val).isdigit():
        print('Reduce procesadas ' + str(val) + ' líneas', file=sys.stderr)
    else:
        print('Error: brake:  ' + val , file=sys.stderr)
    return 0

if __name__ == '__main__':
    main()

