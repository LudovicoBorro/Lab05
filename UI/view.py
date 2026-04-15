import flet as ft
from flet import MainAxisAlignment

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab 05 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddCorso = None
        self._btnCercaIscritti = None
        self._txtMatricola = None
        self._txtNome = None
        self._txtCognome = None
        self._btnCercaStudente = None
        self._btnCercaCorsi = None
        self._btnIscrivi = None
        self._list_view = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text(value="App Gestione Studenti", text_align=ft.TextAlign.CENTER, color="blue", size=24)
        self._page.add(self._title)

        #ROW with some controls
        self._ddCorso = ft.Dropdown(label="Corso", width=1000)
        self._controller.fillddCorsi()
        self._btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handleCercaIscritti, width=200)

        row1 = ft.Row(controls=[self._ddCorso, self._btnCercaIscritti], alignment=MainAxisAlignment.CENTER)

        self._txtMatricola = ft.TextField(label="Matricola", hint_text="Matricola", width=300)
        self._txtNome = ft.TextField(label="Nome", hint_text="Nome", width=400, read_only=True)
        self._txtCognome = ft.TextField(label="Cognome", hint_text="Cognome", width=400, read_only=True)

        row2 = ft.Row(controls=[self._txtMatricola, self._txtNome, self._txtCognome], alignment=MainAxisAlignment.CENTER)

        self._btnCercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handleCercaStudente, width=200)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handleCercaCorsi, width=200)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrivi, width=200)

        row3 = ft.Row(controls=[self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi], alignment=MainAxisAlignment.CENTER)

        self._page.add(row1,row2, row3)
        # text field for the name

        # List View where the reply is printed
        self._list_view = ft.ListView(expand=1,spacing=10,padding=20,auto_scroll=True)
        self._page.controls.append(self._list_view)
        self.update_page()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
