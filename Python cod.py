#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, Word!")


# In[8]:


x=5 # uma variável do tipo inteiro (int)
print(x)


# In[3]:


print(type(x))


# In[4]:


preco = 19.99 # uma variável do tipo real (float)
print(preco, type(preco))


# In[5]:


cidade = "Salvador"
print(cidade, type(cidade))


# In[6]:


disponivel = True
print(disponivel)


# In[7]:


disponivel = False
print(disponivel, type(disponivel))


# In[9]:


escola = "Let's Code" # uma variável literal (string)
print(escola)


# In[12]:


# Podemos fazer operações aritméticas simples
a = 2 + 3  # Soma
b = 2 - 3  # Subtração
c = 2 * 3  # Multiplicação
d = 3 / 3  # Divisão
e = 2 // 3 # Divisão inteira ignora a parte decimal
f = 2 ** 3 # Potência
g = 2 % 3  # Resto de divisão

print (a, b, c, d, e, f, g)


# In[13]:


#Podemos fazer operações com variáveis não inteiras

nome = input('Digite seu primeiro nome:')
nome = nome + ' Silva'
print(nome)


# In[15]:


comparacao_1 = 5 > 3
print(comparacao_1)
comparacao_2 = 5 < 3
print(comparacao_2)


# In[30]:


tem_cafe = True
tem_pao = False

print(not tem_cafe)
print(tem_cafe or tem_pao)
print(tem_cafe and tem_pao)


# In[32]:


# Operador AND

comparacao1 = 5 > 3 and 6 > 3
comparacao2 = 5 < 3 and 6 > 3

print(comparacao1)
print(comparacao2)


# In[33]:


# Operador OR
comparacao1 = 5 > 3 or 6 > 3
comparacao2 = 5 < 3 or 6 > 3

print(comparacao1)
print(comparacao2)


# In[34]:


# Pegando informação digitada pelo usuario
# Tudo que é lido por input() é considerado uma string (str)

idade = input("Informe a sua idade: ")
print(idade, type(idade))


# In[35]:


# Fazendo o cast
idade = int(idade)
print(idade, type(idade))


# In[36]:


print(float('123.25'))
print(str(123.25))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-2))


# In[37]:


# Podemos ler valores do teclado com a função input().
# Ela permite que a gente passe uma mensagem para o usuário.
nome = input('Digite o seu nome: ')
# Para tratar como outros tipos de dados é necessário realizar a conversão:
peso = float(input('Digite o seu peso: ')) # lê o peso como número real
idade = int(input('Digite a sua idade: ')) # lê a idade como número inteiro

print(nome, 'pesa', peso, 'kg e tem', idade, 'anos de idade.')


# In[38]:


salario_mensal = input('Digite o valor do seu salário mensal')
salario_mensal = float(salario_mensal)

gasto_mensal = input('Digite seu gasto mensal')
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print('O montante que você pode economizar ao fim do ano é de', montante_economizado)

