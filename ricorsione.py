
import copy
import random


#CERCA CAMMINO MASSIMO IN TERMINI DI PESO DEGLI ARCHI, CON SOURCE
#NON ORIENTATO!!!!!!!!!!!!!1
#30-6-2021
def cerca_cammino(self, partenza):
    self._best_cammino = []
    self._best_peso = 0
    self._ricorsione([partenza], 0, {partenza})
    return self._best_cammino, self._best_peso


def _ricorsione(self, cammino_parziale, peso_parziale, visited):
    ultimo = cammino_parziale[-1]

    # Caso finale: aggiorna se questo cammino è migliore
    if peso_parziale > self._best_peso:
        self._best_peso = peso_parziale
        self._best_cammino = list(cammino_parziale)

    for vicino in self._grafo.neighbors(ultimo):
        if vicino not in visited:
            peso = self._grafo[ultimo][vicino]['weight']

            visited.add(vicino)
            cammino_parziale.append(vicino)

            self._ricorsione(cammino_parziale, peso_parziale + peso, visited)

            # Backtrack
            visited.remove(vicino)
            cammino_parziale.pop()
#SENZA SOURCE
def getLongestPathByWeight(self):
    self._bestPath = []
    self._bestWeight = 0

    for nodo in self.grafo.nodes:
        self._ricorsionePeso([nodo], 0)

    return self._bestWeight, self._bestPath
def _ricorsionePeso(self, parziale, pesoParziale):
    if pesoParziale > self._bestWeight:
        self._bestWeight = pesoParziale
        self._bestPath = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for vicino in self.grafo.neighbors(ultimo):
        if vicino not in parziale:
            peso = self.grafo[ultimo][vicino]["weight"]
            parziale.append(vicino)
            self._ricorsionePeso(parziale, pesoParziale + peso)
            parziale.pop()




#CERCA CAMMINO MASSIMO IN TERMINI DI NUMERO DEGLI ARCHI, CON SOURCE
#NON ORIENTATO!!!!!!!!!!!!!!!
def getLongestPathByLength(self, nodoPartenza):
    self._soluzione = []
    self._ricorsione_length([nodoPartenza])
    return len(self._soluzione) - 1, self._soluzione
def _ricorsione_length(self, parziale):
    if len(parziale) > len(self._soluzione):
        self._soluzione = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for vicino in self.grafo.neighbors(ultimo):
        if vicino not in parziale:
            parziale.append(vicino)
            self._ricorsione_length(parziale)
            parziale.pop()

                #NEL CONTROLLER ESEMPIO
                # lunghezza, cammino = self._model.getLongestPathByLength(l)
                # self._view.txt_result.controls.append(ft.Text(f"Cammino più lungo da {l}:"))
                # for nodo in cammino:
                #     self._view.txt_result.controls.append(ft.Text(f"- {nodo}"))
                # self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {lunghezza}"))

#SENZA SOURCE
def getLongestPathByLength(self):
    self._bestPath = []

    for nodo in self.grafo.nodes:
        self._ricorsioneLunghezza([nodo])

    return len(self._bestPath) - 1, self._bestPath
def _ricorsioneLunghezza(self, parziale):
    if len(parziale) > len(self._bestPath):
        self._bestPath = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for vicino in self.grafo.neighbors(ultimo):
        if vicino not in parziale:
            parziale.append(vicino)
            self._ricorsioneLunghezza(parziale)
            parziale.pop()


#CERCA CAMMINO MASSIMO IN TERMINI DI PESO DEGLI ARCHI, CON SOURCE
#ORIENTATO!!!!!!!!!!!!!!!!!!!
def getLongestPathByWeight(self, nodoPartenza):
    self._bestPath = []
    self._bestWeight = 0
    self._ricorsionePeso([nodoPartenza], 0)
    return self._bestWeight, self._bestPath


def _ricorsionePeso(self, parziale, pesoParziale):
    if pesoParziale > self._bestWeight:
        self._bestWeight = pesoParziale
        self._bestPath = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for succ in self.grafo.successors(ultimo):
        if succ not in parziale:
            peso = self.grafo[ultimo][succ]["weight"]
            parziale.append(succ)
            self._ricorsionePeso(parziale, pesoParziale + peso)
            parziale.pop()

#SENZA SOURCE
def getLongestPathByWeight(self):
    self._bestPath = []
    self._bestWeight = 0

    for nodo in self.grafo.nodes:
        self._ricorsionePeso([nodo], 0)

    return self._bestWeight, self._bestPath

def _ricorsionePeso(self, parziale, pesoParziale):
    if pesoParziale > self._bestWeight:
        self._bestWeight = pesoParziale
        self._bestPath = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for succ in self.grafo.successors(ultimo):
        if succ not in parziale:
            peso = self.grafo[ultimo][succ]["weight"]
            parziale.append(succ)
            self._ricorsionePeso(parziale, pesoParziale + peso)
            parziale.pop()




#CERCA CAMMINO MASSIMO IN TERMINI DI NUMERO DEGLI ARCHI, CON SOURCE
#ORIENTATO!!!!!!!!!!!!!!!
def getLongestPathByLength(self, nodoPartenza):
    self._bestPath = []
    self._ricorsioneLunghezza([nodoPartenza])
    return len(self._bestPath) - 1, self._bestPath
def _ricorsioneLunghezza(self, parziale):
    if len(parziale) > len(self._bestPath):
        self._bestPath = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for succ in self.grafo.successors(ultimo):
        if succ not in parziale:
            parziale.append(succ)
            self._ricorsioneLunghezza(parziale)
            parziale.pop()

#SENZA SOURCE
def getLongestPathByLength(self):
    self._bestPath = []

    for nodo in self.grafo.nodes:
        self._ricorsioneLunghezza([nodo])

    return len(self._bestPath) - 1, self._bestPath


def _ricorsioneLunghezza(self, parziale):
    if len(parziale) > len(self._bestPath):
        self._bestPath = copy.deepcopy(parziale)

    ultimo = parziale[-1]
    for succ in self.grafo.successors(ultimo):
        if succ not in parziale:
            parziale.append(succ)
            self._ricorsioneLunghezza(parziale)
            parziale.pop()









#SIMULAZIONE CON PROBABILITA' DI EVENTI
#24-2-21
    def simula(self, N):
        self._best_team = self._idMapPlayers[self._bestP][0]
        g_h = 11
        g_a = 11
        t_h = DAO.getTeams(self._match)[0]["TeamHomeID"]
        t_a = DAO.getTeams(self._match)[0]["TeamAwayID"]

        self._azioni[t_h] = []
        self._azioni[t_a] = []

        self.ricorsione(N, g_h, g_a, t_h, t_a)
        goal_th = 0
        es_th = 0
        goal_ta = 0
        es_ta = 0

        for a in self._azioni[t_h]:
            if a == "GOAL":
                goal_th += 1
            if a == "ESPULSO":
                es_th += 1

        for a in self._azioni[t_a]:
            if a == "GOAL":
                goal_ta += 1
            if a == "ESPULSO":
                es_ta += 1

        return (t_h, goal_th, es_th), (t_a, goal_ta, es_ta)

    def ricorsione(self, N, g_h, g_a, t_h, t_a):
        N = int(N)

        if N == 0:
            return self._azioni, g_h, g_a
        else:
            i = random.randint(1, 100)
            if i <= 50:
                if g_h > g_a:
                    self._azioni[t_h].append("GOAL")
                elif g_h < g_a:
                    self._azioni[t_a].append("GOAL")
                else:
                    if self._best_team == t_h:
                        self._azioni[t_h].append("GOAL")
                    else:
                        self._azioni[t_a].append("GOAL")
                N = N - 1


            elif i > 50 and i <= 80:
                teams = [t_h, t_a]
                if self._best_team == t_h:
                    prob = [0.6, 0.4]
                else:
                    prob = [0.4, 0.6]

                espulso = random.choices(teams, weights=prob, k=1)[0]
                self._azioni[espulso].append("ESPULSO")
                if espulso == t_h:
                    g_h = g_h - 1

                else:
                    g_a = g_a - 1

                N = N + random.randint(2, 2)
            else:
                infortunio = random.choice(self._nodes)
                team = self._idMapPlayers[infortunio]
                if t_h == team:
                    g_h = g_h - 1
                else:
                    g_a = g_a - 1
                N = N - 1

            self.ricorsione(N, g_h, g_a, t_h, t_a)

# Trovare il cammino semplice più lungo (massimo numero di archi), tenendo conto del verso degli archi, con:
# Nodo di partenza: nessun arco entrante → grafo.in_degree(n) == 0
# Nodo di arrivo: nessun arco uscente → grafo.out_degree(n) == 0
# Vertici intermedi: cammino semplice orientato, tutti i nodi adiacenti.
# Massima lunghezza in termini di numero di archi.
#ORIENTATO!!!!!
#24-1-21
def getCamminoMaxLunghezza(self):
    self._bestPath = []

    for nodo in self.grafo.nodes:
        if self.grafo.in_degree(nodo) == 0:
            self._ricorsione([nodo])

    return len(self._bestPath) - 1, self._bestPath
def _ricorsione(self, parziale):
    ultimo = parziale[-1]

    # Se non ha successori (out-degree == 0)
    if self.grafo.out_degree(ultimo) == 0:
        if len(parziale) > len(self._bestPath):
            self._bestPath = copy.deepcopy(parziale)
        return

    for succ in self.grafo.successors(ultimo):
        if succ not in parziale:
            parziale.append(succ)
            self._ricorsione(parziale)
            parziale.pop()


