# Francesco Andreuzzi - Discussione

### Presentazione
Buongiorno, sono Francesco Andreuzzi

### Grafi diretti
Un grafo è una struttura matematica composta da un insieme di nodi (V) e un insieme di archi (E) che collegano coppie di nodi. Può essere utilizzato per rappresentare in modo molto naturale reti di vario tipo, come *social network*, reti logistiche, o reti di componenti elettronici.

### Bisimulazione I
L'abbondanza di applicazioni pratiche rende interessante svolgere analisi su sistemi modellizzati tramite grafi. L'analisi di cui mi sono occupato è la ricerca di nodi equivalenti, secondo la nozione di equivalenza data dalla massima bisimulazione. Informalmente, due nodi sono bisimili se si comportano allo stesso modo, cioè per ogni figlio di uno dei due si può trovare un figlio dell'altro nodo che si comporta come il figlio del primo.

Alcuni esempi: è chiaro che due pozzi (nodi senza figli) si comportano allo stesso modo.

### Bisimulazione II
Aggiungiamo i nodi **c** e **d**. Il nodo **c** ha un unico figlio (**a**) che si comporta come l'unico figlio di **d** (**b**). Quindi **c** e **d** sono bisimili.

### Bisimulazione III
Chiaramente aumentando il numero di nodi e archi questo tipo di analisi non si può più fare a occhio, e si rendono necessari algoritmi che risolvano il problema della bisimulazione.

### Massima bisimulazione
Le relazioni binarie che mostrano la proprietà caratteristica della bisimulazione su un grafo si chiamano appunto bisimulazioni. L'unione di tutte le bisimulazioni su un grafo dà la *massima bisimulazione*. Si può dimostrare che è ancora una *bisimulazione* e che è una *relazione di equivalenza*.

### Algoritmi
Per la risoluzione del problema della *massima bisimulazione* abbiamo considerato tre algoritmi: il primo e più celebre, l'algoritmo di **Paige-Tarjan**, che si basa sull'algoritmo di Hopcroft per la minimizzazione di automi a stati finiti; il più recente algoritmo di **Dovier-Piazza-Policriti**, che rifinisce l'approccio di Paige-Tarjan utilizzando un'euristica che consente di ordinare i nodi in base alla distanza dal pozzo raggiungibile più distante; infine l'algoritmo **incrementale di Saha**, che consente di aggiornare la massima bisimulazione dopo l'aggiunta di un nuovo arco, partendo dalla massima bisimulazione precedente alla modifica del grafo, evitando il ricalcolo da zero.

### VII

### VIII

### VIV

### IX

### X
