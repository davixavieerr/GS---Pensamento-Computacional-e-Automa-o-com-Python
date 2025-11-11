class Carreira:
    def __init__(self, nome, competencias_necessarias, area):
        self.nome = nome
        self.competencias_necessarias = competencias_necessarias
        self.area = area

    def __str__(self):
        return f"{self.nome} ({self.area})"
