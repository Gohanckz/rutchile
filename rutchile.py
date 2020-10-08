#!/usr/bin/env python3
#_*_ coding: utf8 _*_

#------------------------------------------------------------
# ----            GENERADOR DE DÍGITOS RUT CHILENOS     ----|
# ----            Gohanckz                              ----|
# ----            Contact : gohanckz@gmail.cl           ----|
# ----            Version : 2.0                         ----|
#------------------------------------------------------------

try:
    import argparse
    import sys
except ImportError as err:
    print("some libraries are missing")
    print(err)

parser = argparse.ArgumentParser(description="RUT CHILE")
parser.add_argument('-l','--list',action='store_true',help="List RUTS without verificador digit.")
parser.add_argument('-d','--digit',action='store_true',help="generate RUT with verificator digit.")
parser.add_argument('-o','--output',help="indicate output list.")
parser = parser.parse_args()


def main():
    rut_list = []
    if parser.list:
        try:
            start = input("start from : ")
            end = input("to : ")

            while len(start) < 8 or len(start) > 8:
                print("The length of the value is wrong. it must be eight digits.")
                print("example: 12345678")
                start = input("start from : ")



            while len(end) > 8 or len(end) < 8:
                print("The length of the value is wrong. it must be eight digits.")
                print("example: 12345678")
                end = input("to : ")

            while int(end) < int(start):
                print("the second value must be greater than the first value.")
                end = input("to : ")
            
            if parser.output:
                path = parser.output
                with open(path,'w') as f: 
                    sys.stdout = f  
                    for n in range(int(start),int(end)+1):         
                        print(n)      
            else:
                for n in range(int(start),int(end)+1):
                    print(n)
                                    
        except:
            print("select a option.")
            print("type \"python rutchile.py -h\" for more information.")
    

    elif parser.digit:
        try:
            start = input("start from : ")
            end = input("to : ")

            while len(start) < 8 or len(start) > 8:
                print("The length of the value is wrong. it must be eight digits.")
                print("example: 12345678")
                start = input("start from : ")



            while len(end) > 8 or len(end) < 8:
                print("The length of the value is wrong. it must be eight digits.")
                print("example: 12345678")
                end = input("to : ")

            while int(end) < int(start):
                print("the second value must be greater than the first value.")
                end = input("to : ")

            for n in range(int(start),int(end)+1):
                 rut_list.append(n)

            if parser.output:
                path = parser.output            
                with open(path,'w') as f:
                    sys.stdout = f
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
            else:
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
        except:
            print("select a option.")
            print("type \"python rutchile.py -h\" for more information.")
    else:
        print("select a option.")
        print("type \"python rutchile.py -h\" for more information.")

if __name__ == "__main__":
    main()
