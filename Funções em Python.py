#!/usr/bin/env python
# coding: utf-8

# # Funções em Python
# 
# Funções são uma espécie de "subprograma". Elas são como pequenos pedacinhos de programa que podem ser chamadas pelo nome. Para criar uma função usamos o comando "def" e o nome da função. Elas são um bloco de comando assim como if/elif/else, while e for.

# In[3]:


def hello():
    print("Olá, mundo!")
    
'''
Quando uma função é chamada pelo nome, o fluxo do programa é interrompido. 
Em seguida, a função inteira é executada, e ao final dela, o programa volta a ser executado do mesmo ponto que parou.
'''

hello()

# Saída: Olá, mundo!


# In[7]:


'''
É possível passarmos informações para uma função.
Chamamos essas informações de "parâmetros" ou "argumentos. Na definição da função, daremos nome a esses parâmetros.
Dentro da função, eles serão tratados como se fossem variáveis.
'''

def ola(nome):
    print("Olá", nome)
    
ola("Verusca")
# Saída: Olá, Verusca

aluno = "Delano"
ola(aluno)
# Saída: Olá, Delano

# A função pode receber vários parâmetros separados por vírgula.

def dadosPessoais(nome, idade, cidade):
    print("Seu nome é {}, você tem {} anos e mora em {}.".format(nome, idade, cidade))

dadosPessoais("Delano", 36, "Salvador")

# Passando paramentros fora da ordem, temos que dizer quais parametros esta sendo passado

dadosPessoais(idade=33, cidade="Salvador", nome="Verusca")


# # Funções com resposta
# Uma função pode ter uma "resposta". Por exemplo, nossa função pode ser uma conta, e o resultado da conta pode ser útil em nosso programa. Dizemos que essas funções "retornam" um valor. Utilizamos a palavra "return" para fazer uma função retornar sua resposta. Quando uma função retorna um valor, ela pode ser usada em expressões matemáticas ou lógicas, ter seu valor atribuído a uma variável, etc.

# In[10]:


def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

numeros = [1, 2, 3, 4, 5, 6]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")


# # Funções recursivas
# Algumas funções são chamadas funções recursivas. A recursividade (ou recursão) é uma propriedade na qual uma função faz referência a si mesma. Quando a função encontra uma nova referência, ela irá pausar sua execução atual e iniciar a execução da nova instância, para só então retomar sua execução.
# 
# Assim como nos loops, é necessário ter alguma condição para que as chamadas recursivas sejam interrompidas, evitando que executem para sempre.

# In[11]:


def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)

print("Testando a função recursiva:")
funcaoRecursiva(10)


# ## Agrupando parâmetros
# Podemos utilizar o operador * - que, neste caso, não será uma multiplicação. Ao colocarmos o * ao lado do nome de um parâmetro na definição da função, estamos dizendo que aquele argumento será uma coleção. Mais especificamente, uma tupla. Porém, o usuário não irá passar uma tupla. Ele irá passar quantos argumentos ele quiser, e o Python automaticamente criará uma tupla com eles:

# In[18]:


def piscina(*infos):
    vol = infos[0]*infos[1]*infos[2]*infos[3]
    return vol

volume = piscina(5, 4, 5, 3)

print('O volume é: ', volume)


# Podemos utilizar o operador * na chamada da função também. Na definição, o operador * indica que devemos agrupar itens avulsos em uma coleção. Na chamada, ele indica que uma coleção deve ser expandida em itens avulsos:

# In[19]:


def piscina(prof, largura, comprimento):
    vol = prof*largura*comprimento
    return vol

lista = [5, 4, 5]

volume = piscina(*lista)

print('O volume é: ', volume)


# ## Parâmetros opcionais
# Outra possibilidade são funções com parâmetros opcionais. Note que isso é diferente de termos quantidade variável de parâmetros. No caso da quantidade variável, normalmente são diversos parâmetros com a mesma utilidade (números a serem somados, valores a serem exibidos etc), enquanto os parâmetros opcionais são informações distintas que podem ou não ser passadas para a função.
# 
# Para criar parâmetros opcionais, usaremos **, e os parâmetros passados serão agrupados em um dicionário: o nome do parâmetro será uma chave, e o valor será... O valor.

# In[20]:


def piscina(prof, **infos):
    vol = prof*infos['largura']*infos['comprimento']
    return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume é: ', volume)


# Analogamente ao caso dos parâmetros múltiplos, é possível que o usuário da função já tenha os dados organizados em um dicionário. Neste caso, basta usar ** na chamada da função para expandir o dicionário em vários parâmetros opcionais:

# In[21]:


def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol

infos = {'largura': 10, 'comprimento': 20}

volume = piscina(5, **infos)

print('O volume é: ', volume)


# In[ ]:




