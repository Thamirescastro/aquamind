# AquaMind 💧 - Checklist de Autocuidado e Hidratação Inteligente!
[![CI Quality Check](https://github.com/Thamirescastro/aquamind/actions/workflows/main.yml/badge.svg)](https://github.com/Thamirescastro/aquamind/actions/workflows/main.yml)

## 📖 Descrição do Problema Real
No cenário de trabalho remoto e estudos intensos, é comum que as pessoas negligenciem necessidades básicas. A desidratação e a falta de pausas para alongamento impactam diretamente a produtividade, o foco e a saúde física a longo prazo.

## 💡 Proposta da Solução
O **AquaMind** é uma aplicação CLI (Interface de Linha de Comando) que permite ao usuário registrar seu consumo de água e gerenciar tarefas essenciais de autocuidado de forma simples e direta, promovendo hábitos saudáveis durante a rotina digital.

## 👥 Público-alvo
Trabalhadores remotos, estudantes, desenvolvedores e qualquer pessoa que passe longos períodos em frente ao computador.

## ✨ Funcionalidades Principais

💧 **Entrega Inicial**
- Registro de consumo de água
- Checklist de autocuidado
- Controle de meditação
- Controle de alongamento
- Exibição de status em tempo real

🌿 **Entrega Intermediária**
- Integração com OpenWeather API
- Consulta de clima em tempo real
- Sugestão automática de ingestão diária de água
- Interface web com Flask
- Layout moderno estilo "clean girl"
- Organização em múltiplas páginas
- Deploy online no Render

## 🛠️ Tecnologias Utilizadas

- **Tecnologia**	Função
- **Python 3.12+**	            Linguagem principal
- **Flask**	                     Aplicação web
- **HTML**                       Estrutura da interface
- **CSS**	                     Estilização
- **Pytest**	                  Testes automatizados
- **Flake**	                     Qualidade e código
- **GitHub Actions**	            CI/CD
- **OpenWeather API**	         Dados climáticos
- **Render**	                  Deploy da aplicação

## ⚙️ **Instalação**

1. Clone o repositório
   
git clone https://github.com/Thamirescastro/aquamind.git

3. Acesse a pasta
   
cd aquamind

5. Instale as dependências
   
pip install -r requirements.txt

## 🔑 **Configuração da API**

Crie um arquivo .env na raiz do projeto:

API_KEY=sua_chave_openweather

Você pode obter uma chave gratuita em:

https://openweathermap.org/api

## ▶️ **Execução do Projeto**

🌐 **Aplicação Web**
python -m src.app

Acesse:

http://127.0.0.1:5000

💧 **Entrega Inicial (CLI)**

python -m src.main_inicial

🌿 **Entrega Intermediária (CLI)**
python -m src.main

🧪 **Executar Testes**

python -m pytest

## 🚀 **Deploy**

**O projeto foi publicado utilizando:**

Render
GitHub Actions
Deploy automatizado
