#!/usr/bin/env python
# coding: utf-8

# # Dicionários
# 
# Um dicionário é uma coleção, assim como as listas e as tuplas. Porém, enquanto as tuplas eram indexadas por um índice, os dicionários são indexados por chaves. Todo elemento em um dicionário possui uma chave e um valor. Chaves tipicamente são strings, valores podem ser qualquer tipo de dado.

# In[2]:


# O dicionário é definido pelos símbolos { e }

dicionario = {}

# O dicionário não possui um "append" = Acresentar.
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))

'''
Saída:
{'cat': 'gato', 'dog': 'cachorro', 'mouse': 'rato'}
<class 'dict'>
'''

# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}


# In[3]:


# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)
# Saída: {'Curso': 'Python Pro', 'Linguagem': 'Python', 'Módulo': 2}


# In[15]:


# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' and 'dog' in dicionario:
    print('cat e dog existe!') # Sim
    
if 'dog' in dicionario:
    print('dog existe!') # Sim
    
if 'gato' in dicionario:
    print('gato existe!') # Não
    
if 'cat' or 'dog' in dicionario:
    print('Existe um dos dois!') # Sim
    
if 'bird' in dicionario:
    print('bird existe!') # Não


# In[18]:


'''
Também podemos utilizar as funções .keys() e .values() para obter listas
com apenas as chaves ou apenas os valores do dicionário.
'''
chaves = dicionario.keys()
print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
print(valores)
# Saída:dict_values(['gato', 'cão', 'rato'])

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário

itens = dicionario.items()
print(itens)
# Saída:dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])


# # Percorrendo coleções
# O for é um tipo especial de loop feito para percorrer elementos de uma coleção. Acima vimos exemplos usando um while e um contador para percorrer uma lista. O for elimina a necessidade de inicializarmos um contador, incrementarmos e verificar a condição de parada. Sintaxe: O for se repete uma vez para cada elemento da lista. A cada repetição, a variável temporária assume o valor de um elemento da lista, na ordem da lista.

# In[19]:


fib = [1, 1, 2, 3, 5, 8, 13]
for elemento in fib:
    print(elemento)


# In[20]:


# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será 1.

for numero in range(10):
    print(numero)
    # este exemplo imprime os números de 0 a 9, de um em um


# In[23]:


# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.

for numero in range(1,11):
    print(numero)
    # este exemplo imprime os números de 1 a 10, de um em um


# In[24]:


# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1,20,2):
    print(numero)
    # este exemplo imprime os ímpares positivos menores do que 20
    # ele começa valendo 1 e salta de 2 em 2 até atingir ou passar 20


# In[27]:


# O incremento pode ser também um decremento (incremento negativo).
for numero in range (10,0,-1):
    print(numero)
    #Imprimindo os números de 1 a 10 em ordem decrescente


# In[ ]:




