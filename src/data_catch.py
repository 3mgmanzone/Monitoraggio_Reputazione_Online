
from datasets import load_dataset


# Carico il dataset prescelto
df = load_dataset("Sp1786/multiclass-sentiment-analysis-dataset")

'''
ho visto tramite la pagina web ed uno script a parte che il DataSet ha queste caratteristiche:
- 31k righe di Train
- 5k righe di Test
- 5k righe di Evaluation

##  from datasets import load_dataset
    dataset = load_dataset("Sp1786/multiclass-sentiment-analysis-dataset")
    print(dataset)
    print( dataset["train"][40] )
    print( dataset["test"][40] )
    print( dataset["validation"][40] )

con questa istruzione a parte mi sono resto conto di cosa c'è dentro, per capire come lavorarci su
'''

# Il dataset è già diviso in Train ed in Test, quindi la separazione è semplice e non richiede controlli
train_data = dataset['train']
test_data = dataset['test']

'''
mi rendo conto di aver fatto correttamente, proseguendo a parte con due piccole istruzioni
print( train_data[40] )
print( test_data[40] )
'''
