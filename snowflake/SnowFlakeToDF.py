from datetime import timedelta
import pandas as pd


class DF:
    def __init__(self, db_engine, querypath, filename):
        self.db_engine = db_engine
        self.querypath = querypath
        self.filename = filename

    def read_sql(self, query):
        database_engine = self.db_engine.get_engine()
        for query in query.rstrip().split(';'):
            if query:
                df = pd.read_sql(query, database_engine)
        self.db_engine.close()

        return df

    @staticmethod
    def to_csv(df):
        return df.to_csv(index=False)