from random import choice
import sys
import time

print('''
##############################################
#    #     #  ###### #      #    #   ##      #
#    #     #  #      #      #    #  #  #     #
#     #   #   ####   #      ###### ######    #
#      # #    #      #      #    # #    #    #
#       #     ###### ###### #    # #    #    #
#                                            #
#                 VERSÃO 1.0c                #
#          BY: Leandro de Oliveira           #   
#           Developed in: PyCharm            # 
#                 PYTHON 3.6                 # 
##############################################
''')

print(''' 
CARA:  VOCÊ É O JOGADOR "X"
COROA: VOCÊ É O JOGADOR "O"
BOA SORTE!''')

print("JOGANDO A MOEDA!")
for i in range(5,0,-1):
    sys.stdout.write(str('.')+' ')
    sys.stdout.flush()
    time.sleep(1)

d = ['CARA', 'COROA']
e = choice(d)

if e == 'CARA':
        f = 'X'
else:
        f = 'O'
        
print(f'\nO resultado foi "{e}", você é o jogador "{f}"!')

j = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('''
###############################################
# A tabela do jogo é representada por campos, #
# escolha o campo que pretende preencher.     #
###############################################
      ''')

m = """###############################################            
       #             Campos      Posições            #
       #           0 | 1 | 2    {} | {} | {}            #
       #          ---+---+---  ---+---+---           #      
       #           3 | 4 | 5    {} | {} | {}            #
       #          ---+---+---  ---+---+---           #  
       #           6 | 7 | 8    {} | {} | {}            #
       ###############################################""".format(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8])
ar = [line.strip() for line in m.split('\n')]
for line in ar:
        print(line.strip())

# As variaveis a seguir é de critério de comparação mais a frente

c = 1
a = '11'
b = '12'

while c <= 10:

        if ((j.count('X') == 4 and j.count('O') == 5) or\
            (j.count('X') == 5 and j.count('O') == 4)):
                print('EMPATE!')
                break

        if ((j[0] == j[1] == j[2] == 'X') or\
            (j[2] == j[5] == j[8] == 'X') or\
            (j[6] == j[7] == j[8] == 'X') or\
            (j[0] == j[3] == j[6] == 'X') or\
            (j[0] == j[4] == j[8] == 'X') or\
            (j[2] == j[4] == j[6] == 'X') or\
            (j[1] == j[4] == j[7] == 'X') or\
            (j[3] == j[4] == j[5] == 'X')):
                print('Jogador "X" é o vencedor!')
                break

        if ((j[0] == j[1]  == j[2] == 'O') or\
            (j[2] == j[5]  == j[8] == 'O') or\
            (j[6] == j[7]  == j[8] == 'O') or\
            (j[0] == j[3]  == j[6] == 'O') or\
            (j[2] == j[4]  == j[6] == 'O') or\
            (j[1] == j[4]  == j[7] == 'O') or\
            (j[3] == j[4]  == j[5] == 'O') or\
            (j[0] == j[4]  == j[8] == 'O')):
                print('Jogador "O" é o vencedor!')
                break

        if c % 2 == 1:

                a = input('Jogador "X", onde pretende fazer a jogada? ')
                q = 1

                while q == 1:

                        if a.isnumeric()and int(a) <= 8 and j[int(a)] == ' ':	
                                a = int(a)
                                break
                        else:
                                if a.isnumeric() and int(a) <= 8 and j[int(a)] != ' ':
                                        a = input('Jogador "X" esse campo já foi preenchido, por favor escolha outro: ')
                                else:
                                        a = input('Jogador "X", digite um caractere numérico entre 0 e 8: ')

                j[a] = 'X'

        else:

                b = input('Jogador "O", onde pretende fazer a jogada? ')
                w = 1

                while w == 1:

                        if b.isnumeric() and int(b) <= 8 and j[int(b)] == ' ':	
                                b = int(b)
                                break
                        else:
                                if b.isnumeric() and int(b) <= 8 and j[int(b)] != ' ':
                                        b = input('Jogador "O" esse campo já foi preenchido, por favor escolha outro: ')
                                else:
                                        b = input('Jogador "O", digite um caractere numérico entre 0 e 8: ')

                j[b] = 'O'

        m = """###############################################         
               #             Campos      Posições            #
               #           0 | 1 | 2    {} | {} | {}            #
               #          ---+---+---  ---+---+---           #    
               #           3 | 4 | 5    {} | {} | {}            #
               #          ---+---+---  ---+---+---           # 
               #           6 | 7 | 8    {} | {} | {}            #
               ###############################################""".format(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8])
        
        arr = [line.strip() for line in m.split('\n')]
        for line in arr:
                print(line.strip())

        c += 1
