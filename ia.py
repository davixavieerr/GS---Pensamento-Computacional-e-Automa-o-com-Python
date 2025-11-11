import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def gerar_recomendacao_ia(perfil):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    Você é um orientador de carreira especialista no "Future at Work", respondendo de forma clara, objetiva e inspiradora.

    Baseado no perfil de {perfil.nome} ({perfil.idade} anos), analise suas competências e recomende 3 carreiras adequadas.

    Perfil:
    - Competências Técnicas: {', '.join(perfil.competencias_tecnicas)}
    - Competências Comportamentais: {', '.join(perfil.competencias_comportamentais)}

    Sua resposta DEVE seguir esta estrutura:

    1.  Uma breve introdução motivacional para o {perfil.nome}.
    2.  As 3 recomendações de carreira.
    3.  Para CADA carreira, inclua uma seção "Trilha de Aprendizado" ou "Próximos Passos", sugerindo 1 ou 2 habilidades, cursos ou tecnologias específicas que {perfil.nome} poderia focar para se destacar nessa área.
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    resposta = model.generate_content(prompt)
    return resposta.text.strip()
