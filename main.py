#! usr/bin/Python3
import os
import module_control

def menu_fluit():
    print("""
=================================================================================
Bem Vindo
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 ( 1 ) - Login 
 ( 2 ) - Criar Novo Login
 ( 3 ) - Sair

""")

while(True):
    menu_fluit()
    opt = str(input("///> " ))
    if opt == "1":
        os.system('clear')
    elif opt == "2":
        os.system('clear')
    elif opt == "3":
        pass
