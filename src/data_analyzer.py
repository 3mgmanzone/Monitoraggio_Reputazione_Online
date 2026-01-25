
from transformers import pipeline

class DataAnalyzer:
    def __init__(self):
        # Prendo il modello che mi è stato indicato su HggingFace - inizializzazione
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
                
        # Crea la pipeline di Hugging Face
        self.classifier = pipeline(
            "sentiment-analysis", 
            model=self.model_name, 
            tokenizer=self.model_name
        )
        
        # Mappatura per questo specifico modello
        self.labels_map = {
            "negative": "Negativo",
            "neutral": "Neutro",
            "positive": "Positivo"
        }

    def _preprocess(self, text):
        # pulizia del testo
        new_text = []
        for t in text.split(" "):
            # Sostituisce i tag utenti e i link per il modello
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    def predict(self, text):
        """Riceve un testo e restituisce sentiment e punteggio di confidenza"""
        # pulizia del testo
        text_cleaned = self._preprocess(text) 
        # ottieni il risultato dalla pipeline
        result = self.classifier(text_cleaned)[0]
        # restituisci il dizionario con le chiavi che app.py si aspetta
        return {
            "label": result['label'],
            "score": round(float(result['score']), 4)
        }
