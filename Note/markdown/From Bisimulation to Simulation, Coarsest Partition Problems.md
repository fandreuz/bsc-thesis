---
tags: [bisimulazione, coarsest partition, paper, tesi]
title: 'From Bisimulation to Simulation, Coarsest Partition Problems'
created: '2020-07-21T06:33:06.901Z'
modified: '2020-07-25T10:57:00.583Z'
---

# From Bisimulation to Simulation, Coarsest Partition Problems

### Bisimulazione massima
Si può dimostrare che la relazione $\equiv_b$, data dai nodi tra i quali esiste una qualche bisimulazione, è una relazione di equivalenza, ed è la massima bisimulazione.

### Proposizione 3.3
+ Dato un grafo $G(N,\to,\Sigma)$ dove $\Sigma$ è una partizione stabile rispetto a $\to$, la relazione $R_{\Sigma}(a,b)$ valida se a e b appartengono allo stesso blocco di $\Sigma$ è una bisimulazione
  - il primo punto della definizione è banale
  - suppongo che valga $R_{\Sigma}(a,b)$. Allora a,b stanno nello stesso blocco $\alpha$. Suppongo che esista un nodo $a \to c$.
    * se $c \in \beta$ con $\beta \neq \alpha$, per la stabilità della partizione si ha che per ogni nodo nel blocco $\alpha$ deve esistere un ramo verso un nodo del blocco $\beta$ (perchè l'intersezione tra $\alpha$ e $\to^{-1}(\beta)$ è non vuota, considerando il ramo $a \to c$). Quindi esite un ramo $b \to d$ per un $d \in \beta$. Allora $R_{\Sigma}(c,d)$ (appartengono allo stesso blocco $\beta$).
    * se $c \in \alpha$, si può fare lo stesso ragionamento applicato sopra? Dipende dalla definizione di stabilità: vale anche se $\alpha = \beta$?
  - lo stesso argomento può essere applicato per un ramo $b \to d$
+ Dato un grafo $G(N,\to)$ ed una bisimulazione $R$ (che sia anche una relazione di equivalenza), la partizione indotta da $R$ è stabile rispetto a $\to$.
Per partizione indotta si intende che i blocchi sono formati dai nodi per cui vale $R(a,b)$.
Infatti suppongo di avere due nodi a,b di un blocco $\alpha$. Suppongo che esista un ramo $a \to c$ con $c \in \beta \neq \alpha$. Allora per definizione di bisimulazione deve esistere un nodo $d \in \beta$ (perchè $R(c,d)$) ed esiste il ramo $b \to d$. Questo ragionamento vale per qualsiasi nodo $b \in \alpha$, quindi $\alpha \subset \to^{-1}(\beta)$ a patto che esista il primo ramo $a \to c$. 
Se non esiste nessun ramo $a \to c$ per qualche $c \notin \alpha$, allora $\alpha \, \cap \to^{-1}(\beta) = \emptyset$.

**Nota**: il richiedere nel secondo punto che la bisimulazione $R$ sia una relazione di equivalenza non fa perdere generalità, in quanto data una bisimulazione $r$, la sua chiusura transitiva, riflessiva e simmetrica è ancora una bisimulazione.

### Bisimulazione e insiemi non ben fondati
Dato un grafo $G(N,\to,\Sigma)$ ed una bisimulazione $R$, è possibile trovare un grafo $G'(N',\to')$ con $N \subset N'$, $\to \subset \to'$, per cui vale $R(a,b)$ su $G$ $\iff$ $R(a,b)$ su $G'$ (non si considera il primo punto della definizione di bisimulazione).
Allora la definizione più "astratta" (senza partizione) di bisimulazione è abbastanza generale da inglobare tutte le bisimulazioni con partizione.

### Rango di un nodo
$$rank(a) = \begin{cases}
0 \qquad \,\,\,\,\,\,\,\, \text{se a è una foglia in } G\\
-\infty \qquad \text{se } C(a) \text{ è una foglia in } G^{SCC} \text{ e a non è una foglia in } G\\
\max \begin{cases}
1 + rank(c) \text{ se } C(a) \to^{SCC} C(c) \land c \in WF(G)\\
rank(c) \text{ se } C(a) \to^{SCC} C(c) \land c \notin WF(G)
\end{cases} \qquad \forall c \in G(a)
\end{cases}$$
Dove $C(a)$ è il sottografo strongly connected in cui è contenuto a.

Due proprietà importanti del rango lo rendono interessante dal punto di vista della bisimulazione:
+ $a \equiv_b b \implies rank(a) = rank(b)$
+ Se $\equiv_b$ è stata computata per tutti i nodi con rango $<$ i, allora può essere computata anche per i nodi con rango $=$ i

### Grafo quoziente rispetto alla bisimulazione $\equiv_b$
Sia $G(N, \to, l)$ un grafo. Il grafo quoziente $G /\equiv_b$ è definito come
$$\begin{cases}
N_{\equiv_b} = N /\equiv_b\\
[a]_b \to_{\equiv_b} [c]_b \iff \exists \,\, c_1 : (c_1 \in [c]_b \land a \to c_1)\\
l_{\equiv_b}([a]_b) = l(a)
\end{cases}$$

### Proposizione 3.10
Sia $G(N, \to, l)$ un grafo. Allora il grafo $G /\equiv_b$ è il **minor grafo** in bisimulazione con $G$.
Abbiamo rimpiazzato i nodi di $G$ con le classi di equivalenza della bisimulazione.
