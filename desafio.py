import random
import os
# FUNÇÃO PARA ENCONTRAR O NUMERO MINIMO DE DIAS
def acharMinimoDeDias(n):
    lista_filmes = []
    while (n != []):
        soma = 0
        lista_auxiliar = []
        for i in n:
            soma += i
            if (soma <= 3.00):
                lista_auxiliar.append(i)
            if (soma > 3.00):
                soma -= i
        [n.remove(i) for i in lista_auxiliar]
        lista_filmes.append(lista_auxiliar)
    return lista_filmes
# FUNÇÃO PRINCIPAL
def main():
    condicaoDeParada = 'N'
    while (condicaoDeParada.upper() == 'N'):
        os.system('clear') or None
        random.seed()
        validacao = False
        validacao2 = False
        opcao = int(input('\nInforme como quer gerar os dados para a aplicação\n\n1 - Para gerar os dados aleatórios\n\n2 - Para inserir os dados manualmente\n\n'))
        while (validacao == False):
            if opcao == 1:
                validacao = True
                while (validacao2 == False):
                    quantidade = int(input('Informe o número de filmes que a lista vai possuir:\n\n Restrição: Quantidade entre [1,1000]\n\n'))
                    if (1 <= quantidade <= 1000):
                        validacao2 = True
                        n = [round(random.uniform(1.01, 3.0) ,2) for i in range(quantidade)]
                        print('Lista Gerada aleatoriamente: {}\n\n'.format(n))
                        lista_filmes = acharMinimoDeDias(n)
                        print('Será preciso {} dias no mínimo para poder assistir os filmes gastando 3 horas por dia\n\n'.format(len(lista_filmes)))
                        print([i for i in lista_filmes])
                    else:
                        print('Fora do intervalo de restrição!\n\n Digite um valor valido!\n\n')
            elif opcao == 2:
                validacao = True
                while (validacao2 == False):
                    quantidade = int(input('Informe o número de filmes que a lista vai possuir:\n\n Restrição: Quantidade entre [1,1000]\n\n'))
                    if (1 <= quantidade <= 1000):
                        validacao2 = True
                        n = []
                        print('Restrição: Duração dos filmes entre [1.01 e 3.0]) \n\n')
                        for i in range(quantidade):
                            validacao3 = False
                            while (validacao3 == False):
                                duracao = round(float(input(f'Digite a {i+1}ª duração:\n\n')), 2)
                                if 1.01 <= duracao <= 3.0:
                                    validacao3 = True
                                else:
                                    print('Fora do intervalo de restrição!\n Digite um valor valido!\n\n')
                            n.append(duracao)
                        lista_filmes = acharMinimoDeDias(n)
                        print('Será preciso {} dias no mínimo para poder assistir os filmes gastando 3 horas por dia\n\n'.format(len(lista_filmes)))
                        print([i for i in lista_filmes])
                    else:
                        print('Fora do intervalo de restrição!\n Digite um valor valido!\n\n')
            elif (opcao != 1) or (opcao != 2):
                opcao = int(input('Opcão invalida! Digite uma opcao valida!\n\n'))
        condicaoDeParada = str(input('Deseja sair da aplicação? (S ou N)\n\n'))
        
if __name__ == '__main__':
    main()