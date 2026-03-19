
#for i in range(1, 30):
 #   resultado = chr(9608) * i
   # print(f"{resultado}")
print("Carregando o sistema, aguarde")

from time import sleep
import os
i = 1
print("\033[?25l")
while i <= 40:
    print(chr(9608) * i + " " + str(i))
    i += 1
    sleep(0.2)
    os.system("cls")