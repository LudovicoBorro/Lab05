from database.corso_DAO import DAO as CorsoDao
from database.studente_DAO import DAO as StudenteDAO

class Model:

    def __init__(self):
        pass

    def getAllCorsi(self):
        return CorsoDao.getAllCorsi()

    def getAllStudentiCorso(self, codins):
        return StudenteDAO.getAllStudentiCorso(codins)

    def getStudente(self, matricola):
        return StudenteDAO.getStudente(matricola)