# from sqlalchemy import create_engine
import pymysql.cursors
import pandas as pd
import sqlalchemy
import pymysql
pymysql.install_as_MySQLdb()
df = pd.read_csv("aartiiiicsv.csv")
df = pd.DataFrame(df)
cnx = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost/test')
df.to_sql('data_table1', con=cnx)
cnx.close
