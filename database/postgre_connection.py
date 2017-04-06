import psycopg2


class PostgreConnection:
    """
    Class used to connect on database and return the connection object
    """
    database_dict = dict(line.strip().split('=') for line in open('database.properties'))

    connection = None

    @staticmethod
    def get_connection():
        """
        Method that returns the open connection to the database
        :return: Connection
        """
        try:
            if not PostgreConnection.connection:
                connection = psycopg2.connect(
                    host=PostgreConnection.database_dict.get("hostname"),
                    user=PostgreConnection.database_dict.get("username"),
                    password=PostgreConnection.database_dict.get("password"),
                    dbname=PostgreConnection.database_dict.get("database"))
        except:
            print "Cannot to connect to the database: " + \
                  PostgreConnection.database_dict.get("database")

        return connection