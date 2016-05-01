#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import argparse
import sys

#pepe 234578910111213
# pepote  asdfasdffasddddd rttt

def check_params():
    parser = argparse.ArgumentParser(description='Process bank files \
            and report stadistical information.')
    parser.add_argument('year', metavar='N', type=int, nargs='*',
                        help='Four digits for the year of log file')
    params = parser.parse_args()
    return params.year[0]


# Map básico que ya clasifica las líneas en franjas horarias y procedencia interna y externa de la ULL
def map(year):
    lines = 0
    error = 0
    meses = {"Dec": "12", "Nov": "11", "Oct": "10", "Sep": "09", "Aug": "08"}
    dias = {" 1": "01", " 2": "02", " 3": "03", " 4": "04", " 5": "05", " 6": "06", " 7": "07", " 8": "08",
            " 9": "09", "10": "10", "11": "11", "12": "12", "13": "13", "14": "14",
            "15": "15", "16": "16", "17": "17", "18": "18", "19": "19", "20": "20", "21": "21", "22": "22", "23": "23",
            "24": "24", "25": "25", "26": "26", "27": "27", "28": "28", "29": "29", "30": "30", "31": "31"}
    horas = {"00": "00", "01": "01", "02": "02", "03": "03", "04": "04", "05": "05", "06": "06", "07": "07", "08": "08",
             "09": "09", "10": "10", "11": "11", "12": "12", "13": "13", "14": "14",
             "15": "15", "16": "16", "17": "17", "18": "18", "19": "19", "20": "20", "21": "21", "22": "22", "23": "23"}
    tipo = {"10.151": "Wifi", "10.254": "Wifi", "10.54": "Cableada", "10.253": "Wifi", "10.21": "Cableada", "10.20": "Cableada", "10.22": "Cableada",
            "10.177": "Wifi", "10.250": "Wifi","10.152": "Wifi","10.249": "Wifi","10.153": "Wifi","10.248": "Wifi",
            "10.154": "Wifi", "10.247": "Wifi","10.155": "Wifi","10.246": "Wifi","10.156": "Wifi","10.245": "Wifi",
            "10.158": "Wifi", "10.244": "Wifi","10.159": "Wifi","10.243": "Wifi","10.160": "Wifi","10.242": "Wifi",
            "10.161": "Wifi", "10.241": "Wifi","10.162": "Wifi","10.252": "Wifi","10.163": "Wifi","10.240": "Wifi",
            "10.164": "Wifi", "10.239": "Wifi","10.165": "Wifi","10.238": "Wifi","10.166": "Wifi","10.237": "Wifi",
            "10.167": "Wifi", "10.236": "Wifi","10.168": "Wifi","10.235": "Wifi","10.169": "Wifi","10.251": "Wifi",
            "10.170": "Wifi", "10.234": "Wifi","10.171": "Wifi","10.233": "Wifi","10.172": "Wifi","10.232": "Wifi",
            "10.173": "Wifi", "10.231": "Wifi","10.174": "Wifi","10.230": "Wifi","10.175": "Wifi","10.229": "Wifi",
            "10.176": "Wifi", "10.228": "Wifi","10.179": "Wifi","10.181": "Wifi","10.178": "Wifi",
            "10.101": "Cableada", "10.201": "Cableada","10.102": "Cableada","10.202": "Cableada","10.103": "Cableada","10.203": "Cableada",
            "10.104": "Cableada", "10.204": "Cableada","10.105": "Cableada","10.205": "Cableada","10.106": "Cableada","10.206": "Cableada",
            "10.108": "Cableada", "10.208": "Cableada","10.109": "Cableada","10.209": "Cableada","10.110": "Cableada","10.210": "Cableada",
            "10.111": "Cableada", "10.211": "Cableada","10.112": "Cableada","10.212": "Cableada","10.113": "Cableada","10.213": "Cableada",
            "10.114": "Cableada", "10.214": "Cableada","10.115": "Cableada","10.215": "Cableada","10.116": "Cableada","10.216": "Cableada",
            "10.117": "Cableada", "10.217": "Cableada","10.118": "Cableada","10.218": "Cableada","10.119": "Cableada","10.219": "Cableada",
            "10.120": "Cableada", "10.220": "Cableada","10.121": "Cableada","10.221": "Cableada","10.122": "Cableada","10.222": "Cableada",
            "10.123": "Cableada", "10.223": "Cableada","10.124": "Cableada","10.224": "Cableada","10.125": "Cableada","10.225": "Cableada",
            "10.126": "Cableada", "10.226": "Cableada","10.127": "Cableada","10.227": "Cableada",
            "10.107": "Cableada"}

    for line in sys.stdin:
        lines += 1
        mes = meses.get(line[0:3], "Error")
        dia = dias.get(line[4:6], "Error")
        hora = horas.get(line[7:9], "Error")
        externo = "externo"
        tipoconex = "externo"
        if mes == "Error":
            error += 1
            return ("Error mes" + line)
        if dia == "Error":
            error += 1
            return ("Error dia " + line)
        if hora == "Error":
            error += 1
            return ("Error hora " + line)
        campos = line.split(" ")
        ip = campos[5].split(".")
        if ip[0][0:6] == "apache":
            ip = campos[6].split(".")

        if (ip[0] == "systemon5"):
            externo = "monitorizar"
            tipoconex = "Cableada"
        elif (ip[0] == "::1"):
            externo = "redirigir"
            tipoconex = "Cableada"
        elif  (ip[0] == "www" and ip[1] == "campusvirtual"):
            externo = "redirigir"
            tipoconex = "Cableada"
        elif  (ip[0] == "ocw" and ip[1] == "ull"):
            externo = "redirigir"
            tipoconex = "Cableada"
        elif (ip[2] == "staticip"):
            externo = "redirigir"
            tipoconex = "Cableada"
        else:
            if not ip[0].isdigit():
                print(campos)
                return ("Error ip1 no es dígito <"+ ip[0] + "> " + line)
            ip1 = int(ip[0])
            if not ip[1].isdigit():
                return ("Error ip2 no es dígito" + line)
            ip2 = int(ip[1])
            if not ip[2].isdigit():
                return ("Error ip3 no es dígito" + line)
            ip3 = int(ip[2])
            if not ip[3].isdigit():
                return ("Error ip4 no es dígito" + line)
            if ip1 == 10:
                externo = "interno"
                clave = ip[0] + '.' + ip[1]
                tipoconex = tipo.get(clave, "Error")
                if tipoconex == 'Error':
                    return ("Error ip conexión" + ip[0] + '.' + ip[1] + ' ' + line)
            if ip1 == 172 and ip2 >= 16 and ip2 <= 31:
                externo = "error"
                return ("Error ip " + campos[5] + 'xxx' + line)
            if ip1 == 192 and ip2 == 168:
                externo = "error"
                return ("Error ip " + campos[5] + 'xxx' + line)
            if ip1 == 193 and ip2 == 145 and ip3 >= 96 and ip3 <= 125:
                externo = "interno"
                tipoconex = "Cableada"
        print("{0};{1};{2};{3};{4};{5};1".format(year, mes, dia, hora, externo, tipoconex))
    return lines


def main():
    val = map(check_params())
    if str(val).isdigit():
        print('Map procesadas ' + str(val) + ' líneas', file=sys.stderr)
    else:
        print('Error: brake:  ' + val, file=sys.stderr)
    return 0


if __name__ == '__main__':
    main()
