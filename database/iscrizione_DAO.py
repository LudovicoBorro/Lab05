from database.DB_connect import DBConnect

class DAO:

    def __init__(self):
        pass

    @staticmethod
    def insertIscrizione(matricola, codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """
        insert into iscrizione (matricola, codins)
        values (%s, %s)
        """

        cursor.execute(query, (matricola, codins))
        cnx.commit()

        cursor.close()
        cnx.close()
        return True