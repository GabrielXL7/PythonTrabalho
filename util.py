def cabecalho():
    print('Bem vindo!\nSelecione a categoria de jogos:')
    print('1- Ação\n2- Aventura\n3- Esporte\n4- RPG\n5- Terror\n6- Para fechar o programa')
    print('Escolha a opção da categoria de jogos:')
def style(dataI):
    linha_horizontal = '-' * 133
    linha_vertical = '|'
    print(linha_horizontal)
    print(f"{linha_vertical} {'Nome':<40} {linha_vertical} {'Preços':<43} {linha_vertical} {'Avaliação':<40} {linha_vertical}")
    print(linha_horizontal)
    for _, row in dataI.iterrows():
        print(f"{linha_vertical} {row['Nome']:<40} {linha_vertical} R$ {row['Preços']:<40} {linha_vertical} {row['Avaliação']:<40} {linha_vertical}")
    print(linha_horizontal)
    finalizar()

def finalizar():
    print('1- Para voltar ao menu\n2- Para fechar o programa')
    item = int(input())
    if item == 2:
        exit()
def menu():
    print('1- Pagos\n2- Gratuito\n3- Pagos/Gratuito\n4- Voltar para o Menu')
    print('Escolha a opção de tipo de jogos:')

