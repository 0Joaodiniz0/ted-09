numeros = []
primeiro = int(input("Digite um número: "))
numeros.append(primeiro)

for i in range(19):
    numeross = int(input("Digite outro número: "))
    numeros.append(numeross)

print(f"Os números na ordem inversa são:")
for num in reversed(numeros):
    print(num)