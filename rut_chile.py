#!/usr/bin/env python
#_*_ coding: utf8 _*_

#------------------------------------------------------------
# ----            GENERADOR DE DÍGITOS RUT CHILENOS     ----|
# ----            Gohanckz                              ----|
# ----            Contact : gohanckz@gmail.cl           ----|
# ----            Version : 1.0                         ----|
#------------------------------------------------------------

#Rango de ruts sin guion
start = 18717901
end = 18717902

rut_list = []

for n in range(start,end+1):
    rut_list.append(n)


def main():
    for i in rut_list:
        rut = str(i)
        dig_1 = int(rut[0])*3
        dig_2 = int(rut[1])*2
        dig_3 = int(rut[2])*7
        dig_4 = int(rut[3])*6
        dig_5 = int(rut[4])*5
        dig_6 = int(rut[5])*4
        dig_7 = int(rut[6])*3
        dig_8 = int(rut[7])*2
        suma = dig_1+dig_2+dig_3+dig_4+dig_5+dig_6+dig_7+dig_8
        digito = str((suma%11)-11)
        if digito == "-11":
            digito = "-0"
        elif digito == "-10":
            digito = "-k"

        print(rut+digito)

if __name__ == "__main__":
    main()
