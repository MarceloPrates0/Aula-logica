import os
os.system("clear")

var1= float(input("Insira o primeira valor: "))
var2= float(input("Insira o segundo valor: "))

media= (var1 + var2) / 2
soma= var1 + var2
produto= var1 * var2

print(f"Sua média é: {media}")       
print(f"Sua soma é: {soma}")       
print(f"Seu produto é: {produto}") 

if var1 > var2:
    print(f"{var1} é o maior número")
    print(f"{var2} é o menor número")
elif var1 == var2:
    print("Você inseriu o mesmo número, não possui um maior que o outro.")
else:
    print(f"{var2} é o maior número")
    print(f"{var1} é o menor número") 
