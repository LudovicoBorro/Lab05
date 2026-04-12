import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCercaIscritti(self, e):
        pass

    def handleCercaStudente(self, e):
        pass

    def handleCercaCorsi(self, e):
        pass

    def handleIscrivi(self, e):
        pass

    def fillddCorsi(self):
        for corso in self._model.getAllCorsi():
            self._view._ddCorso.options.append(
                ft.dropdown.Option(key=corso.codins, text=corso.__str__())
            )