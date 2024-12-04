#OBJETIVOS DO PROJETO:
# 1- Média de Notas por Aluno
# 2- Melhor Aluno em Cada Matéria
# 3- Média de Notas da Turma por Matéria

#FUNÇÃO PARA CALCULAR A MEDIA DE TODOS OS ALUNOS EM TODAS AS MATERIAS JUNTAS
def media_por_aluno(alunos):
    for aluno in alunos:
        media_nota = (aluno["matematica"] + aluno["portugues"] + aluno["ciencias"])/3
        media_nota = round(media_nota, 1)
        #USANDO O ROUND PARA LIMITAR A UMA CASA DECIMAL O RESULTADO
        print('A media de', aluno['nome'],'é',media_nota)

#FUNÇÃO PARA CALCULAR A MEDIA DA TURMA NA MATERIA MATEMATICA
def media_turma_mat(alunos):
        total_mat = sum(aluno['matematica'] for aluno in alunos)
        #PERCORRENDO A LISTA DENTRO DA VARIAVEL PARA QUE A LINGUAGEM ME MOSTRE APENAS UM RESULTADO AO EM VEZ DA SOMA DE TODOS OS ALUNOS
        numero_de_alunos = len(alunos)
        #USANDO O LEN PARA SABER O TAMANHO DA LISTA E QUANTIDADE DE ALUNOS
        media_turma = total_mat / numero_de_alunos
        return media_turma

#FUNÇÃO PARA CALCULAR A MEDIA DA TURMA NA MATERIA PORTUGUES
def media_turma_port(alunos):
        total_port = sum(aluno['portugues'] for aluno in alunos)
        numero_de_alunos = len(alunos)
        media_turma = total_port / numero_de_alunos
        return media_turma

#FUNÇÃO PARA CALCULAR A MEDIA DA TURMA NA MATERIA CIENCIAS
def media_turma_cien(alunos):
        total_cien = sum(aluno['ciencias'] for aluno in alunos)
        numero_de_alunos = len(alunos)
        media_turma = round(total_cien / numero_de_alunos,1)
        return media_turma

#LISTA DE ALUNOS E NOTAS CRIADAS POR IA
alunos = [
    {"nome": "Alice", "matematica": 85.0, "portugues": 78.0, "ciencias": 92.0},
    {"nome": "Bob", "matematica": 79.0, "portugues": 83.0, "ciencias": 88.0},
    {"nome": "Carlos", "matematica": 92.0, "portugues": 89.0, "ciencias": 95.0},
    {"nome": "Diana", "matematica": 70.0, "portugues": 85.0, "ciencias": 80.0},
    {"nome": "Eva", "matematica": 88.0, "portugues": 92.0, "ciencias": 91.0},
    {"nome": "Felipe", "matematica": 76.0, "portugues": 74.0, "ciencias": 85.0},
    {"nome": "Gustavo", "matematica": 90.0, "portugues": 81.0, "ciencias": 87.0},
    {"nome": "Hanna", "matematica": 82.0, "portugues": 79.0, "ciencias": 90.0},
    {"nome": "Irene", "matematica": 95.0, "portugues": 94.0, "ciencias": 96.0},
    {"nome": "João", "matematica": 67.0, "portugues": 72.0, "ciencias": 70.0},
    {"nome": "Karen", "matematica": 89.0, "portugues": 88.0, "ciencias": 92.0},
    {"nome": "Luis", "matematica": 74.0, "portugues": 73.0, "ciencias": 75.0},
    {"nome": "Mariana", "matematica": 80.0, "portugues": 77.0, "ciencias": 82.0},
    {"nome": "Nina", "matematica": 91.0, "portugues": 89.0, "ciencias": 98.0},
    {"nome": "Otávio", "matematica": 65.0, "portugues": 70.0, "ciencias": 68.0},
    {"nome": "Paula", "matematica": 78.0, "portugues": 75.0, "ciencias": 80.0},
    {"nome": "Quintino", "matematica": 83.0, "portugues": 86.0, "ciencias": 85.0},
    {"nome": "Roberta", "matematica": 93.0, "portugues": 91.0, "ciencias": 90.0},
    {"nome": "Sergio", "matematica": 77.0, "portugues": 78.0, "ciencias": 79.0},
    {"nome": "Teresa", "matematica": 68.0, "portugues": 72.0, "ciencias": 70.0}
]

#IMPRIMINDO A MEDIA TOTAL DA TURMA
print(media_por_aluno(alunos),'\n')

#USANDO O KEY=LAMBDA PARA PODER ACESSAR APENAS AS MATERIAS ESPECIFICAS PARA CADA CALCULO
melhor_aluno_mate = max(alunos, key=lambda aluno: aluno["matematica"])
melhor_aluno_port = max(alunos, key=lambda aluno: aluno['portugues'])
melhor_aluno_cien = max(alunos, key=lambda aluno: aluno['ciencias'])
#USANDO O MAX PARA EXTRAIR O MAIOR VALOR EM CADA MATERIA

#IMPRIMINDO O RESULTADO, MELHOR ALUNO POR MATERIA
print(f'Esse é o melhor aluno em matematica: {melhor_aluno_mate['nome']}')
print(f'Esse é o melhor aluno em portugues: {melhor_aluno_port['nome']}')
print(f'Esse é o melhor aluno em ciencias: {melhor_aluno_cien['nome']}','\n')

#IMPRIMINDO A MEDIA DA TURMA EM CADA MATERIA
print(f'A media da turma em matematica é: {media_turma_mat(alunos)}')
print(f'A media da turma em portugues é: {media_turma_port(alunos)}')
print(f'A media da turma em ciencias é: {media_turma_cien(alunos)}')
