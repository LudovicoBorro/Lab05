from database.corso_DAO import DAO as CorsoDao
from database.studente_DAO import DAO as StudenteDAO
from database.iscrizione_DAO import DAO as IscrizioneDao

class Model:

    def __init__(self):
        pass

    @staticmethod
    def getAllCorsi():
        return CorsoDao.getAllCorsi()

    @staticmethod
    def getAllStudentiCorso(codins):
        return StudenteDAO.getAllStudentiCorso(codins)

    @staticmethod
    def getStudente(matricola):
        return StudenteDAO.getStudente(matricola)

    @staticmethod
    def getCorsiStudente(matricola):
        return CorsoDao.getCorsiStudente(matricola)

    @staticmethod
    def insertIscrizione(matricola, codins):
        return IscrizioneDao.insertIscrizione(matricola, codins)