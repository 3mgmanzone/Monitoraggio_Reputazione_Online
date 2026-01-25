
import gradio as gr
import os
import csv
from datetime import datetime
from src.data_analyzer import DataAnalyzer

# inizializzo la Classe DataAnalyzer
analyzer = DataAnalyzer()
CSV_FILE = "riscontri.csv"


def save_to_csv(text: str, label: str, score: float):
    # Controlla se il file esiste già per scrivere l'intestazione solo la prima volta
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Se il file è nuovo, scrivi i nomi delle colonne (header)
        if not file_exists:
            writer.writerow(['timestamp', 'text', 'label', 'score'])
        # Scrive il nuovo riscontro
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text, label, score])


# funzione per analizzare il testo inserito e ricavarne il risultato
def analyze(text: str):
    res = analyzer.predict(text)
    save_to_csv(text, res['label'], res['score'])
    return f"Sentiment: {res['label']} | Confidenza: {res['score']}"


# interfaccia grafica per inserimento dei dati
riscontro = gr.Interface(
    fn=analyze, 
    inputs=gr.Textbox(placeholder="Inserisci un Commento: ........"), 
    outputs="text",
    title="MLOps Reputation Monitor"
)

if __name__ == "__main__":
    # Rimuoviamo i parametri fissi e lasciamo che legga l'ambiente
    riscontro.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 8080)),
        share=True,          # <-- QUESTA è la chiave
        show_error=True
    )
