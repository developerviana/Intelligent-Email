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
        # Dados de treino refinados para o cenário financeiro/corporativo
        self.training_data = [
            # PRODUTIVO: Status, Arquivos, Requisições
            ("Gostaria de saber o status da minha requisição número 1234.", "Produtivo"),
            ("Segue em anexo o comprovante de pagamento para análise.", "Produtivo"),
            ("Qual o prazo para aprovação do contrato enviado ontem?", "Produtivo"),
            ("Encaminho o balanço mensal conforme solicitado.", "Produtivo"),
            ("Precisamos agendar uma reunião para revisar os KPI financeiros.", "Produtivo"),
            ("Favor confirmar o recebimento da nota fiscal e previsão de pagamento.", "Produtivo"),
            ("Atualização sobre o projeto de migração de dados.", "Produtivo"),
            ("Solicito alteração de dados cadastrais na minha conta.", "Produtivo"),
            
            # IMPRODUTIVO: Cumprimentos vazios, Conteúdo irrelevante, Spam
            ("Desejo a todos um Feliz Natal e Próspero Ano Novo!", "Improdutivo"),
            ("Bom dia, apenas passando para desejar uma ótima semana.", "Improdutivo"),
            ("Agradeço a atenção, muito obrigado.", "Improdutivo"),
            ("Você viu o jogo ontem? Foi incrível.", "Improdutivo"),
            ("Promoção exclusiva para você: clique aqui e ganhe prêmios.", "Improdutivo"),
            ("Pessoal, trouxemos bolo para comemorar o aniversário do João.", "Improdutivo"),
            ("Feliz páscoa para você e sua família.", "Improdutivo"),
            ("Qual o cardápio do almoço de hoje?", "Improdutivo"),
        ]
        self._train_model()

    def _train_model(self):
        """Treina um modelo simples de Naive Bayes ao iniciar."""
        texts = [data[0] for data in self.training_data]
        labels = [data[1] for data in self.training_data]
        
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())
        self.model.fit(texts, labels)

    def classify_text(self, text: str):
        """Retorna a categoria e a confiança."""
        if not text:
            return "Improdutivo", 0.0
            
        prediction = self.model.predict([text])[0]
        probs = self.model.predict_proba([text])[0]
        confidence = max(probs)
        
        return prediction, round(confidence, 2)

    def generate_response(self, category: str):
        """Gera uma resposta corporativa baseada na categoria."""
        if category == "Produtivo":
            responses = [
                "Sua solicitação foi recebida e encaminhada para o setor responsável. Retornaremos com o status em breve.",
                "Confirmamos o recebimento do arquivo. Nossa equipe fará a análise e entrará em contato se houver pendências.",
                "Obrigado pelo contato. Seu ticket foi priorizado na nossa fila de atendimento."
            ]
        else:
            responses = [
                "Agradecemos o contato e a cortesia. Desejamos uma ótima semana!",
                "Recebido. Caso tenha alguma solicitação específica no futuro, estamos à disposição.",
                "Agradecemos a mensagem. Equipe Financeira."
            ]
        return random.choice(responses)

ai_engine = AIEngine()