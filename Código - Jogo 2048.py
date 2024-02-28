#/*******************************************************************************
#Autor: João Ruan Araujo de Jesus Silva
#Componente Curricular: Mi algoritmos
#Concluido em: 08/10/2023
#Linguagem de progamação: Python 3.11.5
#Sistema operacional usado na criação do código: Windows 11
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

import random
#Criação das variáveis que serão usadas no loop principal jogo.
direcao = ''
final = ''
score = 0
jogadas = 0
scorerecord = 0
jogadasrecord = 0
jogar = 1
certo = 0

#funções do programa.
def conta_jogadas(conta):
        global jogadas
        jogadas +=1
        return jogadas


def acumula_score(soma):
        global score
        score += soma
        return score


def numero_aleatorio(matriz):
        preencheu = '' 
        lista = []
        for coluna in range(0,4):
                for linha in range(0,4):
                        if matriz [coluna] [linha] == 0:
                                lista.append((coluna,linha))
                                preencheu = 'sim' 


        if preencheu == 'sim':                  
                localaleatorio = random.choice(lista)
                numeroaleatorio = random.randrange(2,5,2)
                coluna , linha = localaleatorio
                matriz [coluna] [linha] = numeroaleatorio

        return matriz


def verifica_venceu(matriz):
        venceu = ''
        for coluna in range(0,4):
                for linha in range(0,4):
                         if matriz [coluna] [linha] == 2048:
                                venceu = 'fim de jogo'
                                
        return venceu


def verifica_perdeu(matriz):
        zeros = 0
        perdeu = ''
        semmovimento = 0
        for coluna in range(0,4):
                for linha in range(0,4):
                        if matriz [coluna] [linha] != 0: 
                                zeros += 1
                                if zeros == 16:
                                        for horizontalnumero in range(0,4):
                                                if matriz [horizontalnumero] [0] != matriz [horizontalnumero] [1]:
                                                        semmovimento +=1
                                                if matriz [horizontalnumero] [1] != matriz [horizontalnumero] [2]:
                                                        semmovimento +=1
                                                if matriz [horizontalnumero] [2] != matriz [horizontalnumero] [3]:
                                                        semmovimento +=1

                                        for verticalnumero in range(0,4):
                                                if matriz [0] [verticalnumero] != matriz [1] [verticalnumero]:
                                                        semmovimento +=1
                                                if matriz [1] [verticalnumero] != matriz [2] [verticalnumero]:
                                                        semmovimento +=1
                                                if matriz [2] [verticalnumero] != matriz [3] [verticalnumero]:
                                                        semmovimento +=1
                                        
                                                if semmovimento == 24:
                                                        perdeu = 'fim de jogo' 
                                                                                 
        return perdeu


def soma_movimento(soma):
#Soma e movimento para a ESQUERDA
        if direcao == 'a':

                for horizontalnumero in range(0,4):
                        for horizontalnumero in range(0,4):
                                if matriz [horizontalnumero] [0] == 0:
                                        matriz [horizontalnumero] [0] = matriz [horizontalnumero] [1]
                                        matriz [horizontalnumero] [1] = 0
                                if matriz [horizontalnumero] [1] == 0:
                                        matriz [horizontalnumero] [1] = matriz [horizontalnumero] [2]
                                        matriz [horizontalnumero] [2] = 0
                                if matriz [horizontalnumero] [2] == 0:
                                        matriz [horizontalnumero] [2] = matriz [horizontalnumero] [3]
                                        matriz [horizontalnumero] [3] = 0



                for horizontalnumero in range(0,4):
                        if matriz [horizontalnumero] [0] == matriz [horizontalnumero] [1]:
                                soma = matriz [horizontalnumero] [0] + matriz [horizontalnumero] [1]
                                matriz [horizontalnumero] [0] = soma
                                matriz [horizontalnumero] [1] = 0
                                acumula_score(soma)

                                
                        if matriz [horizontalnumero] [1] == matriz [horizontalnumero] [2]:
                                soma = matriz [horizontalnumero] [1] + matriz [horizontalnumero] [2]
                                matriz [horizontalnumero] [1] = soma
                                matriz [horizontalnumero] [2] = 0
                                acumula_score(soma)

                        if matriz [horizontalnumero] [2] == matriz [horizontalnumero] [3]:
                                soma = matriz [horizontalnumero] [2] + matriz [horizontalnumero] [3]
                                matriz [horizontalnumero] [2] = soma
                                matriz [horizontalnumero] [3] = 0
                                acumula_score(soma)


                        if matriz [horizontalnumero] [1] == 0 and matriz [horizontalnumero] [2] == 0:
                                if matriz [horizontalnumero] [0] == matriz [horizontalnumero] [3] and matriz [horizontalnumero] [0] != 0:
                                                soma = matriz [horizontalnumero] [0] +  matriz [horizontalnumero] [3]
                                                matriz [horizontalnumero] [0] = soma
                                                matriz [horizontalnumero] [3] = 0
                                                acumula_score(soma)

                       
                        if matriz [horizontalnumero] [0] == 0:
                                matriz [horizontalnumero] [0] = matriz [horizontalnumero] [1]
                                matriz [horizontalnumero] [1] = 0
                        if matriz [horizontalnumero] [1] == 0:
                                matriz [horizontalnumero] [1] = matriz [horizontalnumero] [2]
                                matriz [horizontalnumero] [2] = 0
                        if matriz [horizontalnumero] [2] == 0:
                                matriz [horizontalnumero] [2] = matriz [horizontalnumero] [3]
                                matriz [horizontalnumero] [3] = 0

                if matriz != velhamatriz:
                        numero_aleatorio(matriz)
                        conta_jogadas(matriz)


#Soma e movimento para a DIREITA
        if direcao == 'd':

                for horizontalnumero in range(0,4):
                        for horizontalnumero in range(0,4):
                                if matriz [horizontalnumero] [3] == 0:
                                        matriz [horizontalnumero] [3] = matriz [horizontalnumero] [2]
                                        matriz [horizontalnumero] [2] = 0
                                if matriz [horizontalnumero] [2] == 0:
                                        matriz [horizontalnumero] [2] = matriz [horizontalnumero] [1]
                                        matriz [horizontalnumero] [1] = 0
                                if matriz [horizontalnumero] [1] == 0:
                                        matriz [horizontalnumero] [1] = matriz [horizontalnumero] [0]
                                        matriz [horizontalnumero] [0] = 0

                
                for horizontalnumero in range(0,4):

                        if matriz [horizontalnumero] [3] == matriz [horizontalnumero] [2]:
                                soma = matriz [horizontalnumero] [3] + matriz [horizontalnumero] [2]
                                matriz [horizontalnumero] [3] = soma
                                matriz [horizontalnumero] [2] = 0
                                acumula_score(soma)

                                
                        if matriz [horizontalnumero] [2] == matriz [horizontalnumero] [1]:
                                soma = matriz [horizontalnumero] [2] + matriz [horizontalnumero] [1]
                                matriz [horizontalnumero] [2] = soma
                                matriz [horizontalnumero] [1] = 0
                                acumula_score(soma)

                        if matriz [horizontalnumero] [1] == matriz [horizontalnumero] [0]:
                                soma = matriz [horizontalnumero] [1] + matriz [horizontalnumero] [0]
                                matriz [horizontalnumero] [1] = soma
                                matriz [horizontalnumero] [0] = 0
                                acumula_score(soma)


                        if matriz [horizontalnumero] [1] == 0 and matriz [horizontalnumero] [2] == 0:
                                if matriz [horizontalnumero] [0] == matriz [horizontalnumero] [3] and matriz [horizontalnumero] [0] != 0:
                                                soma = matriz [horizontalnumero] [0] +  matriz [horizontalnumero] [3]
                                                matriz [horizontalnumero] [0] = soma
                                                matriz [horizontalnumero] [3] = 0
                                                acumula_score(soma)

                        
                        if matriz [horizontalnumero] [3] == 0:
                                matriz [horizontalnumero] [3] = matriz [horizontalnumero] [2]
                                matriz [horizontalnumero] [2] = 0
                        if matriz [horizontalnumero] [2] == 0:
                                matriz [horizontalnumero] [2] = matriz [horizontalnumero] [1]
                                matriz [horizontalnumero] [1] = 0
                        if matriz [horizontalnumero] [1] == 0:
                                matriz [horizontalnumero] [1] = matriz [horizontalnumero] [0]
                                matriz [horizontalnumero] [0] = 0


                if matriz != velhamatriz:
                        numero_aleatorio(matriz)
                        conta_jogadas(matriz)

#Soma e movimento para CIMA
        if direcao == 'w':

                for verticalnumero in range(0,4):
                        for verticalnumero in range(0,4):
                                if matriz [0] [verticalnumero] == 0:
                                        matriz [0] [verticalnumero] = matriz [1] [verticalnumero]
                                        matriz [1] [verticalnumero] = 0
                                if matriz [1] [verticalnumero]== 0:
                                        matriz [1] [verticalnumero] = matriz [2] [verticalnumero]
                                        matriz [2] [verticalnumero] = 0
                                if matriz [2] [verticalnumero] == 0:
                                        matriz [2] [verticalnumero] = matriz [3] [verticalnumero]
                                        matriz [3] [verticalnumero] = 0

                for  verticalnumero in range(0,4):
                        if matriz [1] [verticalnumero] == 0 and matriz [2] [verticalnumero] == 0:
                                if matriz [0] [verticalnumero] == matriz [3] [verticalnumero] and matriz [0] [verticalnumero] != 0:
                                                soma = matriz [0] [verticalnumero] + matriz [3] [verticalnumero]
                                                matriz [0] [verticalnumero] = soma
                                                matriz [3] [verticalnumero] = 0
                                                acumula_score(soma)

                        if matriz [0] [verticalnumero] == matriz [1] [verticalnumero]:
                                soma = matriz [0] [verticalnumero] + matriz [1] [verticalnumero]
                                matriz [0] [verticalnumero] = soma
                                matriz [1] [verticalnumero] = 0
                                acumula_score(soma)

                                
                        if matriz [1] [verticalnumero] == matriz [2] [verticalnumero]:
                                soma = matriz [1] [verticalnumero] + matriz [2] [verticalnumero]
                                matriz [1] [verticalnumero] = soma
                                matriz [2] [verticalnumero] = 0
                                acumula_score(soma)

                        if matriz [2] [verticalnumero] == matriz [3] [verticalnumero]:
                                soma = matriz [2] [verticalnumero] + matriz [3] [verticalnumero]
                                matriz [2] [verticalnumero] = soma
                                matriz [3] [verticalnumero] = 0
                                acumula_score(soma)


                        if matriz [0] [verticalnumero] == 0:
                                matriz [0] [verticalnumero] = matriz [1] [verticalnumero]
                                matriz [1] [verticalnumero] = 0
                        if matriz [1] [verticalnumero]== 0:
                                matriz [1] [verticalnumero] = matriz [2] [verticalnumero]
                                matriz [2] [verticalnumero] = 0
                        if matriz [2] [verticalnumero] == 0:
                                matriz [2] [verticalnumero] = matriz [3] [verticalnumero]
                                matriz [3] [verticalnumero] = 0

                                        
                if matriz != velhamatriz:
                        numero_aleatorio(matriz)
                        conta_jogadas(matriz)

#Soma e movimento para BAIXO
        if direcao == 's':

                for verticalnumero in range(0,4):
                        for verticalnumero in range(0,4):
                                if matriz [3] [verticalnumero] == 0:
                                        matriz [3] [verticalnumero] = matriz [2] [verticalnumero]
                                        matriz [2] [verticalnumero] = 0
                                if matriz [2] [verticalnumero] == 0:
                                        matriz [2] [verticalnumero] = matriz [1] [verticalnumero]
                                        matriz [1] [verticalnumero] = 0
                                if matriz [1] [verticalnumero] == 0:
                                        matriz [1] [verticalnumero] = matriz [0] [verticalnumero]
                                        matriz [0] [verticalnumero] = 0

                for verticalnumero in range(0,4):

                        if matriz [1] [verticalnumero] == 0 and matriz [2] [verticalnumero] == 0:
                                if matriz [0] [verticalnumero] == matriz [3] [verticalnumero] and matriz [0] [verticalnumero] != 0:
                                                soma = matriz [0] [verticalnumero] +  matriz [3] [verticalnumero]
                                                matriz [3] [verticalnumero] = soma
                                                matriz [0] [verticalnumero] = 0
                                                acumula_score(soma)

                        if matriz [3] [verticalnumero] == matriz [2] [verticalnumero]:
                                soma = matriz [3] [verticalnumero] + matriz [2] [verticalnumero]
                                matriz [3] [verticalnumero] = soma
                                matriz [2] [verticalnumero] = 0
                                acumula_score(soma)

                                
                        if matriz [2] [verticalnumero] == matriz [1] [verticalnumero]:
                                soma = matriz [2] [verticalnumero] + matriz [1] [verticalnumero]
                                matriz [2] [verticalnumero] = soma
                                matriz [1] [verticalnumero] = 0
                                acumula_score(soma)

                        if matriz [1] [verticalnumero] == matriz [0] [verticalnumero]:
                                soma = matriz [1] [verticalnumero] + matriz [0] [verticalnumero]
                                matriz [1] [verticalnumero] = soma
                                matriz [0] [verticalnumero] = 0
                                acumula_score(soma)

                        
                        if matriz [3] [verticalnumero] == 0:
                                matriz [3] [verticalnumero] = matriz [2] [verticalnumero]
                                matriz [2] [verticalnumero] = 0
                        if matriz [2] [verticalnumero] == 0:
                                matriz [2] [verticalnumero] = matriz [1] [verticalnumero]
                                matriz [1] [verticalnumero] = 0
                        if matriz [1] [verticalnumero] == 0:
                                matriz [1] [verticalnumero] = matriz [0] [verticalnumero]
                                matriz [0] [verticalnumero] = 0


                if matriz != velhamatriz:
                        numero_aleatorio(matriz)
                        conta_jogadas(matriz)

#Matriz principal.
matriz = [
        [ 0 , 0 , 0 , 0],
        [ 0 , 0 , 0 , 0],
        [ 0 , 0 , 0 , 0],
        [ 0 , 0 , 0 , 0],
         ]

numero_aleatorio(matriz)
numero_aleatorio(matriz)
#A velhamatriz é uma matriz de comparação, essa matriz é usada para verificar se houve mudança na matriz principal, quando o usuário fez o movimento. 
velhamatriz = [
        [ 0 , 0 , 0 , 0],
        [ 0 , 0 , 0 , 0],
        [ 0 , 0 , 0 , 0],
        [ 0 , 0 , 0 , 0],
         ]

for coluna in range(0,4):
        for linha in range(0,4):
                matriz[coluna] [linha] = str(matriz[coluna] [linha])
                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '0', ' ')
                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '1 24', '1024')
                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '2 48', '2048')
                print(f'|{matriz[coluna] [linha]:^5}|', end ='' ) 
                matriz[coluna] [linha] = matriz[coluna] [linha].replace( ' ', '0')
                matriz[coluna] [linha] = int(matriz[coluna] [linha])         
        print()

#Aqui começa o loop principal do funcionamento do jogo.
while jogar == 1:
                while final != 'fim de jogo':
                        direcao = (input('Movimento para esquerda [A]\nMovimento para direita [D]\nMovimento para cima [W]\nMovimento para baixo [S]\nSelecione seu comando: '))
                        direcao = direcao.lower()      
                        if direcao == 'a' or direcao == 'd' or direcao =='w' or direcao == 's':
                                #Aqui a velha matriz recebe os mesmos parâmetros da matriz, para assim verificar se houve mudança na matriz depois do comando de direção. Caso houver dita mudança, e assim um movimento válido, a função numero_aleatorio() é ativada.
                                for coluna in range(0,4):
                                        for linha in range(0,4):
                                                velhamatriz [coluna] [linha]= matriz [coluna] [linha]

                                #Chamada da função de soma e movimento.
                                soma_movimento(matriz)
                                #Chamada das funções que verificam se o usuário venceu ou perdeu.
                                final = verifica_venceu(matriz)
                                if verifica_venceu(matriz) != 'fim de jogo':
                                        final = verifica_perdeu(matriz)

                                for coluna in range(0,4):
                                        for linha in range(0,4):
                                                           
                                                matriz[coluna] [linha] = str(matriz[coluna] [linha])
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '0', ' ')
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '1 24', '1024')
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '2 48', '2048')
                                                print(f'|{matriz[coluna] [linha]:^5}|', end ='' )
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( ' ', '0')
                                                matriz[coluna] [linha] = int(matriz[coluna] [linha])
                                        print()

                                #O Score atual é mostrado em tempo real, a cada jogada.
                                print('--' * 14)
                                print(f'Contagem de Score: {score}')
                                print('--' * 14)

                        #Tratamento de erro.
                        else:
                                print('\nCARACTER INVÁLIDO!')
                                for coluna in range(0,4):
                                        for linha in range(0,4):
                                                matriz[coluna] [linha] = str(matriz[coluna] [linha])
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '0', ' ')
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '1 24', '1024')
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( '2 48', '2048')
                                                print(f'|{matriz[coluna] [linha]:^5}|', end ='' )
                                                matriz[coluna] [linha] = matriz[coluna] [linha].replace( ' ', '0')
                                                matriz[coluna] [linha] = int(matriz[coluna] [linha])
                                        print()
                
                if verifica_venceu(matriz) == 'fim de jogo':
                        print('Você venceu! Meus parabéns!')
                if verifica_venceu(matriz) != 'fim de jogo':
                        if verifica_perdeu(matriz) == 'fim de jogo':
                                print('Você perdeu! Não existem mais jogadas possíveis')

                #Aqui é mostrado a relação do score feito pelo usuário, com o score record.
                if score > scorerecord:
                        scorerecord = score
                        jogadasrecord = jogadas
                        print(f'Score final: {scorerecord} \nQuantidade de movimentos: {jogadas} \nNovo Recorde! Seu Score atual é o melhor!')
                if scorerecord > score:
                        print(f'Score final: {score} \nQuantidade de movimentos: {jogadas} \nScore Recorde: {scorerecord} \nQuantidade de movimentos: {jogadasrecord}') 

                if score == scorerecord:
                        if jogadas < jogadasrecord:
                                print(f'Score final: {scorerecord} \nQuantidade de movimentos: {jogadas} \nNovo Recorde! Seu score atual é o melhor!')
                        if jogadasrecord < jogadas: 
                                print(f'Score final: {score} \nQuantidade de movimentos: {jogadas} \nScore Recorde: {scorerecord} \nQuantidade de movimentos: {jogadasrecord} \nO Score declarado como recorde, utilizou menos movimentos para fazer o seu Score final.') 
                #A variável 'certo' verifica se foi escolhido o comando correto no input de 'jogar'.
                certo = 0
                while certo != 1:
                        print('--' * 14)
                        jogar = input("Deseja jogar novamente?\nDigite [1]: Sim\nDigite [2]: Não\n")
                        jogar.isdigit()
                        if jogar.isdigit():
                                jogar = int(jogar)
                                if jogar == 1:
                                        #Aqui os parâmetros se atualizam para iniciar um novo jogo. 
                                        certo = 1
                                        final = ''
                                        score = 0
                                        jogadas = 0
                                        print('--' * 14)
                                        print('Novo jogo:')
                                        print('--' * 14)
                                        matriz = [
                                                [ 0 , 0 , 0 , 0],
                                                [ 0 , 0 , 0 , 0],
                                                [ 0 , 0 , 0 , 0],
                                                [ 0 , 0 , 0 , 0],
                                                ]
                                        numero_aleatorio(matriz)                               
                                        numero_aleatorio(matriz)
                                        velhamatriz = [
                                                [ 0 , 0 , 0 , 0],
                                                [ 0 , 0 , 0 , 0],
                                                [ 0 , 0 , 0 , 0],
                                                [ 0 , 0 , 0 , 0],
                                                ]

                                        for coluna in range(0,4):
                                                for linha in range(0,4):
                                                        matriz[coluna] [linha] = str(matriz[coluna] [linha])
                                                        matriz[coluna] [linha] = matriz[coluna] [linha].replace( '0', ' ')
                                                        matriz[coluna] [linha] = matriz[coluna] [linha].replace( '1 24', '1024')
                                                        matriz[coluna] [linha] = matriz[coluna] [linha].replace( '2 48', '2048')
                                                        print(f'|{matriz[coluna] [linha]:^5}|', end ='' ) 
                                                        matriz[coluna] [linha] = matriz[coluna] [linha].replace( ' ', '0')
                                                        matriz[coluna] [linha] = int(matriz[coluna] [linha])         
                                                print()
                                if jogar == 2:
                                        certo = 1

                                if jogar != 1 and jogar != 2:
                                        print('CARACTER INVÁLIDO!')
                                        
                        else:
                                print('\nCARACTER INVÁLIDO!')
print('Obrigado por jogar!')

                
                


        

       



  