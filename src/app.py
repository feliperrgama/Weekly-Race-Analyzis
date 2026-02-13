# Página inicial para inserção e visualização dos dados contidos no banco de dados:

import pages.insert_data

print(f'{'='*5} MENU {'='*5}')
print('< 1 > Inserir dados de corrida\n< 2 > Visualizar dados das corridas')
opt = input(int('-> '))

match opt:
    case 1:
        # Colocar a função da página 'insert_data'
    case 2:
        # Colocar a função da página 'view_data'
    case _:
        # Colocar tratamento de erro
    