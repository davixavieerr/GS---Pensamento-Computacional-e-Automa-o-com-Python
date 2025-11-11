from carreira import Carreira

class Recomendador:
    def __init__(self):
        self.carreiras = [
            Carreira("Desenvolvedor de Software", 
                     ["lógica", "programação", "python", "java", "resolução de problemas", "tecnologia", "trabalho em equipe"], 
                     "Tecnologia"),
            
            Carreira("Cientista de Dados", 
                     ["estatística", "python", "análise de dados", "curiosidade", "matemática", "machine learning"], 
                     "Tecnologia"),
            
            Carreira("Designer UX/UI", 
                     ["criatividade", "design", "empatia", "interface", "inovação", "experiência do usuário"], 
                     "Design"),
            
            Carreira("Gestor de Projetos", 
                     ["liderança", "organização", "comunicação", "planejamento", "gestão"], 
                     "Administração"),
            
            Carreira("Engenheiro Ambiental", 
                     ["sustentabilidade", "ciência", "análise", "planejamento", "responsabilidade"], 
                     "Engenharia"),
            
            Carreira("Professor", 
                     ["didática", "comunicação", "empatia", "ensino", "paciência", "organização"], 
                     "Educação"),
            
            Carreira("Engenheiro de Automação", 
                     ["python", "eletrônica", "automação", "foco", "análise", "tecnologia"], 
                     "Engenharia"),
            
            Carreira("Psicólogo Organizacional", 
                     ["empatia", "comunicação", "análise comportamental", "colaboração", "escuta ativa"], 
                     "Psicologia")
        ]

        self.sinonimos = {
            "focado": ["foco", "atenção", "concentrado"],
            "trabalho em equipe": ["colaboração", "cooperação", "time"],
            "aprendo rapido": ["aprendizagem", "curioso", "adaptabilidade"],
            "python": ["programação", "lógica"],
            "html": ["web", "frontend", "site"],
            "criativo": ["criatividade", "inovação"],
            "comunicação": ["expressão", "fala", "oratória"],
        }

    def normalizar_competencias(self, competencias):
        """Substitui sinônimos por palavras equivalentes para aumentar as correspondências"""
        competencias_norm = set()
        for comp in competencias:
            comp = comp.lower().strip()
            for chave, lista in self.sinonimos.items():
                if comp == chave or comp in lista:
                    competencias_norm.add(chave)
                    break
            else:
                competencias_norm.add(comp)
        return list(competencias_norm)

    def pontuar_carreira(self, perfil):
        """Calcula pontuação de correspondência entre o perfil e cada carreira"""
        competencias_usuario = self.normalizar_competencias(
            perfil.competencias_tecnicas + perfil.competencias_comportamentais
        )

        pontuacoes = []
        for carreira in self.carreiras:
            match = 0
            for comp in competencias_usuario:
                for chave, lista in self.sinonimos.items():
                    if comp == chave or comp in lista:
                        if chave in carreira.competencias_necessarias:
                            match += 1
                if comp in carreira.competencias_necessarias:
                    match += 1
            pontuacoes.append((carreira, match))
        return pontuacoes

    def recomendar(self, perfil):
        """Retorna as 3 melhores carreiras com base nas pontuações"""
        pontuacoes = self.pontuar_carreira(perfil)
        pontuacoes.sort(key=lambda x: x[1], reverse=True)

        recomendadas = [c for c, p in pontuacoes if p > 0]
        if not recomendadas:
            recomendadas = [self.carreiras[0], self.carreiras[3]]
        return recomendadas[:3]
