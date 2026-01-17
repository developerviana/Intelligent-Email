from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(title="Email Inteligente API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    content: str


@app.get("/")
def read_root():
    return {"status": "online", "message": "API rodando com sucesso!"}

@app.post("/api/classify")
def classify_email(resquest: EmailRequest):
    """
    Recebe o texto do email e retorna a classificação.
    Por enquanto, é um MOCK (simulação) para testar a conexão.
    """
    print(f"Texto recebido: {resquest.content}")
    
    return {
        "category": "Produtivo",
        "confidence": 0.99,
        "suggestion": "Recebemos sua mensagem e retornaremos em breve.",
        "source": "Backend Python (Mock)"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)