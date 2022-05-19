import pandas as pd
import psycopg2 as pg2
from utilitary_functions import present_schools 
from sql_functions import *

# Definição de dados iniciais
schools = {1: 'Escola de Dados',
           2: 'Escola de Programacao',
           3: 'Escola de Mobile',
           4: 'Escola de Front-end',
           5: 'Escola de DevOps',
           6: 'Escola de UI/UX',
           7: 'Escola de Inovacao e Gestao'
}

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

def menu_presentation(database):
    while True:
        print("*" * 10)
        print("Olá! Seja bem-vindo(a) ", end = "")
        print("*" * 10)

        print("Escolha uma opção: ")
        print("""[1] Adicionar registro
        [2] Mostrar os dados
        [3] Sair do programa""")

        choice = input("Digite a sua opção: ")

        if choice == '1':
            name = input("Digite o nome: ")
            school = int(input("Digite o n° da Escola: "))
            present_schools(schools = schools)
            email = input("Digite o e-mail @alura")

            insert_db(f"""INSERT INTO {str(database)}(nome, escola, email) VALUES ('{str(name)}, {str(school)}, {str(email)}');""")


        elif choice == '2':
            sql = f"""SELECT * FROM {str(database)}"""
            print(query_db(sql))

        elif choice == '3':
            break

        else:
            print("Opção inválida. Tente novamente")
            print("*" * 20)

    print("Programa finalizado.")


# Cria o banco de dados da escola semente    
sql = """DROP TABLE IF EXISTS escola_semente;
        CREATE TABLE escola_semente
            (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                escola INTEGER NOT NULL,
                email VARCHAR(40) NOT NULL
            )"""

create_db(sql)

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
