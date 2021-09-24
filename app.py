import dash
import dash_core_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Img(src='/assets/logo.jpg', className="logo"),
    html.H1(children="CoGhent: Dashboard", className="app-header--title")
])

if __name__ == '__main__':
    app.run_server(debug=True)