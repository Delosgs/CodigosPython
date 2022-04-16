# Teste Python fiap elif (Decisoes encadeadas)

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doencaIfectocontagiosa = input("Suspeita de doenca infectocontagiosa? ").upper() # O comando upper converte para letra maiuscula ou minicusla a palavra digitada
if idade >= 65:
    print("o paciente " + nome + " possui atendimento prioritario!")
    
elif doencaIfectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para a sala de espera reservarda.")
    

else:
    print("O paciente " + nome + " nao possui atendimento prioritario e pode aguardar na sala!")
 
    
print("FIM!")