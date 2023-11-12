import csv
import random

def generate_csv(filename, num_records):
    # Abrir o arquivo CSV em modo de escrita
    with open(filename, 'w', newline='') as csvfile:
        # Definir os nomes das colunas
        fieldnames = ['gênero', 'idade', 'peso', 'altura','meta', 'restricao','classificação']

        # Inicializar o escritor CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escrever o cabeçalho no arquivo CSV
        writer.writeheader()

        # Gêneros com 90% masculino e 10% feminino
        gender_choices = ['masculino'] * 3 + ['feminino']
        meta_choices = ['hipertrofia'] + ['emagrecimento']
        # Gerar registros no loop
        for _ in range(num_records):
            genero = random.choice(gender_choices)
            idade = random.randint(18, 40)
            peso = random.randint(65, 110)
            altura = round(random.uniform(1.5, 2.0), 2)
            meta = random.choice(meta_choices)
            classificacao = 'intensivo'

            # Escrever o registro no arquivo CSV
            writer.writerow({
                'gênero': genero,
                'idade': idade,
                'peso': peso,
                'altura': altura,
                'meta': meta,
                'restricao': "nenhuma",
                'classificação': classificacao
            })

    print(f'{num_records} registros foram gerados e salvos no arquivo {filename}')

# Número de registros a serem gerados
num_records = 1000000

# Nome do arquivo CSV
filename = 'base_dados.csv'

# Chamar o método para gerar o arquivo CSV
generate_csv(filename, num_records)