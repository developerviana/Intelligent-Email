from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine import ai_engine 

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
def classify_email(request: EmailRequest):
    """
    Recebe o texto do email e retorna a classificação.
    Por enquanto, é um MOCK (simulação) para testar a conexão.
    """
    print(f"Texto recebido: {request.content}")
    
    return {
        "category": "Produtivo",
        "confidence": 0.99,
        "suggestion": "Recebemos sua mensagem e retornaremos em breve.",
        "source": "Backend Python (Mock)"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.post("/api/classify")
def classify_email(request: EmailRequest):
    # 1. Usa a IA para classificar
    category, confidence = ai_engine.classify_text(request.content)
    
    # 2. Gera a sugestão baseada na categoria
    suggestion = ai_engine.generate_response(category)
    
    print(f"Texto: {request.content[:30]}... -> {category} ({confidence})")

    return {
        "category": category,
        "confidence": float(confidence),
        "suggestion": suggestion,
        "source": "Modelo NaiveBayes (Scikit-Learn)"
    }