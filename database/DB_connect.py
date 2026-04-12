import mysql.connector
from mysql.connector import errorcode

class DBConnect:

    def __init__(self):
        raise RuntimeError('Do not create an instance, use the class method get_connection()!')

    @classmethod
    def get_connection(cls) -> mysql.connector.connection:
        try:
            cnx = mysql.connector.connect(
                option_files='./database/connector.cnf'
            )
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return None
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return None
            else:
                print(err)
                return None
