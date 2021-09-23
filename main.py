import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import psycopg2
import pandas.io.sql as sqlio

from config import *

#connect to db
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="co2etzee1648"
)

#define queries
sql_dmg = 'select * from postgres.public.ldes_dmg'
sql_hva = 'select * from postgres.public.ldes_hva'
sql_stam = 'select * from postgres.public.ldes_stam'
sql_im = 'select * from postgres.public.ldes_im'
sql_archief = 'select * from postgres.public.ldes_archief'
sql_agents = 'select * from postgres.public.ldes_agents'
sql_thes = 'select * from postgres.public.ldes_thes'
sql_all = 'select * from postgres.public.ldes_all'

df_dmg = sqlio.read_sql_query(sql_dmg, conn)
df_hva = sqlio.read_sql_query(sql_hva, conn)
df_stam = sqlio.read_sql_query(sql_stam, conn)
df_im= sqlio.read_sql_query(sql_im, conn)
df_archief = sqlio.read_sql_query(sql_archief, conn)
df_agents = sqlio.read_sql_query(sql_agents, conn)
df_thes = sqlio.read_sql_query(sql_thes, conn)
df_all = sqlio.read_sql_query(sql_all, conn)

