from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from abc import ABC, abstractmethod


class DBEngine(ABC):
    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def close(self):
        pass


class SnowFlakeEngine(DBEngine):
    def __init__(self, account, user, warehouse, database, password=None):
        self.account = account
        self.user = user
        self.warehouse = warehouse
        self.database = database
        self.password = password
        self.engine = None

    def get_engine(self):
        self.engine = create_engine(URL(
            account=self.account,
            user=self.user,
            warehouse=self.warehouse,
            database=self.database
            ),
            connect_args={'authenticator': 'externalbrowser'}
            )
        return self.engine

    def close(self):
        self.engine.dispose()
