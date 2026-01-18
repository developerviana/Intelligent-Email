from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import ai_engine
import io
from pypdf import PdfReader

app = FastAPI(title="Email Inteligente API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "API rodando com sucesso!"}

@app.post("/api/classify")
async def classify_email(text: str = Form(None), file: UploadFile = File(None)):
    """
    Recebe o texto do email ou um arquivo e retorna a classificação!.
    """
    content = text or ""
    
    if file:
        file_bytes = await file.read()
        filename = file.filename.lower()
        
        if filename.endswith(".pdf"):
            try:
                reader = PdfReader(io.BytesIO(file_bytes))
                extracted_text = ""
                for page in reader.pages:
                    extracted_text += page.extract_text() + " "
                content += " " + extracted_text
            except Exception as e:
                print(f"Erro ao ler PDF: {e}")
                content += " " # Falha silenciosa para não quebrar fluxo, logs no console
        else:
            # Assume texto/txt
            content += " " + file_bytes.decode("utf-8", errors="ignore")

    content = content.strip()
    
    category, confidence = ai_engine.classify_text(content)
    suggestion = ai_engine.generate_response(category)

    return {
        "category": category,
        "confidence": float(confidence),
        "suggestion": suggestion,
        "source": "Modelo Scikit-Learn (Backend Real)"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)