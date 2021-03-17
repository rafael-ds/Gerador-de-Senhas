import string
import csv
from time import sleep
from random import choice

letra = string.ascii_letters
numeros = string.digits
caracteres = '_@$&'

concat = letra + numeros + caracteres
temp = []
cast = []


class Dados:
    def __init__(self, inst):
        self.__inst = inst

    def inst(self):
        return f'{self.__inst}'


def senha_auto():
    """
    Função geradora de senha
    :return:
    """

    with open('gerador.csv', 'a', encoding='utf-8', newline='') as gerar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(gerar, fieldnames=cabecalho)
        if gerar.tell() == 0:  # Verifica se existe algo escrito na primeira linha
            escrever.writeheader()

        while True:
            entrada = input('Digite o nome da instituição ou (1) Para sair: - ').title()

            dado = Dados(entrada)
            if entrada != '1':
                # Randomização dos elementos
                cont = 0
                while cont < 12:
                    randomizar = choice(concat)
                    temp.append(randomizar)
                    cont += 1

                soldar = ''.join(temp)  # Concatenando as strings da lista temp
                print('Gerando senha...')
                sleep(0.8)
                print(f'Senha para {entrada} gerada com sucesso! ')
                escrever.writerow({'Instituição': dado.inst(), 'Senha': soldar})
                del temp[:]  # Limpando a lista para qua não haja concatecação na gravação
            else:
                break


def senha_manual():
    with open('gerador.csv', 'a', encoding='utf-8', newline='') as grava:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(grava, fieldnames=cabecalho)
        if grava.tell() == 0:
            escrever.writeheader()

        while True:
            opcao = input('Infomer o nome da  instituição ou (1) para sair: ').title()

            if opcao == '1':
                break
            else:
                senha = input('Informer a senha: ')
                escrever.writerow({'Instituição': opcao, 'Senha': senha})


def ver_senhas():
    """
    Função que mosta as intituições e senhas
    :return:
    """
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        for linhas in ler:
            print(linhas)


def buscar():
    """
    Função que abre o arquivo e retorna um busca do usuario.
    Caso a busca seja False, o mesmo podera adicionar-lo a lista.
    :return:
    """
    with open('gerador.csv', 'r', encoding='utf-8', newline='') as abrir:
        ler = csv.DictReader(abrir)
        buscar = input('Digite o nome da instituição: \n').title()
        item = list(filter(lambda x: x['Instituição'] == buscar, ler))

        if item:
            for i in item:
                print(i)
        else:
            print(f'{buscar} não se encontra na lista.'
                  f' Deseja gerar uma senha para {buscar}? ')

            s_n = input('s/n: ')
            if s_n == 's':
                with open('gerador.csv', 'a', encoding='utf-8', newline='') as gerar:
                    cabecalho = ['Instituição', 'Senha']
                    escrever = csv.DictWriter(gerar, fieldnames=cabecalho)
                    if gerar.tell() == 0:  # Verifica se existe algo escrito na primeira linha
                        escrever.writeheader()

                    # Randomização dos elementos
                    dado = Dados(buscar)
                    cont = 0
                    while cont < 12:
                        randomizar = choice(concat)
                        temp.append(randomizar)
                        cont += 1

                    soldar = ''.join(temp)  # Concatenando as strings da lista temp
                    print('Gerando senha...')
                    sleep(0.8)
                    print(f'Senha para {buscar} gerada com sucesso! ')
                    escrever.writerow({'Instituição': dado.inst(), 'Senha': soldar})
                    del temp[:]  # Limpando a lista para qua não haja concatecação na gravação


def excluir():
    # Abrindo o arquivo e listando os itens
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        for i in ler:
            cast.append(i)

    # pecorrendo o cast
    """nome = 'Cepramed'
    for dados in cast:
        #            chave         valor
        if dados['Instituição'] == nome:
            print(dados)
            cast.remove(dados)
            print(cast)"""

    """with open('gerador_temp.csv', 'w', newline='', encoding='utf-8') as gerar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(gerar, fieldnames=cabecalho, lineterminator='\n')
        if gerar.tell() == 0:
            escrever.writeheader()

        escrever.writerow({'Instituição': cast[0], 'Senha': cast[1]})"""

    with open('gerador.csv', 'r', newline='', encoding='utf-8') as ler:
        with open('gerador_temp.csv', 'w', newline='', encoding='utf-8') as gerar:
            for linha in ler:
                if linha != 'Google':
                    gerar.write(linha)

# Menu
while True:
    print('=' * 25 + ' GERADOR DE SENHA ' + '=' * 25)
    print('1 - Gerar senha automatica | '
          '2 - Gera senha manual | '
          '3 - Ver senhas | '
          '4 - Buscar por senha | '
          '5 - Editar Instituição | '
          '6 - Excuir Instituição | '
          '7 - Sair')

    opc = input('Entre com a opção desejada: ')

    if opc == '1':
        print('=' * 10 + ' Gerando senha automatimente ' + '=' * 10)
        senha_auto()

    elif opc == '2':
        print('=' * 10 + ' Gerando senha manualmente ' + '=' * 10)
        senha_manual()

    elif opc == '3':
        print('=' * 10 + ' Suas senhas ' + '=' * 10)
        ver_senhas()

    elif opc == '4':
        print('=' * 10 + ' Buscar ' + '=' * 10)
        buscar()

    elif opc == '5':
        print('=' * 10 + ' Editar Instituição ' + '=' * 10)

    elif opc == '6':
        print('=' * 10 + ' Excluir Instituição ' + '=' * 10)
        excluir()

    elif opc == '7':
        print('saindo do gerador senha... ')
        sleep(0.8)
        break

