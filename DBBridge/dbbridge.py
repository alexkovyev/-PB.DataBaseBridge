import psycopg2
from .DbCon.dbconfig import dbconfig


class BridgeError(Exception):
    def __init__(self, query, params, error):
        self.query = query
        self.params = params
        self.error = error

    def __str__(self):
        return "Query: {query}\nParams: {params}\nError: {error}".format(
            query=self.query,
            params=self.params,
            error=self.error.__str__()
        )


class db_bridge():

    connection_timeout_sec = 5

    def __init__(self):
        self.__conn = None
        self.__cur = None
        self.__init_db_connection()

    def __del__(self):
        if self.__conn:
            self.__conn.close()

    def __init_db_connection(self):
        conn_params = dbconfig.to_dict()
        self.__conn = psycopg2.connect(user=conn_params['dbuser'],
                                       password=conn_params['dbpassword'],
                                       host=conn_params['dbhost'],
                                       port=conn_params['dbport'],
                                       database=conn_params['dbname'],
                                       connect_timeout=db_bridge.connection_timeout_sec)

    def execute(self, proc_name, param_list=None):
        try:
            self.__cur = self.__conn.cursor()

            sql = self.__invoke_db_proc(proc_name, len(param_list))
            self.__cur.execute(sql, param_list)
            self.__conn.commit()

            return self.__cur.fetchall()

        except (Exception, psycopg2.Error) as error:
            raise BridgeError(proc_name, param_list, error)

        finally:
            if self.__cur:
                self.__cur.close()

    def __invoke_db_proc(self, proc_name, param_list_len):
        sql = "SELECT *\nFROM %s(" % proc_name
        for i in range(param_list_len):
            if i > 0:
                sql = sql + ", "
            sql = sql + '%s'
        sql = sql + ")"

        return sql
