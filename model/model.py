from database.corso_DAO import DAO

class Model:

    def __init__(self):
        pass

    def getAllCorsi(self):
        return DAO.getAllCorsi()