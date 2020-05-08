import csv

#Arquivos de saída
arquivo_q1 = 'base-q1.txt'
arquivo_q2 = 'base-q2.txt'
arquivo_q3 = 'base-q3.txt'
arquivo_q4 = 'base-q4.txt'

with open(arquivo_q1, 'w', encoding='utf-8', newline = '') as csvfile:
    #c = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    c = csv.writer(csvfile, delimiter=';')

with open(arquivo_q2, 'w', encoding='utf-8', newline = '') as csvfile:
    c = csv.writer(csvfile, delimiter=';')

with open(arquivo_q4, 'w', encoding='utf-8', newline = '') as csvfile:
    c = csv.writer(csvfile, delimiter=';')

with open(arquivo_q4, 'w', encoding='utf-8', newline = '') as csvfile:
    c = csv.writer(csvfile, delimiter=';')

#Arquivo de entrada
with open('dados-questionario.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    i = 1
    print('%04d' % i)
    for resposta in leitor:
            resposta_q1 = resposta[0].strip('"\n' + '\n')
            resposta_q2 = resposta[1]
            resposta_q3 = resposta[2]
            resposta_q4 = resposta[3]

            with open(arquivo_q1, 'a', encoding='utf-8', newline = '') as csvfile:
                c = csv.writer(csvfile, delimiter=';')
                #c = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                c.writerow(['**** *n_'+'%04d' % i])
                c.writerow([resposta_q1])
                
            with open(arquivo_q2, 'a', encoding='utf-8', newline = '') as csvfile:
                c = csv.writer(csvfile, delimiter=';')
                #c = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                c.writerow(['**** *n_'+'%04d' % i])
                c.writerow([resposta_q2])

            with open(arquivo_q3, 'a', encoding='utf-8', newline = '') as csvfile:
                c = csv.writer(csvfile, delimiter=';')
                #c = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                c.writerow(['**** *n_'+'%04d' % i])
                c.writerow([resposta_q3])

            with open(arquivo_q4, 'a', encoding='utf-8', newline = '') as csvfile:
                c = csv.writer(csvfile, delimiter=';')
                #c = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                c.writerow(['**** *n_'+'%04d' % i])
                c.writerow([resposta_q4])

            i = i + 1

