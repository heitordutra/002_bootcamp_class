#%%
# Divisão
print(6/4)
# %%
# Valor inteiro da divisão
print(6//4)
# %%
# Resto da divisão
print(6%4)
# %%
nome_aluno = "Heitor"
print(type(nome_aluno))

# %%
print(nome_aluno.lower())
# %%
print(nome_aluno.upper())
# %%
# Separando a string em um determinado caractere
email = "nome@email.com"
print(email.split("@"))
# %%
valor_1 = True
valor_2 = True

print(valor_2 and valor_1)

# %%
try:
    data = input("Insira uma data no formato dd/mm/aaaa: ")
    data_formatada = data.split("/")
    for i in range(len(data_formatada)):
        data_formatada[i]=int(data_formatada[i])
    # data_formatada é uma lista
    print(f"Dia: {data_formatada[0]}\nMês: {data_formatada[1]}\nAno:{data_formatada[2]}")
except:
    print("Não foi inserido um número")
# %%
