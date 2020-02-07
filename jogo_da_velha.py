from random import choice
import sys
import time
import json

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

print(''' CARA:  VOCÊ É O JOGADOR "X"\nCOROA: VOCÊ É O JOGADOR "O"\nBOA SORTE!''')

print("JOGANDO A MOEDA!")
for i in range(5,0,-1):
    sys.stdout.write(str('.')+' ')
    sys.stdout.flush()
    time.sleep(1)

d = [('CARA', 'X'), ('COROA', 'O')]
e = choice(d)
print(f'\nO resultado foi "{e[0]}", você é o jogador "{e[1]}"!')

j = [' ']*9

print('''
###############################################\n# A tabela do jogo é representada por campos, #
# escolha o campo que pretende preencher.     #\n###############################################
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

# As variaveis a seguir são de critério de comparação mais a frente
c = 1
a = '11' # maior que o número de jogadas possiveis no caso é 9 (dimensão do tabuleiro)
b = '12' # diferente e maior que 'a'

def jogada(jog):
	pos = input(f'Jogador "{jog}", onde pretende fazer a jogada? ')
	q = 1
	while q == 1:
		if pos.isnumeric()and int(pos) <= 8 and j[int(pos)] == ' ':	
			pos = int(pos)
			break
		else:
			if pos.isnumeric() and int(pos) <= 8 and j[int(pos)] != ' ':
				pos = input(f'Jogador "{jog}" esse campo já foi preenchido, por favor escolha outro: ')
			else:
				pos = input(f'Jogador "{jog}", digite um caractere numérico entre 0 e 8: ')
	j[pos] = jog
	


while c <= 10:

	if ((j.count('X') == 4 and j.count('O') == 5) or\
		(j.count('X') == 5 and j.count('O') == 4)):
			print('EMPATE!')
			break 
	
	if c % 2 == 1:
		jogador = 'X'
	else:
		jogador = 'O'

	jogada(jogador)

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

	if ((j[0] == j[1] == j[2] == jogador) or\
		(j[2] == j[5] == j[8] == jogador) or\
		(j[6] == j[7] == j[8] == jogador) or\
		(j[0] == j[3] == j[6] == jogador) or\
		(j[0] == j[4] == j[8] == jogador) or\
		(j[2] == j[4] == j[6] == jogador) or\
		(j[1] == j[4] == j[7] == jogador) or\
		(j[3] == j[4] == j[5] == jogador)):
		print(f'Jogador "{jogador}" é o vencedor!')
		break

	c = c + 1
