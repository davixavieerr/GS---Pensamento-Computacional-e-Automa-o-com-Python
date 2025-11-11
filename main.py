from perfil import Perfil
from recomendador import Recomendador
from utils import menu_principal, solicitar_competencias
import ia

perfil_atual = None
recomendador = Recomendador()

while True:
    menu_principal()
    opcao = input("\nEscolha uma opção: ")
    # Opção 1: Criar um novo perfil de usuário
    if opcao == "1":
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        tecnicas = solicitar_competencias("técnicas")
        comportamentais = solicitar_competencias("comportamentais")
        perfil_atual = Perfil(nome, idade, tecnicas, comportamentais)
        print("\nPerfil criado com sucesso!")
    # Opção 2: Exibir o perfil cadastrado
    elif opcao == "2":
        if perfil_atual:
            perfil_atual.exibir_perfil()
        else:
            print("\nNenhum perfil cadastrado.")
    # Opção 3: Obter recomendações pela lógica de pontuação
    elif opcao == "3":
        if not perfil_atual:
            print("\nCrie um perfil primeiro.")
        else:
            recomendacoes = recomendador.recomendar(perfil_atual)
            if recomendacoes:
                print("\nCarreiras recomendadas:")
                for c in recomendacoes:
                    print(f" - {c}")
            else:
                print("\nNenhuma carreira encontrada com base no seu perfil.")
    # Opção 4: Obter recomendações com a IA Gemini
    elif opcao == "4":
        if not perfil_atual:
            print("\nCrie um perfil primeiro.")
        else:
            print("\nGerando recomendações com IA Gemini...\n")
            try:
                resposta = ia.gerar_recomendacao_ia(perfil_atual)
                print(resposta)
            except Exception as e:
                print(f"Erro ao usar IA: {e}")
    # Opção 5: Encerrar o programa
    elif opcao == "5":
        print("\nSaindo... até logo!")
        break
    # Tratamento de entrada inválida
    else:
        print("\nOpção inválida, tente novamente.")
