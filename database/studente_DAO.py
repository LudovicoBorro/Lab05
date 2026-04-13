# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBConnect
from model.studente import Studente

class DAO:

    def __init__(self):
        pass

    @staticmethod
    def getAllStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
            select s.*
            from iscrizione i, studente s
            where i.matricola = s.matricola and i.codins = %s
        """

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudente(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                select *
                from studente s 
                where s.matricola = %s
                """

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res