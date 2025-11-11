class Perfil:
    """Armazena e exibe os dados de um perfil de usuário."""
    
    def __init__(self, nome, idade, competencias_tecnicas, competencias_comportamentais):
        self.nome = nome
        self.idade = idade
        self.competencias_tecnicas = competencias_tecnicas
        self.competencias_comportamentais = competencias_comportamentais

    def exibir_perfil(self):
        """Imprime os detalhes do perfil formatados no console."""
        print(f"\nPerfil de {self.nome} ({self.idade} anos)")
        print(f"Competências Técnicas: {', '.join(self.competencias_tecnicas)}")
        print(f"Competências Comportamentais: {', '.join(self.competencias_comportamentais)}")
        