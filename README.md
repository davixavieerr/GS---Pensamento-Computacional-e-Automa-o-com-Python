- Orientador de Carreiras do Futuro
Sistema de orientação de carreira desenvolvido em Python para a Global Solution 2025.2 - Future at Work da FIAP.

- Descrição
Este projeto é um sistema desenvolvido em Python orientado a objetos que analisa perfis profissionais com base em competências técnicas e comportamentais para recomendar carreiras adequadas.
A aplicação foi criada para a disciplina de Pensamento Computacional e Automação com Python  e simula uma ferramenta inteligente de orientação. O sistema possui dois modos de recomendação:
Recomendação Lógica: Utiliza um sistema de pontuação e normalização de sinônimos para cruzar as competências do usuário com um banco de carreiras pré-definido.
Recomendação com IA: Integra-se à API do Gemini (Google) para fornecer uma análise detalhada e inspiradora do perfil do usuário, sugerindo 3 carreiras com descrições aprofundadas.

- Tecnologias e Conceitos
Linguagem: Python 3
Paradigma: Programação Orientada a Objetos (POO) 
Estrutura de Dados: Listas e Dicionários 
Organização: Código modularizado (dividido em várias classes e arquivos) 
APIs: Integração com a API Google Gemini (via google-generativeai) 
Gerenciamento de Chaves: Uso de python-dotenv para proteger a chave da API 

- Estrutura do Projeto
O projeto foi organizado em módulos para seguir as boas práticas de POO e facilitar a manutenção:

.
├── main.py                 # Ponto de entrada da aplicação, controla o menu e o fluxo principal
├── perfil.py               # Define a classe 'Perfil' (armazena dados do usuário)
├── carreira.py             # Define a classe 'Carreira' (armazena dados das carreiras)
├── recomendador.py         # Define a classe 'Recomendador' (contém a lógica de match sem IA)
├── ia.py                   # Contém a função de integração com a API do Gemini
├── utils.py                # Funções auxiliares (exibir menu, solicitar competências)
├── requirements.txt        # Lista de dependências do Python 
└── .env                    # Arquivo local para armazenar a chave da API (não versionado)

- Instruções de Execução
Para executar este projeto localmente, siga os passos abaixo:

1. Clonar o Repositório

git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO

2. Criar um Ambiente Virtual

python -m venv venv
venv\Scripts\activate

3. Instalar as Dependências

pip install -r requirements.txt

4. Configurar a Chave da API Gemini

(Isso vale para caso não tenhamos conseguido subir o projeto junto com a chave)
Este projeto utiliza a API do Google Gemini.
Obtenha sua chave de API no Google AI Studio.
Na raiz do projeto, crie um arquivo chamado .env.
Adicione sua chave ao arquivo da seguinte forma:
GEMINI_API_KEY=SUA_CHAVE_API_AQUI

5. Executar o Programa

python main.py

- Demonstração de Uso
Abaixo está um exemplo de fluxo de uso completo do sistema, desde a criação do perfil até a consulta de recomendações lógicas e com IA.

=== Menu ===
1. Criar novo perfil
2. Exibir perfil atual
3. Obter recomendações
4. Obter recomendações com IA Gemini
5. Sair

Escolha uma opção: 1
Digite seu nome: Davi
Digite sua idade: 18

Digite 3 competências técnicas separadas por vírgula:
→ java, python, html

Digite 3 competências comportamentais separadas por vírgula:
→ focado, trabalho em equipe, aprendo rapido

Perfil criado com sucesso!

=== Menu ===
1. Criar novo perfil
2. Exibir perfil atual
3. Obter recomendações
4. Obter recomendações com IA Gemini
5. Sair

Escolha uma opção: 2

Perfil de Davi (18 anos)
Competências Técnicas: java, python, html
Competências Comportamentais: focado, trabalho em equipe, aprendo rapido

=== Menu ===
1. Criar novo perfil
2. Exibir perfil atual
3. Obter recomendações
4. Obter recomendações com IA Gemini
5. Sair

Escolha uma opção: 3

Carreiras recomendadas:
 - Desenvolvedor de Software (Tecnologia)
 - Cientista de Dados (Tecnologia)
 - Engenheiro de Automação (Engenharia)

=== Menu ===
1. Criar novo perfil
2. Exibir perfil atual
3. Obter recomendações
4. Obter recomendações com IA Gemini
5. Sair

Escolha uma opção: 4

Gerando recomendações com IA Gemini...

Olá Davi! Que incrível ter você nessa fase cheia de potencial. Aos 18 anos, com um conjunto de habilidades técnicas e comportamentais tão promissor, você tem um futuro brilhante pela frente no mundo da tecnologia. Sua capacidade de aprender rápido, foco e espírito de equipe são superpoderes nesse mercado em constante evolução.

Com base no seu perfil, aqui estão 3 carreiras onde você pode não apenas se destacar, mas também encontrar muita satisfação e crescimento:

---

### 1. Desenvolvedor Web Full-stack
...
### 2. Desenvolvedor Backend / Engenheiro de Software (Java/Python)
...
### 3. Engenheiro de Dados / Analista de Dados (com foco em Python)
...

Davi, você está no início de uma jornada emocionante. Com sua base técnica sólida e, mais importante, sua mentalidade de aprendizagem e colaboração, o céu é o limite. Explore essas áreas, experimente projetos pessoais, e não tenha medo de mergulhar fundo. O futuro é seu para construir!

=== Menu ===
1. Criar novo perfil
2. Exibir perfil atual
3. Obter recomendações
4. Obter recomendações com IA Gemini
5. Sair

Escolha uma opção: 5

Saindo... até logo!