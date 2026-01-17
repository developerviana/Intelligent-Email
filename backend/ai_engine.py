import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

class AIEngine:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.training_data = [
            ("Lembrem-se da reunião de orçamento amanhã às 14h.", "Produtivo"),
            ("Segue em anexo o relatório mensal de vendas.", "Produtivo"),
            ("Precisamos revisar as metas do Q3 urgente.", "Produtivo"),
            ("Confirmação de agendamento de call com cliente.", "Produtivo"),
            ("As notas fiscais foram emitidas e enviadas.", "Produtivo"),
            ("Vamos marcar um happy hour na sexta?", "Improdutivo"),
            ("Olha esse meme engraçado que vi no gato.", "Improdutivo"),
            ("Futebol hoje a noite, quem anima?", "Improdutivo"),
            ("Promoção de viagens imperdível, clique aqui.", "Improdutivo"),
            ("Fofoca: você viu o que aconteceu na copa?", "Improdutivo"),
        ]
        self._train_model()

    def _train_model(self):
        """Treina um modelo simples de Naive Bayes ao iniciar."""
        texts = [data[0] for data in self.training_data]
        labels = [data[1] for data in self.training_data]
        
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())
        self.model.fit(texts, labels)
        print("🤖 IA: Modelo treinado com sucesso!")

    def classify_text(self, text: str):
        """Retorna a categoria e a confiança."""
        if not text:
            return "Improdutivo", 0.0
            
        prediction = self.model.predict([text])[0]
        probs = self.model.predict_proba([text])[0]
        confidence = max(probs)
        
        return prediction, round(confidence, 2)

    def generate_response(self, category: str):
        """Gera uma resposta baseada na categoria (Simulação de GPT)."""
        if category == "Produtivo":
            responses = [
                "Recebido. Vou analisar e retorno em breve.",
                "Obrigado pelo envio. Já coloquei na minha lista de prioridades.",
                "Confirmado. Nos falamos conforme o agendado."
            ]
        else:
            responses = [
                "No momento estou focado em tarefas prioritárias. Conversamos depois.",
                "Agradeço, mas não posso participar agora.",
                "Vou arquivar para leitura posterior."
            ]
        return random.choice(responses)

ai_engine = AIEngine()