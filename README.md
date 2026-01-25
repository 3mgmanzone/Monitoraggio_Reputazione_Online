ARCHITETTURA - Monitoraggio_Reputazione_Online
 ┣ 📂 .github/ workflows
 ┣ 📂 src
 ┣ 📂 venv
 ┣ 📜 Dockerfile
 ┣ 📜 README.md
 ┣ 📜 app.py
 ┗ 📜 monitoring.py












--------    PROGETTO    --------


------ Fase 1: Implementazione del Modello di Analisi del sentiment con FastText (Profession_AI)
---- Servirsi di questo modello: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest (nelle consegne)
---- Dataset: scelgo https://huggingface.co/datasets/Sp1786/multiclass-sentiment-analysis-dataset (consigliato dalla rete)
-- data_catch.py: carica il dataset iniziale indicato solo per poterci sbirciare dentro "a mano"
        -- due istruzioni per sbirciare nel dataset e capire come gestirmelo
-- data_analyzer.py: istanzia la classe "Data_Analyzer" per verificare "a mano" come si comporta il modello
        -- creazione della Classe con le sue caratteristiche
        -- in pratica prende il testo e lo rielabora un attimo per i ns scopi
        -- il risultati del "self.predict" è la valutazione del testo che gli viene passato
-- data_train.py: strumenti per addestrare il modello e tenerlo aggiornato


------ Fase 2: Pipeline CI/CD automatizzata per Training del modello, Test di integrazione e Deploy su HuggingFace
-- main.yml: dico a GitHub che con ogni "push" deve controllare il codice e caricalo su Hugging Face
        -- : non sono in grado di generare da solo un file del genere e l'ho ricercato in rete


------ Fase 3: Deploy e Monitoraggio Continuo
Deploy HuggingFace: Implementa il modello di analisi del sentiment, con dati e applicazione, facilitando integrazione e scalabilità
Sistema di Monitoraggio: configuralo per valutare continuamente le performance del modello e il sentiment rilevato
-- app.py: questo è un po' il main di tutto il Progetto
        -- inizializzo il modello che voglio utilizzare
        -- lancio la parte per raccogliere il "riscontro" dal web
        -- valuto tramite il modello il "riscontro" ottenuto e òo pubblico subito
-- test_df.csv: ho caricato il dataset per il test direttamente nel repository
-- train_df.csv: ho caricato il dataset per il train direttamente nel repository
-- riscontri.csv: qui raccoglo i riscontri ovvero i commenti degli utenti per futuri training
        -- in futuro, con una cadenza da capire, integro il "riscontri.csv" con il "train_df.csv" e con il "test_df.csv"
-- data_train.py: mi creo un modello nuovo quando raccolgo abbastanza dati
        --lancio un nuovo Training con "data_train.py" sfruttando i dati vecchi ed i dati nuovi
-- monitoring.py: ultimo script da lanciare con una cadenza da definire
        -- mi fa un grafico semplice per riassumere i risultati dei riscontri
