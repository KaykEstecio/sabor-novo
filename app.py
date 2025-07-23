import os

restaurantes = [{"nome":"pizza","categoria":"pizzaria","ativo":False},
                {"nome":"hamburguer","categoria":"hamburgueria","ativo":True},
                {"nome":"pastel","categoria":"pastelaria","ativo":False}]


def exibir_nome_do_app():
    """essa funçao exibe o nome do app
    e limpa o terminal"""

    os.system("cls")

    print("sᴀʙᴏʀ ɴᴏᴠᴏ\n")



def voltar_ao_menu_principal():
    """essa funçao exibe uma mensagem de retorno ao menu principal
    e aguarda o usuario pressionar uma tecla """

    input("\ndigite uma tecla poara retornar ao menu principal: ")
    
    
    main()


def exibir_subtitulos(texto):
    """essa funçao exibe o subtitulo do app
    e limpa o terminal"""

    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    """essa funçao exibe as opcoes do app
    e limpa o terminal"""

    print("1. cadastrar restaurante ")
    print("2. listar restaurante ")
    print("3. alternar estado do restaurante ")
    print("4. sair\n ")

def opcao_invalida():
    """essa funçao exibe uma mensagem de opcao invalida
    e limpa o terminal"""

    print("opcao invalida\n")


    voltar_ao_menu_principal()

def cadastrar_restaurante():
    """essa funçao cadastra um novo restaurante
    e limpa o terminal"""

    exibir_subtitulos("cadastro de novos restaurantes")
    nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"digite o nome da categoria do restaurante {nome_do_restaurante}:  ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print("o",nome_do_restaurante,"foi cadastrado!")


    voltar_ao_menu_principal()

def listar_restaurantes():
    """essa funçao lista os restaurantes cadastrados
    e limpa o terminal"""

    exibir_subtitulos("listando restaurantes")

    print(f"{"nome".ljust(22)} | {"categoria".ljust(22)} | status")
    print()

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """essa funçao ativa ou desativa um restaurante
    e limpa o terminal"""

    exibir_subtitulos("ativar ou desativar restaurante")
    nome_restaurante = input("digite o nome do restaurante que deseja ativar ou desativar: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem =f"{nome_restaurante} foi ativado!" if restaurante["ativo"] else f"{nome_restaurante} foi desativado!"
            print(mensagem)
    if not restaurante_encontrado:
        print(f" o restaurante {nome_restaurante} nao foi encontrado!")



    voltar_ao_menu_principal()


def escolher_opcao():
    """essa funçao escolhe a opcao do menu
    e limpa o terminal"""

    try:
        opcao_escolhida = input("escolha uma opção : ")
        opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:        
        opcao_invalida()


def finalizar_app():
    """essa funçao finaliza o app
    e limpa o terminal"""

    exibir_subtitulos("finalizar app")



def main():
    """essa funçao inicia o app
        e limpa o terminal"""

    os.system("cls")
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()            
