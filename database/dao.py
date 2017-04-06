from database.postgre_connection import PostgreConnection


class DAO:
    """
    Class that represents the Data Access Object pattern in a simple way
    """
    @staticmethod
    def execute_fetch_one(query, *params):
        """
        Fecth data based on query and params, return a single result
        :param query: Query 
        :param params: Args
        :return: Single result
        """
        connection = PostgreConnection.get_connection()

        cursor = connection.cursor()
        cursor.execute(query, *params)
        return cursor.fetchone()

    @staticmethod
    def execute_fetch_all(query, *params):
        """
        Fetch data based on query and params, return a list of results
        :param query: Query
        :param params: Args
        :return: List of results
        """
        connection = PostgreConnection.get_connection()

        cursor = connection.cursor()
        cursor.execute(query, *params)

        return cursor.fetchall()

    @staticmethod
    def execute_not_read_only_query(query, *params):
        """
        Execute not read only queries, such as: inserts, updates, deletes
        :param query: Query
        :param params: Args        
        """
        connection = PostgreConnection.get_connection()

        cursor = connection.cursor()
        cursor.execute(query, *params)

        connection.commit()

    @staticmethod
    def execute_not_read_only_queries(queries):
        """
        Uses a dictionary having:
        KEY = query
        VALUE = params
        to execute queries in a single transaction, the commit is executed 
        at the final of all queries 
        :param queries: Dictionary = {Query:Params}
        """
        connection = PostgreConnection.get_connection()

        cursor = connection.cursor()
        for key in queries.keys():
            cursor.execute(key, queries[key])

        connection.commit()