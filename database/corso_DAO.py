# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso


class DAO:

    def __init__(self):
        pass

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
            select *
            from corso
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiStudente(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
            select c.*
            from corso c, iscrizione i 
            where c.codins = i.codins and i.matricola = %s      
        """

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res