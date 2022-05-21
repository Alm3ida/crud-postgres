import pandas as pd
import psycopg2 as pg2
from time import sleep
from utilitary_functions import present_schools 
from sql_functions import *

# Definição de dados iniciais das Escolas
schools = {1: 'Escola de Dados',
           2: 'Escola de Programacao',
           3: 'Escola de Mobile',
           4: 'Escola de Front-end',
           5: 'Escola de DevOps',
           6: 'Escola de UI/UX',
           7: 'Escola de Inovacao e Gestao'
}

# Definição do squad raízes como base de dados primária
root_squad = {"Nome": ['Marcus Almeida', 
                       'Iasmin', 
                       'Jhoysnaira', 
                       'Andre Louis', 
                       'Emerson Laranja'],
              "Escola": [1, 2, 3, 3, 2],
              "Email": ['marcus@email', 
                        'iasmin@email', 
                        'jhoys@email', 
                        'andre@email', 
                        'emerson@email']
}

df = pd.DataFrame(root_squad, columns=['Nome', 'Escola', 'Email'])


def menu_presentation(database):

    print("=" * 10, end = "")
    print(" Olá! Seja bem-vindo(a) ", end = "")
    print("=" * 10)

    while True:
        print("=-" * 20)
        print("Escolha uma opção: ")
        print("[1] Adicionar registro")
        print("[2] Mostrar os dados")
        print("[3] Atualizar registro")
        print("[4] Deletar registro")
        print("[5] Sair do programa")

        choice = input("Digite a sua opção: ")
        print("="* 15, end = "")
        print(f" Banco: {database} ", end="")
        print("="* 15)

        # Adiciona um registro ao banco de dados.
        if choice == '1':

            # Armazena todos os parâmetros requeridos
            name = input("Digite o nome: ")
            present_schools(schools = schools)
            school = int(input("Digite o n° da Escola: "))
            email = input("Digite o e-mail @alura: ")

            # Formata o texto SQL e adiciona ao banco
            sql = f"""INSERT INTO {str(database)}(nome, escola, email) VALUES ('{str(name)}', {str(school)}, '{str(email)}');"""
            insert_db(sql)

        # Mostra todos os registros do banco de dados.
        elif choice == '2':
            sql = f"""SELECT * FROM {str(database)}"""
            reg = query_db(sql)
            for item in reg:
                print(item)
            print(f"\nAo todo, foram localizados {len(reg)} registros.")


        # Atualiza um registro no banco de dados.
        elif choice == '3':
            id = int(input("Digite o indice do item a ser alterado: "))

            name = input("Digite o nome: ")
            present_schools(schools = schools)
            school = int(input("Digite o n° da Escola: "))
            email = input("Digite o e-mail @alura: ")
            sql = f"""UPDATE {str(database)} SET nome = '{name}', escola = {school}, email = '{email}' WHERE id = {str(id)}"""

            update_db(sql)

        # Remove um registro no banco de dados.
        elif choice == '4':
            id = int(input("Digite o indice do item a ser removido: "))
            sql = f"""DELETE FROM {str(database)} WHERE id = {str(id)}"""
            remove_db(sql)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente")
            print("*" * 20)

    print("=-" * 20)
    print("\nPrograma finalizado.")


database = "escola_semente"

# Cria o banco de dados da escola semente    
sql = f"""DROP TABLE IF EXISTS {database};
        CREATE TABLE {database}
            (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                escola INTEGER NOT NULL,
                email VARCHAR(40) NOT NULL
            )"""

create_db(sql)

for i in range(df.shape[0]):
    insert_db(f"""INSERT INTO {database}(nome, escola, email) VALUES (\'{df.loc[i, 'Nome']}\', \'{df.loc[i, 'Escola']}\', \'{df.loc[i, 'Email']}\')""")

menu_presentation(database)


# print(df.shape)
# print(df.iloc[0]['Nome'])

# reg = query_db('SELECT * FROM escola_semente')
# print(reg)


# Dataframe utilizado para a inserção da primeira base de dados;
#df = pd.DataFrame(root_squad, columns=['Nome', 'Escola', 'Email'])

## Formato mais parecido com JSON
# root_squad = {'Marcus Almeida': [1, 'marcus@email'], 
#               'Iasmin': [2, 'iasmin@email'], 
#               'Jhoisnayra': [3, 'jhoys@email'],
#               'Andre Louis': [3, 'andre@email'],
#               'Emerson Laranja': [2, 'emerson@email']
#               }


# # Cria o banco de dados com o nome das escolas
# sql = """DROP TABLE IF EXISTS alura_content;
#           CREATE TABLE alura_content(
#               id SERIAL PRIMARY KEY,
#               nome VARCHAR(255) NOT NULL)
# """
# create_db(sql)

# Define uma base de dados com o nome das Escolas


# for school in schools.items():
#     insert_db(f"""INSERT INTO alura_content(nome) VALUES ('{str(school[1])}');""")

# sql = """SELECT * FROM alura_content"""
# reg = query_db(sql)
# print(reg)
# present_schools(schools)
