import os

restaurantes = [{'nome':'Bob Burguer', 'categoria':'hamburguer', 'ativo':False}, 
                {'nome':'Japa', 'categoria':'japonesa', 'ativo':True},
                {'nome':'Mafia Quadriculada', 'categoria':'italiana', 'ativo':False},]

def exibir_nome_do_programa():
        ''' Exibe o nome estilizado do do programa na tela'''
        print('''
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    █▄▄▄▄▄█▄▄█▄▄█▄▄▄▄██▄▄▄▄█▄▄█▄▄███▄▄▄▄▄█▄▄█▄▄█▄▄▄███▄▄█▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄█
        ''')

def exibir_menu():
        ''' Exibe as opções disponíveis do programa na tela'''
        print('1. Cadastrar restaurante')
        print('2. Listar restaurante')
        print('3. Alternar o estado do restaurante')
        print('4. Sair\n')

def voltar_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nAperte ENTER para voltar ao menu principal.')
    main()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela
    
    Inputs:
    - texto str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '▪' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    '''Exibe uma mensagem de finalização do app'''
    exibir_subtitulo('Encerrando o App')

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadrastar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de resstaurantes
    

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\no restaurante {nome_do_restaurante} foi cadastrado com sucesso! :)')
    
    voltar_menu_principal()

def listar_restaurantes():
    ''' Lista todos os restaurante presentes na lista
    
    Outputs:
    - Exibe a lista de restaurantes na lista
    '''
    exibir_subtitulo('Lista de todos os restaurantes')
    
    titulo_lista = (f'{'Nome do restaurante'.ljust(22)} ║ {'Categoria'.ljust(20)} ║ {'Status'}')
    print(titulo_lista)
    linha2 = '═' * len((titulo_lista))
    print(linha2)
    
    for restaurante in restaurantes:
    # para cada restaurante na lsita de restaurantes
        nome_restaurante = restaurante['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} ║ {categoria.ljust(20)} ║ {ativo}')

    voltar_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativo de um restaurante

    Outputs:
    - Exibe mensagem indicando o sucesso da operação 
    '''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_menu_principal()


def opcao_invalida():
    ''' Exibe uma mensagem de opção invalida e retorna ao menu princial
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção Inválida!')
    voltar_menu_principal()

def escolher_opcao():
   ''' Solicita e executa a opção escolhida pelo usuário
   
   Outputs:
   -  Executa a opção escolhida pelo usuário
   '''
   try:
         opcao_escolhida = int(input('Escolha uma opção: '))
         # opcao_escolhida = int(opcao_escolhida)

         match opcao_escolhida:
            case 1:
               cadastrar_novo_restaurante()
            case 2:
               listar_restaurantes()
            case 3:
               alternar_estado_restaurante()
            case 4:
               finalizar_app()
            #case _:
            #   opcao_invalida()
   except:
       opcao_invalida()         
    
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()