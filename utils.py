def menu_principal():
    #Exibe o menu principal de opções no console.
    print("\n=== Menu ===")
    print("1. Criar novo perfil")
    print("2. Exibir perfil atual")
    print("3. Obter recomendações")
    print("4. Obter recomendações com IA Gemini")
    print("5. Sair")

def solicitar_competencias(tipo):
    #Solicita ao usuário 3 competências de um tipo específico (técnica ou comportamental) e retorna uma lista.
    print(f"\nDigite 3 competências {tipo} separadas por vírgula:")
    return [c.strip().lower() for c in input("→ ").split(",")[:3]]