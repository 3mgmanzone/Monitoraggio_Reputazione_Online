# Monitoraggio della reputazione online di un’azienda

## Descrizione del progetto
Questo progetto ha come obiettivo il **monitoraggio della reputazione online di un’azienda**
attraverso l’**analisi automatica del sentiment** espresso dagli utenti sui social media.

Il lavoro integra concetti di **Machine Learning** e **MLOps**, coprendo le fasi di:
- sviluppo del modello
- addestramento
- analisi dei risultati
- monitoraggio delle prestazioni

## Obiettivo
L’obiettivo principale è permettere all’azienda di:
- analizzare automaticamente il sentiment degli utenti
- monitorare l’andamento della reputazione nel tempo
- supportare decisioni basate sui dati raccolti

## Modello utilizzato
Per l’analisi del sentiment viene utilizzato il seguente modello pre-addestrato:

- **Twitter RoBERTa – Sentiment Analysis**  
  https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

## Dataset utilizzato
Il modello viene addestrato e testato utilizzando un dataset pubblico:

- **Multiclass Sentiment Analysis Dataset**  
  https://huggingface.co/datasets/Sp1786/multiclass-sentiment-analysis-dataset

## Requisiti di installazione
Tutte le librerie necessarie all’esecuzione del progetto sono elencate nel file:

- `requirements.txt`

## Struttura del progetto
```text
src/
├── data_catch.py       # Analisi preliminare del dataset
├── data_train.py       # Addestramento del modello di sentiment analysis
├── data_analyzer.py    # Analisi del sentiment sui dati
├── app.py              # Avvio dell'applicazione
├── monitoring.py       # Monitoraggio delle prestazioni del modello
├── requirements.txt    # Dipendenze del progetto
├── riscontri.csv       # Dati raccolti dagli utenti
├── test_df.csv         # Dataset utilizzato per il test
└── train_df.csv        # Dataset utilizzato per il training
