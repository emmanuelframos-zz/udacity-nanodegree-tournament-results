import psycopg2


class PostgreConnection():
    """
    Class used to connect on database and return the connection object
    """

    hostname = 'localhost'
    username = 'postgres'
    password = '4dm1n'
    database = 'TOURNAMENT'
    connection = None

    @staticmethod
    def get_connection():
        """
        Method that returns the open connection to the database
        :return: Connection
        """
        if not PostgreConnection.connection:
            try:
                connection = psycopg2.connect(host=PostgreConnection.hostname,
                                              user=PostgreConnection.username,
                                              password=PostgreConnection.password,
                                              dbname=PostgreConnection.database)
            except:
                print "Cannot to connect to the database: " + PostgreConnection.database

        return connection