import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._corsi = {}

    def handleCercaIscritti(self, e):
        self._view._list_view.controls.clear()

        if self._view._ddCorso.value is None:
            self._view.create_alert("Selezionare un corso!")
            self._view.update_page()
            return

        studenti = self._model.getAllStudentiCorso(self._view._ddCorso.value)
        print(f"Numero studenti del corso: {len(studenti)}")

        if not len(studenti):
            self._view._list_view.controls.append(
                ft.Text("Nessuno studenti iscritto a questo corso")
            )
            self._view.update_page()
            return

        self._view._list_view.controls.append(
            ft.Text(f"Ci sono {len(studenti)} iscritti al corso {self._corsi.get(self._view._ddCorso.value)}")
        )

        for studente in studenti:
            self._view._list_view.controls.append(
                ft.Text(studente)
            )

        self._view.update_page()

    def handleCercaStudente(self, e):
        self._view._list_view.controls.clear()

        matricola = self._view._txtMatricola.value

        if not self._check_corsi(matricola):
            return

        matricola = int(matricola)

        studente = self._model.getStudente(matricola)

        if not self._check_studente(studente):
            return

        self._view._txtNome.value = studente[0].nome
        self._view._txtCognome.value = studente[0].cognome
        self._view.update_page()

    def handleCercaCorsi(self, e):
        self._view._list_view.controls.clear()

        matricola = self._view._txtMatricola.value

        if not self._check_matricola(matricola):
            return

        matricola = int(matricola)

        corsi = self._model.getCorsiStudente(matricola)

        if not self._check_corsi(corsi):
            return

        self._view._list_view.controls.append(
            ft.Text(f"Risultano {len(corsi)} corsi:")
        )

        for c in corsi:
            self._view._list_view.controls.append(
                ft.Text(c)
            )

        self._view.update_page()

    def handleIscrivi(self, e):
        self._view._list_view.controls.clear()

        matricola = self._view._txtMatricola.value
        cod_corso = self._view._ddCorso.value

        if not self._check_matricola(matricola):
            return

        matricola = int(matricola)

        if cod_corso is None:
            self._view.create_alert("Selezionare un corso!")
            self._view.update_page()
            return

        if self._model.insertIscrizione(matricola, cod_corso):
            self._view._list_view.controls.append(
                ft.Text("Iscrizione avvenuta con successo!", color="green")
            )
        else:
            self._view._list_view.controls.append(
                ft.Text("L'iscrizione non è andata a buon fine!", color="red")
            )

        self._view.update_page()

    def fillddCorsi(self):
        for corso in self._model.getAllCorsi():
            self._view._ddCorso.options.append(
                ft.dropdown.Option(key=corso.codins, text=corso.__str__())
            )
            self._corsi[corso.codins] = corso

    def _check_matricola(self, matricola):

        if matricola is None:
            self._view.create_alert("Inserire una matricola!")
            self._view.update_page()
            return False

        try:
            matricola = int(matricola)
        except ValueError:
            self._view.create_alert("Attenzione! Inserire una matricola valida!")
            self._view.update_page()
            return False

        return True

    def _check_studente(self, studente):

        if len(studente) == 0:
            self._view.create_alert("Matricola non esistente!")
            self._view.update_page()
            return False

        if len(studente) > 1:
            self._view.create_alert("Errore! Trovati più studenti con la stessa matricola!")
            self._view.update_page()
            return False

        return True

    def _check_corsi(self, corsi):

        if len(corsi) == 0:
            self._view.create_alert("Lo studente inserito non è iscritto a nessun corso")
            self._view.update_page()
            return False

        return True