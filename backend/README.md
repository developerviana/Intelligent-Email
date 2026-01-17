# Email Inteligente - Backend API

API REST desenvolvida com **FastAPI** para classificar e-mails utilizando Inteligência Artificial. Este serviço processa textos e arquivos PDF, retornando a categoria ("Produtivo" ou "Improdutivo") e uma sugestão de resposta.

## 🛠️ Tecnologias

-   **Python 3.12**
-   **FastAPI**: Framework web de alta performance.
-   **Scikit-Learn**: Algoritmos de Machine Learning (LinearSVC, MultinomialNB).
-   **NLTK**: Processamento de Linguagem Natural (Stopwords, Tokenização).
-   **PyPDF**: Extração de texto de arquivos PDF.

## 🚀 Como Rodar Localmente

1.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    
    # Windows
    .\venv\Scripts\activate
    
    # Linux/Mac
    source venv/bin/activate
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

    *Nota: Se o arquivo `requirements.txt` não existir, instale manualmente:*
    ```bash
    pip install fastapi uvicorn scikit-learn nltk pypdf python-multipart
    ```

3.  **Inicie o servidor:**
    ```bash
    python main.py
    ```

A API estará disponível em: `http://localhost:8000`

## 📡 Endpoints

### `POST /api/classify`
Classifica um texto ou arquivo enviado.

**Parâmetros (Form Data):**
-   `text` (string, opcional): O corpo do e-mail.
-   `file` (file, opcional): Arquivo `.pdf` ou `.txt`.

**Resposta (JSON):**
```json
{
  "category": "Produtivo",
  "confidence": 0.95,
  "suggestion": "Prezado(a), Recebemos seu documento...",
  "source": "Arquivo PDF"
}
```

### `GET /api/health`
Verifica se a API está online.
