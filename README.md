# Email Inteligente

[![Status](https://img.shields.io/badge/Status-Funcional-brightgreen)]()
[![Angular](https://img.shields.io/badge/Frontend-Angular%2017-red)](https://angular.io/)
[![Python](https://img.shields.io/badge/Backend-FastAPI-blue)](https://fastapi.tiangolo.com/)
[![AI](https://img.shields.io/badge/AI-Scikit--Learn-orange)](https://scikit-learn.org/)

Aplicação web inteligente para classificação automática de e-mails e sugestão de respostas utilizando Inteligência Artificial. O sistema processa textos e arquivos (PDF/TXT), categorizando-os entre "Produtivo" ou "Improdutivo" e sugerindo ações imediatas.

## 🚀 Funcionalidades

-   **Classificação via IA**: Utiliza algoritmo de Machine Learning (*LinearSVC* e *MultinomialNB*) para categorizar e-mails.
-   **Processamento de Arquivos**: Suporte nativo para leitura e extração de texto em arquivos `.pdf` e `.txt`.
-   **Interface Otimizada**: UI Dashboard compacta com design "Dot-Grid", focado em produtividade e visualização clara.
-   **Sugestão de Resposta**: Gera templates de resposta baseados na categoria identificada.

## 🛠️ Tecnologias Utilizadas

### Frontend
-   **Framework**: Angular 17 (Standalone Components)
-   **Estilização**: SCSS, CSS Variables, Layout Responsivo.
-   **Hospedagem**: Vercel (CI/CD Automático).

### Backend
-   **Framework**: FastAPI (Python 3.12)
-   **IA & NLP**: Scikit-Learn (Machine Learning).
-   **Processamento**: PyPDF para extração de dados.
-   **Arquitetura**: REST API com suporte a CORS e Upload de Arquivos.

## 📂 Estrutura do Projeto

```bash
Email-Inteligente/
├── frontend/           # Aplicação Angular (UI/UX)
│   ├── src/app/        # Componentes e Lógica
│   └── vercel.json     # Configuração de Deploy
└── backend/            # API Python
    ├── main.py         # Aplicação FastAPI e Endpoints
    └── train_model.py  # Pipeline de Treinamento da IA
```

## 🏁 Como Executar Localmente

### 1. Backend (API)
Certifique-se de ter o Python 3.10+ instalado.

```bash
cd backend
# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows

# Instale as dependências
pip install fastapi uvicorn scikit-learn pypdf python-multipart

# Inicie o servidor
python main.py
# O servidor rodará em http://localhost:8000
```

### 2. Frontend (Interface)
Certifique-se de ter o Node.js (v18+) e Angular CLI instalados.

```bash
cd frontend
# Instale as dependências
npm install

# Inicie a aplicação
ng serve
# Acesso em http://localhost:4200
```

## 🚀 Deploy

-   **Frontend**: Configurado para deploy automático na **Vercel**.
-   **Backend**: Pronto para deploy em qualquer plataforma compatível com Python/Docker (Render, Railway, AWS).

## 📝 Licença

Este projeto está sob a licença [MIT](LICENSE).
