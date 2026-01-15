
import evaluate
import numpy as np
from datasets import load_dataset
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    TrainingArguments, 
    Trainer,
    DataCollatorWithPadding
)

# caricamento Dataset e Modello
model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
dataset = load_dataset('csv', data_files={
    'train': 'train_df.csv',
    'test': 'test_df.csv'
})
# Prendi solo un piccolo campione per velocizzare il test
dataset['train'] = dataset['train'].shuffle(seed=42).select(range(200))
dataset['test'] = dataset['test'].shuffle(seed=42).select(range(50))

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# pre-processing
def tokenize_function(examples):
    # Convertiamo ogni elemento in stringa per evitare valori None/NaN
    texts = [str(t) if t is not None else "" for t in examples["text"]]
    return tokenizer(texts, truncation=True, padding="max_length", max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# metriche di valutazione
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    # Prende la categoria con il punteggio più alto
    predictions = np.argmax(logits, axis=-1)
    # Calcola la media di quante volte previsione == etichetta reale
    acc = (predictions == labels).mean()
    return {"accuracy": acc}

# configurazione Training (Logica MLOps)
training_args = TrainingArguments(
    output_dir="./modelli/sentiment_results",
    eval_strategy="no",                 # Disabilita la valutazione durante il training per risparmiare tempo
    save_strategy="no",                 # Non salvare file pesanti su disco
    num_train_epochs=1,                 # Fai solo un passaggio (un'epoca)
    per_device_train_batch_size=8,      # Aumenta un po' se la RAM lo permette (velocizza la CPU)
    no_cuda=True                        # Conferma esplicitamente che non usi la GPU
)

# inizializzazione Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

# avvio Training
trainer.train()
# salvataggio Finale
trainer.save_model("./modelli/final_sentiment_model")
