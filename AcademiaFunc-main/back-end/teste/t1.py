from geral.config import *
from geral.modelo import *
import os
#Linkar O treino com exercicio
#sqlviewer

# Teste Aluno

def run():
    db.create_all()

    t1 = Treino(series='4x10', tipo='perna_inicante')
    t2 = Treino(series='4x10', tipo='bicipes')
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()


    a1 = Aluno(nome='José Augusto', email='joséaugusto@gmail.com',
                ativo=True)
    a2 = Aluno(nome='José Augusto', email='joséaugusto@gmail.com',
                ativo=True)
    a3 = Aluno(nome='José Augusto', email='joséaugusto@gmail.com',
                ativo=True)
    #print(f'Aluno: {jose}\n')
    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.commit()

    print(a1)



    ex = Exercicio(nome='Agachamento No Smith', maquina='Polia Smith', treino=t1)
    ex2 = Exercicio(nome='Afundo Bulgaro', maquina='Livre', treino=t1)
    ex3 = Exercicio(nome='ASTDVASTDVCSAOUDTACV', maquina='Livre', treino=t1)


    db.session.add(ex)
    db.session.add(ex2)
    db.session.add(ex3)
    db.session.commit()
    #print(type(t1))


    t1.alunos.append(a1)
    t2.alunos.append(a1)
    db.session.add(t1)
    db.session.commit()

    print(t1)

    print()
    print ('Retornando Todas os Exercicios de um Treino:')
    for t in t1.exercicios:
        print(f'\t{t}')


