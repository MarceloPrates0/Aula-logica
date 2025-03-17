import os
import time
os.system ("cls || clear")

numero = (int(input("Insira um número: ")))

for i in range(numero, 0, -1):
    print(f"Sua contagem regressiva em: {i}")
    time.sleep(1)



