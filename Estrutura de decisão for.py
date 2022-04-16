# Estrutura de decidão for

tabuada = int(input("Digite um numero para exibir tabuada: "))

for valor in range(1,11,1): # os numeros são: inicio, fim e incremento

    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
    
    
