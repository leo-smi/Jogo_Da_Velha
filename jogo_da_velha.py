from random import choice
import sys, time, json

print('''CARA: VOCÊ É O JOGADOR "X"\nCOROA: VOCÊ É O JOGADOR "O"\nBOA SORTE!\n''')
print("JOGANDO A MOEDA!")
for i in range(2, 0, -1):
    sys.stdout.write(str('.') + '  ')
    sys.stdout.flush()
    time.sleep(1)
d = [('CARA', 'X'), ('COROA', 'O')]
e = choice(d)
print(f'\n\nO resultado foi "{e[0]}", você é o jogador "{e[1]}"!\n')

T = [' '] * 9 # T de tabuleiro

print(
    '''+---------------------------------------------+\n| A tabela do jogo é representada por campos, |
| escolha o campo que pretende preencher.     |\n+---------------------------------------------+''')

def tabela():
    m = """\n +---------------------------------------------+           
		|             Campos      Posições            |
		|           0 | 1 | 2    {} | {} | {}            |
		|          ---+---+---  ---+---+---           |      
		|           3 | 4 | 5    {} | {} | {}            |
		|          ---+---+---  ---+---+---           |  
		|           6 | 7 | 8    {} | {} | {}            |
		+---------------------------------------------+"""\
     .format(T[0], T[1], T[2], T[3], T[4], T[5], T[6], T[7], T[8])
    ar = [line.strip() for line in m.split('\n')]
    for line in ar:
        print(line.strip())

tabela()

def jogada(jogador):
    pos = input(f'Jogador "{jogador}", onde pretende fazer a jogada? ')
    while 1:
        if pos.isnumeric() and int(pos) <= 8 and T[int(pos)] == ' ':
            pos = int(pos)
            break
        else:
            if pos.isnumeric() and int(pos) <= 8 and T[int(pos)] != ' ':
                pos = input(f'Jogador "{jogador}" esse campo já foi preenchido, por favor escolha outro: ')
            else:
                pos = input( f'Jogador "{jogador}", digite um caractere numérico entre 0 e 8: ')
    T[pos] = jogador

def situacao(t, jogador): # t de vetor
    if ((t[0] == t[1] == t[2] == jogador) or\
		(t[2] == t[5] == t[8] == jogador) or\
		(t[6] == t[7] == t[8] == jogador) or\
		(t[0] == t[3] == t[6] == jogador) or\
		(t[0] == t[4] == t[8] == jogador) or\
		(t[2] == t[4] == t[6] == jogador) or\
		(t[1] == t[4] == t[7] == jogador) or\
		(t[3] == t[4] == t[5] == jogador)):
        print(f'Jogador "{jogador}" é o vencedor!')
        return 'temos um vencedor'
		
c = 1

while c <= 10:

    XO = 'X' if c % 2 == 1 else 'O'

    jogada(XO)

    tabela()

    if situacao(T, XO) == 'temos um vencedor':
        break

    if c == 9:
        print("EMPATE!")
        break

    c = c + 1
