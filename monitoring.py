import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = "riscontri.csv"

if not os.path.exists(file_path):
    print(f"Errore: Il file {file_path} non esiste ancora. Ricevi qualche feedback dall'app prima!")
    return

# 1. Caricamento dati
df = pd.read_csv(file_path)

# Configurazione estetica
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle('MLOps Monitoring Dashboard - User Feedback Analysis', fontsize=16)

# 2. Grafico a Barre: Conteggio Sentiment (Distribuzione)
sns.countplot(data=df, x='label', ax=axes[0], palette='viridis', order=['negative', 'neutral', 'positive'])
axes[0].set_title('Distribuzione dei Sentiment rilevati')
axes[0].set_xlabel('Sentiment')
axes[0].set_ylabel('Numero di Commenti')

# 3. Boxplot: Distribuzione della Confidenza (Score) per ogni Sentiment
# Il Boxplot mostra mediana, quartili e possibili anomalie
sns.boxplot(data=df, x='label', y='score', ax=axes[1], palette='magma', order=['negative', 'neutral', 'positive'])
axes[1].set_title('Affidabilità (Score) per Categoria')
axes[1].set_xlabel('Sentiment')
axes[1].set_ylabel('Livello di Confidenza (0-1)')

# 4. Salvataggio e visualizzazione
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('monitoring_report.png')
print("Grafico salvato come 'monitoring_report.png'")
plt.show()
