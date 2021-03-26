import logging
import pandas as pd
from pandas.core.algorithms import mode
from snowflake.connector.network import EXTERNAL_BROWSER_AUTHENTICATOR
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
import snowflake.connector

format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt=datefmt)
logger = logging.getLogger('snowflake-dev')


# engine = create_engine(URL(
#     user='*****',
#     account='*****',
#     database='*****'
# ), connect_args={
#     'authenticator': 'externalbrowser'
# }
# )

ctx = snowflake.connector.connect(user='*****',
                                  account='*****',
                                  database='*****',
                                  authenticator='externalbrowser'
                                  )

cur = ctx.cursor()

sql = """SELECT * FROM TABLE;"""

cur.execute(sql)

header = True
for df in cur.fetch_pandas_batches():
    df.to_csv('file.csv', index=False, mode='a', header=header)
    header = False


