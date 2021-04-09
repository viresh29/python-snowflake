import snowflake.connector
from abc import ABC, abstractmethod, ABCMeta


class SFQueryExecution:
    __metaclass__ = ABCMeta

    def __init__(self, account, username, password, warehouse, timeout_counter, timeout_sleep, **kwargs):
        super(SFQueryExecution, self).__init__()
        self.account = account
        self.username = username
        self.password = password
        self.warehouse = warehouse
        self.timeout_counter = timeout_counter
        self.timeout_sleep = timeout_sleep
        self.connection_status = False
        self.cs = None
        self.db_structure = dict(**kwargs)

    def _db_connection(self):

        connection = snowflake.connector()

    def execute_dml_statement(self, query, commit, return_data, close_connection):
        pass

    def _execute_statement(self, statement):
        try:
            self.cs.execute(statement)
        except:
            self.cs.execute("rollback;")
