
# coding: utf-8

# In[ ]:


# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")





# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")


# In[ ]:


# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))


# In[ ]:


# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.


# In[ ]:


# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])


# In[ ]:


input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for line in data_list[0:20]:
    vinte_line = []
    vinte_line.append(line)
    print(vinte_line)


# In[ ]:


# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]


# In[ ]:


# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for sublist in data_list[0:20]:
    print(sublist[6])


# In[ ]:


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
      Função para obter uma lista com as colunas de uma lista com sublistas.
      Argumentos:
          data: uma lista contendo listas.
          index: índice da sublista.
      Retorna:
          Uma lista com os valores de uma coluna específica de uma sublista.

      """
    column_list = []
    for sublist in data:
        column_list.append(sublist[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------


# In[ ]:




input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
for sublist in data_list:
    if sublist[-2] == "Male":
        male +=1
    elif sublist[-2] == "Female":
        female +=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------


# In[ ]:


input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
      Função para contar as ocorrências na coluna Gender da lista desta questão.
      Argumentos:
          data_list =  a lista com que estamos trabalhando.
      Retorna:
          Uma lista contendo as contagens dos gêneros.

      """
    male = 0
    female = 0
    for sublist in data_list:
        if sublist[-2] == "Male":
            male +=1
        elif sublist[-2] == "Female":
            female +=1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------


# In[ ]:



input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
      Função que seleciona o gênero com mais ocorrências.
      Argumentos:
          data_list: a lista com que estamos trabalhando.
      Retorna:
          Uma string com o gênero mais popular.

      """
    male = 0
    female = 0
    lista_sexo = []
    for sublist in data_list:
        if sublist[-2] == "Male":
            male +=1
        elif sublist[-2] == "Female":
            female +=1
        lista_sexo.append(sublist[-2])
    if lista_sexo.count('Male') > lista_sexo.count("Female"):
        answer = "Masculino"
    elif lista_sexo.count('Male') < lista_sexo.count('Female'):
        answer = "Feminino"
    else:
        answer = 'Igual'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------


# In[ ]:




# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)


# In[ ]:


input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types(data_list[i][-3]). Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
user_type_list = column_to_list(data_list, -3)
types = ['Customer', 'Dependent', 'Subscriber']

## gerando contagem de usuarios
def count_users(data_list):
    customer = 0
    dependent = 0
    subscriber = 0
    for sublist in data_list:
        if sublist[-3] == "Customer":
            customer +=1
        elif sublist[-3] == "Dependent":
            dependent +=1
        else:
            subscriber += 1
    return [customer, dependent, subscriber]

quantity = count_users(data_list)


y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

print(quantity)


# In[ ]:


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Male e female não são os únicos valores da variável gênero."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------


# In[ ]:




input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_dur_list = column_to_list(data_list, 2)
trip_int = list(map(float, trip_dur_list))

# mínimo
def minimo(lst):
    """
      Função que calcula o mínimo valor de uma lista.
      Argumentos:
          lst: Uma lista.
      Retorna:
          Um inteiro correspondente ao valor mínimo da lista.

      """
    minimo = None
    for value in lst:
        if not minimo:
            minimo = value
        elif value < minimo:
            minimo = value
    return minimo
min_trip = minimo(trip_int)

# max
def maximo(lst):
    """
      Função que calcula o máximo valor de uma lista.
      Argumentos:
          lst: Uma lista.
      Retorna:
          Um inteiro correspondente ao valor máximo da lista.

      """
    maximo = None
    for value in lst:
        if not maximo:
            maximo = value
        elif value > maximo:
            maximo = value
    return maximo
max_trip = maximo(trip_int)

# media

mean_trip += sum(trip_int)/len(trip_int)

# mediana
def mediana(lst):
    """
      Função que calcula a mediana de uma lista.
      Argumentos:
          lst: Uma lista.
      Retorna:
          Um inteiro correspondente à mediana da lista.

      """
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
median_trip = mediana(trip_int)



print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------


# In[ ]:




input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_type = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_type))
print(user_type)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_type) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------


# In[ ]:



input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """


# In[ ]:


input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = []
    count_items = []
    for types, counts in column_list:
        item_types.append(types)
        count_items.append(counts)
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------

print(count_items(column_list))

