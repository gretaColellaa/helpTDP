def fillDD():
    for n in sorted(self._model._nodes):
        # print(n)
        self._view.ddLocal.options.append(ft.dropdown.Option(n))

def handle_graph():
    self._model.creaGrafo()
    self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumNodes()} nodi"
                                                  f" e {self._model.getNumEdges()} archi"))
#ESEMPIO PER HANDLE_CAMMINO
    def handle_cammino(self, e):
        localization = self._view.ddLocal.value

        path = self._model.cerca_cammino(localization)
        self._view.txt_result.controls.append(ft.Text(f"Il cammino più lungo dal nodo : {localization} è:"))

        for n in path[0]:
            self._view.txt_result.controls.append(ft.Text(f"{n}"))

        self._view.txt_result.controls.append(ft.Text(f"con peso: {path[1]}"))
        self._view.update_page()