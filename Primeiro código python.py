# Teste com Python Fiap

nome = input("Digite um funcionario: ")
empresa = input("Digite o nome da empresa: ")
qtdeFuncionarios = int(input("Digite a quantidade de funcionarios:"))
mediaMensalidade = float(input("Digite a media da mensalidade: "))


print(nome + " trabalha na empresa " + empresa)   # Aqui é uma concatenação de String com String
print("Possui: ", qtdeFuncionarios, " funcionarios.") # Aqui é uma concatenação de String com numero
print("A media da mensalidade é de: " + str(mediaMensalidade))


 # Type é uma função que diz o nome da variavel usada
print("----------Verifique os tipos de dados abaixo:------------")
print("O tipo de dado da variavel [nome] é: ", type(nome))  
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtdeFuncionarios] é: ", type(qtdeFuncionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))