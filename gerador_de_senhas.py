import string
import csv
from time import sleep
from random import choice

letra = string.ascii_letters
numeros = string.digits
caracteres = '_@$&'

concat = letra + numeros + caracteres

temp = []  # lista temporaria para guardar a senha gerada aleatoriamente
cast = []  # Lista temporaria para guardar a leitura da def excluir()


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
    sleep(.8)
    with open('gerador.csv', 'a', encoding='utf-8', newline='') as gerar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(gerar, fieldnames=cabecalho)
        if gerar.tell() == 0:  # Verifica se existe algo escrito na primeira linha
            escrever.writeheader()

        while True:
            entrada = input('Digite o nome da instituição ou (1) para sair: - ').title()

            nome = Dados(entrada)
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
                print(f'A gerada para {entrada} é {soldar}! \n')
                escrever.writerow({'Instituição': nome.inst(), 'Senha': soldar})
                sleep(.8)
                del temp[:]  # Limpando a lista para qua não haja concatecação na gravação
            else:
                break
    print('\n')


def senha_manual():
    with open('gerador.csv', 'a', encoding='utf-8', newline='') as gerar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(gerar, fieldnames=cabecalho)
        if gerar.tell() == 0:
            escrever.writeheader()

        while True:
            opcao = input('Infomer o nome da  instituição ou (1) para sair: ').title()

            if opcao == '1':
                break
            else:
                senha = input('Informer a senha: ')
                escrever.writerow({'Instituição': opcao, 'Senha': senha})
                sleep(.8)
                print(f'A senha para {opcao} é {senha}')
                sleep(.8)
                print(f'Senha gravada com sucesso!')
    print('\n')


def ver_senhas():
    """
    Função que mosta as intituições e senhas
    :return:
    """
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        print('...')
        sleep(.8)
        for linhas in ler:
            print(linhas)
        sleep(.8)
    print('\n')


def auto_manual():
    """
    Função que da escolha se de gerar senhas manualmente ou automaticamente
    :return:
    """
    opcao = input('Criar senha manual (1) -- Gerar senha automatica (2): ')
    if opcao == '1':
        senha_manual()
    elif opcao == '2':
        senha_auto()


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
            sleep(.8)
            for i in item:
                print(i)
            sleep(.8)
            print('\n')
        else:
            print(f'{buscar} não se encontra na lista.'
                  f' Deseja gerar uma senha para {buscar}? ')

            s_n = input('s/n: ')
            if s_n == 's':
                auto_manual()


def excluir():
    # Abrindo o arquivo e listando os itens
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        for linhas in ler:
            cast.append(linhas)

    nome = input('Nome da Instituição: ').title()

    # removendo item do cast
    for chave in cast:
        if chave['Instituição'] == nome:

            print(f'Deseja excluir {nome}? ')

            opc_excluir = input('s/n: ')

            if opc_excluir == 's':
                print(f'Excluindo {nome}... ')
                sleep(0.8)
                cast.remove(chave)
                sleep(0.8)
                print(f'{nome} excluido com sucesso!')
            elif excluir == 'n':
                break

    # Atualizando o arquivo
    with open('gerador.csv', 'w', newline='', encoding='utf-8') as atualizar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(atualizar, fieldnames=cabecalho)
        if atualizar.tell() == 0:
            escrever.writeheader()

        # pecorrendo o cast e acessando so os valores
        for dados in cast:
            escrever.writerow({'Instituição': dados['Instituição'], 'Senha': dados['Senha']})

    # OBS: Necessario limpar o cast para não gerar duplicatas de dados.
    del cast[:]
    print('\n')


def editar():
    with open('gerador.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)
        for linhas in ler:
            cast.append(linhas)

    inst = input('Informe o nome da instituição: ').title()

    for chave in cast:
        if chave['Instituição'] == inst:
            print(f'Deseja alterar {inst}? ')
            opcao = input('s/n: ')

            if opcao == 's':
                cast.remove(chave)
            elif opcao == 'n':
                break

    with open('gerador.csv', 'w', newline='', encoding='utf-8') as atualizar:
        cabecalho = ['Instituição', 'Senha']
        escrever = csv.DictWriter(atualizar, fieldnames=cabecalho)
        if atualizar.tell() == 0:
            escrever.writeheader()

        for dados in cast:
            escrever.writerow({'Instituição': dados['Instituição'], 'Senha': dados['Senha']})

    del cast[:]

    auto_manual()


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
        editar()

    elif opc == '6':
        print('=' * 10 + ' Excluir Instituição ' + '=' * 10)
        excluir()

    elif opc == '7':
        print('saindo do gerador senha... ')
        sleep(0.8)
        break
