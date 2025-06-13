#GET BEST - DIFFERENZA PESI USCENTI E ENTRANTI
#24-2-21
def getBest(self):
    best = 0
    self._bestP = None

    for p in self._nodes:

        peso_uscenti = sum(data["weight"] for _, _, data in self._grafo.out_edges(p, data=True))
        peso_entranti = sum(data["weight"] for _, _, data in self._grafo.in_edges(p, data=True))
        risultato = peso_uscenti - peso_entranti
        if risultato > best:
            best = risultato
            self._bestP = p

    # peso_uscenti = sum(data["weight"] for _, _, data in G.out_edges(nodo, data=True))
    #
    # # Somma dei pesi degli archi entranti
    # peso_entranti = sum(data["weight"] for _, _, data in G.in_edges(nodo, data=True))
    #
    # # Calcolo richiesto
    # risultato = peso_uscenti - peso_entranti

    return self._bestP, best

#CALCOLA STATISTICHE - NODI CONNESSI A QUELLO SELEZIONATO (l) , VISUALIZZANDO IL PESO DELL'ARCO
#NON ORIENTATO!!
#30-6-21
def calcolaStatistiche(self, l):

    archi = self._grafo.edges(l, data=True)
    stat = []
    for a in archi:
        u,v,w = a[0],a[1],a[2]["weight"]
        if l == u:
            stat.append((v,w))
        elif l == v:
            stat.append((u,w))

    return stat


#PIU REDDITIZI (5) -> VERTICI CON MAX_N ARCHI ENTRANTI E 0 USCENTI
#ORIENTATO!!!
#24-1-24
def piuRedditizi(self):
    dizio = {}
    for nodo in self.grafo.nodes:
        if self.grafo.out_degree(nodo) == 0:
            dizio[nodo] = self.grafo.in_degree(nodo)

    print(len(dizio))

    dizioInOrder = dict(sorted(dizio.items(), key=lambda item: item[1], reverse=True))
    top5 = list(dizioInOrder.keys())[:5]
    top5def = []
    for i in top5:
        top5def.append(self._idMapProdotti[i.Product_number])

    print(len(top5def))

    return top5def

