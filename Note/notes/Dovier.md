---
tags: [tesi]
title: Dovier
created: '2020-07-26T07:12:00.794Z'
modified: '2020-08-03T13:28:34.151Z'
---

# Dovier

## Rappresentazione di insiemi con grafi
Possiamo identificare la relazione $a \to b$ come $b \in/\subset a$. Quindi un ciclo rappresenta un insieme che contiene se stesso.

## Accessible pointed graph (APG)
E' un grafo direzionato $G$ con un nodo $v$ distinto ($<G,v>$) tale che tutto $G$ è raggiungibile da $v$.

## Bisimulazione tra APG
Diremo che due APG $<G_1, v_1>,<G_2, v_2>$ sono in bisimulazione se $\exists b : b$ è una bisimulazione tra $G_1, G_2$ e $v_1 b v_2$. 

## Due APG rappresentano lo stesso hyperset $\iff$ sono bisimili
La definizione di bisimulazione per due APG può essere letta come una relazione di (bi-)similitudine tra nodi che "si comportano allo stesso modo". Cioè, diremo che due grafi $G_1 = (N_1, V_1), G_2 = (N_2, V_2)$ sono bisimili secondo $b$ se
1. $\forall u_1, v_1 \in N_1, u_2 \in N_2, (u_1 \to v_1 \land u_1 b u_2) \implies \exists v_2 : (u_2 \to v_2, v_1 b v_2)$
2. Viceversa

Allora i nodi che intervengono si "comportano allo stesso modo": quando $u_1 \to v_1$ (leggi: $v_1 \subset u_1$), se $u_1 b u_2$ (leggi: $u_1, u_2$ sono bisimili, rappresentano lo stesso insieme all'interno della gerarchia di insiemi rappresentata dai grafi $G_1, G_2$) allora anche $v_1 b v_2$, perchè rappresentano lo stesso insieme, ed essendo una diversa rappresentazione dello stesso insieme devono comportarsi allo stesso modo (cioè sono bisimili). Inoltre essendo che la gerarchia $u_1 \to v_1 \equiv v_1 \subset u_1$ è la stessa gerarchia di insiemi in entrambi i grafi, si deve avere anche che $u_2 \to v_2 \equiv v_2 \subset u_2$.

## Bisimulazione massima su APG
Dato un APG $<G,v>$ esiste sempre la bisimulazione massima, e questa è una relazione di equivalenza sull'insieme dei nodi di $G$. La bisimulazione massima è l'unione di tutte le bisimulazioni.

Allora possiamo "collassare" i nodi di $G$ in insiemi di nodi equivalenti (secondo la relazione di bisimulazione). Questa si dice "contrazione per bisimulazione".

## APG in bisimulazione $\iff$ determinazione della bisimulazione massima
Due APG $A_1 = <(N_1, E_1), v_1>, A_2 = <(N_2, E_2), v_2>$ sono in bisimulazione $\iff v_1 \equiv v_2$, dove $\equiv$ è la bisimulazione massima su $$A_3 = <(N_1 \cup N_2 \cup \{\alpha\}, E_1 \cup E_2 \cup \{(\alpha, v_1), (\alpha, v_2)\}), \alpha>$$

### Dimostrazione
Il lato $\impliedby$ è banale.
Suppongo che $A_1,A_2$ siano in bisimulazione. Sia $b$ l'unione di tutte le bisimulazioni tra $A_1,A_2$. Vale sicuramente $v_1 b v_2$ perchè abbiamo supposto che $A_1,A_2$ siano in bisimulazione. Sia $b' = b \cup (\alpha,\alpha)$. $b'$ è ancora una bisimulazione, infatti vale $$\alpha b' \alpha \land (\alpha, v_1) \land ((\alpha, v_2) \land v_1 b' v_2)$$
Allora se considero $\equiv$ la bisimulazione massima su $A_3$ (che contiene $b'$) si deve avere $v_1 \equiv v_2$.

## Bisimulazione $\iff$ Stable partition problem
Sia $G = <N,E>$ un grafo. $E$ è una relazione binaria per cui vale $v_1 E v_2 \iff (v_1, v_2)$.
1. Sia $P$ una partizione di $N$ stabile rispetto a $E$. Allora la relazione binaria su $N$ definita come $$v_1 b_p v_2 \iff \exists B \in P : (v_1 \in B \land v_2 \in B)$$ è una bisimulazione.
2. Sia $b$ una bisimulazione che è anche una relazione di equivalenza. Allora la partizione di $N$ definita dalle classi di equivalenza di $b$ è una partizione stabile rispetto a $E$.

### Dimostrazione
1. Siano $v_1,v_2$ due nodi nella stessa partizione $B_1$. Sia $u_1 : (v_1, u_1)$. Sia $B_2 \in P : u_1 \in B_2$. Per definizione di stabilità si può avere alternativamente che
    1. $B_1 \cap E^{-1}(B_2) = \emptyset$. Ma questo è assurdo perchè per ipotesi esiste un ramo $(v_1, u_1), v_1 \in B_1, u_1 \in B_2$
    2. $B_1 \subset E^{-1}(B_2) \implies \exists u_2 \in B_2 : (v_2, u_2)$ (può essere anche $u_2 = u_1$)
Quindi $(v_1 b_p v_2 \land (v_1, u_1) \implies \exists u_2 : (u_1 b_p u_2 \land (v_2, u_2))) \implies b_p$ è una bisimulazione su $G$.
2. Sia $v_1 \in B_1$. Sia $u_1 \in B_2$. Si possono avere due casi
    1. $\nexists (v_1, u_1) \implies B_1 \cap E^{-1}(B_2) = \emptyset$
    2. $(v_1, u_2)$. Sia $v_2 \in B_1$ (eventualmente va bene anche $v_1 = v_2$). Allora $(v_1 b v_2 \land (v_1, u_1)) \implies \exists u_2 \in N : ((v_2, u_2), u_1 b u_2) \implies u_2 \in B_2$. Allora l'esistenza di un ramo tra due nodi di partizioni differenti $B_1, B_2$ induce l'esistenza di un ramo tra un altro nodo qualsiasi di $B_1$ ed almeno un altro nodo di $B_2$. Quindi $B_1 \subset E^{-1}(B_2)$.

### Osservazione
La bisimulazione che induce una partizione stabile non ha apparentemente alcun legame logico con la relazione $E$, ma questo legame è dato dalla definizione stessa di bisimulazione (la bisimulazione tra due nodi implica una relazione di raggiungibilità tra questi nodi ed altri del grafo).

## Massima bisimulazione $\iff$ Coarsest stable partition problem
1. Suppongo di avere la massima bisimulazione. Questa induce una partizione stabile su $N$. Suppongo che non sia la coarsest. Allora posso trovarne una più coarsest. Ma questa induce una bisimulazione in cui più elementi sono in relazione. Quindi la bisimulazione iniziale non è massima.
2. Suppongo di avere la coarsest stable partition. Questa induce una bisimulazione. Suppongo che non sia massima. Allora posso trovarne una massima, che induce una partizione più coarsest, perchè più elementi sono in relazione secondo la bisimulazione massima. Allora la partizione non è la coarsest.

## Rango
$$rank(u) = \begin{cases}
0 \qquad \text{se } u \text{ è una foglia}\\
1 + \max(rank(v) : (u,v))
\end{cases}$$

## Proposizione 4.2
### $u \equiv v \implies rank(u) = rank(v)$ (dove $\equiv$ è la bisimulazione massima)
### Dimostrazione
Per induzione su $rank(u)$:
+ Se $u$ è una foglia, e $u \equiv v$, allora se p.a. $\exists c : v \to c$ (e quindi se $v$ non fosse una foglia) $\implies \exists d : u \to d \implies u$ non è una foglia. Ma questo è chiaramente assurdo, allora anche $v$ è una foglia $\implies rank(v) = rank(u) = 0$.
+ Suppongo che la proposizione sia vera per $rank(u) = n - 1$. Suppongo che $u \equiv v \land rank(u) = n$. Per la definizione di $rank$ tra i nodi $n \in N : u \to n$ deve esisterne uno tale che $rank(u) = n - 1$. Per definizione di bisimulazione, $(u \to n \land u \equiv v) \implies \exists m : (v \to m \land n \equiv m) \implies rank(m) = rank(n) = n - 1$.
Suppongo p.a. che $\exists x : v \to x \land rank(x) = w > n - 1$. In questo caso assurdo $rank(v) = w + 1 \neq n$, e quindi la proposizione non sarebbe verificata. Ma in questo caso, per definizione di bisimulazione, dovrebbe esistere un nodo $y : u \to y \land x \equiv y$. Ma per definizione di $rank$ deve valere $rank(y) \leq n - 1$, e per la simmetria di $\equiv$ deve valere $n - 1 \geq rank(y) = rank(x) = w > n - 1$, che è assurdo.

## Lemma 4.4a
### $u \not\equiv v$ e $rank(u) = rank(v) \implies u,v$ finiscono in blocchi diversi all'iterazione $i$-esima del ciclo in (5)
### Dimostrazione
Per induzione su $i$
1. Tutti i nodi di rango 0/1 sono bisimili.
2. Suppongo di avere due nodi $u,v$ con $rank(u) = rank(v) = n, u \not\equiv v \implies$ ad esempio $\exists u' : u \to u'$ ma $\forall v' : v \to v'$ si ha $u' \equiv v'$.
Ma per l'ipotesi induttiva $\forall v' \,\,u', v'$ sono stati inseriti in blocchi differenti da un'iterazione precedente, e quando le classi di rango superiore (tra cui quella di rango n) sono state "splittate" rispetto alle due classi in cui sono stati messi $u',v'$ i nodi $u,v$ finiscono in classi necessariamente diverse, perchè $v \to v'$, ma per nessun nodo $u''$ nella stessa classe in cui finisce $v'$ si può dire che $u \to u''$.
