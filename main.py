import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import psycopg2
import plotly.graph_objs as go

from config import *
from utils import *

# connect to postgres
connect_postgres()

