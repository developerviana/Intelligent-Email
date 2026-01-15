# Email Inteligente

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)]()
[![Angular](https://img.shields.io/badge/Frontend-Angular%2017-red)](https://angular.io/)
[![Python](https://img.shields.io/badge/Backend-FastAPI-blue)](https://fastapi.tiangolo.com/)

Aplicação web inteligente para classificação automática de e-mails e sugestão de respostas utilizando Inteligência Artificial. O objetivo é aumentar a produtividade identificando e-mails importantes e agilizando o processo de resposta.

## 🚀 Funcionalidades

-   **Classificação Automática**: Analisa o conteúdo do e-mail (texto ou arquivo PDF/TXT) e categoriza como "Produtivo" ou "Improdutivo".
-   **Sugestão de Resposta**: Gera uma resposta automática contextualizada para e-mails classificados.
-   **Upload de Arquivos**: Suporte para arrastar e soltar arquivos `.txt` e `.pdf`.
-   **Interface Moderna**: Design limpo e responsivo focado na experiência do usuário.

## 🛠️ Tecnologias Utilizadas

O projeto segue uma arquitetura modular dividida entre frontend e backend:

### Frontend
-   **Framework**: Angular 17 (Standalone Components)
-   **Estilização**: SCSS com variáveis CSS e design system moderno.
-   **HTTP Client**: Integração preparada para consumir a API REST.

### Backend (Em Breve)
-   **Framework**: FastAPI (Python)
-   **IA/NLP**: Processamento de Linguagem Natural para classificação e geração de texto.

## 📂 Estrutura do Projeto

```bash
Email-Inteligente/
├── frontend/           # Aplicação Angular (Interface do Usuário)
└── backend/            # API Python (Lógica de IA e Processamento) - Em desenvolvimento
```

## 🏁 Como Executar

### Pré-requisitos
-   Node.js (v18+)
-   Angular CLI (`npm install -g @angular/cli`)
-   Python 3.10+ (para o backend)

### Deploy

O frontend da aplicação é implantado automaticamente na Vercel.

## 📝 Licença

Este projeto está sob a licença [MIT](LICENSE).
