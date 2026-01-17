# Notas Técnicas - Email Inteligente

## 1. Visão Geral
O **Email Inteligente** é uma solução corporativa desenvolvida para automatizar a triagem e resposta de emails no setor financeiro. O sistema utiliza técnicas de Processamento de Linguagem Natural (NLP) para classificar mensagens recebidas e sugerir respostas adequadas, aumentando a produtividade da equipe operacional.

---

## 2. Arquitetura da Solução
O projeto segue uma arquitetura moderna separada em **Frontend (SPA)** e **Backend (REST API)**:

- **Frontend:** Angular 17 (Standalone Components)
- **Backend:** Python 3.12 + FastAPI
- **IA/ML:** Scikit-Learn (Naive Bayes Multinomial) + NLTK
- **Processamento de Arquivos:** PyPDF para extração de texto em PDFs

---

## 3. Frontend (Interface do Usuário)
Desenvolvido em **Angular 17**, focando em performance e limpeza de código.

### Estrutura e Estilo
- **Style:** SCSS com variáveis CSS (CSS Variables) para fácil manutenção de tema.
- **Design System:** Interface "Dashboard" compacta, otimizada para viewport 1080p sem rolagem excessiva.
- **Visual:** Background com textura técnica (`dot-grid`) e iluminação central para foco no conteúdo.

### Funcionalidades
- **Upload Híbrido:** Aceita arquivos `.txt` e `.pdf` via Drag & Drop ou seleção.
- **Input de Texto:** Área para colagem direta de corpo de email.
- **Comunicação:** Integração direta com API via `HttpClient` (Mock local removido para produção).
- **Feedback:** Indicadores de carregamento (Skeleton screens) e mensagens de erro amigáveis.

---

## 4. Backend (API e Processamento)
Desenvolvido em **Python** utilizando o framework **FastAPI** pela sua alta performance e tipagem estática (Pydantic).

### Endpoints
- `GET /`: Health check da API.
- `POST /api/classify`: 
  - Aceita `Multipart/Form-Data` (campo `text` e/ou `file`).
  - Processa arquivos PDF extraindo texto das páginas.
  - Retorna JSON com: `category`, `confidence` e `suggestion`.

### Dependências Principais
- `fastapi`: Framework web assíncrono.
- `uvicorn`: Servidor ASGI para produção.
- `python-multipart`: Para parsing de uploads de arquivo.
- `pypdf`: Para leitura e extração de texto de PDFs anexados.

---

## 5. Motor de Inteligência Artificial (`ai_engine.py`)
O núcleo de inteligência reside numa classe dedicada `AIEngine` que implementa um pipeline de Machine Learning (Scikit-Learn).

### Pipeline de Processamento
1.  **Vetorização (CountVectorizer):** Converte o texto livre em uma matriz de contagem de tokens (Bag of Words).
2.  **Classificação (MultinomialNB):** Algoritmo Naive Bayes, ideal para classificação de texto e NLP simples.

### Dados de Treinamento
O modelo é treinado *on-the-fly* (na inicialização) com um dataset curado para o cenário financeiro/corporativo:
- **Classe Produtivo:** Solicitações de status, envio de boletos, contratos, dúvidas operacionais.
- **Classe Improdutivo:** Cumprimentos vazios (Bom dia, Feliz Natal), spam, conversas pessoais.

### Geração de Resposta
Sistema híbrido determinístico que seleciona respostas de um pool pré-aprovado com base na categoria inferida, garantindo tom de voz corporativo e seguro.

---

## 6. Como Executar o Projeto

### Pré-requisitos
- Node.js (v18+)
- Python (v3.10+)

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
# Servidor rodará em http://127.0.0.1:8000
```

### Frontend
```bash
cd frontend
npm install
npm start
# Acessar em http://localhost:4200
```
