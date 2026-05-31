# AquaMind 💧 - Checklist de Autocuidado e Hidratação Inteligente!
[![CI Quality Check](https://github.com/Thamirescastro/aquamind/actions/workflows/main.yml/badge.svg)](https://github.com/Thamirescastro/aquamind/actions/workflows/main.yml)

## 📖 Descrição do Problema Real
No cenário de trabalho remoto e estudos intensos, é comum que as pessoas negligenciem necessidades básicas. A desidratação e a falta de pausas para alongamento impactam diretamente a produtividade, o foco e a saúde física a longo prazo.

## 💡 Proposta da Solução
O **AquaMind** é uma aplicação focada em bem-estar que permite ao usuário gerenciar tarefas essenciais de autocuidado de forma simples e direta, promovendo hábitos saudáveis durante a rotina digital através de uma interface web e de linha de comando (CLI).

## 👥 Público-alvo
Trabalhadores remotos, estudantes, desenvolvedores e qualquer pessoa que passe longos períodos em frente ao computador.

## 🚀 **Deploy & Integração Contínua**

O projeto possui esteira de CI/CD configurada via **GitHub Actions** para testes automatizados e deploy automatizado na nuvem.

* **Link da Aplicação (Render):** https://aquamind-77j8.onrender.com

---

## ✨ Evolução do Projeto e Funcionalidades

💧 **Entrega Inicial**
- Registro de consumo de água (unidades simples).
- Checklist de autocuidado básico.
- Controle de tarefas como meditação e alongamento.
- Exibição de status em tempo real.

🌿 **Entrega Intermediária**
- Integração com a **OpenWeather API** para consulta de clima em tempo real.
- Sugestão automática de ingestão diária de água baseada na temperatura local.
- Criação da interface web dinâmica utilizando **Flask**.
- Layout moderno e responsivo com organização em múltiplas páginas.
- Configuração do deploy online no **Render**.

🚀 **Entrega Final (Nova Funcionalidade)**
- **Gerenciamento de Metas Dinâmicas:** Permite ao usuário definir e alterar sua própria meta de hidratação diária em mililitros (ml) direto pela interface.
- **Registro Realista de Consumo:** Atualização do contador para registrar o consumo em ml (incrementos de 250ml por copo).
- **Indicador de Progresso Visual:** Implementação de uma barra de progresso gráfica (`<progress>`) e cálculo de porcentagem em tempo real para acompanhar a meta do dia.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python 3.12+** | Linguagem principal do projeto |
| **Flask** | Framework para desenvolvimento da aplicação web |
| **HTML5 / CSS3** | Estruturação e estilização visual da interface |
| **Pytest** | Framework de testes unitários automatizados |
| **Flake8** | Linter para garantia de qualidade e padronização do código |
| **GitHub Actions** | Automação da esteira de CI/CD (Quality Check) |
| **OpenWeather API** | Serviço de integração para consumo de dados climáticos |
| **Render** | Plataforma de nuvem para hospedagem do app |

---

## Histórico de Hidratação

O sistema permite consultar os registros de hidratação armazenados no Supabase, possibilitando ao usuário acompanhar seu consumo de água ao longo do tempo.

---

## Integrantes: Thamires Mendonça, Abner Trindade, Julia Marques e Emanuelle Christinie 
