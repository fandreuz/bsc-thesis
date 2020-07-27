---
tags: [tesi]
title: Definizioni
created: '2020-07-21T06:36:50.829Z'
modified: '2020-07-22T16:47:07.577Z'
---

# Definizioni

### Relazione antisimmetrica
Sia $R$ una relazione. Diremo che $R$ è antisimmetrica se il fatto che valga $R(a,b)$ implica che non vale $R(b,a)$

### Transitive closure
Sia $R$ una relazione. Chiameremo "transitive closure" di $R$, $R_+$, la più piccola relazione (cioè che mette in relazione il minor numero di elementi) tale che
+ $R \subset R_+$
+ $R_+$ è transitiva

### Bisimulazione
Diremo che una relazione $R$ è una bisimulazione se
+ $R(a,b)$ implica che a,b stanno nella stessa partizione (quindi il concetto di bisimulazione dipende dalla scelta della partizione(?))
+ Se $R(a,b)$, e se esiste un ramo $a \to c$, allora esiste un nodo d tale che $R(c,d)$ ed esiste un ramo $b \to d$
+ La stessa cosa vale se il ragionamento viene fatto dalla parte di b

I punti 2,3 per la bisimulaione $\equiv_b$ si possono scrivere come
$$\begin{gathered} 
\forall \,\, a,b,c : (a \to c \land b \in [a]_b) \implies \,\, \exists \,\, d : (b \to c \land d \in [c]_b 
\end{gathered}$$
dove $[a]_b$ indica l'insieme dei nodi che sono in bisimulazione (per qualche bisimulazione) con a.

### Bisimulazione tra grafi
Siano due grafi $G_1(N_1, \to_1, l_1)$ e $G_2(N_2, \to_2, l_2)$, con $l_1, l_2$ funzioni "etichettanti" che mappano i nodi dei rispettivi grafi in un insieme comune di etichette.
Diremo che $R: N_1 \times N_2$ è una bisimulazione tra $G_1, G_2$ se
+ $R(a,b) \implies l_1(a) = l_2(b)$
+ punti 2,3 della bisimulazione (sono validi perchè non si chiede che esistano rami tra a,b o tra c,d)
+ $\forall \,\, a \in N_1 \,\, \exists \,\, b \in N_2 : R(a,b)$
+ $\forall \,\, b \in N_2 \,\, \exists \,\, a \in N_1 : R(a,b)$

### Partizione
Sia $E$ un insieme. Diremo che $\Sigma$, un insieme di sosttoinsiemi di $E$, è una partizione di $E$, se $\forall \alpha, \beta \in \Sigma$ si ha che $\alpha \cap \beta = \emptyset$

### Rifinitura di una partizione
Diremo che la partizione $\Sigma$ rifinisce la partizione $M$ se per ogni blocco $\alpha$ di $\Sigma$ si ha che $\alpha \subset a$ per un blocco di $M$.

### Relazione inversa
Sia $R \subset U\times U$ (cioè $R$ è una relazione binaria su $U$). Sia $S \subset U$.
$$\begin{gathered}
E(S) = \{y : \exists x \in U : R(x,y)\}\\
E^{-1}(s) = \{x : \exists y \in U : R(x,y)\}
\end{gathered}$$

### Partizione stabile
Diremo che una partizione $\Sigma$ è stabile rispetto ad una relazione binaria $R$ se $\forall \alpha, \beta \in \Sigma$ vale uno dei seguenti punti ($R^{-1}$ è inteso come relazione inversa di $R$)
+ $\alpha \cap R^{-1}(\beta) = \emptyset$
+ $\alpha \subset R^{-1}(\beta)$

Supponendo che $R^{-1}(\beta)$ significhi "l'insieme dei nodi a tali che esiste un $b \in \beta$ tale che $R(a,b)$, il significato del secondo punto è "$\alpha$ è interamente contenuto nell'insieme $R^{-1}(\beta)$, cioè tutti gli $a \in \alpha$ hanno la proprietà di essere in relazione con qualche $b \in \beta$ (in particolare devono essere i primi membri della relazione)".
Si può immaginare $R = \to$, quindi in questo caso da tutti gli $a \in \alpha$ parte un nodo verso almeno un $b \in \beta$. E' evidente che i blocchi $\alpha, \beta$ sono "molto connessi".

### Strongly connected component
Un grafo è "strongly connected" se per ogni coppia di nodi a,b esiste un percorso per andare da a a b. Un grafo può essere suddiviso in SCC, in cui i sottografi sono strongly connected. Ogni SCC può essere considerato un nodo, quindi si ottiene un nuovo grafo in cui i nodi sono i SCC, ed i rami sono i rami che legano i singoli nodi tra due SCC.

### Well-Founded part
Sia $G(N, \to)$ un grafo. Sia $G(a)$ l'insieme di tutti i nodi raggiungibili partendo dal nodo a.
Allora 
$$\begin{gathered} WF(G) = \{a \in N : G(a) \text{ non contiene cicli} \} \end{gathered}$$.
