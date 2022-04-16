# Listas simples

inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: ")) # append significa acresentar em portugues
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper() # O comando upper converte para letra maiuscula ou minicusla a palavra digitada
   
for elemento in inventario:
    print(elemento)
   